import pandas as pd
import os, sys
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re
import docx
from win32com import client as wc
import mammoth

print(os.getcwd())  # 获得当前工作目录
abspath = os.path.abspath('.')
print(os.listdir('.'))
if "DownloadUrls" not in abspath:
    print(os.chdir("Demo/DownloadUrls"))
cur_abspath = os.path.abspath('.')
print(os.listdir('.'))

data_in = pd.read_excel('文件清单.xlsx')


def savePage(url, pagefilename='page'):
    def soupfindnSave(pagefolder, tag2find='img', inner='src'):
        """保存所有的标记文本"""
        if not os.path.exists(pagefolder):  # 如果没有创建一个
            os.mkdir(pagefolder)
        for res in soup.findAll(tag2find):  # 保存标记文件
            try:
                if not res.has_attr(inner):  # 检查知否还有内部的标记文件
                    continue
                filename = re.sub('\W+', '', os.path.basename(res[inner]))  # clean special chars
                fileurl = urljoin(url, res.get(inner))
                filepath = os.path.join(pagefolder, filename)
                # html原文的重命名保存
                res[inner] = os.path.join(os.path.basename(pagefolder), filename)
                if not os.path.isfile(filepath):  # 保存到本地
                    with open(filepath, 'wb') as file:
                        filebin = session.get(fileurl)
                        file.write(filebin.content)
            except Exception as exc:
                print(exc, file=sys.stderr)
        return soup

    session = requests.Session()

    response = session.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features="lxml")
    pagefolder = './outFiles/' + pagefilename + '_files'  # page contents
    soup = soupfindnSave(pagefolder, 'img', 'src')
    soup = soupfindnSave(pagefolder, 'link', 'href')
    soup = soupfindnSave(pagefolder, 'script', 'src')
    with open('./outFiles/' + pagefilename + '.html', 'wb') as file:
        file.write(soup.prettify('gb18030'))
    return soup

# 测试保存百度首页
soup = savePage('https://www.baidu.com/', 'baidu')

data_in_url = data_in[data_in['type'] == "url"]
for index, row in data_in_url[['url', 'label']].iterrows():
    print(row['url'])
    print(str(row['label']))
    savePage(row['url'], str(row['label']))

# 处理附件doc
# 首先将doc转换成docx
word = wc.Dispatch("Word.Application")

doc = word.Documents.Open(cur_abspath + "\\" + r"14.doc")
# 使用参数16表示将doc转换成docx
doc.SaveAs(cur_abspath + "\\" + r"temp.docx", 16)
doc.Close()
word.Quit()

# 读取word内容
doc = docx.Document(cur_abspath + "\\" + r"temp.docx")

# 转换成html
f = open(cur_abspath + "\\" + r"temp.docx", 'rb')
b = open(cur_abspath + "\\" + r"temp.html", 'wb')
document = mammoth.convert_to_html(f)
b.write(document.value.encode('gb18030'))
f.close()
b.close()
