import numpy as np
import pylab
from scipy import signal

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

sos = signal.butter(f1,f2, 'highpass',fs=8000, output='sos')
filtered = signal.sosfilt(sos, y)


pylab.subplot(211)
pylab.title("Fala sinusoidalna")
pylab.xlabel("Time [ms]")
pylab.ylabel("Amplitude")
pylab.grid(True)
pylab.plot(x, y)

pylab.subplot(212)
pylab.title("Po filtracji")
pylab.xlabel("Time [ms]")
pylab.ylabel("Amplitude")
pylab.grid(True)
pylab.plot(x, filtered)



pylab.show()