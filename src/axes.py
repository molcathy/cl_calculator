from tkinter import Tk, Canvas, mainloop
from scale import fixed_scale_values, y_scale, x_scale


def draw_lines(
    canvas,
    x1,
    x2,
    y1,
    y2,````
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
    canvas,
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
                canvas,
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
                canvas,
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

    draw_lines(
        canvas,
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
        canvas,
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
        canvas,
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
        canvas,
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
    mainloop()


if __name__ == "__main__":
    main()
