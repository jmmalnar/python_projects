# Solve a first order Differential Equation initial value problem
# using Runge-Kutta 4
from math import sqrt
import matplotlib.pyplot as plt

# y'(t) = t*sqrt(y)
def f(t, y):
    return t * sqrt(y)

# f is the function
# x0 and y0 are initial values
def rk4(function, t, y, h, t_max):
    t_list = [t]
    y_list = [y]
    for i in range(t, t_max):
        k1 = h * function(t, y)
        k2 = h * function(t + h/2, y + k1/2)
        k3 = h * function(t + h/2, y + k2/2)
        k4 = h * function(t + h, y + k3)
        y = y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        t = t + h
        t_list.append(t)
        y_list.append(y)
    return t_list, y_list


# t, y = rk4(f, 0, 1, 0.1, 100)
# print(t)
# results = zip(t, y)
# for t, y in results:
#     print("{:.1f},{:.5f}".format(t, y))

# plt.plot([0.0, 0.1, 0.2, 0.3, 0.4, 0.5], [1.0, 1.005, 1.0201, 1.0455, 1.0816, 1.12891])
# plt.axis([0,10,0,700])
# plt.xlabel("X LABEL")
# plt.ylabel("Y LABEL")
# plt.show()