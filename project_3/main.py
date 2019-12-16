"""
    Isaac Ingles
    CS 1400 
    Fall 2019

    Project 3 -- Turtle Tesselation

"""

import turtle

""" 

Start in the top lefthand corner (Uses Cartesian Coordinates)
where 0,0 is the center of the screen; so these numbers are somewhat
arbitrary; this will be affected by screen size.
 
"""
x = -300
y = 150

#number of rows
#number of shapes per row
#size of the hexagon

rows = int( input("Enter the number of rows: ") )
shapes = int( input("Enter the number of shapes per row: ") )
hexSize = int( input("Enter the size of one side of the shape: ") )

#keep turtle names simple :)
t = turtle.Turtle()
u = turtle.Turtle()

t.speed(10)
u.speed(10)
# Use the color/fill methods that ship with Turtle
t.color('red')
u.color('orange')
t.fillcolor('yellow')
u.fillcolor('blue')

for i in range(rows):
  t.up()
  u.up()
  # One side of a hexagon is 2 * the square root of 3
  y = y - (hexSize * (3 ** 0.5))
  """ 
  Shift position of hexagons on every other row to make triangles in between
  Multiply the hex size by the side length (which is 2 * square root of 3)
  Round to prevent offset problems 
  
  """
  
  if(i % 2 == 0):
    x += hexSize * round((3**0.5) / 2)
  else: x -= hexSize * round((3**0.5) / 2)
  #goto method that ships with Turtle; go to x,y on the coordinate plane
  t.goto(x,y)
  u.goto(x + hexSize,y)
  t.down()
  u.down()
  for j in range(shapes):
    t.up()
    u.up()
    t.forward(hexSize * 2)
    u.forward(hexSize * 2)
    t.down()
    u.down()

    #Fill method that ships with Turtle
    t.begin_fill()
    u.begin_fill()
    #draw the hexagon here (six sides, angle of 60 degrees)
    for k in range(6):      
      t.forward(hexSize)
      t.left(60)
      
    #draw the triangles here
    for l in range(3): 
      if(i < rows - 1):
        #Keep from drawing an unused row of triangles
        u.left(60)
        u.forward(hexSize)
        u.right(120)
        u.forward(hexSize)
  
        u.right(120)
        u.forward(hexSize)

        u.up()
        u.left(60)
        u.forward(hexSize)
        u.right(120)
        u.forward(hexSize)
        u.down()
 

    t.end_fill()
    u.end_fill()
turtle.done() 






