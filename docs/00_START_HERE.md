# Start here

This file tells you the order to work in. The order follows the flow chart and work plan in your proposal.
Fill things in as you learn them. Do not try to fill everything on day one.

## Step 0 (before any hardware): answer the open questions
Open docs/open_questions.md. The proposal does not give numbers for these, and you need them before you buy or build.
Write down your best guess and the reason. You can change it later, and when you do, log it in docs/decision_log.md.

## Step 1: learn the one idea the whole project rests on
Read hardware/design_notes/00_how_eit_works.md and write the answers in your own words.
Go slowly. Ask yourself: if I push current in at electrodes 1 and 2, why does a voltage show up at electrodes 4 and 5?

## Step 2: follow the work plan (16 weeks in the proposal)
| Weeks | Work | Folder to use | Test to run |
|---|---|---|---|
| 1-3 | Order parts, build ONE measurement channel, first noise test | hardware/design_notes/04, tests/01 | tests/01_noise_resistor_ring.md |
| 4-5 | Current source + measurement chain, checked on resistors. Decision: hand-etch or JLCPCB | hardware/design_notes/01, 02, 03 | tests/01 again |
| 6-7 | Multiplexers and the eight-electrode board | hardware/design_notes/03, hardware/pcb | tests/01 on the full board |
| 8-9 | Firmware, USB link, EIDORS pipeline, first images | firmware/, host/, eidors/ | first image of an empty tank |
| 10-11 | Known-object tests, noise and accuracy results | tests/02, analysis/ | tests/02_known_object.md |
| 12 | Faulty-electrode test | tests/03, analysis/ | tests/03_faulty_electrode.md |
| 13-14 | Fixes, documentation, cost table | hardware/bom, docs/report | - |
| 15-16 | Final report and presentation | docs/report | - |

Your proposal says about 7 months are available, so you have slack. Use it for the things that always take longer than planned (the current source and the first EIDORS images).

## Step 3: every week
1. Add a file in docs/logbook/ (copy TEMPLATE.md). Ten minutes is enough.
2. Commit and push (see docs/github_howto.md).
3. Update the Status line in README.md.

## Rule of thumb
If a result is not written down with the date, the settings and the file it came from, it does not count. The report is built from the logbook, so a good logbook means an easy report.
