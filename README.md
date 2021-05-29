# Koch-Snowflake
Final Project Code in Place 2021

I attended [Code in Place 2021](https://codeinplace.stanford.edu/) which is an intro-to-coding course built off the first half of one of most popular courses at Stanford University (CS106A). Koch Snowflake is my final project for the course which I wrote in Python. 

## What is Koch Snowflake?
[Koch Snowflake](https://en.wikipedia.org/wiki/Koch_snowflake) is a fractal - that is an image which can be built up iteratively. Koch snowflake starts as an equilateral triangle. Then in each step every segment is divided into three parts where the middle part is replaced by two sides of a smaller equilateral triangle. And this process repeats over and over again.

The image below is Koch Snowflake which my program ([koch.py](koch.py)) draws if the user asks for 1000 by 1000 pixels and 5 iterations.
![koch 1000 5 github](https://user-images.githubusercontent.com/84993454/120040077-d008ec00-bfba-11eb-8992-e21917709d05.JPG)

## Library my_geometry.py
To produce such images, I used the [simpleimage](https://codeinplace2021.github.io/pythonreader/en/images/) library which we learned during Code in Place. I also wrote my own library ([my_geometry.py](my_geometry.py)) which includes functions such as 
* draw a line segment with given endpoints
* find third vertex of an equilateral triangle
* locate one third and two thirds on a given segment

## Recursive approach
I designed a recursive function `iterate_triangle()`. This function calls itself repeatedly on smaller and smaller segments and includes the number of steps that have been computed so far as a parameter.


## Koch Anti-slowflake
I further adapted the basic snowflake by drawing the triangles in each step inwards as opposed to outwards which produces a structure known as anti-snowflake.
![koch anti 1000 5 github](https://user-images.githubusercontent.com/84993454/120042320-b10c5900-bfbe-11eb-8142-be3968d0076c.JPG)


## Generalization - squares
Finally, I applied the same iterative concept on squares instead of triangles by replacing middle quarter of each segment by a square.
![koch square 1000 6 github](https://user-images.githubusercontent.com/84993454/120042326-b4074980-bfbe-11eb-9b15-c644438a1f56.JPG)


