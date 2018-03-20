import scipy as sp
import matplotlib.pyplot as plt

def error(f,x,y):
    return sp.sum((f(x)-y)**2)

data = sp.genfromtxt('web_traffic.tsv',delimiter = "\t")
x = data[:,0]
y = data[:,1]

inflection = 3.5*7*24

#before inflection
xa = x[:inflection]
ya = y[:inflection]

#after inflection
xb = x[inflection:]
yb = y[inflection:]

fpa1 = sp.polyfit(xa,ya,1)
fa1 = sp.poly1d(fpa1)

fpb1 = sp.polyfit(xb,yb,1)
fb1 = sp.poly1d(fpb1)

fx = sp.linspace(0,x[-1],1000)

print(error(fa1,x,y))

plt.plot(fx,fa1(fx),linewidth = 4)
plt.plot(fx,fb1(fx),linewidth = 4)
plt.legend(["d=%i" %fa1.order],loc="upper left")

plt.scatter(x,y)
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],['week %i' %w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()

