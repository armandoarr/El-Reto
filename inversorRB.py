#!/usr/bin/env python

from __future__ import division 
from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt 
import colorsys

#matplotlib inline

imagen = Image.open("./i-see-no-god.png")
RGBarr = np.asarray(imagen)
#imagen.show()
print imagen.size

#print imagen.size, imagen.mode, imagen.format

#imagengris = imagen.convert('L')

#print imagengris.mode

#imagengris.save('i-see-no-god-gris.tif')

xs, ys = imagen.size

newRGB = np.tile(1, (ys, xs, 3))


red = RGBarr[..., 0]
blue = RGBarr[..., 2]
green = RGBarr[...,1]

newRGB[..., 0] = blue 
newRGB[..., 2] = red
newRGB[..., 1] = green

nueva = Image.fromarray(newRGB, 'RGB')

nueva.save('nueva.png')

nueva.show() 

print nueva.size

