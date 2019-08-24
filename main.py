from random import randrange
from tkinter import *


def randBall():
    global ball
    x = randrange(5, HEIGHT - 5)
    y = randrange(5, HEIGHT - 5)
    ball = can.create_oval(x, y, x - 20, y - 20, outline="red", fill="red")
    return x, y


def up(event):
    if (can.coords(ping)[1] > 0):
        can.move(ping, 0, -20)


def down(event):
    if (can.coords(ping)[3] < 500):
        can.move(ping, 0, 20)


def haut(event):
    if (can.coords(pong)[1] > 0):
        can.move(pong, 0, -20)


def bas(event):
    if (can.coords(pong)[3] < 500):
        can.move(pong, 0, 20)


def newGame():
    global score_pong, score_ping, ball

    score_pong = 0
    score_ping = 0
    can.delete(ball)
    randBall()


def update_score():
    global lab_score1, lab_score2
    lab_score1.config(text=str(score_ping))
    lab_score2.config(text=str(score_pong))


def movement():
    global dy, dx, score_ping, score_pong
    if (can.coords(ball)[0] < 0):
        dx *= -1
        score_ping += 1
    elif (can.coords(ball)[2] > WIDTH):
        dx *= -1
        score_pong += 1
    if (can.coords(ball)[3] > HEIGHT or can.coords(ball)[1] < 0):
        dy *= -1
    if len(can.find_overlapping(can.coords(ping)[0], can.coords(ping)[1], can.coords(ping)[2],
                                can.coords(ping)[3])) > 1 or len(
        can.find_overlapping(can.coords(pong)[0], can.coords(pong)[1], can.coords(pong)[2],
                             can.coords(pong)[3])) > 1:
        dx *= -1
    can.move(ball, dx, dy)
    score2.set(str(score_pong))
    score1.set(str(score_ping))

    root.after(5, movement)


HEIGHT = 500
WIDTH = 700
dx = 3
dy = 3
ball = None
score_ping = 0
score_pong = 0

root = Tk()
root.configure(bg="black")
root.title("Ping Pong")
root.resizable(0, 0)
score1 = StringVar()
score2 = StringVar()
top_frame = Frame(root).pack(side=TOP)
bot_frame = Frame(root).pack(side=BOTTOM)

lab_score1 = Label(top_frame, textvariable=score1, font="Times 22 bold").pack(side=RIGHT)
lab_score2 = Label(top_frame, textvariable=score2, font="Times 22 bold").pack(side=LEFT)

can = Canvas(bot_frame, width=WIDTH, height=HEIGHT, bg='black')
can.pack()

ping = can.create_rectangle(685, 170, 695, 230, fill="red")
pong = can.create_rectangle(5, 170, 15, 230, fill="red")

b1 = Button(bot_frame, text='New Game', command=newGame, fg='black')
b1.pack(padx=5, pady=5)

b2 = Button(bot_frame, text='Quit', command=root.destroy, fg='black')
b2.pack(padx=5, pady=5)

randBall()
movement()

root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('<z>', haut)
root.bind('<s>', bas)
root.mainloop()
