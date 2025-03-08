# Nathan Parker
# 03/07/25
# Program #4: Coordinates

# import the math module
import math

# define the distance function
def distance(t1,t2):

    # calculate the distance
    d = math.sqrt((t2[0] - t1[0])**2 + (t2[1] - t1[1])**2 + (t1[2] - t2[2])**2)

    # return the calculated value
    return d

# define the main function
def main():

    # catch faulty input
    try:

        # get the first point from the user
        x1 = float(input('Enter the x coordinate for the first point: '))
        y1 = float(input('Enter the y coordinate for the first point: '))
        z1 = float(input('Enter the z coordinate for the first point: '))

        # get the second point from the user
        x2 = float(input('Enter the x coordinate for the second point: '))
        y2 = float(input('Enter the y coordinate for the second point: '))
        z2 = float(input('Enter the z coordinate for the second point: '))

        # put the points into two tuples
        tuple1 = (x1, y1, z1)
        tuple2 = (x2, y2, z2)

        # call the distance function
        returned_value = distance(tuple1, tuple2)

        # print the returned value
        print(f'The distance between these two points is {returned_value}')

    # catch faulty input
    except ValueError:

        # display error message
        print('Enter only numbers.')

# call the main function
if __name__ == '__main__':
    main()

