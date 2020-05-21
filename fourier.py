import pylab
import numpy as np


f = 50
fs = 100000
x = np.arange(65536)

phase = (x*2*np.pi*f/fs)%(2*np.pi)
sinus = np.sin(phase)


y = sinus
yf = np.fft.fft(y)      # fast fourier transform
yf2 = np.fft.ifft(y)    # odwrotna transformata
freq = np.fft.fftfreq(y.shape[-1])

# sinus
pylab.subplot(311)
pylab.grid(True)
pylab.plot(x,y)

# fourier
pylab.subplot(312)
pylab.plot(freq,yf.real, freq, yf.imag)

# odwrotny fourier
# pylab.subplot(313)
# pylab.plot(freq,yf2.real, freq, yf2.imag)


pylab.show()