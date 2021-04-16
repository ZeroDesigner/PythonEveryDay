---
title: Python每日一谈｜No.25.实例.6-Life.2-Python-加密
categories: Python每日一谈
top: true
---

### 简介：

起因，由于收到邮件需要修改密码

![image-20210322170040695](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210322170040695.png)

没得说，那就改

### 实例

使用`random`来生成随机密码，包含大写字母，小写字母，数字，特殊字符的密码

首先生成一个长度为15，包含大写字母，小写字母，数字，特殊字符的密码

```python
In [1]: import random
# 首先，创建几个字符串
In [9]: a = "qwertyuiopasdfghjklzxcvbnm"

In [10]: b = a.upper()

In [11]: b
Out[11]: 'QWERTYUIOPASDFGHJKLZXCVBNM'

In [12]: c ='0123456789'

In [13]: d ='~!@#$%^&*():?'


# 创建一个列表，包含15个元素
In [14]: pw = [i for i in range(15)]

In [15]: pw
Out[15]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
  

# 随机选取字母替换列表
# 列表嵌套为新列表
In [20]: sec_list = [a,b,c,d]

In [21]: sec_list
Out[21]:
['qwertyuiopasdfghjklzxcvbnm',
 'QWERTYUIOPASDFGHJKLZXCVBNM',
 '0123456789',
 '~!@#$%^&*():?']

# 首先，从sec_list中随机选择一个列表
# 然后，从a,b,c,d中随机选择一个元素
In [31]: for i in range(len(pw)):
    ...:     pw[i] = str(random.choice(random.choice(sec_list)))
In [32]: pw
Out[32]: ['g', '6', '3', 'w', 'N', '4', 'd', '6', '9', '$', '6', '5', 'g', '1', '1']

# 但是这样潜在的可能是存在有大写字母，小写字母，特殊字符，数字缺少其中一个或者几个的状况
# 虽然概率很低
# 加一个判断条件
In [43]: judge = []
    ...: for i in pw:
    ...:     if i in a:
    ...:         judge.append('a')
    ...:     elif i in b:
    ...:         judge.append('b')
    ...:     elif i in c:
    ...:         judge.append('c')
    ...:     elif i in d:
    ...:         judge.append('d')

In [44]: judge
Out[44]: ['a', 'c', 'c', 'a', 'b', 'c', 'a', 'c', 'c', 'd', 'c', 'c', 'a', 'c', 'c']
  
# 然后我们将其转化为集合
In [45]: judge_set = set(judge)
In [46]: judge_set
Out[46]: {'a', 'b', 'c', 'd'}
  
# 判断其长度，如果不为4，则抛弃，直到等于4出现
In [47]: len(judge_set)
Out[47]: 4
  
# 然后，列表转化为字符串
In [38]: passwd = ''.join(pw)
In [39]: passwd
Out[39]: 'g63wN4d69$65g11'
```

### 整体代码

```python
import random
def get_passwd(num):
    # 设置大写字母，小写字母，数字，特殊字符
    a = 'qwertyuiopasdfghjklzxcvbnm'
    b = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    c = '0123456789'
    d = '~!@#$%^&*():?'
    # 创建一个指定长度的列表，并随机替换其中元素
    pw = [i for i in range(num)]
    sec_list = [a,b,c,d]
    for i in range(len(pw)):
        pw[i] = str(random.choice(random.choice(sec_list)))
    # 判断生成的列表中的字符都是属于什么类型
    judge = []
    for i in pw:
        if i in a:
            judge.append('a')
        elif i in b:
            judge.append('b')
        elif i in c:
            judge.append('c')
        elif i in d:
            judge.append('d')
    # 如果全部包含4种类型，则输出为字符串
    # 否则则重新开始
    if len(set(judge)) == 4:
        return ''.join(pw)
    else:
        get_passwd(num)
```

如果，密码和账号太多了

我一般会存在一个指定的文本中，然后给他上锁，下次需要的时候进行查看



### 接上

我思考了一下，这样保密性虽然很强

但是他不道德,你反正肯定记不住，我也记不住

