## Python每日一谈｜No.7

### 循环

循环，是最常用的命令，和判断语句一样，一般情况下，我们将问题或者实际情况进行拆解，分类，然后使用循环以及判断来寻找潜在的解。

python的循环有两个`for`以及`while`

我们先来看`for`循环

`for`循环可以遍历字符串，列表，字典等等数据结构。

一般的情况就是：

```python
for i in a:
	print(i)
# 列表
In [1]: a = [1,2,3,4]

In [2]: for i in a:
   ...:     print(i)
   ...:
1
2
3
4
# 字符串
In [3]: a = '1,2,3,4'
In [4]: for i in a:
   ...:     print(i)
   ...:
1
,
2
,
3
,
4
# 字典
# 字典会比较复杂，你可以遍历keys，value以及（key，value）
# 我们来遍历key+value
In [6]: a = {'b':1,'c':2,'d':3}
   ...: for i in a.items():
   ...:     print(i)
   ...:
('b', 1)
('c', 2)
('d', 3)
```

或者你可以通过索引来进行遍历，最常见是遍历列表

```python
In [7]: a = [1,2,3,4]

In [8]: for i in range(len(a)):
   ...:     print(a[i])
   ...:
1
2
3
4
# 让我们来看看整个过程发生了什么
# 当然是用代码来进行表示
In [9]: a
Out[9]: [1, 2, 3, 4]
#获取列表长度
In [10]: len(a)
Out[10]: 4
#使用range函数创建一个整数列表
In [11]: range(4)
Out[11]: range(0, 4)
#使用for来遍历这个整数列表
In [12]: for i in range(4):
    ...:     print(i)
    ...:
0
1
2
3
#使用索引来遍历列表a中的所有元素
In [13]: for i in range(4):
    ...:     print(a[i])
    ...:
1
2
3
4

```

让我们再来看看`else`

else在循环中也可以使用，

