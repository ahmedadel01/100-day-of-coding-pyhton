from turtle import Turtle, Screen
import random

isRaceOn = False

screen = Screen()
screen.setup(width= 500, height=400)
userBet = screen.textinput(title = "Make your bet", prompt= "Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'green', 'yellow', 'blue', 'purple']
yPositions = [-70, -40, -10, 20, 50, 80]
allTurtles = []

for turtleIndex in range(0, 6):
  newTurtle = Turtle(shape="turtle")
  newTurtle.color(colors[turtleIndex])
  newTurtle.penup()
  newTurtle.goto(x = -230, y = yPositions[turtleIndex])
  allTurtles.append(newTurtle)

if userBet:
  isRaceOn = True

while isRaceOn:
  
  for turtle in allTurtles:
    if turtle.xcor() > 230:
      winningColor = turtle.pencolor()
      if winningColor == userBet:
        print(f"You've won! The {winningColor} turtle is the winner!")
        isRaceOn = False
      else:
        print(f"You've lost! The {winningColor} turtle is the winner!")
        isRaceOn = False
    randomDistance = random.randint(0, 10)
    turtle.forward(randomDistance)

screen.exitonclick()
