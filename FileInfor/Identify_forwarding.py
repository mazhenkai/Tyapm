import re
import os

print(os.getcwd())  # 获得当前工作目录
abspath = os.path.abspath('.')
print(os.listdir('.'))
if "FileInfor" not in abspath:
    print(os.chdir("Demo/FileInfor"))
cur_abspath = os.path.abspath('.')
print(os.listdir('.'))

text_in = '关于转发<关于印发<上海市党政机关会议定点管理实施细则>的通知>的通知'

pattern = r'(?!<)((?!<).)+?(?=>)'
m = re.search(pattern, text_in)
print(m.group(0))

