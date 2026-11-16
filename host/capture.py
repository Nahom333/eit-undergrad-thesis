"""Read frames from the STM32 over USB serial and save them. Skeleton: fill in the TODOs."""
import time
import numpy as np
import serial  # pip install pyserial

PORT = "COM3"        # TODO: your port
BAUD = 115200        # TODO: match firmware (ignored for native USB CDC)
N_FRAMES = 100       # TODO
OUT = "data/raw/test_name.npy"   # TODO: follow data/README.md naming

def read_frame(ser):
    """TODO: parse one frame following firmware/docs/frame_format.md.
    Return an array of 40 values (8 injections x 5 readings)."""
    raise NotImplementedError

def main():
    frames = []
    with serial.Serial(PORT, BAUD, timeout=2) as ser:
        for i in range(N_FRAMES):
            frames.append(read_frame(ser))
            print(i, end="\r")
    np.save(OUT, np.array(frames))
    print("saved", OUT)

if __name__ == "__main__":
    main()
