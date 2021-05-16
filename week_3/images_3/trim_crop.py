"""
Trim Crop
Write a function trim_crop_image which removes trim_size amount of pixels from each side of the image.


def trim_crop_image(original_img, trim_size):
    
This function returns a new SimpleImage which is a trimmed and
cropped version of the original image by shaving trim_sz pixels
 from each side(top, left, bottom, right) of the image. You may
  assume trim_size is less than half the width of the image.

   Inputs:
        - original_img: The original image to process
        - trim_size: The number of pixels to shave from each side
        of the original image

    Returns:
        A new SimpleImage with trim_size pixels shaved off each
        side of the original image
    


For example, if we called trim crop on this picture of Karel, and removed trim_size = 30 pixels from all sides:


It would produce an image that looks something like this:


Note that the dimensions of this new image is smaller(both the width and the height have been reduced by 60 pixels).
"""
from simpleimage import SimpleImage


def main():
    image = SimpleImage('images/karel.png')
    trimmed_img = trim_crop_image(image, 30)
    trimmed_img.show()


def trim_crop_image(original_img, trim_size):
    """
    This function returns a new SimpleImage which is a trimmed and
    cropped version of the original image by shaving trim_sz pixels
    from each side (top, left, bottom, right) of the image. You may
    assume trim_sz is less than half the width of the image.

    Inputs:
        - original_img: The original image to process
        - trim_size: The number of pixels to shave from each side
                   of the original image

    Returns:
        A new SimpleImage with trim_sz pixels shaved off each
        side of the original image

    dimensions of new image = dimensions of old image - trimmed off image
    copy pixels from original image to new image
    src_x = x + trim size src
    copy pixels = copy color components
    """
    # creates a blank image, 400px width 200px height
    output = SimpleImage.blank(400, 200)


if __name__ == '__main__':
    main()
