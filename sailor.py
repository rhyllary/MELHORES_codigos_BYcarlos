import turtle  

li = turtle.Turtle()    
li.screen.bgcolor("pale turquoise")
li.pensize(2)
li.color("green")
li.left(100)
li.backward(80)
li.speed(6000)
li.shape("turtle")

def love(i):
    if i < 10:
        return
    else:
        li.forward(i)
        li.color("dark violet") 
        li.circle(3)
        li.color("green")
        li.left(30)
        love(3 * i / 4)
        li.right(60)
        love(3 * i / 4)
        li.left(30)
        li.backward(i)

love(60)

def escrever_texto():
    li.penup()
    li.color("dark violet")
    li.goto(-50, -150) 
    li.write("Violetas para ti, Rhyllary", align="center", font=("Arial", 24, "bold"))
    li.hideturtle()

escrever_texto()

def desenhar_passarinho(x, y):
    li.penup()
    li.goto(x, y)
    li.pendown()
    li.color("black")
    li.setheading(60)  
    li.forward(10)
    li.right(120)
    li.forward(10)
    li.left(120)
    li.forward(10)
    li.right(120)
    li.forward(10)
    li.penup()

passarinhos = [(-110, 200), (-40, 220), (0, 210), (30, 230), (90, 215)]
for x, y in passarinhos:
    desenhar_passarinho(x, y)

turtle.done()
