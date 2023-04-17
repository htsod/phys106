# vector_field_2.py
# Max Liang
# created 04/14/23
# Description:
#
#


import numpy as np
import matplotlib.pyplot as plt


x, y = np.meshgrid(np.linspace(-10, 10, 10), np.linspace(-10, 10, 10))
v = -y - x * (1 - 1/np.sqrt(1+x**2))
u = y


fig, ax = plt.subplots(figsize=(10, 10))
ax.quiver(x, y, u, v)
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()
