import turtle
#create a window
wn=turtle.Screen()
#set text to window title
wn.title(":::PING PONG GAME:::")
#set back-color
wn.bgcolor("black")
#set size of window
wn.setup(width=800,height=600)
#
wn.tracer(0)
#first paddle
paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(4.0,0.90)


paddle1.penup()
paddle1.goto(-350,0)
#second paddle
paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(4.0,0.90)


paddle2.penup()
paddle2.goto(350,0)
#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(0.9,0.9)
ball.penup()
# delta - x- y
ball.dx=0.4
ball.dy=0.4

#score system
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-40,260)
pen.write("PLAYER 1 : 0 || PLAYER 2 : 0")

#functions 
def paddle1Up():
    #set 'y' to a variable
    y=paddle1.ycor()
    #y++
    y+=20
    paddle1.sety(y)

def paddle1Down():
    #set 'y' to a variable
    y=paddle1.ycor()
    #y--
    y-=20
    paddle1.sety(y)

def paddle2Up():
    #set 'y' to a variable
    y=paddle2.ycor()
    #y++
    y+=20
    paddle2.sety(y)
def paddle2Down():
    #set 'y' to a variable
    y=paddle2.ycor()
    y-=20
    paddle2.sety(y)
#Keyboard events
#keyboard listenin'
wn.listen()
#set event which is keypress params 
wn.onkeypress(paddle1Up,"w")
wn.onkeypress(paddle1Down,"s")
wn.onkeypress(paddle2Up,"Up")
wn.onkeypress(paddle2Down,"Down")

#scores
paddle1_score=0
paddle2_score=0

#Main game loop
while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    if paddle1.ycor()>300:
        paddle1.sety(290-50)
    if paddle2.ycor()>300:
        paddle2.sety(290-50)
    if paddle1.ycor()<-300:
        paddle1.sety(-290+50)
    if paddle2.ycor()<-300:
        paddle2.sety(-290+50)
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy+=-0.25
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy+=+0.25
    if ball.xcor()>390:
        ball.setx(390)
        ball.dx+=-0.25
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx+=+0.25
    if ball.xcor()>340 and ball.ycor()<paddle2.ycor()+50 and ball.ycor()>paddle2.ycor()-50:
        ball.dx=-ball.dx
    if ball.xcor()<-340 and ball.ycor()>paddle1.ycor()-50 and ball.ycor()<paddle1.ycor()+50:
        ball.dx=-ball.dx
    if ball.xcor()>paddle2.xcor()+20:
        paddle1_score+=1
        ball.goto(0,0)
        pen.clear()
        pen.write("PLAYER 1: {0} || PLAYER 2: {1}".format(paddle1_score,paddle2_score))
        ball.dx=-ball.dx
    if ball.xcor()<paddle1.xcor()-20:
        paddle2_score+=1
        ball.goto(0,0)
        pen.clear()
        ball.dx=-ball.dx
        pen.write("PLAYER 1: {0} || PLAYER 2: {1}".format(paddle1_score,paddle2_score))