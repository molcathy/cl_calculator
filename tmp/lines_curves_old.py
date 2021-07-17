from tkinter import Tk, Canvas, mainloop
from scale import fixed_scale_values, y_scale, x_scale

# NOTE - I did:
# * split power2_curve in 3 smaller functions
# * renamed some parameters e.g.:
#   - all parameters containing x, y modified to *start* with x_, y_

# TODO!
# * pass width and width to canvas as parameters to the functions that invokes them
# * write proper comments by replacing <TAKES> <DOES> and <RETURNS> with actual comments
# * brake line() in 3 functions in the same way I did power2_curve() e.g.
#   - get_line(): to perform the math and return its results
#   - draw_line(): to perform the math and return its results
# * implement tests for functions that preform the math:
#   - get_power2_curve_coordinates()
#   - get_line()
# * _maybe_ rename lines.py to lines_curves.py because it draws both lines and curves or even brake them down in 2 different volumes
# * used lambda to generalize get_power2_curve_coordinates


def get_power2_curve_coordinates(a, b, c, x_start, x_end, y_start, y_end):
    """get_power2_curve_coordinates ... <TAKES> <DOES> and <RETURNS>"""
    x_coordinates = []
    y_coordinates = []
    x = x_start
    while x <= x_end:
        y = (a * x ** 2) + (b * x) + c
        if y >= y_start and y <= y_end:
            x_coordinates.append(x)
            y_coordinates.append(y)
        # add a really small amount so it looks like a curve
        x += 0.01
    return x_coordinates, y_coordinates


def draw_power2_curve(
    canvas,
    x_start,
    x_end,
    x_tk_start,
    x_tk_end,
    y_start,
    y_end,
    y_tk_start,
    y_tk_end,
    x_coordinates,
    y_coordinates,
):
    """draw_power2_curve  ... <TAKES> <DOES> and <RETURNS>"""
    for i in range(0, len(y_coordinates) - 1):
        canvas.create_line(
            x_scale(x_coordinates[i], x_start, x_end, x_tk_start, x_tk_end),
            y_scale(y_coordinates[i], y_start, y_end, y_tk_start, y_tk_end),
            x_scale(x_coordinates[i + 1], x_start, x_end, x_tk_start, x_tk_end),
            y_scale(y_coordinates[i + 1], y_start, y_end, y_tk_start, y_tk_end),
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
    x_tk_start,
    x_tk_end,
    y_start,
    y_end,
    y_tk_start,
    y_tk_end,
):
    """power2_curve ... <TAKES> <DOES> and <RETURNS>"""
    x_coordinates, y_coordinates = get_power2_curve_coordinates(
        a,
        b,
        c,
        x_start,
        x_end,
        y_start,
        y_end,
    )
    draw_power2_curve(
        canvas,
        x_start,
        x_end,
        x_tk_start,
        x_tk_end,
        y_start,
        y_end,
        y_tk_start,
        y_tk_end,
        x_coordinates,
        y_coordinates,
    )


def get_line_coordinates(x_start, x_end, y_start, y_end, m, c):
    x_coordinates = []
    y_coordinates = []

    x = x_start
    while x <= x_end:
        y = x * m + c
        if y >= y_start and y <= y_end:
            y_coordinates.append(y)
            x_coordinates.append(x)
        # the smaller the value added the more accurate the result and matches the graph
        x += 0.1
    return x_coordinates, y_coordinates


def draw_line(
    canvas,
    x_coordinates,
    y_coordinates,
    x_start,
    x_end,
    x_tk_start,
    x_tk_end,
    y_start,
    y_end,
    y_tk_start,
    y_tk_end,
):
    for i in range(0, len(y_coordinates) - 1):
        canvas.create_line(
            x_scale(x_coordinates[i], x_start, x_end, x_tk_start, x_tk_end),
            y_scale(y_coordinates[i], y_start, y_end, y_tk_start, y_tk_end),
            x_scale(x_coordinates[i + 1], x_start, x_end, x_tk_start, x_tk_end),
            y_scale(y_coordinates[i + 1], y_start, y_end, y_tk_start, y_tk_end),
            width=2,
            fill="black",
        )


def line(
    canvas,
    m,
    c,
    x_start,
    x_end,
    x_tk_start,
    x_tk_end,
    y_start,
    y_end,
    y_tk_start,
    y_tk_end,
):
    """line ... <TAKES> <DOES> and <RETURNS>"""
    x_coordinates, y_coordinates = get_line_coordinates(
        x_start, x_end, y_start, y_end, m, c
    )
    draw_line(
        canvas,
        x_coordinates,
        y_coordinates,
        x_start,
        x_end,
        x_tk_start,
        x_tk_end,
        y_start,
        y_end,
        y_tk_start,
        y_tk_end,
    )


def main():
    root = Tk()
    canvas = Canvas(width=1000, height=1000, bg="lightblue")
    canvas.grid()

    x_start = -5
    x_end = 5
    x_tk_start = 100
    x_tk_end = 700

    y_start = -5
    y_end = 5
    y_tk_start = 100
    y_tk_end = 700

    power2_curve(
        canvas,
        3,
        4,
        2,
        x_start,
        x_end,
        x_tk_start,
        x_tk_end,
        y_start,
        y_end,
        y_tk_start,
        y_tk_end,
    )
    line(
        canvas,
        1,
        8,
        x_start,
        x_end,
        x_tk_start,
        x_tk_end,
        y_start,
        y_end,
        y_tk_start,
        y_tk_end,
    )

    mainloop()


if __name__ == "__main__":
    main()
