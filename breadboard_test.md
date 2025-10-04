# TL431 Shunt Regulator - Breadboard Assembly Guide
## 11.1V to 3.3V Step-Down Circuit

---

## Components Required

✅ **Active Components:**
- 1× TL431A voltage reference IC (TO-92 or SOT-23 package)

✅ **Passive Components:**
- 1× Fuse 3A (glass tube or automotive blade type)
- 1× Resistor 4.7kΩ (1/4W or better)
- 1× Potentiometer 10kΩ (trimmer or rotary)
- 1× Capacitor 680µF electrolytic (16V or higher rating)
- 1× Capacitor 22nF ceramic (50V rated)

✅ **Power:**
- 1× Battery 11.1V (3S LiPo with connector)

✅ **Tools:**
- Breadboard (at least 830 tie points)
- Jumper wires (22 AWG solid core) in various colors
- Multimeter (for voltage measurement)
- Wire strippers
- Small flathead screwdriver (for potentiometer adjustment)

---

## Understanding the Breadboard Layout

### Breadboard Basics
- **Rows A-E** and **F-J** are electrically connected horizontally (within each row)
- **Center gap** separates the top (A-E) and bottom (F-J) sections
- **Power rails** run vertically along the sides (+ and - rails)
- Columns are numbered 1-60 (or 1-63 depending on breadboard)

### Our Circuit Column Assignments
- **Column 11:** Fuse input
- **Column 16:** Fuse output / Resistor input
- **Column 21:** Resistor output / VOUT
- **Column 26:** Main VOUT distribution point
- **Column 36:** TL431 IC
- **Columns 41-46-51:** Potentiometer (3 pins)
- **Column 56:** 22nF compensation capacitor

---

## Step-by-Step Assembly

### ⚡ **STEP 1: Safety First**
1. **Disconnect the battery** - never wire a live circuit
2. Set your multimeter to DC voltage mode (0-20V range)
3. Keep the battery terminals insulated (tape over connectors)

---

### 📍 **STEP 2: Install Power Rails**

**Connect Battery to Breadboard Rails:**

1. **Battery Positive (+):**
   - Take a RED jumper wire
   - Connect one end to battery positive terminal (outside breadboard)
   - Connect other end to top **+ rail** (red stripe) at any point
   
2. **Battery Negative (-):**
   - Take a BLACK jumper wire
   - Connect one end to battery negative terminal
   - Connect other end to top **- rail** (blue stripe) at any point

3. **Bridge Top and Bottom GND Rails:**
   - Connect a BLACK jumper from top **- rail** to bottom **- rail**
   - This ensures ground is available on both sides

> **Result:** Both power rails are now live (but battery still disconnected)

---

### 🔌 **STEP 3: Install the Fuse**

**Position:** Column 11 to Column 16, Row C

1. Insert fuse lead 1 into **11C** (column 11, row C)
2. Insert fuse lead 2 into **16C**
3. Bend leads gently if needed to span the 5-column distance

**Connect Fuse Input to Power:**
4. Take a RED jumper wire
5. Connect from **+ rail** to **11C** (same row as fuse input)

> **Result:** Power flows from + rail → Fuse input

---

### 🎨 **STEP 4: Install the Series Resistor (4.7kΩ)**

**Position:** Column 16 to Column 26, Row C

1. **Identify resistor bands:**
   - Yellow-Violet-Red-Gold = 4.7kΩ ±5%
   
2. Insert resistor lead 1 into **16C** (shares column with fuse output)
3. Insert resistor lead 2 into **26C**
4. Bend to fit horizontal layout

**Connect Fuse to Resistor:**
5. They share column 16, row C - already connected!

> **Result:** Power flows: + rail → Fuse → Resistor → Column 26 (VOUT node)

---

### ⚡ **STEP 5: Mark the VOUT Node**

**Position:** Column 26, Row C and Row E

The regulated 3.3V output appears at **column 26**.

