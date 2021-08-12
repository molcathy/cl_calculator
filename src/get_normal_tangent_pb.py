from tokenizef import get_tokens, get_constant_power, generate_equation
from integration_differentiation import differentiation, integration


def get_highest_power(powers):
    highest = powers[0]
    for p in range(0, len(powers)):
        if highest < powers[p]:
            highest = powers[p]


def line_yintercept(m, x, y):
    yintercept = (m * (-1 * x)) - y
    return yintercept


def get_tangent(powers, constants, x, y):
    m_constants, m_powers = differentiation(powers, constants)
    t_m = generate_equation(
        m_constants,
        m_powers,
    )
    t_m(x)
    yintercept = line_yintercept(t_m, x, y)

    t_constants = [t_m, yintercept]
    t_powers = [1, 0]
    return t_m, t_constants, t_powers


def get_normal(powers, constants, x, y):
    t_m, m_constants, m_powers = get_tangent(powers, constants, x)
    n_m = (t_m ** -1) * -1
    yintercept = line_yintercept(n_m, x, y)

    n_constants = [n_m, yintercept]
    n_powers = [1, 0]
    return n_constants, n_powers


def get_pb(powers, constants, startx, starty, endx, endy):
    mid_x = (endx - startx) / 2
    mid_y = (starty - endy) / 2
    pb_constants, pb_powers = get_normal(powers, constants, mid_x, mid_y)

    return pb_constants, pb_powers


def main():
    formula = "5x^3 + 4x^2 - 4x - 4"
    tokens = get_tokens(formula)
    constants, powers = get_constant_power(tokens)


if __name__ == "__main__":
    main()
