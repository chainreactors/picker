---
title: AI应用-pyinstaller反编译
url: https://saucer-man.com/information_security/1241.html
source: yanq的个人博客
date: 2025-05-25
fetch_date: 2025-10-06T22:26:43.540403
---

# AI应用-pyinstaller反编译

* [Home](https://saucer-man.com/)
* [Archives](https://saucer-man.com/archives.html)
* [About](https://saucer-man.com/about.html)
* [Github](https://github.com/saucer-man)

Previous post
Next post
Back to top
Share post

* [1. 背景](#cl-1)
* [2. pyc是什么？](#cl-2)
* [3. pyc反编译成py文件的几种方案](#cl-3)
* [4. AI实现的pyc反编译](#cl-4)

# AI应用-pyinstaller反编译

2025-05-24

1275

[信息安全](https://saucer-man.com/category/information_security/) [AI](https://saucer-man.com/category/ai/)

> 文章最后更新时间为：2025年05月24日 23:35:19

## 1. 背景

关于如何对pyinstaller编译出的exe进行反编译，很久之前写过一篇文章 [python代码打包和逆向](https://saucer-man.com/information_security/825.html)，总结来看大概是分为以下两步：

1. exe -> pyc 使用 pyinstxtractor
2. pyc -> py 使用 uncompyle6

第一步基本没太大问题，第二步由于uncompyle6的兼容性，只支持到python3.8，所以反编译的场景非常有限

本文主要是使用AI来处理 `pyc->py`的过程

## 2. pyc是什么？

***关于这个问题，AI回答的也许更好：***

`.pyc` 是 **Python Compiled** 的缩写，是 Python 将 `.py` 源代码编译成的 **字节码文件**（Bytecode），用于提升程序启动和运行的效率。

在你运行一个 `.py` 文件时，Python 会自动将其编译成字节码并保存为 `.pyc` 文件（通常保存在 `__pycache__` 文件夹中），以供下次直接使用。

`.pyc` 文件存在的意义

1. **加快启动速度**
   Python 在执行 `.py` 文件前，必须将其编译成字节码。如果存在 `.pyc` 文件并且是最新的，Python 可以直接加载，避免重复编译。
2. **缓存机制**
   Python 会自动缓存 `.py` 文件的编译结果，以节省下次运行时的处理时间。
3. **部分隐藏源代码**（虽然不是安全方式）
   发布 `.pyc` 文件而不包含 `.py` 文件，可以一定程度上避免源码泄露（但可以反编译回来）。
4. **用于发布或部署**
   一些部署场景中只需要 `.pyc` 文件，例如 `.pyc-only` 的部署模式。

## 3. pyc反编译成py文件的几种方案

* uncompyle6

这是前文介绍过的软件，项目地址为：<https://github.com/rocky/python-uncompyle6>，主要支持Python 2.7 ~ 3.8版本

* decompyle3

这是对uncompyle6的重构版本，项目地址为：<https://github.com/rocky/python-decompile3>，从github主页看支持Python 3.7 ~ 较新版本

* pycdc

使用C++ 实现的反编译器，项目地址为<https://github.com/zrax/pycdc>，其区别在于它寻求支持任何 Python 版本的字节码
（成品可使用 <https://github.com/extremecoders-re/decompyle-builds>）

## 4. AI实现的pyc反编译

上述软件对pyc文件的反编译不够稳定，原因在于.pyc 是字节码，而字节码随 Python 版本变化，每个 Python 版本的编译器会把 .py 转换为不同的 字节码（Bytecode）格式。比如某个指令（如 LOAD\_CONST, CALL\_FUNCTION）在不同版本中可能语义不同或参数格式不同。

而大模型可以通过上下文关系推测，来大致还原出源码，这其实已经足够拿到更多的信息了。

首先可以利用下面的代码来读取pyc中的函数和对应的字节码：

使用 `marshal` 和 `dis` 模块

```
import marshal, dis

with open("your_file.pyc", "rb") as f:
    f.read(16)  # 跳过 header
    code_obj = marshal.load(f)
    dis.dis(code_obj)
```

然后将字节码发送给AI来进行还原：

* system prompt

  ```
  你是一位擅长 Python 反编译的专家。
  你将收到由 dis 模块反汇编后的 Python 字节码，来源于pyc文件
  你的任务是准确还原该函数的源码，函数名称使用提供的函数名！保持格式正确，包括缩进和逻辑。
  输出时只返回直接的 Python 代码，不要添加任何说明或注释。也不用添加反引号之类的无关字符
  ```
* user prompt

  ```
  函数名称是:`_getuuid`
  请根据以下字节码还原 Python 函数源码：

  RESUME
  LOAD_CONST ''
  STORE_FAST default
  LOAD_CONST 'ABCDEF0123456789'
  STORE_FAST seed
  BUILD_LIST
  STORE_FAST sa
  LOAD_GLOBAL NULL + range
  LOAD_CONST 62
  PRECALL
  CALL
  GET_ITER
  FOR_ITER to 128
  STORE_FAST _
  LOAD_FAST sa
  LOAD_METHOD append
  LOAD_GLOBAL NULL + random
  LOAD_ATTR choice
  LOAD_FAST seed
  PRECALL
  CALL
  PRECALL
  CALL
  POP_TOP
  JUMP_BACKWARD to 44
  LOAD_CONST ''
  LOAD_METHOD join
  LOAD_FAST sa
  PRECALL
  CALL
  STORE_FAST result
  LOAD_FAST default
  LOAD_FAST result
  BINARY_OP +
  RETURN_VALUE
  ```

  ![2025-05-24T15:28:19.png](https://saucer-man.com/usr/uploads/2025/05/1838111131.png "2025-05-24T15:28:19.png")

下面将整个流程自动化即可。项目更新在旧版本的地址上：<https://github.com/saucer-man/exe2py>

1 + 9 =

 回复

快来做第一个评论的人吧~

Copyright © 2025 By [Typecho](https://www.typecho.org) & [saucerman](https://saucer-man.com)

* [Home](https://saucer-man.com/)
* [Archives](https://saucer-man.com/archives.html)
* [About](https://saucer-man.com/about.html)
* [Github](https://github.com/saucer-man)