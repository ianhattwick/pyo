"""Pyo FFT example
Ian Hattwick
March 13, 2018

Uses the Pyo Python module for audio signal processing. 
http://ajaxsoundstudio.com/software/pyo/

Uses the Fast Fourier transform classes: 
FFT to convert to frequency domain
IFFT to convert back to time domain.
http://ajaxsoundstudio.com/pyodoc/api/classes/fourier.html

"""
from pyo import *
s = Server().boot()
s.start()

path = sys.path[0] #retrieve the path to the directory the script is located in
path = path + "/AuthBulgarian3.wav" #any audio file in the same directory is ok

#set a sound source for FFT input
#snd = Noise(.25).mix(2)
snd = SfPlayer(path, speed = [1.], loop = True, mul=1)

#set FFT parameters Try 512, 1024, 2048, 4096 FFT sizes
#sample window types (from documentation): 0 none; 1 hamming; 2 hanning; 4 blackman
fftSize = 8
numOverlaps = 8
window = 4

#perform the FFT and IFFT
fin = FFT(snd, size=fftSize, overlaps=numOverlaps, wintype=window)
re = fin["real"]
im = fin["imag"]
fout = IFFT(re, im, size=fftSize, overlaps=numOverlaps, wintype=window).mix(2).out()

#open the pyo gui to start/stop audio
s.gui()