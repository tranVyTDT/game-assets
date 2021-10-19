#imports
import turtle
import time
import random

# turtle.register_shape("bruh.gif")
turtle.register_shape("16_burger_dish.gif")
turtle.register_shape("50_giantgummybear.gif")
turtle.register_shape("74_omlet_dish.gif")
turtle.register_shape("41_eggsalad_bowl.gif")
turtle.register_shape("52_gingerbreadman.gif")
turtle.register_shape("54_hotdog.gif")
turtle.register_shape("57_icecream.gif")
turtle.register_shape("60_jelly_dish.gif")
turtle.register_shape("86_roastedchicken_dish.gif")
turtle.register_shape("87_ramen.gif")
turtle.register_shape("101_waffle.gif")
turtle.register_shape("44_frenchfries.gif")
turtle.register_shape("47_fruitcake_dish.gif")
turtle.register_shape("49_garlicbread_dish.gif")
turtle.register_shape("18_burrito.gif")
turtle.register_shape("72_nacho_dish.gif")
turtle.register_shape("76_pudding_dish.gif")
turtle.register_shape("26_chocolate.gif")
turtle.register_shape("29_cookies_dish.gif")
turtle.register_shape("38_friedegg.gif")
turtle.register_shape("60_jelly_dish.gif")
turtle.register_shape("61_jam.gif")

delay=0.1

shapes=(
    "61_jam.gif",
    "60_jelly_dish.gif",
    "38_friedegg.gif",
    "29_cookies_dish.gif",
    "26_chocolate.gif",
    "72_nacho_dish.gif",
    "76_pudding_dish.gif",
    "18_burrito.gif",
    "49_garlicbread_dish.gif",
    "47_fruitcake_dish.gif",
    "44_frenchfries.gif",
    "101_waffle (1).gif",
    "87_ramen.gif",
    "86_roastedchicken_dish.gif",
    "60_jelly_dish.gif",
    "57_icecream.gif",
    "54_hotdog.gif",
    "52_gingerbreadman.gif",
    "41_eggsalad_bowl.gif",
    "74_omlet_dish.gif",
    "50_giantgummybear.gif",
    "16_burger_dish.gif")
#điểm
score=0
high_score=0

hs=open("h_s.txt", "r+")
high_score = int(hs.readline())
hs.close()

#thiết lập màn hình
wn=turtle.Screen()
wn.title("Snake Game")
#wn.bgpic("C:/Users/HP/3D Objects/bài cuối khóa/241197269_407748587380064_7625747773453388800_n.png")
wn.bgcolor('yellow')
wn.setup(width=1000, height=1000)
wn.tracer(0)

#đầu rắn
head = turtle.Turtle()
head.speed(3)
head.shape("bruh.gif")
#head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#đồ ăn cho rắn
foods=[]
for _ in range(random.randint(2,4)):
    food = turtle.Turtle()
    food.speed(0)
    food.shape("61_jam.gif")
    food.penup()
    food.goto(random.randint(-200,200), random.randint(-200,200))
    foods.append(food)

segments=[]

#bảng điểm
sc = turtle.Turtle()
sc.write("score: {} High score: {}".format(score,high_score), align="center", font=("ds-digital",30,"normal"))
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
#sc.write("score: 0 High score: 0",align="center",font=("ds-digital", 30,"normal"))

#functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction !="up":
        head.direction = "down"
def go_left():
    if head.direction !="right":
        head.direction = "left"
def go_right():
    if head.direction !="left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#phím
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#vòng lặp chính:D
while True:
    wn.update()
    
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        if head.direction == "stop":
            if score > high_score:
                s_=open("h_s.txt","w")
                high_score = score
                s_.write(str(score))
                s_.close()
            
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        delay = 0.1

        
        sc.clear()        
        sc.write("score: {} High score: {}".format(score,high_score), align="center", font=("ds-digital",30,"normal"))

    for food in foods:             
        if head.distance(food) <20:

            food.shape(random.choice(shapes))     
            x = random.randint(-190,190)
            y = random.randint(-190,190)
            food.goto(x,y)

            new_segment=turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("black")
            new_segment.penup()
            segments.append(new_segment)

            delay -= 0.001
            score += 1

            hs.close()
            sc.clear()
            sc.write("score: {} High score: {}".format(score,high_score),align="center", font=("ds-digital",30,"normal"))

    
    
#:))
    for index in range(len(segments)-1,0,-1):
        x= segments[index-1].xcor()
        y= segments[index-1].ycor()
        segments[index].goto(x,y)
#:D
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()
                 
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            if head.direction == "stop":
                if score > high_score:
                    c=open("h_s.txt","w")
                    high_score = score
                    c.write(str(score))
                    c.close()

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
                 
            score=0
            delay=0.1
                 
            sc.clear()
            sc.write("score: {} High score: {}".format(score,high_score), align="center", font=("ds-digital",30,"normal"))
    time.sleep(delay)
wn.mainloop()
