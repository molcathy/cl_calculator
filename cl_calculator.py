# from teacher_programme import draw_axes
from tkinter import Tk, Canvas, mainloop


def fixed_scale_values(start_choice, end_choice, real_start, real_end):
    """Figures out the gradient (m) and the y intercept (c)."""
    real_difference = real_end - real_start
    choice_difference = end_choice - start_choice
    m = real_difference / choice_difference
    c = real_end - (end_choice * m)
    return m, c


def y_scale(y, start_y_choice, end_y_choice, real_y_start, real_y_end):
    """Figures out the actual value of y, using the gradient and y
    intercept, but also y * -1, because  it needs to start from the bottom as it goes upwards for a positive gradient."""
    y_m, y_c = fixed_scale_values(
        start_y_choice, end_y_choice, real_y_start, real_y_end
    )
    return (y * -1) * y_m + y_c


def x_scale(x, start_x_choice, end_x_choice, real_x_start, real_x_end):
    """This figures out the actual value of x."""
    x_m, x_c = fixed_scale_values(
        start_x_choice, end_x_choice, real_x_start, real_x_end
    )
    return x * x_m + x_c


def draw_lines(
    x1,
    x2,
    y1,
    y2,
    start_x_choice,
    end_x_choice,
    real_x_start,
    real_x_end,
    start_y_choice,
    end_y_choice,
    real_y_start,
    real_y_end,
):
    """"""
    canvas.create_line(
        x_scale(x1, start_x_choice, end_x_choice, real_x_start, real_x_end),
        y_scale(y1, start_y_choice, end_y_choice, real_y_start, real_y_end),
        x_scale(x2, start_x_choice, end_x_choice, real_x_start, real_x_end),
        y_scale(y2, start_y_choice, end_y_choice, real_y_start, real_y_end),
        width=2,
        fill="green",
    )


def indent(
    x1,
    x2,
    y1,
    y2,
    start_x_choice,
    end_x_choice,
    real_x_start,
    real_x_end,
    start_y_choice,
    end_y_choice,
    real_y_start,
    real_y_end,
):
    """This creates indentations along the x and y axis lines with the values of the indents."""
    if int(y1) == 0:
        for x in range(x1, (x2 + 1)):
            draw_lines(
                x,
                x,
                0,
                -0.3,
                start_x_choice,
                end_x_choice,
                real_x_start,
                real_x_end,
                start_y_choice,
                end_y_choice,
                real_y_start,
                real_y_end,
            )
            canvas.create_text(
                x_scale(x, start_x_choice, end_x_choice, real_x_start, real_x_end),
                y_scale(-0.5, start_y_choice, end_y_choice, real_y_start, real_y_end),
                text=str(x),
                fill="green",
            )

    if int(x1) == 0:
        for y in range(y1, (y2 + 1)):
            draw_lines(
                0,
                -0.15,
                y,
                y,
                start_x_choice,
                end_x_choice,
                real_x_start,
                real_x_end,
                start_y_choice,
                end_y_choice,
                real_y_start,
                real_y_end,
            )
            canvas.create_text(
                x_scale(-0.5, start_x_choice, end_x_choice, real_x_start, real_x_end),
                y_scale(y, start_y_choice, end_y_choice, real_y_start, real_y_end),
                text=str(y),
                fill="green",
            )


def power2_curve(
    a,
    b,
    c,
    start_x_choice,
    end_x_choice,
    real_x_start,
    real_x_end,
    start_y_choice,
    end_y_choice,
    real_y_start,
    real_y_end,
):
    """This creates a curve made by a polynomial to the power of 2."""
    new_x = []
    new_y = []
    max = 0
    x = start_x_choice
    while x <= end_x_choice:
        y = a * x ** 2 + b * x + c
        if y >= start_y_choice and y <= end_y_choice:
            new_x.append(x)
            new_y.append(y)
        x += 0.01  # add a really small amount so it looks like a curve
    for i in range(0, len(new_y) - 1):
        canvas.create_line(
            x_scale(new_x[i], start_x_choice, end_x_choice, real_x_start, real_x_end),
            y_scale(new_y[i], start_y_choice, end_y_choice, real_y_start, real_y_end),
            x_scale(
                new_x[i + 1], start_x_choice, end_x_choice, real_x_start, real_x_end
            ),
            y_scale(
                new_y[i + 1], start_y_choice, end_y_choice, real_y_start, real_y_end
            ),
            width=2,
            fill="blue",
        )


def line(
    m,
    c,
    start_x_choice,
    end_x_choice,
    real_x_start,
    real_x_end,
    start_y_choice,
    end_y_choice,
    real_y_start,
    real_y_end,
):
    """This creates a line."""
    list_x = []
    list_y = []

    x = start_x_choice
    while x <= end_x_choice:
        y = x * m + c

        if y >= start_y_choice and y <= end_y_choice:
            list_y.append(y)
            list_x.append(x)

        x += 0.1
        # the smaller the value added the more accurate the result and matches the graph
    for i in range(0, len(list_y) - 1):
        canvas.create_line(
            x_scale(list_x[i], start_x_choice, end_x_choice, real_x_start, real_x_end),
            y_scale(list_y[i], start_y_choice, end_y_choice, real_y_start, real_y_end),
            x_scale(
                list_x[i + 1], start_x_choice, end_x_choice, real_x_start, real_x_end
            ),
            y_scale(
                list_y[i + 1], start_y_choice, end_y_choice, real_y_start, real_y_end
            ),
            width=2,
            fill="black",
        )


if __name__ == "__main__":
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

    x_m, x_c = fixed_scale_values(
        start_x_choice, end_x_choice, real_x_start, real_x_end
    )
    y_m, y_c = fixed_scale_values(
        start_y_choice, end_y_choice, real_y_start, real_y_end
    )

    draw_lines(
        start_x_choice,
        end_x_choice,
        0,
        0,
        start_x_choice,
        end_x_choice,
        real_x_start,
        real_x_end,
        start_y_choice,
        end_y_choice,
        real_y_start,
        real_y_end,
    )
    draw_lines(
        0,
        0,
        start_y_choice,
        end_y_choice,
        start_x_choice,
        end_x_choice,
        real_x_start,
        real_x_end,
        start_y_choice,
        end_y_choice,
        real_y_start,
        real_y_end,
    )

    indent(
        start_x_choice,
        end_x_choice,
        0,
        0,
        start_x_choice,
        end_x_choice,
        real_x_start,
        real_x_end,
        start_y_choice,
        end_y_choice,
        real_y_start,
        real_y_end,
    )
    indent(
        0,
        0,
        start_y_choice,
        end_y_choice,
        start_x_choice,
        end_x_choice,
        real_x_start,
        real_x_end,
        start_y_choice,
        end_y_choice,
        real_y_start,
        real_y_end,
    )

    power2_curve(
        3,
        4,
        2,
        start_x_choice,
        end_x_choice,
        real_x_start,
        real_x_end,
        start_y_choice,
        end_y_choice,
        real_y_start,
        real_y_end,
    )
    line(
        1,
        8,
        start_x_choice,
        end_x_choice,
        real_x_start,
        real_x_end,
        start_y_choice,
        end_y_choice,
        real_y_start,
        real_y_end,
    )

    mainloop()
