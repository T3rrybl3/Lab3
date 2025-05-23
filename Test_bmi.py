import Lab2.lab2 as bmi


def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.7, 54)

    assert (result == 2)


def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.7, 73)

    assert (result == 1)


def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.7, 53)

    assert (result == -1)
