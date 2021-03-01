## Python每日一谈｜No.10.迭代器

### 迭代器

迭代器呢，是一种**对象**。。。。

> 我如何和你们解释**对象**这个比较抽象的词呢（在某些同学仍然单身的情况下hhh）

> 言归正传，编程可以分为两类，面向过程的编程，以及面向对象的编程

> 我们写的一般普通的脚本是面向过程的，因为，处理问题比较简单，应用情景比较单一

> 但是如果对于比较复杂的操作一般会使用面向对象的编程

> 当然，你也可以记住一句话

> **万物皆对象**



为了更细致的了解,迭代器，我们先来给他下定义

1. 迭代器是可迭代的对象

2. 迭代器只能往前不会后退。

3. 迭代器有两个基本的方法：**iter()** 和 **next()**

4. 字符串，列表，元组，字典对象都可用于创建迭代器

简而言之，一个字符串，列表或元组被迭代化后，他就变成了一个迭代器类似的存在，迭代器可以进行迭代，且只能向前不能向后

我们看个例子

```python
In [1]: a='abcd'

In [10]: type(b)
Out[10]: str_iterator

In [5]: next(b)
Out[5]: 'a'

In [6]: next(b)
Out[6]: 'b'

In [7]: next(b)
Out[7]: 'c'

In [8]: next(b)
Out[8]: 'd'

In [9]: next(b)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-9-adb3e17b0219> in <module>
----> 1 next(b)

# 当然列表，元祖也基本一致
In [11]: a = [1,2,3,4]

In [12]: b = iter(a)

In [13]: print(b)
<list_iterator object at 0x7fc9b8337ed0>

In [14]: next(b)
Out[14]: 1

In [15]: next(b)
Out[15]: 2

In [16]: next(b)
Out[16]: 3

In [17]: next(b)
Out[17]: 4

In [18]: next(b)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-18-adb3e17b0219> in <module>
----> 1 next(b)

#当然，如果是字典的话
In [19]: a={'b':1,'c':2}

In [20]: iter(a)
Out[20]: <dict_keyiterator at 0x7fc9b8331170>

In [21]: d = iter(a)

In [22]: next(d)
Out[22]: 'b'

In [23]: next(d)
Out[23]: 'c'

In [24]: next(d)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-24-9b2daf1403f5> in <module>
----> 1 next(d)

StopIteration:
 
```



那其实现在，我们就有一个问题，为什么要用迭代器呢？

话说直接使用`for`，`while`循环遍历他不香吗？

一方面，同学们要了解，迭代的思想和精髓呀，这个你们高中老师就教过了，我就不教了，我们下一谈来直接写一个看看。

第二方面，迭代器所占的内存更小，我们看个例子

```python
In [33]: import sys

In [34]: a = [1,2,3,4,5]

In [35]:  print(sys.getsizeof(a))
112

In [36]: b = iter(a)

In [37]: print(sys.getsizeof(b))
64

#这里我们使用两种方式创建了a，这个列表，一种是正常方式
#一种是正常方式，在正常方式下，a所占的内存为112字节
#一种是迭代器方式，a所占的内存的为64字节

```

所以，**迭代器比较香是因为它占据的内存比较小**

