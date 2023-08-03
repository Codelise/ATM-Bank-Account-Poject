import turtle

# turtle.color('green')
# turtle.forward(100)
# turtle.right(45)
# turtle.color('blue')
# turtle.forward(50)
# turtle.right(45)
# turtle.color('pink')
# turtle.forward(100)

# for loops in turtle
# for steps in range(4):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.color('red')
# turtle.forward(200)

#nested loops
# for steps in range(4):
#      turtle.forward(100)
#      turtle.right(90)
#      for moresteps in range(4):
#           turtle.forward(50)
#           turtle.right(90)

# for steps in range(5):
#     turtle.forward(100)
#     turtle.right(360/5)
#     for moresteps in range(5):
#         turtle.forward(50)
#         turtle.right(360/5)

# nbrSides = 6 # used to divide
# for steps in range(nbrSides):
#     turtle.forward(100)
#     turtle.right(360/nbrSides)
#     for moresteps in range(nbrSides):
#         turtle.forward(50)
#         turtle.right(360/nbrSides)

# accessing the loop value
# for steps in range(4):
#     print(steps)

# for steps in range(1,4):
#     print(steps)

# for steps in range(1,10,2):
#     print(steps)

# for steps in [1,2,3,4,5]:
#     print(steps)

for steps in ['red', 'blue', 'green', 'black']:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(90)
     