# Test cases for Case Study 31 - Exam Answer Evaluation
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


# TC1 all correct
check("all correct", solution.evaluate("BCADABDCCA"), (10, 0, 0, 40))
# TC2 all unanswered
check("all blank", solution.evaluate("----------"), (0, 0, 10, 0))
# TC3 mixed answers
check("Keerthi", solution.evaluate("BCADCBDA-A"), (7, 2, 1, 26))
# TC4 negative marking
check("Pavan score", solution.evaluate("DDDDDDDDDD")[3], 0)
check("all wrong gives -10", solution.evaluate("ABCABCABAB")[3], -10)
# TC5 validation
check("valid sheet", solution.validate_answers("BCADAB--CA"), "")
check("short sheet", solution.validate_answers("BCADAB"), "expected 10 answers, got 6")
check("invalid letter", solution.validate_answers("BCADABDCXA"), "invalid option 'X'")
check("small letters invalid before upper()", solution.validate_answers("bcadabdcca") != "", True)
# TC6 lowercase converted in main gives same result
check("lowercase converted", solution.evaluate("bcadabdcca".upper())[3], 40)


print("-" * 40)
print("Passed :", passed, " Failed :", failed)

