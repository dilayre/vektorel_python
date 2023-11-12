import turtle

def kareciz():
    for a in range(4):
        turtle.forward(100)
        turtle.right(90)

def ucgenciz():
    for a in range(3):
        turtle.forward(100)
        turtle.left(120)

        
def besgenciz():
    for a in range(5):
        turtle.forward(100)
        turtle.left(72)


def cokgenciz(ks,buyukluk):
    for b in range(ks):
        turtle.forward(buyukluk)
        turtle.right(360/ks)

cokgenciz(9,200)
