import turtle

pen = turtle.Turtle()

shape = input("what shape do you want. do you want a pentagon,circle,star or triangle")
colour = input("what coulor do you want your shape")

if shape == 'circle':
    pen.fillcolor(colour)
    pen.begin_fill()
    pen.circle(110)
    pen.end_fill
    pen.up()
    
turtle.mainloop()
    
    