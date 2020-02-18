from scipy import signal
import matplotlib.pyplot as plt
s1 = signal.lti([1], [1, 3 ,2]) #Transfer Function = 1/(s^2+3s+2)
w, mag, phase = signal.bode(s1)
plt.figure()
plt.semilogx(w, mag)    #magnitude plot
plt.grid()
plt.figure()

plt.semilogx(w, phase)  #phase plot
plt.grid()
plt.show()
