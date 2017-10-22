#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/22 11:33
# @Author  : Hython.com
# @File    : p3test.py
import csv
import sys
# con_file = 'test.cfg'
# with open(con_file, 'w+') as f:
#     f.write('JiShuL = 2193.00\n')
#     f.write('JiShuH = 16446.00\n')
#     f.write('YangLao = 0.08\n')
#     f.write('YiLiao = 0.02\n')
#     f.write('ShiYe = 0.005\n')
#     f.write('GongShang = 0\n')
#     f.write('ShengYu = 0\n')
#     f.write('GongJiJin = 0.06')


# csvfile = 'userinfo.csv'
# output_file = open(csvfile, 'w', newline='')
# output_writer = csv.writer(output_file)
# output_writer.writerow([101, 3500])
# output_writer.writerow([203, 5000])
# output_writer.writerow([309, 15000])
# output_file.close()


# define deduction
deductions = {0.03: 0, 0.1: 105, 0.2: 555, 0.25: 1005, 0.3: 2755, 0.35: 5505, 0.45: 13505}


class Config:
    """read and get the tax rate from config file"""

    def __init__(self, configfile):
        self.__config = {}
        file = open(configfile, 'r')
        file_list = file.readlines()
        for i in file_list:
            key = i.split('=')[0].strip()
            value = i.split('=')[1].strip()
            self.__config[key] = value
        file.close()

    def get_config(self, *names):
        for name in names:
            print(self.__config[name])
        return float(self.__config[names])

    @property
    def rate(self):
        rate = sum([float(self.__config['YangLao']),
                    float(self.__config['YiLiao']),
                    float(self.__config['ShiYe']),
                    float(self.__config['GongShang']),
                    float(self.__config['ShengYu']),
                    float(self.__config['GongJiJin'])])
        return float(rate)

    def basic(self, income):
        p_rate = self.rate
        low = float(self.__config['JiShuL'])
        high = float(self.__config['JiShuH'])
        if float(income) < low:
            annuity = low * p_rate
        elif float(income) > high:
            annuity = high * p_rate
        else:
            annuity = float(income) * p_rate
        return float(annuity)


class UserData:
    """read userdate and output new userdata file """
    def __init__(self, userdatafile):
        self.userdatas = []
        datafile = open(userdatafile)
        reader = csv.reader(datafile)
        for row in reader:
            self.userdatas.append(row)
        # print(self.userdatas)

    @staticmethod
    def insurance(self, income):
        """Definition insurance"""
        return float(income * config.rate)

    def tax_rate(self, income):
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

    def calculator(self, income):
        """calculate payable tax and after tax income"""
        annuity = float(config.basic(income))  # 社保总额
        out = []
        if float(income) > 3500.00:
            taxable_income = (float(income) - float(annuity) - 3500.00)  # 课税对象金额
            taxrate = self.tax_rate(taxable_income)  # 税率
            deduction = deductions[taxrate]  # 速算扣除数
            tax = taxable_income * taxrate - deduction  # 个税金额
            after = float(income) - float(tax) - float(annuity)  # 税后工资
            # print("社保总额:{}， 个税金额：{}， 税后工资：{}".format(annuity, tax, after))
        else:
            tax = 0.00  # 个税金额
            after = float(income) - annuity
        for i in [annuity, tax, after]:
            out.append(i)
        return out

    def full(self):
        datas = []
        for p in userdata.userdatas:
            for j in self.calculator(p[1]):
                p.append(j)
            datas.append(p)
        print(datas)
        return datas

    def dumptofile(self, outputfile):
        contents = self.full()
        out_file = open(outputfile, 'w', newline='')
        outwriter = csv.writer(out_file)
        outwriter.writerow(contents)
        out_file.close()


# if __name__ == '__main__':
#     if len(sys.argv[1]) > 1:
#         args = sys.argv[1:]
#         if '-c' in args:
#             index = args.index('-c')
#             configfile = args[index+1]
#             config = Config(configfile)
#         if '-d' in args:
#             index = args.index('-d')
#             userfile = args[index+1]
#             userdata = UserData(userfile)
#         if '-o' in args:
#             index = args.index('-o')
#             outfile = args[index+1]
#             userdata.dumptofile(outfile)
#
#         income = []
#         p_no = []
#         for i in args:
#             try:
#                 before_tax = int(i.split(":")[1])
#                 income.append(int(before_tax))
#                 p_no.append(i.split(":")[0])
#             except ValueError:
#                 print("Parameter Error")
#         p_after_tax = []
#         p_after_tax.extend([after_tax(x) for x in income])
#         try:
#             for i, j in zip(p_no, p_after_tax):
#                 print("{}:{:.2f}".format(i, j))
#         except ValueError:
#             print("Parameter Error")

config = Config('test.cfg')
userdata = UserData('userinfo.csv')
print(userdata.userdatas)
r = userdata.calculator(5000)
#print(r)
#userdata.dumptofile('calculated.csv')
userdata.full()
