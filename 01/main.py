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


def main():
    lines = read_input_lines("./input")
    print("Sum is: ", sum([calibration_value(line) for line in lines]))


main()
