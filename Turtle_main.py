import turtle
import random


WIN_WIDTH=500
WIN_HEIGHT=500

window=turtle.Screen()
window.setup(WIN_WIDTH,WIN_HEIGHT)

Bob_the_racer=turtle.Turtle()
Tom_the_racer=turtle.Turtle()
Fred_the_racer=turtle.Turtle()
Creed_the_racer=turtle.Turtle()
Peep_the_racer=turtle.Turtle()

class Racer:

    def __init__(self,turtle):
        self.turtle=turtle

    def move_turtle(self,x,y):

        self.turtle.pencolor("black")

        self.turtle.setx(x)
        self.turtle.sety(y)

        self.turtle.penup()
        self.turtle.left(90)

        self.turtle.pendown()

        sum=0
        k=0
        while (sum<400):
            rand_num=random.randrange(0,5)
            self.turtle.forward(rand_num)
            sum=sum+rand_num
            k=k+1

        return k

    def finish_line(self):


        self.turtle.pencolor("red")
        self.turtle.penup()
        self.turtle.setx(-220)
        self.turtle.sety(200)
        self.turtle.pendown()
        self.turtle.forward(400)

        self.turtle.penup()
        self.turtle.setx(-225)
        self.turtle.sety(205)
        self.turtle.pendown()
        self.turtle.forward(410)

        self.turtle.penup()
        self.turtle.setx(-230)
        self.turtle.sety(210)
        self.turtle.pendown()
        self.turtle.forward(420)

        self.turtle.penup()
        self.turtle.setpos(-100,205)
        self.turtle.write("FINISH!",font=("arial",30,"bold"))

    def penup(self):
        self.turtle.penup()

    def make_turtle(self,x,y):


        self.penup()


        self.turtle.setx(x)
        self.turtle.sety(y)
        self.turtle.pendown()
        t=60

        a=1
        while a<17:
            self.turtle.forward(t)
            t=t-5
            self.turtle.left(90)
            a=a+1


    def shape(self,a):
        return  self.turtle.shape(a)

    def color(self,x):
        return self.turtle.color(x)

    def speed(self,xx):
        return self.turtle.speed(xx)

    def forward(self,xxx):
        return self.turtle.forward(xxx)

    def turn(self):
        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.pendown()




Racer1=Racer(Bob_the_racer)
Racer2=Racer(Tom_the_racer)
Racer3=Racer(Fred_the_racer)
Racer4=Racer(Creed_the_racer)
Racer5=Racer(Peep_the_racer)

Racer1.finish_line()



Racer1.penup()
Racer1.speed(0)
Racer1.color("black")
Racer1.shape("turtle")
Racer1.make_turtle(-200,-200)
Racer1.turn()
#k1=Racer1.move_turtle(-200,-200)




Racer2.penup()
Racer2.speed(0)
Racer2.shape("turtle")
Racer2.color("cyan")
Racer2.make_turtle(-120,-200)
Racer2.turn()
#k2=Racer2.move_turtle(-120,-200)

Racer3.penup()
Racer3.speed(0)
Racer3.color("yellow")
Racer3.shape("turtle")
Racer3.make_turtle(-40,-200)
Racer3.turn()
#k3=Racer3.move_turtle(-40,-200)

Racer4.penup()
Racer4.speed(0)
Racer4.color("orange")
Racer4.shape("turtle")
Racer4.make_turtle(40,-200)
Racer4.turn()
#k4=Racer4.move_turtle(40,-200)

Racer5.penup()
Racer5.speed(0)
Racer5.color("pink")
Racer5.shape("turtle")
Racer5.make_turtle(120,-200)
Racer5.turn()
#k5=Racer5.move_turtle(120,-200)



k1=0
k2=0
k3=0
k4=0
k5=0
while (k1 < 400 and k2 < 400 and k3 < 400 and k4 <400 and k5 < 400):


    rand_num1 = random.randrange(0, 5)
    Racer1.forward(rand_num1)
    k1 = k1 + rand_num1

    rand_num2 = random.randrange(0, 5)
    Racer2.forward(rand_num2)
    k2 = k2 + rand_num2


    rand_num3 = random.randrange(0, 5)
    Racer3.forward(rand_num3)
    k3 = k3 + rand_num3


    rand_num4 = random.randrange(0, 5)
    Racer4.forward(rand_num4)
    k4 = k4 + rand_num4

    rand_num5 = random.randrange(0, 5)
    Racer5.forward(rand_num5)
    k5 = k5 + rand_num5



if k1>=k2 and k1>=k3 and k1>=k4 and k1>=k5:
    print("THE FIRST TURTLE IS THE FASTEST, AND IT MADE {} STEPS ".format(k1))
elif k2>=k1 and k2>=k3 and k2>=k4 and k2>=k5:
    print("THE SECOND TURTLE IS THE FASTEST, AND IT MADE {} STEPS ".format(k2))
elif k3>=k1 and k3>=k2 and k3>=k4 and k3>=k5:
    print("THE THIRD TURTLE IS THE FASTEST, AND IT MADE {} STEPS ".format(k3))
elif k4>=k1 and k4>=k2 and k4>=k3 and k4>=k5:
    print("THE FOURTH TURTLE IS THE FASTEST, AND IT MADE {} STEPS ".format(k4))
else:
    print("THE FIFTH TURTLE IS THE FASTEST, AND IT MADE {} STEPS ".format(k5))

if k1<=k2 and k1<=k3 and k1<=k4 and k1<=k5:
    print("THE FIRST TURTLE IS THE SLOWEST, AND IT MADE {} STEPS ".format(k1))
elif k2<=k1 and k2<=k3 and k2<=k4 and k2<=k5:
    print("THE SECOND TURTLE IS THE SLOWEST, AND IT MADE {} STEPS ".format(k2))
elif k3<=k1 and k3<=k2 and k3<=k4 and k3<=k5:
    print("THE THIRD TURTLE IS THE SLOWEST, AND IT MADE {} STEPS ".format(k3))
elif k4<=k1 and k4<=k2 and k4<=k3 and k4<=k5:
    print("THE FOURTH TURTLE IS THE SLOWEST, AND IT MADE {} STEPS ".format(k4))
else:
    print("THE FIFTH TURTLE IS THE SLOWEST, AND IT MADE {} STEPS ".format(k5))

print(k1,k2,k3,k4,k5)

