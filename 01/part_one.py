import typing


def read_input_lines(filepath: str) -> typing.List[str]:
    with open(filepath, "r") as input_file:
        return input_file.readlines()


def calibration_value(line: str) -> int:
    first_digit = None
    last_digit = None

    for char in line:
        if char.isnumeric():
            first_digit = int(char)
            break

    for char in reversed(line):
        if char.isnumeric():
            last_digit = int(char)
            break

    return int(f"{first_digit}{last_digit}")


def calibration_values_sum(lines: typing.List[str]) -> int:
    return sum([calibration_value(line) for line in lines])


def main():
    lines = read_input_lines("./part_one_input")
    print(
        "Sum is: ",
        calibration_values_sum(lines),
    )


main()
