# coding=utf-8
import logging.config
from decode import *


def oridatafile_transform(path):  # 单个文件解析
    log = logging.getLogger('exeTestLog')
    if path:
        filename = os.path.basename(path)
        if filename:
            newfilename = re.match("^.+(?=\.)", filename).group(0)
            decodehandler = DecodeGPSAndHeardData()
            with open(path, 'r')  as fp:
                a = fp.read()
                decodehandler.decodeGPSAndHeardDataString(a, newfilename)  # 解析成文件
                return decodehandler.out_lon_and_lat_list()  # 返回经纬度的列表
        else:
            log.error("未获取到文件名")

    else:
        log.error("给定的路径为空")


if __name__ == '__main__':
    print(oridatafile_transform(u"F:/GUI/无跑步数据的gps数据.txt"))
