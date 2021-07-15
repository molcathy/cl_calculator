from tkinter import Tk, Canvas, mainloop
from scale import fixed_scale_values, y_scale, x_scale


def power2_curve(
    canvas,
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
    x = start_x_choice
    while x <= end_x_choice:
        y = (a * x ** 2) + (b * x) + c
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
    canvas,
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


def main():
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

    power2_curve(
        canvas,
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
        canvas,
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


if __name__ == "__main__":
    main()
