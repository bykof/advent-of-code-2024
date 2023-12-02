from part_one import Color, Game, GameRound, read_game, sum_of_possible_game_ids


def test_game_round():
    assert Game(
        round=1,
        game_rounds=[
            GameRound(store={Color.red: 4, Color.green: 0, Color.blue: 3}),
            GameRound(store={Color.red: 1, Color.green: 2, Color.blue: 6}),
            GameRound(store={Color.red: 0, Color.green: 2, Color.blue: 0}),
        ],
    ) == read_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert Game(
        round=4,
        game_rounds=[
            GameRound(store={Color.red: 3, Color.green: 1, Color.blue: 6}),
            GameRound(store={Color.red: 6, Color.green: 3, Color.blue: 0}),
            GameRound(store={Color.red: 14, Color.green: 3, Color.blue: 15}),
        ],
    ) == read_game(
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    )


def assert_is_fitting():
    assert (
        GameRound(store={Color.red: 3, Color.green: 1, Color.blue: 6}).is_fitting
        == True
    )
    assert (
        GameRound(store={Color.red: 13, Color.green: 1, Color.blue: 6}).is_fitting
        == False
    )
    assert (
        GameRound(store={Color.red: 2, Color.green: 14, Color.blue: 6}).is_fitting
        == False
    )
    assert (
        GameRound(store={Color.red: 2, Color.green: 2, Color.blue: 15}).is_fitting
        == False
    )


def assert_is_win():
    assert (
        Game(
            round=4,
            game_rounds=[
                GameRound(store={Color.red: 3, Color.green: 1, Color.blue: 6}),
                GameRound(store={Color.red: 6, Color.green: 3, Color.blue: 0}),
                GameRound(store={Color.red: 14, Color.green: 3, Color.blue: 15}),
            ],
        ).is_win
        == False
    )

    assert (
        Game(
            round=4,
            game_rounds=[
                GameRound(store={Color.red: 3, Color.green: 1, Color.blue: 6}),
                GameRound(store={Color.red: 6, Color.green: 3, Color.blue: 0}),
                GameRound(store={Color.red: 12, Color.green: 3, Color.blue: 14}),
            ],
        ).is_win
        == True
    )


def test_sum_of_possible_game_ids():
    games = [
        Game(
            round=2,
            game_rounds=[
                GameRound(store={Color.red: 23, Color.green: 7, Color.blue: 21}),
            ],
        ),
        Game(
            round=1,
            game_rounds=[
                GameRound(store={Color.red: 5, Color.green: 4, Color.blue: 9}),
                GameRound(store={Color.red: 1, Color.green: 3, Color.blue: 7}),
            ],
        ),
        Game(
            round=4,
            game_rounds=[
                GameRound(store={Color.red: 5, Color.green: 4, Color.blue: 9}),
                GameRound(store={Color.red: 1, Color.green: 3, Color.blue: 7}),
            ],
        ),
    ]

    assert sum_of_possible_game_ids(games=games) == 5
