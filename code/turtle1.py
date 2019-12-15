import turtle

p = turtle.Pen()

p.color('red','yellow')
p.begin_fill()
while True:
       p.forward(200)
       p.left(170)
       if abs(p.pos()) < 1:
            break
p.end_fill()
turtle.exitonclick()
