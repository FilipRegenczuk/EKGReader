import numpy as np
import matplotlib.pyplot as plt

f = 50
l = 65536
# Number of samplepoints
N = int(l/f)
# sample spacing
T = 1.0 / 8000.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + np.sin(60.0 * 2.0*np.pi*x)
yf = np.fft.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

plt.subplot(211)
plt.grid(True)
plt.plot(x, y)

plt.subplot(212)
plt.grid(True)
plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
# fig, ax = plt.subplots()
# ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))

plt.show()