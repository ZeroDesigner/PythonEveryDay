---
title: Python每日一谈｜No.36.实例.16.Colab-一个免费的深度学习开发环境(免费使用GPU和TPU)
categories: Python每日一谈
top: true
---



[TOC]

# Colab-一个免费的深度学习开发环境(免费使用GPU和TPU)

## 简介

工欲善其事，必先利其器。

对于国内，我是不指望他们可以出什么免费的CPU，GPU算力来做公益。

但是总得学习吧，就找到了Colab，免费提供GPU算力以供学习。

唉，现在的显卡都去用于挖矿了，等一波矿难。

Colab由Geogle开发，当然我这里不教翻墙，你可以自己去学习，网上教程不少。

## 使用

1. 打开网页

   网站：https://colab.research.google.com/
   
   ![image-20210417233551942](/Users/sujiaqi/Pictures/Typora/image-20210417233551942.png)

2. 你可以点击cancel，来看看colab教学

   ![image-20210417233731086](/Users/sujiaqi/Pictures/Typora/image-20210417233731086.png)

3. 你也可以直接新建notebook

   或者从左上角File中进行新建notebook

   <img src="/Users/sujiaqi/Pictures/Typora/image-20210417233835879.png" alt="image-20210417233835879" style="zoom:50%;" />

4. 使用

   colab你可以直接作为jupyter notenook 使用

   简单方便

   我们现在看下如何设置GPU或TPU

   Edit -- > Notebook Settings

   ![image-20210417234114641](/Users/sujiaqi/Pictures/Typora/image-20210417234114641.png)

   然后在硬件加速这边，选择使用GPU或者CPU

   ![image-20210417234232371](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210417234232371.png)

   

5. 查看安装包

   我安装了一些包，但是忘掉了colab是否自带一些包

   反正都是可以直接安装的

   运行即可

   ![image-20210417234440816](/Users/sujiaqi/Pictures/Typora/image-20210417234440816.png)

6. 内存和运存

   在右上角

   <img src="/Users/sujiaqi/Pictures/Typora/image-20210417235158356.png" alt="image-20210417235158356"  />

   

7. 一个例子

   ![image-20210418000430239](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210418000430239.png)
   
   ![image-20210418000949324](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210418000949324.png)
   
   
   
 8. 注意

    截止到目前为止，你已经拿到了一个TPU用于计算

    当然你可以设置为GPU

    但是你必须需要注意其运算时间有限制，挂载只有12个小时，也就是12小时之后，就需要重现挂载一次

    当然，你可以保存check point



