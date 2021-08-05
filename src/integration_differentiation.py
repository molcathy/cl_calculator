from tokenizef import get_tokens, get_constant_power, equation


def differentiation(powers, constants, x):
    fx = 0

    for p in range(0, len(powers)):
        power = powers[p] - 1
        fx += powers[p] * constants[p] * (x ** power)

    return fx


def integration(powers, constants, x):
    fx = 0

    for p in range(0, len(powers)):
        power = powers[p] + 1
        fx += (constants[p] / power) * (x ** power)

    return fx


def main():
    pass


if __name__ == "__main__":
    main()
