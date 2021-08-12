from tokenizef import get_tokens, get_constant_power, equation
from get_coordinates import get_coordinates
from get_normal_tangent_pb import (
    get_highest_power,
    line_yintercept,
    get_tangent,
    get_normal,
    get_pb,
)
from get_coordinates import get_coordinates
import math


def get_x_y_intercept(constants, powers, x):
    y_intercept = equation(constants, powers, 0)
    x_intercept = []
    if get_highest_power(powers) == 1:
        x_intercept.append((constants[1] * -1) / constants[0])

    elif get_highest_power(powers) == 2:
        x_intercept.append(
            (
                -constants[1]
                + math.sqrt((constants[1] ** 2) - (4 * constants[0] * constants[2]))
            )
            / (2 * constants[0])
        )
        x_intercept.append(
            (
                -constants[1]
                - math.sqrt((constants[1] ** 2) - (4 * constants[0] * constants[2]))
            )
            / (2 * constants[0])
        )
    else:
        pass


def smallest_x_intercept(x_start, x_end, y_start, y_end, formula):
    x_coordinates, y_coordinates = get_coordinates(
        x_start,
        x_end,
        y_start,
        y_end,
        formula,
    )
    x = 0
    y = 0
    small = False
    while small == False:
        for y in range(0, len(y_coordinates) - 1):
            if y_coordinates[y] < 1 and y_coordinates[y] > -1:
                x = x_coordinates[y]
                y = y_coordinates[y]
                small = True


def newton_step(constants, powers):
    def newton_step(f, f_prime, x0, tol):
        """
        f is the function
        f_prime is the derivative
        x0 is the inital guess
        tol is the tolerance
        """
        tol = 0.000000000001
        if abs(f(x0)) < tol:
            return x0
        else:
            return newton_step(f, f_prime, x0 - f(x0) / f_prime(x0), tol)

    pass


def main():
    formula = "5x^3 + 4x^2 - 4x - 4"
    tokens = get_tokens(formula)
    constants, powers = get_constant_power(tokens)
    y = equation(constants, powers, 1)

    x_start = -5
    x_end = 5
    x_tk_start = 100
    x_tk_end = 700

    y_start = -5
    y_end = 5
    y_tk_start = 100
    y_tk_end = 700


if __name__ == "__main__":
    main()
