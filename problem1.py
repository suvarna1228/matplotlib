import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-2*np.pi,2*np.pi,1000)
tan_t=np.tan(x)
cot_t=1/np.tan(x)

plt.figure(figsize=(10, 6))
plt.plot(x,tan_t,color='red',label=r'$\tan(x)$')
plt.plot(x,cot_t,color='blue',label=r'$\cot(x)$')


plt.xlabel('x')
plt.ylabel('Function values')
plt.title(r'Plots of $\tan(x)$ and $\cot(x)$')

plt.legend(loc='lower right')

plt.axhline(0, color='gray', linestyle='-', linewidth=0.5)
plt.axvline(0, color='gray', linestyle='-', linewidth=0.5)

plt.xlim(-2 * np.pi, 2 * np.pi)
plt.ylim(-10, 10)



plt.grid(True)
plt.show()
