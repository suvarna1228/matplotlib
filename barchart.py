import matplotlib.pyplot as plt
import numpy as np

company=['hi','hlo','hey','hoi']
revenue=[90,80,70,89]
profit=[40,50,39,2]

xpos=np.arange(len(company))
plt.xticks(xpos,company)
plt.ylabel("revenue(bln)")
plt.title("us tech stocks")
plt.bar(xpos-0.2,revenue,width=0.4,label='revenue')
plt.bar(xpos+0.2,profit,width=0.4,label='profit')


plt.legend(loc='upper right')
plt.show()