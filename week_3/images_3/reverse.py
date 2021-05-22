from simpleimage import SimpleImage


def invert_image(image):
    for pixel in image:
        red = pixel.red
        blue = pixel.blue
        green = pixel.green

        inverse_red = 255 - red
        inverse_blue = 255 - blue
        inverse_green = 255 - green

        pixel.red = inverse_red
        pixel.blue = inverse_blue
        pixel.green = inverse_green

    image.show()


def main():
    image = SimpleImage('images/burrito.jpeg')
    # inverted_image = invert_image(image)
    # inverted_image.show()

   # make a new blank image
    output_image = SimpleImage.blank(2 * image.width, image.height)

  # get the coordinates of the pixels
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.get_pixel(x, y)

            pixel_left = output_image.get_pixel(x, y)
            pixel_left.red = pixel.red
            pixel_left.green = pixel.green
            pixel_left.blue = pixel.blue

            # reflection, get to the very end of the image and move to the left from there and y is height
            pixel_right = output_image.get_pixel(output_image.width - 1 - x, y)
            pixel_right.red = pixel.red
            pixel_right.green = pixel.green
            pixel_right.blue = pixel.blue

    output_image.show()


if __name__ == '__main__':
    main()
