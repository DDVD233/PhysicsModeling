import numpy as np
import math
import scipy.constants as const
import Projectile
import matplotlib.pyplot as plt


g = const.g  # gravitational constant
x_length = 1  # Length of x
length_ratio = 3.75  # y/x
y_length = 3.75  # Length of y
counterweight = 50  # Mass of the counterweight
fruit_weight = 0.02  # Mass of the fruit (kg)
initial_angle = -45  # Horizontal level arm Initial angle (degree)
launch_angle = 45  # Launch Angle (degree)
rod_weight = 1  # Weight of the rod
pi = math.pi

# When the coefficient is very large, it could cause stack overflow

dt = 1e-5  # integration time step (delta t)

'''
v0 = 35  # Average speed at t=0
v0min = 30  # Minimum Speed
v0max = 40  # Maximum Speed
'''

time = np.arange(0, 2000, dt)  # create time axis
c = 0.47  # Drag Coefficient
p = 1.225  # Density of the air (kg/m^3)
A = 0.01  # Surface Area (m^2)
inity = 0  # Initial height (m)
windx = 0  # Wind velocity in the x direction（vector) (m/s)
wind_y = 0  # Wind velocity in the y direction（vector) (m/s)

launch_angle = launch_angle / 180 * math.pi  # Convert to radian

Projectile.plot_graph(final_velocity, 'Average')
Projectile.plt.xlabel('Distance')
plt.ylabel('height')
plt.legend(loc='upper left')
plt.show()