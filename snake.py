

import turtle
import time
import random

delay = 0.1
score=0
high_schore=0


# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @RAHAF")
wn.bgcolor("antiquewhite")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates



# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("saddlebrown")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("chocolate")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("saddlebrown")
food.penup()
food.goto(0,100)

segments = []





# Functions
def go_up():
    if head.direction!='down':
        head.direction = "up"

def go_down():
    if head.direction !='up':
        head.direction = "down"

def go_left():
    if head.direction !='right':
        head.direction = "left"

def go_right():
    if head.direction!='left':
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen() 

wn.onkeypress(go_up,'Up')         

wn.onkeypress(go_down,'Down')         

wn.onkeypress(go_left,'Left')         

wn.onkeypress(go_right,'Right') 


# Main game loop
while True:
    wn.update()

    ##chick for a collosion with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'
       #hide the segment
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segments list
        segments.clear()
        #cleat the score
        score=0
        pen.clear()
        pen.write('score = {}   high score = {}'.format(score,high_schore), align="center", font=("Courier", 24, "normal"))    




        


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("burlywood")
        new_segment.penup()
        segments.append(new_segment)



        # shorten the delay
        delay-=0.001

        ## increase the score
        score+=10
        if score>high_schore:
            high_schore=score
        pen.clear()
        pen.write('score = {}   high score = {}'.format(score,high_schore), align="center", font=("Courier", 24, "normal"))    

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()    

    # Check for head collision with the body segments
    for segment in segments:

        if segment.distance(head)< 20:
            time.sleep(1)
            head.goto(0,0)
               #hide the segment
            for segment in segments:
                segment.goto(1000,1000)



        # Clear the segments list
            segments.clear()
        # cleat the score
            pen.clear()
            #reset the score
            score=0
            #reset the delay
            delay=0.1

            pen.write('score = {}   high score = {}'.format(score,high_schore), align="center", font=("Courier", 24, "normal"))    


        

    time.sleep(delay)

wn.mainloop()
