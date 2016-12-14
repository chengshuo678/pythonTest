# 用shelve模块保存变量
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zoo', 'Alice', 'Mike', 'Gods']
shelfFile['cats'] = cats
shelfFile.close()

# 用shelve模块读取变量
shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()