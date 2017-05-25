from variables import *


def rod_mass_calculation(total_mass, ratio):
    x = total_mass / (1 + ratio)
    y = total_mass * ratio / (1 + ratio)

    return x, y


mass_x, mass_y = rod_mass_calculation(rod_weight, length_ratio)  # mass of x and y


def lever_system_changing_height_calculation():
    changing_height = math.sqrt(2 * (y_length **2) - 4 * y_length * math.cos(launch_angle - initial_angle))

    return changing_height


changing_height = lever_system_changing_height_calculation()


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
