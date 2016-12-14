#!/usr/bin/python
import os
import sys
import xlrd
from datetime import date

sqlFormat='insert into tb_vivox5_coupon(uid,couponCode,status,sendTime,allocateTime,insertTime,updateTime)\
 values("","{code}",0,unix_timestamp("{dt} 00:00:00")*1000,0,unix_timestamp(now())*1000,unix_timestamp(now())*1000);\n'

def createCoupon():
    fd = date(2016,10,26)
    dt = fd - date(2016,10,14)

    print(fd)
    print(date(2016,10,14))
    print(dt)

    xls = xlrd.open_workbook('test.xlsx')
    sf = open('test.sql','w')
    sheet = xls.sheet_by_index(0)
    rowNum = sheet.nrows
    for i in range(1, rowNum):
        row = sheet.row_values(i)
        code = row[0]
        nd = (i-1) / 10000
        sd = fd + nd*dt
        dtstr = sd.strftime('%Y-%m-%d')
        sqlStr = sqlFormat.format(code=code,dt=dtstr)
        sf.write(sqlStr)
    sf.close()

if __name__ == '__main__':
    createCoupon()
