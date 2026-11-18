# How EIT Works (Design Note 00)
**Author:** Nahom Zeray  
**Project:** Low-Cost 8-Electrode EIT System (AAU Senior Thesis)

---

### 1. Current Flow in the Saline Tank
* **Question:** Picture a round tank of salt water with 8 electrodes on the wall. I push a small current in at electrode 1 and out at electrode 2. Where does the current go?
* **My Answer:** Current enters at Electrode 1 and exits at Electrode 2. Because the saline solution is a continuous volume conductor, current does not flow in a straight line. Instead, it spreads out through the water. For adjacent electrodes, most of the current stays near the tank wall between 1 and 2, while only a small portion reaches the center and the opposite boundary.

---

### 2. Effect of a Non-Conductive Object
* **Question:** Now I put a plastic object in the tank. Plastic does not conduct. What happens to the current paths near it? What happens to the voltage I measure at the other electrodes?
* **My Answer:** Because plastic does not conduct electricity ($\sigma \approx 0$), current cannot pass through it. The current lines spread over all available paths and squeeze around the outer surface of the object. This crowding of current around the object alters the electric field inside the tank, which produces measurable voltage changes at the sensing electrodes on the boundary—especially those closest to the object.

---

### 3. Need for Multiple Injection Pairs
* **Question:** Why do I need many injection pairs and not just one?
* **My Answer:** A single injection pair only illuminates the tank from one direction, providing good sensitivity near that pair but very little information elsewhere. Rotating the injection through all 8 adjacent pairs around the tank interrogates the interior from multiple angles. This provides more independent data to estimate the location and size of internal objects, although with only 8 electrodes the answer is never completely unique.

---

### 4. Throwing Away Current-Carrying Electrodes
* **Question:** Adjacent pattern, 8 electrodes: 8 injections, and for each injection 5 voltage readings (the pairs that do not include the two current electrodes), so 40 readings per frame. Why are the readings that touch a current electrode thrown away?
* **My Answer:** At the two electrodes carrying current, the 1 mA injection current creates a large, unpredictable voltage drop across the metal-to-water contact impedance ($I \times Z_c$). This contact drop is much larger than the actual signal from the water, so we discard any reading that touches a current-carrying electrode. 
  
  *(Note on buffers:* The high-impedance buffers solve a different problem: on the quiet electrodes being sensed, almost zero current flows into the buffer, so there is no significant $I \times Z_c$ drop on the sensing side.)

---

### 5. Forward vs. Inverse Problem and Noise
* **Question:** Forward problem: given the conductivity inside, compute the voltages. Inverse problem: given the voltages, find the conductivity. Why is the second one hard and why does it make noise worse?
* **My Answer:** 
  * The **Forward Problem** is direct: given the conductivity inside, solving Laplace's equation gives one exact, unique set of boundary voltages.
  * The **Inverse Problem** is hard because we only collect 40 boundary measurements—and due to reciprocity (swapping injection and sensing pairs gives the same voltage), only 20 of these measurements are truly independent. We are trying to estimate hundreds of internal pixels from just 20 independent numbers. Furthermore, because current diffuses smoothly, changes deep in the center create only tiny voltage changes at the boundary. Many different internal arrangements produce almost identical boundary voltages. The solver cannot distinguish real tiny signals from noise, so it must be regularized (instructed to favor smooth solutions). Inverting this system magnifies tiny analog circuit noise into large image artifacts.
  * *(Practical value:* Because reciprocal pairs should theoretically match, measuring the difference between reciprocal readings provides a built-in check of our hardware quality.)

---

### 6. Why EIT Images Are Blurry
* **Question:** Why are the images blurry?
* **My Answer:** The blur comes from two sources:
  1. **The physics:** Electrical current diffuses and spreads out smoothly through conductive water rather than traveling in straight lines like an X-ray beam, losing fine edge details.
  2. **The software:** Because the inverse problem is sensitive to noise, reconstruction software deliberately applies smoothing (regularization) to prevent noise from turning into fake color artifacts. 
  Blur and noise trade against each other, which is why keeping analog hardware noise low is critical to image quality.
