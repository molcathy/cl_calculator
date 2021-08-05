from tokenizef import get_tokens, get_constant_power, equation


def check_polynomial(powers):
    power = False
    for p in powers:
        if p >= 2:
            power = True
    return power


def get_tangent(powers, constants, xcoordinate, ycoordinate):
    """How do I find the gradient for any power of x, generally larger than 3"""
    curve = check_polynomial(powers)
    if curve == True:
        pass


def get_normal():
    pass


def get_pb():
    pass


def main():
    formula = "5x^3 + 4x^2 - 4x - 4"
    xcoordinate = 0
    ycoordinate = 0
    tokens = get_tokens(formula)
    constants, powers = get_constant_power(tokens)
    y = equation(constants, powers, 1)


if __name__ == "__main__":
    main()
