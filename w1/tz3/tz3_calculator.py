#! /usr/bin/env python3
"""calculating the person tax"""

import sys

# define deduction
deductions = {0.03: 0, 0.1: 105, 0.2: 555, 0.25: 1005, 0.3: 2755, 0.35: 5505, 0.45: 13505}

class Config:
    """read and get the tax rate from config file"""

    def __init__(self, configfile):
        self.__config = {}
        file = open(configfile, 'r')
        filelist = file.readlines()
        for i in filelist:
            key = i.split('=')[0].strip()
            value = i.split('=')[1].strip()
            self.__config[key] = value

    def get_config(self, name):
        print(self.__config[name])
        return self.__config[name]


config = Config('test.cfg')
config.get_config('GongJiJin')


def insurance(income):
    """Definition insurance"""
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
    annuity = insurance(income)
    if income > 3500:
        taxable_income = (income - annuity - 3500)
        taxrate = tax_rate(taxable_income)
        deduction = deductions[taxrate]
        tax = taxable_income * taxrate - deduction
        after = income - tax - annuity
        # print(str(income) + '\'s after tax is {:.2f}.'.format(after))
    else:
        after = income - annuity
        # print(str(income) + '\'s after tax is {:.2f}.'.format(after))
    return after


if __name__ == '__main__':
    # if sys.argv[1] is not None:
    if len(sys.argv[1]) > 1:
        info = sys.argv[1:]
        income = []
        p_no = []
        for i in info:
            try:
                before_tax = int(i.split(":")[1])
                income.append(int(before_tax))
                p_no.append(i.split(":")[0])
            except ValueError:
                print("Parameter Error")
        p_after_tax = []
        p_after_tax.extend([after_tax(x) for x in income])
        try:
            for i, j in zip(p_no, p_after_tax):
                print("{}:{:.2f}".format(i, j))
        except ValueError:
            print("Parameter Error")
