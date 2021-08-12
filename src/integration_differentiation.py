from tokenizef import get_tokens, get_constant_power, generate_equation


def differentiation(powers, constants):
    fx_powers = []
    fx_constant = []

    for p in range(0, len(powers)):
        power = powers[p] - 1
        fx_powers.append(power)
        fx_constant.append(constants[p] * powers[p])

    return fx_constant, fx_powers


def integration(powers, constants):
    fx_powers = []
    fx_constant = []

    for p in range(0, len(powers)):
        power = powers[p] + 1
        fx_powers.append(power)
        fx_constant.append(constants[p] / power)

    return (
        fx_constant,
        fx_powers,
    )


def main():
    pass


if __name__ == "__main__":
    main()
