import typing

Schematic = typing.List[typing.List[str]]
Numbers = typing.List[int]
SYMBOL_REGEX = r"\W(?<![.])"


def contains_symbol(value: str) -> bool:
    return value == "*"


def get_number_from_index(
    schematic: Schematic, y: int, x: int
) -> typing.Tuple[int, Numbers]:
    number = [schematic[y][x]]
    walked_x_indices = [x]
    if x > 0:
        for x_left in range(x - 1, -1, -1):
            value = schematic[y][x_left]

            if value.isnumeric():
                walked_x_indices.append(x_left)
                number.insert(0, value)
            else:
                break

    if x < len(schematic[y]):
        for x_right in range(x + 1, len(schematic[y])):
            value = schematic[y][x_right]

            if value.isnumeric():
                walked_x_indices.append(x_right)
                number.append(value)
            else:
                break
    return int("".join(number)), list(sorted(walked_x_indices))


def x_indices_not_in_found_indices(x_indices: Numbers, found_indices: Numbers) -> bool:
    return not all([x_index in found_indices for x_index in x_indices])


def find_part_numbers(schematic: Schematic) -> Numbers:
    found_numbers = []

    for y in range(len(schematic)):
        for x in range(len(schematic[y])):
            if contains_symbol(schematic[y][x]):
                adjacent_numbers = []

                if x - 1 >= 0:
                    if schematic[y][x - 1].isnumeric():
                        number, _ = get_number_from_index(
                            schematic=schematic, y=y, x=x - 1
                        )
                        adjacent_numbers.append(number)
                if x + 1 < len(schematic[y]):
                    if schematic[y][x + 1].isnumeric():
                        number, _ = get_number_from_index(
                            schematic=schematic, y=y, x=x + 1
                        )

                        adjacent_numbers.append(number)

                if y - 1 >= 0:
                    if schematic[y - 1][x].isnumeric():
                        number, _ = get_number_from_index(
                            schematic=schematic, y=y - 1, x=x
                        )
                        adjacent_numbers.append(number)

                    else:
                        if x - 1 >= 0 and schematic[y - 1][x - 1].isnumeric():
                            number, _ = get_number_from_index(
                                schematic=schematic, y=y - 1, x=x - 1
                            )

                            adjacent_numbers.append(number)

                        if (
                            x + 1 < len(schematic[y - 1])
                            and schematic[y - 1][x + 1].isnumeric()
                        ):
                            number, _ = get_number_from_index(
                                schematic=schematic, y=y - 1, x=x + 1
                            )
                            adjacent_numbers.append(number)
                if y + 1 < len(schematic):
                    if schematic[y + 1][x].isnumeric():
                        number, _ = get_number_from_index(
                            schematic=schematic, y=y + 1, x=x
                        )
                        adjacent_numbers.append(number)

                    else:
                        if x - 1 >= 0 and schematic[y + 1][x - 1].isnumeric():
                            number, _ = get_number_from_index(
                                schematic=schematic, y=y + 1, x=x - 1
                            )
                            adjacent_numbers.append(number)

                        if (
                            x + 1 < len(schematic[y + 1])
                            and schematic[y + 1][x + 1].isnumeric()
                        ):
                            number, _ = get_number_from_index(
                                schematic=schematic, y=y + 1, x=x + 1
                            )
                            adjacent_numbers.append(number)

                if len(adjacent_numbers) == 2:
                    found_numbers.append(adjacent_numbers[0] * adjacent_numbers[1])
    return found_numbers


def read_schematic(lines: typing.List[str]) -> Schematic:
    return [list(line) for line in lines]


def read_input_lines(filepath: str) -> typing.List[str]:
    with open(filepath, "r") as input_file:
        return input_file.read().split("\n")


def sum_part_numbers(schematic: Schematic) -> int:
    return sum(find_part_numbers(schematic=schematic))


def main():
    lines = read_input_lines("./part_one_input")
    schematic = read_schematic(lines)
    result = sum_part_numbers(schematic=schematic)
    print(f"Result is: {result}")


main()
