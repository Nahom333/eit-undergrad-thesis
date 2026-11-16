# Open questions (decide these before building)

These are things the proposal does not fix. For each one write your current answer and why.
Do not leave them blank for long: several of them change which parts you buy.

| # | Question | My answer (TODO) | Why / what I based it on | Date decided |
|---|---|---|---|---|
| 1 | Drive frequency (what Hz do I inject at?) | | Think about: electrode-water contact, CD4051 and op-amp bandwidth, how fast the STM32 ADC can sample | |
| 2 | Current amplitude (peak, in mA or uA) | | Think about: voltage swing at the electrodes, Howland source supply rails, signal vs noise | |
| 3 | Supply rails for the analog part (single or dual?) | | The TL071, TL084 and NE5532 want dual rails; the STM32 ADC wants 0 to 3.3 V. How do I connect the two worlds? | |
| 4 | The noise limit for the "Noise within the limit?" decision | | The flow chart branches on this. Write the number BEFORE you measure, or you will be tempted to pick it afterwards | |
| 5 | Tank diameter and water depth | | | |
| 6 | Electrode material and size | | Stainless steel is common. What will you have access to? | |
| 7 | Salt concentration / water conductivity | | Measure it with something, do not guess | |
| 8 | Plastic object sizes and the positions you will test | | Positions must be measurable with a ruler (specific objective 3) | |
| 9 | How many frames per test position, and at what frame rate | | More frames = better noise statistics | |
| 10 | Which fault levels to test (open circuit, and which stepped contact impedances) | | Specific objective 4 says "disconnect or degrade". Pick the resistor values in advance | |
| 11 | Hand-etched board or JLCPCB, and who decides | | Decision point at the end of week 5 | |
| 12 | Which GREIT metrics exactly (position error, resolution, shape deformation, ringing, amplitude response) | | Your proposal names position error. Decide whether to report the others | |

Reference to check: the reference list in the proposal still has incomplete entries (items 4, 5, 7, 8 lack authors/years or volume numbers). Fix before the final report.
