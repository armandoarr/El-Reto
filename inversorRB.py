#!/usr/bin/env python

from __future__ import division 
from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt 
import colorsys

#matplotlib inline

imagen = Image.open("./cielo.jpg")
RGBarr = np.asarray(imagen)

#print imagen.size
#print imagen.size, imagen.mode, imagen.format

#imagengris = imagen.convert('L')

#print imagengris.mode

#imagengris.save('i-see-no-god-gris.tif')

xs, ys = imagen.size

newRGB = np.full_like(RGBarr, 1)

#newRGB = np.zeros((ys, xs, 3))


red = RGBarr[..., 0]
green = RGBarr[...,1]
blue = RGBarr[..., 2]

#newRGB[...] = (blue, green, red)
newRGB[..., 0] = blue 
newRGB[..., 1] = green
newRGB[..., 2] = red

nueva = Image.fromarray(newRGB, 'RGB')

nueva.save('nueva.png')

nueva.show() 

#print nueva.size

#print newRGB[..., 0]
#print RGBarr[..., 2]
