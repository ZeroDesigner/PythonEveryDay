---
title: Python每日一谈｜No.21.实例.3-Life-每天一句名人名言+天气预报
categories: Python每日一谈
---

### 简介

今天我们来写一个每日一句

先看看效果

---

👻👽⭐👽🗻👻

python every day

 生活的道路一旦选定，就要勇敢地走到底，决不回头。

————————————

🗓|日期：2021-03-20

🌏|坐标： 北京

🌌|天气： 晴

🌡|温度：低温 2℃~高温 15℃

🌬|风力：3级

---

先来简单分析下

1. emoji

   web:https://www.emojiall.com/zh-hans

   简介：绘文字（日语：絵文字/えもじemoji）是日本在无线通信中所使用的视觉情感符号，绘指图画，文字指的则是字符，可用来代表多种表情，如笑脸表示笑、蛋糕表示食物等。 在NTTDoCoMo的i-mode系统电话系统中，绘文字的尺寸是12x12像素，在传送时，一个图形有2个字节。Unicode编码为E63E到E757，而在Shift-JIS编码则是从F89F到F9FC。基本的绘文字共有176个符号，在C-HTML4.0的编程语言中，则另增添了76个情感符号。 最早由栗田穰崇（Shigetaka Kurita）创作，并在日本网络及手机用户中流行。 自苹果公司发布的iOS 5输入法中加入了emoji后，这种表情符号开始席卷全球，目前emoji已被大多数现代计算机系统所兼容的Unicode编码采纳，普遍应用于各种手机短信和社交网络中。

   来源于--知乎

   然后，使用一个python包来调用

   web：https://pypi.org/project/emoji/

   安装：`pip install emoji`

   先看一下关键字和表情的对应表：https://www.webfx.com/tools/emoji-cheat-sheet/

   ![image-20210320143730509](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210320143730509.png)

   使用：

   
   
   ```
   In [29]:import emoji
   In [30]: print(emoji.emojize(':smile:',use_aliases=True))
   😄
   ```
   
2. python every day

   欢迎关注我的微信公众号(FindKey)，知乎(ZeroDesigner)，b站(ZeroDesigner)什么的，没了，这就是一个字符串

3. 名人名言

   我们先来找碗鸡汤

   我这里准备了一份，在当前目录下，为`tsv`格式,分割符为`table`键，名称为`名人名言.tsv`

   先来看下

   ```
   名言	出处
   君子赠人以言，庶人赠人以财。	荀况
   使意志获得自由的唯一途径，就是让意志摆脱任性。	黑尔
   如烟往事俱忘却，心底无私天地宽。	陶铸
   执着追求并从中得到最大快乐的人，才是成功者。	梭罗
   有百折不挠的信念的所支持的人的意志，比那些似乎是无敌的物质力量有更强大的威力。	爱因斯坦
   生活在我们这个世界里，不读书就完全不可能了解人。	高尔基
   一个人即使已登上顶峰，也仍要自强不息。	罗素·贝克
   对具有高度自觉与深邃透彻的心灵的人来说，痛苦与烦恼是他必备的气质。	陀思妥耶夫斯基
   先相信你自己，然后别人才会相信你。	屠格涅夫
   上天赋予的生命，就是要为人类的繁荣和平和幸福而奉献。	松下幸之助
   ```
   安装`pandas`:
   
   ```shell
   pip install pandas
   ```
    使用：
   ```python
   import pandas as pd
   data = pd.read_csv('./名人名言.tsv',sep='\t')
   ```
   
   
   
4. 获取日期

   使用python自带的datatime模块

   例如:
   
   ```python
   In [39]: # 导入
       ...: import datetime
       ...: # 获取当前时间，并且格式化为年-月-日形式
       ...: t = datetime.datetime.now().strftime('%Y-%m-%d')
       ...: print(t)
   2021-03-20
   ```
   
