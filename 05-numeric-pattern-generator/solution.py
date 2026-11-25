# Case Study 27 : Advanced Numeric Pattern Generator
# Name    : AKKALA LAKSHMI VENKATA SAI
# Roll No : 26000414
#
# Prints a hollow number diamond and a symmetric number pyramid for the
# size given by the user. Invalid sizes are rejected with a message.
#
# Run normally  : python3 solution.py          (uses the sample sizes)
# Own input     : python3 solution.py ask      (asks for the size)

import sys

MIN_SIZE = 1
MAX_SIZE = 9      # above 9 the numbers become 2 digits and alignment breaks


def validate_size(text):
    # returns (True, size, "") or (False, 0, error message)
    text = text.strip()
    if text == "":
        return False, 0, "size cannot be empty"
    if text[0] == "-" and text[1:].isdigit():
        return False, 0, "size cannot be negative"
    if not text.isdigit():
        return False, 0, "size must be a whole number"
    n = int(text)
    if n < MIN_SIZE or n > MAX_SIZE:
        return False, 0, "size must be between 1 and 9"
    return True, n, ""


def hollow_diamond(n):
    # row i shows the number i only at the two edges
    lines = []
    for i in range(1, n + 1):
        line = " " * (n - i) + str(i)
        if i > 1:
            line = line + " " * (2 * i - 3) + str(i)
        lines.append(line)
    for i in range(n - 1, 0, -1):
        line = " " * (n - i) + str(i)
        if i > 1:
            line = line + " " * (2 * i - 3) + str(i)
        lines.append(line)
    return lines


def number_pyramid(n):
    # 1, 121, 12321, ... centred
    lines = []
    for i in range(1, n + 1):
        line = " " * (n - i)
        for j in range(1, i + 1):
            line = line + str(j)
        for j in range(i - 1, 0, -1):
            line = line + str(j)
        lines.append(line)
    return lines


def show_patterns(text):
    print(f"Input size : '{text}'")
    ok, n, msg = validate_size(text)
    if not ok:
        print("  INVALID ->", msg)
        print()
        return
    print(f"Hollow diamond (n = {n}):")
    for line in hollow_diamond(n):
        print("  " + line)
    print(f"Symmetric pyramid (n = {n}):")
    for line in number_pyramid(n):
        print("  " + line)
    print()


def main():
    print("=" * 40)
    print("     NUMERIC PATTERN GENERATOR")
    print("=" * 40)
    if len(sys.argv) > 1 and sys.argv[1] == "ask":
        size = input("Enter size (1-9): ")
        show_patterns(size)
    else:
        sample_inputs = ["5", "0", "abc", "12", "-3", "3"]
        for s in sample_inputs:
            show_patterns(s)


if __name__ == "__main__":
    main()
