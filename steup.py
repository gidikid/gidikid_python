import turtle
import time
turtle.title("Background Change")
pen = turtle.Turtle()
pen.shape("turtle")



for i in range(10):
     turtle.bgcolor("red")
     time.sleep(1)
     turtle.bgcolor("green")
     time.sleep(1)
     turtle.bgcolor("purple")
     time.sleep(1)
          
     
turtle.mainloop()    