## Python每日一谈｜No.7

### 循环

循环，是最常用的命令，和判断语句一样，一般情况下，我们将问题或者实际情况进行拆解，分类，然后使用循环以及判断来寻找潜在的解。

python的循环有两个`for`以及`while`

我们先来看`for`循环

for循环可以遍历字符串，列表，字典等等数据结构。

一般的情况就是：

```
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

```



