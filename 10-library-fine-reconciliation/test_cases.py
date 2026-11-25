# Test cases for Case Study 58 - Library Fine Reconciliation
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


# TC1 returned within loan period
check("returned on day 15", solution.late_days(5, 15), 0)
# TC2 exactly 14 days is not late
check("exactly 14 days", solution.late_days(10, 24), 0)
# TC3 late return
check("Ramya 6 days late", solution.late_days(10, 30), 6)
# TC4 not returned - counted till today
check("Teja not returned", solution.late_days(12, 0), 34)
# TC5 fine in first 7 days
check("fine 6 days", solution.fine_for(6), 12)
check("fine 7 days", solution.fine_for(7), 14)
# TC6 fine after 7 days
check("fine 8 days", solution.fine_for(8), 19)
check("fine 21 days", solution.fine_for(21), 84)
# TC7 maximum fine
check("fine capped at 200", solution.fine_for(45), 200)
check("no fine", solution.fine_for(0), 0)
# TC8 catalogue search with tuples
check("find B04", solution.find_book("B04"), ("B04", "Digital Logic", 1))
check("unknown book", solution.find_book("B09"), ())


print("-" * 40)
print("Passed :", passed, " Failed :", failed)

