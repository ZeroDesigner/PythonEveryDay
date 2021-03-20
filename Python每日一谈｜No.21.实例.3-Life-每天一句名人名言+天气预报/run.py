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
        num: 需要emoji 的数目，默认为 6，int
        file: 名人名言文件存放目录，默认为 ./soup-master/名人名言.tsv，str
        token: 申请的http://api.ip138.com/ip 的token，默认为 get_by_yourself，str
    返回：
        out(str)：含有emoji的字符串
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
