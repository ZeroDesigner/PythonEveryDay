---
title: Python每日一谈｜No.27.实例.8-Bioinfor.2-Psipred-蛋白质二级结构预测
categories: Python每日一谈
top: true
---



### 蛋白质二级结构预测

这里我应该和Rosetta还有I-Tasser进行一个联动.

毕竟某些时候，好的二级结构预测可以影响蛋白质三级结构预测,我们来看经典的

> web:http://bioinf.cs.ucl.ac.uk/psipred/

> Paper:https://pubmed.ncbi.nlm.nih.gov/10493868/

> Download:http://bioinf.cs.ucl.ac.uk/software_downloads/

来看下准确率：PSI-PRED的预测准确率可达75％。

### 使用步骤

online版本的话大家自己无脑式提交就好

我们来看下本地版本

1. 下载：http://bioinfadmin.cs.ucl.ac.uk/downloads/psipred/

   直接下载最新版本psipred.4.02就阿訇

   ![image-20210325204436052](https://gitee.com/luskyqi/markdown-png/raw/master/uPic/image-20210325204436052.png)

2. 解压

   这个用的指令就是

   `tar -zxvf  psipred.4.02.tar.gz`

3. 随后，我们进入到解压之后的文件夹中

   ```shell
   [psipred]$ ls
   BLAST+   README   bin   example     runpsipred_single
   LICENSE  VERSION  data  runpsipred  src
   ```

4. 万事先看Readme

   ```shell
   [cryoem@IMCAS psipred]$ cat README
   PSIPRED RELEASE NOTES
   =====================
   
   PSIPRED Version 4.01
   
   By David Jones, October 2016
   
   *** IMPORTANT *****************************************************
   NCBI are now trying to move users to the new BLAST+ package. Please
   see the README file in the BLAST+ subdirectory for more information
   on PSIPRED's support for BLAST+. For now the preferred option is
   to stick with the classic BLAST package as the default. If the tar
   or rpm file you are downloading from NCBI has "+" in the filename,
   then you are downloading BLAST+ rather than BLAST.
   *******************************************************************
   
   Here are some very brief notes on using the PSIPRED V4 software.
   
   PSIPRED is supplied in source code form - it must be compiled before
   it can be used. The code should compile on any ANSI C compiler e.g.
   the GNU C compiler.
   
   Please see the LICENSE file for the license terms for the software.
   Basically it's free to anyone (including commercial users) as long as
   you don't want to sell the software or, for example, store the results
   obtained with it in a database and then try to sell the database.
   If you do wish to sell the software or use it in a commercial product,
   then please contact UCL Business (http://www.uclb.com).
   
   PSIPRED is run via a tcsh shell script called "runpsipred" - this is a
   very simple script which you should be able to convert to Perl or whatever
   scripting language you like.
   
   If your sequence does not have any homologues in the current data banks,
   then it is possible to run PSIPRED on a single sequence. In this case,
   PSIPRED is run via a tcsh shell script called "runpsipred_single". Unfortunately,
   like every other secondary structure prediction method, PSIPRED does not
   perform as well on single sequences. Any secondary structure prediction based on
   a single sequence should be considered as unreliable.
   
   Before running PSIPRED, please check the runpsipred and runpsipred_single scripts
   to see if the path variables are set to wherever you have installed the
   program and data files. The default is to assume that the program is
   installed in the current directory - this is probably NOT what you want!
   
   INSTALLATION
   ============
   
   Firstly compile the software:
   
   tcsh% cd to-wherever-you-untarred-PSIPRED
   
   tcsh% cd src
   
   tcsh% make
   
   tcsh% make install
   
   The executables will be placed in the PSIPRED bin directory.
   
   You must also install the PSI-BLAST and Impala software from the
   NCBI toolkit, and also install appropriate sequence data banks.
   
   The NCBI toolkit can be obtained from URL ftp://ftp.ncbi.nih.gov
   
   PSI-BLAST executables can be obtained from ftp://ftp.ncbi.nih.gov/blast
   
   
   EXAMPLE USAGE
   =============
   
   In this example the target sequence is called "example.fasta":
   
   tcsh% runpsipred example.fasta
   
   Running PSI-BLAST with sequence example.fasta ...
   Predicting secondary structure...
   Pass1 ...
   Pass2 ...
   Cleaning up ...
   Final output file: example.horiz
   Finished.
   
   That's it - you can then look at the output:
   
   tcsh% more example.horiz
   
   
   SPECIAL OPTIONS
   ===============
   
   The psipass2 program has several special options which you can use if you wish.
   
   For example, the default command is as follows:
   
   psipass2 weights_p2.dat 1 1.0 1.0 output.ss2 input.ss > output.horiz
   
   Arguments 2,3 & 4 are as follows:
   
   Argument 2: No of filter iterations
   This controls the amount of "smoothing" that is carried out on the final
   prediction. The recommended setting is 1, but it may be worth trying
   higher values to increase the level of smoothing.
   
   Argument 3&4: Helix/Strand Decision constants
   These options control the bias for helix (Arg3) and strand (Arg4) predictions.
   The default values are equal to 1.0, but if you know your protein is, for
   example, mostly comprised of beta strands then you can increase the bias
   towards beta strand prediction. For example:
   
   psipass2 weights_p2.dat 1 1.0 1.3 output.ss2 input.ss > output.horiz
   
   increases the bias towards beta strand prediction by approximately 30%.
   
   
   
   SEQUENCE DATA BANK
   ==================
   
   As of PSIPRED V4.0 onwards, we no longer believe it is necessary for the sequence
   data banks used with PSI-BLAST to be filtered to remove low-complexity regions,
   transmembrane regions, and coiled-coil segments. The search data bank can
   therefore be any large non-redundant protein sequence data bank, with
   UNIREF90 (http://www.uniprot.org/help/uniref) being the recommended one.
   
   
   
   CHANGES FROM THE ORIGINAL PSIPRED
   =================================
   
   The following is a quick summary of the main changes since the original
   PSIPRED.
   
   1. The program now makes use of PSI-BLAST binary checkpoint files (using the
   Impala program makemat) to reduce loss of precision when parsing the original
   ASCII position specific matrices.
   
   2. By default the 1st pass uses an average of 3 different neural network
   weight sets - this improves prediction accuracy slightly.
   
   3. In addition to the normal horizontal summary output format, the program
   now also produces a full table of results which shows the individual
   coil, helix, strand network outputs.
   
   4. A one-line header is output at the start of the output files to allow
   THREADER (and other programs) to automatically recognise a PSIPRED
   prediction.
   
   5. An experimental interface to BLAST+ has been added (V3.0). This will extract
   PSSM data directly from ASN.1 checkpoint files.
   
   6. Minor formatting bugs in .horiz file output for very long sequences
   have now been fixed (V3.21).
   
   7. Minor output bug loses singleton residue coil predictions fixed (V3.3)
   
   8. V4.0 released: new neural network architectures.
   ```

6. 主要安装指令

   ```shell
   tcsh% cd to-wherever-you-untarred-PSIPRED
   
   tcsh% cd src
   
   tcsh% make
   
   tcsh% make install
   ```

   

7. 运行

   看下官方案例

   ```shell
   In this example the target sequence is called "example.fasta":
   
   tcsh% runpsipred example.fasta
   
   Running PSI-BLAST with sequence example.fasta ...
   Predicting secondary structure...
   Pass1 ...
   Pass2 ...
   Cleaning up ...
   Final output file: example.horiz
   Finished.
   
   That's it - you can then look at the output:
   
   tcsh% more example.horiz
   ```

8. 修改runpsipred

   我们需要修改的

   set dbname = uniref90

   uniref90

   例如

   set dbname = 

   set dbname = /home/to/uniprot_sprot

   改为昨天设置的blast 对比蛋白序列库名，绝对路径

   set ncbidir = /usr/local/bin

   修改为昨天设置的blast路径

   ```shell
   #!/bin/tcsh
   
   # This is a simple script which will carry out all of the basic steps
   # required to make a PSIPRED prediction. Note that it assumes that the
   # following programs are in the appropriate directories:
   # blastpgp - PSIBLAST executable (from NCBI toolkit)
   # makemat - IMPALA utility (from NCBI toolkit)
   # psipred - PSIPRED V4 program
   # psipass2 - PSIPRED V4 program
   
   # NOTE: Script modified to be more cluster friendly (DTJ April 2008)
   
   # The name of the BLAST data bank
   set dbname = uniref90
   
   # Where the NCBI programs have been installed
   set ncbidir = /usr/local/bin
   
   # Where the PSIPRED V4 programs have been installed
   set execdir = ./bin
   
   # Where the PSIPRED V4 data files have been installed
   set datadir = ./data
   
   set basename = $1:r
   set rootname = $basename:t
   
   # Generate a "unique" temporary filename root
   set hostid = `hostid`
   set tmproot = psitmp$$$hostid
   ```

   

