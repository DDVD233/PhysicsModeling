import math


def rod_mass_calculation(rod_weight, ratio):
    x = rod_weight / (1 + ratio)
    y = rod_weight * ratio / (1 + ratio)

    return x, y


def total_mass_calculation(rod_weight, counterweight, fruit_weight):
    total_mass = (rod_weight + counterweight + fruit_weight)

    return total_mass


def lever_system_changing_height_calculation(total_mass, mass_x, mass_y, initial_angle,
                                             launch_angle, counterweight, fruit_weight, x_length, y_length):
    changing_angle = math.sin(-initial_angle) + math.sin(launch_angle)  # See paper for detail
    # Because in this equation we are assuming the initial angle is positive, while in the variable it's negative,
    # we added a minus sign before it.
    mx_sum = counterweight * x_length + x_length / 2 * mass_x - fruit_weight * y_length - y_length/2 * mass_y
    changing_height = changing_angle * mx_sum / total_mass

    return changing_height


def gravitational_potential_energy_calculation(total_mass, changing_height, g):
    gravitational_potential_energy = total_mass * changing_height * g

    return gravitational_potential_energy


def lever_system_monment_of_inertia_calculation(rod_weight, rod_length, counterweight, x_length, fruit_weight, y_length):
    moment_of_inertia = (1/3) * rod_weight * (rod_length **2) + counterweight * (x_length ** 2) + fruit_weight * (y_length ** 2)

    return moment_of_inertia


def final_angular_velocity_calculation(gravitational_potential_energy, moment_of_inertia):
    final_angular_velocity = math.sqrt((2 * gravitational_potential_energy) / moment_of_inertia)

    return final_angular_velocity


def final_velocity_calculation(rod_weight, length_ratio, counterweight, fruit_weight
                               , x_length, y_length, initial_angle, launch_angle_radian, g, rod_length):
    mass_x, mass_y = rod_mass_calculation(rod_weight, length_ratio)  # mass of x and y

    total_mass = total_mass_calculation(rod_weight, counterweight, fruit_weight)

    changing_height = lever_system_changing_height_calculation(total_mass, mass_x, mass_y, initial_angle, launch_angle_radian
                                                               , counterweight, fruit_weight, x_length, y_length)

    gravitational_potential_energy = gravitational_potential_energy_calculation(total_mass, changing_height, g)

    moment_of_inertia = lever_system_monment_of_inertia_calculation(rod_weight, rod_length, counterweight,
                                                                    x_length, fruit_weight, y_length)

    final_angular_velocity = final_angular_velocity_calculation(gravitational_potential_energy, moment_of_inertia)

    final_velocity = final_angular_velocity * y_length

    print('Final Velocity:', final_velocity)

    return final_velocity

