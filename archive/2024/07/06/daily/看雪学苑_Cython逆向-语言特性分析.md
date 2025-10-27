---
title: Cython逆向-语言特性分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458562186&idx=1&sn=bd95ad7951c93578ed5f0cbb1971332c&chksm=b18d9e0086fa1716382e78c54135a0a296fa215688b9a741576d41897729625284287e598faf&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-06
fetch_date: 2025-10-06T17:43:42.885410
---

# Cython逆向-语言特性分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FeKI2dpuEZmzElBSWjbK2SeOibTlZdKMWJJO8UALHqXMWlcfSOeFRXQVlPseQR6ejvFoTg4NWhDgA/0?wx_fmt=jpeg)

# Cython逆向-语言特性分析

gir@ffe

看雪学苑

```
一

概述
```

##

## 1.简述

之前遇到的很多python题目逆向都是pyc的逆向比较简单，最近遇到了很多cython的题目，但是不太清楚原理做的就很难受，这里就想梳理一下cython的原理。

## 2.Cython的概述

这里引自官方文档：

Cython - an overview — Cython 3.1.0a0 documentation（https://docs.cython.org/en/latest/src/quickstart/overview.html#pyrex）

Cython是一种编程语言，可以编写 C 扩展 对于 Python 语言来说，就像 Python 本身一样简单 它旨在成为 语言的超集，赋予它高级， 面向对象、函数式和动态编程。

主要的 Python 执行环境通常称为 CPython用 C 语言编写的。其他主要实现使用 Java 和 Python 本身 。

它的主要特点 ：

1.支持可选的静态类型声明，如 语言的一部分。

2.源代码被翻译成优化的 C/C++ 代码并编译为 Python 扩展模块

3.允许程序执行速度非常快，并且与外部 C 紧密集成 库，同时保持高生产力

## 3.Cython的起源

Cython 项目最初基于著名的 [PyrexPyrex]已经通过源代码编译器解决了这个问题 将 Python 代码转换为等效的 C 代码。

特性：

1.保留了 Python 的原始界面源代码

2.可以直接从 Python 代码中使用

3.使用快速二进制模块扩展 CPython 解释器

4.将Python 代码与外部C库连接

```
二

Cython环境配置
```

与大多数 Python 软件不同，Cython 需要在系统上存在 C 编译器。

## 1.不同系统的配置

###

### （1）**Linux**

GNU C 编译器（gcc）通常存在，或通过包系统轻松获得。

在 Ubuntu 或 Debian 命令：

```
sudo apt-get install build-essential
```

###

### （2）Mac OS X

木有apple，所以自己官网看

https://developer.apple .com /

###

### 3.Windows

使用开源 MinGW（Windows 的 gcc 分发版）

## 2.安装操作

###

### （1）直接包安装

```
pip install Cython
```

###

### （2）官网下载安装最新版本

https://cython.org/

解压缩 tarball 或 zip 文件，输入目录

再运行

```
python setup.py install
```

```
pip install cython setuptools
```

#

#

```
三

语言特性分析
```

##

## 前言

###

### 1.学习

跟着无名侠仙贝学习Cython Reverse - Pandaos's blog (https://panda0s.top/2021/05/07/Cython-Reverse/#Cython-Reverse-notes)

###

### 2.编译

####

#### （1）原理

Cython 有一个个功能可以将 Python 编译成 C语言实现，再由 GCC/Clang 将 C 编译成动态库。

#### （2）build（便于对应分析）

build的源码：

```
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("hello.pyx", annotate=True)
)
```

`annotate=True`选项可以生成一个 html 页面

==显示 Py源码与生成的C代码的对应关系==

build命令：

```
python setup.py build_ext --inplace
```

成功后在当前目录下找到对应的动态库与对应的 xxx.c 源文件。

==直接用 python import 导入==

### 3.基于Hello.py 编译成的动态库分析

版本：Python 3.7.6，Cython 0.29.21

#### （1）将这个文件改为pyx后缀

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8ETI9A3HLowibJvC6rDlXpianLv361QDGqYY1ibficAkNl4gljckQ3o3nJffIcssCEy3wic0IXNUGHDJVg/640?wx_fmt=png&from=appmsg)

####

