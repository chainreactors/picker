---
title: Python逆向总结
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458564526&idx=2&sn=277d972105dc7d7333bc81399e02afb2&chksm=b18d872486fa0e32d30db777b9a1ad68118a62ca5628e106e691f91ad2db34e25cc0a3f07001&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-20
fetch_date: 2025-10-06T17:43:14.474617
---

# Python逆向总结

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Fic0jo2Hu76p5858SiceSyULrhWoVw3FcHElDvnl22OjRvl7El3Dll5IyXgNYCrxauCliaBbLR4FTWQ/0?wx_fmt=jpeg)

# Python逆向总结

祝今朝

看雪学苑

讲述一下常见的python题型

```
一

第一种：直接反编译型
```

除了直接获得题目内容的python文件外，出题人也可以稍微加工一点点，给出题目python文件所对应的pyc文件，即python的字节码。

**PYC 文件的定义**

pyc 文件是 python 在编译过程中出现的主要中间过程文件。pyc 文件是二进制的，类似 java 的字节码，可以由 python 虚拟机直接执行的。

这个时候我们一般使用uncompyle6（适用于python3.8)或者Pycdc将pyc文件反编译成py文件。

### Uncompyle6下载以及使用：https://github.com/rocky/python-uncompyle6

命令：

`pip install uncompyle6`

安装完成后可以使用

`uncompyle6 --version`

查看是否安装成功，若成功显示版本号，则安装成功

（注意：下载的uncompyle6的版本最好别高于所使用的python版本）

使用命令：

`uncompyle6`-o output\_file.py your\_file.pyc

-o 目标生成的Python文件名 原pyc文件名

### pycdc下载以及使用：

https://github.com/extremecoders-re/decompyle-builds

pycdc -o output\_file.py your\_file.pyc

当然也可以使用一些在线网站将Pyc文件转换为python文件。

```
二

第二种:打包成exe的py文件
```

一般来说py文件打包生成的exe的图标是：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGicLUQf9oqsibCjVc5BdhCDbuCqepvWMdBfmwE6fmfsbiaGwI5ZQXdxXn2Q/640?wx_fmt=other&from=appmsg)

并且如果直接使用IDA打开会有很多包含python的字样。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGicbLZWlsicQ708fTchibpcZiahBhN8uIFaNelqt7icJSiau6HsU2kaicAuTkjg/640?wx_fmt=other&from=appmsg)

然后即可以判断是Py文件打包而成的exe。

这个时候我们需要使用Pyinstxtractor工具将exe文件进行解包。

`pyinstxtractor.py` 工具的下载地址：https://sourceforge.net/projects/pyinstallerextractor/将上面下载好的pyinstxtractor文件复制到题目所在目录下，然后直接在打包的exe的路径下打开终端。

使用命令：pythonpyinstxtractor.py待解包的文件名.exe：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGicB2loiaFZ2luUy1XLd8Zoia7xWl4Uhs1rZc741SAMLSHDWaKp1V2xzWQw/640?wx_fmt=other&from=appmsg)

然后获得生成的解包后的文件夹。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGicFAiaKLby7iac6TGnbuJF7WlEgibGFwhYkFwj4GCPicZToxJ1cFaqd4RBfg/640?wx_fmt=other&from=appmsg)

打开extracted文件夹：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGicolEFZzSrNNOcEXLw6SMuGibOlhVXFJSZNKEF7saBWGpepv4wZSkHerA/640?wx_fmt=other&from=appmsg)

一般来说我们会获得一个和我们解包的exe同名的pyc文件，这个时候就和第一种类型题目一样，将pyc文件还原成py文件进行逆向即可。

但是有特殊情况，因为使用Pyinstxtractor进行解包以后源文件一般不会包含原始的魔术数字和时间戳，在反编译的时候就可能会出错，如下图查看login.pyc。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGicmpYibInl7KShBa1DicnjVgcksVaY3psTmickUic6WVJ8Mte4eGJKBlJiciaw/640?wx_fmt=webp&from=appmsg)

而解包后的`struct.pyc`文件会保留其原始的 Python`.pyc`文件的魔数和时间戳信息。

所以我们通常使用strcut.pyc中的信息对原来的Pyc进行补全。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGicMpXJtx0xZJDOkOib5WpbydI4zCwxCEJwjhPCUqcb6TicGbJdmic8zYibTQ/640?wx_fmt=other&from=appmsg)

将E3前的数字复制粘贴到test.pyc的前面即可。

