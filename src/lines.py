from tkinter import Tk, Canvas, mainloop
from scale import fixed_scale_values, y_scale, x_scale

# NOTE - I did:
# * split power2_curve in 3 smaller functions
# * renamed some parameters e.g.:
#   - all parameters containing x, y modified to *start* with x_, y_

# TODO!
# * improve variables e.g.:
#   - a, b, c: do not mean anything
#   - x_start_real, x_end_real: what real means
#   - list_x, list_y ... mean nothing other then they are lists; the variable names must say something about its main role/feature
# * pass width and width to canvas as parameters to the functions that invokes them
# * write proper comments by replacing <TAKES> <DOES> and <RETURNS> with actual comments
# * brake line() in 3 functions in the same way I did power2_curve() e.g.
#   - get_line(): to perform the math and return its results
#   - draw_line(): to perform the math and return its results
# * implement tests for functions that preform the math:
#   - get_power2_curve()
#   - get_line()
# * _maybe_ rename lines.py to lines_curves.py because it draws both lines and curves or even brake them down in 2 different volumes
# * used lambda to generalize get_power2_curve


def get_power2_curve(a, b, c, x_start, x_end, y_start, y_end, operation):
    """get_power2_curve ... <TAKES> <DOES> and <RETURNS>"""
    x_new = []
    y_new = []
    while x_start <= x_end:
        # maybe y must be replaced with what actually the operation does to x_start
        y = operation(x_start)
        if y >= y_start and y <= y_end:
            x_new.append(x_start)
            y_new.append(y)
        # add a really small amount so it looks like a curve
        x_start += 0.01
    return x_new, y_new


# def get_power2_curve(a, b, c, x_start, x_end, y_start, y_end):
#     """get_power2_curve ... <TAKES> <DOES> and <RETURNS>"""
#     x_new = []
#     y_new = []
#     x = x_start
#     while x <= x_end:
#         y = (a * x ** 2) + (b * x) + c
#         if y >= y_start and y <= y_end:
#             x_new.append(x)
#             y_new.append(y)
#         # add a really small amount so it looks like a curve
#         x += 0.01
#     return x_new, y_new


def draw_power2_curve(
    canvas,
    x_start,
    x_end,
    x_start_real,
    x_end_real,
    y_start,
    y_end,
    y_start_real,
    y_end_real,
    x_new,
    y_new,
):
    """draw_power2_curve  ... <TAKES> <DOES> and <RETURNS>"""
    for i in range(0, len(y_new) - 1):
        canvas.create_line(
            x_scale(x_new[i], x_start, x_end, x_start_real, x_end_real),
            y_scale(y_new[i], y_start, y_end, y_start_real, y_end_real),
            x_scale(x_new[i + 1], x_start, x_end, x_start_real, x_end_real),
            y_scale(y_new[i + 1], y_start, y_end, y_start_real, y_end_real),
            width=2,
            fill="blue",
        )


def power2_curve(
    canvas,
    a,
    b,
    c,
    x_start,
    x_end,
    x_start_real,
    x_end_real,
    y_start,
    y_end,
    y_start_real,
    y_end_real,
):
    """power2_curve ... <TAKES> <DOES> and <RETURNS>"""
    x_new, y_new = get_power2_curve(
        a,
        b,
        c,
        x_start,
        x_end,
        y_start,
        y_end,
        operation=lambda i: (a * i ** 2) + (b * i) + c,
    )
    draw_power2_curve(
        canvas,
        x_start,
        x_end,
        x_start_real,
        x_end_real,
        y_start,
        y_end,
        y_start_real,
        y_end_real,
        x_new,
        y_new,
    )


def line(
    canvas,
    m,
    c,
    x_start,
    x_end,
    x_start_real,
    x_end_real,
    y_start,
    y_end,
    y_start_real,
    y_end_real,
):
    """line ... <TAKES> <DOES> and <RETURNS>"""
    list_x = []
    list_y = []

    x = x_start
    while x <= x_end:
        y = x * m + c
        if y >= y_start and y <= y_end:
            list_y.append(y)
            list_x.append(x)
        # the smaller the value added the more accurate the result and matches the graph
        x += 0.1
    for i in range(0, len(list_y) - 1):
        canvas.create_line(
            x_scale(list_x[i], x_start, x_end, x_start_real, x_end_real),
            y_scale(list_y[i], y_start, y_end, y_start_real, y_end_real),
            x_scale(list_x[i + 1], x_start, x_end, x_start_real, x_end_real),
            y_scale(list_y[i + 1], y_start, y_end, y_start_real, y_end_real),
            width=2,
            fill="black",
        )


def main():
    root = Tk()
    canvas = Canvas(width=1000, height=1000, bg="lightblue")
    canvas.grid()

    x_start = -5
    x_end = 5
    x_start_real = 100
    x_end_real = 700

    y_start = -5
    y_end = 5
    y_start_real = 100
    y_end_real = 700

    power2_curve(
        canvas,
        3,
        4,
        2,
        x_start,
        x_end,
        x_start_real,
        x_end_real,
        y_start,
        y_end,
        y_start_real,
        y_end_real,
    )
    line(
        canvas,
        1,
        8,
        x_start,
        x_end,
        x_start_real,
        x_end_real,
        y_start,
        y_end,
        y_start_real,
        y_end_real,
    )

    mainloop()


if __name__ == "__main__":
    main()
