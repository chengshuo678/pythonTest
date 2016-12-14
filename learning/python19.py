# 启动外部程序
import subprocess,threading

def open():
    subprocess.Popen('C:\\Windows\\System32\\calc.exe')

for i in range(0,3):
    thread = threading.Thread(target=open)
    thread.start()

