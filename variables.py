import numpy as np
import math
import scipy.constants as const


g = const.g  # gravitational constant

x_length = 0.21  # Length of x
y_length = 1.117  # Length of y
length_ratio = y_length/x_length  # y/x
rod_length = x_length + y_length  # total length of rod
counterweight = 11.79  # Mass of the counterweight
fruit_weight = 0.02  # Mass of the fruit (kg)
initial_angle = -40  # Horizontal level arm Initial angle (degree)
launch_angle = 70  # Launch Angle (degree)
launch_angle_radian = launch_angle * math.pi / 180
rod_weight = 0.168  # mass of the rod


# When the coefficient is very large, it could cause stack overflow

dt = 1e-4  # integration time step (delta t)

'''
v0 = 35  # Average speed at t=0
v0min = 30  # Minimum Speed
v0max = 40  # Maximum Speed
'''

time = np.arange(0, 2000, dt)  # create time axis
c = 0.47  # Drag Coefficient
p = 1.225  # Density of the air (kg/m^3)
A = 0.0113  # Surface Area (m^2)
inity = 1.597  # Initial height (m)
windx = 0  # Wind velocity in the x direction（vector) (m/s)
wind_y = 0  # Wind velocity in the y direction（vector) (m/s)
