from tkinter import Tk, Canvas, mainloop
from scale import get_fixed_scale_values, get_y_scale, get_x_scale


def draw_lines(
    canvas,
    x1,
    x2,
    y1,
    y2,
    x_start,
    x_end,
    x_tk_start,
    x_tk_end,
    y_start,
    y_end,
    y_tk_start,
    y_tk_end,
):
    """draw_lines takes the values of the x and y axes
    getting the values of each axes by having the the start
    and end values then draws the line."""

    canvas.create_line(
        get_x_scale(x1, x_start, x_end, x_tk_start, x_tk_end),
        get_y_scale(y1, y_start, y_end, y_tk_start, y_tk_end),
        get_x_scale(x2, x_start, x_end, x_tk_start, x_tk_end),
        get_y_scale(y2, y_start, y_end, y_tk_start, y_tk_end),
        width=2,
        fill="green",
    )


def indent(
    canvas,
    x1,
    x2,
    y1,
    y2,
    x_start,
    x_end,
    x_tk_start,
    x_tk_end,
    y_start,
    y_end,
    y_tk_start,
    y_tk_end,
):
    """indent takes in the values of the axis, figuring
    out wether its a y or x axis then drawing indents
    along said axis at intervals as well as stating
    the current values underneath"""

    if int(y1) == 0:
        for x in range(x1, (x2 + 1)):
            draw_lines(
                canvas,
                x,
                x,
                0,
                -0.3,
                x_start,
                x_end,
                x_tk_start,
                x_tk_end,
                y_start,
                y_end,
                y_tk_start,
                y_tk_end,
            )
            canvas.create_text(
                get_x_scale(x, x_start, x_end, x_tk_start, x_tk_end),
                get_y_scale(-0.5, y_start, y_end, y_tk_start, y_tk_end),
                text=str(x),
                fill="green",
            )

    if int(x1) == 0:
        for y in range(y1, (y2 + 1)):
            draw_lines(
                canvas,
                0,
                -0.15,
                y,
                y,
                x_start,
                x_end,
                x_tk_start,
                x_tk_end,
                y_start,
                y_end,
                y_tk_start,
                y_tk_end,
            )
            canvas.create_text(
                get_x_scale(-0.5, x_start, x_end, x_tk_start, x_tk_end),
                get_y_scale(y, y_start, y_end, y_tk_start, y_tk_end),
                text=str(y),
                fill="green",
            )


def main():
    root = Tk()
    canvas = Canvas(width=1000, height=1000, bg="lightblue")
    canvas.grid()

    x_tk_start = 100
    x_tk_end = 700
    x_start = -5
    x_end = 5

    y_tk_start = 100
    y_tk_end = 700
    y_start = -5
    y_end = 5

    draw_lines(
        canvas,
        x_start,
        x_end,
        0,
        0,
        x_start,
        x_end,
        x_tk_start,
        x_tk_end,
        y_start,
        y_end,
        y_tk_start,
        y_tk_end,
    )
    draw_lines(
        canvas,
        0,
        0,
        y_start,
        y_end,
        x_start,
        x_end,
        x_tk_start,
        x_tk_end,
        y_start,
        y_end,
        y_tk_start,
        y_tk_end,
    )

    indent(
        canvas,
        x_start,
        x_end,
        0,
        0,
        x_start,
        x_end,
        x_tk_start,
        x_tk_end,
        y_start,
        y_end,
        y_tk_start,
        y_tk_end,
    )
    indent(
        canvas,
        0,
        0,
        y_start,
        y_end,
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
