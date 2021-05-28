import math
import numpy
from simpleimage import SimpleImage

def find_triangle_vertex(p1, p2):
# Given two points p1 and p2, this functions finds the coordinates of the third vertex of an equilateral triangle.
# Rotates p2 about p1 by +60° 
    return (p2[0] - p1[0]) * 1/2 - (p2[1] - p1[1]) * math.sqrt(3) / 2 + p1[0], (p2[0] - p1[0]) * math.sqrt(3) / 2 + (p2[1] - p1[1]) * 1/2 + p1[1]

def find_square_vertices(p1, p2):
# Given two points p1 and p2, this functions finds the coordinates of the two remaining vertices of a square.
# Rotates p2 about p1 by +90°, Rotates p1 about p2 by -90° 
    return [-(p2[1]-p1[1]) + p1[0],p2[0]-p1[0] + p1[1]], [(p1[1]-p2[1]) + p2[0],- (p1[0]-p2[0]) + p2[1]]

def draw_line(image, q1, q2, colors):
# draws a black line segment between points p1 and p2
# The line drawing routine is based on https://www.cs.helsinki.fi/group/goa/mallinnus/lines/gsoft2.html?fbclid=IwAR2_has5oFnvuuGkB651cqJBv9pg3LqVK1Tdaym2HMWC6UZynJUpHERKa34
    p1 = [round(q1[0]), round(q1[1])]
    p2 = [round(q2[0]), round(q2[1])]
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    for i in numpy.arange(0.0, 1.0, 0.001):
        pixel = image.get_pixel(p1[0] + round(dx * i), p1[1] + round(dy * i))
        pixel.red = colors[0]
        pixel.green = colors[1]
        pixel.blue = colors[2]

def locate_fraction(p1, p2, f):
# returns coordinates of a point which lies on line p1, p2 and is exactly f * distance(p1,p2) from p1
    return p1[0] + f * (p2[0] - p1[0]), p1[1] + f * (p2[1] - p1[1])
