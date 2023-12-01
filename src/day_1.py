from __future__ import annotations
"""
1abc2 -> 12
pqr3stu8vwx -> 38
a1b2c3d4e5f -> 15
treb7uchet -> 77
"""

import re
import helper


def get_calibration_value_from_line(calibration_line: str) -> int:
    first_number_letter, last_number_letter = None, None
    for letter in calibration_line:
        if letter.isdigit() and not first_number_letter:
            first_number_letter = letter
        if letter.isdigit():
            last_number_letter = letter
    assert first_number_letter is not None and last_number_letter is not None
    return int(first_number_letter + last_number_letter)

def get_calibration_document_code(calibration_data: list[str]) -> int:
    calibration_values = map(get_calibration_value_from_line, calibration_data)
    return sum(calibration_values)
    

if __name__ == "__main__":
    # read input
    input_file = open(helper.get_input_data_path(1))
    # Convert the input file into a list.
    calibration_data = input_file.readlines()
    res = get_calibration_document_code(calibration_data)
    print("Part 1 answer: ", res)

