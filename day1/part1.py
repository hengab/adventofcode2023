# input_file_name = "sample_input.txt"
input_file_name = "input.txt"
print("--------Part 1--------")

import typing as typ
import time

start_time = time.perf_counter()

def find_first_digit(input: str) -> str:
    for c in input:
        if c.isdigit():
            return c

with open(input_file_name) as input_file:
    calibration_values = []
    for line in input_file.readlines():
        line = line.strip()
        first_digit = find_first_digit(line)
        last_digit = find_first_digit(line[::-1])
        
        calibration_value = int(f"{first_digit}{last_digit}")
        calibration_values.append(calibration_value)

    print(sum(calibration_values))
print(f"Elapsed time: {time.perf_counter() - start_time} s")