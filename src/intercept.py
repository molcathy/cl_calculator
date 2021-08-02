from tokenizef import get_tokens, get_constant_power, equation


def gt_x_y_intercept(constants, powers, x):
    y_intercept = 0
    x_intercept = 0
    for constant in range(0, len(constants)):
        c = constants[constant]
        p = powers[constant]
        y_intercept += c * (0 ** p)
    """find the x_intercept"""


def main():
    formula = "5x^3 + 4x^2 - 4x - 4"
    tokens = get_tokens(formula)
    constants, powers = get_constant_power(tokens)
    y = equation(constants, powers, 1)


if __name__ == "__main__":
    main()
