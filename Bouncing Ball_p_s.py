import turtle,time
wn=turtle.Screen()
turtle.tracer(2)
wn.setup(1000,1000,100,0)
wn.bgcolor('black')
ball=turtle.Turtle('circle')
box=turtle.Turtle()
ball.turtlesize(1)
ball.hideturtle()
ball.color('white')
ball.penup()
box.hideturtle()
box.pensize(20)
box.penup()
length=200
box.goto(-length,length)
box.pendown()
box.color('white')
for m in range(4):
    box.fd(2*length)
    box.right(90)
ball.goto(-2*length,2*length)
dx,dy=3,1.7
X,Y=50,50
ball.showturtle()

while True:
    wn.update()
    time.sleep(0.03)
    ball.goto(X+dx,Y+dy)
    X,Y=ball.xcor(),ball.ycor()
    if X<-length+20:
        ball.setx(-length+20)
        dx=dx*-1 
    if X>(length-20):
        ball.setx(length-20)
        dx=dx*-1              
    if Y<-length+20:
        ball.sety(-length+20)
        dy=dy*-1
    if Y>(length-20):
        ball.sety(length-20)
        dy=dy*-1
    

