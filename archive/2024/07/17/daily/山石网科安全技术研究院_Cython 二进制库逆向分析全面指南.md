---
title: Cython 二进制库逆向分析全面指南
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247507102&idx=1&sn=5b38235bb8f8bb1dd5b4e2e0325f3f48&chksm=fa520920cd2580369b112cd7f1c2a2841bec74afecdaffdcaab85a4e93dd6e34ccf005e299a5&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-07-17
fetch_date: 2025-10-06T17:42:23.773727
---

# Cython 二进制库逆向分析全面指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnQpwBfkgA4uol1Yrurxp7k12LvxrHxhhJLDXyWYErPEt3D0w6jib5jg5ur6LXPQNdW2YuISeEAaRHQ/0?wx_fmt=jpeg)

# Cython 二进制库逆向分析全面指南

原创

c10udlnk

山石网科安全技术研究院

众所周知，Python 类题目最难的一类是使用 **cython**（https://github.com/cython/cython）工具将 Python 代码转成 C 代码并编译成二进制库。此类题目比单纯使用 **Python/C API** 编写 C 代码编译成二进制库的方式更加复杂，cython 工具作为一类通用工具，为了提高稳健性，其在转换时会对 Python 代码做额外处理（包括对引用计数的调整），从而干扰我们的逆向。当然，也正是因为它是通用工具，其整体框架和对类似 Python 字节码的处理也有一定规律，当我们熟悉这个规律以后，手撕 cython 二进制库就非常轻松了。

## 初探 cython

先用最经典的 **Hello world** 做例子，保存为`hello_world.py`：

```
print("Hello, World!")
```

然后调用 cython 转成 C 并编译：

```
cythonize -i hello_world.py
```

然后我们可以看到一个`hello_world.c`生成在同一目录中，可以看到这个 c 文件足足有4155行……！

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQpwBfkgA4uol1Yrurxp7k1tp0sVbe13lnk5B0d5mVQTFFAtibqUpibqWRoUib8je0F1XtHZP12QERFw/640?wx_fmt=png&from=appmsg)

足以证明其框架代码和处理代码之多。

实际上真正执行了`print("Hello, World!")`的代码是以下几行，作用写在了注释中：

```
// 字符串赋值
static const char __pyx_k_print[] = "print";
static const char __pyx_k_Hello_World[] = "Hello, World!";
// 将字符串和变量/变量名联系在一起
static int __Pyx_CreateStringTabAndInitStrings(void) {
  __Pyx_StringTabEntry __pyx_string_tab[] = {
    // ...
    {&__pyx_kp_s_Hello_World, __pyx_k_Hello_World, sizeof(__pyx_k_Hello_World), 0, 0, 1, 0},
    // ...
    {&__pyx_n_s_print, __pyx_k_print, sizeof(__pyx_k_print), 0, 0, 1, 1},
    // ...
  };
  return __Pyx_InitStrings(__pyx_string_tab);
}
// 获取print代码对象，并以arg_tuple为参数进行调用
static int __Pyx_Print(PyObject* stream, PyObject *arg_tuple, int newline) {
    // ...
    if (unlikely(!__pyx_print)) {
        __pyx_print = PyObject_GetAttr(__pyx_b, __pyx_n_s_print);
        // ...
    }
    // ...
    result = PyObject_Call(__pyx_print, arg_tuple, kwargs);
    // ...
}
// print参数只有一个的情况
static int __Pyx_PrintOne(PyObject* stream, PyObject *o) {
    // ...
    PyObject* arg_tuple = PyTuple_Pack(1, o);
    // ...
    res = __Pyx_Print(stream, arg_tuple, 1);
    // ...
}
// 调用__Pyx_PrintOne(0, __pyx_kp_s_Hello_World)
static CYTHON_SMALL_CODE int __pyx_pymod_exec_hello_world(PyObject *__pyx_pyinit_module) {
  // ...
  if (__Pyx_PrintOne(0, __pyx_kp_s_Hello_World) < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  // ...
}
```

print 函数的调用实际上还是做了优化的，普通的函数调用会在后文中介绍。

然后也是同一个思路，在二进制库中可以找到：

```
int __cdecl _Pyx_CreateStringTabAndInitStrings()
{
  // ...
  __pyx_string_tab[1].encoding = 0LL;
  *(__m128i *)&__pyx_string_tab[1].p = _mm_unpacklo_epi64(
                                         (__m128i)(unsigned __int64)&_pyx_mstate_global_static.__pyx_kp_s_Hello_World,
                                         (__m128i)(unsigned __int64)"Hello, World!");
  // ...
  __pyx_string_tab[1].n = 14LL;
  *(_WORD *)&__pyx_string_tab[1].is_unicode = 256;
  __pyx_string_tab[1].intern = 0;
  // ...
  *(__m128i *)&__pyx_string_tab[7].p = _mm_unpacklo_epi64(
                                         (__m128i)(unsigned __int64)&_pyx_mstate_global_static.__pyx_n_s_print,
                                         (__m128i)(unsigned __int64)"print");
  __pyx_string_tab[7].n = 6LL;
  __pyx_string_tab[7].encoding = 0LL;
  *(_WORD *)&__pyx_string_tab[7].is_unicode = 256;
  __pyx_string_tab[7].intern = 1;
  // ...
}
__int64 __fastcall _pyx_pymod_exec_hello_world(PyObject *__pyx_pyinit_module)
{
                        // ...
                        if ( PyDict_GetItemString(ModuleDict, "hello_world")
                          || (int)PyDict_SetItemString(v17, "hello_world", _pyx_m) >= 0 )
                        {
                          v18 = (PyObject *)PyTuple_Pack(1LL, _pyx_mstate_global_static.__pyx_kp_s_Hello_World);
                          if ( !v18 )
                            goto LABEL_42;
                          if ( (_pyx_print
                             || (pyx_b = _pyx_mstate_global_static.__pyx_b,
                                 (_pyx_print = (PyObject *)PyObject_GetAttr(
                                                             _pyx_mstate_global_static.__pyx_b,
                                                             _pyx_mstate_global_static.__pyx_n_s_print)) != 0LL))
                            && (v19 = (PyObject *)PyObject_Call(_pyx_print, v18, 0LL), (pyx_b = v19) != 0LL) )
                          {
                            v22 = v19->ob_refcnt-- == 1;
                            if ( v22 )
                              _Py_Dealloc(v19);
                            v21 = 0;
                          }
                          // ...
}
```

