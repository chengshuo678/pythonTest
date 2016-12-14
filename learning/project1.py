# 操作剪切板里的东西

import pyperclip
text = pyperclip.paste()

#将剪切板中 每一行 加入 *空格

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* '+lines[i]

#将列表转换成字符串
text = "\n".join(lines)

pyperclip.copy(text)
