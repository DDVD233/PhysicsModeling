from variables import *
import matplotlib.pyplot as plt
from Launching import final_velocity_calculation


def coef_calculation(c, p, A, mass):
    coef = 0.5 * c * p * A / mass
    return coef


coef = coef_calculation(c, p, A, fruit_weight)


def traj_fr(coef, angle, v0, inity):  # function that computes trajectory for some launch angle & velocity
    vx0 = math.cos(math.pi / 2 - angle) * v0  # compute x components of starting velocity
    vy0 = math.sin(math.pi / 2 - angle) * v0  # compute y components of starting velocity
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
        vx[i + 1] = vx[i] + (ax[i + 1] + ax[i]) * dt / 2
        vy[i + 1] = vy[i] + (ay[i + 1] + ay[i]) * dt / 2
        x[i + 1] = x[i] + (vx[i + 1] + vx[i]) * dt / 2
        y[i + 1] = y[i] + (vy[i + 1] + vy[i]) * dt / 2
        i += 1  # increment i for next iteration

    x = x[0:i + 1]  # truncate x array
    y = y[0:i + 1]  # truncate y array
    # print('Max: X:', maxy_x, 'Y:', maxy)
    return x, y, (dt * i), x[i]  # return x, y, flight time, range of projectile


def plot_graph(v, launch_angle, explanation):
    (x, y, duration, distance) = traj_fr(coef, launch_angle, v,
                                         inity)  # define variables for output of traj_fr function

    print(explanation, ' Distance: ', distance)
    print('Duration: ', duration)

    plt.plot(x, y, label=explanation)  # quick plot of x vs y to check trajectory
    return x, y


launch_angle = launch_angle / 180 * math.pi  # Convert to radian

v0 = final_velocity_calculation(rod_weight, length_ratio, counterweight, fruit_weight
                                , x_length, y_length, initial_angle, launch_angle_radian, g, rod_length)
# plot_graph(v0, launch_angle_radian, "Average")


angle_data = np.zeros(len(time))
distance_data = np.zeros(len(time))
maximum_distance = 0
maximum_distance_angle = 0
for degree in range(0, 90):
    print('Angle: ', degree)
    angle = degree * math.pi / 180
    v0 = final_velocity_calculation(rod_weight, length_ratio, counterweight, fruit_weight
                                    , x_length, y_length, initial_angle, degree, g, rod_length)
    x, y, duration, distance = traj_fr(coef, angle, v0, inity)
    # plot_graph(v0, angle, "Average")
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
plt.plot(angle_data, distance_data, color="blue", linewidth=2.5, linestyle="-")
# -----------------Annotate----------------------
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
annotate_angle_text = 'Optimization Angle=' + str(maximum_distance_angle) + '°'
plt.annotate(annotate_angle_text, xy=(maximum_distance_angle, maximum_distance), xycoords='data',
             xytext=(+10, +20), textcoords='offset points', fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
annotate_distance_text = 'Maximum Distance\n=' + str(round(maximum_distance, 3)) + "m"
plt.annotate(annotate_distance_text, xy=(maximum_distance_angle, maximum_distance/2), xycoords='data',
             xytext=(+5, +5), textcoords='offset points', fontsize=10)
plt.plot([maximum_distance_angle, maximum_distance_angle], [0, maximum_distance], color='blue'
         , linewidth=2.5, linestyle="--")
plt.scatter([maximum_distance_angle, ], [maximum_distance, ], 50, color='blue')
# -----------------Annotate----------------------

plt.xlabel('Angle (Degree)')
plt.ylabel('Distance (m)')
# plt.legend(loc='upper left')
plt.show()
