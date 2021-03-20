---
title: Python每日一谈｜No.8
categories: Python每日一谈
---

### 循环

另外一个常用的循环语句是`while`,在`while`语句中只要满足条件，就可以一直循环

基本形式为

```
while 判断语句：
	执行语句
```

例如

```python
In [1]: a = 0
In [2]: b = 10
In [4]: while a < b :
   ...:     print(a)
   ...:     a = a + 1
   ...: print('end')
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
end

```

当然利用这个特性，你也可以使用一个死循环

```python
In [9]: a = 1

In [10]: b = 1

In [11]: while a == b:
    ...:     print(a)
1
1
1
1
1
# 此时你可以关闭终端，或者ctrl + c来进行终止
```

当然`while`也可以与`else`联用，个人理解在`while`执行完成之后，不符合判段条件时，便可以执行`else`语句

基本形式为

```python
while 判断条件:

	执行语句

else :

	执行语句
```

例如：

```python
In [12]: a = 1

In [13]: b = 3

In [14]: while a < b :
    ...:     print(a)
    ...:     a = a + 1
    ...: else:
    ...:     print('jump')
    ...:
1
2
jump
```

