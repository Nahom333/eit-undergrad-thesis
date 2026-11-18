# How EIT Works (Design Note 00)
**Author:** Nahom Zeray  
**Project:** Low-Cost 8-Electrode EIT System (AAU Senior Thesis)

---

### 1. Current Flow in the Saline Tank
* **Question:** Picture a round tank of salt water with 8 electrodes on the wall. I push a small current in at electrode 1 and out at electrode 2. Where does the current go?
* **My Answer:** Current enters at Electrode 1 and exits at Electrode 2. Because the saline solution is a continuous volume conductor, the current does not travel in a thin straight wire. Instead, it spreads out into curved streamlines throughout the entire volume of the tank. The current density is highest directly between electrodes 1 and 2, but a portion of the current diffuses deep into the center and the opposite boundaries.

---

### 2. Effect of a Non-Conductive Object
* **Question:** Now I put a plastic object in the tank. Plastic does not conduct. What happens to the current paths near it? What happens to the voltage I measure at the other electrodes?
* **My Answer:** Because plastic is an electrical insulator ($\sigma \approx 0$), current cannot pass through it. The electric current lines are forced to bend and divert around the outer perimeter of the object (taking the path of least resistance through the surrounding saline). This crowding of current around the object changes the internal electric field distribution, producing measurable voltage shifts at the sensing boundary electrodes—especially those closest to the object.

---

### 3. Need for Multiple Injection Pairs
* **Question:** Why do I need many injection pairs and not just one?
* **My Answer:** A single injection pair only illuminates the tank from one perspective, giving high sensitivity near that pair but very low sensitivity on the far side. By rotating the current injection through all 8 adjacent pairs around the circle, we interrogate the internal domain from multiple independent angular perspectives ($360^\circ$). This multi-angle data is mathematically necessary to triangulate and uniquely resolve the position and shape of internal anomalies.

---

### 4. Throwing Away Current-Carrying Electrodes (The 4-Electrode Principle)
* **Question:** Adjacent pattern, 8 electrodes: 8 injections, and for each injection 5 voltage readings (the pairs that do not include the two current electrodes), so 40 readings per frame. Why are the readings that touch a current electrode thrown away?
* **My Answer:** When current flows through an electrode, an unpredictable electrochemical contact impedance ($Z_c$) forms at the metal-electrolyte interface, causing a large, noisy voltage drop ($I \times Z_c$). If we measured voltage across those same electrodes, this contact noise would drown out the small internal signal. By measuring voltage with separate electrodes connected to ultra-high-input-impedance buffers (TL084), virtually zero current flows into the sensing wires ($I_{\text{sense}} \approx 0$), completely eliminating the contact impedance voltage drop ($V_{\text{drop}} \approx 0$).

---

### 5. Forward vs. Inverse Problem and Noise Amplification
* **Question:** Forward problem: given the conductivity inside, compute the voltages. Inverse problem: given the voltages, find the conductivity. Why is the second one hard and why does it make noise worse?
* **My Answer:** 
  * The **Forward Problem** is direct and stable: given the internal conductivity distribution, solving Laplace's equation ($\nabla \cdot (\sigma \nabla u) = 0$) gives one unique, exact set of boundary voltages.
  * The **Inverse Problem** is ill-posed and underdetermined: we only have 40 boundary voltage measurements trying to estimate hundreds of internal pixels. Deep inside the tank, current spreads out, so internal conductivity changes produce only microscopic voltage differences at the boundary. Inverting this mathematical system requires high gain, which dramatically magnifies tiny analog hardware noise into large image artifacts.

---

### 6. Why EIT Images Are Blurry
* **Question:** Why are the images blurry?
* **My Answer:** Unlike CT scans or X-rays where photons travel in straight, razor-sharp lines, electrical current in a conductive fluid naturally diffuses and spreads out in all directions. Because current paths are smooth and continuous throughout the medium, sharp physical boundaries get smoothed out in the reconstructed conductivity map, resulting in inherently soft-focus images.
