"""
Test Program
"""


def decimal_to_hexadecimal(decimal_number):
    """
    Converts a decimal number to hexadecimal.
    Args:
    decimal_number: The decimal number to convert.
    Returns:
    The hexadecimal equivalent of the decimal number.
    """
    hexadecimal_digits = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]
    hexadecimal = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal = hexadecimal_digits[remainder] + hexadecimal
        decimal_number //= 16
    return "0x" + hexadecimal


print(decimal_to_hexadecimal(10))
print(decimal_to_hexadecimal(257))
