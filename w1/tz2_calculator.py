#! /usr/bin/env python3
"""calculating the person tax"""

import sys

# define
deductions = {0.03: 0, 0.1: 105, 0.2: 555, 0.25: 1005, 0.3: 2755, 0.35: 5505, 0.45: 13505}


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


def tax_payable(income):
    """calculate payable tax"""
    if income > 3500:
        taxable_income = (income - 0 - 3500)
        taxrate = tax_rate(taxable_income)
        deduction = deductions[taxrate]
        tax = taxable_income * taxrate - deduction
        print(str(income) + '\'s tax is {:.2f}.'.format(tax))
    else:
        tax = 0
        print(str(income) + '\'s tax is {:.2f}.'.format(tax))


if __name__ == '__main__':
    # if sys.argv[1] is not None:
    if len(sys.argv[1]) > 1:
        try:
            income = int(sys.argv[1])
        except ValueError:
            print("Parameter Error")
        tax_payable(income)
    else:
        print("Parameter Error")
