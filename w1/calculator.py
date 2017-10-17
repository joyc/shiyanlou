#! /usr/bin/env python3
"""calculate the person tax"""

import sys


deductions = {0.03: 0, 0.1: 105, 0.2: 555, 0.25: 1005, 0.3: 2755, 0.35: 5505, 0.45: 13505}

# if sys.argv[1] is not None:
if len(sys.argv[1]) > 1:
    try:
        income = int(sys.argv[1])
    except ValueError:
        print("Parameter Error")

def tax_rate(income):
    "get tax rate with income"
    if income <= 1500:
        tax_rate = 0.03
    elif income <= 4500:
        tax_rate = 0.1
    elif income <= 9000:
        tax_rate = 0.2
    elif income <= 35000:
        tax_rate = 0.25
    elif income <= 55000:
        tax_rate = 0.3
    elif income <= 80000:
        tax_rate = 0.35
    else:
        tax_rate = 0.45
    return

# def tax_payable(income):
#     "calculate payable tax"
    tax_rate(income)
    deduction = deductions[tax_rate]
    taxable_income = (income - 0 - 3500)
    tax = taxable_income * tax_rate - deduction
    print(income + '\'s tax is {:.2f}.'.format(tax))
