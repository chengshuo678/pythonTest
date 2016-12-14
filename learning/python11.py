# 文件处理
helloFile = open('D:\\test.txt')
fileContent = helloFile.read()
print(fileContent)
file = open('D:\\test.txt', 'a') #添加模式
#file = open('D:\\test.txt', 'w') #写模式
file.write('you are my world!')
print(helloFile.read())

helloFile.close()
file.close()