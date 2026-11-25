# Case Study 25 : Progressive Water Tariff Analysis
# Name    : AKKALA LAKSHMI VENKATA SAI
# Roll No : 26000414
#
# Calculates the monthly water bill of several households using slabs,
# a fixed fee and penalties, then compares their usage.

# slabs in kilolitres (KL): (upper limit, rate per KL)
SLABS = [(10, 7), (20, 11), (30, 18), (10 ** 6, 25)]
FIXED_FEE = 60
EXCESS_LIMIT = 30          # usage above 30 KL gets a penalty
EXCESS_PENALTY = 100       # flat penalty for excess usage
LATE_RATE = 0.02           # 2% late payment penalty

# (house no, owner, KL used this month, family members, paid late?)
HOUSEHOLDS = [
    ("H-101", "Rao", 8, 3, False),
    ("H-102", "Lakshmi", 18, 4, False),
    ("H-103", "Prasad", 34, 5, True),
    ("H-104", "Swathi", 12, 2, True),
    ("H-105", "Naidu", 26, 4, False),
    ("H-106", "Farooq", 45, 6, False),
]


def water_charge(kl):
    charge = 0
    lower = 0
    for upper, rate in SLABS:
        if kl > lower:
            used_in_slab = min(kl, upper) - lower
            charge = charge + used_in_slab * rate
        lower = upper
    return charge


def calculate_bill(kl, late):
    usage = water_charge(kl)
    penalty = 0
    if kl > EXCESS_LIMIT:
        penalty = penalty + EXCESS_PENALTY
    subtotal = usage + FIXED_FEE + penalty
    late_fee = 0
    if late:
        late_fee = round(subtotal * LATE_RATE, 2)
    total = subtotal + late_fee
    return usage, penalty, late_fee, total


def main():
    print("=" * 70)
    print("                 WATER BILL STATEMENT (monthly)")
    print("=" * 70)
    print(f"{'House':<7}{'Owner':<9}{'KL':>4}{'Usage':>8}{'Fixed':>7}"
          f"{'Excess':>8}{'Late':>8}{'Total':>10}")
    print("-" * 70)

    total_kl = 0
    total_amount = 0
    for house, owner, kl, members, late in HOUSEHOLDS:
        usage, penalty, late_fee, total = calculate_bill(kl, late)
        total_kl = total_kl + kl
        total_amount = total_amount + total
        print(f"{house:<7}{owner:<9}{kl:>4}{usage:>8}{FIXED_FEE:>7}"
              f"{penalty:>8}{late_fee:>8.2f}{total:>10.2f}")
    print("-" * 70)

    average = total_kl / len(HOUSEHOLDS)
    print(f"Total water supplied : {total_kl} KL")
    print(f"Average per house    : {average:.2f} KL")
    print(f"Total amount billed  : Rs {total_amount:.2f}")

    # comparison of usage
    print()
    print("CONSUMPTION COMPARISON")
    print("-" * 70)
    print(f"{'House':<7}{'KL':>4}{'Per person':>12}{'vs avg':>9}  Remark")
    excessive = []
    for house, owner, kl, members, late in HOUSEHOLDS:
        per_person = kl / members
        diff = (kl - average) * 100 / average
        remark = "normal"
        if kl > EXCESS_LIMIT or kl > 1.5 * average:
            remark = "EXCESSIVE USAGE"
            excessive.append(house)
        elif kl < 0.5 * average:
            remark = "low usage"
        print(f"{house:<7}{kl:>4}{per_person:>12.2f}{diff:>+8.1f}%  {remark}")

    # ranking from highest to lowest consumption
    ranking = []
    for house, owner, kl, members, late in HOUSEHOLDS:
        ranking.append((kl, house, owner))
    ranking.sort(reverse=True)

    print()
    print("RANKING BY CONSUMPTION")
    rank = 1
    for kl, house, owner in ranking:
        print(f"  {rank}. {house} ({owner}) - {kl} KL")
        rank = rank + 1
    print()
    print("Houses with excessive usage :", ", ".join(excessive))


if __name__ == "__main__":
    main()
