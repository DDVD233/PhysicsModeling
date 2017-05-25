import matplotlib.pyplot as plt
from variables import *
from Launching import final_velocity


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

    if wind_y > vy[0]:
        ay[0] = coef * ((wind_y - vy[0]) ** 2) - g
    else:
        ay[0] = -coef * ((wind_y - vy[0]) ** 2) - g
    # When the wind velocity is greater than the initial velocity, the "air resistance" actually accelerates the fruit

    i = 0
    while y[i] >= 0:  # loop continuous until y becomes <0, ie projectile hits ground
        if vy[i] > wind_y:
            ay[i + 1] = -coef * ((wind_y - vy[i]) ** 2) - g
        else:
            ay[i + 1] = coef * ((wind_y - vy[i]) ** 2) - g

        if windx > vx[i]:
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
    (x, y, duration, distance) = traj_fr(coef, launch_angle, v,
                                         inity)  # define variables for output of traj_fr function

    print(explanation, ' Distance: ', distance)
    print('Duration: ', duration)

    plt.plot(x, y, label=explanation)  # quick plot of x vs y to check trajectory
    return x, y


# xmax, ymax = plot_graph(v0max, 'Maximum')
# xmin, ymin = plot_graph(v0min, 'Minimum')
# plt.fill_between(time, ymin, ymax, where=(ymax > ymin), color='blue', alpha=0.25)
plot_graph(final_velocity, 'Average')
plt.xlabel('Distance')
plt.ylabel('height')
plt.legend(loc='upper left')
plt.show()
