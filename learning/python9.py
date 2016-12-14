#字典
# birthdays = {'Alice':'Apr 1','Bob':'Dec 12','Carol':'Mar 4'}
#
# while True:
#     print('Enter a name:(Blank to quit)')
#     name = input()
#     if name == '':
#         break
#
#     if name in birthdays:
#         print(birthdays[name]+ ' is the birthday of '+name)
#     else:
#         print('no information')
#         print('Please input :')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated!')

def displayInventory(dict):
    sum = 0
    for k,v in dict.items():
        print('name:',k,' and v :',v)
        sum = sum + int(v)
    print("in total: ",sum)

testDict = {'rope':1,'torch':6,'gold coin':8}

displayInventory(testDict)
