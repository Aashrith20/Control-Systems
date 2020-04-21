import numpy as np
import matplotlib.pyplot as plt 

t=np.linspace(-3,15,1000)
y1=(1-np.exp(-t)-t*np.exp(-t))*np.heaviside(t,1)
plt.plot(t,y1,label='$y(t)=(1-e^{t}-te^{t})u(t)$')


x2=np.linspace(-3,5.834,1000)
y2=0.98*np.ones(1000)
plt.plot(x2,y2,'--',label='$y(t)=0.98$')


x3=5.834*np.ones(1000)
y3=np.linspace(0,0.98,1000)

plt.plot(x3,y3,'--',label='$t=5.834sec$')
plt.text(5.834,0.98,'(5.834,0.98)',horizontalalignment='right')
plt.grid()
plt.xlabel('time(sec)')
plt.ylabel('step response y(t)')
plt.legend()
plt.show()
