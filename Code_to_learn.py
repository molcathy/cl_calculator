from tkinter import *
root = Tk()
root.title('Line Drawing')

canvas = Canvas(width=1000,height=800, bg="lightblue")
canvas.pack(expand=YES,fill=BOTH)

canvas.create_line(400, 100, 400, 500, width = 4, fill="green")
canvas.create_line(650, 300, 150, 300, width = 4, fill="green")

canvas.create_text(400, 90, text = 'y', fill = 'green')
canvas.create_text(660, 300, text = 'x', fill = 'green')

equation = input('Enter an equation in the form, mx + c: ')

equation2 = equation.split('x')
equation3 = equation2[1].split('+')
newEquation = [equation2[0], equation3[1]]
print(equation2)
print(newEquation)
print(newEquation)
m = float(newEquation[0])
c = float(newEquation[1])

for i in range(80, 110):
        x1 = m * i
        x2 = (m * x1) + 1
        y1 = x1 + c
        y2 = x2 + c
        canvas.create_line(x1, y1, x2, y2, width = 3, fill = 'black')

mainloop()
