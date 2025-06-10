"""
Functions are structured as follows:

def name_of_the_function(parameter1, parameter2,...):
    line of code 1
    line of code 2
    ...
    line of code n
    return -expression-

    obs: you can't have funcitons and variables with the same name.
"""

""" length = 10
height = 5
depth = 7

def volume_of_a_cuboid (length, height, depth):
    return length * height * depth

volume = volume_of_a_cuboid (length, height, depth)
print(volume)"""

# two ways of getting writing the same function

def volume_of_a_cube(length, height, depth):
    """
    Calculates the volume of a cube
    """
    volume_of_cube = 5 * 10 * 7
    return volume_of_cube

print(volume_of_a_cube(5, 10, 7))