5. 获取地址，定位到城市
   
   a. 首先查询本机ip地址
   
   ```
   In [100]: #导入python自带的包
        ...: import requests
        ...: url = 'http://txt.go.sohu.com/ip/soip'
        ...: web = requests.get(url)
        ...: web.text
   Out[100]: 'String.prototype.getQueryString=function(v){var reg=new RegExp("(^|&|\\\\?)" + v + "=([^&]*)(&|$)"), r;if(r=this.match(reg)){return unescape(r[2]);}return null;};var sohu_IP_Loc="unknown",LocUrl=document.location.href;if((LocUrl.indexOf("sohusce.com") >= 0)||(LocUrl.indexOf("sohu.com") >= 0)||(LocUrl.indexOf("chinaren.com") >= 0)||(LocUrl.indexOf("17173.com") >= 0)||(LocUrl.indexOf("focus.cn") >= 0)){window.sohu_user_ip="111.201.148.162";sohu_IP_Loc="CN110000";sohu_IP_Loc_V="CN110000";}var AdLoc2=sohu_IP_Loc.substr(0,2),AdLoc4=sohu_IP_Loc.substr(0,4),AdLoc6=sohu_IP_Loc.substr(0,6);if(window.location.href.getQueryString("ip"))sohu_IP_Loc=AdLoc2=AdLoc4=AdLoc6=window.location.href.getQueryString("ip");'
   # 可以看到ip地址为111.201.148.162
   #先分割，取1号，再分割，取0，当然，你喜欢用正则，我也不拦着
   In [103]: web.text.split('{window.sohu_user_ip="')[1].split('";sohu_IP_Loc=')[0]
   Out[103]: '111.201.148.162'
   ```
   
   b. 根据ip地址获取城市信息
   
   一般分为两种方式
   
   1. 一种是使用api通过网页
   
   2. 一种是离线：https://blog.csdn.net/qf0129/article/details/83145765
   
   我现在使用网页api
   
   地址：https://www.ip138.com
   
   申请一个token
   
   https://user.ip138.com/ip/
   
   ![image-20210320162145213](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210320162145213.png)
   
   选择在线API申请，注册完成之后，校验信息那边有token
   
   ![Screen Shot 2021-03-20 at 4.22.14 PM](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/Screen%20Shot%202021-03-20%20at%204.22.14%20PM.png)
   
   ip查询接口文档为：
   
   https://user.ip138.com/ip/doc
   
   查询：
   
   http://api.ip138.com/ip/?ip=填入你的ip地址&datatype=text&token=填入你的token
   
   ```
   In [98]: import requests
    ...: url = 'http://api.ip138.com/ip/?ip=111.200.157.165&datatype=text&token=abbbcccddd123456789'
    ...: web = requests.get(url)
    ...: web.text
   Out[98]: '111.200.157.165\t中国 北京 北京  联通 100000 010'
   In [99]: # 很明显的可以看到是国家省份城市
    ...: # 我们再来看一个
   In [97]: import requests
   ...: url = 'http://api.ip138.com/ip/?ip=27.128.190.0&datatype=text&token=f6f
   ...: 83777eef0804454d340dd7aabbcb4'
   ...: web = requests.get(url)
   ...: web.text
   Out[97]: '27.128.190.0\t中国 河北 石家庄  电信 050000 0311'
   In [97]: # 获取城市信息
   In [74]: city = web.text.split()[3]
   In [75]: city
   Out[75]: '石家庄'  
   ```
   

   
6. 查询本市的天气

   使用中华万年历API接口，获取天气信息，json格式

   http://wthrcdn.etouch.cn/weather_mini?city=北京

   ```
   In [96]: import requests
       ...: url = 'http://wthrcdn.etouch.cn/weather_mini?city=北京'
       ...: web = requests.get(url)
       ...: web.text
   Out[96]: '{"data":{"yesterday":{"date":"19日星期五","high":"高温 10℃","fx":"西南风","low":"低温 3℃","fl":"<![CDATA[2级]]>","type":"小雨"},"city":"北京","forecast":[{"date":"20日星期六","high":"高温 15℃","fengli":"<![CDATA[3级]]>","low":"低温 3℃","fengxiang":"西北风","type":"晴"},{"date":"21日星期天","high":"高温 13℃","fengli":"<![CDATA[3级]]>","low":"低温 0℃","fengxiang":"西北风","type":"晴"},{"date":"22日星期一","high":"高温 18℃","fengli":"<![CDATA[2级]]>","low":"低温 3℃","fengxiang":"西南风","type":"晴"},{"date":"23日星期二","high":"高温 19℃","fengli":"<![CDATA[1级]]>","low":"低温 7℃","fengxiang":"南风","type":"晴"},{"date":"24日星期三","high":"高温 20℃","fengli":"<![CDATA[2级]]>","low":"低温 4℃","fengxiang":"北风","type":"晴"}],"ganmao":"感冒易发期，外出请适当调整衣物，注意补充水分。","wendu":"12"},"status":1000,"desc":"OK"}'
   In [97]: # 解析json
   In [104]: import json
   In [131]: wea_dict=json.loads(web.text)
   In [132]: wea_dict
   Out[132]:
   {'data': {'yesterday': {'date': '19日星期五',
      'high': '高温 10℃',
      'fx': '西南风',
      'low': '低温 3℃',
      'fl': '<![CDATA[2级]]>',
      'type': '小雨'},
     'city': '北京',
     'forecast': [{'date': '20日星期六',
       'high': '高温 15℃',
       'fengli': '<![CDATA[3级]]>',
       'low': '低温 3℃',
       'fengxiang': '西北风',
       'type': '晴'},
      {'date': '21日星期天',
       'high': '高温 13℃',
       'fengli': '<![CDATA[3级]]>',
       'low': '低温 0℃',
       'fengxiang': '西北风',
       'type': '晴'},
      {'date': '22日星期一',
       'high': '高温 18℃',
       'fengli': '<![CDATA[2级]]>',
       'low': '低温 3℃',
       'fengxiang': '西南风',
       'type': '晴'},
      {'date': '23日星期二',
       'high': '高温 19℃',
       'fengli': '<![CDATA[1级]]>',
       'low': '低温 7℃',
       'fengxiang': '南风',
       'type': '晴'},
      {'date': '24日星期三',
       'high': '高温 20℃',
       'fengli': '<![CDATA[2级]]>',
       'low': '低温 4℃',
       'fengxiang': '北风',
       'type': '晴'}],
     'ganmao': '感冒易发期，外出请适当调整衣物，注意补充水分。',
     'wendu': '12'},
    'status': 1000,
    'desc': 'OK'}
   
   In [135]: # 所以今天的天气为
   In [136]: wea_dict['data']['forecast'][0]
   Out[136]:
   {'date': '20日星期六',
    'high': '高温 15℃',
    'fengli': '<![CDATA[3级]]>',
    'low': '低温 3℃',
    'fengxiang': '西北风',
    'type': '晴'}
      
   ```
   
