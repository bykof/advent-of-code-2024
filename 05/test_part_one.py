import typing

from part_one import (
    Map,
    Range,
    Seed,
    find_map_and_translate,
    read_maps,
    read_seeds,
    traverse_maps_with_seed,
)


def read_test_input() -> typing.List[str]:
    with open("./test_input") as test_input_file:
        return test_input_file.read().split("\n")


def test_read_seeds():
    test_input = read_test_input()
    assert read_seeds(test_input) == [
        Seed(value=79),
        Seed(value=14),
        Seed(value=55),
        Seed(value=13),
    ]


def test_read_maps():
    test_input = read_test_input()
    maps = read_maps(test_input)
    assert len(maps) == 7
    assert len(maps[0].ranges) == 2
    assert len(maps[1].ranges) == 3
    assert len(maps[2].ranges) == 4
    assert len(maps[3].ranges) == 2
    assert len(maps[4].ranges) == 3
    assert len(maps[5].ranges) == 2
    assert len(maps[6].ranges) == 2

    assert maps[0].name == "seed-to-soil"
    assert maps[0].ranges[0] == Range(
        destination_range_start=50, source_range_start=98, range_length=2
    )
    assert maps[0].ranges[1] == Range(
        destination_range_start=52, source_range_start=50, range_length=48
    )


def test_translate():
    assert (
        Range(
            destination_range_start=52,
            source_range_start=50,
            range_length=48,
        ).translate(79)
        == 81
    )

    assert (
        Range(
            destination_range_start=52,
            source_range_start=50,
            range_length=48,
        ).translate(79)
        == 81
    )

    assert (
        Range(
            destination_range_start=52,
            source_range_start=50,
            range_length=48,
        ).translate(14)
        == 14
    )

    assert (
        Range(
            destination_range_start=52,
            source_range_start=50,
            range_length=48,
        ).translate(55)
        == 57
    )

    assert (
        Range(
            destination_range_start=52,
            source_range_start=50,
            range_length=48,
        ).translate(13)
        == 13
    )


def test_map_seed_matches():
    seed = Seed(state="seed", value=0)
    map = Map(
        name="seed-to-soil",
        ranges=[
            Range(
                destination_range_start=50,
                source_range_start=98,
                range_length=2,
            ),
            Range(
                destination_range_start=52,
                source_range_start=50,
                range_length=48,
            ),
        ],
    )
    assert map.seed_matches(seed=seed) is True


def test_map_translate():
    map = Map(
        name="seed-to-soil",
        ranges=[
            Range(
                destination_range_start=50,
                source_range_start=98,
                range_length=2,
            ),
            Range(
                destination_range_start=52,
                source_range_start=50,
                range_length=48,
            ),
        ],
    )

    assert map.translate(Seed(value=79)) == Seed(value=81, state="soil")
    assert map.translate(Seed(value=14)) == Seed(value=14, state="soil")
    assert map.translate(Seed(value=55)) == Seed(value=57, state="soil")
    assert map.translate(Seed(value=13)) == Seed(value=13, state="soil")


def test_find_map_and_translate():
    maps = [
        Map(
            name="seed-to-soil",
            ranges=[
                Range(
                    destination_range_start=50,
                    source_range_start=98,
                    range_length=2,
                ),
                Range(
                    destination_range_start=52,
                    source_range_start=50,
                    range_length=48,
                ),
            ],
        ),
        Map(
            name="soil-to-fertilizer",
            ranges=[
                Range(
                    destination_range_start=0,
                    source_range_start=15,
                    range_length=37,
                ),
                Range(
                    destination_range_start=37,
                    source_range_start=52,
                    range_length=2,
                ),
                Range(
                    destination_range_start=39,
                    source_range_start=0,
                    range_length=15,
                ),
            ],
        ),
    ]

    assert find_map_and_translate(maps=maps, seed=Seed(value=79)) == (
        Seed(value=81, state="soil"),
        True,
    )
    assert find_map_and_translate(maps=maps, seed=Seed(value=81, state="soil")) == (
        Seed(value=81, state="fertilizer"),
        True,
    )


def test_traverse_maps_with_seed():
    maps = read_maps(read_test_input())

    assert traverse_maps_with_seed(maps=maps, seed=Seed(value=79)) == Seed(
        value=82, state="location"
    )
    assert traverse_maps_with_seed(maps=maps, seed=Seed(value=14)) == Seed(
        value=43, state="location"
    )
    assert traverse_maps_with_seed(maps=maps, seed=Seed(value=55)) == Seed(
        value=86, state="location"
    )
    assert traverse_maps_with_seed(maps=maps, seed=Seed(value=13)) == Seed(
        value=35, state="location"
    )
