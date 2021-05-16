"""
SECTION 4: IMAGES AND FUNCTIONS

This program loads an image and applies the narok filter
to it by setting "bright" pixels to grayscale values.

Recall that a pixel can be represented by 3 integers between 0 and 255, representing its red, green and blue components. A pixel's 'average component' is just the average of its red, green and blue components, which can be calculated by adding them all together and dividing by 3.

The idea behind the Narok filter is to replace each bright pixel in an image with its grayscale equivalent. A bright pixel in an image is defined as a pixel whose average component is greater than 153 (which is 60% of 255). All non-bright pixels in the image should remain unchanged.

To make a pixel grayscale, simply set each of its red, green and blue components to be equal to its average component.

Tip! As a first step in a program like this, we recommend defining a function to get the average component of a pixel. This is a calculation you'll find yourself needing to do repeatedly.
"""

from simpleimage import SimpleImage


BRIGHT_THRESHOLD = 153


def main():
    image = SimpleImage('images/simba-sq.jpeg')

    for pixel in image:
        pixel_average = get_pixel_average(pixel)
        if pixel_average > BRIGHT_THRESHOLD:
            pixel.red = pixel_average
            pixel.green = pixel_average
            pixel.blue = pixel_average

    # Apply the filter
    image.show()


def get_pixel_average(pixel):
    color_component_sum = pixel.red + pixel.green + pixel.blue
    average_color_component = color_component_sum // 3
    return average_color_component


if __name__ == '__main__':
    main()
