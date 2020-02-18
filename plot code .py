import numpy as np
import matplotlib.pyplot as plt 

t=np.linspace(-3,10,1000)
f=t*(np.exp(-t))*np.heaviside(t,1)
plt.plot(t,f)
plt.grid()
plt.show()

