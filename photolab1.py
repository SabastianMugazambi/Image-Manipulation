# Updated by Student: Sabastian Mugazambi to edit an image color.
# Starter program by : Sherri Goings
# Created 9/30/2010, last updated 05/09/2014
# Updated by Jadrian Miles to work with the new image library 2014-05-06.

from imageManip import *
import sys
import math

def oneColor(image, color):
    """Given an image and a color choice either as a full word or starting
    letter only (e.g red or just r); converts the whole image to the
    desired color maintaining the value of the requested color"""
    #color = raw_input("What single color do you want?")
    #I could have put raw input so that the user enters what color they want but
    #according to the example main function given it seems like the user
    #is already calling main with the right arguments.

    s_color = image.copy()

    #loop that directs the program to convert the image to the right requested color.
    if color.startswith("r"):
        for x in range(s_color.getNumPixels()):
            pixel = s_color.getPixel1D(x)
            s_color.setPixel1D(x, (pixel[0],0,0))
    elif color.startswith("g"):
        for x in range(s_color.getNumPixels()):
            pixel = s_color.getPixel1D(x)
            s_color.setPixel1D(x, (0,pixel[1],0))
    elif color.startswith("b"):
        for x in range(s_color.getNumPixels()):
            pixel = s_color.getPixel1D(x)
            s_color.setPixel1D(x, (0,0, pixel[2]))

    return s_color

def greyscale(image):
    """Convertin the image to grayscale by setting every pixel
    to the average value of every color"""
    #creating a copy to be edited.
    s_greyscale = image.copy()
    for x in range(s_greyscale.getNumPixels()):
        pixel = s_greyscale.getPixel1D(x)
        average = (pixel[0]+pixel[1]+pixel[2])/3
        s_greyscale.setPixel1D(x, (average,average,average))

    return s_greyscale

def invert(image):
    """Inverting the picture by subtracting every Rgb_color value from 255."""
    s_inverted = image.copy()
    for x in range(s_inverted.getNumPixels()):
        pixel = s_inverted.getPixel1D(x)
        s_inverted.setPixel1D(x, (255-pixel[0],255-pixel[1],255-pixel[2]))

    return s_inverted

def saturate(image, k):
    """ Saturating the image by calling the saturatedRgb function with the
    arguments taken from the Rgb_color values of each pixel."""
    s_saturate = image.copy()
    for x in range(s_saturate.getNumPixels()):
        pixel = s_saturate.getPixel1D(x)
        s_saturate.setPixel1D(x, saturatedRgb((pixel[0],pixel[1],pixel[2]), k))

    return s_saturate

def saturatedRgb(rgb, k):
    """Given an RGB color triplet (a list or tuple), and a number k,
    returns an RGB color triplet representing the original color
    saturated to the appropriate intensity as determined by k."""
    r = clipColor((.3+.7*k)*rgb[0] + .6*(1-k)*rgb[1] + .1*(1-k)*rgb[2])
    g = clipColor(.3*(1-k)*rgb[0] + (.6+.4*k)*rgb[1] + .1*(1-k)*rgb[2])
    b = clipColor(.3*(1-k)*rgb[0] + .6*(1-k)*rgb[1] + (.1+.9*k)*rgb[2])

    return (r, g, b)

def clipColor(intensity):
    return int(min(255, max(0, intensity)))


def main():
    """Tests all photolab functions."""
    if len(sys.argv) < 2:
        print "Usage: python photolab1.py <filename>"
        print "  where <filename> is an image file."
        return

    # Open file given as a command line argument.
    image = Image(sys.argv[1])

    # Display the image.
    window = DisplayWindow(1024, 768)
    image.draw(window)
    oneColor(image, 'b').draw(window)
    #invert(image).draw(window)
    #greyscale(image).draw(window)
    #saturate(image, k).draw(window)
    raw_input("Hit [Enter] to quit. ")

if __name__ == "__main__":
    main()
