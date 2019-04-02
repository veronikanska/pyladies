import turtle

t = turtle.Turtle()


def tree(length = 100):

    if length < 10:
        return
    t.forward(length)
    t.left(30)
    tree(length *.7)
    t.right(60)
    tree(length * .7)
    t.left(30)
    t.backward(length)
    return


tree()

turtle.done()