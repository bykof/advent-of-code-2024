import typing

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def read_input_lines(filepath: str) -> typing.List[str]:
    with open(filepath, "r") as input_file:
        return input_file.readlines()


def find_first_digit(line: str, is_reversed=False) -> int:
    if is_reversed:
        line = "".join(reversed(line))

    for i, char in enumerate(line):
        if char.isnumeric():
            return int(char)

        for digit in DIGITS:
            starts_with_digit = digit
            if is_reversed:
                starts_with_digit = "".join(reversed(digit))

            if line[i:].startswith(starts_with_digit):
                return DIGITS[digit]
    return -1


def calibration_value(line: str) -> int:
    first_digit = None
    last_digit = None

    first_digit = find_first_digit(line)
    last_digit = find_first_digit(line, is_reversed=True)
    return int(f"{first_digit}{last_digit}")


def calibration_values_sum(lines: typing.List[str]) -> int:
    return sum([calibration_value(line) for line in lines])


def main():
    lines = read_input_lines("./part_two_input")
    print(
        "Sum is: ",
        calibration_values_sum(lines),
    )


main()
