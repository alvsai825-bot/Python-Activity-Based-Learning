# Test cases for Case Study 25 - Progressive Water Tariff
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


# TC1 first slab only
check("8 KL charge", solution.water_charge(8), 56)
# TC2 exactly 10 KL
check("10 KL charge", solution.water_charge(10), 70)
# TC3 two slabs  70 + 8*11
check("18 KL charge", solution.water_charge(18), 158)
# TC4 three slabs  70 + 110 + 6*18
check("26 KL charge", solution.water_charge(26), 288)
# TC5 four slabs  70 + 110 + 180 + 15*25
check("45 KL charge", solution.water_charge(45), 735)
# TC6 zero usage
check("0 KL charge", solution.water_charge(0), 0)
# TC7 no penalty at exactly 30 KL
check("30 KL no excess penalty", solution.calculate_bill(30, False)[1], 0)
# TC8 excess penalty above 30 KL
check("34 KL excess penalty", solution.calculate_bill(34, False)[1], 100)
# TC9 late fee 2%
check("late fee for H-104", solution.calculate_bill(12, True)[2], 3.04)
# TC10 total bill
check("total bill H-103", solution.calculate_bill(34, True)[3], 632.4)
check("total bill H-101", solution.calculate_bill(8, False)[3], 116)


print("-" * 40)
print("Passed :", passed, " Failed :", failed)

