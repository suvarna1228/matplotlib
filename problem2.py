import matplotlib.pyplot as plt 
import numpy as np

x=np.linspace(-np.pi,np.pi,1000)

sin_x = np.sin(x)
cos_x = np.cos(x)

plt.plot(x,sin_x,color='orange',label="sin(x)")
plt.plot(x,cos_x,color='green',label='cos(x)')

plt.axhline(0, color='gray', linestyle='-', linewidth=0.5)
plt.axvline(0, color='gray', linestyle='-', linewidth=0.5)

plt.xlim(-np.pi, np.pi)
plt.ylim(-1.1, 1.1)

plt.xlabel('x')
plt.ylabel('fuctional value')
plt.title('sin x & cos x vs x')

plt.legend(loc='best')

plt.grid(True)
plt.show()