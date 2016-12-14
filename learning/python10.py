# regex
# import re
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-(\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-888-3666')
# if mo:
#     print('number is: ' + mo.group(1))
# else:
#     print("no match")

import re
phoneNum = re.compile(r'\d\d-\d')
match = phoneNum.findall("my num is 12-1 and 78-4 79-0")
for content in match:
    print(content)
