---
title: Python每日一谈｜No.20.实例.1-PyMol.1-导入蛋白，创建蛋白
categories: Python每日一谈
---

已经写到20了，我知道你们也有点烦了

姑且认为以前的都会了吧

今天写PyMol

~~然后这次水一波PyMol~~

1. 安装

   + 官网：https://pymol.org/2/
   + 开源版本：https://sourceforge.net/projects/pymol/

   + 或者假设你已经安装了[conda](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

   ​        命令行安装：`conda install -c schrodinger pymol-bundle`

   

2. 使用

   当然你可以在某一环境下，直接输入pymol，打开可视化界面
   
   类似于这样
   
   当然，这并不是我们的主题
   
   ![Screen Shot 2021-03-14 at 10.43.41 AM](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/Screen%20Shot%202021-03-14%20at%2010.43.41%20AM-5689935.png)

   这次，直接打开`ipython`

   我的使用界面

   ![Screen Shot 2021-03-14 at 10.47.52 AM](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/Screen%20Shot%202021-03-14%20at%2010.47.52%20AM.png)

3. pymol 的api

   api：看下释义，懒得解释

   > API（Application Programming Interface，[应用程序接口](https://baike.baidu.com/item/应用程序接口/10418844)）是一些预先定义的接口（如函数、HTTP接口），或指[软件系统](https://baike.baidu.com/item/软件系统/224122)不同组成部分衔接的约定。 [1] 用来提供[应用程序](https://baike.baidu.com/item/应用程序)与开发人员基于某[软件](https://baike.baidu.com/item/软件)或硬件得以访问的一组[例程](https://baike.baidu.com/item/例程/2390628)，而又无需访问源码，或理解内部[工作机制](https://baike.baidu.com/item/工作机制/9905789)的细节。源于百度百科

   其实，就是pymol给我提供了一些简单的接口命令，让我们可以更加方便的使用

   首先，来获取一个蛋白

   ```python
   # 导入pymol
   In [1]: import pymol
   
   In [2]: Feature has expired.
   Feature:       PYMOL_MAIN
   Expire date:   01-nov-2020
   License path:  /Users/sujiaqi/.pymol/license.lic:
   FlexNet Licensing error:-10,32
   For further information, refer to the FlexNet Licensing documentation,
   available at "www.flexerasoftware.com".
   # 看下帮助指令
   In [14]: help(pymol)
   Help on package pymol:
   
   NAME
       pymol
   
   DESCRIPTION
       PyMOL Molecular Graphics System
       Copyright (c) Schrodinger, Inc.
   
       Supported ways to launch PyMOL:
   
         If $PYMOL_PATH is a non-default location, it must be set and exported
         before launching PyMOL.
   
         From a terminal:
   
           shell> python /path/to/pymol/__init__.py [args]
   
   # 获取蛋白3nss
   In [5]: pymol.cmd.fetch('3nss')
    PyMOL not running, entering library mode (experimental)
    ExecutiveLoad-Detail: Detected mmCIF
   Out[5]: '3nss'
   # 查看object 
   In [10]: pymol.cmd.get_object_list()
   Out[10]: ['3nss']
   # 将object保存为fasta格式
   In [23]: pymol.cmd.save('3nss.fasta','3nss',format='fasta')
   >3nss_A
   SVKLAGNSSLCPVSGWAIYSKDNSVRIGSKGDVFVIREPFISCSPLECRTFFLTQGALLNDKHSNGTIKD
   RSPYRTLMSCPIGEVPSPYNSRFESVAWSASACHDGINWLTIGISGPDNGAVAVLKYNGIITDTIKSWRN
   NILRTQESECACVNGSCFTVMTDGPSNGQASYKIFRIEKGKIVKSVEMNAPNYHYEECSCYPDSSEITCV
   CRDNWHGSNRPWVSFNQNLEYQIGYICSGIFGDNPRPNDKTGSCGPVSSNGANGVKGFSFKYGNGVWIGR
   TKSISSRNGFEMIWDPNGWTGTDNNFSIKQDIVGINEWSGYSGSFVQHPELTGLDCIRPCFWVELIRGRP
   KENTIWTSGSSISFCGVNSDTVGWSWPDGAELPFTIDK
   >3nss_B
   SVKLAGNSSLCPVSGWAIYSKDNSVRIGSKGDVFVIREPFISCSPLECRTFFLTQGALLNDKHSNGTIKD
   RSPYRTLMSCPIGEVPSPYNSRFESVAWSASACHDGINWLTIGISGPDNGAVAVLKYNGIITDTIKSWRN
   NILRTQESECACVNGSCFTVMTDGPSNGQASYKIFRIEKGKIVKSVEMNAPNYHYEECSCYPDSSEITCV
   CRDNWHGSNRPWVSFNQNLEYQIGYICSGIFGDNPRPNDKTGSCGPVSSNGANGVKGFSFKYGNGVWIGR
   TKSISSRNGFEMIWDPNGWTGTDNNFSIKQDIVGINEWSGYSGSFVQHPELTGLDCIRPCFWVELIRGRP
   KENTIWTSGSSISFCGVNSDTVGWSWPDGAELPFTIDK
   # 然后，我们看下蛋白结构
   # 两条链，有离子，有水，有配体
   # 你打开pymol就好了，命令行下，我现在没有找到一个比较好的显示蛋白信息的方法
   
   ```
   
   
   
   然后，我们再来创建一个新的蛋白，使用fab指令
   
```python
   In [8]: help(pymol.cmd.fab)
Help on function fab in module pymol.editor:
   fab(input, name=None, mode='peptide', resi=1, chain='', segi='', state=-1, dir=1, hydro=-1, ss=0, async_=0, quiet=1, _self=<module 'pymol.cmd' from '/Users/sujiaqi/miniconda3/envs/py3/lib/python3.7/site-packages/pymol/cmd.py'>, **kwargs)
 DESCRIPTION
   
        Build a peptide
    
    ARGUMENTS
    
        input = str: sequence in one-letter code
    
        name = str: name of object to create {default: }
    
        ss = int: Secondary structure 1=alpha helix, 2=antiparallel beta, 3=parallel beta, 4=flat
    
    EXAMPLE
    
        fab ACDEFGH
        fab ACDEFGH, helix, ss=1
   In [10]: pymol.cmd.fab('ACDEFGH', 'helix', ss=1)
   # 看下object列表
   In [11]:  pymol.cmd.get_object_list()
   Out[11]: ['3nss', 'helix']
   # 保存
   In [13]: pymol.cmd.save('helix.pdb','helix',format='pdb')
   # 你可以使用jupyter notebook进行查看，bio3d包
   # 也可以使用pymol直接打开进行查看
```

   ![image-20210314115756456](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210314115756456.png)

水文结束，see u.