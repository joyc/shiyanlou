#! /usr/bin/env python3
"""calculating the person tax"""

import sys

# define
deductions = {0.03: 0, 0.1: 105, 0.2: 555, 0.25: 1005, 0.3: 2755, 0.35: 5505, 0.45: 13505}


def baoxian(income):
    """bao xian"""
    return income * (0.08 + 0.02 + 0.005 + 0.06)


def tax_rate(income):
    """get tax rate with incom"""
    if income <= 1500:
        rate = 0.03
    elif income <= 4500:
        rate = 0.1
    elif income <= 9000:
        rate = 0.2
    elif income <= 35000:
        rate = 0.25
    elif income <= 55000:
        rate = 0.3
    elif income <= 80000:
        rate = 0.35
    else:
        rate = 0.45
    return rate


def after_tax(income):
    """calculate payable tax"""
    bx = baoxian(income)
    if income > 3500:
        taxable_income = (income - bx - 3500)
        taxrate = tax_rate(taxable_income)
        deduction = deductions[taxrate]
        tax = taxable_income * taxrate - deduction
        after = income - tax - bx
        print(str(income) + '\'s after tax is {:.2f}.'.format(after))
    else:
        after = income - bx
        print(str(income) + '\'s after tax is {:.2f}.'.format(after))


if __name__ == '__main__':
    # if sys.argv[1] is not None:
    if len(sys.argv[1]) > 1:
        try:
            income = int(sys.argv[1])
        except ValueError:
            print("Parameter Error")
        after_tax(income)
    else:
        print("Parameter Error")
