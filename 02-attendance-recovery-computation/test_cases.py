# Test cases for Case Study 12 - Attendance Recovery
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


# TC1 percentage calculation
check("52/80 percentage", solution.percentage(52, 80), 65.0)
# TC2 zero classes conducted
check("0 classes conducted", solution.percentage(0, 0), 0.0)
# TC3 already eligible needs 0 classes
check("eligible student needs 0", solution.classes_needed(66, 80, 1, 1), 0)
# TC4 attend every class
check("Deepika every class", solution.classes_needed(58, 80, 1, 1), 8)
# TC5 9 out of 10 scenario
check("Anil 9 out of 10", solution.classes_needed(56, 80, 9, 10), 24)
# TC6 boundary - exactly all remaining classes needed
check("Charan needs all 40", solution.classes_needed(50, 80, 1, 1), 40)
# TC7 not possible returns -1
check("Eswar cannot recover", solution.classes_needed(30, 80, 1, 1), -1)
# TC8 exactly 75% counts as eligible
check("60/80 is exactly 75", solution.classes_needed(60, 80, 1, 1), 0)
# TC9 how many classes can be skipped
check("Bhavya can skip 8", solution.classes_can_skip(66, 80), 8)
check("exactly 75% can skip 0", solution.classes_can_skip(60, 80), 0)


print("-" * 40)
print("Passed :", passed, " Failed :", failed)

