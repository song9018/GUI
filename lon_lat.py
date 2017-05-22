#! /usr/bin/env python
# -*- coding=utf-8 -*-
import math
import random
import os


def DistanceToLogLat(distance, number, logLatPtStr):
    """
    将相对于起点的距离转换为经纬度,distance代表到点的距离，angle代表方位角度
    """
    lat_lng = logLatPtStr.split(",")
    lng1 = float(lat_lng[0])  # 经度
    lat1 = float(lat_lng[1])  # 纬度
    LngLat = []
    for i in range(number):
        angle = random.randint(-180, 180)  # 方位角随机设置
        lon = lng1 + (float(distance) * math.sin(angle * math.pi / 180)) / (
            111.31955 * math.cos(lat1 * math.pi / 180))  # 将距离转换成经度
        lat = lat1 + (float(distance) * math.cos(angle * math.pi / 180)) / 111.31955  # 将距离转换成纬度
        lon1 = round(lon, 6)  # 保留六位小数点
        lat1 = round(lat, 6)
        lnglat = str(lon1) + "," + str(lat1)
        LngLat.append(lnglat)
    return LngLat


def jiazao(distance, number, file_name):
    """
    原始GPS数据，提取经纬度信息
    """
    try:
        file = open(file_name, 'r')
        list = file.readlines()

        list1 = []
        list2=[]

        j = 0
        for line in list:
            data = line.split()
            if data[1] != '0.000000' and data[2] != '0.000000':
                data_str = data[1] + "," + data[2]
                list1.append(data_str)  # 获取定位成功后经纬度信息
            else:
                j += 1  # 统计定位定位成功后持续时间，1s为单位

        i = random.randint(j, len(list1))  # 随机获取定位成功后的某一点的经纬度
        dd = list[i].split()
        log_Lat = dd[1] + "," + dd[2]
        LonLnt = DistanceToLogLat(distance, number, log_Lat)  # 以某一点为圆心，获取特定距离的若干个经纬度信息
        for k in range(number):
            lon = LonLnt[k].split(",")[0]
            lat = LonLnt[k].split(",")[1]
            dd[0] = str(int(dd[0]) + 1)
            dd[1] = lon
            dd[2] = lat
            lat_lng = (" ").join(dd)
            list.insert(i + k + 1, lat_lng + "\n")  # 将获取到的噪声插入到原始经纬度数据
            count = i + k + 1

        for i in range(len(list) - count - 1):
            """
            加噪后对中心点以后的经纬度的时间戳做处理
            """
            change_list = list[count + i + 1].split()
            change_list[0] = str(int(change_list[0]) + 10)
            list0 = (" ").join(change_list)
            list[count + i + 1] = list0

        for i in range(len(list)):
            data_str1 = []
            data_gps = list[i].split()
            if data_gps[1] != '0.000000' and data_gps[2] != '0.000000':
                data_str1.append(float(data_gps[1]))
                data_str1.append(float(data_gps[2]))
                list2.append(data_str1)
        return list2

    except Exception as e:
        print(e)

def ori_file(file_name):
    try:
        file = open(file_name, 'r')
        list = file.readlines()
        list1=[]
        for i in range(len(list)):
            data_str1 = []
            data_gps = list[i].split()
            if data_gps[1] != '0.000000' and data_gps[2] != '0.000000':
                data_str1.append(float(data_gps[1]))
                data_str1.append(float(data_gps[2]))
                list1.append(data_str1)
        return list1
    except Exception as e:
        print e


def park_ios(file_name):
    """
    提取原始数据文件的经纬度写入算法程序所需的文件：zsPark_iOS.txt
    """
    file = open(file_name, 'r')
    list = file.readlines()
    list1 = []
    for line in list:
        data0 = line.split()
        if data0 != []:
            if data0[1] != '0.000000' and data0[2] != '0.000000':
                data = line.split()[:6]
                data1 = (" ").join(data)
                list1.append(data1)
    file1 = open(os.path.join(os.getcwd(), "build/zsPark_iOS.txt"), 'w')
    file1.write("# %s\n" % str(len(list1)))
    file1.write("# time lon lat ele hdop vdop\n")
    for i in range(len(list1)):
        file1.write(list1[i] + "\n")

def run_exe():
    os.system(os.path.join(os.getcwd(), "./build/main.exe ./build/zsPark_iOS"))

def gps_handle_data(file_name):
    """
    经过算法程序处理后，提取经纬度信息写入kml文件。
    """
    try:
        park_ios(file_name)
        run_exe()
        file = open(os.path.join(os.getcwd(), 'build/zsPark_iOS.plt'), 'r')
        list = file.readlines()
        list1 = []
        for line in list:
            if ",," in line:
                data = line.split(",")
                ll = []
                ll.append(float(data[1]))
                ll.append(float(data[0]))
                list1.append(ll)
        return list1
    except Exception as e:
        print(e)

#def add_voice_handle(latlon):

