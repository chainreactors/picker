---
title: IDAPython获取函数参数个数
url: http://blog.nsfocus.net/idapython/
source: 绿盟科技技术博客
date: 2022-11-08
fetch_date: 2025-10-03T21:56:28.705457
---

# IDAPython获取函数参数个数

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# IDAPython获取函数参数个数

### IDAPython获取函数参数个数

[2022-11-07](https://blog.nsfocus.net/idapython/ "IDAPython获取函数参数个数")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")

阅读： 1,703

## 一、背景介绍

起因是在IDA中快速识别静态链接的OpenSSL库函数SSL\_read、SSL\_write，有很多搞法。参看

《IoT设备逆向工程中的函数识别》
http://scz.617.cn:8/misc/201905081756.txt

就此次原始需求而言，上文中各方案显得重型。bluerust用了一种轻型方案，基于特征字符串交叉引用定位多个函数，根据函数特征过滤出最终结果，这是逆向工程常见动作。函数特征包含但不限于对指定地址的交叉引用计数，call指令计数、block计数、参数个数等等。我卡在IDAPython获取函数参数个数这个问题上。

## 二、 idaapi.decompile

uid(5162883301)、uid(3907374211)指出可以借助idaapi.decompile获取函数参数个数，uid(7483708707)在后台直接给我下列完整实现。

————————————————————————–
#
# IDASDK77\include\typeinf.hpp
#
# dos2unix CC\_Map.txt
# awk -F’ ‘ ‘{printf(“%8s : \”%s\”,\n”,tolower($3),$1);}’ CC\_Map.txt
#
CC\_Map = \
{
0x00 : “CM\_CC\_INVALID”,
0x10 : “CM\_CC\_UNKNOWN”,
0x20 : “CM\_CC\_VOIDARG”,
0x30 : “CM\_CC\_CDECL”,
0x40 : “CM\_CC\_ELLIPSIS”,
0x50 : “CM\_CC\_STDCALL”,
0x60 : “CM\_CC\_PASCAL”,
0x70 : “CM\_CC\_FASTCALL”,
0x80 : “CM\_CC\_THISCALL”,
0x90 : “CM\_CC\_MANUAL”,
0xa0 : “CM\_CC\_SPOILED”,
0xb0 : “CM\_CC\_GOLANG”,
0xc0 : “CM\_CC\_RESERVE3”,
0xd0 : “CM\_CC\_SPECIALE”,
0xe0 : “CM\_CC\_SPECIALP”,
0xf0 : “CM\_CC\_SPECIAL”
}

#
# from uid(7483708707)
#
# generate\_func\_info( idc.here() )
#
def generate\_func\_info ( ea ) :
func = idaapi.get\_func( ea )
cfunc = idaapi.decompile( func )
#
# 这两步有替代方案
#
func\_type = idaapi.tinfo\_t()
cfunc.get\_func\_type( func\_type )
#
# IDASDK77\include\typeinf.hpp
#
nargs = func\_type.get\_nargs()
arg\_list = []
for i in range( nargs ) :
arg\_list.append( str( func\_type.get\_nth\_arg(i) ) )
rettype = str( func\_type.get\_rettype() )
fi = idaapi.func\_type\_data\_t()
func\_type.get\_func\_details( fi )
func\_info = {}
func\_info[‘args’] = arg\_list
func\_info[‘ret’] = rettype
func\_info[‘cc’] = CC\_Map[fi.cc]
func\_info[‘name’] = idc.get\_func\_name( ea )
return func\_info
#
# end of generate\_func\_info
#
————————————————————————–
#
# generate\_func\_info\_1( idc.here() )
#
def generate\_func\_info\_1 ( ea ) :
func = idaapi.get\_func( ea )
cfunc = idaapi.decompile( func )
nargs = cfunc.type.get\_nargs()
arg\_list = []
for i in range( nargs ) :
arg\_list.append( str( cfunc.type.get\_nth\_arg(i) ) )
rettype = str( cfunc.type.get\_rettype() )
fi = idaapi.func\_type\_data\_t()
cfunc.type.get\_func\_details( fi )
func\_info = {}
func\_info[‘args’] = arg\_list
func\_info[‘ret’] = rettype
func\_info[‘cc’] = CC\_Map[fi.cc]
func\_info[‘name’] = idc.get\_func\_name( ea )
return func\_info
#
# end of generate\_func\_info\_1
#
————————————————————————–

bluerust指出，对idc.get\_type(idc.here())的返回值进行字符串解析也能得到一些信息，形如

‘\_\_int64 \_\_fastcall(\_\_int64, void \*, int)’

显然idaapi.decompile更优雅，此处有其详解

IDAPython CTREE
https://gist.github.com/icecr4ck/9dea9d1de052f0b2b417abf0046cc0f6

generate\_func\_info\_2与generate\_func\_info本质相同，取函数参数的办法略有不同，用到了cfunc.argidx，uid(3907374211)也提到这个点。

————————————————————————–
#
# generate\_func\_info\_2( idc.here() )
#
def generate\_func\_info\_2 ( ea ) :
func = idaapi.get\_func( ea )
cfunc = idaapi.decompile( func )
lvars = cfunc.get\_lvars()
arg\_list = []
for i in cfunc.argidx :
tinfo = lvars[i].type()
arg\_list.append( tinfo )
rettype = cfunc.type.get\_rettype()
fi = idaapi.func\_type\_data\_t()
cfunc.type.get\_func\_details( fi )
func\_info = {}
func\_info[‘args’] = arg\_list
func\_info[‘ret’] = rettype
func\_info[‘cc’] = CC\_Map[fi.cc]
func\_info[‘name’] = idc.get\_func\_name( ea )
return func\_info
#
# end of generate\_func\_info\_2
#
————————————————————————–

## 三、 FLARE IDA Decompiler Library (FIDL)

uid(5162883301)、bluerust分别提及FIDL的实现，我没用过这个IDA插件，简单测试之。

1) 安装FIDL

