from __future__ import annotations

import helper
import re

WINNING_NUMBERS_REGEX = r'(\b\d+\b)(?!:)'
CHOSEN_NUMBERS_REGEX = r'(\b\d+\b)'
from collections import defaultdict

def get_card_points(card_line: str) -> int:
    num_winning = get_num_winning_numbers(card_line)
    if not num_winning:
        return 0
    return 2 ** (num_winning - 1)


def get_num_winning_numbers(card_line: str) -> int:
    card_data = card_line.split("|")
    winning_nums = set([int(s) for s in re.findall(WINNING_NUMBERS_REGEX, card_data[0])])
    chosen_nums = [int(s) for s in re.findall(CHOSEN_NUMBERS_REGEX, card_data[1])]
    num_winning = 0
    for num in chosen_nums:
        if num in winning_nums:
            num_winning += 1
    return num_winning

def part_1(input_data: list[str]) -> int:
    res = 0
    for line in input_data:
        res += get_card_points(line)
    return res


def part_2(input_data: list[str]) -> int:
    num_copies = defaultdict(lambda: 1)
    for card_num, line in enumerate(input_data):
        n_copies = num_copies[card_num]
        num_winning = get_num_winning_numbers(line)
        for offset in range(1, num_winning + 1):
            next_card_num = card_num + offset
            num_copies[next_card_num] += n_copies
    return sum(num_copies.values())

if __name__ == "__main__":
    # read input
    input_file = open(helper.get_input_data_path(4))
    # Convert the input file into a list.
    test_data = input_file.readlines()
    test_data = [line.strip() for line in test_data]
    # res = get_calibration_document_code(calibration_data, False)
    res = part_1(test_data)
    print(res)
    res = part_2(test_data)
    print("part 2: ", res)