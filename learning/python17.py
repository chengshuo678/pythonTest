# 保持时间计划任务 和 启动程序
import time,datetime
print(time.time())

for i in range(1,4):
    print('hi')
    time.sleep(1)

print(datetime.datetime.now())

dt = datetime.datetime.now()
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)