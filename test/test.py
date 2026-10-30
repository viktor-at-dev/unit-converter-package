from unit import unit_convert

import pytest


def test_kg_to_lbs():
    assert unit_convert.kg_to_lbs(1) == pytest.approx(2.2046226218)
    assert unit_convert.kg_to_lbs(0) == 0


def test_metres_to_feet():
    assert unit_convert.metres_to_feet(1) == pytest.approx(3.280839895)
    assert unit_convert.metres_to_feet(0) == 0