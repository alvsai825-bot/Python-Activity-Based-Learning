# Case Study 58 : Library Borrowing and Fine Reconciliation
# Name    : AKKALA LAKSHMI VENKATA SAI
# Roll No : 26000414
#
# Borrowing records are tuples. Days are counted as day numbers of the
# semester (day 1, day 2 ...). A return day of 0 means not yet returned.
#
# Fine rules:
#   loan period 14 days
#   Rs 2 per day for the first 7 late days
#   Rs 5 per day after that
#   maximum fine Rs 200 per book

TODAY = 60
LOAN_DAYS = 14
FIRST_RATE = 2
FIRST_DAYS = 7
LATER_RATE = 5
MAX_FINE = 200

# catalogue : (book id, title, number of copies)
CATALOGUE = (
    ("B01", "Python Basics", 3),
    ("B02", "Data Structures", 2),
    ("B03", "Engg Maths", 2),
    ("B04", "Digital Logic", 1),
    ("B05", "C Programming", 2),
)

# borrow records : (record no, book id, member, issue day, return day)
RECORDS = (
    (1, "B01", "Sai", 5, 15),
    (2, "B01", "Ramya", 10, 30),
    (3, "B02", "Teja", 12, 0),
    (4, "B03", "Vamsi", 20, 31),
    (5, "B04", "Pooja", 25, 0),
    (6, "B02", "Manasa", 40, 0),
    (7, "B05", "Rahul", 1, 60),
    (8, "B04", "Kavya", 30, 0),
    (9, "B03", "Sai", 50, 0),
    (10, "B09", "Ajay", 15, 20),
)


def late_days(issue, ret):
    # if the book is not returned, count till today
    if ret == 0:
        ret = TODAY
    days_kept = ret - issue
    if days_kept > LOAN_DAYS:
        return days_kept - LOAN_DAYS
    return 0


def fine_for(days_late):
    if days_late <= 0:
        return 0
    if days_late <= FIRST_DAYS:
        fine = days_late * FIRST_RATE
    else:
        fine = FIRST_DAYS * FIRST_RATE + (days_late - FIRST_DAYS) * LATER_RATE
    if fine > MAX_FINE:
        fine = MAX_FINE
    return fine


def find_book(book_id):
    for bid, title, copies in CATALOGUE:
        if bid == book_id:
            return (bid, title, copies)
    return ()


def main():
    print("=" * 70)
    print(f"          LIBRARY FINE AND AVAILABILITY REPORT  (today = day {TODAY})")
    print("=" * 70)
    print(f"{'No':<4}{'Book':<6}{'Member':<9}{'Issue':>6}{'Return':>8}"
          f"{'Late':>6}{'Fine':>6}  Status")
    print("-" * 70)

    total_fine = 0
    overdue_list = []
    invalid_list = []
    member_fines = []          # list of [member, fine]

    for rec_no, book_id, member, issue, ret in RECORDS:
        book = find_book(book_id)
        if book == () or (ret != 0 and ret < issue) or issue > TODAY:
            invalid_list.append(rec_no)
            print(f"{rec_no:<4}{book_id:<6}{member:<9}{issue:>6}{ret:>8}"
                  f"{'-':>6}{'-':>6}  INVALID RECORD")
            continue
        late = late_days(issue, ret)
        fine = fine_for(late)
        total_fine = total_fine + fine
        if ret == 0:
            ret_text = "--"
            if late > 0:
                status = "OVERDUE (not returned)"
                overdue_list.append((member, book_id, late))
            else:
                status = "with member"
        else:
            ret_text = str(ret)
            if late > 0:
                status = "returned late"
            else:
                status = "returned on time"
        print(f"{rec_no:<4}{book_id:<6}{member:<9}{issue:>6}{ret_text:>8}"
              f"{late:>6}{fine:>6}  {status}")

        # add fine to member total
        if fine > 0:
            found = False
            for item in member_fines:
                if item[0] == member:
                    item[1] = item[1] + fine
                    found = True
            if not found:
                member_fines.append([member, fine])

    print("-" * 70)
    print(f"Total fine collected / due : Rs {total_fine}")
    print("Fine by member :")
    for member, fine in member_fines:
        print(f"   {member:<8} Rs {fine}")

    print()
    print("OVERDUE BOOKS STILL NOT RETURNED")
    for member, book_id, late in overdue_list:
        print(f"   {member} has {book_id}, {late} day(s) late")

    # reconcile availability
    print()
    print("BOOK AVAILABILITY")
    print(f"{'Book':<6}{'Title':<18}{'Copies':>7}{'Out':>5}{'Available':>11}  Check")
    for bid, title, copies in CATALOGUE:
        out = 0
        for rec_no, book_id, member, issue, ret in RECORDS:
            if book_id == bid and ret == 0 and rec_no not in invalid_list:
                out = out + 1
        available = copies - out
        check = "ok"
        if available < 0:
            check = "MISMATCH - more issued than copies"
        elif available == 0:
            check = "all copies issued"
        print(f"{bid:<6}{title:<18}{copies:>7}{out:>5}{available:>11}  {check}")

    print()
    print("Invalid records :", invalid_list)


if __name__ == "__main__":
    main()
