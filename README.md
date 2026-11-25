# Python Activity-Based Learning

**Subject:** Python Programming  
**Activity:** Select any 10 case studies and develop complete Python solutions  
**Name:** AKKALA LAKSHMI VENKATA SAI  
**Roll No:** 26000414

---

## Case studies selected

| # | Case study (number in the list) | Folder |
|---|---------------------------------|--------|
| 1 | Employee Payroll and Deduction Analysis (4) | [01-employee-payroll-deduction](01-employee-payroll-deduction/) |
| 2 | Attendance Recovery Computation (12) | [02-attendance-recovery-computation](02-attendance-recovery-computation/) |
| 3 | ATM Transaction Sequence Simulation (13) | [03-atm-transaction-sequence](03-atm-transaction-sequence/) |
| 4 | Progressive Water Tariff Analysis (25) | [04-progressive-water-tariff](04-progressive-water-tariff/) |
| 5 | Advanced Numeric Pattern Generator (27) | [05-numeric-pattern-generator](05-numeric-pattern-generator/) |
| 6 | String-Based Examination Answer Evaluation (31) | [06-exam-answer-evaluation](06-exam-answer-evaluation/) |
| 7 | Text Compression Using Character Runs (35) | [07-text-compression-rle](07-text-compression-rle/) |
| 8 | Multi-Stage Examination Eligibility System (39) | [08-exam-eligibility-system](08-exam-eligibility-system/) |
| 9 | Student Marks Matrix Analysis (42) | [09-student-marks-matrix](09-student-marks-matrix/) |
| 10 | Library Borrowing and Fine Reconciliation (58) | [10-library-fine-reconciliation](10-library-fine-reconciliation/) |

## What is in each folder

- `README.md` - problem statement, objectives, assumptions, algorithm, flowchart, pseudocode, source code, test cases, output screenshot and conclusion
- `flowchart.png` - flowchart of the program
- `solution.py` - the Python program
- `test_cases.py` - test cases to check the program
- `output.txt` - output of the program
- `output_screenshot.png` - screenshot of the output

All 10 case studies are also put together in one PDF: [Python-Activity-Based-Learning-Complete.pdf](Python-Activity-Based-Learning-Complete.pdf)

## Topics used

| Topic | Case studies |
|-------|--------------|
| Variables, data types, operators | all |
| Conditional statements | all (mainly 1, 3, 4, 8) |
| Loops | all (simulation loop in 2, nested loops in 5, 9) |
| Strings | 5 (input validation), 6 (answer strings), 7 (encoding) |
| Pattern generation | 5 (diamond and pyramid), 6 (answer pattern) |
| Lists | 3, 4, 6, 8, 10 |
| Nested lists | 9 (marks matrix) |
| Tuples, tuple operations, unpacking | 1, 2, 4, 10 (catalogue and records) |
| Algorithm, flowchart, pseudocode | README of every folder |

## How to run

```bash
# run a program
python3 01-employee-payroll-deduction/solution.py

# run its test cases
cd 01-employee-payroll-deduction
python3 test_cases.py

# pattern generator with your own size
python3 05-numeric-pattern-generator/solution.py ask
```

## Test results

| Case study | Tests | Result |
|------------|-------|--------|
| 4. Employee Payroll and Deduction Analysis | 13 | all passed |
| 12. Attendance Recovery Computation | 10 | all passed |
| 13. ATM Transaction Sequence Simulation | 15 | all passed |
| 25. Progressive Water Tariff Analysis | 11 | all passed |
| 27. Advanced Numeric Pattern Generator | 13 | all passed |
| 31. String-Based Examination Answer Evaluation | 10 | all passed |
| 35. Text Compression Using Character Runs | 14 | all passed |
| 39. Multi-Stage Examination Eligibility System | 11 | all passed |
| 42. Student Marks Matrix Analysis | 14 | all passed |
| 58. Library Borrowing and Fine Reconciliation | 12 | all passed |
| **Total** | **123** | |

## Notes

- Only Python 3 is needed, no extra packages are used.
- All the data in the programs (names, marks, amounts) is sample data.
- The sample data includes some wrong / boundary inputs on purpose so that the validation part of each program can be seen in the output.
