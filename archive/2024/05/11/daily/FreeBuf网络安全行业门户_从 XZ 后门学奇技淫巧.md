---
title: 从 XZ 后门学奇技淫巧
url: https://www.freebuf.com/articles/network/400523.html
source: FreeBuf网络安全行业门户
date: 2024-05-11
fetch_date: 2025-10-06T17:16:55.194187
---

# 从 XZ 后门学奇技淫巧

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

从 XZ 后门学奇技淫巧

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

从 XZ 后门学奇技淫巧

2024-05-10 18:14:01

**作者：Hcamael@知道创宇404实验室
原文链接：[https://paper.seebug.org/3060/](https://paper.seebug.org/3061/ "https://paper.seebug.org/3060/")**

对CVE-2024-3094漏洞的分析文章网上已经有好几篇了，这里来学习一下在该事件中后门隐藏的奇技淫巧。

# 1 技巧一之GLIBC的IFUNC特性

GLIBC 中存在一个名为IFUNC（Indirect Functions）的特性。为了理解IFUNC的功能，我们可以先看一段简单的示例代码，如下所示：

```
#include <stdio.h>
#include <stdlib.h>

void foo_1()
{
	printf("This is foo1\n");
}

void foo_2()
{
	printf("This is foo2\n");
}

typedef void (*foo_t)();

void foo() __attribute__((__ifunc__("foo_resolver")));
foo_t foo_resolver()
{
	char *path;

  printf("do foo_resolver\n");
	path = getenv("FOO");
	if (path)
		return foo_1;
	else
		return foo_2;
}

void __attribute__((constructor)) initFunc(void) {
    printf("do initFunc.\n");
}

int main(int argc, char *argv[])
{
	char *env;
	printf("Do Main Func.\n");
	env = getenv("FOO");
	if (env)
		printf("do test FOO = %s\n", env);
	foo();
	return 0;
}
```

上述代码片段首先是定义一个IFUNC特性的`foo`函数：`void foo() __attribute__((__ifunc__("foo_resolver")));`

`foo`函数执行的代码由`foo_resolver`函数决定，我们编写`foo_resolver`函数的作用是用来判断是否设置了环境变量`FOO`，如果设置了，那么`foo`函数等于`foo_1`函数，否则等于`foo_2`函数。

最后，代码还包含一个构造函数`initFunc`，用于比较构造函数和IFUNC函数执行的顺序。

接下来，我们将编译并运行上述代码，如下所示：

```
# 加上-g，方便我们后续调试
$ gcc test.c -o test -g
$ ./test
do foo_resolver
do initFunc.
Do Main Func.
This is foo2
$ FOO=1 ./test
do foo_resolver
do initFunc.
Do Main Func.
do test FOO = 1
This is foo2
```

从上面的执行结果来看，可以能发现：

* 执行顺序是`foo_resolver`-> `initFunc`-> `main`。
* `foo_resolver`函数无法获取FOO环境变量。

接着再从代码层面来看，通过`IDA`对`test`程序进行逆向分析，发现`foo`函数被放在`.got`表中，并没有发现任何调用`foo_resolver`函数的代码。说明是由glibc的ld加载时确定`foo`函数的地址，但是ld是如何知道要调用`foo_resolver`函数呢？经过研究发现：

```
$ readelf -s test |grep foo
    19: 00000000000011c3    26 FUNC    GLOBAL DEFAULT   16 foo_2
    31: 00000000000011a9    26 FUNC    GLOBAL DEFAULT   16 foo_1
    32: 00000000000011dd    71 IFUNC   GLOBAL DEFAULT   16 foo
    38: 00000000000011dd    71 FUNC    GLOBAL DEFAULT   16 foo_resolver
```

在二进制文件的符号表中，定义了`foo`函数的`IFUNC`标志位，且定义的地址为`foo_resolver`函数的地址。

从这可以推断出，glibc在处理`.got`表的地址时，如果发现`IFUNC`标志位，那么执行该函数，然后把返回值写入`.got`表中。

下一步，将对代码进行调试来确认我们的推断，调试过程如下：

```
$ gdb test
pwndbg> b foo_resolver
pwndbg> r
......
 ? 0   0x5555555551e9 foo_resolver+12
   1   0x7ffff7fd46eb _dl_relocate_object+2443
   2   0x7ffff7fd46eb _dl_relocate_object+2443
   3   0x7ffff7fd46eb _dl_relocate_object+2443
   4   0x7ffff7fe6a63 dl_main+8579
   5   0x7ffff7fe283c _dl_sysdep_start+1020
   6   0x7ffff7fe4598 _dl_start+1384
   7   0x7ffff7fe4598 _dl_start+1384
......
 RAX  0x5555555551c3 (foo_2) ?— endbr64
  ? 0x555555555223 <foo_resolver+70>             ret                                  <0x7ffff7fd46eb; _dl_relocate_object+2443>
pwndbg> x/10gx 0x3FD0 + 0x555555554000 - 0x10
0x555555557fc0 <puts@got.plt>:	0x00007ffff7e0ce50	0x00007ffff7dec6f0
0x555555557fd0 <*ABS*@got.plt>:	0x0000000000001060	0x00007ffff7db5dc0
pwndbg> b main
pwndbg> x/10gx 0x3FD0 + 0x555555554000 - 0x10
0x555555557fc0 <puts@got.plt>:	0x00007ffff7e0ce50	0x00007ffff7dec6f0
0x555555557fd0 <*ABS*@got.plt>:	0x00005555555551c3	0x00007ffff7db5dc0
```

在上面的调试内容中，我们可以得知：

* `foo_resolver`函数的调用流程大概是：`_dl_start`->`dl_main`->`_dl_relocate_object`-> `foo_resolver`。
* `*ABS*@got.plt`就是`foo`函数的got表，该got表的值在调用完`foo_resolver`函数后写入。

到这，可以解答前面的一个疑惑：由于`foo_resolver`函数在dl链接阶段被加载调用，此时环境变量尚未被GLIBC加载，因此调用`getenv`函数将返回`NULL`，导致最终返回的都是`foo_2`函数。

到此我们可以得出结论：GLIBC的IFUNC特性，可以让我们像使用构造函数(`__attribute__((constructor))`)一样，在程序的LD加载阶段时自动运行。XZ后门利用了这一特性，在liblzma.so依赖库文件被加载时，自动运行后门代码。

另外，需要注意的是，IFUNC特性在glibc 2.11.1版本以上才被支持，如需编译含有IFUNC功能的代码，需使用GCC 4.6以上的编译器，且要求GNU Binutils版本在2.20.1以上。

我们还可以写一个脚本简单的check一下所有包含IFUNC的so库：

```
#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import os
import sys
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection

def find_all_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            yield os.path.join(root, file)

def is_elf(file):
    try:
        with open(file, "rb") as f:
            data = f.read(4)
    except:
        return False
    return data == b"\x7FELF"

def get_ifunc_symbols(file_path):
    with open(file_path, 'rb') as f:
        elffile = ELFFile(f)
        ifunc_symbols = []
        for section in elffile.iter_sections():
            # 只处理符号表部分
            if isinstance(section, SymbolTableSection):
                for symbol in section.iter_symbols():
                    # 检查符号类型是否为 'STT_GNU_IFUNC'
                    if symbol['st_info']['type'] == 'STT_LOOS':
                        ifunc_symbols.append(symbol)
        return ifunc_symbols

for file in find_all_files(sys.argv[1]):
    if is_elf(file):
        symbols = get_ifunc_symbols(file)
        if symbols:
            print(f"{file} found ST_IFUNC")
        for symbol in symbols:
            print(f"Name: {symbol.name}, Address: {hex(symbol['st_value'])}")
```

使用方法如下：

```
$ python3 check.py /lib
/lib/x86_64-linux-gnu/libz.so.1.2.11 found ST_IFUNC
Name: crc32_z, Address: 0x75e0
/lib/x86_64-linux-gnu/libz.so found ST_IFUNC
Name: crc32_z, Address: 0x75e0
/lib/x86_64-linux-gnu/libmvec.so.1 found ST_IFUNC
Name: _ZGVdN8vv_atan2f, Address: 0x8450
Name: _ZGVdN4v_atan, Address: 0x6a90
Name: _ZGVbN4v_acosf, Address: 0x7e50
Name: _ZGVdN8v_sinf, Address: 0x8780
......
```

最后还需考虑一点，在上述示例中，IFUNC函数在可执行程序中执行，因此设置断点相对较容易。然而，如果需要调试so库中的IFUNC函数，可能需要采用更巧妙的方法来设置断点。

随便找了一个[示例代码](https://chromium.googlesource.com/chromium/deps/xz/%2B/dd8415469606fe7bfdc2ebc12b8457b912ede326/doc/examples/01_compress_easy.c "示例代码")，编译命令使用：`gcc test2.c -o test2 -llzma -g`。

然后使用`patchelf`工具，修改二进制程序的RPATH为`liblzma.so`的路径：`patchelf --set-rpath /home/ubuntu/xz-utils-vul/src/liblzma/.libs/ test2`。

接着写一个`.gdbinit`脚本，可以直接断到`lzma_crc64`函数：

```
$ cat .gdbinit
b _start
r
b _dl_relocate_object
c
b *0x7ffff7f84580  (自行计算lzma_crc64地址)
c
c
$ gdb test2
pwndbg> source .gdbinit
 ? 0x7ffff7f84580    endbr64
```

# 2 技巧二之利用 Radix Tree 隐藏字符

经常做逆向分析的都知道，很多时候都是通过特殊字符串来定位代码。但是在XZ事件后门文件liblzma.so中，却没有发现任何异常字符串，尽管我们了解到XZ后门是针对SSH服务的关键函数进行hook，但是在`liblzma.so`中并未包含任何`sshd`相关的字符串，这是因为XZ后门利用了`radix tree`算法。

已经有人针对该算法把`liblzma.so`中的字符串进行提取，可以参考提取出的[字符串](https://gist.github.com/q3k/af3d93b6a1f399de28fe194add452d01 "字符串")和提取字符串的[代码](https://gist.github.com/q3k/3fadc5ce7b8001d550cf553cfdc09752 "代码")。

上述代码是针对该算法的逆向过程，我学习了该算法，并用Python编写了一个正向过程的代码，如下所示：

```
#!/usr/bin/env python3
# -*- coding=utf-8 -*-

class RadixObject:
    louint64: int
    hiuint64: int
    childPtr: dict
    def __init__(self, lo: int, hi: int):
        self.louint64 = lo
        self.hiuint64 = hi
        self.endPoint = 0
        self.childPtr = {}
    # 判断char是否在当前链表中，char的范围是0-128
    def isExist(self, char: int) -> bool:
        if char < 0 or char >= 128:
            raise Exception(f"isExist: char value err, char = {char}")
        if char < 0x40:
            return (self.louint64 >> char) & 1 == 1
        else:
            char -= 0x40
            return (self.hiuint64 >> char) & 1 == 1
    def getChild(self, char: int):
        if char >= 0x40:
            char -= 0x40
        return self.childPtr[char]

class RadixTree:
    def __init__(self):
     ...