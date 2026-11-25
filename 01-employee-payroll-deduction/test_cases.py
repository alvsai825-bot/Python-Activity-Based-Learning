# Test cases for Case Study 4 - Employee Payroll
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


# TC1 overtime is paid at 150 per hour
check("overtime for 6 hours", solution.overtime_pay(6), 900)
# TC2 overtime above 20 hours is not paid
check("overtime capped at 20 hours", solution.overtime_pay(25), 3000)
# TC3 negative hours treated as zero
check("negative overtime hours", solution.overtime_pay(-2), 0)
# TC4 gross salary
check("gross of E101", solution.gross_salary(18000, 6, 1000)[3], 26800)
# TC5 PF is 12% of basic
check("PF for basic 14000", solution.provident_fund(14000), 1680)
# TC6 PF limit
check("PF limited to 1800", solution.provident_fund(60000), 1800)
# TC7 professional tax slabs
check("PT for 15000", solution.professional_tax(15000), 0)
check("PT for 18000", solution.professional_tax(18000), 150)
check("PT for 22700", solution.professional_tax(22700), 200)
# TC8 no income tax up to 25000
check("income tax on 22700", solution.income_tax(22700), 0)
# TC9 5% slab only on amount above 25000
check("income tax on 45600", round(solution.income_tax(45600), 2), 1030)
# TC10 10% slab
check("income tax on 66800", round(solution.income_tax(66800), 2), 2930)
# TC11 net salary
check("net salary of E105", solution.net_salary(60000, 4, 8000)[2], 81040)


print("-" * 40)
print("Passed :", passed, " Failed :", failed)

