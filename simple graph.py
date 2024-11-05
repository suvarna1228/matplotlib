import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[50,51,52,53,54,48,49]
plt.xlabel('day')
plt.ylabel('temperature')
plt.title('weather')
plt.plot(x,y,color='red',linewidth=5,linestyle='dashed')
plt.show()