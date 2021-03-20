---
title: Python每日一谈｜No.6
categories: Python每日一谈
---

### 条件控制

简单说下就是`if`判断

![cainiaojiaocheng1](https://i.loli.net/2021/02/25/EHfGhODU4zk9mqx.jpg)





简单来说下基本形式就是：

```python
if 条件一：
	执行动作一
elif 条件二：
	执行动作二：
else 条件三：
	执行动作三
```

如果你只需要判断一种条件那么：

```python
if 条件一：
	执行动作一
```

甚至不需要else

需要注意的是  `if`判断条件后面需要加`：`

`if`常和`while`以及`for`联用

 

### 实例：

```python
# 从一个列表中用判断某个数字是否存在
a = [1,2]
if 1 in a:
	print('1 in a')
	
# 判断一个列表中特定数字是否存在
# 创建一个列表，包含`1,2,3,4`四个元素
a = [1,2,3,4]
# 遍历列表
for i in a:
#判断列表元素是否等于1
	if i == 1:
		print('1 in a')
#判断列表元素是否等于2	
	elif 1 < i <  3:
		print('2 in a')
#如果列表元素既不等于1也不等于2
	else:
		print('this >= 3')
	
```

当然列表也可以嵌套，这取决你的解决问题的复杂程度

**你当然可以按照下述操作进行使用**

**但是需要注意**

**当你的问题达到一个很复杂的程度的时候，使用嵌套方式会加大你的记忆程度，以及程序的使用难度以及设计难度**

**而且会使问题的解决方式实际上变得更为复杂，这取决于你的记忆以及编码水平**

**同时在这里你应该注意缩进符对python的影响，只要有一个缩进有问题，此程序便不可运行**



```python
In [13]: a = [1,2,3,4,5,6,7,8,9]
    ...:
    ...: for i in a:
    ...:	if 1<i<4:
    ...:		if i == 1:
    ...:			print('this is 1 and this < 4')
    ...:		elif i == 2:
    ...:			print('this is 2 and this < 4')
    ...:	if i > 4:
    ...:		if i == 5:
    ...:			print('this is 5 and this > 4')
    ...:		elif i == 6:
    ...:			print('this is 6 and this > 4')
    ...:		else:
    ...:			print('this is others')
    
this is 2 and this < 4
this is 5 and this > 4
this is 6 and this > 4
this is others
this is others
this is others
```



`if`中常用的一些判断符号

| 判断符 | 描述                     |
| :----- | :----------------------- |
| `<`    | 小于                     |
| `<=`   | 小于或等于               |
| `>`    | 大于                     |
| `>=`   | 大于或等于               |
| `==`   | 等于，比较两个值是否相等 |
| `!=`   | 不等于                   |

