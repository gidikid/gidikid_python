import turtle
import time


turtle.title("Background Change")

pencil = turtle.Turtle()

pencil.shape("turtle")




pencil.pencolor("#38bc6a")
pencil.fillcolor("#5f3fd1")
pencil.pensize(15)
pencil.speed(1)


pencil.begin_fill()
pencil.circle(100)
pencil.end_fill()

pencil.up()
pencil.fd(190)
pencil.down()

pencil.begin_fill()
pencil.circle(100)
pencil.end_fill()



turtle.mainloop()