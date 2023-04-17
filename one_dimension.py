# one_dimension.py
# Max Liang
# created 04/14/2023
# Description:
#
#
#


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


def function(x, r):
    # The parametrized function to be plotted
    return r + np.cos(x) + np.cos(2 * x)


x = np.linspace(-10, 10, 1000)
# Define initial parameters
r_init = 0
# Create the figure and the line that we will manipulate
fig, ax = plt.subplots(figsize=(10, 10))
line, = ax.plot(x, function(x, r_init), lw=2)
ax.set_xlabel("x")
ax.set_ylabel("x_dot")
# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.25)
# Make a vertical slider to control the frequency.
axr_val = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
# Make a vertically oriented slider to control the amplitude
r_slider = Slider(
    ax=axr_val,
    label="r",
    valmin=-30,
    valmax=30,
    valinit=r_init,
    orientation="vertical"
)


def update(val):
    # The function to be called anytime a slider's value changes
    line.set_ydata(function(x, r_slider.val))
    ax.plot(x, np.zeros(len(x)), 'r')
    fig.canvas.draw_idle()


# register the update function with each slider
r_slider.on_changed(update)
# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
reset_ax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(reset_ax, "Reset", hovercolor='0.975')


def reset(event):
    r_slider.reset()


button.on_clicked(reset)

plt.show()




