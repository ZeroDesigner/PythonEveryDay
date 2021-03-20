---
title: Python每日一谈｜No.18.序列化
categories: Python每日一谈
---

### 定义

。。。，我摘抄一个

系列化，将对象存储为二进制。

反序列化，将二进制返回为对象。

### 释义

我们再来看一个例子

```python
# 创建一个文件，模式为写入
In [1]: f = open('tmp.txt','w')
# 创建一个字符串对象
In [2]: a= '1234'
# 将a写入文件
In [3]: f.write(a)
Out[3]: 4
# 关闭文件对象
In [4]: f.close()
  
# 获取文件内容
In [5]: !cat tmp.txt
1234
```



well，我们上述操作即为创建了一个字符串a，并将字符串写入了文件`tmp.txt`中

当然，你可以认为此次操作结束了，你获得了一个含有内容的文件

但是如果我们想储存的是对象或者说为变量a怎么对待呢，如何将其储存，并在下次启动时仍然可以进行使用.

Python提供了`pickle`模块来实现序列化。

```python
# 导入模块
In [6]: import pickle
# 打开文件
In [8]: f = open('a.txt', 'wb')
# 将变量a输入到文件中
In [9]: pickle.dump(a,f)
# 关闭文件
In [10]: f.close()
```

那么我们就可以在下次启动的时候，使用反序列化获得a

```python
# 打开文件
In [11]: f = open('a.txt', 'rb')
# 反序列化
In [12]: b = pickle.load(f)
# 查看b
In [13]: b
Out[13]: '1234'
```







