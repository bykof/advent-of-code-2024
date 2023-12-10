import typing
from dataclasses import dataclass


@dataclass
class Seed:
    value: int
    state: str = "seed"


Seeds = typing.List[Seed]


@dataclass
class Range:
    destination_range_start: int
    source_range_start: int
    range_length: int

    def translate(self, value: int) -> int:
        if (
            self.source_range_start
            <= value
            <= self.source_range_start + self.range_length - 1
        ):
            return self.destination_range_start + (value - self.source_range_start)

        return value


Ranges = typing.List[Range]


@dataclass
class Map:
    name: str
    ranges: Ranges

    def source(self) -> str:
        return self.name.split("-to-")[0]

    def target(self) -> str:
        return self.name.split("-to-")[1]

    def seed_matches(self, seed: Seed) -> bool:
        return self.source() == seed.state

    def translate(self, seed: Seed) -> Seed:
        seed.state = self.target()
        initial_value = seed.value

        for range in self.ranges:
            translated_value = range.translate(value=initial_value)

            if translated_value != initial_value:
                seed.value = translated_value

        return seed


Maps = typing.List[Map]


def read_input_lines(filepath: str) -> typing.List[str]:
    with open(filepath, "r") as input_file:
        return input_file.read().split("\n")


def read_maps(lines: typing.List[str]) -> Maps:
    maps = []
    map = None

    for line in lines[2:]:
        if "map:" in line:
            if map is not None:
                maps.append(map)
            map = Map(name=line.replace(" map:", ""), ranges=[])
        else:
            if map is not None and line != "":
                destination, source, range = line.split(" ")
                range = Range(
                    destination_range_start=int(destination),
                    source_range_start=int(source),
                    range_length=int(range),
                )
                map.ranges.append(range)
    maps.append(map)
    return maps


def read_seeds(lines: typing.List[str]) -> Seeds:
    return [
        Seed(value=int(part)) for part in lines[0].replace("seeds: ", "").split(" ")
    ]


def find_map_and_translate(maps: Maps, seed: Seed) -> typing.Tuple[Seed, bool]:
    for map in maps:
        if map.seed_matches(seed=seed):
            return map.translate(seed=seed), True
    return seed, False


def traverse_maps_with_seed(maps: Maps, seed: Seed) -> Seed:
    seed, found_map = find_map_and_translate(maps=maps, seed=seed)
    while found_map:
        seed, found_map = find_map_and_translate(maps=maps, seed=seed)
    return seed


def main():
    lines = read_input_lines("./input")
    maps = read_maps(lines=lines)
    seeds = read_seeds(lines=lines)
    seeds = [traverse_maps_with_seed(seed=seed, maps=maps) for seed in seeds]
    lowest_seed = None

    for seed in seeds:
        if lowest_seed is None:
            lowest_seed = seed
            continue

        if lowest_seed.value > seed.value:
            lowest_seed = seed
    print(f"Lowest seed is: {lowest_seed}")


if __name__ == "__main__":
    main()
