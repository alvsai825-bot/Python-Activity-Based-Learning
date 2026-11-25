# Case Study 12 : Attendance Recovery Computation
# Name    : AKKALA LAKSHMI VENKATA SAI
# Roll No : 26000414
#
# Finds the current attendance % of each student and the minimum number of
# classes needed to reach 75% under different future attendance scenarios.

REQUIRED = 75            # eligibility threshold in percent
REMAINING_CLASSES = 40   # classes still left in the semester

# (roll no, name, classes attended, classes conducted)
STUDENTS = [
    ("26A01", "Anil", 56, 80),
    ("26A02", "Bhavya", 66, 80),
    ("26A03", "Charan", 50, 80),
    ("26A04", "Deepika", 58, 80),
    ("26A05", "Eswar", 30, 80),
]

# scenario name, attends X classes out of every Y classes
SCENARIOS = [
    ("Attends every class", 1, 1),
    ("Attends 9 out of 10", 9, 10),
    ("Attends 4 out of 5", 4, 5),
]


def percentage(attended, conducted):
    if conducted == 0:
        return 0.0
    return attended * 100 / conducted


def classes_needed(attended, conducted, x, y):
    # simulate the future classes one by one
    # returns number of classes needed, or -1 if not possible this semester
    if percentage(attended, conducted) >= REQUIRED:
        return 0
    for k in range(1, REMAINING_CLASSES + 1):
        conducted = conducted + 1
        # inside every block of y classes the student attends the first x
        if (k - 1) % y < x:
            attended = attended + 1
        if percentage(attended, conducted) >= REQUIRED:
            return k
    return -1


def classes_can_skip(attended, conducted):
    # for students already above 75%: how many classes can be missed in a row
    skip = 0
    while percentage(attended, conducted + skip + 1) >= REQUIRED:
        skip = skip + 1
    return skip


def main():
    print("=" * 64)
    print("          ATTENDANCE RECOVERY REPORT  (threshold 75%)")
    print("=" * 64)
    print(f"Classes remaining in semester : {REMAINING_CLASSES}")
    print()
    print(f"{'Roll':<7}{'Name':<10}{'Attended':>9}{'Total':>7}{'Percent':>9}  Status")
    print("-" * 64)
    for roll, name, att, total in STUDENTS:
        pct = percentage(att, total)
        if pct >= REQUIRED:
            status = "ELIGIBLE"
        else:
            status = "SHORTAGE"
        print(f"{roll:<7}{name:<10}{att:>9}{total:>7}{pct:>8.2f}%  {status}")

    print()
    print("RECOVERY PLAN (minimum consecutive classes needed)")
    print("-" * 64)
    shortage_count = 0
    cannot_recover = []
    for roll, name, att, total in STUDENTS:
        pct = percentage(att, total)
        if pct >= REQUIRED:
            can_skip = classes_can_skip(att, total)
            print(f"{name}: already eligible, can miss {can_skip} class(es) and stay above 75%")
            continue
        shortage_count = shortage_count + 1
        print(f"{name}: current {pct:.2f}%")
        possible_any = False
        for scen_name, x, y in SCENARIOS:
            need = classes_needed(att, total, x, y)
            if need == -1:
                print(f"    {scen_name:<22}: NOT possible within {REMAINING_CLASSES} classes")
            else:
                possible_any = True
                print(f"    {scen_name:<22}: {need} classes")
        if not possible_any:
            cannot_recover.append(name)

    print("-" * 64)
    print(f"Students with shortage      : {shortage_count}")
    if len(cannot_recover) == 0:
        print("Students who cannot recover : none")
    else:
        print("Students who cannot recover :", ", ".join(cannot_recover))


if __name__ == "__main__":
    main()
