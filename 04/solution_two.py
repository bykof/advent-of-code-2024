from copy import deepcopy
from functools import cache
import re
import typing
from dataclasses import dataclass


@dataclass
class Card:
    card_name: str
    winning_numbers: typing.List[int]
    card_numbers: typing.List[int]

    def copy(self) -> "Card":
        return deepcopy(self)

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

    def __str__(self) -> str:
        return f"{self.card_name}"


Cards = typing.List[Card]


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


def get_next_n_cards(all_cards: Cards, card_name: str, amount: int) -> Cards:
    for index, card in enumerate(all_cards):
        if card.card_name == card_name:
            to = index + amount + 1
            if to >= len(all_cards):
                to = len(all_cards)
            return all_cards[index + 1 : to]


def calculate_score(all_cards: Cards, cards: Cards) -> typing.Dict[str, int]:
    score = {}
    for card in cards:
        matching_cards = len(card.card_numbers_in_winning_numbers())
        copied_cards = list(
            map(
                lambda card: card.copy(),
                get_next_n_cards(
                    all_cards=all_cards, card_name=card.card_name, amount=matching_cards
                ),
            )
        )

        if card.card_name not in score:
            score[card.card_name] = 0

        score[card.card_name] += 1

        if len(copied_cards) != 0:
            for key, value in calculate_score(
                all_cards=all_cards, cards=copied_cards
            ).items():
                if key not in score:
                    score[key] = 0
                score[key] += value

    return score


def main():
    lines = read_input_lines("./input_two")
    cards = [read_card(line) for line in lines]
    score = calculate_score(all_cards=cards, cards=cards)
    print(f"Score is: {sum(score.values())}")


if __name__ == "__main__":
    main()
