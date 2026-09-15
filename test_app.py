from app import calculate_shipping


def test_light_package():
    assert calculate_shipping(3) == 50


def test_medium_package():
    assert calculate_shipping(7) == 100


def test_heavy_package():
    assert calculate_shipping(15) == 150