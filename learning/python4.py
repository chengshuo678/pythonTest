#global
def spam():
    eggs = 'big egg' #局部作用
eggs = 'little egg'
spam()
print(eggs)
