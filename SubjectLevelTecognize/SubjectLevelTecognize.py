import re
import os

print(os.getcwd())  # 获得当前工作目录
abspath = os.path.abspath('.')
print(os.listdir('.'))
if "SubjectLevelTecognize" not in abspath:
    print(os.chdir("Demo/SubjectLevelTecognize"))
cur_abspath = os.path.abspath('.')
print(os.listdir('.'))

text_in = "广西壮族自治区爱国卫生运动委员会办公室2020年1月13日"
# text_in = "2020/01/13"

pattern = r'\d{1,4}(\-|\/|\.|年)\d{1,2}(\-|\/|\.|月)\d{1,2}(\-|\/|\.|日)'
m = re.search(pattern, text_in)
print(m.group(0))
