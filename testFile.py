import turtle

turtle = turtle.Turtle()

def right():
  turtle.right(90)
  turtle.forward(50)

def left():
  turtle.left(90)
  turtle.forward(50)

def forward():
  turtle.forward(50)

def backward():
  turtle.backward(50)

def play(health, power):
  print "Health: ", health
  print "Power: ", power
  
  direction = raw_input ("Which direction would you like to go? (right, left, forward, backward)")
  
  if(direction == "right"):
    print "You forced the turtle to walk 50 centimeters."

    right()

    play(health, power - 10)

  elif(direction == "left"):
    print "The turtle walked 50.1 centimeters and broke the world record for the longest distance ever walked by a turtle!"

    left()

    play(health, power - 10)

  elif(direction == "forward"):
    print "The turtle encountered another turtle and moved forward. The other turtle countered with move forward. Both took a lot of damage. "

    forward()

    play(health - 50, power - 10)

  elif (direction == "backward"):
    print "Turtle learned backward!"
    backward()

    play(health, power - 15)

  else: 
    print "Turtle somehow flipped himself over and is unable to move. Game Over."

play(100, 50)




