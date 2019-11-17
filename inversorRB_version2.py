#!/usr/bin/env python

from __future__ import division 
from PIL import Image 
import numpy as np 
import os


path = str(raw_input("En donde se encuentra la imagen? "))
nombre = str(raw_input("Como se llama el archivo? "))
#nuevo_nombre = str(raw_input("Nombre de la imagen nueva:"))

imagen = Image.open(os.path.join(path, nombre))
RGB = np.asarray(imagen)


#newRGB = np.full_like(RGB, 1)

BGR = RGB[...,::-1]

#red = RGB[..., 0]
#green = RGB[...,1]
#blue = RGB[..., 2]


#newRGB[..., 0] = blue 
#newRGB[..., 1] = green
#newRGB[..., 2] = red

nueva = Image.fromarray(BGR, 'RGB')

nueva.save('new.png')

nueva.show() 

#print nueva.size

#print newRGB[..., 0]
#print RGBarr[..., 2]
