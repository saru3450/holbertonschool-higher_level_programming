#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
    numb = 0
    previous_value = 0
    for char in roman_string:
        value = roman_numbers[char]
        if value > previous_value:
            numb += value - 2 * previous_value
        else:
            numb += value
            previous_value = value
    return numb
