# Case Study 4 : Employee Payroll and Deduction Analysis
# Name    : AKKALA LAKSHMI VENKATA SAI
# Roll No : 26000414
#
# Gross salary = basic + HRA + DA + TA + overtime + incentive
# Deductions   = PF + professional tax + income tax (progressive)
# Net salary   = gross - deductions

# allowance rules
HRA_RATE = 0.20          # 20% of basic
DA_RATE = 0.10           # 10% of basic
TA_FIXED = 1500          # travel allowance (same for all)
OT_RATE = 150            # rupees per overtime hour
MAX_OT_HOURS = 20        # only 20 hours of overtime are paid in a month

# deduction rules
PF_RATE = 0.12           # 12% of basic
PF_LIMIT = 1800          # PF cannot be more than 1800

# income tax slabs on monthly gross (upper limit, rate)
TAX_SLABS = [(25000, 0.00), (50000, 0.05), (10 ** 9, 0.10)]

# (emp id, name, basic pay, overtime hours, incentive)
EMPLOYEES = [
    ("E101", "Ravi Kumar", 18000, 6, 1000),
    ("E102", "Sneha Reddy", 32000, 0, 2500),
    ("E103", "Kiran Babu", 45000, 12, 5000),
    ("E104", "Divya Sri", 14000, 25, 0),
    ("E105", "Mahesh Varma", 60000, 4, 8000),
]


def overtime_pay(hours):
    if hours < 0:
        hours = 0
    if hours > MAX_OT_HOURS:
        hours = MAX_OT_HOURS
    return hours * OT_RATE


def gross_salary(basic, ot_hours, incentive):
    hra = basic * HRA_RATE
    da = basic * DA_RATE
    ot = overtime_pay(ot_hours)
    gross = basic + hra + da + TA_FIXED + ot + incentive
    return hra, da, ot, gross


def provident_fund(basic):
    pf = basic * PF_RATE
    if pf > PF_LIMIT:
        pf = PF_LIMIT
    return pf


def professional_tax(gross):
    if gross <= 15000:
        return 0
    elif gross <= 20000:
        return 150
    else:
        return 200


def income_tax(gross):
    # progressive: each slab rate applies only to the part inside that slab
    tax = 0
    lower = 0
    for upper, rate in TAX_SLABS:
        if gross > lower:
            amount_in_slab = min(gross, upper) - lower
            tax = tax + amount_in_slab * rate
        lower = upper
    return tax


def net_salary(basic, ot_hours, incentive):
    hra, da, ot, gross = gross_salary(basic, ot_hours, incentive)
    pf = provident_fund(basic)
    pt = professional_tax(gross)
    it = income_tax(gross)
    total_ded = pf + pt + it
    return gross, total_ded, gross - total_ded


def print_statement(emp):
    emp_id, name, basic, ot_hours, incentive = emp
    hra, da, ot, gross = gross_salary(basic, ot_hours, incentive)
    pf = provident_fund(basic)
    pt = professional_tax(gross)
    it = income_tax(gross)
    total_ded = pf + pt + it
    net = gross - total_ded

    print("-" * 50)
    print(f"Employee : {name} ({emp_id})")
    print("-" * 50)
    print(f"{'EARNINGS':<25}{'Amount (Rs)':>15}")
    print(f"{'Basic Pay':<25}{basic:>15.2f}")
    print(f"{'HRA (20%)':<25}{hra:>15.2f}")
    print(f"{'DA (10%)':<25}{da:>15.2f}")
    print(f"{'TA':<25}{TA_FIXED:>15.2f}")
    paid_hours = ot_hours if ot_hours <= MAX_OT_HOURS else MAX_OT_HOURS
    print(f"{'Overtime (' + str(paid_hours) + ' hrs)':<25}{ot:>15.2f}")
    print(f"{'Incentive':<25}{incentive:>15.2f}")
    print(f"{'GROSS SALARY':<25}{gross:>15.2f}")
    print(f"{'DEDUCTIONS':<25}")
    print(f"{'Provident Fund':<25}{pf:>15.2f}")
    print(f"{'Professional Tax':<25}{pt:>15.2f}")
    print(f"{'Income Tax':<25}{it:>15.2f}")
    print(f"{'TOTAL DEDUCTIONS':<25}{total_ded:>15.2f}")
    print(f"{'NET SALARY':<25}{net:>15.2f}")
    if ot_hours > MAX_OT_HOURS:
        print(f"Note: {ot_hours} OT hours worked, only {MAX_OT_HOURS} are paid")
    return gross, total_ded, net


def main():
    print("=" * 50)
    print("        MONTHLY SALARY STATEMENT")
    print("=" * 50)

    total_gross = 0
    total_net = 0
    highest_name = ""
    highest_net = -1

    for emp in EMPLOYEES:
        gross, ded, net = print_statement(emp)
        total_gross = total_gross + gross
        total_net = total_net + net
        if net > highest_net:
            highest_net = net
            highest_name = emp[1]

    print("=" * 50)
    print("PAYROLL SUMMARY")
    print("=" * 50)
    print(f"{'ID':<6}{'Name':<15}{'Gross':>10}{'Deduct':>9}{'Net':>10}")
    for emp_id, name, basic, ot_hours, incentive in EMPLOYEES:
        gross, ded, net = net_salary(basic, ot_hours, incentive)
        print(f"{emp_id:<6}{name:<15}{gross:>10.2f}{ded:>9.2f}{net:>10.2f}")
    print("-" * 50)
    print(f"Number of employees : {len(EMPLOYEES)}")
    print(f"Total gross payout  : Rs {total_gross:.2f}")
    print(f"Total net payout    : Rs {total_net:.2f}")
    print(f"Highest net salary  : {highest_name} (Rs {highest_net:.2f})")


if __name__ == "__main__":
    main()
