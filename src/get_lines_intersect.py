from get_normal_tangent_pb import (
    get_highest_power,
    line_yintercept,
    get_tangent,
    get_normal,
    get_pb,
)
from get_intercept import (
    quadratic_roots,
    smallest_x_intercept,
    newton_step,
    newton_raphson_approximation,
    get_x_y_intercept,
)
from tokenizef import generate_equation, string_constant_power

# P1: [2,1,0] and C1: [2,3,4]
# P2: [1,0] and C2: [3,8]


def sorted_insert(list1, list2, value):
    """
    list1 is the powers list
    list2 is the constants list
    """
    for i in range(len(list1)):
        if list1[i] < value:
            index = i
            break
    if index == -1:
        new_powers = list1 + [value]
        new_constants = list2 + [0]
    else:
        new_powers = list1[:i] + [value] + list1[i:]
        new_constants = list2[:i] + [0] + list2[i:]
    return new_powers, new_constants


def sort_pairs(p, c):
    p, c = zip(*sorted(zip(p, c), reverse=True))
    p = list(p)
    c = list(c)

    return p, c


def merge_polynomials(p1, c1, p2, c2):
    p3 = sorted(set(p1 + p2), reverse=True)  # At this point p3 = [2,1,0]
    c3 = []

    # p1 = [2,0,1] c1 = [5,6,7]
    # zip(p1,c1) -> [(2,5), (0,6), (1,7)]
    # sorted(_)  -> [(0,6), (1,7), (2,5)]
    # *          -> (0,6), (1,7), (2,5)
    # zip(_)     -> (0,1,2), (6,7,5)
    # list(p1)   -> [0,1,2]
    # list(c1)   -> [6,7,5]
    p1, c1 = sort_pairs(p1, c1)
    p2, c2 = sort_pairs(p2, c2)

    for p in p3:
        if p not in p1:
            p1, c1 = sorted_insert(p1, c1, p)
        if p not in p2:
            p2, c2 = sorted_insert(p2, c2, p)

    p1, c1 = sort_pairs(p1, c1)
    p2, c2 = sort_pairs(p2, c2)

    for i in range(0, len(p1)):
        c3.append(c1[i] - c2[i])

    return p3, c3


def get_intersect(p1, c1, p2, c2, x_start, x_end, y_start, y_end):
    p3, c3 = merge_polynomials(p1, c1, p2, c2)
    formula = string_constant_power(c3, p3)
    y_intercept, x_intercept = get_x_y_intercept(
        c3, p3, x_start, x_end, y_start, y_end, formula
    )

    y_coordinates = []
    for x in x_intercept:
        fx = generate_equation(p3, c3)
        y_coordinates.append(fx(x))

    return x_intercept, y_coordinates
    # get code from the get_intercept module


def main():
    pass
    x_start = -5
    x_end = 5

    y_start = -5
    y_end = 5

    p1 = [3, 2, 0]
    p2 = [2, 1, 0]
    c1 = [5, 6, 8]
    c2 = [4, 5, 2]
    sorted_insert(p1, c1, 1)
    merge_polynomials(p1, c1, p2, c2)


if __name__ == "__main__":
    main()
