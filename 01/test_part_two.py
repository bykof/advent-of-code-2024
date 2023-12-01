from part_two import calibration_value, calibration_values_sum


def test_calibration_value():
    assert calibration_value("eightwothree") == 83
    assert calibration_value("xtwone3four") == 24
    assert calibration_value("zoneight234") == 14


def test_calibration_values_sum():
    input_text = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    lines = input_text.splitlines()
    assert calibration_values_sum(lines) == 281
