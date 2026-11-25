# Test cases for Case Study 35 - Text Compression (RLE)
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


# TC1 normal encoding
check("encode AAAABBBCCDAA", solution.encode("AAAABBBCCDAA"), "A4B3C2D1A2")
# TC2 counts with 2 digits
check("encode 15 z", solution.encode("z" * 15), "z15")
# TC3 no repeats - encoded becomes longer
check("encode ABCDEF", solution.encode("ABCDEF"), "A1B1C1D1E1F1")
# TC4 case sensitive
check("encode aaAA", solution.encode("aaAA"), "a2A2")
# TC5 empty string and single character
check("encode empty", solution.encode(""), "")
check("encode single char", solution.encode("x"), "x1")
# TC6 spaces are characters too
check("encode with spaces", solution.encode("a   b"), "a1 3b1")
# TC7 decode
check("decode W12B1", solution.decode("W12B1"), "W" * 12 + "B")
check("decode back", solution.decode(solution.encode("hello world")), "hello world")
# TC8 comparison remarks
check("beneficial", solution.compare("AAAA", "A4")[1], "beneficial")
check("no gain", solution.compare("aaAA", "a2A2")[1], "no gain")
check("not beneficial", solution.compare("AB", "A1B1")[1], "NOT beneficial (encoded is longer)")
# TC9 digits rejected
check("digits rejected", solution.is_valid("room 101"), False)
check("letters accepted", solution.is_valid("room"), True)


print("-" * 40)
print("Passed :", passed, " Failed :", failed)

