# encoding:utf-8

from xml.dom.minidom import Document


class WLP(object):
    def heart_wlp(self):
        self.doc = Document()  # 创建DOM文档对象
        self.SportDatabase = self.doc.createElement('SportDatabase')  # 创建根元素
        # SportDatabase.setAttribute('xmlns:xsd', "http://www.w3.org/2001/XMLSchema")  # 设置命名空间
        # SportDatabase.setAttribute('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
        self.SportDatabase.setAttribute('xmlns', 'http://www.weloop.com/xmlschemas/SportDatabase/v1')
        self.doc.appendChild(self.SportDatabase)

        # 根节点
        self.Activities = self.doc.createElement('Activities')
        self.SportDatabase.appendChild(self.Activities)

        # 第一子节点
        self.Activity = self.doc.createElement('Activity')
        self.Activity.setAttribute('DataType', 'SportData')
        self.Activities.appendChild(self.Activity)

    def add_activity(self, device_name, time, heart_rate=None, distance=None, step=None, speed=None, longitude=None,
                     latitude=None):
        self.device = self.doc.createElement('DeviceName')
        self.device_text = self.doc.createTextNode("%s" % device_name)  # 元素内容写入
        self.device.appendChild(self.device_text)
        self.Activity.appendChild(self.device)

        self.Time = self.doc.createElement('Time')
        self.Time.setAttribute('StartTime', '%s' % time)
        self.Activity.appendChild(self.Time)
        self.DistanceKMeters = self.doc.createElement("DistanceKMeters")
        self.HeartRate = self.doc.createElement("HeartRate")
        self.StepSpm = self.doc.createElement("StepRate")
        self.Speed = self.doc.createElement("Speed")
        self.LongitudeDegrees = self.doc.createElement("LongitudeDegrees")
        self.LatitudeDegrees = self.doc.createElement("LatitudeDegrees")
        # Gensor =
        self.DistanceKMeters_text = self.doc.createTextNode("%s" % distance)
        self.HeartRateBpm_text = self.doc.createTextNode("%s" % heart_rate)
        self.StepSpm_text = self.doc.createTextNode("%s" % step)
        self.Speed_text = self.doc.createTextNode("%s" % speed)
        self.LongitudeDegrees_text = self.doc.createTextNode("%s" % longitude)
        self.LatitudeDegrees_text = self.doc.createTextNode("%s" % latitude)

        self.Time.appendChild(self.HeartRate)
        self.Time.appendChild(self.DistanceKMeters)
        self.Time.appendChild(self.StepSpm)
        self.Time.appendChild(self.Speed)
        self.Time.appendChild(self.LongitudeDegrees)
        self.Time.appendChild(self.LatitudeDegrees)

        self.DistanceKMeters.appendChild(self.DistanceKMeters_text)
        self.HeartRate.appendChild(self.HeartRateBpm_text)
        self.StepSpm.appendChild(self.StepSpm_text)
        self.Speed.appendChild(self.Speed_text)
        self.LongitudeDegrees.appendChild(self.LongitudeDegrees_text)
        self.LatitudeDegrees.appendChild(self.LatitudeDegrees_text)

        self.Activity.appendChild(self.Time)

    def close_file(self):
        f = open('bookstore.xml', 'w')
        f.write(self.doc.toprettyxml(indent=''))
        f.close()


def heart():
    file = open("PPG1.txt", "r")
    lines = file.readlines()
    list_heart = []
    list_time = []
    for line in lines:

        if line.split(",")[0] != "Time":
            list_heart.append(line.split(",")[3])
            list_time.append(line.split(",")[0])
    return list_heart, list_time


if __name__ == "__main__":
    list_heart, list_time = heart()
    wlp = WLP()
    wlp.heart_wlp()
    for i in range(len(list_time)):
        wlp.add_activity("XH3", str(list_time[i]), str(list_heart[i]))
    wlp.close_file()
    file = open("bookstore.xml", "r")
    lines = file.readlines()
    for line in lines:
        if "<HeartRate>" in line:
            print line.split("<HeartRate>")[1].split("</HeartRate>")[0]
