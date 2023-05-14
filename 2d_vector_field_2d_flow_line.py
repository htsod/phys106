# 2_vector_field_2d_flow_line.py
# Max Liang
# created 04/14/23
# Description:
#
#


import numpy as np
import matplotlib.pyplot as plt


# hw3_p3
def func(x):
    return np.array([x[0]*(3-2*x[0]-x[1]), x[1]*(2-x[0]-x[1])])


x_bound, y_bound, field_density, step, T = [-0.5, 2], [-0.5, 3], 30, 1000, 100
init_pos = [[0.1, 0.1], [1/2, 0], [0.1, 2.5]]




# hw3_p2
# def func(x):
#     return np.array([np.sin(x[1]), x[0] - x[0]**(3)])


# x_bound, y_bound, field_density, step, T = [-3.5, 3.5], [-3.5, 3.5], 30, 1000, 10
# init_pos = [[1/2, 1/2], [0, 2], [1, 1]]


def runge_kutta(func, dt, x):
    k1 = func(x) * dt
    k2 = func(x+k1/2) * dt
    k3 = func(x+k2/2) * dt
    k4 = func(x+k3/2) * dt
    return (x + (k1 + 2*k2 + 2*k3 + k4)/6)


def gen_vec(init_pos, step, T):
    dt = T/step
    initial_vec = []
    initial_name = []
    for i in range(len(init_pos)):
        initial_vec.append(np.array(init_pos[i]))
        initial_name.append(f"init_pos = {init_pos[i]}")

    x_list = [[] for i in range(len(initial_vec))]
    for j in range(len(initial_vec)):
        for i in range(step):
            x_list[j].append(initial_vec[j])
            initial_vec[j] = runge_kutta(func, dt, initial_vec[j])

    pos_list = [[] for i in range(len(x_list))]
    for i in range(len(x_list)):
        pos_list[i] = np.array(x_list[i]).T
    return pos_list, initial_name

        
def plotting(x_bound, y_bound, field_density, func, init_pos, step, T):
    x_list, init_name = gen_vec(init_pos, step, T)
    x, y = np.meshgrid(np.linspace(x_bound[0], x_bound[1], field_density), 
                       np.linspace(y_bound[0], y_bound[1], field_density))
    u, v = func([x, y])[0], func([x, y])[1]
    u = u / np.sqrt(u**2 + v**2)
    v = v / np.sqrt(u**2 + v**2)

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.quiver(x, y, u, v, alpha=0.5)
    ax.set_xlim(x_bound[0], x_bound[1])
    ax.set_ylim(y_bound[0], y_bound[1])

    for i in range(len(x_list)):
        ax.plot(x_list[i][0], x_list[i][1], label=init_name[i])

    ax.legend(loc=1)
    ax.set_title("Vector Field and Flow Lines", fontsize=14)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("y", fontsize=12)
    plt.show()


plotting(x_bound, y_bound, field_density, func, init_pos, step, T)



