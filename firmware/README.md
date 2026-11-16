# Firmware (STM32)

Job of the firmware: generate the drive signal, set both multiplexers, wait for settling, sample the ADC, send frames to the laptop.

## Fill in
- Board and chip used: TODO
- Toolchain (STM32CubeIDE, PlatformIO, ...): TODO
- Pin map: firmware/docs/pin_map.md
- Frame format: firmware/docs/frame_format.md

## Suggested order to write it
1. Blink an LED and print over USB.
2. Output a sine from the DAC and check it on the scope.
3. Sample the ADC and send raw samples to the laptop.
4. Add multiplexer control (one pair, then the full sequence).
5. Add the full frame (8 injections x 5 readings).
