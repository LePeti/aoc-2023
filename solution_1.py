import re
from input_1 import get_input

input = get_input()


# example_input = "3asdfasd4"
# example_input = input[1]
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
