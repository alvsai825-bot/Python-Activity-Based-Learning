# Test cases for Case Study 27 - Numeric Pattern Generator
# Run: python3 test_cases.py

import solution

passed = 0
failed = 0


def check(test_name, result, expected):
    global passed, failed
    if result == expected:
        passed = passed + 1
        print("PASS :", test_name)
    else:
        failed = failed + 1
        print("FAIL :", test_name, "| expected", expected, "got", result)


# TC1 valid size
check("size 5 valid", solution.validate_size("5"), (True, 5, ""))
# TC2 spaces around the number are ignored
check("size with spaces", solution.validate_size(" 4 "), (True, 4, ""))
# TC3 invalid inputs
check("size 0", solution.validate_size("0")[0], False)
check("size 12", solution.validate_size("12")[0], False)
check("size abc", solution.validate_size("abc")[2], "size must be a whole number")
check("size -3", solution.validate_size("-3")[2], "size cannot be negative")
check("empty size", solution.validate_size("")[2], "size cannot be empty")
check("decimal 2.5", solution.validate_size("2.5")[0], False)
# TC4 diamond has 2n-1 lines
check("diamond lines for n=5", len(solution.hollow_diamond(5)), 9)
# TC5 diamond shape for n=3
check("diamond n=3", solution.hollow_diamond(3), ["  1", " 2 2", "3   3", " 2 2", "  1"])
# TC6 diamond n=1
check("diamond n=1", solution.hollow_diamond(1), ["1"])
# TC7 pyramid
check("pyramid n=3", solution.number_pyramid(3), ["  1", " 121", "12321"])
# TC8 last row of pyramid n=9
check("pyramid n=9 last row", solution.number_pyramid(9)[-1], "12345678987654321")


print("-" * 40)
print("Passed :", passed, " Failed :", failed)

