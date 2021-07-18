#
# TODO!
# * replace 'choice' in variable names e.g. start_choice, ...
# * replace 'real' in variable names e.g. real_difference, ...
# * replace prepend functions name that return some values with get e.g. 'fixed_scale_values' -> 'get_fixed_scale_values'
# * replace function comments with '<FUNCTION-NAME> <TAKES> <DOES> <RETURNS>'
# * update the tests with the new function names


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


def main():
    gradient, y_intercept = fixed_scale_values(-4, 4, 100, 900)
    y_value = y_scale(3, -5, 5, 600, 100)
    x_value = x_scale(3, -5, 5, 100, 600)

    print(f"fixed_scale_values: {gradient}, {y_intercept}")
    print(f"y_scale: {y_value}")
    print(f"x_scale: {x_value}")


if __name__ == "__main__":
    main()