`'g63wN4d69$65g11'`

而且你保存这个密码到文件中，再给文件加密还是弱密码

基本等于没用

那么怎么拿到一个比较好记的强密码呢

其实我觉得需要满足三个问题

1. 常用单词组合，满足记忆
2. 足够强，防止破解
3. 在不同的平台上，有不同的形式，防止厂家泄漏隐私

### 先考古

看下常用的加密模式

>  https://www.zhihu.com/search?type=content&q=加密方式

1. 凯撒密码

   你有一个字典，每次你想说的话的字母向后偏移3位，就变为了密文

   凯撒加密的缺陷是，英文字母出现是有规律的，假如我们将提取文本中出现次数最多的字符，获得其偏移量，就可以瞬间破解

2. 多表密码

   凯撒密码的进阶版

   凯撒密码是每个字母拥有固定的偏移量

   而多表密码的每个字母的偏移量是不确定的

   你有一本字典

   ​	dog表 = 第一个字母向后偏移3位，第二个字母向后偏移14位，第三个字母向后偏移6位，第四个字母向后偏移3位，第五个14位、第六个6位、第七个3位……以此类推

   这样每次都会出现不同的排列组合，打破了高频字母的出现规律

3. 一次性密匙（one time pad）

   你拥有一个密码本，上面全部都是偏移量相关

   例如：一个4长度的单词的加密 是 1334

   ​			一个10长度的单词的加密 是 9868978909

   这样就是完整的加密了，不过比较麻烦

4. 德军的恩尼格码

   三个转子

   每个转子的初始位置不同，会导致密码表完全不同，并且一个字母除了其本身之外，可以突变为任意其余字母，

   请原谅我用突变这个词

   详情可以看b站的这个视频我就不搬运了

   https://www.bilibili.com/video/BV1Rf4y1U7L1?from=search&seid=10765877265519806021

   

### 在来看看我想要加密模式

1. 他需要包含字母大小写，特殊字符，数字

   字母大小写，这个大多数人用的可能是名字，

   不过名字的排列组合也有很多种

   本命：`LiXiaoMing`

   可能：`xiaoming.li` , ` judge.Li` , `Lixm` ,` Lxm`等等

   这算我们的第一种组合

2. 第二种，数字

   数字，一串对我们有特殊意义的数字

   你不可能写` 20000614`或者`123456`。。。。太出生日期了，也太弱了

   我想到了无理数，你可以在Pi中找到任意一串数字

   一个网站：http://www.subidiom.com/pi/pi.asp

   如你所见，那么`80094756`，即为数字在`pi`中的出现位置，也可以作为数字的一部分

   ![image-20210327181717467](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210327181717467.png)
   
3. 特殊字符

   共有` . @$!%*#_~?&^`，两种模式使用
   
   - 作为分割符 xiaoming.li.80094756.anyword
   
   - 第二种模式：事实上，人民群众的创造力是无限的
   
     http://xh.5156edu.com/page/z8434m9808j20096.html
   
     你可以看到这是一种流传很久的符号表情艺术，且十分容易记忆
   
     我们可以将上述密码改为：`xiaoming.li^_^80094756@_@anyword`
   
     ```
     @_@
     疑惑、晕头转向
     o_O
     讶异
     ^_^
     高兴
     T_T
     哭得很伤心
     ```
   
4. 在平台上的特殊性，也就是在每个平台都有自己的特殊性

   如何在避免一个平台泄密之后，不会影响其余平台

   比如 美团外卖密码

   我可以改为：`xiaoming.li^_^80094756@_@anyword#MTWM`

   当然，你可以这样使用，每次更改`#MTWM`就好

   但是这样也不是很安全，一平台泄密之后，如果解密者在认真一点，那么其余平台的密码等于空文
   
   那么，你仍然可以配置相关的密码，那么我的想法就是将`MTWM`转化为一个数字，加入到前面的文本和数字中，以便造成随机性
   
   其实最简单的~~就是找到对应的`ASCII`码，相关网站：http://c.biancheng.net/c/ascii/~~
   
   **发音**，没错，发音，美：3，团：2，外：2，卖，2
   
   那么`MTWM`就可以变为`3，2，2，2`，为了保持其容易记忆的特性，我偏向于对`80094756`，此数字进行修改，而不是`xiaoming.li`，那么我们简单粗暴的来进行一下更改：`80094756 + 3222 = 800947563222 `，我这里指得是字符串意义上的相加，而不是数字相加
   
   当然你也可以数字相加：`80094756 + 3222 = 80097978`
   
   那么现在密码就变为了：`xiaoming.li^_^800947563222@_@anyword#MTWM`
   
