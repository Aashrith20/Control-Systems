# License
'''
Code by Aashrith
May 19th,2020
Released under GNU GPL
'''

from scipy import signal
import matplotlib.pyplot as plt
from pylab import*

s1 = signal.lti([2*np.pi*(10**6)],[1,2*np.pi*10])

w,mag,phase = signal.bode(s1)

subplot(2,1,1)
plt.ylabel('20log|G(s)|')
plt.title('Magnitude plot')
plt.semilogx(w, mag)        # Bode Magnitude plot
plt.semilogx(w,97*np.ones(len(w))) 
plt.annotate("A(62.8,97)",(62.8,97))
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.title('Phase plot')
plt.semilogx(w,phase)          # Bode phase plot
plt.grid() 

plt.show()
