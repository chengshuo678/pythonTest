# 时间多线程
import threading, time

print('start this program')

def takeANap():
    time.sleep(5)
    print("wake up!")

threadObj = threading.Thread(target=takeANap)
threadObj.start()
for i in range(1,3):
    time.sleep(1)
    print("main Program:",i)

print('End of program.')