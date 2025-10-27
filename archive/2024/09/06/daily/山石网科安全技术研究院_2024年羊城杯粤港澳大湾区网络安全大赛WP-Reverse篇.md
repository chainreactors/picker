---
title: 2024年羊城杯粤港澳大湾区网络安全大赛WP-Reverse篇
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247508141&idx=1&sn=a1a77850ae2e404e982affed0995f4b8&chksm=fa527513cd25fc05fe3b66db8f77d678c69b40bac8d5a58fae06ce7399b0b2816af1c037141a&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-09-06
fetch_date: 2025-10-06T18:27:50.554701
---

# 2024年羊城杯粤港澳大湾区网络安全大赛WP-Reverse篇

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnT5iadVicAO65Y9ZR5iaKQA0IBdI2qP7NBq8u1M007WUpy6cLowr4LlozBKFnTszCatiaHmrfHiaQREBJQ/0?wx_fmt=jpeg)

# 2024年羊城杯粤港澳大湾区网络安全大赛WP-Reverse篇

原创

NEURON

山石网科安全技术研究院

## chal（赛后出flag的零解题）

cython的逆向万变不离其宗，用[Cython 二进制库逆向分析全面指南](https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247507102&idx=1&sn=5b38235bb8f8bb1dd5b4e2e0325f3f48&scene=21#wechat_redirect)里的方法能逆出个大概。赛后又去再看了一下，（以为只是用来防多解的）`self._tips`才发现它才是真正的check。真正的密文竟然不是已知数组，而是……

先看题目给的main.py的调用，是直接用`chal.chal(flag)`对flag进行检查：

```
import chal

flag = input("flag: ")
chal.chal(flag)
```

然后看一下chal的各属性：

```
>>> import chal
>>> dir(chal)
['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__test__', 'chal', 'os', 'random']
>>> dir(chal.chal)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_p1', '_p2', '_p3']
>>> chal.chal._p1
<cyfunction chal._p1 at 0x4000fa0450>
>>> chal.chal._p2
<cyfunction chal._p2 at 0x4000fa0520>
>>> chal.chal._p3
<cyfunction chal._p3 at 0x4000fa05f0>
>>> dir(chal.chal("a"))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_p1', '_p2', '_p3', '_tips', '_var1', '_var2', '_var3']
>>> chal.chal("a")._tips
"Don't peek!!!"
>>> chal.chal("a")._var1
'a'
>>> chal.chal("a")._var2
[121, 73, 141, 146, 115, 230, 181, 65, 238, 17, 146, 73, 228, 82, 188, 66, 12, 148, 225, 66, 255, 254, 47, 22, 163, 250, 222, 133, 35, 232, 106, 176]
>>> chal.chal("a")._var3
[12, 243, 133, 147, 7, 36, 29, 49, 226, 211, 156, 56, 142, 78, 254, 12]
```

可以看到，chal实际上是chal模块里的一个类，类里面有`_p1`、`_p2`、`_p3`三个函数，初始化以后多了`_tips`、`_var1`、`_var2`、`_var3`四个变量。那main.py里面实际上是用flag初始化了一个chal.chal类，对flag的check也在类的`__init__`函数中。而`__init__`函数透露的信息很少，所以只能老老实实看伪代码。

### cython伪代码阅读

这里介绍一下如何通过伪代码恢复出原来的Python代码。限于篇幅，以下仅列举一些典型的代码序列。

#### C级别的全局变量赋值

**字符串类型**

> `_Pyx_CreateStringTabAndInitStrings`

全局字符串赋值一般在`_Pyx_CreateStringTabAndInitStrings`中，该函数中使用的字符串定义数组形如：

```
typedef struct {
    PyObject **p;
    const char *s;
    const Py_ssize_t n;
    const char* encoding;
    const char is_unicode;
    const char is_str;
    const char intern;
} __Pyx_StringTabEntry;
```

而字符串是通过`__Pyx_StringTabEntry`的数组进行初始化的，也就是说当我们在该函数中看到以下伪代码时：

```
__m128i v8;
__int64 v9;
__int64 v10;
__int16 v11;
char v12;

v8 = _mm_unpacklo_epi64(&qword_28A98, "AttributeError");
v9 = 15LL;
v10 = 0LL;
v11 = 0x100;
v12 = 1;
```

就代表这是一个`{&qword_28A98, "AttributeError", 15, 0, 1, 0, 1}`的`__Pyx_StringTabEntry`，也就是说`qword_28A98`中将要初始化一个内容是`"AttributeError"`的字符串对象的地址，在后续调用中，调用到AttributeError字符串的地方都会用`&qword_28A98`指代。

**整数类型**

> `_pyx_pymod_exec_chal`

```
qword_29170 = PyLong_FromLong(113LL, v9, v244, v245);
if ( qword_29170 )
```

`qword_29170`中将存储一个值为`113`的整数类型的Python对象。

```
qword_29600 = PyLong_FromString("2654435769", 0LL, 0LL);
if ( qword_29600 )
```

大数会用`PyLong_FromString`函数来初始化，这里`qword_29600`中将存储一个值为`2654435769`的整数类型的Python对象，后续用到2654435769的地方将使用`qword_29600`。

**内建函数/变量**

> `_Pyx_InitCachedBuiltins`, called by `_pyx_pymod_exec_chal`
>
> （在某些优化下也会直接嵌入 `_pyx_pymod_exec_chal`）

```
qword_296B8 = _Pyx_GetBuiltinName(qword_28A98);
if ( !qword_296B8 )
  return 0xFFFFFFFFLL;
```

`qword_28A98`就是前面的`"AttributeError"`，这里是通过名字找到`AttributeError`对象，并赋值给`qword_296B8`，后续用到`AttributeError`对象的地方将使用`qword_296B8`。

**常量**

> `_Pyx_InitCachedConstants`, called by `_pyx_pymod_exec_chal`
>
> （在某些优化下也会直接嵌入 `_pyx_pymod_exec_chal`）

```
qword_29630 = PyTuple_Pack(2LL, qword_29600, qword_29618);
if ( !qword_29630 )
  return 0xFFFFFFFFLL;
```

`qword_29600`就是前面的值为`2654435769`的整数类型的Python对象，同理`qword_29618`就是值为`3337565984`的整数类型的Python对象。这里将这两个对象打包成了一个长度为`2`的元组`(2654435769, 3337565984)`，并赋值给`qword_29630`变量，后续用到这个元组的地方将使用`qword_29630`。

**函数声明及定义**

> 声明在`_Pyx_InitCachedConstants`, called by `_pyx_pymod_exec_chal`
>
> （在某些优化下也会直接嵌入 `_pyx_pymod_exec_chal`）
>
> 定义在`_pyx_pymod_exec_chal`

这里变量太多直接上手动恢复后的符号。

```
// *** _Pyx_InitCachedConstants ***
// 元组赋值
v1 = PyTuple_Pack(7LL, self, x1, x2, tmp, low, high, ans);
if ( !v1 )
  return 0xFFFFFFFFLL;
// 函数定义
qword_29688 = _Pyx_PyCode_New_constprop_0(
  3, 7, qword_28A80, qword_28A78, qword_28A78, v1, qword_28A78,
  qword_28A78, chal_py, p1, 19, qword_28A80
);
if ( !qword_29688 )
  return 0xFFFFFFFFLL;
```

`_Pyx_PyCode_New_constprop_0`用于创建一个`PyCodeObject`，其参数就是`PyCodeObject`的各属性，具体可参考各版本cpython源码中对`PyCodeObject`的定义，这里就是以`v1`元组为参数+局部变量名（前`3`个为参数），原Python函数第一行在文件中的第`19`行（`qword_28A78`是`()`，`qword_28A80`是`""`，无内容不用关注）创建了一个名为`_p1`的函数`PyCodeObject`，相当于是函数声明（因为`co_code`字段是空的，没有指定具体行为）。

```
// *** _pyx_pymod_exec_chal ***
v559 = _Pyx_CyFunction_New_constprop_0(&_pyx_mdef_4chal_4chal_3_p1, chal__p1, chal, _pyx_mstate_global_static, qword_29688);
v560 = PyObject_SetItem(v6, p1, v559) >> 31; // self._p1 = v559
```

cython中一般使用`PyMethodDef`进行指定：

```
ctypedef struct PyMethodDef:
    const char* ml_name
    PyCFunction ml_meth
    int ml_flags
    const char* ml_doc
```

伪代码中的`_pyx_mdef_4chal_4chal_3_p1`就是一个`PyMethodDef`：

```
.data:00000000000289C0 AD 41 02 00 00 00 00 00           __pyx_mdef_4chal_4chal_3_p1 dq offset aChalChalP1+0Ah
.data:00000000000289C0                                                                 ; DATA XREF: __pyx_pymod_exec_chal+236B↑o
.data:00000000000289C0                                                                 ; "_p1"
.data:00000000000289C8 70 F7 00 00 00 00 00 00           dq offset __pyx_pw_4chal_4chal_3_p1
.data:00000000000289D0 82 00 00 00                       dd 82h
.data:00000000000289D4 00                                db 0
```

`_p1`的函数体实际上在`__pyx_pw_4chal_4chal_3_p1`中。

**import**

> `_pyx_pymod_exec_chal`

```
v539 = _Pyx_ImportDottedModule_constprop_0(random);
if ( PyDict_SetItem(_pyx_mstate_global_static, random, v539) < 0 )
{
```

导入random模块，同`import random`。

#### Python代码的转译

**对象变量赋值**

```
v22 = PyObject_SetAttr(self, var1, s);
```

直接用了`PyObject_SetAttr`函数，其实反编译过来就是`self._var1 = s`。

**数组赋值**

```
v23 = PyList_New(32LL); // 1. 创建新的列表对象
v24 = pyx_int_121; // 2. v24 = 121
if ( *pyx_int_121 != -1 ) // 3. 错误处理
  ++*pyx_int_121;
v25 = v23[3]; // 4. 列表对象（v23）的[3]是数据部分
*v25 = v24; // 5. 列表第一个元素为v24即121
// ... 重复以上2、3、5步处理对列表赋值
v58 = PyObject_SetAttr(self, var2, v23);
```

最后将成型的列表`v23`赋给`self._var2`，这里就是`self._var2 = v23 = [121, ...]`

**函数调用**

以下是一段如果参数为变量对Python函数的完整调用，没有标注的都是框架代码及错误处理。

```
    v150 = *(*(self + 8) + 144LL);
// v2 = self._p3
    if ( v150 )
      v2 = v150(self, p3);
    else
      v2 = PyObject_GetAttr(self, p3);
    if ( !v2 )
    {
      v101 = 0LL;
      v1 = 0LL;
      v23 = 0LL;
      v122 = 4493LL;
      v123 = 10LL;
      goto LABEL_211;
    }
    if ( *(v2 + 8) == &PyMethod_Type && (v151 = *(v2 + 24)) != 0LL )
    {
      v1 = *(v2 + 16);
      if ( *v151 != -1 )
        ++*v151;
      if ( *v1 != -1 )
        ++*v1;
      if ( *v2 >= 0 )
      {
        v152 = *v2 - 1LL;
        *v2 = v152;
        if ( !v152 )
          _Py_Dealloc(v2);
      }
// 参数是("Don't hook!!!")
      v192 = _mm_loadh_ps(&Don_thook___);
// 函数调用，执行self._p3("Don't hook!!!")，返回值给v23
      v23 = _Pyx_PyObject_FastCallDict_constprop_0(v1, &v192, 2LL);
      if ( *v151 >= 0 )
      {
        v153 = *v151 - 1LL;
        *v151 = v153;
        if ( !v153 )
          _Py_Dealloc(v151);
      }
    }
// 不同的调用方式，和上面的if同层
    else
    {
      v1 = v2;
      v192.m128_u64[0] = 0LL;
      v192.m128_u64[1] = Don_thook___;
      v23 = _Pyx_PyObject_FastCallDict_constprop_0(v2, v187, 1LL);
    }
    if ( !...