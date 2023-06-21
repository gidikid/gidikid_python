import turtle
import time


turtle.title("Background Change")

pencil = turtle.Turtle()

pencil.shape("turtle")




pencil.pencolor("blue")
pencil.pensize(15)
pencil.speed(1)


pencil.circle(90)


pencil.up()
pencil.fd(100)
pencil.down()


pencil.circle(90)


pencil.pencolor("black")
pencil.pensize(15)
pencil.speed(1)



pencil.circle(90)

pencil.up()
pencil.fd(190)
pencil.down()

pencil.pencolor("red")
pencil.pensize(15)
pencil.speed(1)



pencil.circle(90)

pencil.up()
pencil.fd(190)
pencil.down()



turtle.mainloop()