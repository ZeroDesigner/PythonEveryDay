---
title: Python每日一谈｜No.12.列表生成式.1
categories: Python每日一谈
---

### 额

竟然就到了函数，为什么这么快，我。。。是不是落了一些hh

来看一个我经常使用的方式

**列表生成式 **

一般来说我们如果要创建一个列表的话，那么可选的方案有

1. 直接定义列表

   ```python
   In [1]: a = [1,2,3,4]
   
   In [2]: type(a)
   Out[2]: list
   ```

   

2. 将其余数据结构直接列表化

```python
In [3]: b = (1,2,3,4)

In [4]: type(b)
Out[4]: tuple

In [5]: c = list(a)

In [6]: type(c)
Out[6]: list

In [7]: print(c)
[1, 2, 3, 4]
```

3. 先创建一个空列表，然后往里面塞元素

```python
In [8]: d = []

In [9]: for i in range(0,4):
   ...:     d.append(i)
   ...:

In [10]: d
Out[10]: [0, 1, 2, 3]

In [11]: type(d)
Out[11]: list
```



但是python提供了一个更为强大的列表生成方案

他的一般形式是

```
列表 = [表达式 for i in 列表]
```

当然你也可以复杂一点

```
列表 = [表达式 for i in 列表 判断式]
```

那么我们就可以这样使用

```python
In [12]: a = [i for i in range(0,4)]

In [13]: a
Out[13]: [0, 1, 2, 3]
```

或者

```python
In [14]: a = [i**2 for i in range(0,4)]

In [15]: a
Out[15]: [0, 1, 4, 9]
```

甚至于这样

```python
In [16]: a = [i**2 for i in range(0,4) if i > 1]

In [17]: a
Out[17]: [4, 9]

  
```

