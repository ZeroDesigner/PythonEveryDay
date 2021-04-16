---
title: Python每日一谈｜No.34.实例.14. Pubchem简介
categories: Python每日一谈
top: true
---



## 1：Pubchem简介

**PubChem**，即**有机小分子生物活性数据**，是一种化学模组的[数据库]，由美国国家健康研究院（ US National Institutes of Health，NIH）支持，[美国国家生物技术信息中心]。
其主要目标是向CAS看齐，是目前开源的最大的化学数据库之一。

## 2：爬虫简介
百科：（又被称为[网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有[蚂蚁](https://www.baidu.com/s?wd=%E8%9A%82%E8%9A%81&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)、自动索引、模拟程序或者蠕虫。

目的：
主要是想通过手中的小分子（药物）的CAS编号，从PubChem上爬取其相关的信息。
首要是先把PubChem的CID编号爬取下来，PubChem并没有向SDF文件中添加CAS编号相关信息。所以必须取得其唯一的CID编号才可以进行检索。

## 过程记录：
### 1：初期的文本为 cas.txt
内容：
113775-47-6
50924-49-7
37106-97-1
104206-65-7
2152-44-5

### 2：环境设置
python使用版本为3.7，IDE为PyCharm，需要的包为：re(正则表达式)，fake_useragent（请求头随机生成器），selenium（爬虫工具），webdriver（浏览器驱动）

### 3：脚本编写

#### 包导入

```
import re
from fake_useragent import UserAgent
from selenium import webdriver
```
**webdriver可以认为是浏览器的驱动器，要驱动浏览器必须用到webdriver，支持多种浏览器，这里以Edge为例 **

```
browser = webdriver.Edge()
```
##### 添加网址，PubChem的。

```
url='https://pubchem.ncbi.nlm.nih.gov/search/#query=cas'
```
#### 创建关于CAS以及CID的列表,请求头导入

```
CASid=[]
CIDid=[]
ua=UserAgent()
```
####  打开文件，导入初始文件, 将CAS编号转变为列表储存

```
CAS_file=open('C:\\Users\\cas.txt','r',encoding='utf-8')
cas_line=CAS_file.readlines()
```
```python
for i in range(len(cas_line)):
    cas_url=re.sub(r'cas',cas_line[i],url)
   # 替换url中的cas，使其成为cas编码
    headers = {"User-Agent": ua.random}
    # 请求头设置随机,为了反爬虫
    browser.get(cas_url)
    text=browser.page_source
    # browser.page_source是获取网页的全部html，下面是通过正则表达式来进行网页的文本内容检索，即获取检索后的网页上的CID编号
    if re.search(r'CID' + '\d+', text):
        CID = re.findall(r'CID' + '\d+', text)
        CASid.append(cas_line[i])
        CIDid.append(CID)
        str1=str(CIDid[i])+','+str(CASid[i])
        cas_cid.write(str1)
        str2 = str(CIDid[i]) + ',' + str(CASid[i])
        cas_cid_num.write(str2)
    else:
        CASid.append(cas_line[i])
        CIDid.append('none')
        str1 = str(CIDid[i]) + ',' + str(CASid[i])
        cas_cid.write(str1)
        str2 = str(CIDid[i]) + ',' + str(CASid[i])
        cas_cid_no.write(str2)
#然后是将结果导出到新的文本
for i in range(len(CASid)):
    cas_cid = open('C:\\Users\\CAS-CID.txt', 'a',
                   encoding='utf-8', newline='')
    str1 = str(CIDid[i]) + ',' + str(CASid[i])
    cas_cid.write(str1)
browser.close()

```

