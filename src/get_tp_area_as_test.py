import pytest
import get_tp_area_as


def test_max_or_min():
    constants = [2, -5, -4, 2]
    powers = [3, 2, 1, 0]
    tp_x = 2
    constants2 = [1, 4, 4]
    powers = [2, 1, 0]
    assert get_tp_area_as.max_or_min(constants, powers, tp_x) == False
    assert get_tp_area_as.max_or_min(constants, powers, -(1 / 3)) == True


def test_complete_the_square():
    constants = [1, 6, 1]
    assert get_tp_area_as.complete_the_square(constants) == (-3, -8)


def test_get_turning_point():
    constants = [2, -5, -4, 2]
    powers = [3, 2, 1, 0]
    assert get_tp_area_as.get_turning_point(powers, constants) == (
        [-10, (73 / 27)],
        [
            2,
            -(1 / 3),
        ],
    )


def test_get_area():
    constants = [2, -5, -4, 2]
    powers = [3, 2, 1, 0]
    x_start = 1
    x_end = 3
    assert round(
        get_tp_area_as.get_area(powers, constants, x_start, x_end), 3
    ) == round((46 / 3), 3)


# What do I do for graphs such as 3/x + 2 = y
def test_get_asymptote():
    constants = [3 / 1, 2]
    powers = [1, 0]
