'''
Fern L-System
By Cameron Cassells

An implementation of an L-system for a fern found in Przemyslaw Prusinkiewicz & 
Aristid Lindenmayer's book "The Algorithmic Beauty of Plants".

V = {X,F,+,-,[,]}
ω = X
P = {(X→F+[[X]-X]-F[-FX]+X),(F→FF)}
n = 8
δ = 22.5
'''

import turtle

#Creation Parameters
GENERATION = 8
LENGTH = 2
ANGLE = 22.5
AXIOM = "X"

#Placement Parameters
INIT_X = -650
INIT_Y = -450
INIT_HEADING = 45

#Generate string according to rules
for _ in range(GENERATION):
    temp_string = ""
    for char in AXIOM:
        if char == 'X':
            temp_string += "F+[[X]-X]-F[-FX]+X"
        elif char == 'F':
            temp_string += "FF"
        else:
            temp_string += char
    AXIOM = temp_string

print(AXIOM)

#Initialise canvas
window = turtle.Screen()
window.title("ABOP Fern")
window.bgcolor("#222222")
window.tracer(0) #Comment out to see drawing

t = turtle.Turtle()
t.pencolor("#adff00")
t.speed("fastest")
t.hideturtle()

t.penup()
t.setposition(INIT_X, INIT_Y)
t.setheading(INIT_HEADING)
t.pendown()

#Draw plant
stack = []

for char in AXIOM:
    if char == 'X':
        continue
    elif char == 'F':
        t.forward(LENGTH)
    elif char == '+':
        t.left(ANGLE)
    elif char == '-':
        t.right(ANGLE)
    elif char == '[':
        stack.append((t.position(), t.heading()))
    elif char == ']':
        position, heading = stack.pop()
        t.penup()
        t.setposition(position)
        t.setheading(heading)
        t.pendown()

window.update()
window.mainloop()
