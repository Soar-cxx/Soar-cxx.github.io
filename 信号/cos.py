import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-np.pi,np.pi, 100)
x1 = [t*np.pi for t in x]
y = np.cos(x1)

plt.plot(x, y)

plt.xlabel('t/s')
plt.ylabel('X(t)')

plt.xlim(x.min()*1.2, x.max()*1.2)
plt.ylim(y.min()*1.2, y.max()*1.2)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.show()