5. 画蛇添足/画龙点睛
   
   看到了那个`anyword`吗，那是我所设置的关键词，他可以是任意的，也可以不存在，只是为了防止潜在的风险
   
   当然，你可以随意的更换位置
   

`xiaoming.li@_@anyword#MTWM^_^800947563222`

   `800947563222@_@xiaoming.li^_^anyword#MTWM`

   

### Code

现在使用python进行实现

```
In [9]: import random
   ...: name = 'li.xiaoming'
   ...: special_num = '800947563222'
   ...: face_cidt = ['^_^' , '@_@' , 'o_o' , '(+_+)?']
   ...: special_c = ['.', '@', '$', '!', '%', '*', '#', '_', '~', '?', '&', '^']
   ...:
   ...: plat_form = 'MTWM'
# random.choice为随机选择
#不需要太复杂了
#你的密码就可以为
In [11]: print(name +
    ...: 			random.choice(random.choice([face_cidt,special_c])) +
    ...: 			special_num +
    ...: 			random.choice(random.choice([face_cidt,special_c])) +
    ...: 			plat_form)
li.xiaoming!800947563222(+_+)?MTWM
```



然后，下一个问题是

### 怎么存放密码   

即便我们说了很多，就密码如何编写，但是他任然是一个20多个字母的字符串

人总是会忘掉的

当然保存密码，你可以简单的粗暴的,存为文本格式

```
账号：xiaoming
密码：800947563222@_@xiaoming.li^_^anyword#MTWM
```

但是，一般上锁的文本格式是弱密码，或者你写一个强密码来进行记忆

然后，来看另外一种存放密码的方式

隐写术：https://zh.wikipedia.org/wiki/隐写术

简单而言，将密码存放在图片中

看一个例子

![IMG_8448](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/IMG_8448.JPG)

   

   

   

   

   

   你可以下载这幅图片然后使用文本打开

​	当你使用文本编辑器打开时，拉到最下面，你会发现，是的，welcome to findkey

![image-20210327195309171](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210327195309171.png)



   

这是仿照`蝉3301`所进行的编写，有兴趣的可以看下：https://zhuanlan.zhihu.com/p/51948500

不过·这是·比较简单的存储，但是其实你用文本打开一眼就可以看到，毫无隐秘

看一个网站：http://www.jsons.cn/imghideinfo/

选择图片隐写术加密，上传图片

![image-20210327195559548](/Users/sujiaqi/Pictures/Typora/image-20210327195559548.png)

然后，输入字符串，确定密码，下载图片

![image-20210327195811183](/Users/sujiaqi/Pictures/Typora/image-20210327195811183.png)



图片：你可以再次用文本文件打开，当然没有有任何字符串显示

但是使用上述web打开后，仍然可以进行显示内容

![findkey-++](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/findkey-++.png)





### code

关于图片隐写术，有很多方式

可以看这里：https://www.zhihu.com/search?type=content&q=图片隐写术

用Python实现其中一种：数字水印，也称为盲水印/隐水印

安装包：`pip install blind-watermark`

```python
# 打入水印
from blind_watermark import WaterMark
bwm1 = WaterMark(password_wm=1, password_img=1)
# 读取原图
bwm1.read_img('logo.JPG')
# 读取水印
bwm1.read_wm('welcome to FindKey', mode = 'str')
# 打上盲水印
bwm1.embed('out.png')
```

原图：

![logo](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/logo.JPG)

生成的图片：

![out](/Users/sujiaqi/Pictures/Typora/out.png)

提取盲水印：

