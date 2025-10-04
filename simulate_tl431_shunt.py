"""
PySpice simulation for a basic 3.3 V TL431 shunt regulator using only the provided parts:

- 11.1 V LiPo battery (modeled as an ideal DC source, swept 10.5→12.6 V)
- 3 A fuse (modeled as a very small series resistance)
- 4.7 kΩ resistor (series from battery to output)
- TL431A (simplified behavioral macromodel inside this netlist)
- 10 kΩ potentiometer (modeled as two resistors whose sum = 10 kΩ)
- 22 nF capacitor (from cathode/Vout to REF for stability)
- 680 µF capacitor (output bulk capacitor from Vout to GND)

Notes:
- This is a simple shunt topology. With a 4.7 kΩ series resistor and ~11 V in, the available load current at 3.3 V is very small (≈1–2 mA total through the series resistor, minus TL431 minimum current). The circuit is suitable for very light loads.
- The TL431 is modeled behaviorally to avoid external model files. It regulates by sinking current from K (cathode) to A (anode) when V(REF,A) > 2.495 V.
- The potentiometer is represented as two resistors, R_top and R_bot, that sum to 10 kΩ. Their ratio is chosen to target ~3.3 V.
"""

from __future__ import annotations

import math
from typing import Tuple, List

from PySpice.Logging.Logging import setup_logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *


def compute_pot_split_for_target_vout(
    v_out_target: float,
    r_total_ohm: float = 10_000.0,
    v_ref: float = 2.495,
) -> Tuple[float, float]:
    """
    Compute the equivalent split of a 10 kΩ potentiometer into R_top (Vout→REF) and
    R_bot (REF→GND) so that a TL431 sees V_ref at REF when Vout = v_out_target.

    Relationship: Vout = Vref * (1 + R_top / R_bot).
    Given R_top + R_bot = r_total_ohm, solve for R_top and R_bot.
    """
    if v_out_target <= 0.0:
        raise ValueError("v_out_target must be positive")
    ratio = (v_out_target / v_ref) - 1.0
    if ratio <= 0.0:
        raise ValueError("Requested Vout is below Vref; increase v_out_target.")
    r_top = r_total_ohm * (ratio / (1.0 + ratio))
    r_bot = r_total_ohm - r_top
    return r_top, r_bot


def build_circuit(v_bat_volts: float = 11.1, fuse_resistance_ohm: float = 0.01):
    """
    Construct the TL431 shunt regulator circuit using only the provided components.
    """
    circuit = Circuit("TL431 3.3V Shunt")

    # Battery (LiPo 3S nominal ~11.1 V, we will also sweep it later)
    vbat = circuit.V("BAT", "VBAT", circuit.gnd, v_bat_volts @ u_V)

    # Fuse (3 A rated) modeled as a very small series resistance
    circuit.R("FUSE", "VBAT", "VIN", fuse_resistance_ohm @ u_Ohm)

    # 4.7 kΩ series resistor from VIN to VOUT
    circuit.R("SER", "VIN", "VOUT", 4.7 @ u_kOhm)

    # Output bulk capacitor 680 µF from VOUT to GND
    circuit.C("OUT", "VOUT", circuit.gnd, 680 @ u_uF)

    # Potentiometer 10 kΩ between VOUT and GND, wiper to REF
    # Target 3.3 V output with 2.495 V reference
    r_top, r_bot = compute_pot_split_for_target_vout(3.3, 10_000.0, 2.495)
    circuit.R("POTTOP", "VOUT", "REF", r_top @ u_Ohm)
    circuit.R("POTBOT", "REF", circuit.gnd, r_bot @ u_Ohm)
    
    # TL431 compensation capacitor 22 nF from VOUT to REF
    circuit.C("COMP", "VOUT", "REF", 22 @ u_nF)

    # ---------------------------------------------------------------------
    # TL431A simplified behavioral model:
    # Acts as a current sink from VOUT to GND when V(REF) > 2.495 V
    # The TL431 tries to keep REF at 2.495 V by sinking current from cathode
    # ---------------------------------------------------------------------
    # High-gain error amplifier: sense error at REF
    # If V(REF) > 2.495V, increase gate drive
    circuit.BehavioralSource('ERRAMP', 'GATE', circuit.gnd, 
                            v='1000*(V(REF) - 2.495)')
    
    # Limit the gate voltage
    circuit.R('GATE_LIM', 'GATE', 'GATE_LIM', 1 @ u_Ohm)
    circuit.D('GATE_CLIP_LO', circuit.gnd, 'GATE_LIM', model='DCLIP')
    circuit.D('GATE_CLIP_HI', 'GATE_LIM', 'VOUT', model='DCLIP')
    circuit.model('DCLIP', 'D', Is=1e-14, n=1.0)
    
    # Current sink controlled by gate (VCCS)
    # When GATE is high (REF > 2.495V), sink current from VOUT to GND
    circuit.BehavioralSource('TL431_SINK', 'VOUT', circuit.gnd,
                            i='LIMIT(0.01*V(GATE_LIM), 0, 0.1)')
    
    # REF input impedance (high)
    circuit.R('REF_IN', 'REF', circuit.gnd, 1 @ u_MOhm)

    return circuit, vbat


def run_nominal_op(circuit: Circuit) -> float:
    """
    Run an operating point at the circuit's current VBAT value.
    Returns the Vout (float, volts).
    """
    simulator = circuit.simulator(temperature=25.0, nominal_temperature=25.0)
    analysis = simulator.operating_point()
    # ngspice converts node names to lowercase
    vout_node = analysis.nodes["vout"]
    vout_volts = float(vout_node)
    return vout_volts


def run_line_sweep(
    circuit: Circuit,
    v_source,
    vbat_values: List[float],
) -> List[Tuple[float, float]]:
    """
    Sweep VBAT over the provided list of voltages, returning [(VBAT, VOUT), ...].
    """
    results: List[Tuple[float, float]] = []
    simulator = circuit.simulator(temperature=25.0, nominal_temperature=25.0)

    for vb in vbat_values:
        v_source.dc_value = vb @ u_V
        analysis = simulator.operating_point()
        # ngspice converts node names to lowercase
        vout_volts = float(analysis.nodes["vout"])
        results.append((vb, vout_volts))

    return results


def main() -> None:
    setup_logging()

    # Build circuit at nominal 11.1 V (will sweep later too)
    circuit, vbat = build_circuit(v_bat_volts=11.1, fuse_resistance_ohm=0.01)

    # Nominal operating point
    vout_nom = run_nominal_op(circuit)
    print(f"Nominal OP @ VBAT=11.10 V -> VOUT={vout_nom:.4f} V")

    # Line sweep (no load), from 10.5 V (near empty 3S) to 12.6 V (full 3S)
    sweep_points = [round(v, 2) for v in [10.5 + 0.3 * i for i in range(int((12.6-10.5)/0.3) + 1)]]
    sweep_results = run_line_sweep(circuit, vbat, sweep_points)

    print("\nLine sweep (no load):")
    for vb, vo in sweep_results:
        print(f"  VBAT={vb:>4.1f} V -> VOUT={vo:.4f} V")

    # Quick sanity hint about current budget with 4.7 kΩ series resistor
    # (only informative text, not used in the simulation itself)
    vb_nom = 11.1
    i_series_nom = (vb_nom - 3.3) / 4700.0
    print(f"\nInfo: Series current at 11.1 V ≈ {i_series_nom*1e3:.2f} mA (available for TL431 + load)")


if __name__ == "__main__":
    main()


