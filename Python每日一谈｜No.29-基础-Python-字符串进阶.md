---
title: Python每日一谈｜No.29-基础-Python-字符串进阶
categories: Python每日一谈
top: true
---

字符串是最常用的数据类型

我们可以使用`‘`或者`“`来创建一个字符串

例如

```python
In [2]: a = 'hellow world'

In [4]: print(a)
hellow world
```



一般情况下我们可以使用加号进行连接

```python
In [5]: b = ' john'

In [6]: a+b
Out[6]: 'hellow world john'
```



如果我们遇见了转义字符

例如：你需要这样的字符串 `I'm liming`

你可以这样生成

```python
In [7]: a = 'I\'m liming'

In [8]: a
Out[8]: "I'm liming"
```

当然这些很容易查到，如下表，来自菜鸟教程

| 转义字符    | 描述                                                     |
| :---------- | :------------------------------------------------------- |
| \(在行尾时) | 续行符                                                   |
| \\          | 反斜杠符号                                               |
| \'          | 单引号                                                   |
| \"          | 双引号                                                   |
| \a          | 响铃                                                     |
| \b          | 退格(Backspace)                                          |
| \e          | 转义                                                     |
| \000        | 空                                                       |
| \n          | 换行                                                     |
| \v          | 纵向制表符                                               |
| \t          | 横向制表符                                               |
| \r          | 回车                                                     |
| \f          | 换页                                                     |
| \oyy        | 八进制数，y 代表 0~7 的字符，例如：\012 代表换行。       |
| \xyy        | 十六进制数，以 \x 开头，yy代表的字符，例如：\x0a代表换行 |
| \other      | 其它的字符以普通格式输出                                 |

### 字符串格式化

字符串格式化，如上文所述，共有两种形式

1. %

   ```python
   In [9]: print(' i come to %s' % ('beijing') )
    i come to beijing
   ```

​      你可以在其中添加任意的%s,来进行格式化，但是s代表的是字符串，如果是数字的话，则为

   ```
In [10]: print(' i come to %d century' % (21) )
i come to 21 century
   ```

| 符  号 | 描述                                 |
| :----- | :----------------------------------- |
| %c     | 格式化字符及其ASCII码                |
| %s     | 格式化字符串                         |
| %d     | 格式化整数                           |
| %u     | 格式化无符号整型                     |
| %o     | 格式化无符号八进制数                 |
| %x     | 格式化无符号十六进制数               |
| %X     | 格式化无符号十六进制数（大写）       |
| %f     | 格式化浮点数字，可指定小数点后的精度 |
| %e     | 用科学计数法格式化浮点数             |
| %E     | 作用同%e，用科学计数法格式化浮点数   |
| %g     | %f和%e的简写                         |
| %G     | %F 和 %E 的简写                      |
| %p     | 用十六进制数格式化变量的地址         |

2. `format`

   ```python
   In [15]: name = 'Peter'
       ...: age = 23
   
   In [16]: print('{} is {} years old'.format(name, age))
       ...:
   Peter is 23 years old
   ```

   

3. 字典

   其基本形式为

   你可以直接进行使用，只需要首先创造一个字典，然后通过`**`来进行引用

   ```python
   In [11]: str_dict = { 'name' :'xiaoming',
       ...:                'action' : 'eat',
       ...:                'food' : 'apple'
       ...:              }
       ...: command = '{name} {action} {food}'
       ...: command.format(**str_dict)
   Out[11]: 'xiaoming eat apple'
   
   ```

   

当然除了这些，还有其余许多的格式化特性，挖个坑，慢慢填