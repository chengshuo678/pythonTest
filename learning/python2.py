# name = ''
# while name != 'chengshuozhang':
#     print('Please input your name.')
#     name = input()
# print('Thank you')


# while 1:
#     print('Please input your name.')
#     name = input()
#     if name == "chengshuozhang":
#         print("a good man.")
#         break

name=''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
num = int(input())
if num:
    print('Be sure to have enough root for all your guests:')
print('done')
