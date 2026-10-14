"""Pong für das Git-Labor. Start: python pong.py"""
import tkinter as tk

WIDTH, HEIGHT = 640, 360
PADDLE_STEP = 222

window = tk.Tk()
window.title("Pong | Git-Labor")
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="#111827", highlightthickness=0)
canvas.pack()
canvas.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="#475569", dash=(7, 10))
left = canvas.create_rectangle(24, 140, 36, 220, fill="white", outline="")
right = canvas.create_rectangle(604, 140, 616, 220, fill="white", outline="")
ball = canvas.create_oval(312, 172, 328, 188, fill="#facc15", outline="")
score = [0, 0]
score_text = canvas.create_text(WIDTH / 2, 35, fill="white", font=("Arial", 24))
dx, dy = 4, 3


def show_score():
    canvas.itemconfig(score_text, text=f"{score[0]} : {score[1]}")


def move_paddle(paddle, amount):
    _, y1, _, y2 = canvas.coords(paddle)
    amount = max(-y1, min(amount, HEIGHT - y2))
    canvas.move(paddle, 0, amount)


def on_key(event):
    key = event.keysym.lower()
    if key == "w":
        move_paddle(left, -PADDLE_STEP)
    elif key == "s":
        move_paddle(left, PADDLE_STEP)
    # TODO (Aufgabe 1): Rechten Schläger mit den Pfeiltasten (Up/Down) steuern.


window.bind("<KeyPress>", on_key)


def reset_ball():
    canvas.coords(ball, 312, 172, 328, 188)


def tick():
    global dx, dy
    canvas.move(ball, dx, dy)
    x1, y1, x2, y2 = canvas.coords(ball)

    if y1 <= 0 or y2 >= HEIGHT:
        dy = -dy

    lx1, ly1, lx2, ly2 = canvas.coords(left)
    rx1, ry1, rx2, ry2 = canvas.coords(right)
    if dx < 0 and x1 <= lx2 and x2 >= lx1 and y2 >= ly1 and y1 <= ly2:
        dx = abs(dx)
    elif dx > 0 and x2 >= rx1 and x1 <= rx2 and y2 >= ry1 and y1 <= ry2:
        dx = -abs(dx)

    if x2 < 0 or x1 > WIDTH:
        scorer = 0 if x1 > WIDTH else 1
        score[scorer] += 1
        show_score()
        reset_ball()
        dx = -dx

    window.after(16, tick)


show_score()
tick()
window.mainloop()
