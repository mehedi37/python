import turtle
import time

screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=111)
squary = turtle.Turtle()
squary.speed(100)

for i in range(500):
    squary.forward(i)
    squary.left(91)


style = ('Arial', 40, 'italic')
shadow = ('Arial', 40, 'italic', 'bold')
turtle.color('#000')
turtle.write('Mehedi', font = shadow, align='center')
turtle.color('#00ff55')
turtle.write('Mehedi', font=style, align='center')
turtle.hideturtle()
time.sleep(5)
