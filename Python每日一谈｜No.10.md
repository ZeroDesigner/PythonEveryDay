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

4. 字符串，列表或元组对象都可用于创建迭代器

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

StopIteration:
  
 
```



In [1]: a='abcd'