然后保存即可正常得到Py文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGicFLiaiaOqf0dnfmDvfn1CHGVAE4mLMnuMvfInIvpicRKDibE4TEiakyqIwsA/640?wx_fmt=other&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGicNTky0Ws9T050YrvpKujLiaLaufbeDWczezr9JAh8hhUjtUXPsGY0NnQ/640?wx_fmt=other&from=appmsg)

```
三

第三种： 给pyc字节码（类汇编形式）
```

如果出题人给的题目形式如下，那么我们应该怎么操作呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGic5eSKf4EDz5iaNGKPxM40aKKsxKXey4fK6fKhictoWFQicCKqyh8uvqARA/640?wx_fmt=other&from=appmsg)

###

### 前述：

####

#### 1.dis库：

用于反汇编 Python 字节码。它可以将 Python 函数或代码对象的字节码指令序列转换成我们的可读形式，显示每个字节码指令的操作码和操作数。

`dis.dis`函数的作用：

◆接受一个 Python 函数对象或者代码对象作为参数。

◆将这个函数或代码对象的字节码指令序列反汇编成易于理解的格式。

◆显示每个字节码指令的操作码（opcode）和操作数（operand），以及相应的行号和位置信息。

例如，对于一个简单的 Python 函数：

```
def add_numbers(a, b):
    return a + b
```

使用`dis.dis`来查看其字节码：

import dis

dis.dis(add\_numbers)

输出结果：

0 LOAD\_FAST                0 (a)

2 LOAD\_FAST                1 (b)

4 BINARY\_ADD

6 RETURN\_VALUE

#### 2.marshal:

Python 标准库中的一个模块，提供了对 Python 对象进行序列化（转换为字节流）和反序列化（从字节流恢复为对象）功能。

## 不同python版本的pyc文件头

python2的pyc文件的前4个字节是一个固定的魔数（03 F3 0D 0A），而紧接着的后 4 个字节表示编译这个 `.pyc` 文件的 Python 解释器的版本号。

python3的pyc文件前4个字节是固定的魔数 （33 0D 0D 0A），然后是两个字节的时间戳，标识了 `.py` 文件的最后修改时间， 接着是 4 个字节的源文件大小，最后是源文件名的字符串，以 null 字节结尾。

注意：Python3的pyc文件头部并非固定的 16 个字节，而是一个不确定的长度，至少是 12 个字节，加上源文件名字符串的长度。

## 怎么获取pyc字节码

在交互模式下：

```
import dis,marshal
#导入 Python 的两个标准库模块 dis 和 marshal。dis 用于反汇编字节码，marshal 用于序列化和反序列化对象
f=open("Pz.pyc","rb").read()
#以二进制只读模式打开文件 Pz.pyc
f
#将读取的字节流内容存储在变量 f 中
code=marshal.loads(f[8:])
#跳过文件头部分将字节码加载到code中
code
#查看
dis.dis(code)
```

#反汇编字节码

最后获得输出（可以理解为python的汇编）。

最后不理解的可以对照官方文档搜索去还原字节码的含义

32.12. dis — Disassembler for Python bytecode — Python 2.7.18 documentation

这里贴几个常见的含义：

LOAD\_CONST ：加载const 变量，比如数值，字符串等等， 一般用于传递给函数作为参数。

LOAD\_FAST ：一般用于加载局部变量的值，也就是读取值，用于计算或者函数调用传传等。

STORE\_FAST ：一般用于保存值到局部变量。

CALL\_FUNCTION：`CALL_FUNCTION n`，其中`n`表示函数调用时传递的参数数量。表示在此处调用了一个函数，并且传递了n个参数。

```
四

第四种：加花的pyc
```

这里需要了解一下pyc的文件结构。

pyc文件分为**pyc文件头部分**和**PyCodeObject部分。**

文件头部分即为上文中谈到的魔数时间戳部分，而PyCodeObject是在CPython（Python 的官方解释器实现）中用来表示编译后的代码对象的结构体。实际上，pyc 文件就是 PyCodeObject 对象在硬盘上的保存形式。

## 不同版本的python的魔数头

## **PyObject\_HEAD**

不同的 Python 版本会有不同的 PyObject\_HEAD：

