import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb

fig = plt.figure(111, facecolor='grey')
xmin = -10
xmax = 10
dx = 0.1

xlist = np.around(np.arange(xmin, xmax, dx), decimals=4)
for i in range(len(xlist)):
    if(xlist.__getitem__(i)==0):
        xlist.__setitem__(i, 0.1)


ylist = 1 / xlist
ylist2 = 2 / xlist
ylist3 = 0.5/xlist

plt.grid(10, color='grey')
plt.title("Туник Евгений")
plt.xlabel("Вісь X", color = 'blue')
plt.ylabel("Вісь Y", color = 'blue')
plt.plot(xlist, ylist, label = 'y = 1/x', color = 'purple', linestyle='--')
plt.plot(xlist, ylist2, label = 'y = 2/x', color = 'g')
plt.plot(xlist, ylist3, label = 'y = 0.5/x', color = 'darkorange', linestyle='-.')
plt.legend(loc = 'lower right')
plt.show()


