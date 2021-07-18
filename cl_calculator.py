import sys

sys.path.append("./src")
from tkinter import Tk, Canvas, mainloop
from src import axes, lines_curves

# TODO!
# -[] replace variables having 'real' in names as per already established standard
# -[] replace variables having 'choice' in names as per already established standard


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

    axes.draw_lines(
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
    axes.draw_lines(
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

    axes.indent(
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
    axes.indent(
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

    lines_curves.power2_curve(
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

    lines_curves.line(
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
