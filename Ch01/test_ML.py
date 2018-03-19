import scipy as sp
import matplotlib.pyplot as plt

data = sp.genfromtxt('web_traffic.tsv',delimiter = "\t")
x = data[:,0]
y = data[:,1]

fp1 = sp.polyfit(x,y,1)
f1 = sp.poly1d(fp1)

fx = sp.linspace(0,x[-1],1000)


plt.plot(fx,f1(fx),linewidth = 4)
plt.legend(["d=%i" %f1.order],loc="upper left")
plt.scatter(x,y)
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],['week %i' %w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()