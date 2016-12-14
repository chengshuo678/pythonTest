# project 关于密码口令的应用

PASSWORDS = {'email':'eamildasfdsf',
             'blog':'VmALvQyKAxiVH5G',
             'git':'1222git'
             }

import sys,pyperclip
if len(sys.argv)<2:
    print('Usage:python pw.y [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account + 'copied to clipboard')
else:
    print('There is no account named '+ account)


