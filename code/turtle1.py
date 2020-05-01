import turtle

p = turtle.Pen()
p.speed(0)
p.color('red','yellow')
p.up();p.backward(250); p.down()
p.begin_fill()
c = 1
while c <= 300:
       p.forward(500)
       p.left(170)
       c += 1
p.end_fill()
turtle.exitonclick()
