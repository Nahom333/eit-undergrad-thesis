# How EIT Works (Design Note 00)
Nahom Zeray  

---

### 1. Current Flow in the Saline Tank

Current enters at Electrode 1 and exits at Electrode 2. Because the saline solution is a continuous conductor, current does not flow in a straight line. Instead, it spreads out through the water. For the adjacent electrodes, most of the current stays near the tank wall between 1 and 2, while only a small portion reaches the center and the opposite boundary.

---

### 2. Effect of a Non-Conductive Object

Because plastic does not conduct electricity, current cannot pass through it. The current lines spread over all available paths and squeeze around the outer surface of the object. This alters the electric field inside the tank, which produces measurable voltage changes at the sensing electrodes on the boundary, especially those closest to the object.

---

### 3. Need for Multiple Injection Pairs

A single injection pair only illuminates the tank from one direction, providing good sensitivity near that pair but very little information elsewhere. Rotating the injection through all 8 adjacent pairs around the tank shows the interior from multiple angles. This provides more independent data to estimate the location and size of internal objects.

---

### 4. Throwing Away Current-Carrying Electrodes

At the two electrodes carrying current, the 1 mA injection current creates a large, unpredictable voltage drop across the metal due to contact impedance. This contact drop is much larger than the actual signal from the water, so we discard any reading that touches a current-carrying electrode.

The high-impedance buffers work on the quiet electrodes being sensed, almost zero current flows into the buffer, so there is no significant drop on the sensing side.

---

### 5. Forward vs. Inverse Problem and Noise

* The **Forward Problem** is easy: if what is inside the tank is known, voltages at the electrodes can be calculated.

* The **Inverse Problem** is hard: we only have the voltages, and many different things inside the tank give almost the same voltages. Because we only collect 40 boundary measurements, and due to reciprocity, only 20 of these measurements are truly independent. We are trying to estimate hundreds of internal pixels from just 20 independent numbers. Also, because current diffuses smoothly, changes deep in the center create only tiny voltage changes at the boundary. Many different internal arrangements produce almost identical boundary voltages. The solver cannot distinguish real tiny signals from noise, so it must be regularized (instructed to favor smooth solutions).

---

### 6. Why EIT Images Are Blurry

The blur comes from two sources:
1. Electrical current diffuses and spreads out smoothly through conductive water rather than traveling in straight lines like an X-ray beam, losing fine edge details.
2. Because the inverse problem is sensitive to noise, reconstruction software deliberately applies smoothing to prevent noise from turning into fake color artifacts. 

Blur and noise trade against each other, which is why keeping analog hardware noise low is critical to image quality.
