# turtle graphic draw 

import turtle

t = turtle.Turtle()
t.shape('turtle')
t.color('green')

for _ in range(4):
    t.fd(200)
    t.right(90)
    
t.circle(100)