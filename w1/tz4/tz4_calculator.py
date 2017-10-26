#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/22 11:33
# @Author  : Hython.com
# @File    : p3test.py
import csv
import sys
from multiprocessing import Process, Queue, Pool

queue = Queue()

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
        self.userdatafile = userdatafile

    def read_user_info(self, userdatafile):
        """read user data from csv file"""
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
            out.append('{:.2f}'.format(i))
        return out

    def full(self):
        datas = []
        pool = Pool(processes=3)
        for p in userdata.userdatas:
            for j in pool.apply(self.calculator, ((p[1]),)): # use pool for processes
                p.append(j)
            datas.append(p)
        return datas

    def dumptofile(self, outputfile):
        #contents = self.full()
        contents = Process(target=self.full)
        contents.start()
        contents.join()
        queue.put(contents)
        out_file = open(outputfile, 'w', newline='')
        outwriter = csv.writer(out_file)
        for row in queue.get(contents): #get process data by queue.get
            outwriter.writerow(row)
        out_file.close()


def main():
    if len(sys.argv[1]) > 1:
        args = sys.argv[1:]
        try:
            if '-c' in args:
                index = args.index('-c')
                configfile = args[index+1]
                config = Config(configfile)
            if '-d' in args:
                index = args.index('-d')
                userfile = args[index+1]
                userdata = UserData(userfile)
                p = Process(target=userdata.read_user_info, args=(userfile, ))
                p.start()
                p.join()
                queue.put(p)
                #userdata.read_user_info(userfile)
            if '-o' in args:
                index = args.index('-o')
                outfile = args[index+1]
                #userdata.dumptofile(outfile)
                q = Process(target=userdata.dumptofile, args=(outfile, ))
                q.start()
                q.join()
        except ValueError:
            print("Parameter Error")
    else:
        print("Parameter Error")


if __name__ == '__main__':
    main()
