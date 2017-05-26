from variables import *


def rod_mass_calculation(total_mass, ratio):
    x = total_mass / (1 + ratio)
    y = total_mass * ratio / (1 + ratio)

    return x, y


mass_x, mass_y = rod_mass_calculation(rod_weight, length_ratio)  # mass of x and y


def lever_system_changing_height_calculation(mass_x, mass_y):
    total_mass = rod_weight + fruit_weight + counterweight
    changing_angle = math.sin(-initial_angle) + math.sin(launch_angle)  # See paper for detail
    # Because in this equation we are assuming the initial angle is positive, while in the variable it's negative,
    # we added a minus sign before it.
    mx_sum = counterweight * x_length + x_length / 2 * mass_x - fruit_weight * y_length - y_length/2 * mass_y
    changing_height = changing_angle * mx_sum / total_mass

    return changing_height


changing_height = lever_system_changing_height_calculation(mass_x, mass_y)


def lever_system_monment_of_inertia_calculation():
    moment_of_inertia = ((1/3) * rod_weight * (rod_length **2) + counterweight * (x_length ** 2)) + fruit_weight * (y_length ** 2))

    return moment_of_inertia


moment_of_inertia = lever_system_monment_of_inertia_calculation()


def angular_acceleration_calculation():
    angular_acceleration = torque / moment_of_inertia
    print('Angular Acceleration: ', angular_acceleration)

    return angular_acceleration


angular_acceleration = angular_acceleration_calculation()


def theta_lever_has_moved_calculation():
    theta = (launch_angle - initial_angle) * pi / 180

    return theta


theta = theta_lever_has_moved_calculation()


def final_velocity_calculation():
    final_velocity = math.sqrt(2 * (y_length ** 2) * angular_acceleration * theta)

    return final_velocity


final_velocity = final_velocity_calculation()
print('Final Velocity:', final_velocity)
