---
title: Python每日一谈｜No.15.模块(包)的安装
categories: Python每日一谈
---

上一谈中我们使用了Python自带的包进行使用来阐述

这一部分，我们来看看第三方python包，如何安装，如何使用

以BioPython为例，难度低，用途比较广

biopython网站：https://biopython.org/wiki/Documentation

### biopython简介

[Biopython是Python的最大，最受欢迎的生物信息学软件包。它包含许多用于常规生物信息学任务的不同子模块。它由Chapman和Chang开发，主要使用Python编写。它还包含C代码，以优化软件的复杂计算部分。它可以在Windows，Linux，Mac OS X等操作系统上运行。](https://www.yiibai.com/biopython/biopython_introduction.html )

### 安装

1. pip

   pip是python的包管理器

   `pip install biopython`

   你可以在这个网站上查询需要安装的python包：https://pypi.org

   如果你需要安装特定的biopython版本的话

   `pip install biopython==version`

   

2. conda

   conda是一个强大的开源的软件包管理系统和环境管理系统

   你可以在这个网站上查询需要安装的python包

   `conda install biopython`

   如果需要安装特定的版本

   `conda install biopython=version`

3. 离线安装

   以上两种都属于在线安装，也即为有网状态下

   下面来看下离线状态下如何安装python的第三方包

   首先，我们要找到软件的官网

   然后下载其文件：http://biopython.org/DIST/biopython-1.78.zip

   下载完成后，解压

   ```shell
   user:biopython-1.78/ $ ls                                         [14:17:30]
   Bio                DEPRECATED.rst     NEWS.rst           Tests
   BioSQL             Doc                PKG-INFO           biopython.egg-info
   CONTRIB.rst        LICENSE.rst        README.rst         setup.cfg
   CONTRIBUTING.rst   MANIFEST.in        Scripts            setup.py
   ```

   

     然后，我们直接运行`python setup.py install `

     就可以进行安装

### 使用

详细使用的话需要查看其原文档以及手册

http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec3

我们这里的使用以3D模块为例：http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec178

我们需要下载这个文件`1fat.cif`：http://files.rcsb.org/download/1FAT.cif

```python
# 先导入
In [4]: import Bio
  
# 查看版本
In [5]: print(Bio.__version__)
1.78
In [15]: from Bio.PDB.MMCIFParser import MMCIFParser
    ...: parser = MMCIFParser()
In [16]: structure = parser.get_structure("1fat", "1fat.cif")
  
# 我们使用biopython获取了1fat这个蛋白的结构信息
# 然后来进行一个简单的示例
In [18]: for model in structure:
    ...:     for chain in model:
    ...:         for residue in chain:
    ...:             for atom in residue:
    ...:                 print(atom)
 
...
<Atom O>
<Atom CB>
<Atom CG>
<Atom CD1>
<Atom CD2>
<Atom N>
<Atom CA>
<Atom C>
<Atom O>
<Atom N>
<Atom CA>
<Atom C>
<Atom O>
<Atom CB>
<Atom CG>
<Atom CD1>
...
```

下面是biopython中对于结构的解析

![img](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/smcra.png)



