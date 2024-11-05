import matplotlib.pyplot as plt
exp_vals = [1400,600,300,410,250]
exp_labels = ["Home Rent","Food","Phone/Internet Bill","Car ","Other Utilities"]
plt.pie(exp_vals,labels=exp_labels,autopct="%0.1f%%" ,explode=[0,0,0,0.1,0])
plt.show()