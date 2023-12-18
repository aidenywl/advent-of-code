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

def get_number(input_data: list[str], checked: set[int, int], r: int, c: int) -> int:
    # Check left and right adding all numbers.
    col_length = len(input_data[0])
    result = input_data[r][c]
    # check to the left
    for left in range(c - 1, -1, -1):
        left_digit = input_data[r][left]
        checked.add((r, left))
        if left_digit.isdigit():
            result = left_digit + result
        else:
            break
    for right in range(c + 1, col_length):
        right_digit = input_data[r][right]
        checked.add((r, right))
        if right_digit.isdigit():
            result = result + right_digit
        else:
            break
    return int(result)


def get_gear_ratio(input_data: list[str], row_index: int, col_index: int) -> int:
    checked = set()
    adjacent_numbers = []
    max_rows = len(input_data)
    max_cols = len(input_data[0])
    for ro in [-1, 0, 1]:
        for co in [-1, 0, 1]:
            r = row_index + ro
            c = col_index + co
            if r >= max_rows or c >= max_cols or r < 0 or c < 0:
                continue
            if (r, c) in checked:
                continue
            checked.add((r, c))
            digit = input_data[r][c]
            if digit.isdigit():
                num = get_number(input_data, checked, r, c)
                adjacent_numbers.append(num)
    if len(adjacent_numbers) != 2:
        return 0
    return adjacent_numbers[0] * adjacent_numbers[1]

def part_2(input_data: list[str]) -> int:
    res = 0
    for row_index, line in enumerate(input_data):
        for col_index, digit in enumerate(line):
            if digit == "*":
                gear_ratio = get_gear_ratio(input_data, row_index, col_index)
                res += gear_ratio
    return res


if __name__ == "__main__":
    # read input
    input_file = open(helper.get_input_data_path(3))
    # Convert the input file into a list.
    test_data = input_file.readlines()
    test_data = [line.strip() for line in test_data]
    # res = get_calibration_document_code(calibration_data, False)
    # res = part_1(test_data)
    # print(res)
    res = part_2(test_data)
    print('part 2 result: ', res)
