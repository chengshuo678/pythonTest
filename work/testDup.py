# 读取 1.txt 判断重复

content = open('3', encoding='utf-8')
sum = []
for line in content.readlines():
    nub = line[0:4]
    if nub not in sum :
        sum.append(nub)
    else:
        print("error!:"+nub)
    print(nub)
sum.sort()
print(sum)
print(str(len(sum)))

