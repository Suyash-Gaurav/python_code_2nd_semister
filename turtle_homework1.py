import turtle


def consec_rec():
    t1 = turtle.Turtle()
    t1.bk(90)
    for g in range(4):
        for i in range(4):
            t1.pensize(5)
            t1.forward(45)
            t1.left(90)
        t1.up()
        t1.forward(60)
        t1.down()
    t1.hideturtle()


def four_rec():
    n = 100
    t2 = turtle.Turtle()
    for g in range(4):
        for i in range(4):
            t2.pensize(5)
            t2.color('purple')
            t2.forward(n)
            t2.left(90)
        t2.up()
        t2.forward(10)
        t2.left(90)
        t2.forward(10)
        t2.right(90)
        t2.down()
        n = n - 20
    t2.hideturtle()


four_rec()
consec_rec()