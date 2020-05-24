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
fft = np.fft.fft(y)
ifft = np.fft.ifft(fft)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

pylab.subplot(411)
pylab.title("Fala sinusoidalna")
pylab.xlabel("Time [ms]")
pylab.ylabel("Amplitude")
pylab.grid(True)
pylab.plot(x, y)

pylab.subplot(412)
pylab.title("Transformata Fouriera")
pylab.xlabel("Frequency [Hz]")
pylab.ylabel("Amplitude")
pylab.grid(True)
pylab.plot(xf, 2.0/N * np.abs(fft[0:N//2]))

pylab.subplot(413)
pylab.title("Odwrotna transformata Fouriera")
pylab.xlabel("Time [ms]")
pylab.ylabel("Amplitude")
pylab.grid(True)
pylab.plot(x, ifft)

pylab.subplot(414)
pylab.title("Porównanie sygnałów")
pylab.xlabel("Time [ms]")
pylab.ylabel("Amplitude")
pylab.grid(True)
pylab.plot(x, y, 'b', x, ifft, 'r')

pylab.show()