import pylab
import numpy as np


f = 50
fs = 100000
x = np.arange(65536)

phase = (x*2*np.pi*f/fs)%(2*np.pi)
sinus = np.sin(phase)


y = sinus
yf = np.fft.fft(y)      # fast fourier transform
freq = np.fft.fftfreq(y.shape[-1])

yf2 = np.fft.ifft(y)

pylab.subplot(311)
pylab.plot(x,y)
pylab.subplot(312)
pylab.plot(freq,yf.real, freq, yf.imag)
pylab.subplot(313)
pylab.plot(freq,yf2.real, freq, yf2.imag)
pylab.show()