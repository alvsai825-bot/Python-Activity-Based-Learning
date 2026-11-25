# Test cases for Case Study 39 - Exam Eligibility
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


# TC1 everything satisfied
check("Akhil eligible", solution.check_eligibility(("26C01", "Akhil", 88, 10, 32, True)), ("ELIGIBLE", []))
# TC2 exact boundary values are eligible
check("boundary 75/8/16", solution.check_eligibility(("X", "A", 75, 8, 16, True))[0], "ELIGIBLE")
# TC3 attendance 65-74 -> condonation
check("70% condonation", solution.check_eligibility(("X", "A", 70, 9, 25, True))[0], "CONDONATION")
check("65% condonation", solution.check_eligibility(("X", "A", 65, 9, 25, True))[0], "CONDONATION")
# TC4 below 65 detained
check("64% not eligible", solution.check_eligibility(("X", "A", 64, 9, 25, True))[0], "NOT ELIGIBLE")
# TC5 labs short
check("labs 7", solution.check_eligibility(("X", "A", 80, 7, 25, True))[0], "NOT ELIGIBLE")
# TC6 every failed condition is reported
status, reasons = solution.check_eligibility(("26C05", "Jaswanth", 55, 5, 10, False))
check("Jaswanth 4 reasons", len(reasons), 4)
status, reasons = solution.check_eligibility(("26C04", "Gayathri", 92, 10, 12, False))
check("Gayathri 2 reasons", len(reasons), 2)
# TC7 condonation does not hide other failures
check("70% with fee due", solution.check_eligibility(("X", "A", 70, 9, 25, False))[0], "NOT ELIGIBLE")
# TC8 invalid data
check("attendance 101", solution.check_eligibility(("X", "A", 101, 8, 30, True))[0], "INVALID")
check("internal 45", solution.check_eligibility(("X", "A", 80, 8, 45, True))[0], "INVALID")


print("-" * 40)
print("Passed :", passed, " Failed :", failed)

