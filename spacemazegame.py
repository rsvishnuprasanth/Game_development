import turtle

rocket=turtle.Turtle()
spaceman=turtle.Turtle()
space=turtle.Screen()

space.addshape("Spaceman.gif")
spaceman.shape("Spaceman.gif")
spaceman.penup()
spaceman.goto(-103,255)

space.bgpic("Maze_background.gif")
space.addshape("Rocket.gif")
rocket.shape("Rocket.gif")
rocket.penup()
rocket.goto(180,-250)
rocket.speed(5000)


def up():
    rocket.setheading(90)
    rocket.forward(10)
    rocket.setheading(0)

def down():
    rocket.setheading(270)
    rocket.forward(10)
    rocket.setheading(0)

def left():
    rocket.setheading(180)
    rocket.forward(10)
    rocket.setheading(0)

def right():  
    rocket.forward(10)
  
turtle.listen()

turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")


while True:
    space.update()
    if rocket.distance(spaceman)<10:
        space.bgpic("winning_game.gif")

turtle.done()