"""Pyo Spectrum Analyzer example
Ian Hattwick
March 13, 2018

Uses the Pyo Python module for audio signal processing. 
http://ajaxsoundstudio.com/software/pyo/

Spectrum is one of Pyo's audio signal analysis classes. Documentation here:
http://ajaxsoundstudio.com/pyodoc/api/classes/analysis.html


"""
from pyo import *
s = Server().boot()
s.start()


path = sys.path[0] #retrieve the path to the directory the script is located in
path = path + "/AuthBulgarian3.wav" #any audio file in the same directory is ok

sf = SfPlayer(path, speed = [1.], loop = True, mul=1)
spec = Spectrum(sf,size = 1024)
s.gui(locals)