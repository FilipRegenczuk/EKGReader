import numpy as np
import pylab

# Frequency 1
f1 = 50
# Frequency 2
f2 = 60
# Signal length
l = 65536
# Number of samplepoints
N = int(l/f1)
# sample spacing
T = 1.0 / 8000.0

x = np.linspace(0.0, N*T, N)
y = np.sin(f1 * 2.0*np.pi*x) + np.sin(f2 * 2.0*np.pi*x)
yfft = np.fft.fft(y)
yifft = np.fft.ifft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

pylab.subplot(311)
pylab.title("Fala łączone")
pylab.xlabel("Time [ms]")
pylab.ylabel("Amplitude")
pylab.grid(True)
pylab.plot(x, y)

pylab.subplot(312)
pylab.title("Transformata Fouriera")
pylab.xlabel("Frequency [Hz]")
pylab.ylabel("Amplitude")
pylab.grid(True)
pylab.plot(xf, 2.0/N * np.abs(yfft[:N//2]))

pylab.subplot(313)
pylab.title("Odwrotna transformata Fouriera")
pylab.xlabel("Frequency [Hz]")
pylab.ylabel("Amplitude")
pylab.grid(True)
pylab.plot(xf, 2.0/N * np.abs(yifft[:N//2]))


pylab.show()