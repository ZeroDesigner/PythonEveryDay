---
title:  Python每日一谈｜No.2.IDE简介
categories: Python每日一谈
---

### 前言：

我总喜欢把已有的信息放在前面，而不是最后。一方面是因为前人的树，致敬一下；另一方面，我的教学，也是从他们当中进行学习，汇总，精炼，如果觉得我的教程比较慢的话，你也可以直接去学习。

### IDE简介：

> 集成开发环境（IDE，Integrated Development Environment ）是用于提供程序开发环境的应用程序，一般包括代码编辑器、编译器、调试器和图形用户界面工具。集成了代码编写功能、分析功能、编译功能、调试功能等一体化的开发软件服务套。所有具备这一特性的软件或者软件套（组）都可以叫集成开发环境。如微软的Visual Studio系列，Borland的C++ Builder、Delphi系列等。该程序可以独立运行，也可以和其它程序并用。IDE多被用于开发HTML应用软件。例如，许多人在设计网站时使用IDE（如HomeSite、DreamWeaver等），因为很多项任务会自动生成。微软的Visual Basic是早期的典型的可视化开发环境，后来的包括Borland公司的Delphi等。

摘自：https://www.zhihu.com/topic/20018211/intro

> Python 中IDE各凭习惯，环境以及爱好来进行使用

> 个人建议新手入坑PyCharm，虽然他慢，但是大部分图形化操作界面，容易上手，对新手很友好，当你不知道怎么配置的时候，default一般是最佳选项。社区版免费下载。

> 然后说说我的配置，我是conda，ipython，jupyter notebook三者联用。我安装的conda为miniconda不是anaconda，因为miniconda更快一点，体积更小一点，然后分别创造python2.x以及python3.x两个环境，在其中安装好ipython以及jupyter notebook进行使用。

**后续的所有程序均在IDE中运行，如果你喜欢简单那么ipython，如果你需要一些可视化比较强的那么jupyter notebook，如果你需要一套强大的工具包那么PyCharm，vscode或者conda**

### IDE安装：

1. Pycharm安装：https://zhuanlan.zhihu.com/p/51780281

   很简单的过程，不多做赘述

2. Conda安装：

   miniconda版本：https://www.jianshu.com/p/edaa744ea47d

   anaconda版本：https://blog.csdn.net/tqlisno1/article/details/108908775
   
   

### IDE使用：

基本就是Miniconda使用

```shell
查看conda版本
conda -V/--version
conda env list
#激活或推出环境
conda activate env_name
conda deactivate

#新建虚拟环境：
conda create --name py36 python=3.6

#删除环境：
conda remove -n py36 --all

#复制环境：
conda create -n newpy36 --clone py36

#列出所有包：
conda list

#安装包
conda install package_name
#package_name为包的名称

#指定安装包版本
conda install python=3.5

#安装ipython
conda install -c anaconda ipython 

#启动ipython
ipython

```

#### conda 包查询网址：https://anaconda.org/anaconda

```python
mymac:~/ $ conda activate py3                                                                                [20:21:30]
(py3) mymac:~/ $ ipython                                                                                     [20:26:57]
Python 3.7.7 (default, Mar 26 2020, 10:32:53)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: print('hellow world!')
hellow world!
```



