from neopixel import Neopixel
from machine import Pin
from random import randint

pin_nrs = [25, 26, 18, 19, 27, 13, 12]
pins = [Pin(i, Pin.IN) for i in pin_nrs]
pin_indices = {
    str(p): i
    for i, p in enumerate(pins)
}

pixels = Neopixel(7, 0, 20, "RGB")

pixels.fill((60, 60, 60))
pixels.show()

def random_color(pin):
    ind = pin_indices[str(pin)]
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    pixels.set_pixel(ind, (g, r, b))
    pixels.show()

for p in pins:
    p.irq(random_color, Pin.IRQ_FALLING)
