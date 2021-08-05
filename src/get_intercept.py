from tokenizef import get_tokens, get_constant_power, equation


def gt_x_y_intercept(constants, powers, x):
    y_intercept = equation(constants, powers, 0)
    x_intercept = 0
    """how do I find all of the x_intercepts, for any power of x"""
    """
    num = 0
    x1 = False
    x2 = False
    while x1 or x2 is True:
        fx = 0
        num1 = 0
        num2 = 0
        for constant in range(0, len(constants)):
            c = constants[constant]
            p = powers[constant]
            fx += c * (num1 ** p)
        if fx
    """


def main():
    formula = "5x^3 + 4x^2 - 4x - 4"
    tokens = get_tokens(formula)
    constants, powers = get_constant_power(tokens)
    y = equation(constants, powers, 1)


if __name__ == "__main__":
    main()
