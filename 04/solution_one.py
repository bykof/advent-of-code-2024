import re
import typing
from dataclasses import dataclass


@dataclass
class Card:
    card_name: str
    winning_numbers: typing.List[int]
    card_numbers: typing.List[int]

    def card_numbers_in_winning_numbers(self) -> typing.List[int]:
        return [
            card_number
            for card_number in self.card_numbers
            if card_number in self.winning_numbers
        ]

    def calculate_points(self) -> int:
        amount_winning_cards = len(self.card_numbers_in_winning_numbers())
        if amount_winning_cards <= 0:
            return 0

        return pow(2, (amount_winning_cards - 1))


def read_card(line: str) -> Card:
    card_name, values = line.split(": ")
    winning_numbers, card_numbers = values.split(" | ")
    return Card(
        card_name=card_name,
        winning_numbers=list(
            map(
                lambda x: int(x),
                [
                    number
                    for number in re.split(r"(\d+)", winning_numbers)
                    if number.isnumeric()
                ],
            )
        ),
        card_numbers=list(
            map(
                lambda x: int(x),
                [
                    number
                    for number in re.split(r"(\d+)", card_numbers)
                    if number.isnumeric()
                ],
            )
        ),
    )


def read_input_lines(filepath: str) -> typing.List[str]:
    with open(filepath, "r") as input_file:
        return input_file.read().split("\n")


def calculate_score(cards: typing.List[Card]) -> int:
    score = 0
    for card in cards:
        current_score = card.calculate_points()
        print(f"{card.card_name} has score: {current_score}")
        score += current_score
    return score


def main():
    lines = read_input_lines("./input_one")
    cards = [read_card(line) for line in lines]
    score = calculate_score(cards=cards)
    print(f"Score is: {score}")


if __name__ == "__main__":
    main()
