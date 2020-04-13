import pylab
import numpy as np


f = 50
fs = 1000000
x = np.arange(65536)

phase = (x*2*np.pi*f/fs)%(2*np.pi)
sinus = np.sin(faza)

y = sinus

pylab.plot(x,y)
pylab.show()