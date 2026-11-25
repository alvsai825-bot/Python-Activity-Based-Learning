# Case Study 42 : Student Marks Matrix Analysis
# Name    : AKKALA LAKSHMI VENKATA SAI
# Roll No : 26000414
#
# Marks are stored in a nested list (matrix).
#   each row    = one student
#   each column = one subject
# Row-wise and column-wise statistics are calculated using nested loops.

SUBJECTS = ["Maths", "Physics", "Chem", "Python", "English"]
STUDENTS = ["Arjun", "Bhargavi", "Chandu", "Durga", "Ganesh", "Hema"]
PASS_MARK = 35
LOW_AVERAGE = 60

MARKS = [
    [78, 65, 70, 92, 81],
    [88, 72, 69, 95, 90],
    [45, 38, 30, 67, 58],
    [92, 81, 77, 89, 85],
    [56, 49, 52, 71, 66],
    [67, 33, 58, 84, 74],
]


def row_stats(matrix):
    # returns list of (total, average) for every student
    stats = []
    for row in matrix:
        total = 0
        for m in row:
            total = total + m
        stats.append((total, total / len(row)))
    return stats


def column_stats(matrix):
    # returns list of (average, highest, lowest, fail count) for every subject
    stats = []
    for j in range(len(matrix[0])):
        total = 0
        high = matrix[0][j]
        low = matrix[0][j]
        fails = 0
        for i in range(len(matrix)):
            m = matrix[i][j]
            total = total + m
            if m > high:
                high = m
            if m < low:
                low = m
            if m < PASS_MARK:
                fails = fails + 1
        stats.append((total / len(matrix), high, low, fails))
    return stats


def grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 55:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def main():
    rows = row_stats(MARKS)
    cols = column_stats(MARKS)

    print("=" * 72)
    print("                    STUDENT MARKS MATRIX ANALYSIS")
    print("=" * 72)
    header = f"{'Student':<10}"
    for s in SUBJECTS:
        header = header + f"{s:>8}"
    header = header + f"{'Total':>7}{'Avg':>7}{'Grd':>5}"
    print(header)
    print("-" * 72)
    for i in range(len(MARKS)):
        line = f"{STUDENTS[i]:<10}"
        for m in MARKS[i]:
            if m < PASS_MARK:
                line = line + f"{str(m) + '*':>8}"
            else:
                line = line + f"{m:>8}"
        total, avg = rows[i]
        line = line + f"{total:>7}{avg:>7.1f}{grade(avg):>5}"
        print(line)
    print("-" * 72)
    labels = ["Average", "Highest", "Lowest", "Fails"]
    for k in range(4):
        line = f"{labels[k]:<10}"
        for j in range(len(SUBJECTS)):
            value = cols[j][k]
            if k == 0:
                line = line + f"{value:>8.1f}"
            else:
                line = line + f"{value:>8}"
        print(line)
    print("(* = below pass mark 35)")

    # top performers - sort (total, name) tuples
    ranking = []
    for i in range(len(STUDENTS)):
        ranking.append((rows[i][0], STUDENTS[i]))
    ranking.sort(reverse=True)
    print()
    print("TOP 3 PERFORMERS")
    for pos in range(3):
        total, name = ranking[pos]
        print(f"  {pos + 1}. {name} - {total}/{len(SUBJECTS) * 100}")

    # subject toppers
    print()
    print("SUBJECT TOPPERS")
    for j in range(len(SUBJECTS)):
        best = 0
        for i in range(len(MARKS)):
            if MARKS[i][j] > MARKS[best][j]:
                best = i
        print(f"  {SUBJECTS[j]:<8}: {STUDENTS[best]} ({MARKS[best][j]})")

    # low performing subjects
    print()
    print(f"SUBJECTS WITH LOW AVERAGE (below {LOW_AVERAGE})")
    found = False
    for j in range(len(SUBJECTS)):
        avg, high, low, fails = cols[j]
        if avg < LOW_AVERAGE:
            found = True
            print(f"  {SUBJECTS[j]} - average {avg:.1f}, {fails} student(s) failed")
    if not found:
        print("  none")

    # class average
    class_total = 0
    for total, avg in rows:
        class_total = class_total + total
    print()
    print(f"Class average total : {class_total / len(STUDENTS):.1f}")


if __name__ == "__main__":
    main()
