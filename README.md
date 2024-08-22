# HBB-colorful
A simple micropython program on HBB (RP2040 + neopixel LED strip).

# hardware
- [HBB](https://github.com/bigtreetech/HBB/)
- GPIO pinout can be found in the above link too.
  - GPIO20 to control the neopixel

# Installation
- Upload the micropython binary file to the board. See [instructions](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
- Install the mpremote tool on the host OS.
- `mpremote a0 cp neopixel.py :/`
- `mpremote a0 cp main.py :/`
- Reboot HBB.
- Done :D

# References
This little program uses this awesome library [pi_pico_neopixel](https://github.com/blaz-r/pi_pico_neopixel).
