from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,10,0.01)
y = np.arange(0,0.99,0.001)
t,k = np.meshgrid(x,y)
y = 1-((np.exp(-t))*(((np.sinh(t*np.sqrt(1-k)))/(np.sqrt(1-k)))+(np.cosh(t*np.sqrt(1-k)))))

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

# Plot a 3D surface
ax.plot_surface(t, k, y)
ax.set_xlabel('time(sec)')
ax.set_ylabel('k')
ax.set_zlabel('y(t)')

plt.show()
