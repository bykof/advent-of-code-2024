from solution_two import Card
from solution_two import read_card


def test_read_card():
    actual_card = read_card("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")
    expected_card = Card(
        card_name="Card 6",
        winning_numbers=[31, 18, 13, 56, 72],
        card_numbers=[74, 77, 10, 23, 35, 67, 36, 11],
    )
    assert actual_card.card_name == expected_card.card_name
    assert actual_card.winning_numbers == expected_card.winning_numbers
    assert actual_card.card_numbers == expected_card.card_numbers


def test_card_numbers_in_winning_numbers():
    assert (
        Card(
            card_name="Card 6",
            winning_numbers=[31, 18, 13, 56, 72],
            card_numbers=[74, 77, 10, 23, 35, 67, 36, 11],
        ).card_numbers_in_winning_numbers()
        == []
    )
    assert Card(
        card_name="Card 1",
        winning_numbers=[83, 86, 6, 3, 17, 9, 48, 53],
        card_numbers=[41, 48, 83, 86, 17],
    ).card_numbers_in_winning_numbers() == [48, 83, 86, 17]


def test_calculate_points():
    assert (
        Card(
            card_name="Card 1",
            winning_numbers=[83, 86, 6, 3, 17, 9, 48, 53],
            card_numbers=[41, 48, 83, 86, 17],
        ).calculate_points()
        == 8
    )

    assert (
        Card(
            card_name="Card 6",
            winning_numbers=[31, 18, 13, 56, 72],
            card_numbers=[74, 77, 10, 23, 35, 67, 36, 11],
        ).calculate_points()
        == 0
    )
