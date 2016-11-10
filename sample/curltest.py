# -*- coding:utf-8 -*-
import pycurl
import os,sys
from io import BytesIO

buffer = BytesIO()
URL = "http://www.chinamcloud.com"
c = pycurl.Curl()
c.setopt(pycurl.URL, URL)
c.setopt(pycurl.CONNECTTIMEOUT, 10)
c.setopt(pycurl.TIMEOUT, 5)
#c.setopt(c.WRITEDATA, buffer)
bodyfile = open(r'C:\Users\Administrator\Desktop\text.txt','wb')
c.setopt(c.WRITEHEADER, bodyfile)
c.setopt(c.WRITEDATA, bodyfile)


try:
    c.perform()
except Exception as e:
    print("connection error:" + str(e))
    c.close()
#body = buffer.getvalue()
#print(body.decode('utf-8'))

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE =  c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD =  c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)

print ("HTTP状态码：%s" %(HTTP_CODE))
print("DNS解析时间：%.2f ms" % (NAMELOOKUP_TIME*1000))
print("建立连接时间：%.2f ms" % (CONNECT_TIME *1000))
print("准备传输时间：%.2f ms" % (PRETRANSFER_TIME*1000))
print("传输开始时间：%.2f ms" % (STARTTRANSFER_TIME *1000))
print("总时间：%.2f ms" % (TOTAL_TIME *1000))
print("下载数据包大小：%d bytes/s" %(SIZE_DOWNLOAD))
print("HTTP头部大小：%d byte" %(HEADER_SIZE))
print("平均下载速度：%d bytes/s" %(SPEED_DOWNLOAD))
c.close()