| Python 版本 | 十六进制文件头 |
| --- | --- |
| Python 2.7 | 03f30d0a00000000 |
| Python 3.0 | 3b0c0d0a00000000 |
| Python 3.1 | 4f0c0d0a00000000 |
| Python 3.2 | 6c0c0d0a00000000 |
| Python 3.3 | 9e0c0d0a0000000000000000 |
| Python 3.4 | ee0c0d0a0000000000000000 |
| Python 3.5 | 170d0d0a0000000000000000 |
| Python 3.6 | 330d0d0a0000000000000000 |
| Python 3.7 | 420d0d0a000000000000000000000000 |
| Python 3.8 | 55 0d 0d 0a 00 00 00 00 00 00 00 00 00 00 00 00 |
| Python 3.9 | 610d0d0a000000000000000000000000 |
| Python 3.10 | 6f0d0d0a000000000000000000000000 |
| Python 3.11 | a70d0d0a000000000000000000000000 |

## PyCodeObject 的结构如下：

typedef struct {

PyObject\_HEAD

int co\_argcount;        /\* 位置参数个数 \*/

int co\_nlocals;         /\* 局部变量个数 \*/

int co\_stacksize;       /\* 栈大小 \*/

int co\_flags;

PyObject*co\_code;      /*字节码指令序列 \*/

PyObject*co\_consts;    /*所有常量集合 \*/

PyObject*co\_names;     /*所有符号名称集合 \*/

PyObject*co\_varnames;  /*局部变量名称集合 \*/

PyObject*co\_freevars;  /*闭包用的的变量名集合 \*/

PyObject*co\_cellvars;  /*内部嵌套函数引用的变量名集合 \*/

/\* The rest doesn’t count for hash/cmp \*/

PyObject*co\_filename;  /*代码所在文件名 \*/

PyObject*co\_name;      /*模块名|函数名|类名 \*/

int co\_firstlineno;     /\* 代码块在文件中的起始行号 \*/

PyObject*co\_lnotab;    /*字节码指令和行号的对应关系 \*/

void*co\_zombieframe;   /*for optimization only (see frameobject.c) \*/

} PyCodeObject;

而在PyCodeObject中有一个部分我们在做逆向题目时需要尤其注意，那就是

PyObject*co\_code;      /*字节码指令序列 \*/

数值代表了Pyc字节码的指令的字节数。

如果我们对Pyc里面的指令进行了删减，那么在删减过后我们需要对PyObject \*co\_code数值也进行修改，将数值修改为删减后的字节数。

查看指令数的参考命令：

len(code.co\_code)其中第一个code为你装载字节码所命名的变量。

例如下图我们可以看到删改前指令长度是27。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGic0wxlksg976tyFY61JVUniauPyobT7Jv2egYsM4wIkvvhccJ5J0npPgQ/640?wx_fmt=webp&from=appmsg)

在读取的字节码中，看到偏移量是12和15的地方。在12处我们可以看到指令会让我们跳转到偏移为18的位置。而在15处LOAD\_CONST 255表示从常量表中加载索引为 255 的常量，并将其推入栈顶。

但此处很显然我们没有那么多的常量。所以可以判断这个地方是一个花指令。和c汇编花指令的思路差不多，我们需要将12和15处给直接去掉（类比c去花的nop）。

所以我们选择将该pyc文件使用010Editor打开后搜索对应的十六进制数据来定位指令所在。

例如搜索官方文档发现JUMP\_ABSOLUTE的操作码对应的十六级进制是0x71,所以从0x71往下的三个字节即为偏移量12处的指令。

而LOAD\_CONST的操作码对应的十六进制是0x64。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGicgshIlrncYiaQy7gBXvjlP7u0wUdJZSClIuszA7Lk4AhWTqPyordN5JA/640?wx_fmt=other&from=appmsg)

所以我们只需要将从71开始的往后6个字节全部删除然后再修改PyObject \*co\_code的值即可。

通过最初查看我们得知PyObject \*co\_code的值是27，十六进制为1B。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGicuXbUG2u1twNc5jmJ1noPpztTNWWdCibCr2dgwDAsQGVXqsGBKwvuIpA/640?wx_fmt=other&from=appmsg)

然后我们减去了六个字节，所以我们需要将27改为21（0x15）。

修改完成后：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGicHMActsS0lBouJLpBHnt4XbgyKO5Vic5kbOe0NJ0ibqgEk3iaXbgB5f20w/640?wx_fmt=other&from=appmsg)

最后即可以正确使用uncompyle6得到对应python源码。

内容参考大佬视频【Python逆向】浅谈CTF-Python逆向（https://www.bilibili.com/video/BV1JL4y1p7Tt/?spm\_id\_from=333.880.my\_history.page.click&vd\_source=d7f903c8e55e49011126ea9ac27a3d31）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fic0jo2Hu76p5858SiceSyULEe7aibYggnwmzmVic0tJicKDjNnlqgZ0vKC8QDJgZp50OEXzWSDuAXFSA/640?wx_fmt=png...