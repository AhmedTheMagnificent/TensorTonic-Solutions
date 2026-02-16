def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    h, w = len(image), len(image[0])
    gray_scale = [[0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2] for pixel in row] for row in image]
    return gray_scale
    