#### （2）运行前面的build命令

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8ETI9A3HLowibJvC6rDlXpianT86bL8ibKbQ6m2QGNtKEsaYPGibXHvBUnnlqwSmveEib0AxN1KibVZeXRw/640?wx_fmt=jpeg&from=appmsg)

#### （3）进入文件夹中查看便于分析的html文件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8ETI9A3HLowibJvC6rDlXpianf4d3ctOfKSaAPI9iaQlGia5nj4PD8TiaEvQUzicW6Mdm74SSRssrIWmmOA/640?wx_fmt=jpeg&from=appmsg)

#### （4）源码

```
import datetime
import math

def myfunc1():
    print("This is myfunc1.")

def test_variables():
    # 定义局部变量并打印
    x = 5
    y = "variables test."
    print(x)
    print(y)

def test_strVar():
    # 定义字符串变量并打印
    x = "Hello world."
    print(x)

def test_global_var():
    # 使用全局变量 gy 并打印
    global gy
    print(gy)

def test_cast():
    # 类型转换：将整数和字符串进行类型转换并打印
    x = int(5)
    y = str(3)
    print(x, y)

def test_numbers():
    # 打印整数、浮点数和大整数（十六进制）
    x = 123
    y = 12.3
    z = 0x112233445566778899AABBCCDD
    print(x, y, z)

def test_if(x):
    # 条件语句：判断 x 是否大于 456
    if x > 456:
        print("x > 456")
    else:
        print("x <= 456")

def test_string():
    # 字符串操作：获取长度、索引、切片，并检查子字符串
    x = "I am str."
    y = len(x)
    z = x[1]
    w = x[2:]
    print(x, y, z, w)

    if "am" in x:
        print("yes")
    else:
        print("wrong")

def test_list():
    # 列表操作：添加元素、遍历、切片和替换部分元素
    x = list()
    x.append(1)
    x.append(2)
    x.append(3)
    x.append(4)
    x.append("five")
    print(x)
    print(len(x))
    for i in x:
        print(i)
    x = x[1:]
    x[2:4] = [22, 33]

def test_dict():
    # 字典操作：添加键值对、访问值、检查键和遍历字典
    x = {}
    x["one"] = 1
    x["two"] = 2
    x["three"] = 3
    y = x["one"]
    z = x["two"]
    if "one" in x:
        print(y)

    for k in x:
        print(k, x[k])

def test_for():
    # for 循环：计算 0 到 100 的和
    s = 0
    for i in range(101):
        s = s + i
    print(s)

def test_while():
    # while 循环：计算 1 到 100 的和
    s = 0
    i = 1
    while i <= 100:
        s = s + i
        i += 1
    print(s)

def test_exception():
    # 异常处理：尝试执行错误操作并捕获异常
    x = 1
    try:
        x = x + "1"
        print(x)
    except NameError:
        print("Variable x is not defined")
    except:
        print("Something else went wrong")

def test_datetime():
    # 获取并打印当前日期和时间
    x = datetime.datetime.now()
    print(x)

def test_format():
    # 字符串格式化：使用 % 操作符进行字符串格式化
    x = 1
    y = "One"
    z = "%s is %d" % (y, x)
    print(z)

def test_math():
    # 数学函数：使用 ceil 和 floor 函数
    x = math.ceil(1.4)
    y = math.floor(1.4)
    print(x) # 返回 2
    print(y) # 返回 1

def test_arg(x, y, z):
    # 传递参数：修改参数并打印
    x = x + 1
    y = y + "2"
    z = z[:]
    print(x, y, z)

class test_class:
    # 定义一个类及其方法
    def __init__(self):
        self.aa = 1

    def test_class_hh(self):
        print(self.aa)

# 定义全局变量并调用所有函数
gy = 123
myfunc1()
test_variables()
test_strVar()
test_global_var()
test_cast()
test_numbers()
test_string()
test_list()
test_dict()
test_for()
test_while()
test_exception()
test_datetime()
test_format()
test_math()
test_arg(1, "2", [4, 5, 6])
```

##

## \_\_pyx\_string\_tab

### 1.概述

在pyx文件编译为.c的文件时，\_\_pyx\_string\_tab是一个包含代码中所有需要使用的字符串（避免重复创建相同的字符串，从而优化字符串的使用和查找）。

