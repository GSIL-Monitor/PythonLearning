#!/usr/bin/env python
import math

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 10000)
y = x
x2 = []
z = []
for i in x:
    k = 0
    if i > 0:
        x2.append(i)
        z.append(8 * math.log10(i))
        # print 8*math.log10(i),i
        k = 8 * math.log10(i) - i
    if math.fabs(k) <= 0.001:
        print(i)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color="red", linewidth=2)
plt.plot(x2, z, color="blue")

plt.xlabel('X')
plt.ylabel('Y')
plt.ylim(0, 10)
plt.legend()
plt.show()
