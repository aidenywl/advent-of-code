from __future__ import annotations

import helper
import re

WINNING_NUMBERS_REGEX = r'(\b\d+\b)(?!:)'
CHOSEN_NUMBERS_REGEX = r'(\b\d+\b)'

def get_card_points(card_line: str) -> int:
    card_data = card_line.split("|")
    winning_nums = set([int(s) for s in re.findall(WINNING_NUMBERS_REGEX, card_data[0])])
    chosen_nums = [int(s) for s in re.findall(CHOSEN_NUMBERS_REGEX, card_data[1])]
    num_winning = 0
    for num in chosen_nums:
        if num in winning_nums:
            num_winning += 1
    if not num_winning:
        return 0
    return 2 ** (num_winning - 1)

def part_1(input_data: list[str]) -> str:
    res = 0
    for line in input_data:
        res += get_card_points(line)
    return res

if __name__ == "__main__":
    # read input
    input_file = open(helper.get_input_data_path(4))
    # Convert the input file into a list.
    test_data = input_file.readlines()
    test_data = [line.strip() for line in test_data]
    # res = get_calibration_document_code(calibration_data, False)
    res = part_1(test_data)
    print(res)