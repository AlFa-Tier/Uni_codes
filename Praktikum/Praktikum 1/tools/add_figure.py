#!/usr/bin/python3
from os import getcwd 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def add_figure(RELPATH, WIDTH=10.0, HEIGHT=10.0):
    """
    Display figure located at RELPATH through matplotlib rendering machine.
    
    WIDTH and HEIGHT can be given as parameters of type float to determine the 
    measures of the figure. Nominally both are given in inches. Axes will be 
    suppressed.
    """
    PREFIX=getcwd()+"/"
    print(PREFIX+RELPATH)
    print(RELPATH[:RELPATH.rfind(".")].replace("/", "_"))
    img = plt.figure(RELPATH[:RELPATH.rfind(".")].replace("/", "_"), figsize=(WIDTH, HEIGHT))
    img = mpimg.imread(PREFIX+RELPATH)
    # Render image in background
    imgplot = plt.imshow(img)
    # Hide axes
    imgplot.axes.get_xaxis().set_visible(False)
    imgplot.axes.get_yaxis().set_visible(False)
    # Show image
    plt.show()

import argparse

parser = argparse.ArgumentParser(
    prog="PROG",
    description="Add figure to code cell in Jupyter-notebook."
    )
parser.add_argument('filename', type=str, nargs=1,
    help='Filename with relative path statement.')
parser.add_argument('--witdh', type=float, dest='WIDTH', nargs=1, default=10.0,
    help='Width of file (default 10.0 inches).')
parser.add_argument('--height', type=float, dest='HEIGHT', nargs=1, default=10.0,
    help='Height of file (default 10.0 inches).')
args = parser.parse_args()
add_figure(args.filename[0], args.WIDTH, args.HEIGHT)