1. Place a small label or marker at column 26 (you'll measure here later)
2. This is your main **VOUT = 3.3V** distribution point

---

### 🔋 **STEP 6: Install the Output Capacitor (680µF)**

**Position:** Column 26, Row E to Row H (crosses center gap)

⚠️ **POLARITY CRITICAL:**
1. Identify the **negative stripe** on the capacitor body
2. Insert **POSITIVE lead** (longer leg) into **26E** (top section)
3. Insert **NEGATIVE lead** (shorter leg, marked side) into **26H** (bottom section)
4. The capacitor should straddle the center gap

**Connect Capacitor Negative to GND:**
5. Take a BLACK jumper wire
6. Connect from **26H** to bottom **- rail**

> **Result:** 680µF filters the output voltage between VOUT and GND

---

### 🔲 **STEP 7: Install the TL431 IC**

**Position:** Column 36, Rows C, F, H

**TL431 Pinout (TO-92 package, flat side facing you, pins down):**
- **Pin 1 (LEFT):** REF (reference input)
- **Pin 2 (MIDDLE):** Anode (A) - connects to GND
- **Pin 3 (RIGHT):** Cathode (K) - connects to VOUT

**Installation:**
1. Insert Pin 1 (REF) into **36C** (top section)
2. Insert Pin 2 (Anode) into **36F** (bottom section, crosses gap)
3. Insert Pin 3 (Cathode) into **36H** (bottom section)

**Connect TL431 Anode to GND:**
4. Take a BLACK jumper wire
5. Connect from **36F** to bottom **- rail**

**Connect TL431 Cathode to VOUT:**
6. Take an ORANGE jumper wire
7. Connect from **26E** to **36H**

> **Result:** TL431 now senses VOUT and can regulate by sinking current

---

### 🎛️ **STEP 8: Install the Potentiometer (10kΩ)**

**Position:** Columns 41, 46, 51 (Row D)

**Potentiometer Pinout:**
- **Pin 1:** One end of resistor → connects to VOUT
- **Pin 2 (CENTER):** Wiper/cursor → connects to TL431 REF
- **Pin 3:** Other end → connects to GND

**Installation:**
1. Insert Pin 1 into **41D**
2. Insert Pin 2 (wiper/center) into **46D**
3. Insert Pin 3 into **51D**
4. Ensure pot sits flat on breadboard

**Connect POT Pin 1 to VOUT:**
5. Take an ORANGE jumper wire
6. Connect from **26D** to **41D**

**Connect POT Wiper (Pin 2) to TL431 REF:**
7. Take a GREEN jumper wire
8. Connect from **46D** to **36C** (TL431 pin 1)

**Connect POT Pin 3 to GND:**
9. Take a BLACK jumper wire
10. Connect from **51D** to bottom **- rail**

> **Result:** Potentiometer forms voltage divider; wiper voltage goes to TL431 REF

---

### 🧩 **STEP 9: Install the Compensation Capacitor (22nF)**

**Position:** Column 56, Row C to Row G

1. Insert one lead into **56C** (top section)
2. Insert other lead into **56G** (bottom section)
3. Ceramic capacitors are non-polarized (either way works)

**Connect 22nF Top to VOUT:**
4. Take a YELLOW jumper wire
5. Connect from **56C** to **26C**

**Connect 22nF Bottom to REF:**
6. Take a GREEN jumper wire
7. Connect from **56G** to **46D** (shares with pot wiper)

> **Result:** 22nF stabilizes the feedback loop between VOUT and REF

---

## ✅ Pre-Power Checklist

Before connecting the battery, verify:

- [ ] **Fuse** is in series with positive power (11C to 16C)
- [ ] **4.7kΩ resistor** connects fuse to VOUT (16C to 26C)
- [ ] **680µF capacitor** positive to 26E, negative to GND (26H to - rail)
- [ ] **TL431 Pin 1** (REF) is at 36C
- [ ] **TL431 Pin 2** (Anode) is at 36F and connected to GND
- [ ] **TL431 Pin 3** (Cathode) is at 36H and connected to VOUT (via 26E)
- [ ] **POT Pin 1** at 41D connects to VOUT
- [ ] **POT Pin 2** (wiper) at 46D connects to TL431 REF (36C)
- [ ] **POT Pin 3** at 51D connects to GND
- [ ] **22nF capacitor** connects between VOUT (56C→26C) and REF (56G→46D)
- [ ] **All GND connections** go to bottom - rail
- [ ] **No short circuits** between + and - rails

---

## ⚡ Power-Up and Adjustment

### **STEP 10: Initial Power-Up**

1. **Set multimeter to DC voltage (20V range)**
2. Connect multimeter BLACK probe to GND (bottom - rail or 26H)
3. Connect multimeter RED probe to VOUT (column 26, row E or C)
4. **Double-check polarity** - red to VOUT, black to GND
5. **Connect battery** positive and negative terminals
6. **Observe multimeter reading**

**Expected Reading:** Between 2.0V and 5.0V (depends on pot position)

⚠️ **If you see:**
- **0V:** Check connections, fuse may be blown, or TL431 shorted
- **11.1V:** TL431 not regulating - check pin connections and polarity
- **Negative voltage:** Reverse multimeter probes

---

### **STEP 11: Adjust to 3.3V**

1. Locate the **adjustment screw** on the potentiometer
2. Using a small flathead screwdriver, **slowly turn clockwise or counter-clockwise**
3. Watch the multimeter display
4. **Target voltage: 3.30V ±0.05V**

**Adjustment Tips:**
- Turn **very slowly** - small movements change voltage significantly
- If voltage increases when turning clockwise, continue that direction
- If voltage decreases, reverse direction
- Once close to 3.30V, make tiny adjustments (1/16 turns)

**Final Target:** **3.30V** on the multimeter

---

### **STEP 12: Load Test (Optional)**

To verify regulation under load:

1. Connect a resistor (e.g., 330Ω) between VOUT and GND
   - This draws ~10mA load current
2. Voltage should remain at 3.30V ±0.05V
3. If voltage drops significantly, your load is too high for this design

⚠️ **Current Limit:** With 4.7kΩ series resistor, maximum load current is ~1.5mA

---

## 📊 Expected Results

| **Parameter** | **Value** |
|---------------|-----------|
| Input Voltage | 10.5V - 12.6V (3S LiPo range) |
| Output Voltage | 3.30V (adjustable 2.5V - 5V) |
| Output Ripple | <50mV (with 680µF cap) |
| Load Current | <1.5mA (limited by 4.7kΩ) |
| Regulation | ±50mV across input range |
| Quiescent Current | ~2mA (TL431 + divider) |

---

## 🛠️ Troubleshooting

### **Problem: No voltage at output (0V)**

**Possible Causes:**
1. ✅ Check fuse - may be blown
2. ✅ Verify battery voltage (should be >10V)
3. ✅ Check 4.7kΩ resistor - may be open circuit
4. ✅ TL431 may be damaged or inserted backwards

**Solutions:**
- Replace fuse if blown
- Check battery with multimeter
- Measure resistor with ohmmeter (should be ~4.7kΩ)
- Verify TL431 pinout (pin 1 = REF, pin 2 = A, pin 3 = K)

---

### **Problem: Output voltage equals input (11.1V)**

**Possible Causes:**
1. ✅ TL431 not regulating (REF pin not connected)
2. ✅ Potentiometer not connected properly
3. ✅ TL431 anode not grounded

**Solutions:**
- Verify GREEN wire from pot wiper (46D) to TL431 REF (36C)
- Check BLACK wire from TL431 anode (36F) to GND rail
- Ensure pot pin 3 (51D) is grounded

---

### **Problem: Cannot adjust voltage / stuck at one value**

**Possible Causes:**
1. ✅ Potentiometer broken or not making contact
2. ✅ Wiper pin not connected to REF
3. ✅ 22nF capacitor shorted

**Solutions:**
- Measure resistance across pot pins (should change when turning)
- Re-seat pot firmly into breadboard holes
- Check continuity from wiper to REF pin

---

### **Problem: Voltage unstable / oscillating**

**Possible Causes:**
1. ✅ Missing 22nF compensation capacitor
2. ✅ 680µF capacitor installed backwards
3. ✅ Poor breadboard contacts

**Solutions:**
- Verify 22nF between VOUT and REF
- Check 680µF polarity (+ to VOUT, - to GND)
- Re-insert components firmly; try different rows

---

### **Problem: Output voltage too low (<2.5V)**

**Possible Causes:**
1. ✅ Load current too high (>1.5mA)
2. ✅ Series resistor value too high
3. ✅ TL431 in current limit

**Solutions:**
- Remove load and measure again
- Verify 4.7kΩ resistor (color bands: Yellow-Violet-Red)
- Reduce load current or use smaller series resistor (WARNING: recalculate!)

---

## 🔍 Measurement Points

Use your multimeter to verify voltages at key points:

| **Point** | **Expected Voltage** | **Description** |
|-----------|---------------------|-----------------|
| Battery + | 10.5V - 12.6V | 3S LiPo voltage range |
| After Fuse | 10.5V - 12.6V | Same as battery (small drop) |
| After Resistor (VOUT) | 3.30V | Regulated output |
| TL431 REF (36C) | 2.495V | Internal reference |
| POT Wiper (46D) | 2.495V | Should match REF |
| TL431 Anode (36F) | 0V | Grounded |
| TL431 Cathode (36H) | 3.30V | Same as VOUT |
| 680µF Negative | 0V | Grounded |

---

## ⚠️ Important Safety Notes

1. **LiPo Battery Safety:**
   - Never discharge below 3.0V per cell (9.0V total)
   - Use a LiPo-safe charging bag
   - Disconnect when not in use
   - Monitor battery temperature

2. **Polarity:**
   - Double-check 680µF capacitor polarity (+ to VOUT)
   - Reverse polarity can cause explosion
   - Always verify with multimeter before applying power

3. **Current Limits:**
   - This circuit provides only ~1.5mA maximum
   - Do not connect high-current loads (e.g., motors, LEDs without resistor)
   - For higher currents, use a buck converter module

4. **First Power-Up:**
   - Always use a current-limited power supply for testing if possible
   - Have fuse rating appropriate for your circuit (3A protects battery)

---

## 📈 Next Steps / Improvements

Once your circuit works, consider:

1. **Increase Current Capability:**
   - Add a pass transistor (PNP or P-MOSFET) for 100mA+ loads
   - Replace 4.7kΩ with smaller value (e.g., 330Ω for ~20mA)

2. **Fixed Output (Remove Potentiometer):**
   - Calculate fixed resistor divider:
     - R1 (VOUT to REF) = 3.23kΩ (use 3.3kΩ)
     - R2 (REF to GND) = 10kΩ
   - Replace pot with these two resistors

3. **PCB Version:**
   - Design a permanent PCB for reliability
   - Add screw terminals for battery and output
   - Include power LED indicator

4. **Protection Features:**
   - Add reverse polarity protection (diode or P-MOSFET)
   - Include output short-circuit protection
   - Add low-battery voltage cutoff

---

## 📚 Additional Resources

- **TL431 Datasheet:** [Texas Instruments TI.com](https://www.ti.com/product/TL431)
- **LiPo Battery Safety Guide:** [Battery University](https://batteryuniversity.com)
- **Breadboard Tutorial:** [SparkFun Breadboard Guide](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

---

## ✅ Completion Checklist

Mark when complete:

- [ ] All components installed in correct positions
- [ ] All jumper wires connected per schematic
- [ ] Visual inspection for shorts or wrong connections
- [ ] Pre-power checklist verified
- [ ] Multimeter connected to VOUT and GND
- [ ] Battery connected with correct polarity
- [ ] Output voltage reads ~2-5V initially
- [ ] Potentiometer adjusted to exactly 3.30V
- [ ] Voltage remains stable for 5 minutes
- [ ] Load test passed (optional)
- [ ] Circuit documented with photo

---

## 📸 Document Your Build

Take photos at each step:
1. Empty breadboard with column/row markers
2. After each component installation
3. Complete wired circuit (top view)
4. Multimeter showing 3.30V output
5. Final working circuit with battery

---

**Congratulations! Your TL431 shunt regulator is now working! 🎉**

**Output:** Stable 3.3V from 11.1V LiPo battery  
**Regulation:** Maintains voltage across 10.5V - 12.6V input range  
**Efficiency:** Low (linear regulation - heat dissipated in series resistor)  
**Best Use:** Low-current applications like sensor power, microcontroller standby

---

*Created: 2025-10-04*  
*Circuit Type: Linear Shunt Regulator*  
*Target Output: 3.3V @ <1.5mA*

