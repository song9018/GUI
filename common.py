import re, os, glob, time


def yf_format_buf(org_buf, marker='dt:', skip='.*dt: len = '):  # for one line
    index = 0
    try:
        index = org_buf.index(marker)
    except:
        index = -1
    buf = ''
    if re.match(skip, org_buf):  # skip the len
        return buf
    if index >= 0:

        for chr in org_buf[index + len(marker):]:
            if chr.isdigit() or chr.isalpha():
                buf += chr
                # print buf
    return buf


def yf_byte(two_byte, rever=False):
    assert len(two_byte) == 4
    if rever:
        return two_byte[2:4] + two_byte[0:2]
    else:
        return two_byte


def get_bit_vaule(value, mask, offset=0):
    return ((value >> offset) & mask)


def yf_2byte_list(buf, rever=False):
    buf_list = []
    two_byte = ''
    i = 0
    for tmp in buf:
        # print tmp
        two_byte += tmp
        i += 1
        if i == 4:
            buf_list.append('0x' + yf_byte(two_byte, rever))
            two_byte = ''
            i = 0
    # if i != 0:
    #    print buf_list
    assert i == 0
    return buf_list


def yf_1byte_list(buf):
    buf_list = []
    one_byte = ''
    i = 1
    for tmp in buf:
        # print tmp
        one_byte += tmp
        if i % 2 == 0:
            buf_list.append('0x' + one_byte)
            one_byte = ''
        i += 1
    assert i % 2 != 0
    return buf_list


def yf_byte_list(buf, num):
    try:

        # assert(len(buf)%num == 0)
        buf_list = []

        for i in range(0, len(buf), num):
            buf_list.append(buf[i:i + num])
        return buf_list
    except Exception  as  e:
        print(e)


def rever_bytes(str_buf):
    assert (len(str_buf) % 2 == 0)
    out = ''
    for i in range(0, len(str_buf), 2):
        out = str_buf[i:i + 2] + out
    return out


def remove_end(buf):
    buf = buf.replace('\r', '')
    buf = buf.replace('\n', '')
    return buf


def utf8toGBK(utf_8_buf):
    unicodebuf = utf_8_buf.decode('UTF-8')
    return unicodebuf.encode('GBK')


def get_real_ord(num):
    # num_len = len(hex(num))-2
    num_len = len(hex(num).replace('0x', '').replace('L', ''))
    num_bytes = num_len / 2 if num_len % 2 == 0 else num_len / 2 + 1
    num = num if num & (int(pow(2, (num_bytes * 8 - 1)))) == 0 else -((pow(2, num_bytes * 8)) - 1 - num + 1)
    return num


def remove_txt(path):
    for file in glob.glob(os.path.join(path, '*.txt')):
        os.remove(file)


def remove_allfile(path):
    for file in glob.glob(os.path.join(path, '*')):
        os.remove(file)


def hex2dec(string_num):
    # print(str(int(string_num.upper(),16)))
    return str(int(string_num.upper(), 16))


def count(filepath):
    file = open(filepath, 'r', encoding='utf-8').read(4)
    # print(file)
    count = str(int(rever_bytes(file), 16))

    return int(count)


def decode_head(str_buf):
    uuid = int(hex2dec(rever_bytes(str_buf[0:32])))
    mode = int(hex2dec(rever_bytes(str_buf[32:34])))
    length = int(hex2dec(rever_bytes(str_buf[34:42])))
    discp = {'uuid': uuid, 'mode': mode, 'length': length}

    return discp


def decode_body(str_buf):
    UTC = int(hex2dec(rever_bytes(str_buf[0:8])))
    lat = int(hex2dec(rever_bytes(str_buf[8:16]))) / 10000000
    lon = int(hex2dec(rever_bytes(str_buf[16:24]))) / 10000000
    altitude = int(hex2dec(rever_bytes(str_buf[24:32]))) / 10000
    level = int(hex2dec(rever_bytes(str_buf[32:40]))) / 10000
    speed1 = (int(hex2dec(rever_bytes(str_buf[40:]))) / 10000) * 3.6
    speed = round(speed1, 2)
    discp = {'UTC': UTC, 'lat': lat, 'lon': lon, 'altitude': altitude, 'speed': speed}
    return discp


def timestamp_to_localtime(ptimestamp):
    ptime_struct = time.localtime(ptimestamp)
    time_format = time.strftime("%Y-%m-%d  %H:%M:%S", ptime_struct)
    return time_format


def localtime_format_to_timestamp(ptime):

    datestr = time.strptime(ptime, "%Y-%m-%d  %H:%M:%S")
    ptimestamp = time.mktime(datestr)
    return ptimestamp

# if __name__ == '__main__':
# buf = yf_format_buf('565.560 dt:01 E8 47 C3 ED D8 01 80 00 00 00 00 00 00 00 00 00 00 00 00 ')
# #yf_list = yf_2byte_list(buf, True)
# yf_list = yf_1byte_list(buf)
# print (yf_list)
