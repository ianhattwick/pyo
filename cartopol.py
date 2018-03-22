"""Pyo CarToPol example
Ian Hattwick
March 13, 2018

Uses the Pyo Python module for audio signal processing. 
http://ajaxsoundstudio.com/software/pyo/

Uses the Fast Fourier transform classes: 
FFT to convert to frequency domain
IFFT to convert back to time domain.
CarToPol and PolToCar to translate between cartesian and polar coordinates
http://ajaxsoundstudio.com/pyodoc/api/classes/fourier.html

"""

from pyo import *
import random

s = Server().boot()

#load input audio file
path = sys.path[0] #retrieve the path to the directory the script is located in
path = path + "/AuthBulgarian3.wav" #any audio file in the same directory is ok
snd = SfPlayer(path, speed = [1.], loop = True, mul=1)

#FFT
fftSize = 4096
numOverlaps = 16
window = 2

fin = FFT(snd, size=fftSize, overlaps=numOverlaps, wintype=window)
re = fin["real"]
im = fin["imag"]

pol = CarToPol(re, im)

# create a data table to scale amplitudes
t = DataTable(size = fftSize/4)
t.graph()
amp = TableIndex(t, fin["bin"])

#scale the amplitude of the bins using our table
mag = pol["mag"] * amp
pha = pol["ang"] 

car = PolToCar(mag, pha)
fout = IFFT(car["real"], car["imag"], size=fftSize, overlaps=numOverlaps, wintype=window).mix(2).out()
s.start()
s.gui()