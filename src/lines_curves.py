from tkinter import Tk, Canvas, mainloop
from scale import fixed_scale_values, y_scale, x_scale

# TODO!
# * write proper comments by replacing <TAKES> <DOES> and <RETURNS> with actual comments
# * implement tests for functions that preform the math:
#   - get_coordinates()


def get_coordinates(x_start, x_end, y_start, y_end, equation):
    """get_coordinates takes x and y starting and ending coordinates,
    calculates coordinates that are inside the graph
    and returns them as two lists of values"""
    x_coordinates = []
    y_coordinates = []
    while x_start <= x_end:
        # maybe y must be replaced with what actually the equation does to x_start
        y = equation(x_start)
        if y >= y_start and y <= y_end:
            x_coordinates.append(x_start)
            y_coordinates.append(y)
        # add a really small amount so it looks like a curve
        x_start += 0.01
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
    """draw_power2_curve takes the x and y coordinates,
    of the begining and end of the points on the curve,
    from each list for the curve and draws them"""
    for i in range(0, len(y_coordinates) - 1):
        canvas.create_line(
            x_scale(x_coordinates[i], x_start, x_end, x_tk_start, x_tk_end),
            y_scale(y_coordinates[i], y_start, y_end, y_tk_start, y_tk_end),
            x_scale(x_coordinates[i + 1], x_start, x_end, x_tk_start, x_tk_end),
            y_scale(y_coordinates[i + 1], y_start, y_end, y_tk_start, y_tk_end),
            width=2,
            fill="blue",
        )


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
    """draw_line takes the x and y coordinates,
    of the begining and end of the points on the line,
    from each list and draws a line with them"""
    for i in range(0, len(y_coordinates) - 1):
        canvas.create_line(
            x_scale(x_coordinates[i], x_start, x_end, x_tk_start, x_tk_end),
            y_scale(y_coordinates[i], y_start, y_end, y_tk_start, y_tk_end),
            x_scale(x_coordinates[i + 1], x_start, x_end, x_tk_start, x_tk_end),
            y_scale(y_coordinates[i + 1], y_start, y_end, y_tk_start, y_tk_end),
            width=2,
            fill="black",
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
    """power2_curve uses the values of a quadratic curve,
    calls a function to get the lists of x and y coordinates for the curve
    and calls a function in order to draw a curve using that list"""
    x_coordinates, y_coordinates = get_coordinates(
        x_start,
        x_end,
        y_start,
        y_end,
        equation=lambda x: (a * x ** 2) + (b * x) + c,
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
    """line uses the values of a line, calls a function
    to get the lists of x and y coordinates for the line
    and calls a function in order to draw a line using that list"""
    x_coordinates, y_coordinates = get_coordinates(
        x_start,
        x_end,
        y_start,
        y_end,
        equation=lambda x: x * m + c,
    )
    print(x_coordinates)
    print(y_coordinates)
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
