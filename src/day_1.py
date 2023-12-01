from __future__ import annotations
"""
1abc2 -> 12
pqr3stu8vwx -> 38
a1b2c3d4e5f -> 15
treb7uchet -> 77
"""

import re
import helper

NUMBER_MAP = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9
}
# REGEX to match word numbers
NUMBER_WORDS_REGEX = r'(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))'
print(NUMBER_WORDS_REGEX)
def get_calibration_value_from_line(calibration_line: str) -> int:
    first_number_letter, last_number_letter = None, None
    for letter in calibration_line:
        if letter.isdigit() and not first_number_letter:
            first_number_letter = letter
        if letter.isdigit():
            last_number_letter = letter
    assert first_number_letter is not None and last_number_letter is not None
    return int(first_number_letter + last_number_letter)

def get_calibration_document_code(calibration_data: list[str], count_words: bool) -> int:
    if not count_words:
        calibration_values = map(get_calibration_value_from_line, calibration_data)
        return sum(calibration_values)
    else:
        calibration_values = map(find_true_calibration_value, calibration_data)
        return sum(calibration_values)
    

def find_true_calibration_value(calibration_line: str) -> int:
    # Find all matches in the string
    matches = re.findall(NUMBER_WORDS_REGEX, calibration_line)
    numbers = [NUMBER_MAP[match] if match in NUMBER_MAP else match for match in matches]
    return int(str(numbers[0]) + str(numbers[-1]))

if __name__ == "__main__":
    # read input
    input_file = open(helper.get_input_data_path(1))
    # Convert the input file into a list.
    calibration_data = input_file.readlines()
    # res = get_calibration_document_code(calibration_data, False)
    # print("Part 1 answer: ", res)
    res = get_calibration_document_code(calibration_data, True)
    print("Part 2 answer: ", res)

