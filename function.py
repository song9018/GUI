# coding:utf-8

import os
import xlrd
from xlutils.copy import copy
import time
from wlp import *


class func:
    def __init__(self, file_name):
        self.file_name = file_name

    def time_change(self, s_time):
        s_time = s_time.split(":")
        if s_time[2] == "0":
            s_time[2] = '00'
            date = (":").join(s_time)
            return date
        elif s_time[2] == "1":
            s_time[2] = '01'
            date = (":").join(s_time)
            return date
        elif s_time[2] == "2":
            s_time[2] = '02'
            date = (":").join(s_time)
            return date
        elif s_time[2] == "3":
            s_time[2] = '03'
            date = (":").join(s_time)
            return date
        elif s_time[2] == "4":
            s_time[2] = '04'
            date = (":").join(s_time)
            return date
        elif s_time[2] == "5":
            s_time[2] = '05'
            date = (":").join(s_time)
            return date
        elif s_time[2] == "6":
            s_time[2] = '06'
            date = (":").join(s_time)
            return date
        elif s_time[2] == "7":
            s_time[2] = '07'
            date = (":").join(s_time)
            return date
        elif s_time[2] == "8":
            s_time[2] = '08'
            date = (":").join(s_time)
            return date
        elif s_time[2] == "9":
            s_time[2] = '09'
            date = (":").join(s_time)
            return date
        else:
            date = (":").join(s_time)
            return date

    def XLD(self):
        try:
            time_list = []
            heart_list = []
            file = open(self.file_name, 'r')
            line = file.readline()
            list = line.strip().split(',')
            i = 0

            while i < 5:
                if list[i] == " BLE1" or list[i] == " Pol":
                    break
                else:
                    i += 1

            s = file.readlines()
            for line1 in s:
                list1 = line1.strip().split(',')
                time = list1[0]
                time_list.append(time)
                if i != 5:
                    Pol = list1[i]
                    if Pol != " Pol" or Pol != " BLE1":
                        Pol = int(Pol)
                        heart_list.append(Pol)
                else:
                    Pol = None

            # self.wlp.heart_wlp()
            # for i in range(len(time_list)):
            #     self.wlp.add_activity("XH3", str(time_list[i]), str(heart_list[i]))
            #     self.wlp.close_file()
            return time_list, heart_list
        except Exception as e:
            pass

    def XH3(self):
        try:
            time_list = []
            heart_list = []
            k = 0
            file = open(self.file_name, 'r')
            line1 = file.readlines()
            for line in line1:
                l = 1
                k += 1
                if 'HR:***' in line:
                    heart = line.strip().split('HR:***')[1].split('***')
                    date = line.strip().split('HR:***')[0].split('***')
                    date11 = date[0].split()
                    heart = int(heart[0])
                    time_list.append(date11)
                    heart_list.append(heart)
            return time_list, heart_list
        except Exception as e:
            print(e)

    def NOW2(self):
        try:
            time_list = []
            heart_list = []
            file = open(self.file_name, 'r')
            line1 = file.readlines()
            for line in line1:
                l = 1
                list = line.strip().split(' ')
                date = line.strip().split('[')[1].split(']')[0].split()
                heart = list[0]
                heart = int(heart)
                heart_list.append(heart)
                date_time1 = date[1]  # 转换
                date_time = self.time_change(date_time1)
                time_list.append(date_time)
            return time_list, heart_list
        except Exception as e:
            pass

    def PPG_8011(self):
        try:
            time_list = []
            heart_list = []
            file = open(self.file_name, 'r')
            line = file.readline()
            list = line.strip().split(',')
            h = 0
            while h < 5:
                if list[h] == " P11":
                    break
                else:
                    h += 1
            s = file.readlines()
            for line1 in s:
                l = 1
                list1 = line1.strip().split(',')
                if h != 5:
                    P11 = list1[h]
                    if P11 != " P11":
                        P11 = int(P11)
                        heart_list.append(P11)
                else:
                    P11 = None
                date = list1[0].split()
                time_list.append(date)
            return time_list, heart_list
        except Exception as e:
            print(e)

    def MTK2511(self):
        try:
            time_list = []
            heart_list = []
            file = open(self.file_name, 'r')
            lines = file.readlines()
            for line in lines:
                l = 1
                if "22,0," in line:
                    list = line.strip().split(',')
                    if list[0] == "22" and list[1] == "0":
                        heart = list[2]
                        heart_list.append(heart)
                        time1 = list[-1]
                        format = '%Y-%m-%d %H:%M:%S'

                        # value为传入的值为时间戳(整形)，如：1332888820
                        value = time.localtime(int(time1))
                        dtime = time.strftime(format, value)
                        time_list.append(dtime)
            return time_list, heart_list
        except Exception as e:
            print(e)

    def COROS(self):
        try:
            time_list = []
            heart_list = []
            file = open(self.file_name, 'r')
            lines = file.readlines()
            for line in lines:
                l = 1
                list = line.split()
                date = list[0]
                time = date.split('[')[1].split(']')[0]
                heart = abs(int(list[2]))
                heart_list.append(heart)
                time_list.append(time)
            return time_list, heart_list
        except Exception as e:
            print(e)


if __name__ == "__main__":
    ppg = func("PPG1.txt")
    ppg.XLD()
