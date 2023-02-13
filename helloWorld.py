# create new env -> python3 -m venv .venv
# activate enviroment -> source .venv/bin/activate
#deactivate enviroment -> deactive

import turtle

wn = turtle.Screen()
wn.title('Pong by ZerpaCode')
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #prevent window for update (improve program speed)

# Score
score_a = 0
score_b = 0

def monitorBallBorderCollision(ball):
    global score_a,score_b #telling the function to use this global variables instead of create new local variables 
        #border checking
        #Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

def handlePaddleBallCollission(ball):
        if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1 
        elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1

class Paddle():
    shape="square"

    def __init__(self, positionx, positiony, color):
        self.positionx=positionx
        self.positiony=positiony
        self.color=color
        
    def initPaddle(self):
        paddle = turtle.Turtle()
        paddle.speed(0) #animation speed = max posible
        paddle.shape(self.shape)
        paddle.color(self.color)
        paddle.shapesize(stretch_wid=5, stretch_len=1) # width*5 and length*1 (width is vert and length is horizontal)
        paddle.penup() #avoid draw a lign when Turtle moves
        paddle.goto(self.positionx, self.positiony) # x and y position
        return paddle
    

class Ball():
    def __init__(self, initx, inity, color, shape, speed=.1):
        self.initx=initx
        self.inity=inity
        self.color=color
        self.shape=shape
        self.speed=speed
        
    def initBall(self):
        ball = turtle.Turtle()
        ball.speed(0) #animation speed = max posible
        ball.shape(self.shape)
        ball.color(self.color)
        ball.penup() #avoid draw a lign when Turtle moves
        ball.goto(self.initx, self.inity) # x and y position
        ball.dx = self.speed #custom prop -> delta x position (delta means change)
        ball.dy = self.speed #custom prop -> delta x position (delta means change)
        return ball



#Paddles
paddle_a = Paddle(-350, 0, 'green').initPaddle()
paddle_b = Paddle(350, 0, 'purple').initPaddle()


#Ball
ball = Ball(0,0, 'orange', 'circle').initBall()

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#Actions
def padle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def padle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def padle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def padle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(padle_a_up, "w")
wn.onkeypress(padle_a_down, "s")
wn.onkeypress(padle_b_up, "Up")
wn.onkeypress(padle_b_down, "Down")

#Main game loop (this is like javascript requestAnimationFrame)
while True:
    wn.update()
    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    monitorBallBorderCollision(ball)
    handlePaddleBallCollission(ball)

    


