import re
import os

print(os.getcwd())  # 获得当前工作目录
abspath = os.path.abspath('.')
print(os.listdir('.'))
if "FileInfor" not in abspath:
    print(os.chdir("Demo/FileInfor"))
cur_abspath = os.path.abspath('.')
print(os.listdir('.'))

text_in = '厅关于印发医药卫生体制五项重点改革2009年工作安排的通知国办函〔2009〕75号各省、自治区、直辖市人民政府，国务院各有关部门：《医药卫生体制五项重点改革2009年工作安排》（以下简称《工作安排》）已经国务院同意，现印发给你们，请结合实际，认真组织实施。'
text_in ='沪府办发〔2018〕29号上海市人民政府办公厅关于印发《上海市推进社会公益事业建设领域政府信息公开工作实施方案》的通知'


pattern = r'.{1,10}[令发言任复文函电字][组综经资财金审土能农林水工交商海旅市安城环科教文广新卫体人妇劳事监公全司明扶族宗对港防粮盐烟其]{0,2}〔20[0-9]{2}〕[0-9]{1,3}号'
m = re.search(pattern, text_in)
print(m.group(0))

