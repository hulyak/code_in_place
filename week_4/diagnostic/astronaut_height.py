"""
Write a program which asks the user for their height in meters and prints whether or not they are the correct height to be a NASA astronaut.

If their height is between 1.6 meters and 1.9 meters, print "Correct height to be an astronaut". If their height is less than 1.6 meters, print "Below minimum astronaut height". If their height is greater than 1.9 meters, print "Above maximum astronaut height".

"""


# Example Solution 1
def main():
    # get the user height, cast it to a float, save as a variable
    user_height = float(input('Enter your height in meters: '))
    # first rule out that they are too short
    if user_height < 1.6:
        print('Below minimum astronaut height')
    # then rule out that they are too tall
    elif user_height > 1.9:
        print('Above maximum astronaut height')
    # at this point you know they are the correct height
    else:
        print('Correct height to be an astronaut')


# Example Solution 2
def main():
    user_height = float(input('Enter you height in meters: '))
    if user_height >= 1.6 and user_height <= 1.9:
        print('Correct height to be an astronaut')
    elif user_height < 1.6:
        print('Below minimum astronaut height')
    else:
        print('Above maximum astronaut height')
