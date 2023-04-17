# vector_field_1.py
# Max Liang
# created 04/14/23
# Description:
#
#


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

damp = 1
spring = 1

X, Y = np.meshgrid(np.linspace(-10, 10, 10), np.linspace(-20, 20, 20))

U = Y
V = - damp * Y - spring * X * (1 - 1 / np.sqrt(1 + X ** 2))

length = np.sqrt(U**2 + V**2)

fig, ax = plt.subplots(figsize=(10, 10))
Q = plt.quiver(X, Y, U, V,
                color='b',
                scale=5, units='y')

plt.subplots_adjust(left=0.25, bottom=0.25)


axdamp = plt.axes([0.25, 0.10, 0.65, 0.03])
axspring = plt.axes([0.1, 0.25, 0.0225, 0.63])

sd = Slider(axdamp, 'damp', 1, 10, valinit=spring, orientation="horizontal")
ss = Slider(axspring, 'spring', 1, 10, valinit=damp, orientation="vertical")


def update(val):
    damp = sd.val
    spring = ss.val
    U = Y
    V = - damp * Y - spring * X * (1 - 1 / np.sqrt(1 + X ** 2))
    Q.set_UVC(U, V)
    fig.canvas.draw_idle()


sd.on_changed(update)
ss.on_changed(update)


resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    sd.reset()
    ss.reset()


button.on_clicked(reset)

plt.show()
