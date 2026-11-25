# Case Study 13 : ATM Transaction Sequence Simulation
# Name    : AKKALA LAKSHMI VENKATA SAI
# Roll No : 26000414
#
# Processes a list of deposits and withdrawals on one account, checks every
# transaction against the limits and prints a summary at the end.

OPENING_BALANCE = 10000
MIN_BALANCE = 500             # balance should not go below this
MAX_WITHDRAW_ONCE = 20000     # per transaction withdrawal limit
DAILY_WITHDRAW_LIMIT = 40000  # total withdrawal limit for the day
MAX_DEPOSIT_ONCE = 50000      # per transaction deposit limit

# (type, amount)   D = deposit, W = withdrawal
TRANSACTIONS = [
    ("D", 5000),
    ("W", 3000),
    ("W", 2550),
    ("W", 25000),
    ("D", 60000),
    ("D", 30000),
    ("W", 20000),
    ("X", 1000),
    ("W", -500),
    ("W", 15000),
    ("W", 6000),
    ("D", 2000),
]


def check_transaction(t_type, amount, balance, withdrawn_today):
    # returns (True, "") if valid, otherwise (False, reason)
    if t_type != "D" and t_type != "W":
        return False, "invalid transaction type"
    if amount <= 0:
        return False, "amount must be positive"
    if t_type == "D":
        if amount > MAX_DEPOSIT_ONCE:
            return False, "deposit limit is 50000"
        return True, ""
    # withdrawal checks
    if amount % 100 != 0:
        return False, "amount must be a multiple of 100"
    if amount > MAX_WITHDRAW_ONCE:
        return False, "per transaction limit is 20000"
    if withdrawn_today + amount > DAILY_WITHDRAW_LIMIT:
        return False, "daily limit of 40000 crossed"
    if balance - amount < MIN_BALANCE:
        return False, "insufficient balance (min 500)"
    return True, ""


def run(transactions):
    balance = OPENING_BALANCE
    withdrawn = 0
    deposited = 0
    log = []          # list of (no, type, amount, status, balance/reason)
    rejected = 0
    no = 1
    for t_type, amount in transactions:
        ok, reason = check_transaction(t_type, amount, balance, withdrawn)
        if ok:
            if t_type == "D":
                balance = balance + amount
                deposited = deposited + amount
            else:
                balance = balance - amount
                withdrawn = withdrawn + amount
            log.append((no, t_type, amount, "OK", "Bal " + str(balance)))
        else:
            rejected = rejected + 1
            log.append((no, t_type, amount, "REJECTED", reason))
        no = no + 1
    return balance, deposited, withdrawn, rejected, log


def main():
    balance, dep, wd, rejected, log = run(TRANSACTIONS)
    print("=" * 62)
    print("              ATM TRANSACTION SIMULATION")
    print("=" * 62)
    print(f"Opening balance : Rs {OPENING_BALANCE}")
    print("-" * 62)
    print(f"{'No':<4}{'Type':<6}{'Amount':>8}  {'Status':<10}Details")
    print("-" * 62)
    for no, t_type, amount, status, info in log:
        if t_type == "D":
            name = "DEP"
        elif t_type == "W":
            name = "WDL"
        else:
            name = t_type
        print(f"{no:<4}{name:<6}{amount:>8}  {status:<10}{info}")
    print("-" * 62)
    print("TRANSACTION SUMMARY")
    print(f"Total transactions   : {len(TRANSACTIONS)}")
    print(f"Successful           : {len(TRANSACTIONS) - rejected}")
    print(f"Rejected             : {rejected}")
    print(f"Total deposited      : Rs {dep}")
    print(f"Total withdrawn      : Rs {wd}")
    print(f"Daily limit left     : Rs {DAILY_WITHDRAW_LIMIT - wd}")
    print(f"Closing balance      : Rs {balance}")


if __name__ == "__main__":
    main()
