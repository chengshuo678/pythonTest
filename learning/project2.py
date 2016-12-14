# phone And email
import pyperclip,re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    numlist = [groups[1],groups[3],groups[5]]
    phoneNum = '-'.join(numlist)
    # if groups[8] != '':
    #     phoneNum += ' x' + groups[0]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy result to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')

# test data
# General inquiries: info@nostarch.com dfsfmedia@nostarch1.com 555-888-7777
# Media requests: media@nostarch.com dfsdf 777-555-6598
# Academic requests: academic@nostarch.com (Please see this page for academic review requests)
# Help with your order: info@nostarch.com