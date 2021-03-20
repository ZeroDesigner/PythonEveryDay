---
title: Python每日一谈｜No.19.异常
categories: Python每日一谈
---

我们在运行python程序时，经常会出现一些异常。

异常是一种跳出代码块的正常控制流来处理错误或者其它异常条件的方式.

+ 有可能是你自己写错了

+ 也有可能是程序本身无法处理

但是，活得干呀，我们现在就来看下怎么处理异常

python内部有很多异常，可以向用户直接汇报出信息

来看下python本身的异常

摘自：https://www.php.cn/python/python-exceptions.html

| 异常名称                  | 描述                                               |
| ------------------------- | -------------------------------------------------- |
|                           |                                                    |
| BaseException             | 所有异常的基类                                     |
| SystemExit                | 解释器请求退出                                     |
| KeyboardInterrupt         | 用户中断执行(通常是输入^C)                         |
| Exception                 | 常规错误的基类                                     |
| StopIteration             | 迭代器没有更多的值                                 |
| GeneratorExit             | 生成器(generator)发生异常来通知退出                |
| StandardError             | 所有的内建标准异常的基类                           |
| ArithmeticError           | 所有数值计算错误的基类                             |
| FloatingPointError        | 浮点计算错误                                       |
| OverflowError             | 数值运算超出最大限制                               |
| ZeroDivisionError         | 除(或取模)零 (所有数据类型)                        |
| AssertionError            | 断言语句失败                                       |
| AttributeError            | 对象没有这个属性                                   |
| EOFError                  | 没有内建输入,到达EOF 标记                          |
| EnvironmentError          | 操作系统错误的基类                                 |
| IOError                   | 输入/输出操作失败                                  |
| OSError                   | 操作系统错误                                       |
| WindowsError              | 系统调用失败                                       |
| ImportError               | 导入模块/对象失败                                  |
| LookupError               | 无效数据查询的基类                                 |
| IndexError                | 序列中没有此索引(index)                            |
| KeyError                  | 映射中没有这个键                                   |
| MemoryError               | 内存溢出错误(对于Python 解释器不是致命的)          |
| NameError                 | 未声明/初始化对象 (没有属性)                       |
| UnboundLocalError         | 访问未初始化的本地变量                             |
| ReferenceError            | 弱引用(Weak reference)试图访问已经垃圾回收了的对象 |
| RuntimeError              | 一般的运行时错误                                   |
| NotImplementedError       | 尚未实现的方法                                     |
| SyntaxError               | Python 语法错误                                    |
| IndentationError          | 缩进错误                                           |
| TabError                  | Tab 和空格混用                                     |
| SystemError               | 一般的解释器系统错误                               |
| TypeError                 | 对类型无效的操作                                   |
| ValueError                | 传入无效的参数                                     |
| UnicodeError              | Unicode 相关的错误                                 |
| UnicodeDecodeError        | Unicode 解码时的错误                               |
| UnicodeEncodeError        | Unicode 编码时错误                                 |
| UnicodeTranslateError     | Unicode 转换时错误                                 |
| Warning                   | 警告的基类                                         |
| DeprecationWarning        | 关于被弃用的特征的警告                             |
| FutureWarning             | 关于构造将来语义会有改变的警告                     |
| OverflowWarning           | 旧的关于自动提升为长整型(long)的警告               |
| PendingDeprecationWarning | 关于特性将会被废弃的警告                           |
| RuntimeWarning            | 可疑的运行时行为(runtime behavior)的警告           |
| SyntaxWarning             | 可疑的语法的警告                                   |
| UserWarning               | 用户代码生成的警告                                 |

我们在运行程序时，需要捕捉或者避开这些异常

就可以使用`try expect` 这个语句

一般使用情景是：

```python
try:
	判断语句或者执行语句
except 报错名称：
	报错之后的处理语句（你也可以简单打印）
else:
  如果没有的报错的话，可以在这里执行
  例如：
  print('No Bug,happy')
finally:
  扫尾语句
```

你也可以处理多个异常

```python
try:
	判断语句或者执行语句
except(Exception1[, Exception2[,...ExceptionN]]]):
	报错之后的处理语句（你也可以简单打印）
else:
  如果没有的报错的话，可以在这里执行
  例如：
  print('No Bug,happy')
finally:
  扫尾语句
```

当然，你也可以使用`expect:`来直接跳过所有异常

但是，我并不建议使用，因为这比较容易隐藏一些bug

而且你应该尽量减少`try expect` 中的代码量，毕竟，你是补货异常并处理，而不是再制造一个异常

此外还有一种格式` try  finally` 

finally 通常放在最后作为扫尾工作

在整个异常处理机制中，finally 语句的功能是：无论 try 块是否发生异常，最终都要进入 finally 语句，并执行其中的代码块。

其实try expect的最简形式为·：

```python
try:
	判断语句或者执行语句
except 报错名称：
	报错之后的处理语句（你也可以简单打印）
```



我们来看个例子

```python
In [1]: a= [1,2,3,4]

In [2]: for i in  range(0,5):
   ...:     print(a[i])
   ...:
1
2
3
4
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-2-2cb727696c4c> in <module>
      1 for i in  range(0,5):
----> 2     print(a[i])
      3

IndexError: list index out of range
```

此时报错是IndexError 

接下来，我们来捕获他

```python
In [3]: for i in  range(0,5):
   ...:     try:
   ...:         print(a[i])
   ...:     except IndexError:
   ...:         print('find index error')
   ...:
1
2
3
4
find index error
```

上面是，我们发现了一个index error ，然后捕获了他

然后我们，在加入else看下：

```python
In [4]: for i in  range(0,5):
   ...:     try:
   ...:         print(a[i])
   ...:     except IndexError:
   ...:         print('find index error')
   ...:     else:
   ...:         print('no bug,lucky')
   ...:
1
no bug,lucky
2
no bug,lucky
3
no bug,lucky
4
no bug,lucky
find index error
```

我们可以很明显的看出，程序是先执行try except,再执行else

我再加finally试一下

```python
In [9]: for i in  range(0,5):
   ...:     try:
   ...:         print(a[i])
   ...:     except IndexError:
   ...:         print('find index error')
   ...:     else:
   ...:         print('no bug,lucky')
   ...:     finally:
   ...:         print('finally')
   ...:
1
no bug,lucky
finally
2
no bug,lucky
finally
3
no bug,lucky
finally
4
no bug,lucky
finally
find index error
finally
```

我们可以看到，不管是是否出现异常总会有finally中的语句被执行

而只有不报错时，else中的语句才会被执行