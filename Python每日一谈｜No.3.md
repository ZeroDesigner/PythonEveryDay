## Python每日一谈｜No.3 

### 开始第一个编程

当然是  输出 Hellow World

```python
print('Hellow World!')
```

有两种选项

1. 使用ipython或者jupyter notebook等，在其中直接输入此命令然后运行
2. 保存此命令为`hellow.py`文件，在命令行中输入`python hellow.py`

**Welcom to Python!**

现在你已经完成了你的第一个程序，成功的输出了`Hellow World!`在屏幕上

接下来，我们会进行进一步的学习

### Python中的注释

python可以进行单行注释，用`#`开头

也可以进行多行注释，使用三个单引号` ''' `或者三个双引号` """ `将内容涵盖在内

如下:

```python

In [84]: # 这是一个注释
    ...: print("Hello, World!")
    ...: '''
    ...: 这是多行注释，用三个单引号
    ...: 这是多行注释，用三个单引号
    ...: 这是多行注释，用三个单引号
    ...: '''
    ...: print("Hello, World!")
    ...: """
    ...: 这是多行注释，用三个双引号
    ...: 这是多行注释，用三个双引号
    ...: 这是多行注释，用三个双引号
    ...: """
    ...: print("Hello, World!")
      
Hello, World!
Hello, World!
Hello, World!
```

**我们为什么需要注释，以及该如何注释**

注释是编程能力的重要一部分，良好的注释能力意味着你有了良好的团队合作能力

想象一下，当你面对自己三年前编写的万行无注释代码时，会是什么样的感觉

但是注释也应该有一个标准，以便交流，这里推荐谷歌风格规范，不仅仅是注释，更是对其余方面也进行了阐释

```
Google 开源项目风格指南 (中文版)

在线文档托管在 ReadTheDocs : 在线阅读最新版本 [https://google-styleguide.readthedocs.io/zh_CN/latest/]
中文风格指南 GitHub 托管地址：zh-google-styleguide [https://github.com/zh-google-styleguide/zh-google-styleguide]
离线文档下载地址：release [https://github.com/zh-google-styleguide/zh-google-styleguide/releases]”

```

一个例子：

```
关于函数的几个方面应该在特定的小节中进行描述记录， 这几个方面如下文所述. 每节应该以一个标题行开始. 标题行以冒号结尾. 除标题行外, 节的其他内容应被缩进2个空格.

Args:
列出每个参数的名字, 并在名字后使用一个冒号和一个空格, 分隔对该参数的描述.如果描述太长超过了单行80字符,使用2或者4个空格的悬挂缩进(与文件其他部分保持一致). 描述应该包括所需的类型和含义. 如果一个函数接受*foo(可变长度参数列表)或者**bar (任意关键字参数), 应该详细列出*foo和**bar.

Returns: (或者 Yields: 用于生成器)
描述返回值的类型和语义. 如果函数返回None, 这一部分可以省略.

Raises:
列出与接口有关的所有异常.”

def fetch_smalltable_rows(table_handle: smalltable.Table,
                        keys: Sequence[Union[bytes, str]],
                        require_all_keys: bool = False,
) -> Mapping[bytes, Tuple[str]]:
    """
    Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        table_handle: An open smalltable.Table instance.
        keys: A sequence of strings representing the key of each table
        row to fetch.  String keys will be UTF-8 encoded.
        require_all_keys: Optional; If require_all_keys is True only
        rows with values set for all keys will be returned.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {b'Serak': ('Rigel VII', 'Preparer'),
        b'Zim': ('Irk', 'Invader'),
        b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).

    Raises:
        IOError: An error occurred accessing the smalltable.
		"""
```



### Python中的数据类型

数据类型和基本的数据结构是根本，这意味着你使用怎样的方式来存储数据

在进行实际使用时，我们使用等号（=）来进行赋值



```python
In [7]: a = 100          # 整型变量
   ...: b = 1000.0       # 浮点型变量
   ...: c = "runoob"     # 字符串

In [8]: type(a)
Out[8]: int

In [9]: type(b)
Out[9]: float

In [10]: type(c)
Out[10]: str
#当然，我们也可以更改变量类型
In [14]: d = str(a)

In [15]: type(d)
Out[15]: str
```



数据类型和基本的数据结构是根本，这意味着你使用怎样的方式来存储数据

+ 数值类型
  + 整数型(Int)：没有小数，无大小，你的电脑内存有多大，整数就可以创造多大
  + 浮点型(float)：存在小数点，可以使用普通写法`1.23,3.5,-9.1`等，也可以使用科学计数法`2.5e2,2.5**10`
  + 复数型( (complex))：我使用的比较少， 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点--摘自，菜鸟教程

+ 字符串：字符串是最常见的数字类型，`hellow world!`便是

  + 我们可以直接进行赋值：例如`a = 'u can u up'` 或者 `a = "no can no bb"`,当然你也可以使用`a = "i say 'somthing'"`，来进行表示，唯一需要注意的一点是中英文的切换。

  + 转义字符，python中的转衣字符有`\n`表示换行，`\t`表示制表符，我们最常见的用法是

    + ```python
      In [61]: print('Hellow\tWorld!\nNi\tHao.')
      Hellow	World!
      Ni	Hao.
      ```

    + 在进行使用时，如果你不想转义，则可以在，前面加`r`,如下

    + ```python
      In [62]: print(r'Hellow\tWorld!\nNi\tHao.')
      Hellow\tWorld!\nNi\tHao.
      ```
      
    + 说到这个，不得不提起PDB格式(蛋白质数据专用格式)，PDB格式ATOM共80列，每一列都需要填充，也就是，你在分割时需要按照index进行分割，而不是`\t`

  

+ 布尔值：一个布尔值只有`True`、`False`两种值，布尔值可以用`and`、`or`和`not`运算,常常用作比较，以及判断

  + ```python
    In [68]: print(8 > 7)
        ...: print(8 < 7)
    True
    False
    In [75]: a
    Out[75]: 7
    
    In [76]: a <10 and a >5
    Out[76]: True
    ```
    
    

+ 空值：`None`不能理解为`0`,`""`,`[]`，`False`，`None`是一个特殊的空值。

  + ```python
    In [65]: a = None
        ...: type(a)
    Out[65]: NoneType
    In [66]: print(a)
    None
    ```

  + 从类型层面上，`False`是布尔类型，而`None`是`class 'NoneType'`；从意义层面上，`None`表示不存在，而`False`表示真假。


> 关于数据类型与内存空间

> 在python中，如果改变变量的数值类型，那么其内存空间将会重新分配，但重新引用并不会造成内存空间的重分配
>
> 我们来看一个例子

```python
# a赋值为100
In [26]: a  = 100
  
 #查看内存地址
In [27]: id(a)
Out[27]: 4452845280
  
#查看数据类型
In [28]: type(a)
Out[28]: int

In [29]: b = a

In [30]: id(b)
Out[30]: 4452845280

In [31]: c = float(a)

In [32]: type(c)
Out[32]: float

In [33]: id(c)
Out[33]: 4485900944
  
In [52]: d = str(a)
  
In [54]: type(d)
Out[54]: str

In [53]: id(d)
Out[53]: 4485942256
  
```





