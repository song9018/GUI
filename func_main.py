# coding:utf-8
import os
import xlrd
from xlutils.copy import copy
import time


class PPG:
    def __init__(self):
        pass

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

    def PPG1(self,file_name):
        try:
            file = open(file_name, 'r')
            line = file.readline()
            list = line.strip().split(',')
            i = 0
            j = 0
            k = 1
            f = 0
            while f < 5:
                if list[f] == " P11":
                    break
                else:
                    f += 1
            while i < 5:
                if list[i] == " BLE1" or list[i] == " Pol" :
                    break
                else:
                    i += 1
            while j < 5:
                if list[j] == "Time":
                    break
                else:
                    j += 1
            s = file.readlines()
            excel = xlrd.open_workbook(os.path.join(os.getcwd(), 'build\\data.xls'), 'w')
            wb = copy(excel)
            ws = wb.get_sheet(0)
            ws1= wb.get_sheet(1)
            for line1 in s:
                list1 = line1.strip().split(',')
                if i != 5:
                    Pol = list1[i]
                    if Pol != " Pol" or Pol != " BLE1":
                        Pol = int(Pol)
                else:
                    Pol = None

                if j != 5:
                    TIME = list1[j]
                else:
                    TIME = None

                if f != 5:
                    P11 = list1[f]
                    if P11 != " P11":
                        P11 = int(P11)
                else:
                    P11 = None

                if k < len(s):
                    ws.write(k, 0, TIME)
                    ws.write(k, 1, Pol)
                    ws.write(k, 4, P11)
                    ws1.write(k, 0, TIME)
                    k += 1
            wb.save(os.path.join(os.getcwd(), 'build\\data.xls'))
        except Exception as e:
            pass
        finally:
            wb.save(os.path.join(os.getcwd(), 'build\\data.xls'))

    def PPG2(self,file_name):
        try:
            k = 0
            file = open(file_name, 'r')
            excel = xlrd.open_workbook(os.path.join(os.getcwd(), 'build\\data.xls'), 'r')
            rs = excel.sheet_by_index(0)
            rs1 = excel.sheet_by_index(1)
            wb = copy(excel)
            ws = wb.get_sheet(0)
            ws1 = wb.get_sheet(1)
            line1 = file.readlines()
            for line in line1:
                l = 1
                k+=1

                if 'HR:***' in line:
                    heart = line.strip().split('HR:***')[1].split('***')
                    date = line.strip().split('HR:***')[0].split('***')
                    date11 = date[0].split()
                    heart = heart[0]
                    heart = int(heart)
                    rate = int(line1[k-2].strip().split(",")[3])

                    while l < rs.nrows:
                        date1 = rs.cell_value(l, 0).split()
                        if date11[1] == date1[1]:
                            ws.write(l, 2, heart)
                            ws1.write(l, 1, rate)
                            break
                        l += 1

            wb.save(os.path.join(os.getcwd(), 'build\\data.xls'))
        except Exception as e:
            print(e)
        finally:
            wb.save(os.path.join(os.getcwd(), 'build\\data.xls'))

    def PPG3(self,file_name):
        try:
            file = open(file_name, 'r')
            excel = xlrd.open_workbook(os.path.join(os.getcwd(), 'build\\data.xls'), 'r')
            rs = excel.sheet_by_index(0)
            wb = copy(excel)
            ws = wb.get_sheet(0)
            line1 = file.readlines()
            for line in line1:
                l = 1
                list = line.strip().split(' ')
                date = line.strip().split('[')[1].split(']')[0].split()
                heart = list[0]
                heart = int(heart)
                date_time1 = date[1]  # 转换
                date_time = self.time_change(date_time1)
                while l < rs.nrows:
                    date1 = rs.cell_value(l, 0).split()
                    if date_time == date1[1]:
                        ws.write(l, 3, heart)
                        break
                    l += 1
            wb.save(os.path.join(os.getcwd(), 'build\\data.xls'))
        except Exception as e:
            pass
        finally:
            wb.save(os.path.join(os.getcwd(), 'build\\data.xls'))

    def PPG_4_5(self,file_name, name_col):
        try:
            file = open(file_name, 'r')
            line = file.readline()
            list = line.strip().split(',')
            h = 0
            while h < 5:
                if list[h] == " P11":
                    break
                else:
                    h += 1
            s = file.readlines()
            excel = xlrd.open_workbook(os.path.join(os.getcwd(), 'build\\data.xls'), 'r')
            rs = excel.sheet_by_index(0)
            wb = copy(excel)
            ws = wb.get_sheet(0)
            for line1 in s:
                l = 1
                list1 = line1.strip().split(',')
                if h != 5:
                    P11 = list1[h]
                    if P11 != " P11":
                        P11 = int(P11)
                else:
                    P11 = None
                sss = list1[0].split()

                if list1[0] != "Time":
                    while l < rs.nrows:
                        date1 = rs.cell_value(l, 0).split()

                        if sss[1] == date1[1]:
                            ws.write(l, name_col, P11)
                            break
                        l += 1
            wb.save(os.path.join(os.getcwd(), 'build\\data.xls'))
        except Exception as e:
            print(e)
        finally:
            wb.save(os.path.join(os.getcwd(), 'build\\data.xls'))

    def MTK2511(self,file_name):
        try:
            file = open(file_name, 'r')
            lines = file.readlines()
            excel = xlrd.open_workbook(os.path.join(os.getcwd(), 'build\\data.xls'), 'r')
            rs = excel.sheet_by_index(0)
            wb = copy(excel)
            ws = wb.get_sheet(0)
            for line in lines:
                l = 1
                if "22,0," in line:
                    list = line.strip().split(',')
                    if list[0] == "22" and list[1] == "0":
                        heart = list[2]
                        time1 = list[-1]
                        format = '%Y-%m-%d %H:%M:%S'

                        # value为传入的值为时间戳(整形)，如：1332888820
                        value = time.localtime(int(time1))
                        dtime = time.strftime(format, value)
                        while l < rs.nrows:
                            date1 = rs.cell_value(l, 0).split()

                            if dtime.split()[1] == date1[1]:
                                ws.write(l, 7, int(heart))

                                break
                            l += 1
            wb.save(os.path.join(os.getcwd(), 'build\\data.xls'))
        except Exception as e:
            print(e)
        finally:
            wb.save(os.path.join(os.getcwd(), 'build\\data.xls'))

    def COROS(self, file_name):
        try:
            file = open(file_name, 'r')
            lines = file.readlines()
            excel = xlrd.open_workbook(os.path.join(os.getcwd(), 'build\\data.xls'), 'r')
            rs = excel.sheet_by_index(0)
            wb = copy(excel)
            ws = wb.get_sheet(0)
            for line in lines:
                l=1
                list = line.split()
                date = list[0]
                time = date.split('[')[1].split(']')[0]
                heart = abs(int(list[2]))

                while l < rs.nrows:
                    date1 = rs.cell_value(l, 0).split()
                    if time == date1[1]:
                        ws.write(l, 8, heart)
                        break
                    l += 1
            wb.save(os.path.join(os.getcwd(), 'build\\data.xls'))
        except Exception as e:
            print(e)
        finally:
            wb.save(os.path.join(os.getcwd(), 'build\\data.xls'))


def copy_file():
    path = os.path.join(os.getcwd(), 'build\\data.xls')
    path1 = os.path.join(os.getcwd(), "build\\UI_main\\data.xls")
    if os.path.isfile('data.xls'):
        os.system('del data.xls')
        if os.path.isfile('data_chart.xls'):
            os.system('del data_chart.xls')
        os.system("copy %s %s" % (path1, path))
    else:
        os.system("copy %s %s" % (path1, path))

def read_excel(i):
    l = 1
    heart0=[]

    excel = xlrd.open_workbook(os.path.join(os.getcwd(), 'build\\data.xls'), 'r')
    rs = excel.sheet_by_index(0)
    wb = copy(excel)
    ws = wb.get_sheet(0)
    while l < rs.nrows:
        heart = rs.cell_value(l, i)
        if heart!="":
            heart0.append(int(heart))
        else:
            heart0.append(None)
        l+=1
    return heart0

if __name__ =="__main__":
    p =PPG()
    p.PPG1("PPG1.txt")
    p.PPG2("PPG2.txt")
