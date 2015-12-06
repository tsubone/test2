#!/usr/bin/env python

from PIL import Image
import time

im = Image.open ("Lenna.png")
#im2 = Image.new ("RGBA", (512,512), (255,0,0)).rotate(45).show ()
im2 = Image.new ("RGBA", (512,512), (255,0,0,0x7f))
#im.show ()

print im2

#im.copy().show ()

#time.sleep(5)
