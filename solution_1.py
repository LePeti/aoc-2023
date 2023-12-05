import re

from input_1 import get_input

input = get_input()


# 1/1
def return_digits(input_string):
    first_number_pattern = "^[a-z]*(\\d)"
    last_number_pattern = "[a-z0-9]*(\\d)[a-z]*$"

    first_digit = re.match(first_number_pattern, input_string).group(1)
    last_digit = re.match(last_number_pattern, input_string).group(1)

    double_digit = int(first_digit + last_digit)

    print(f"{input_string}\n{double_digit}")

    return double_digit


double_digits = [return_digits(line) for line in input]

print(f"solution: {sum(double_digits)}")


# 1/2
def return_digits_new(input_string):
    letter_digit_map = {
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
    letter_digit_pattern = "|".join(letter_digit_map.keys())
    first_number_pattern = f"[a-z]*?(\\d|{letter_digit_pattern})"
    last_number_pattern = f"[a-z0-9]*(\\d|{letter_digit_pattern})[a-z]*$"

    first_digit = re.match(first_number_pattern, input_string).group(1)
    last_digit = re.match(last_number_pattern, input_string).group(1)

    if len(first_digit) > 1:
        first_digit = letter_digit_map.get(first_digit)
    if len(last_digit) > 1:
        last_digit = letter_digit_map.get(last_digit)

    double_digit = int(first_digit + last_digit)

    print(f"{input_string}\n{double_digit}")

    return double_digit


double_digits = [return_digits_new(line) for line in input]

print(f"solution: {sum(double_digits)}")