`_Pyx_CreateStringTabAndInitStrings`和 C 源码中的大致一致；`_pyx_pymod_exec_hello_world`把`__Pyx_PrintOne`展开编进了函数中（都被指定了`__attribute__((cold))`扩展的函数），这里调用主要是把`__pyx_kp_s_Hello_World`即字符串`"Hello, World!"`的 PyObject 打成一个 tuple，然后用`PyObject_Call`调用`PyObject_GetAttr`拿到的`print`函数的 PyCodeObject，完成了对`print("Hello, World!")`的调用。

**这也是普通函数的调用流程，有一个 tuple 存非关键字参数（args）、一个 dict 存关键字参数（kwargs），然后调用`PyObject_Call`，其三个参数分别是被调用函数的 PyCodeObject、args tuple、kwargs dict，这样就完成了对 Python 函数的调用。**

手撕 cython 无非就是把它调用了什么 Python 函数还原出来，所以可以围绕伪代码中的`PyObject_Call`进行简单拼凑，其他的操作（如赋值、运算、循环等）也可以在阅读伪代码时通过排除非关键代码的情况下得出。

## 从 cython 中识别关键代码

将`hello_world.py`改一下：

```
for i in range(16):
    print("Hello, World!")
```

加了一个循环，cython 转成的 C 代码里是：

```
static CYTHON_SMALL_CODE int __pyx_pymod_exec_hello_world2(PyObject *__pyx_pyinit_module) {
  // ...
  for (__pyx_t_2 = 0; __pyx_t_2 < 16; __pyx_t_2+=1) {
    __pyx_t_3 = __Pyx_PyInt_From_long(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_i, __pyx_t_3) < 0) __PYX_ERR(0, 1, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple_, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 2, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  }
  // ...
}
```

可以看到 Python 代码中的 for 循环转成了`for (__pyx_t_2 = 0; __pyx_t_2 < 16; __pyx_t_2+=1)`。

`__Pyx_PyInt_From_long`函数是将数字转化为 Python 中的数字类型的 PyObject，便于后续计算（虽然这里并没有用到 for 循环中的变量 i），`PyDict_SetItem(__pyx_d, __pyx_n_s_i, __pyx_t_3)`是将转化后的数字存进变量 i 中。

然后关键的 print 还是那一句 `__Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple_, NULL)`，`__pyx_tuple_`是在常量初始化时赋值的，跟前文一样是将被转成字符串类型 PyObject 的字符串打进 tuple 中：

```
static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  // ...
  __pyx_tuple_ = PyTuple_Pack(1, __pyx_kp_s_Hello_World); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 2, __pyx_L1_error)
  // ...
}
```

在回到前面的 C 代码中，类似`if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1, __pyx_L1_error)`的代码作用是为了避免前一个函数（如这里的`__Pyx_PyInt_From_long`）失败导致 return 的结果（这里的`__pyx_t_3`）为 0，从而引发空指针解引用漏洞。此类 handle error 的代码我们可以忽略。

至于`__Pyx_GOTREF`和`__Pyx_DECREF`等类似函数是用于调整 PyObject 的引用计数，此处由于不是重点不再细说，只要知道这是用于维稳的非关键函数即可。

再看二进制库反编译后的伪代码，提取了包含关键代码的一部分，写了一些注释以辅助理解：

```
__int64 __fastcall _pyx_pymod_exec_hello_world2(PyObject *__pyx_pyinit_module)
{
  // ...
// 确认有没有 range，实际上 range(16) 已经在后面被融入 for 循环里了
  if ( !_Pyx_GetBuiltinName(_pyx_mstate_global_static.__pyx_n_s_range)
// 获取 print 的 PyCodeObject
    || (BuiltinName = _Pyx_GetBuiltinName(_pyx_mstate_global_static.__pyx_n_s_print),
        (_pyx_builtin_print = BuiltinName) == 0LL) )
// handle error，忽略
  {
    v27 = 2333;
    v28 = 1;
    goto LABEL_63;
  }
// 把字符串 "Hello, World!" 打成一个 tuple
  _pyx_mstate_global_static.__pyx_tuple_ = (PyObject *)PyTuple_Pack(
                                                         1LL,
                                                         _pyx_mstate_global_static.__pyx_kp_s_Hello_World);
// handle error，忽略
  if ( !_pyx_mstate_global_static.__pyx_tuple_ )
  {
    v27 = 2335;
    v28 = 1;
    goto LABEL_63;
  }
// for 循环开始
  for ( k = 0LL; k != 16; ++k )
  {
// 上文的 __Pyx_PyInt_From_long
    v18 = PyLong_FromLong(k);
    v19 = (_QWORD *)v18;
// handle error，忽略
    if ( !v18 )
    {
      v27 = 2354;
LABEL_147:
      code_line = 1;
      goto LABEL_148;
    }
// 给 i 赋值
    if ( (int)PyDict_SetItem(_pyx_mstate_global_static.__pyx_d, _pyx_mstate_global_static.__pyx_n_s_i, v18) < 0 )
...