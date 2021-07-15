import pytest
import scale


def test_fixed_scale_values():
    assert scale.fixed_scale_values(-4, 4, 100, 900) == (100, 500)


def test_y_scale():
    assert scale.y_scale(3, -5, 5, 600, 100) == 500


def test_x_scale():
    assert scale.x_scale(3, -5, 5, 100, 600) == 500
