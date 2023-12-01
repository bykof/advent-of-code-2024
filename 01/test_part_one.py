from part_one import calibration_value, calibration_values_sum


def test_calibration_value():
    assert calibration_value("1abc2") == 12
    assert calibration_value("pqr3stu8vwx") == 38
    assert calibration_value("treb7uchet") == 77


def test_calibration_values_sum():
    input_text = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""
    lines = input_text.splitlines()
    assert calibration_values_sum(lines) == 142
