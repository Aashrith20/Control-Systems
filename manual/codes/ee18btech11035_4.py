import numpy as np
import matplotlib.pyplot as plt 

t=np.linspace(-3,25,1000)
y1=(1-np.exp(-t)*(np.cosh(t/(np.sqrt(2)))+np.sqrt(2)*np.sinh(t/(np.sqrt(2)))))*np.heaviside(t,1)
plt.plot(t,y1,label='$k=0.5(overdamped)$')
y2=(1-np.exp(-t)*(np.cos(t)+np.sin(t)))*np.heaviside(t,1)
plt.plot(t,y2,label='$k=2(under damped)$')

y3=(1-np.exp(-t)-t*np.exp(-t))*np.heaviside(t,1)
plt.plot(t,y3,label='$k=1(Critical Damped)$')
plt.grid()
plt.xlabel('time(sec)')
plt.ylabel('step response y(t)')
plt.legend()
plt.show()