参看

————————————————————————–
《Portable Python》
http://scz.617.cn:8/python/202011191444.txt

《Portable IDA+IDAPython》
http://scz.617.cn:8/python/202011182246.txt

https://fidl.readthedocs.io/en/latest/installation.html
————————————————————————–

测试环境是”Portable Python + Portable IDA”，FIDL严重依赖IDA，不想安装到”Portable Python”中，只想在”Portable IDA”环境中使用FIDL。

git clone https://github.com/mandiant/FIDL.git FIDL
cd /d X:\work\FIDL
X:\temp\Python39\python.exe -m pip install .

“X:\temp\Python39″源自”X:\Green\Python\portable\Python39″，此外还复制了一份”X:\temp\Python39\_”。安装完FIDL，用BC进行目录比较，找出实际改动:

————————————————————————–
X:\temp\Python39\
share\
doc\
networkx-2.8.8\
Lib\
site-packages\
FIDL\
FIDL-1.3.dist-info\
networkx\
networkx-2.8.8.dist-info\
six-1.16.0.dist-info\
six.py
————————————————————————–

share目录下是文档，不需要；将”X:\temp\Python39\Lib\site-packages\”下的几项复制到”X:\Green\IDA\Lib\site-packages\”即可。此外，FIDL依赖bz2模块，需要复制\_bz2.pyd到IDA目录。

X:\temp\Python39\\_bz2.pyd
X:\Green\IDA\\_bz2.pyd

2) 用FIDL获取函数参数个数

在IDA的Python提示符中测试如下命令

import FIDL.decompiler\_utils as fdu
c = fdu.controlFlowinator( ea=idc.here(), fast=False )
dir(c)
c.args
len(c.args)
dir(c.args[0])
type(c.args[0].ti)
c.args[0]
c.args[0].name
c.args[0].type\_name
c.args[0].size

3) FIDL对idaapi.decompile的封装

参看

https://github.com/mandiant/FIDL/blob/master/FIDL/decompiler\_utils.py

就此次原始需求而言，主要查看这些类与函数

class controlFlowinator
def my\_decompile
def get\_function\_vars
def get\_return\_type

由于uid(7483708707)珠玉在前，很容易看懂FIDL如何封装idaapi.decompile的，但说实话，无基础时直接看FIDL实现，这些封装没那么浅显易懂。

### 参考资源

[1] Porting from IDAPython 6.x-7.3, to 7.4
https://www.hex-rays.com/products/ida/support/ida74\_idapython\_no\_bc695\_porting\_guide.shtml

IDAPython documentation
https://www.hex-rays.com/products/ida/support/idapython\_docs/

Hex-Rays Decompiler Primer
https://hex-rays.com/blog/hex-rays-decompiler-primer/

Hex-Rays SDK Reference
https://www.hex-rays.com/products/decompiler/manual/sdk/hexrays\_8hpp\_source.shtml

[2] https://gist.github.com/icecr4ck/

IDAPython cheatsheet
https://gist.github.com/icecr4ck/7a7af3277787c794c66965517199fc9c
(入门推荐阅读)

IDAPython CTREE
https://gist.github.com/icecr4ck/9dea9d1de052f0b2b417abf0046cc0f6
(详解idaapi.decompile用法)

[3] FLARE IDA Decompiler Library (FIDL)
https://fidl.readthedocs.io/en/latest/installation.html
https://fidl.readthedocs.io/en/latest/tutorial.html
https://fidl.readthedocs.io/en/latest/api.html

https://github.com/mandiant/FIDL
https://github.com/mandiant/FIDL/blob/master/FIDL/decompiler\_utils.py
(A sane API for IDA Pro’s decompiler)

[4] IDAPython: How to get function argument values – joxeankoret [2018-03-04]
https://reverseengineering.stackexchange.com/questions/17593/idapython-how-to-get-function-argument-values
print( map(hex, ida\_typeinf.get\_arg\_addrs(idc.here())))

Getting function arguments in ida – [2020-06-15]
https://reverseengineering.stackexchange.com/questions/25301/getting-function-arguments-in-ida
(解释为什么ida\_typeinf.get\_arg\_addrs不灵)

idahunt
https://github.com/nccgroup/idahunt/
https://github.com/nccgroup/idahunt/blob/master/ida\_helper.py

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担...