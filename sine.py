import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0,4*np.pi,0.5)
plt.plot(t,np.sin(t),marker='+',label="sin")
plt.plot(t,np.cos(t),marker='^',label="cos")
plt.xticks(t)
plt.title("sin and cos graph")
plt.xlabel("angle")
plt.ylabel("sine and cos")
plt.legend()

plt.show()