from tkinter import *

def fixed_scale_values(start_choice, end_choice, real_start, real_end):
    '''Example comment'''
    # figures out the gradient (m) and the y intercept (c)
    real_difference = real_end - real_start
    choice_difference = end_choice - start_choice
    m = real_difference / choice_difference
    c = real_end - (end_choice * m)
    return m, c

def y_scale(y, start_y_choice, end_y_choice, real_y_start, real_y_end):
    # figures out the actual value of y, using the gradient and y intercept, but also y * -1, because  it needs to start from the bottom as it goes upwards for a positive gradient
    y_m, y_c = fixed_scale_values(start_y_choice, end_y_choice, real_y_start, real_y_end)
    return (y * -1) * y_m + y_c

def x_scale(x, start_x_choice, end_x_choice, real_x_start, real_x_end):
    # this figures out the actual value of x
    x_m, x_c = fixed_scale_values(start_x_choice, end_x_choice, real_x_start, real_x_end)
    return x * x_m + x_c

def power3_curve(a, b, c, d, start_x_choice, end_x_choice, real_x_start, real_x_end, start_y_choice, end_y_choice, real_y_start, real_y_end):
    # this creates a curve made by a polynomial to the power of 2
    new_x = []
    new_y = []
    x = start_x_choice
    while x <= end_x_choice:
        y = (a * x**3) + (b * x ** 2) + (c * x) + d
        if y >= start_y_choice and y <= end_y_choice:
            new_x.append(x)
            new_y.append(y)
        x += 0.01 #add a really small amount so it looks like a curve
    for i in range(0, len(new_y) - 1):
        canvas.create_line(x_scale(new_x[i], start_x_choice, end_x_choice, real_x_start, real_x_end), y_scale(new_y[i], start_y_choice, end_y_choice, real_y_start, real_y_end), x_scale(new_x[i + 1], start_x_choice, end_x_choice, real_x_start, real_x_end), y_scale(new_y[i + 1], start_y_choice, end_y_choice, real_y_start, real_y_end), width = 2, fill = "blue")

root = Tk()

canvas = Canvas(width=1000, height=1000, bg="lightblue")
canvas.grid()

real_x_start = 100
real_x_end = 700
start_x_choice = -5
end_x_choice = 5

real_y_start = 100
real_y_end = 700
start_y_choice = -5
end_y_choice = 5

power3_curve(2, -7, -5, 4, start_x_choice, end_x_choice, real_x_start, real_x_end, start_y_choice, end_y_choice, real_y_start, real_y_end)

mainloop()