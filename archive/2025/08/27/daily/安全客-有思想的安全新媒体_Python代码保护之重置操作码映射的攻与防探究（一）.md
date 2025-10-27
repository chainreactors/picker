---
title: Python代码保护之重置操作码映射的攻与防探究（一）
url: https://www.anquanke.com/post/id/311484
source: 安全客-有思想的安全新媒体
date: 2025-08-27
fetch_date: 2025-10-07T00:17:56.696000
---

# Python代码保护之重置操作码映射的攻与防探究（一）

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Python代码保护之重置操作码映射的攻与防探究（一）

阅读量**197768**

发布时间 : 2025-08-26 10:49:47

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

> 作者：SWDD[@360SRC](https://github.com/360SRC "@360SRC")

## 前言

本文针对于Python在部署过程通过重置opcode保护的一些手法，以及逆向手法。

## Python定制化虚拟机保护原理

Python虚拟机是Python编程语言的核心组件，他负责解释和执行Python字节码，即虚拟机逐条执行字节码指令，操作栈帧中的数据。

Python编译之后的字节码储存在pyc文件中，pyc文件实际上就是PyCodeObject对象的序列化文本。

其结构体定义如下：

```
/* Bytecode object */
typedef struct {
   PyObject_HEAD
   int co_argcount;            /* Code Block的位置参数个数，比如说一个函数的位置参数个数*/
   int co_nlocals;             /* Code Block中局部变量的个数，包括其中位置参数的个数 */
   int co_stacksize;           /* 执行该段Code Block需要的栈空间 */
   int co_flags;               /* CO_..., see below */
   PyObject *co_code;          /* Code Block编译所得的字节码指令序列。以PyStingObjet的形式存在 */
   PyObject *co_consts;        /* PyTupleObject对象，保存CodeBlock中的所常量 */
   PyObject *co_names;         /* PyTupleObject对象，保存CodeBlock中的所有符号 */
   PyObject *co_varnames;      /* Code Block中的局部变量名集合 */
   PyObject *co_freevars;      /* Python实现闭包需要用的东西 */
   PyObject *co_cellvars;      /* Code Block中内部嵌套函数所引用的局部变量名集合 */
   /* The rest doesn't count for hash/cmp */
   PyObject *co_filename;      /* Code Block所对应的.py文件的完整路径 */
   PyObject *co_name;          /* Code Block的名字，通常是函数名或类名 */
   int co_firstlineno;         /* Code Block在对应的.py文件中起始行 */
   PyObject *co_lnotab;        /* 字节码指令与.py文件中source code行号的对应关系，以PyStringObject的形式存在 */
   void *co_zombieframe;     /* for optimization only (see frameobject.c) */
} PyCodeObject;
```

其中co\_code字段则为Python编译所得的字节码指令序列，反编译工作主要也是针对这个序列识别后续根据AST进行代码还原。

既然要保护co\_code，观察Python源码可以发现源码中的opcode.py文件（Python-3.8.5\Lib\opcode.py）

![]()

本opcode.py中对应的map主要用于dis模块与pip模块，因此如果需要使用pip和dis模块则需要保证源码中如下三个文件保持对应关系

\Lib\opcode.py

\Include\opcode.h

\Python\opcode\_targets.h

其中opcode\_targets.h需要保证在opcode\_targets数组中对应的位置与对应的opcode的值一致，不然会导致无法编译

这样编译出来的Python虚拟机生成的pyc文件的字节码则是重置映射之后的code直接使用反编译工具反编译则会报错

![]()

## 定制化虚拟机字节码自吐

既然对代码使用定制化的虚拟机编译成pyc文件那么该pyc文件显然无法通过正常的python虚拟机所解释执行，因此通常需要将定制化的虚拟机与产品的pyc代码一起打包发版，这意味着用户可以使用我们的Python虚拟机执行任何py代码。

上文说到既然定制化的虚拟机也需要一起交付，那么用户便可以拿定制化虚拟机执行一些“恶意”的代码。

以编译好的python\_360为例，首先我们写一个简单的python代码：

```
s = '360'
i = 10

def func():
   print ('hello 360')
   ss = 'halo 360'
   return ss
s2 = func()
print (s2)
```

使用编译好的python3.6运行：

![]()

再使用py\_compile进行编译

```
./python3.6 -m py_compile test.py
```

我们就可以获取编译好的pyc了

![]()

显然该pyc是无法使用常规的反编译工具反编译的，例如uncompyle6：

![]()

无法解析opcode问题。

但前文提到过我们可以利用该python虚拟机执行自己编写的python代码既然如此这样就出现了一个很爆炸的模块:dis模块，它可以将 Python 源代码编译后的字节码指令以可读的形式展示，帮助开发者深入理解代码的底层执行逻辑，从而优化性能或调试问题。

那我们尝试使用dis模块解析编译好的这个pyc文件。

```
import marshal
import dis

with open('__pycache__/test.cpython-36.pyc', 'rb') as f:
    f.read(12) #跳过文件信息
    code = marshal.load(f)

dis.dis(code)
```

我们得到如下输出：

![]()

反序列化解析成功了，此时其实已经可以通过AI工具还原源码了

![]()

![]()

![]()

![]()

经过对比与源码一致。

那么既然可以运行dis.dis来解析这个代码，有没有更优雅的方法呢？

我们可以通过dis中opmap字段来打印整个映射关系

```
import dis as dis
print(dis.opmap)
```

![]()

不难发现所有的字节码映射关系都直接被输出了。

## pyinstaller打包魔改后字节码，防止直接执行dis输出opcode

前文说到，如果直接使用python虚拟机加编译好的pyc交付的话，可以直接使用python执行输出字节码的代码来破解，那我们不妨思考如果使用pyinstaller这种打包工具打包字节码岂不是无法执行这个恶意代码了。

当然在打包我们的我们的elf的时候Pyinstaller会使用dis模块 位置于site-packages/PyInstaller/lib/modulegraph/util.py

原版的iterate\_instructions 可能会报错 超出限制，所以我们需要修改一下

```
import dis

def iterate_instructions(code_object):
    code_bytes = code_object.co_code
    i = 0
    n = len(code_bytes)
    EXTENDED_ARG = dis.EXTENDED_ARG

    while i < n:
        op = code_bytes[i]
        opname = dis.opname[op]
        i += 1
        arg = None
        if op >= dis.HAVE_ARGUMENT:
            arg = code_bytes[i] | (code_bytes[i+1] << 8)
            i += 2
            if op == EXTENDED_ARG:
                arg = arg << 16 | (code_bytes[i] | (code_bytes[i+1] << 8))
                i += 2

        argval = None
        # 防止 co_names 越界
        if opname in ('LOAD_NAME', 'STORE_NAME', 'DELETE_NAME',
                      'LOAD_ATTR', 'STORE_ATTR', 'DELETE_ATTR',
                      'IMPORT_NAME', 'IMPORT_FROM',
                      'LOAD_GLOBAL', 'STORE_GLOBAL', 'DELETE_GLOBAL'):
            if arg is not None and arg >= len(code_object.co_names):
                argval = "UNK_NAME_%d" % arg
            else:
                argval = code_object.co_names[arg] if arg is not None else None

        yield dis.Instruction(opname, op, arg, argval, repr(argval), i, code_bytes, code_object)
```

这样就可以愉快的打包我们的python代码了。

![]()

并且解包后的文件不存在我们的可执行python文件

![]()

此刻如果我们直接对其反编译会导致报错。

## 通过打包的opcode.pyc 取出对应的字节码

在解包的归档文件中我们其实是可以找到opcode.pyc文件的

![]()

pyc这种文件格式本身他是不带加密的，我们可以根据文首给出的数据结构来看，我们其实可以在其中找到对应的一个opcode的关系

![]()

这样就可以写一个脚本来提取了

```
py38_opcode = {'POP_TOP': 1, 'ROT_TWO': 2, 'ROT_THREE': 3, 'DUP_TOP': 4, 'DUP_TOP_TWO': 5, 'ROT_FOUR': 6, 'NOP': 9, 'UNARY_POSITIVE': 10, 'UNARY_NEGATIVE': 11, 'UNARY_NOT': 12, 'UNARY_INVERT': 15, 'BINARY_MATRIX_MULTIPLY': 16, 'INPLACE_MATRIX_MULTIPLY': 17, 'BINARY_POWER': 19, 'BINARY_MULTIPLY': 20, 'BINARY_MODULO': 22, 'BINARY_ADD': 23, 'BINARY_SUBTRACT': 24, 'BINARY_SUBSCR': 25, 'BINARY_FLOOR_DIVIDE': 26, 'BINARY_TRUE_DIVIDE': 27, 'INPLACE_FLOOR_DIVIDE': 28, 'INPLACE_TRUE_DIVIDE': 29, 'GET_AITER': 50, 'GET_ANEXT': 51, 'BEFORE_ASYNC_WITH': 52, 'BEGIN_FINALLY': 53, 'END_ASYNC_FOR': 54, 'INPLACE_ADD': 55, 'INPLACE_SUBTRACT': 56, 'INPLACE_MULTIPLY': 57, 'INPLACE_MODULO': 59, 'STORE_SUBSCR': 60, 'DELETE_SUBSCR': 61, 'BINARY_LSHIFT': 62, 'BINARY_RSHIFT': 63, 'BINARY_AND': 64, 'BINARY_XOR': 65, 'BINARY_OR': 66, 'INPLACE_POWER': 67, 'GET_ITER': 68, 'GET_YIELD_FROM_ITER': 69, 'PRINT_EXPR': 70, 'LOAD_BUILD_CLASS': 71, 'YIELD_FROM': 72, 'GET_AWAITABLE': 73, 'INPLACE_LSHIFT': 75, 'INPLACE_RSHIFT': 76, 'INPLACE_AND': 77, 'INPLACE_XOR': 78, 'INPLACE_OR': 79, 'WITH_CLEANUP_START': 81, 'WITH_CLEANUP_FINISH': 82, 'RETURN_VALUE': 83, 'IMPORT_STAR': 84, 'SETUP_ANNOTATIONS': 85, 'YIELD_VALUE': 86, 'POP_BLOCK': 87, 'END_FINALLY': 88, 'POP_EXCEPT': 89, 'STORE_NAME': 90, 'DELETE_NAME': 91, 'UNPACK_SEQUENCE': 92, 'FOR_ITER': 93, 'UNPACK_EX': 94, 'STORE_ATTR': 95, 'DELETE_ATTR': 96, 'STORE_GLOBAL': 97, 'DELETE_GLOBAL': 98, 'LOAD_CONST': 100, 'LOAD_NAME': 101, 'BUILD_TUPLE': 102, 'BUILD_LIST': 103, 'BUILD_SET': 104, 'BUILD_MAP': 105, 'LOAD_ATTR': 106, 'COMPARE_OP': 107, 'IMPORT_NAME': 108, 'IMPORT_FROM': 109, 'JUMP_FORWARD': 110, 'JUMP_IF_FALSE_OR_POP': 111, 'JUMP_IF_TRUE_OR_POP': 112, 'JUMP_ABSOLUTE': 113, 'POP_JUMP_IF_FALSE': 114, 'POP_JUMP_IF_TRUE': 115, 'LOAD_GLOBAL': 116, 'SETUP_FINALLY': 122, 'LOAD_FAST': 124, 'STORE_FAST': 125, 'DELETE_FAST': 126, 'RAISE_VARARGS': 130, 'CALL_FUNCTION': 131, 'MAKE_FUNCTION': 132, 'BUILD_SLICE': 133, 'LOAD_CLOSURE': 135, 'LOAD_DEREF': 136, 'STORE_DEREF': 137, 'DELETE_DEREF': 138, 'CALL_FUNCTION_KW': 141, 'CALL_FUNCTION_EX': 142, 'SETUP_WITH': 143, 'LIST_APPEND': 145, 'SET_ADD': 146, 'MAP_ADD': 147, 'LOAD_CLASSDEREF': 148, 'EXTENDED_ARG': 144, 'BUILD_LIST_UNPACK': 149, 'BUILD_MAP_UNPACK': 150, 'BUILD_MAP_UNPACK_WITH_CALL': 151, 'BUILD_TUPLE_UNPACK': 152, 'BUILD_SET_UNPACK': 153, 'SETUP_ASYNC_WITH': 154, 'FORMAT_VALUE': 155, 'BUILD_CONST_KEY_MAP': 156, 'BUILD_STRING': 157, 'BUILD_TUPLE_UNPACK_WITH_CALL': 158, 'LOAD_METHOD': 160, 'CALL_METHOD': 161, 'CALL_FINALLY': 162, 'POP_FINALLY': 163}

with open('./opcode.pyc','rb') as f:
    extracted = f.read()

mapping = {}
for keyword in py38_opcode:
    value = py38_opcode[keyword]
    keyword = keyword.encode()
    co_code = extracted[extracted.find(keyword)+len(keyword)+1]
    if extracted.find(keyword) != -1:
        if extracted[extracted.find(keyword)+len(keyword)] == 0xE9:
            mapping[co_code] = value
    else:
        print(keyword)

print(mapping)
```

![]()

这样就可以读取到对应的关系然后编译反编译工具来直接解...