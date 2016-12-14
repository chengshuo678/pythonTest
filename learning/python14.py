# 遍历目录树

import os

for folderName, subfolders, fileNames in os.walk('D:\\pythonTest2'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF '+ folderName + ': ' + subfolder)
    for fileName in fileNames:
        print('FILE INSIDE '+ folderName + ': ' + fileName )

    print(' ')