###

### 2.查看源码

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8ETI9A3HLowibJvC6rDlXpianpaUCAPbDr9oPLY7Oruic9L1SWZzianlpH09Tc8dsiaekHjRwUgHxIvloA/640?wx_fmt=jpeg&from=appmsg)

```
static int __Pyx_CreateStringTabAndInitStrings(void) {
  __Pyx_StringTabEntry __pyx_string_tab[] = {
    {&__pyx_kp_s_1, __pyx_k_1, sizeof(__pyx_k_1), 0, 0, 1, 0},
    {&__pyx_kp_s_2, __pyx_k_2, sizeof(__pyx_k_2), 0, 0, 1, 0},
    {&__pyx_kp_s_Hello_world, __pyx_k_Hello_world, sizeof(__pyx_k_Hello_world), 0, 0, 1, 0},
    {&__pyx_kp_s_I_am_str, __pyx_k_I_am_str, sizeof(__pyx_k_I_am_str), 0, 0, 1, 0},
    {&__pyx_n_s_NameError, __pyx_k_NameError, sizeof(__pyx_k_NameError), 0, 0, 1, 1},
    {&__pyx_n_s_One, __pyx_k_One, sizeof(__pyx_k_One), 0, 0, 1, 1},
    {&__pyx_kp_s_Something_else_went_wrong, __pyx_k_Something_else_went_wrong, sizeof(__pyx_k_Something_else_went_wrong), 0, 0, 1, 0},
    {&__pyx_kp_s_This_is_myfunc1, __pyx_k_This_is_myfunc1, sizeof(__pyx_k_This_is_myfunc1), 0, 0, 1, 0},
    {&__pyx_kp_s_Variable_x_is_not_defined, __pyx_k_Variable_x_is_not_defined, sizeof(__pyx_k_Variable_x_is_not_defined), 0, 0, 1, 0},
    {&__pyx_n_s__10, __pyx_k__10, sizeof(__pyx_k__10), 0, 0, 1, 1},
    {&__pyx_n_s__38, __pyx_k__38, sizeof(__pyx_k__38), 0, 0, 1, 1},
    {&__pyx_n_s_aa, __pyx_k_aa, sizeof(__pyx_k_aa), 0, 0, 1, 1},
    {&__pyx_n_s_am, __pyx_k_am, sizeof(__pyx_k_am), 0, 0, 1, 1},
    {&__pyx_n_s_asyncio_coroutines, __pyx_k_asyncio_coroutines, sizeof(__pyx_k_asyncio_coroutines), 0, 0, 1, 1},
    {&__pyx_n_s_ceil, __pyx_k_ceil, sizeof(__pyx_k_ceil), 0, 0, 1, 1},
    {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
    {&__pyx_n_s_datetime, __pyx_k_datetime, sizeof(__pyx_k_datetime), 0, 0, 1, 1},
    {&__pyx_n_s_dict, __pyx_k_dict, sizeof(__pyx_k_dict), 0, 0, 1, 1},
    {&__pyx_n_s_doc, __pyx_k_doc, sizeof(__pyx_k_doc), 0, 0, 1, 1},
    {&__pyx_n_s_five, __pyx_k_five, sizeof(__pyx_k_five), 0, 0, 1, 1},
    {&__pyx_n_s_floor, __pyx_k_floor, sizeof(__pyx_k_floor), 0, 0, 1, 1},
    {&__pyx_n_s_gy, __pyx_k_gy, sizeof(__pyx_k_gy), 0, 0, 1, 1},
    {&__pyx_n_s_hello, __pyx_k_hello, sizeof(__pyx_k_hello), 0, 0, 1, 1},
    {&__pyx_kp_s_hello_pyx, __pyx_k_hello_pyx, sizeof(__pyx_k_hello_pyx), 0, 0, 1, 0},
    {&__pyx_n_s_i, __pyx_k_i, sizeof(__pyx_k_i), 0, 0, 1, 1},
    {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
    {&__pyx_n_s_init, __pyx_k_init, sizeof(__pyx_k_init), 0, 0, 1, 1},
    {&__pyx_n_s_init_subclass, __pyx_k_init_subclass, sizeof(__pyx_k_init_sub...