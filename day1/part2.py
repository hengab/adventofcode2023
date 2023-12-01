# input_file_name = "sample_input_2.txt"
input_file_name = "input.txt"
print("--------Part 2--------")

import typing as typ
import time

start_time = time.perf_counter()

digits = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_first_digit(input: str, reverse: bool) -> str:
    for index in range(len(input)):
        for digit in digits:
            key = digit[::-1] if reverse else digit
            if input[index::].startswith(key):
                return digits[digit]


with open(input_file_name) as input_file:
    calibration_values = []

    for line in input_file.readlines():
        line = line.strip()
        first_digit = find_first_digit(line, False)
        last_digit = find_first_digit(line[::-1], True)

        calibration_value = int(f"{first_digit}{last_digit}")
        calibration_values.append(calibration_value)

    print(sum(calibration_values))
print(f"Elapsed time: {time.perf_counter() - start_time} s")
