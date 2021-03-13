import re
import os
from bs4 import BeautifulSoup

print(os.getcwd())  # 获得当前工作目录
abspath = os.path.abspath('.')
print(os.listdir('.'))
if "ExtractPlainText" not in abspath:
    print(os.chdir("Demo/ExtractPlainText"))
cur_abspath = os.path.abspath('.')
print(os.listdir('.'))

soup = BeautifulSoup(open("16.html"))
all_text = soup.text
all_text_net = re.sub('\s+', '', all_text)

resentencesp = re.compile('([﹒﹔﹖﹗．；。！？]["’”」』]{0,2}|：(?=["‘“「『]{1,2}|$))')

sentence = '他不停地说：“这样下去是很难的"'

def splitsentence(sentence):
    s = sentence
    slist = []
    for i in resentencesp.split(s):
        if resentencesp.match(i) and slist:
            slist[-1] += i
        elif i:
            slist.append(i)
    return slist

splitsentence(sentence)

res = splitsentence(all_text_net)
res
