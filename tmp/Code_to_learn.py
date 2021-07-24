# I would like to use this as a future refrence, there is still some code to be used

from tkinter import *

root = Tk()
root.title("Line Drawing")

canvas = Canvas(width=1000, height=800, bg="lightblue")
canvas.pack(expand=YES, fill=BOTH)

canvas.create_line(400, 100, 400, 500, width=4, fill="green")
canvas.create_line(650, 300, 150, 300, width=4, fill="green")

canvas.create_text(400, 90, text="y", fill="green")
canvas.create_text(660, 300, text="x", fill="green")

equation = input("Enter an equation in the form, mx + c: ")

equation2 = equation.split("x")
equation3 = equation2[1].split("+")
newEquation = [equation2[0], equation3[1]]
print(equation2)
print(newEquation)
print(newEquation)
m = float(newEquation[0])
c = float(newEquation[1])

start = 0
end = 0

if int(m) < 0:
    start = 200
    end = 20
    next1 = -1
else:
    start = 20
    end = 200
    next1 = 1


def graphScale(start, end, m, c):
    middlex = (((end * m) + c) - ((start * m) + c)) / 2
    middley = ((end * m) - (start * m)) / 2
    # canvas.create()
    canvas.create_line((start * m), middlex, (end * m), middlex, width=4, fill="green")
    canvas.create_line(
        (middley, (start * m) + c), middley, ((end * m) + c), width=4, fill="green"
    )


def xscale(x):
    return x


def yscale(y):
    return y * -1


for i in range(start, end):
    x1 = m * i
    x2 = (m * x1) + next1
    y1 = x1 + c
    y2 = x2 + c
    print(x1, y1)
    canvas.create_line(
        xscale(x1), yscale(y1), xscale(x2), yscale(y2), width=3, fill="black"
    )

graphScale(start, end, m, c)

mainloop()

# monday tuesday friday
# String functions
