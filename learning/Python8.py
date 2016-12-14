# 练习题

def converFunction(list):
    last = len(list)-1
    list[last] = 'and '+list[last]

testList = ['21','dfsds','ccc']
converFunction(testList)
str = ''
for name in testList:
    str = str + ',' +name

output = str[1:len(str)]
print(output)

