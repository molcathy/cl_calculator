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
    from tokenizef import get_constant_power, get_tokens, generate_equation

    formula = "3x^2 + 4x + 2"
    tokens = get_tokens(formula)
    constants, powers = get_constant_power(tokens)

    dif_constant, dif_powers = differentiation(powers, constants)
    int_constant, int_powers = integration(powers, constants)

    print("Normal consant and powers: ", constants, powers)
    print("Differentiatied constants and powers: ", dif_constant, dif_powers)
    print("Integrated constants and powers: ", int_constant, int_powers)


if __name__ == "__main__":
    main()
