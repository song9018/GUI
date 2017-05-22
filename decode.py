# coding=utf-8
import logging,logging.config
from common import *
from yf_time import *
from DataStructure import *


class DecodeGPSAndHeardData(object):
    tag = 0
    cadence_type = 0
    cacence_tag = 0
    lon = 0
    lat = 0
    altitude = 0
    UTC = 0
    result_dir = os.path.join(os.getcwd(), 'result')
    log_dir = os.path.join(os.getcwd(), 'log')
    lon_lat_list = []

    def __init__(self):
        self.log = logging.getLogger('exeTestLog')
        self.yf = utc_time()
        self.yf.modify_utc_start_time()
        self.lon_lat_list = []

    def decodeGPSAndHeardDataString(self, pstring="", filename="gpsData", file_kml='gps_ori_data.kml'):
        cell_data_len = 0
        temp_disc = {}
        buf = pstring.replace(" ", "").strip()  # 去空格

        for cell in yf_byte_list(buf, 16):
            if cell_data_len == 0:  # 每个完整单位才计算tag,例如gps标签数据需要16byte，即2个8byte，循环值第二个8byte不需要求tag

                self.tag = eval('0x' + cell[0:2]) & 0x0f
                self.cadence_type = eval('0x' + cell[0:2]) & 0x0700
                self.cacence_tag = eval('0x' + cell[0:2]) & 0x0800

            cell_data_len += int(len(cell) / 2)
            if self.tag in temp_disc.keys():
                temp_disc[self.tag] += cell
            else:
                temp_disc[self.tag] = cell
            if cell_data_len == DATA[TAG[self.tag]]:
                if hasattr(self, TAG[self.tag]):
                    result = getattr(self, TAG[self.tag])(temp_disc[self.tag])
                    if 'gpsData' in result.keys():
                        each_dist = []
                        each_dist.append(result['gpsData']['lon'])
                        each_dist.append(result['gpsData']['lat'])
                        self.lon_lat_list.append(each_dist)
                        with open(os.path.join(self.result_dir, filename + "_gpsData.txt"), 'a') as fp:
                            fp.write(str(result['gpsData']))
                            fp.write("\n")

                    if 'heartData' in result.keys():
                        with open(os.path.join(self.result_dir, filename + "_heartData.txt"), 'a') as fp:
                            fp.write(str(result['heartData']))
                            fp.write("\n")

                    if 'step_frequeData' in result.keys():
                        with open(os.path.join(self.result_dir, filename + "_step_frequeData.txt"), 'a') as fp:
                            fp.write(str(result['step_frequeData']))
                            fp.write("\n")

                    if 'stroke_frequeData' in result.keys():
                        with open(os.path.join(self.result_dir, filename + "_stroke_frequeData.txt"), 'a') as fp:
                            fp.write(str(result['stroke_frequeData']))
                            fp.write("\n")

                    if 'bicycle_frequeData' in result.keys():
                        with open(os.path.join(self.result_dir, filename + "_bicycle_frequeData.txt"), 'a') as fp:
                            fp.write(str(result['bicycle_frequeData']))
                            fp.write("\n")
                else:
                    self.log.info("不存在该数据类型")
                temp_disc = {}
                cell_data_len = 0

    def RECORD_TAG_GPS_HEAD(self, pstr):
        try:
            dist = {}

            self.log.info("RECORD_TAG_GPS_HEAD       " + pstr)
            type = eval('0x' + rever_bytes(pstr[0:4])) & 0x000f
            speed = eval('0x' + rever_bytes(pstr[0:4])) & 0xfff0
            self.lon = get_real_ord(eval('0x' + rever_bytes(pstr[4:12])))
            self.lat = get_real_ord(eval('0x' + rever_bytes(pstr[12:20])))
            self.altitude = get_real_ord(eval('0x' + rever_bytes(pstr[20:24])))
            self.UTC = eval('0x' + rever_bytes(pstr[24:]))
            dist = {"type": type, "speed": speed / 100, "lon": self.lon / 1000000, "lat": self.lat / 1000000,
                    "altitude": self.altitude, "UTC": self.yf.seconds_to_utc(self.UTC).show()}
            self.log.info("解析结果 " + str(dist))
            return {'gpsData': dist}
        except Exception as e:
            self.log.info("解析gps标签数据：" + pstr + "出错")
            self.log.info(e)

    def UPDATE_RECORD_TAG_GPS(self, pdist):
        dist = {}
        dist['type'] = pdist["type"]
        dist['speed'] = pdist['speed'] / 100
        self.lon = self.lon + pdist["lon"]
        self.lat = self.lat + pdist["lat"]
        self.altitude = self.altitude + pdist["altitude"]
        self.UTC = self.UTC + pdist["UTC"]
        dist['lon'] = self.lon / 1000000
        dist['lat'] = self.lat / 1000000
        dist['altitude'] = self.altitude
        dist['UTC'] = self.yf.seconds_to_utc(self.UTC).show()
        return dist

    def RECORD_TAG_GPS_DIFF(self, pstr):
        try:

            self.log.info("RECORD_TAG_GPS_DIFF    " + pstr)
            dist = {}
            type = eval('0x' + rever_bytes(pstr[0:4])) & 0x000f
            speed = eval('0x' + rever_bytes(pstr[0:4])) & 0xfff0
            lon = get_real_ord(eval('0x' + rever_bytes(pstr[4:8])))
            lat = get_real_ord(eval('0x' + rever_bytes(pstr[8:12])))
            altitude = get_real_ord(eval('0x' + pstr[12:13]))
            UTC = eval('0x' + pstr[13:])
            dist = {"type": type, "speed": speed, "lon": lon, "lat": lat, "altitude": altitude, "UTC": UTC}
            gpsdist = self.UPDATE_RECORD_TAG_GPS(dist)
            self.log.info("gps差值数据解析结果为    " + str(dist))
            self.log.info("经叠加gps差值数据后的数据为  " + str(gpsdist))
            return {'gpsData': gpsdist}
        except Exception as e:
            self.log.info("解析gps差值数据： " + pstr + "出错")
            self.log.info(e)

    def RECORD_TAG_SPORT_CADENCE(self, pstr):  # 其他运动数据在此基础上扩展

        self.log.info("RECORD_TAG_SPORT_CADENCE   " + pstr)
        if self.cadence_type == 0 and self.cacence_tag == 0:  # 心率数据
            if hasattr(self, CADENCETYPE[self.cadence_type]):
                return getattr(self, CADENCETYPE[self.cadence_type])(pstr)

        elif self.cadence_type == 1 and self.cacence_tag == 1:  # 运动步频数据
            if hasattr(self, CADENCETYPE[self.cadence_type]):
                return getattr(self, CADENCETYPE[self.cadence_type])(pstr)

    def bytelist_to_declist(self, plist):
        fre_list = []
        for one in yf_1byte_list(str):
            fre_list.append(eval(one))
        return fre_list

    def CADENCE_TYPE_HERAT(self, pstr):
        """
        #解析心率数据
        :param pstr: 字节串
        :return: json格式的数据
        """
        try:
            hutc = eval('0x' + rever_bytes(pstr[2:10]))
            hinterval = eval('0x' + pstr[10:12])
            reserve = []
            for one in yf_1byte_list(pstr[12:]):
                reserve.append(eval(one))
            self.log.info("心率数据解析结果为    " + str({'utc': hutc, 'interva': hinterval, 'reserve': reserve}))
            return {"heartData": {'utc': hutc, 'interva': hinterval, 'reserve': reserve}}
        except Exception as e:
            self.log.info("解析心率数据：" + pstr + "出错")
            self.log.info(e)

    def CADENCE_TYPE_STEP(self, pstr):  # 运动步频
        self.log.info("解析的数据为运动步频数据，原始数据为：  " + pstr)
        return {"step_frequeData": self.bytelist_to_declist(pstr)}

    def CADENCE_TYPE_STROKE(self, pstr):  # 划水频率
        self.log.info("解析的数据为划水频率数据，原始数据为：  " + pstr)
        return {"stroke_frequeData": self.bytelist_to_declist(pstr)}

    def CADENCE_TYPE_BICYCLE(self, pstr):  # 自行车踏频
        self.log.info("解析的数据为pstr数据，原始数据为：  " + pstr)
        return {"bicycle_frequeData": self.bytelist_to_declist(pstr)}

    def RECORD_TAG_SPORT_INFO(self, str):  # 待后续添加

        self.log.info("RECORD_TAG_SPORT_INFO    " + str)
        return

    def out_lon_and_lat_list(self):
        return self.lon_lat_list

    def out_kmlfile(self, file_kml, filename="gps"):
        try:
            file = open(os.path.join(os.getcwd(), file_kml), 'r', encoding='utf-8')
            list = file.readlines()

            len_t = len(list) - 1
            for i in range(len_t):
                if '<coordinates>' in list[i]:
                    data = list[i].split('<coordinates>')[1].split('</coordinates>\n')
                    data = data[0]
                    data1 = ','.join(self.lon_lat_list)
                    mewdata = data1.replace(',0,', ',0 ')


                    list[i] = list[i].replace(data, mewdata)
                    if os.path.isdir(self.result_dir):
                        newfile = open(os.path.join(self.result_dir, filename + "_gps.kml"), 'w',
                                       encoding='utf-8')
                        newfile.writelines(list)
        except Exception as e:
            print(e)
