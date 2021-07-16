from tkinter import Tk, Canvas, mainloop
from scale import fixed_scale_values, y_scale, x_scale


# def get_p2c(a, b, c, start_x, end_x, start_y, end_y):
#     """get_p2c (get power 2 curve)"""
#     new_x = [i for i in [float(j) / 100 for j in range(start_x, end_x + 1)]]
#     new_y = []
#     for x in new_x:
#         y = (a * x ** 2) + (b * x) + c
#         if y >= start_y and y <= end_y:
#             new_y.append(y)
#     return new_x, new_y


def get_p2c(a, b, c, start_x, end_x, start_y, end_y):
    """get_p2c (get power 2 curve)"""
    new_x = []
    new_y = []
    x = start_x
    while x <= end_x:
        y = (a * x ** 2) + (b * x) + c
        if y >= start_y and y <= end_y:
            new_x.append(x)
            new_y.append(y)
        x += 0.01  # add a really small amount so it looks like a curve
    return new_x, new_y


def draw_p2c(
    canvas,
    start_x,
    end_x,
    real_x_start,
    real_x_end,
    start_y,
    end_y,
    real_y_start,
    real_y_end,
    new_x,
    new_y,
):
    """draw_p2c (draw power 2 curve)"""
    for i in range(0, len(new_y) - 1):
        canvas.create_line(
            x_scale(new_x[i], start_x, end_x, real_x_start, real_x_end),
            y_scale(new_y[i], start_y, end_y, real_y_start, real_y_end),
            x_scale(new_x[i + 1], start_x, end_x, real_x_start, real_x_end),
            y_scale(new_y[i + 1], start_y, end_y, real_y_start, real_y_end),
            width=2,
            fill="blue",
        )


def p2c(
    canvas,
    a,
    b,
    c,
    start_x,
    end_x,
    real_x_start,
    real_x_end,
    start_y,
    end_y,
    real_y_start,
    real_y_end,
):
    new_x, new_y = get_p2c(a, b, c, start_x, end_x, start_y, end_y)
    draw_p2c(
        canvas,
        start_x,
        end_x,
        real_x_start,
        real_x_end,
        start_y,
        end_y,
        real_y_start,
        real_y_end,
        new_x,
        new_y,
    )


def line(
    canvas,
    m,
    c,
    start_x,
    end_x,
    real_x_start,
    real_x_end,
    start_y,
    end_y,
    real_y_start,
    real_y_end,
):
    """This creates a line."""
    list_x = []
    list_y = []

    x = start_x
    while x <= end_x:
        y = x * m + c
        if y >= start_y and y <= end_y:
            list_y.append(y)
            list_x.append(x)
        x += 0.1
        # the smaller the value added the more accurate the result and matches the graph
    for i in range(0, len(list_y) - 1):
        canvas.create_line(
            x_scale(list_x[i], start_x, end_x, real_x_start, real_x_end),
            y_scale(list_y[i], start_y, end_y, real_y_start, real_y_end),
            x_scale(list_x[i + 1], start_x, end_x, real_x_start, real_x_end),
            y_scale(list_y[i + 1], start_y, end_y, real_y_start, real_y_end),
            width=2,
            fill="black",
        )


def main():
    root = Tk()
    canvas = Canvas(width=1000, height=1000, bg="lightblue")
    canvas.grid()

    real_x_start = 100
    real_x_end = 700
    start_x = -5
    end_x = 5

    real_y_start = 100
    real_y_end = 700
    start_y = -5
    end_y = 5

    p2c(
        canvas,
        3,
        4,
        2,
        start_x,
        end_x,
        real_x_start,
        real_x_end,
        start_y,
        end_y,
        real_y_start,
        real_y_end,
    )
    line(
        canvas,
        1,
        8,
        start_x,
        end_x,
        real_x_start,
        real_x_end,
        start_y,
        end_y,
        real_y_start,
        real_y_end,
    )

    mainloop()


if __name__ == "__main__":
    main()
