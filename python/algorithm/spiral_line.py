import turtle
t = turtle.Turtle()
def drawSpiral(t,linelen):
    if linelen > 0 :
        t.forward(linelen)
        t.right(90)
        drawSpiral(t,linelen - 5)

drawSpiral(t,100)
turtle.done()