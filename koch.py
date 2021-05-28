from simpleimage import SimpleImage
import math 
import my_geometry

INITIAL_COLOR = [200, 200, 150]

def place_triangle_base(size, direction):
# Returns coordinates of the vertices that form the horizontal side of an equilateral triangle based on the size of the image. (The triangle is pointing down: \-/ )
    if direction == 'out':
        return [round(size * 1 / 6), round(size / 3)], [round(size * 5 / 6), round(size / 3)]
    else:
        return [round(size * 1 / 6), round(size * 0.21)], [round(size * 5 / 6), round(size * 0.21)]


def place_square_base(size, direction):
# Returns coordinates of the vertices that form the top horizontal side of a square based on the size of the image.
    if direction == 'out':
        return [round(size * 1 / 4), round(size * 1 / 4)], [round(size * 3 / 4), round(size * 1 / 4)]
    else:
        return [round(size * 1 / 8), round(size * 1 / 8)], [round(size * 7 / 8), round(size * 1 / 8)]

def iterate_triangle(image, p1, p2, step, steps, colors):
# recursive function 
# in each step, segment p1, p2 is replaced by 4 segments between consecutive points p1, q1, q, q2, p2 in the following way: ___ becomes _/\_
    if step < steps:
        step += 1
        q1 = my_geometry.locate_fraction(p1, p2, 1 / 3)
        q2 = my_geometry.locate_fraction(p1, p2, 2 / 3)
        q = my_geometry.find_triangle_vertex(q1, q2)
        scale = 1 - 0.5 ** step # makes big changes in the first few steps, the changes are less visible as step increases
        new_colors = [round(colors[0] * scale),round(colors[1]), round(colors[2])] # reduces red 
        iterate_triangle(image, p1, q1, step, steps, new_colors)
        new_colors = [round(colors[0]), round(colors[1] * scale),round(colors[2])] # reduces green
        iterate_triangle(image, q1, q, step, steps, new_colors)
        iterate_triangle(image, q, q2, step, steps, new_colors)
        new_colors = [round(colors[0]*scale),round(colors[1]),round(colors[2])] # reduces red
        iterate_triangle(image, q2, p2, step, steps, new_colors)
    else:
    # the recursive function only draws the segments in the last step
        my_geometry.draw_line(image, p1, p2, colors)

def iterate_square(image, p1, p2, step, steps, colors):
# recursive function 
# in each step, segment p1, p2 is replaced by 4 segments between consecutive points p1, q1, q3, q4, q2, p2 in the following way: ___ becomes _|-|_
    if step < steps:
        step += 1
        q1 = my_geometry.locate_fraction(p1, p2, 3 / 8)
        q2 = my_geometry.locate_fraction(p1, p2, 5 / 8)
        q3, q4 = my_geometry.find_square_vertices(q1, q2)
        scale = 1 - 0.5 ** step # makes big changes in the first few steps, the changes are less visible as step increases
        new_colors = [round(colors[0]),round(colors[1] * scale), round(colors[2])] # reduces green
        iterate_square(image, p1, q1, step, steps, new_colors)
        new_colors = [round(colors[0]),round(colors[1]),round(colors[2]*scale)] # reduces blue
        iterate_square(image, q1, q3, step, steps, new_colors)
        iterate_square(image, q3, q4, step, steps, new_colors)
        iterate_square(image, q4, q2, step, steps, new_colors)
        new_colors = [round(colors[0]*scale),round(colors[1] * scale),round(colors[2])] # reduces green
        iterate_square(image, q2, p2, step, steps, new_colors)
    else:
    # the recursive function only draws the segments in the last step
        my_geometry.draw_line(image, p1, p2, colors)

def construct_koch_triangle(size,steps, direction):
# places the initial triangle and calls the recursive function iterate_triangle
    image = SimpleImage.blank(size, size)
    p1, p2 = place_triangle_base(size, direction)
    p = my_geometry.find_triangle_vertex(p1, p2)
    if direction == 'out':
        # snowflake
        iterate_triangle(image, p2, p1, 0, steps, INITIAL_COLOR)
        iterate_triangle(image, p1, p, 0, steps, INITIAL_COLOR)
        iterate_triangle(image, p, p2, 0, steps, INITIAL_COLOR)
    else:
        #anti-snowflake
        iterate_triangle(image, p1, p2, 0, steps, INITIAL_COLOR)
        iterate_triangle(image, p, p1, 0, steps, INITIAL_COLOR)
        iterate_triangle(image, p2, p, 0, steps, INITIAL_COLOR)
    return image

def construct_koch_square(size, steps, direction):
# places the initial square and calls the recursive function iterate_square
    image = SimpleImage.blank(size, size)
    p1, p2 = place_square_base(size, direction)
    p3, p4 = my_geometry.find_square_vertices(p1, p2)
    if direction == 'out':
        # square outwards
        iterate_square(image, p2, p1, 0, steps, INITIAL_COLOR)
        iterate_square(image, p1, p3, 0, steps, INITIAL_COLOR)
        iterate_square(image, p3, p4, 0, steps, INITIAL_COLOR)
        iterate_square(image, p4, p2, 0, steps, INITIAL_COLOR)
    else:
        # square inwards
        iterate_square(image, p1, p2, 0, steps, INITIAL_COLOR)
        iterate_square(image, p3, p1, 0, steps, INITIAL_COLOR)
        iterate_square(image, p4, p3, 0, steps, INITIAL_COLOR)
        iterate_square(image, p2, p4, 0, steps, INITIAL_COLOR)
    return image

def construct_square_with_triangular_iteration(size, steps, direction):
# outlines the initial square and calls the recursive function iterate_triangle
    image = SimpleImage.blank(size, size)
    p1, p2 = place_square_base(size, direction)
    p3, p4 = my_geometry.find_square_vertices(p1, p2)
    if direction == 'out':
        # triangle outwards
        iterate_triangle(image, p2, p1, 0, steps, INITIAL_COLOR)
        iterate_triangle(image, p1, p3, 0, steps, INITIAL_COLOR)
        iterate_triangle(image, p3, p4, 0, steps, INITIAL_COLOR)
        iterate_triangle(image, p4, p2, 0, steps, INITIAL_COLOR)
    else:
        # triangle inwards
        iterate_triangle(image, p1, p2, 0, steps, INITIAL_COLOR)
        iterate_triangle(image, p3, p1, 0, steps, INITIAL_COLOR)
        iterate_triangle(image, p4, p3, 0, steps, INITIAL_COLOR)
        iterate_triangle(image, p2, p4, 0, steps, INITIAL_COLOR)
    return image

def main():
    size = int(input('Enter the side-length of the square image in pixels. '))
    steps = int(input('Enter the number of iterations. '))
    direction = input('Type in or out. ')
    while not (direction == 'in' or direction == 'out'):
        direction = input('Try again. You should type either in or out. ')
    shape = input('Type 3 for triangle, 4 for square or any other key for a surprise. ')
    if shape == '3':
        img = construct_koch_triangle(size, steps, direction)
    elif shape == '4':
        img = construct_koch_square(size, steps, direction)
    else:
        img = construct_square_with_triangular_iteration(size, steps, direction)
    img.show()


if __name__ == '__main__':
        main()
