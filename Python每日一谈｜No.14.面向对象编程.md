---
title: Python每日一谈｜No.14.模块(包)的使用
categories: Python每日一谈
---

本来打算写类的，但是想了下，写一个类然后打包发布，对于使用者来说难度有点大

所以我们就简单介绍一下包的使用和安装，足够大家使用就好

**python的一大优势就是有很多的第三方包**

+ 蛋白设计：PyRosetta等

+ 化学信息学：Rdkit，PyBel，ODDT等

+ 生物信息学：BioPython，Dash Bio等

+ AI：Sklearn，Tensorflow，PyTorch等

当你熟练的使用这些包的时候，就可以很方便的使用各个学科的相关知识，降低你的入门难度，

而一些，你只需要输入**`import everything`**就可以实现

![OIP.eTnkGiSxg4Ri-FmUNTGIgwHaEh](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/OIP.eTnkGiSxg4Ri-FmUNTGIgwHaEh.jpeg)

我们先来看下python自带的一些包

python内置了一些很有用的模块

几个例子，`os, sys,time`等

我们看下使用

以[os](https://www.runoob.com/python/os-file-methods.html)为例

os是`operating system`的缩写，他是python与系统进行交互的接口

我们来看几个常见的功能

```python
# 首先import
In [1]: import os
#获取当前路径
In [2]: os.getcwd()
Out[2]: '/Users/user'
#显示当前路径下的目录和文件列表
In [3]: os.listdir()
Out[3]:
['1S2d.pdb',
 'knime']
# 更改工作目录
In [5]: os.chdir('Public/')
# 如果你想看os的相关帮助的话
In [8]: help(os)
Help on module os:

NAME
    os - OS routines for NT or Posix depending on what system we're on.

MODULE REFERENCE
    https://docs.python.org/3.8/library/os

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
# 或者只是想看下os这个模块中定义过的函数或者变量
In [10]: dir(os)
Out[10]:
['CLD_CONTINUED',
 'CLD_DUMPED',
 'CLD_EXITED',
 'CLD_TRAPPED',
 'DirEntry',
 'EX_CANTCREAT',
 'EX_CONFIG',
 'EX_DATAERR',
 'EX_IOERR',
 'EX_NOHOST',
 'EX_NOINPUT',
 'EX_NOPERM',
 'EX_NOUSER',
 'EX_OK',
 'EX_OSERR',
 'EX_OSFILE',
 'EX_PROTOCOL',
 'EX_SOFTWARE',
 'EX_TEMPFAIL',
 'EX_UNAVAILABLE',
 'EX_USAGE',
 'F_LOCK',
 'F_OK',
 'F_TEST',
 'F_TLOCK',
 'F_ULOCK',
 'MutableMapping',
 'NGROUPS_MAX',
 'O_ACCMODE',
 'O_APPEND']
```








