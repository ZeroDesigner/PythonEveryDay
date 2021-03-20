---
title: Python每日一谈｜No.16.错误
categories: Python每日一谈
---

在使用Python时报错是不可避免的事情

我们来看错误的产生以及分类，以及如何对其进行调试

### 错误

python有两种错误，十分容易辨别

1. 语法错误

   语法错误是因为不规范的代码引发的，例如

   ```python
   In [3]: while True print('Hello world')
     File "<ipython-input-3-2b688bc740d7>", line 1
       while True print('Hello world')
                  ^
   SyntaxError: invalid syntax
   ```

   引发错误的内容就是少加了一个`:`，关键词是这个`SyntaxError: invalid syntax`

2. 异常

   异常是python另外一个容易遇见的错误，即使你的语法是正常的，在运行期间也有可能遇到错误

   可能原因有变量未定义,int与str搞错等等

   例如

   ```python
   In [5]: a = 1
   
   In [6]: b = 2
   
   In [7]: c = 'nihao'
   
   # 打印出一个未定义的变量
   In [8]: print(d)
   ---------------------------------------------------------------------------
   NameError                                 Traceback (most recent call last)
   <ipython-input-8-85549cb1de5f> in <module>
   ----> 1 print(d)
   
   NameError: name 'd' is not defined
   
   # 整数和字符串相加
   In [9]: a + c
   ---------------------------------------------------------------------------
   TypeError                                 Traceback (most recent call last)
   <ipython-input-9-e81e582b6fa9> in <module>
   ----> 1 a + c
   
   TypeError: unsupported operand type(s) for +: 'int' and 'str'
   ```

   



