from __future__ import annotations

import re
import helper

def is_symbol(item: str):
    return not item.isalnum()

def calc_is_adjacent_to_symbol(input_data: list[str], row_index: int, col_index: str):
    max_rows = len(input_data)
    max_cols = len(input_data[0])
    for r_offset in [-1, 0, 1]:
        for c_offset in [-1, 0, 1]:
            if r_offset == 0 and c_offset == 0:
                continue
            r = row_index + r_offset
            c = col_index + c_offset
            if r >= max_rows or c >= max_cols or r < 0 or c < 0:
                continue
            adjacent_item = input_data[r][c]
            if not adjacent_item.isalnum() and adjacent_item != '.':
                return True
    return False

def part_1(input_data: list[str]) -> int:
    col_length = len(input_data[0])
    res = 0
    for row_index, line in enumerate(input_data):
        number = ""
        is_adjacent_to_symbol = False
        numbers_in_line: list((int, bool)) = []
        print("line is: ", line)
        for col_index, digit in enumerate(line):
            # if digit check if the digit is numeric and append
            if digit.isdigit():
                number += digit
                is_adjacent_to_symbol |= calc_is_adjacent_to_symbol(input_data, row_index, col_index)
            # Handle case where this is a full number by itself.
            if not digit.isdigit() or col_index == col_length - 1:
                if not number.isdigit():
                    is_adjacent_to_symbol = False
                    continue
                numbers_in_line.append((int(number), is_adjacent_to_symbol))
                is_adjacent_to_symbol = False
                number = ""
        # For all the numbers in line, if it's adjacent add to result.
        for num, is_adj in numbers_in_line:
            if is_adj:
                res += num
    return res

if __name__ == "__main__":
    # read input
    input_file = open(helper.get_input_data_path(3))
    # Convert the input file into a list.
    test_data = input_file.readlines()
    test_data = [line.strip() for line in test_data]
    # res = get_calibration_document_code(calibration_data, False)
    res = part_1(test_data)
    print(res)
