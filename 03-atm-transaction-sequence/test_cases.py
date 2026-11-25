# Test cases for Case Study 13 - ATM Transaction Sequence
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


# TC1 valid deposit
check("valid deposit", solution.check_transaction("D", 5000, 10000, 0), (True, ""))
# TC2 deposit above limit
check("deposit above 50000", solution.check_transaction("D", 60000, 10000, 0)[0], False)
# TC3 wrong type
check("invalid type X", solution.check_transaction("X", 100, 10000, 0)[1], "invalid transaction type")
# TC4 negative / zero amount
check("negative amount", solution.check_transaction("W", -500, 10000, 0)[0], False)
check("zero amount", solution.check_transaction("D", 0, 10000, 0)[0], False)
# TC5 multiple of 100
check("2550 not multiple of 100", solution.check_transaction("W", 2550, 10000, 0)[1], "amount must be a multiple of 100")
# TC6 per transaction limit
check("withdraw 25000", solution.check_transaction("W", 25000, 90000, 0)[0], False)
# TC7 daily limit
check("daily limit crossed", solution.check_transaction("W", 6000, 20000, 35000)[1], "daily limit of 40000 crossed")
# TC8 minimum balance
check("min balance 500", solution.check_transaction("W", 9600, 10000, 0)[0], False)
check("exactly 500 left is ok", solution.check_transaction("W", 9500, 10000, 0)[0], True)
# TC9 full run on sample data
balance, dep, wd, rejected, log = solution.run(solution.TRANSACTIONS)
check("closing balance", balance, 9000)
check("total deposited", dep, 37000)
check("total withdrawn", wd, 38000)
check("rejected count", rejected, 6)
# TC10 empty list
check("no transactions", solution.run([])[0], solution.OPENING_BALANCE)


print("-" * 40)
print("Passed :", passed, " Failed :", failed)

