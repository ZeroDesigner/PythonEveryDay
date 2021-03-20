---
title: Python每日一谈｜No.13.列表生成式.2
categories: Python每日一谈
---

 上篇我们说到了列表生成式

你可以很简单的通过

`a = [i for i in b]`

来搭建一个列表

**但是，问题还在于内存**，是不是有种熟悉的味道

是的，你可以在生成列表之后使用迭代器来减少内存

其实方法很简单，~~我是为了水文才拆成了两篇~~,怕你们记不住

我们只需要将`[]`修改为`()`便可以直接生成一个迭代器

我们看个例子

```python
In [3]: a = [i for i in range(0,1000)]

In [4]: type(a)
Out[4]: list

In [5]: import sys

In [6]: sys.getsizeof(a)
Out[6]: 9032

In [9]: b = (i for i in range(0,1000))

In [10]: sys.getsizeof(b)
Out[10]: 128
```



我们生成迭代器之后的使用方法和原来的一样

```python
In [12]: next(b)
Out[12]: 0

In [13]: next(b)
Out[13]: 1

In [14]: next(b)
Out[14]: 2

In [15]: next(b)
Out[15]: 3

In [16]: next(b)
Out[16]: 4

In [17]: next(b)
Out[17]: 5
```

当然，你也可以通过循环来进行调用

```python
In [20]: b = (i for i in range(0,10))

In [21]: for i in b:
    ...:     print(i)
    ...:
0
1
2
3
4
5
6
7
8
9
```

好，水文结束，大家早午晚安