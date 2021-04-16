---
title: Python每日一谈｜No.26.实例.7-Bioinfor.1-Blast-Python调用
categories: Python每日一谈
top: true
---

今天来看看blast

### 简介

Blast ，全称：Basic Local Alignment Search Tool，“基于局部比对算法的搜索工具”，是[生物信息学](https://baike.baidu.com/item/生物信息学/207195)常用的工具软件，可将输入的[核酸](https://baike.baidu.com/item/核酸/530683)或[蛋白质](https://baike.baidu.com/item/蛋白质/309120)序列与数据库中的已知序列进行比对，获得序列相似度等信息，从而判断序列的来源或进化关系。

目前这套软件包含五种基本功能：

- 核酸序列对核酸序列库比对（blastn）：直接将输入的核酸序列与数据库中的核酸序列进行比对。

- 核酸序列对蛋白质序列库比对（blastx）：自动将输入的核酸序列翻译为蛋白质氨基酸序列后（根据可能的读码框和编码链的差别，一段核酸序列可能翻译为六种氨基酸序列），比对数据库中的蛋白质序列。

- 蛋白质序列对蛋白质序列库比对（blastp）：直接将输入的蛋白质氨基酸序列与数据库中的氨基酸序列进行比对。

- 蛋白序列对核酸序列库比对（tblastn）：将输入的蛋白质氨基酸序列，与由核酸数据库中的序列翻译而来的潜在的蛋白质氨基酸序列进行比对。

- 核酸序列的翻译序列对核酸序列库的翻译序列的比对（tblastx）：自动将输入的核酸序列翻译为蛋白质氨基酸序列后，与由核酸数据库中的序列翻译而来的潜在的蛋白质氨基酸序列进行比对

---摘自百度百科

### 官网

online版本的我们不提，因为大家基本用的差不多，默认会用，不会使用的请百度

https://blast.ncbi.nlm.nih.gov/Blast.cgi

![image-20210324220129007](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210324220129007.png)



### 本地版blast安装

blast 目前有两个版本，我们以旧版为例，暂时不多赘述新版，理由后面你们会慢慢知道

1. blast 

   下载地址为：https://ftp.ncbi.nlm.nih.gov/blast/executables/legacy.NOTSUPPORTED/

2. blast+

   下载地址为:https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/


下载之后，解压安装

将bin文件夹添加到环境变量中，待用

![image-20210324221621883](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210324221621883.png)

### blast使用

1. 首先，我们需要建立本地版的Blast数据库

   ​	两个大类：核酸；蛋白质

   ​	其中又可以细分为很多小类

   ​	这里我们选择蛋白质类数据库

   >  **数据库介绍：**

   > Unified Protein Database（简称UniProt）是信息最丰富、资源最广的蛋白质序列数据库，整合Swiss-Prot、TrEMBL和PIR三大数据库的数据而成。

   > UniProt包含3个部分：

   > （1）UniProt Knowledgebase（UniProtKB）是蛋白质序列、功能、分类、交叉引用等信息存取中心；UniProtKB主要由两部分组成：

   > UniProtKB/Swiss-Prot:高质量的、手工注释的、非冗余的数据集；主要来自文献中的研究成果和E-value校验过计算分析结果。有质量保证的数据才被加入该数据库；

   > UniProtKB/TrEMBL：该数据集包含高质量的计算分析结果，一般都在自动注释中富集，主要应对基因组项目获得的大量数据流以人工校验在时间上和人力上的不足。注释所有可用的蛋白序列。在三大核酸数据库（EMBL-Bank/GenBank/DDBJ）中注释的编码序列都被自动翻译并加入该数据库中。它也有来自PDB数据库的序列，以及Ensembl、Refeq和CCDS基因预测的序列；

   > （2）UniProt Non-redundant Reference（UniRef）将密切相关的蛋白质序列组合到一条记录中，以便提高搜索速度。目前，根据序列相似程度形成3个子库，即UniRef100、UniRef90和UniRef50；

   > （3）UniProt Archive（UniParc）是一个综合性的非冗余数据库，包含了所有主要的、公开的数据库的蛋白质序列。由于蛋白质可能在不同的数据库中存在，并且可能在同一个数据库中有多个版本，为了去冗余，UniaraParc对每条唯一的序列只存一次，无论是否为同一物种的序列，只要序列相同就被合并为一条，每条序列提供稳定的、唯一的编号UPI。该数据库含有蛋白质的序列信息，而没有注释数据。用户可以通过文本查询数据库，可以利用BLAST程序搜索数据库，也可以直接通过FTP下载数据。
   >
   > --- 来源于 中国药科大学图书馆

   官网地址：http://www.uniprot.org/

   数据库下载地址：https://www.uniprot.org/downloads#uniprotkblink

   我们选择比较小的数据库：[Swiss-Prot](https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz)

   下载解压之后会出现：`uniprot_sprot.fasta`

   这里面就是蛋白序列：

   ```shell
   >sp|Q6GZX4|001R_FRG3G Putative transcription factor 001R OS=Frog virus 3 (isolate Goorha) OX=654924 GN=FV3-001R PE=4 SV=1
   MAFSAEDVLKEYDRRRRMEALLLSLYYPNDRKLLDYKEWSPPRVQVECPKAPVEWNNPPS
   EKGLIVGHFSGIKYKGEKAQASEVDVNKMCCWVSKFKDAMRRYQGIQTCKIPGKVLSDLD
   AKIKAYNLTVEGVEGFVRYSRVTKQHVAAFLKELRHSKQYENVNLIHYILTDKRVDIQHL
   EKDLVKDFKALVESAHRMRQGHMINVKYILYQLLKKHGHGPDGPDILTVKTGSKGVLYDD
   SFRKIYTDLGWKFTPL
   >sp|Q6GZX3|002L_FRG3G Uncharacterized protein 002L OS=Frog virus 3 (isolate Goorha) OX=654924 GN=FV3-002L PE=4 SV=1
   MSIIGATRLQNDKSDTYSAGPCYAGGCSAFTPRGTCGKDWDLGEQTCASGFCTSQPLCAR
   IKKTQVCGLRYSSKGKDPLVSAEWDSRGAPYVRCTYDADLIDTQAQVDQFVSMFGESPSL
   AERYCMRGVKNTAGELVSRVSSDADPAGGWCRKWYSAHRGPDQDAALGSFCIKNPGAADC
   ```

   

2. 接下来我们要对此数据库进行格式化

   使用 `formatdb`指令

   看下参数说明

   | 参数 | 说明                      | 值         | 默认值       | 备注                                       |
   | ---- | ------------------------- | ---------- | ------------ | ------------------------------------------ |
   | -t   | 数据库的标题【可选】      | 字符       |              |                                            |
   | -i   | 需要创建数据库的文件名    | 文件名     |              |                                            |
   | -l   | 日志文件名                | 文件名     | formatdb.log |                                            |
   | -p   | 文件数据类型              | [T/F]      | T            | T – 蛋白质F – 核苷酸                       |
   | -o   | 解析选项                  | [T/F]      | F            | T表示解析序列文件并产生索引文件，F则不解析 |
   | -a   | 数据库文件是否为ASN.1格式 | [T/F]      | F            | T为是ASN.1格式                             |
   | -b   | ASN.1的模式               | [T/F]      | F            | T为二进制，F为文本模式                     |
   | -e   | ASN.1数据库的序列数       | [T/F]      | F            | T表示数据库中只有一条序列                  |
   | -n   | 重命名数据库文件的名称    | 字符窜     |              |                                            |
   | -v   | 数据库卷的大小            | 整数       | 0            | 单位：兆字符                               |
   | -s   | 限制索引的类型            | [T/F]      | F            | T为仅用接收号创建索引                      |
   | -L   | 创建数据库别名            | 输出文件名 |              |                                            |
   | -F   | Gi列表的文件名            | 输入文件   |              | 配合-L使用                                 |
   | -B   | 生成的Gi二进制的文件名    | 输出文件   |              | 配合-F使用                                 |

   >  来源于：https://blog.csdn.net/weixin_33972649/article/details/86092026
   
   示例：
   `formatdb -i uniprot_sprot.fasta -n uniprot_sprot -t uniprot_sprot -l uniprot_sprot.log -p T`
   
   然后，当前文件夹会出现以下文件：
   
   ```
   formatdb.log         uniprot_sprot.phr  uniprot_sprot.psq
   uniprot_sprot.fasta  uniprot_sprot.pin
   ```

3. 进行比对

   使用blastall

   ```
   blastall是最常用的blast程序之一，其功能非常强大，其下面有非常多的参数，但是一般使用的参数如：-p、-i、-d、-o、-e等几个。
   
   -p: 执行的程序名称
   -d: 搜索的数据库名称
   -i : 要查询的序列文件名(Query File)
   -e:(数学)期望值(Expectation value)，E值是个统计阈值，缺省值10, 意指比对结果中由于随机偶然性产生的匹配结果不大于10,E值越小结果越可靠。
   -o :查询结果输出文件名
   -m: 比对结果显示格式选项，缺省值为0 ，即pairwise格式。另外还可以根据不同的需要选择1~6等不同的格式。
   -I :在描述行中显示gi号[T/F]，缺省值F
   -v :单行描述（one-line description）的最大数目，缺省值500
   -b :显示的比对结果的最大数目，缺省值250
   -F :对于要查询的序列做低复杂度区域(low complexity regions, LCR)的过滤[T/F]，缺省值T。对blastn用的是DUST程序，其他比对用的是SEG程序。
   所谓“低复杂度区域”是指某些或一些残基过多表现，短周期重复等。对于高等哺乳动物的基因组序列，可以先用RepeatMask程序遮蔽重复元件。在输出结果中，对LCR区的序列核酸用“N”代替，蛋白质序列用“X”代替。
   -a:运行BLAST程序所使用的处理器的数目，缺省值1
   -S:在数据库中搜索时所使用的核酸链（strand），只对blastn、blastx和tblastx有效；1表示top，2表示bottom，3表示both；缺省值3
   -T: 产生HTML格式的输出[T/F]，缺省值F
   -n: 使用MegaBlast搜索[T/F]，缺省值F
   -G: 打开一个gap的罚分（0表示使用缺省设置值），默认0
   -E: 扩展一个gap的罚分（0表示使用缺省设置值），默认0
   -q: 一个核酸碱基的错配(mismatch)的罚分（只对blastn有效），缺省值-3
   -r : 一个核酸碱基的正确匹配(match)的奖分（只对blastn有效），缺省值1
   -M: 所使用的打分矩阵，缺省值BLOSUM62
   ————————————————
   版权声明：本文为CSDN博主「gaorongchao1990626」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
   原文链接：https://blog.csdn.net/g_r_c/article/details/8477924
   ```

   实例：

   ```shell
   blastall -p blastp -i eg.fasta -d path/to/uniprot_sprot -o myresult.blastout -a 2 -F F -e 1e-10
   ```

   eg.fasta

   ```fasta
   >P51664|P53_SHEEP
   MEESQAELGVEPPLSQETFSDLWNLLPENNLLSSELSAPVDDLLPYSEDVVTWLDECPNE
   APQMPEPPAQAALAPATSWPLSSFVPSQKTYPGNYGFRLGFLHSGTAKSVTCTYSPSLNK
   LFCQLAKTCPVQLWVDSPPPPGTRVRAMAIYKKLEHMTEVVRRSPHHERSSDYSDGLAPP
   QHLIRVEGNLRAEYFDDRNTFRHSVVVPYESPEIESECTTIHYNFMCNSSCMGGMNRRPI
   LTIITLEDSRGNLLGRSSFEVRVCACPGRDRRTEEENFRKKGQSCPEPPPGSTKRALPSS
   TSSSPQQKKKPLDGEYFTLQIRGRKRFEMFRELNEALELMDAQAGREPGESRAHSSHLKS
   KKGPSPSCHKKPMLKREGPDSD
   ```

   `myresult.blastout`

   前几十行

   ```
   Reference: Altschul, Stephen F., Thomas L. Madden, Alejandro A. Schaffer,
   Jinghui Zhang, Zheng Zhang, Webb Miller, and David J. Lipman (1997),
   "Gapped BLAST and PSI-BLAST: a new generation of protein database search
   programs",  Nucleic Acids Res. 25:3389-3402.
   
   Reference for compositional score matrix adjustment: Altschul, Stephen F.,
   John C. Wootton, E. Michael Gertz, Richa Agarwala, Aleksandr Morgulis,
   Alejandro A. Schaffer, and Yi-Kuo Yu (2005) "Protein database searches
   using compositionally adjusted substitution matrices", FEBS J. 272:5101-5109.
   
   Query= P51664|P53_SHEEP
            (382 letters)
   
   Database: uniprot_sprot
              564,277 sequences; 203,340,877 total letters
   
   Searching..................................................done
   
   
   
                                                                    Score    E
                                                                                                                                     20,1           0%
   sp|P10361|P53_RAT Cellular tumor antigen p53 OS=Rattus norvegicu...   556   0.0
   sp|P02340|P53_MOUSE Cellular tumor antigen p53 OS=Mus musculus O...   553   0.0
   sp|Q64662|P53_OTOBE Cellular tumor antigen p53 (Fragment) OS=Oto...   491   e-174
   sp|P79892|P53_HORSE Cellular tumor antigen p53 (Fragment) OS=Equ...   447   e-158
   sp|Q29480|P53_EQUAS Cellular tumor antigen p53 (Fragment) OS=Equ...   352   e-121
   sp|P07193|P53_XENLA Cellular tumor antigen p53 OS=Xenopus laevis...   354   e-120
   sp|P25035|P53_ONCMY Cellular tumor antigen p53 OS=Oncorhynchus m...   352   e-118
   sp|P10360|P53_CHICK Cellular tumor antigen p53 OS=Gallus gallus ...   349   e-118
   sp|Q9W678|P53_BARBU Cellular tumor antigen p53 OS=Barbus barbus ...   348   e-117
   sp|P79734|P53_DANRE Cellular tumor antigen p53 OS=Danio rerio OX...   337   e-113
   sp|O93379|P53_ICTPU Cellular tumor antigen p53 OS=Ictalurus punc...   318   e-105
   sp|O57538|P53_XIPHE Cellular tumor antigen p53 OS=Xiphophorus he...   304   e-100
   sp|Q92143|P53_XIPMA Cellular tumor antigen p53 OS=Xiphophorus ma...   304   e-100
   sp|Q9W679|P53_TETMU Cellular tumor antigen p53 OS=Tetraodon miur...   296   3e-97
   sp|Q9JJP2|P73_MOUSE Tumor protein p73 OS=Mus musculus OX=10090 G...   288   1e-90
   sp|Q9XSK8|P73_CHLAE Tumor protein p73 OS=Chlorocebus aethiops OX...   285   2e-89
   sp|O15350|P73_HUMAN Tumor protein p73 OS=Homo sapiens OX=9606 GN...   285   2e-89
   sp|O88898|P63_MOUSE Tumor protein 63 OS=Mus musculus OX=10090 GN...   276   1e-85
   sp|Q9H3D4|P63_HUMAN Tumor protein 63 OS=Homo sapiens OX=9606 GN=...   276   1e-85
   sp|Q9JJP6|P63_RAT Tumor protein 63 OS=Rattus norvegicus OX=10116...   276   1e-85
   sp|O12946|P53_PLAFE Cellular tumor antigen p53 OS=Platichthys fl...   263   3e-84
   sp|P79820|P53_ORYLA Cellular tumor antigen p53 OS=Oryzias latipe...   248   2e-78
   sp|P84857|LEAF_CYNDA Leaf protein OS=Cynodon dactylon OX=28909 P...    33   3.7
   sp|Q6A6J8|MURB_CUTAK UDP-N-acetylenolpyruvoylglucosamine reducta...    33   4.3
   
   >sp|P51664|P53_SHEEP Cellular tumor antigen p53 OS=Ovis aries
              OX=9940 GN=TP53 PE=2 SV=1
             Length = 382
   
    Score =  789 bits (2037), Expect = 0.0,   Method: Compositional matrix adjust.
    Identities = 382/382 (100%), Positives = 382/382 (100%)
   
   Query: 1   MEESQAELGVEPPLSQETFSDLWNLLPENNLLSSELSAPVDDLLPYSEDVVTWLDECPNE 60
              MEESQAELGVEPPLSQETFSDLWNLLPENNLLSSELSAPVDDLLPYSEDVVTWLDECPNE
   Sbjct: 1   MEESQAELGVEPPLSQETFSDLWNLLPENNLLSSELSAPVDDLLPYSEDVVTWLDECPNE 60
   
   Query: 61  APQMPEPPAQAALAPATSWPLSSFVPSQKTYPGNYGFRLGFLHSGTAKSVTCTYSPSLNK 120
              APQMPEPPAQAALAPATSWPLSSFVPSQKTYPGNYGFRLGFLHSGTAKSVTCTYSPSLNK
   Sbjct: 61  APQMPEPPAQAALAPATSWPLSSFVPSQKTYPGNYGFRLGFLHSGTAKSVTCTYSPSLNK 120
   
   Query: 121 LFCQLAKTCPVQLWVDSPPPPGTRVRAMAIYKKLEHMTEVVRRSPHHERSSDYSDGLAPP 180
              LFCQLAKTCPVQLWVDSPPPPGTRVRAMAIYKKLEHMTEVVRRSPHHERSSDYSDGLAPP
   Sbjct: 121 LFCQLAKTCPVQLWVDSPPPPGTRVRAMAIYKKLEHMTEVVRRSPHHERSSDYSDGLAPP 180
   
   ```

   ##### 概念

   ```
   alignments 代表比对上的两个序列
   hits 表示两个序列比对上的片段
   Score 比对得分，分值越高，两个序列相似性越高 
   E Value 值越小，越可信，相对的一个统计值。 
   Length 输入序列的长度 
   Identities 一致性，就是两个序列有多少是一样的 
   Query 代表输入序列 
   Sbjct 代表数据库中的序列
   ```

   

### 日常强制使用python调用blast

不能跑题

看一个指令`os`

这个指令我们以前说过

```python
In [5]: import os
   ...: import time
   ...: a = time.time()
   ...: blast_path = '/path/to/blastall'
   ...: data_path = '/path/to/uniprot_sprot'
   ...: out_file = '/path/to/myresult.txt'
   ...: my_query = '/path/to/eg.fasta'
   ...: program_name = 'blastp'
   ...: print(blast_path +
   ...:       ' -p ' + program_name +
   ...:       ' -i ' + my_query +
   ...:       ' -d ' + data_path +
   ...:       ' -o  '+ out_file +
   ...:       ' -a 2 -F F -e 1e-10')
   ...: os.system(blast_path +
   ...:           ' -p ' + program_name +
   ...:           ' -i ' + my_query +
   ...:           ' -d ' + data_path +
   ...:           ' -o  '+out_file +
   ...:           ' -a 2 -F F -e 1e-10')
   ...: b = time.time()
   ...: print(b - a)
/path/to/blastall -p blastp -i ./eg.fasta -d /path/to/uniprot_sprot -o  /path/to/myresult.txt -a 2 -F F -e 1e-10
2.365309238433838

# 在这里我们需要注意下，一定要保持代码的整洁和优雅
# 否则你的代码在1个月之后，大概就成为了黑盒子
# 来看一下 

In [6]:
   ...: print(blast_path +
   ...:       ' -p ' + program_name +
   ...:       ' -i ' + my_query +
   ...:       ' -d ' + data_path +
   ...:       ' -o  '+ out_file +
   ...:       ' -a 2 -F F -e 1e-10')
      
# 我们使用这种形式来调用指令，当然他现在是清晰明了
# 但是大多数人是：

In [7]: print(blast_path + ' -p ' + program_name + ' -i ' + my_query + ' -d ' + data_path + ' -o  ' + out_file + ' -a 2 -F F -e 1e-10')
  
# 我的刀呢
# 还记得我们的geogle代码规范吗
# https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id12
# 假如你真的想这样做的话
In [2]: command = '%s -p %s -i %s -d %s -o  %s -a 2 -F F -e 1e-10'
In [5]: print(command%(blast_path, program_name, my_query, data_path, out_file))
/path/to/blastall -p blastp -i /path/to/eg.fasta -d /path/to/uniprot_sprot -o  /path/to/myresult.txt -a 2 -F F -e 1e-10

# 或许你觉得这样也是很麻烦
# 那么假如我们这样呢

In [6]: args_words = { 'blast_path' :'/path/to/blastall',
   ...:                'program_name' : 'blastp',
   ...:                'my_query' : '/path/to/eg.fasta',
   ...:                'data_path' : '/path/to/uniprot_sprot',
   ...:                'out_file' : '/path/to/myresult.txt'
   ...:              }
   ...: command = '{blast_path} -p {program_name} -i {my_query} -d {data_path} -o {out_file} -a 2 -F F -e 1e-10'
   ...: command.format(**args_words)
Out[6]: '/path/to/blastall -p blastp -i /path/to/eg.fasta -d /path/to/uniprot_sprot -o /path/to/myresult.txt -a 2 -F F -e 1e-10'
  
# 这称之为字符串的格式化
# 挖个坑，等以后有时间再说
   
```