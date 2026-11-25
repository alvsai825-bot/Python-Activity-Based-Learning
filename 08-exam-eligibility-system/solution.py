# Case Study 39 : Multi-Stage Examination Eligibility System
# Name    : AKKALA LAKSHMI VENKATA SAI
# Roll No : 26000414
#
# A student can write the final exam only if ALL four conditions are met:
#   1. attendance >= 75%   (65% to 74% allowed after paying condonation fee)
#   2. at least 8 out of 10 lab experiments completed
#   3. internal marks >= 16 out of 40
#   4. fee is fully paid
# Every condition that is not met is reported, not just the first one.

MIN_ATTENDANCE = 75
CONDONATION_ATTENDANCE = 65
TOTAL_LABS = 10
MIN_LABS = 8
MAX_INTERNAL = 40
MIN_INTERNAL = 16

# (roll, name, attendance %, labs done, internal marks, fee paid?)
STUDENTS = [
    ("26C01", "Akhil", 88, 10, 32, True),
    ("26C02", "Bindu", 70, 9, 25, True),
    ("26C03", "Chaitanya", 80, 6, 18, True),
    ("26C04", "Gayathri", 92, 10, 12, False),
    ("26C05", "Jaswanth", 55, 5, 10, False),
    ("26C06", "Lahari", 76, 8, 16, True),
    ("26C07", "Naveen", 101, 8, 30, True),
]


def check_eligibility(student):
    # returns (status, list of reasons)
    roll, name, att, labs, internal, fee_paid = student
    reasons = []

    # input checks first
    if att < 0 or att > 100:
        return "INVALID", ["attendance value " + str(att) + " is not possible"]
    if labs < 0 or labs > TOTAL_LABS or internal < 0 or internal > MAX_INTERNAL:
        return "INVALID", ["labs or internal marks out of range"]

    condonation = False
    if att < CONDONATION_ATTENDANCE:
        reasons.append("attendance " + str(att) + "% is below 65% (detained)")
    elif att < MIN_ATTENDANCE:
        condonation = True

    if labs < MIN_LABS:
        reasons.append("only " + str(labs) + "/10 labs completed (need 8)")
    if internal < MIN_INTERNAL:
        reasons.append("internal marks " + str(internal) + "/40 (need 16)")
    if not fee_paid:
        reasons.append("fee not cleared")

    if len(reasons) > 0:
        return "NOT ELIGIBLE", reasons
    if condonation:
        return "CONDONATION", ["attendance " + str(att) + "% - pay condonation fee"]
    return "ELIGIBLE", []


def main():
    print("=" * 66)
    print("          FINAL EXAMINATION ELIGIBILITY REPORT")
    print("=" * 66)
    print(f"{'Roll':<7}{'Name':<11}{'Att%':>5}{'Labs':>6}{'Int':>5}{'Fee':>6}  Status")
    print("-" * 66)

    eligible = 0
    condonation = 0
    not_eligible = 0
    invalid = 0
    # count of each reason type
    att_fail = 0
    lab_fail = 0
    int_fail = 0
    fee_fail = 0

    for student in STUDENTS:
        roll, name, att, labs, internal, fee_paid = student
        status, reasons = check_eligibility(student)
        fee_text = "Paid" if fee_paid else "Due"
        print(f"{roll:<7}{name:<11}{att:>5}{labs:>6}{internal:>5}{fee_text:>6}  {status}")
        for r in reasons:
            print("        -", r)
            if "detained" in r:
                att_fail = att_fail + 1
            elif "labs" in r:
                lab_fail = lab_fail + 1
            elif "internal" in r:
                int_fail = int_fail + 1
            elif "fee not" in r:
                fee_fail = fee_fail + 1

        if status == "ELIGIBLE":
            eligible = eligible + 1
        elif status == "CONDONATION":
            condonation = condonation + 1
        elif status == "NOT ELIGIBLE":
            not_eligible = not_eligible + 1
        else:
            invalid = invalid + 1

    print("-" * 66)
    print("SUMMARY")
    print(f"Eligible                  : {eligible}")
    print(f"Eligible with condonation : {condonation}")
    print(f"Not eligible              : {not_eligible}")
    print(f"Invalid records           : {invalid}")
    print("Unmet requirement count   :")
    print(f"   attendance below 65%   : {att_fail}")
    print(f"   labs incomplete        : {lab_fail}")
    print(f"   low internal marks     : {int_fail}")
    print(f"   fee pending            : {fee_fail}")


if __name__ == "__main__":
    main()
