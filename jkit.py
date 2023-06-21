# python program to draw a smile
# face emoji using turtle 
import turtle

# turtle object
pencil = turtle.Turtle() # how we create a pencil to draw with

# draw face
pencil.fillcolor('blue') # allows us to add colours ]
# our shapes/drawings | picked up a crayon

pencil.begin_fill() # we use pencil.begin_fill() to
# start colouring

# (100) saying how big the circle should be
# (radius)
pencil.circle(100) # what we have under pencil.begin_fill() is what turtle would 
#color for us using the color we specified
pencil.end_fill() #means that turtle should stop coloring now
pencil.up()


# function if creation of eye
def eye (col, radius) :
    pencil.down()
    pencil.fillcolor(col)
    pencil.begin_fill()
    pencil.circle(radius)
    pencil.end_fill()
    pencil.up()
    
# draw eyes
pencil.goto(-40, 120)
eye('white', 15)
pencil.goto(-37, 125)
eye('black', 5)
pencil.goto(40, 120)
eye('white', 15) 
pencil.goto(40, 125)
eye('black', 5)

# draw nose
pencil.goto( 0, 75)
eye('black', 8)

# draw mouth
pencil.goto(-40, 85)
pencil.down()
pencil.right(90)
pencil.circle(40, 180)
pencil.up()

# draw tongue
pencil.goto(-10, 45)
pencil.down()
pencil.right(180)
pencil.fillcolor('red')
pencil.begin_fill()
pencil.circle(10, 180)
pencil.end_fill()
pencil.hideturtle()



turtle.mainloop()






