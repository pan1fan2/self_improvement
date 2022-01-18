import turtle
# from typing import ForwardRef
t = turtle.Turtle()
# def drawSpiral(t,linelen):
#     if linelen > 0 :
#         t.forward(linelen)
#         t.right(90)
#         drawSpiral(t,linelen - 5)

# drawSpiral(t,100)
# turtle.done()


for i in range(0,3):
    t.forward(100)
    t.left(120)
    t.backward(100)
    if i ==1:
        break
turtle.done()