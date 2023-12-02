from __future__ import annotations
"""
1abc2 -> 12
pqr3stu8vwx -> 38
a1b2c3d4e5f -> 15
treb7uchet -> 77
"""

import re
import helper
def is_subset_possible(subset: list[str]) -> bool:
    cube_count_map = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    for s in subset:
        play = s.split(" ")
        num, color  = int(play[0]), play[1]
        cube_count_map[color] -= num
    # check if any are negative
    for value in cube_count_map.values():
        if value < 0:
            return False
    return True


def is_game_possible(line: str) -> (bool, int):
    game_metadata = [s.strip() for s in line.split(":")]
    game_id = int(game_metadata[0].split(" ")[1])
    game_subsets = [g.strip() for g in game_metadata[1].split(";")]
    for subset in game_subsets:
        subset_list = [s.strip() for s in subset.split(",")]
        if not is_subset_possible(subset_list):
            return (False, 0)
    return (True, game_id)


def part_one(data: list[str]) -> int:
    res = 0
    for line in data:
        is_possible, game_id = is_game_possible(line)
        if is_possible:
            res += game_id
    return res

if __name__ == "__main__":
    # read input
    input_file = open(helper.get_input_data_path(2))
    # Convert the input file into a list.
    calibration_data = input_file.readlines()
    res = part_one(calibration_data)
    print("Part 1 answer: ", res)

