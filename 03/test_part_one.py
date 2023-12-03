from part_one import (
    contains_symbol,
    find_part_numbers,
    get_number_from_index,
    read_schematic,
    sum_part_numbers,
)


def test_get_number_from_index():
    assert get_number_from_index(read_schematic(["617.*..534.."]), 0, 0) == (617, [0, 1, 2])
    assert get_number_from_index(read_schematic(["617.*..534.."]), 0, 1) == (617, [0, 1, 2])
    assert get_number_from_index(read_schematic(["617.*..534.."]), 0, 2) == (617, [0, 1, 2])
    assert get_number_from_index(read_schematic(["617.*..534.."]), 0, 7) == (534, [7, 8, 9])
    assert get_number_from_index(read_schematic(["617.*..534.."]), 0, 8) == (534, [7, 8, 9])
    assert get_number_from_index(read_schematic(["617.*..534.."]), 0, 9) == (534, [7, 8, 9])


def test_find_vertical_part_numbers():
    assert find_part_numbers(read_schematic(["..35..633.", "......#..."])) == [
        633
    ]

    assert find_part_numbers(read_schematic(["...$.*....", ".664.598.."])) == [
        664,
        598,
    ]

    assert find_part_numbers(read_schematic(["....*.....", ".664.598.."])) == [
        664,
        598,
    ]


def test_read_schematic():
    assert read_schematic(
        [
            "467..114..",
            "...*......",
        ]
    ) == [
        ["4", "6", "7", ".", ".", "1", "1", "4", ".", "."],
        [
            ".",
            ".",
            ".",
            "*",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
        ],
    ]


def test_contains_symbol():
    assert contains_symbol("a") == False
    assert contains_symbol("1") == False
    assert contains_symbol(".") == False
    assert contains_symbol("&") == True
    assert contains_symbol("#") == True
    assert contains_symbol("+") == True
    assert contains_symbol("$") == True
    assert contains_symbol("$1") == True
    assert contains_symbol("1$") == True


def test_sum_part_numbers():
    lines = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()
    schematic = read_schematic(lines=lines)
    assert sum_part_numbers(schematic=schematic) == 4361
