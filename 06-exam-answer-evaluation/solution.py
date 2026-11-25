# Case Study 31 : String-Based Examination Answer Evaluation
# Name    : AKKALA LAKSHMI VENKATA SAI
# Roll No : 26000414
#
# Each student's answers are stored as one string. The string is compared
# with the answer key character by character.
#   correct    -> +4
#   wrong      -> -1   (negative marking)
#   '-'        -> unanswered, 0

ANSWER_KEY = "BCADABDCCA"
CORRECT_MARKS = 4
WRONG_MARKS = -1
PASS_PERCENT = 40
VALID_OPTIONS = "ABCD-"

# (roll no, name, answer string)
STUDENTS = [
    ("26B01", "Harsha", "BCADABDCCA"),
    ("26B02", "Keerthi", "BCADCBDA-A"),
    ("26B03", "Manoj", "ACBDAB--CD"),
    ("26B04", "Nikhitha", "----AB-CCA"),
    ("26B05", "Pavan", "DDDDDDDDDD"),
    ("26B06", "Rupa", "BCADAB"),
    ("26B07", "Sai Teja", "bcadabdcXa"),
]


def validate_answers(answers):
    # returns "" if okay otherwise the problem
    if len(answers) != len(ANSWER_KEY):
        return "expected " + str(len(ANSWER_KEY)) + " answers, got " + str(len(answers))
    for ch in answers:
        if ch not in VALID_OPTIONS:
            return "invalid option '" + ch + "'"
    return ""


def evaluate(answers):
    correct = 0
    wrong = 0
    unanswered = 0
    for i in range(len(ANSWER_KEY)):
        if answers[i] == "-":
            unanswered = unanswered + 1
        elif answers[i] == ANSWER_KEY[i]:
            correct = correct + 1
        else:
            wrong = wrong + 1
    score = correct * CORRECT_MARKS + wrong * WRONG_MARKS
    return correct, wrong, unanswered, score


def main():
    max_marks = len(ANSWER_KEY) * CORRECT_MARKS
    print("=" * 66)
    print("            OBJECTIVE EXAM - ANSWER SHEET EVALUATION")
    print("=" * 66)
    print("Answer key :", ANSWER_KEY)
    print(f"Marking    : +{CORRECT_MARKS} correct, {WRONG_MARKS} wrong, 0 unanswered"
          f"   Max = {max_marks}")
    print("-" * 66)
    print(f"{'Roll':<7}{'Name':<10}{'Right':>6}{'Wrong':>6}{'Blank':>6}"
          f"{'Score':>7}{'%':>8}  Result")
    print("-" * 66)

    results = []     # (score, roll, name) for valid sheets
    invalid = []
    for roll, name, answers in STUDENTS:
        answers = answers.strip().upper()   # small letters are accepted
        problem = validate_answers(answers)
        if problem != "":
            invalid.append((roll, name, problem))
            print(f"{roll:<7}{name:<10}  INVALID SHEET : {problem}")
            continue
        c, w, u, score = evaluate(answers)
        pct = score * 100 / max_marks
        if pct >= PASS_PERCENT:
            result = "PASS"
        else:
            result = "FAIL"
        results.append((score, roll, name))
        print(f"{roll:<7}{name:<10}{c:>6}{w:>6}{u:>6}{score:>7}{pct:>7.1f}%  {result}")
    print("-" * 66)

    # question wise mark of the answers (pattern line), only for valid sheets
    print("Answer pattern ( + correct, x wrong, . blank )")
    for roll, name, answers in STUDENTS:
        answers = answers.strip().upper()
        if validate_answers(answers) != "":
            continue
        line = ""
        for i in range(len(ANSWER_KEY)):
            if answers[i] == "-":
                line = line + ". "
            elif answers[i] == ANSWER_KEY[i]:
                line = line + "+ "
            else:
                line = line + "x "
        print(f"  {name:<10}{line}")

    results.sort(reverse=True)
    print("-" * 66)
    print("RANK LIST")
    rank = 1
    for score, roll, name in results:
        print(f"  {rank}. {name} ({roll}) - {score}/{max_marks}")
        rank = rank + 1
    total = 0
    for score, roll, name in results:
        total = total + score
    print(f"Class average (valid sheets) : {total / len(results):.2f}")
    print(f"Invalid answer sheets        : {len(invalid)}")


if __name__ == "__main__":
    main()