7. 整体代码




```
# -*- coding: utf-8 -*-
# 导入所需包

import json
import emoji
import random
import datetime
import requests
import pandas as pd

# 随机形成几个emoji字符
def random_emoji(num):
    # 挑选几个比较优质的emoji
    emoji_list = [':thumbs_up:',':collision:',':star:',':sparkles:',':alien:',':fire:',':whale:',   ':mount_fuji:',':ghost:']
    # 将其随机组合成几个字符
    emoji_str = ''
    for i in range(num):
      emoji_str = emoji_str + random.choice(emoji_list)
    return emoji_str
  
# 读取名人名言并随机选择一条
def get_saying(file):
    df = pd.read_csv(file,sep='\t')
    return random.choice(df['名言'])

# 定义获取ip的函数
def get_host_ip():
    url = 'http://txt.go.sohu.com/ip/soip'
    web = requests.get(url)
    return web.text.split('{window.sohu_user_ip="')[1].split('";sohu_IP_Loc=')[0]
  
# 定义通过ip获取城市的函数
def get_city(ip,token):
    url = 'http://api.ip138.com/ip/?ip='+ip+'&datatype=text&token='+token
    web = requests.get(url)
    return web.text.split()[3]
  
# 定义通过城市获取天气信息的函数
def get_weather(city):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='+city
    web = requests.get(url)
    wea_dict = json.loads(web.text)
    return wea_dict['data']['forecast'][0]
  
# 填入我们的格式化字符串中
def output_str(emoji_str,saying,city,wea_dict):
    # 获取日期
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    # 格式化字符串
    format_str = "%s \npython every day\n %s \n————————————  \n🗓|日期：%s \n🌏|坐标： %s\n🌌|天气： %s\n🌡|温度：%s\n🌬|风力：%s"
    # 解析天气信息
    wea_type = wea_dict['type']
    wind = wea_dict['fengli'].split('CDATA[')[1][:2]
    temp = wea_dict['low'] + '~' + wea_dict['high']
    out = format_str % (emoji_str, saying, date, city, wea_type, temp,wind)
    return out

def simply_get_everyday(num = 6, file = './soup-master/名人名言.tsv', token = 'get_by_yourself'):
    # 注释：因为无复杂函数，所以只是为此函数作说明
    """
    描述:
        自动获取当前地理位置，天气，以及名人名言
        输出每日一句
    参数:
        num: 需要emoji 的数目,默认为 6,类型:int
        file: 名人名言文件存放目录,默认为 ./soup-master/名人名言.tsv,类型:str
        token: 申请的http://api.ip138.com/ip 的token,默认为 get_by_yourself,类型:str
    返回：
        out,含有emoji的字符串,类型:str
    使用：
        >>> out = simply_get_everyday(6,'./soup-master/名人名言.tsv','aaaaaaaabbbbbbcccccddddd123454')
        >>> print(out)
            👻👽⭐👽🗻👻
            python every day
             生活的道路一旦选定，就要勇敢地走到底，决不回头。
            ————————————
            🗓|日期：2021-03-20
            🌏|坐标： 北京
            🌌|天气： 晴
            🌡|温度：低温 2℃~高温 15℃
            🌬|风力：3级
    异常：
        TypeError: emoji的数目类型输入错误
        IndexError: token输入错误，或者已经失效
        FileNotFoundError: 名人名言文件位置输入错误
    """
    emoji_str = random_emoji(num)
    saying = get_saying(file)
    ip = get_host_ip()
    city = get_city(ip,token)
    wea_dict = get_weather(city)
    out = output_str(emoji_str,saying,city,wea_dict)
    return emoji.emojize(out)
# 进入主函数
if __name__ == "__main__":
    print(simply_get_everyday(num = 6, file = './soup-master/名人名言.tsv', token = 'aaaaaabbbbbcccccddddd1234'))

```

