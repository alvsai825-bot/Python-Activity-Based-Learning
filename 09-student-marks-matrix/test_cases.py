# Test cases for Case Study 42 - Student Marks Matrix
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


rows = solution.row_stats(solution.MARKS)
cols = solution.column_stats(solution.MARKS)
# TC1 row totals
check("Arjun total", rows[0][0], 386)
check("Durga total", rows[3][0], 424)
# TC2 row average
check("Chandu average", round(rows[2][1], 1), 47.6)
# TC3 column average
check("Maths average", round(cols[0][0], 1), 71.0)
check("Python average", round(cols[3][0], 1), 83.0)
# TC4 highest and lowest in a subject
check("Chem highest", cols[2][1], 77)
check("Chem lowest", cols[2][2], 30)
# TC5 fail count
check("Physics fails", cols[1][3], 1)
check("Maths fails", cols[0][3], 0)
# TC6 grades
check("grade 85", solution.grade(85), "A")
check("grade 77.2", solution.grade(77.2), "B")
check("grade 39.9", solution.grade(39.9), "F")
# TC7 small matrix
check("2x2 rows", solution.row_stats([[10, 20], [30, 40]]), [(30, 15.0), (70, 35.0)])
check("2x2 cols", solution.column_stats([[10, 20], [30, 40]]), [(20.0, 30, 10, 2), (30.0, 40, 20, 1)])


print("-" * 40)
print("Passed :", passed, " Failed :", failed)

