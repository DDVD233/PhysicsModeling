import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.constants as const

g = const.g  # gravitational constant
x_length = 1  # Length of x
length_ratio = 3.75  # y/x
y_length = 3.75 # Length of y
counterweight = 50  # Mass of the counterweight
fruit_weight = 0.02  # Mass of the fruit (kg)
initial_angle = -45  # Horizontal level arm Initial angle (degree)
launch_angle = 45  # Launch Angle (degree)
rod_weight = 1  # Weight of the rod
pi = math.pi




def rod_mass_calculation(total_mass, ratio):
    x = total_mass / (1 + ratio)
    y = total_mass * ratio / (1 + ratio)

    return x, y

mass_x, mass_y = rod_mass_calculation(rod_weight, length_ratio)  # mass of x and y

def lever_system_torque_calculation:
    torque = (mass_x + counterweight) * g * x_length + (mass_y + fruit_weight) * g * y_length

    return torque

torque = lever_system_torque_calculation()

def lever_system_monment_of_inertia_calculation:
    moment_of_inertia = ((1/3) * mass_x * g * (x_length **2) + counterweight * (x_length **2) ) + ((1/3) * mass_y * g * (y_length **2) + fruit_weight * (y_length **2))

    return moment_of_inertia

moment_of_inertia = lever_system_monment_of_inertia_calculation()

def angular_acceleration_calculation:
    angular_acceleration = torque / moment_of_inertia

    return angular_acceleration

angular_acceleration = angular_acceleration_calculation()

def theta_lever_has_moved_calculation:
    theta = (launch_angle - initial_angle) * pi / 180

    return theta

theta = theta_lever_has_moved_calculation()

def final_velocity_calculation:
    final_velocity = sqrt(2 * (y_length **2) * angular_acceleration * theta)

    return final_velocity

final_velocity = final_velocity_calculation()


# -----------------------分割线----------------------------------------

# When the coefficient is very large, it could cause stack overflow

dt = 1e-9  # integration time step (delta t)
v0 = 15  # Average speed at t=0
v0min = 30  # Minimum Speed
v0max = 40  # Maximum Speed
time = np.arange(0, 2000, dt)  # create time axis
c = 0.47  # Drag Coefficient
p = 1.225  # Density of the air (kg/m^3)
A = 0.01  # Surface Area (m^2)
inity = 0  # Initial height (m)
windx = -5  # Wind velocity （vector) (m/s)

launch_angle = launch_angle / 180 * math.pi  # Convert to radian


def coef_calculation(c, p, A, mass):
    coef = 0.5 * c * p * A / mass
    return coef


coef = coef_calculation(c, p, A, fruit_weight)


def traj_fr(coef, angle, v0, inity):  # function that computes trajectory for some launch angle & velocity
    vx0 = math.cos(angle) * v0  # compute x components of starting velocity
    vy0 = math.sin(angle) * v0  # compute y components of starting velocity
    x = np.zeros(len(time))  # initialize x array
    y = np.zeros(len(time))  # initialize y array
    vx = np.zeros(len(time))  # initialize vx array
    vy = np.zeros(len(time))  # initialize vy array
    ax = np.zeros(len(time))  # initialize ax array
    ay = np.zeros(len(time))  # initialize ay array

    x[0], y[0] = 0, inity  # initial position at t=0s, ie motion starts at (0,0)
    vx[0] = vx0
    vy[0] = vy0
    if windx > vx[0]:
        ax[0] = coef * ((vx[0] - windx) ** 2)
    else:
        ax[0] = -coef * ((vx[0] - windx) ** 2)
    # When the windx velocity is greater than the initial velocity, the "air resistance" actually accelerates the fruit

    ay[0] = -coef * (vy[0] ** 2) - g
    i = 0
    while y[i] >= 0:  # loop continuous until y becomes <0, ie projectile hits ground
        if vy[i] > 0:
            ay[i + 1] = -coef * (vy[i] ** 2) - g
        else:
            ay[i + 1] = coef * (vy[i] ** 2) - g

        if windx > vx[0]:
            ax[i + 1] = coef * ((vx[i] - windx) ** 2)
        else:
            ax[i + 1] = -coef * ((vx[i] - windx) ** 2)
        vx[i + 1] = vx[i] + ax[i + 1] * dt
        vy[i + 1] = vy[i] + ay[i + 1] * dt
        x[i + 1] = x[i] + (vx[i + 1] + vx[i]) * dt / 2
        y[i + 1] = y[i] + (vy[i + 1] + vy[i]) * dt / 2
        i += 1  # increment i for next iteration

    x = x[0:i + 1]  # truncate x array
    y = y[0:i + 1]  # truncate y array
    # print('Max: X:', maxy_x, 'Y:', maxy)
    return x, y, (dt * i), x[i]  # return x, y, flight time, range of projectile


'''
angle_data = np.zeros(len(time))
distance_data = np.zeros(len(time))
maximum_distance = 0
maximum_distance_angle = 0
for degree in range(0, 90):
    angle = degree / 180 * math.pi
    x, y, duration, distance = traj_fr(coef, angle, v0, inity)
    angle_data[degree] = degree
    distance_data[degree] = distance
    if distance > maximum_distance:
        maximum_distance = distance
        maximum_distance_angle = degree
    print('Distance: ', distance)
    print('Duration: ', duration)

angle_data = angle_data[0:90]
distance_data = distance_data[0:90]
print('Maximum distance:', maximum_distance)
print('Angle for maximum distance', maximum_distance_angle)
plt.plot(angle_data, distance_data)

'''


def plot_graph(v, explanation):
    (x, y, duration, distance) = traj_fr(coef, launch_angle, v, inity)  # define variables for output of traj_fr function

    print(explanation, ' Distance: ', distance)
    print('Duration: ', duration)

    plt.plot(x, y, label=explanation)  # quick plot of x vs y to check trajectory
    return x, y


# xmax, ymax = plot_graph(v0max, 'Maximum')
# xmin, ymin = plot_graph(v0min, 'Minimum')
# plt.fill_between(time, ymin, ymax, where=(ymax > ymin), color='blue', alpha=0.25)
plot_graph(v0, 'Average')
plt.xlabel('time')
plt.ylabel('height')
plt.legend(loc='upper left')
plt.show()
