from dataclasses import dataclass
import enum
import typing


class Color(str, enum.Enum):
    red = "red"
    green = "green"
    blue = "blue"


@dataclass
class GameRound:
    store: dict[Color, int]

    @property
    def is_fitting(self):
        return (
            self.store[Color.green] <= 13
            and self.store[Color.red] <= 12
            and self.store[Color.blue] <= 14
        )


@dataclass
class Game:
    round: int
    game_rounds: typing.List[GameRound]

    def power_of_maximum_colors(self) -> int:
        maximum_colors = {color.name: 0 for color in Color}
        for game_round in self.game_rounds:
            for color in Color:
                value = game_round.store[color]
                if maximum_colors[color] < value:
                    maximum_colors[color] = value
        power = 0
        for value in maximum_colors.values():
            if power == 0:
                power = value
                continue

            power *= value
        print("Game: ", self.round, " - power: ", power)
        return power

    @property
    def is_win(self):
        for game_round in self.game_rounds:
            if not game_round.is_fitting:
                return False
        return True


# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def read_game(line: str) -> Game:
    game_meta, rounds = line.split(":")

    game_rounds = []
    for round in rounds.split(";"):
        store = {color.value: 0 for color in Color}
        color_counts = round.split(",")
        for color_count in color_counts:
            count, color = color_count.strip().split(" ")
            store[color] += int(count)
        game_rounds.append(
            GameRound(
                store=store,
            )
        )
    return Game(round=int(game_meta.replace("Game ", "")), game_rounds=game_rounds)


def read_games(input_lines: typing.List[str]) -> typing.List[Game]:
    return [read_game(input_line) for input_line in input_lines]


def sum_of_power(games: typing.List[Game]) -> int:
    return sum([game.power_of_maximum_colors() for game in games])


def read_input_lines(filepath: str) -> typing.List[str]:
    with open(filepath, "r") as input_file:
        return input_file.readlines()


def main():
    input_lines = read_input_lines("./part_two_input")
    game_rounds = read_games(input_lines=input_lines)
    result = sum_of_power(games=game_rounds)
    print(f"Result is: {result}")


main()
