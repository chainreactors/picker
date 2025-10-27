---
title: pyd文件逆向
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458590213&idx=1&sn=8ac33f2b66257296cc0e4c41ae141301&chksm=b18c2c8f86fba5997ae75b0871ce90ce64f79d6864e5707578a521fac3c88bdc27ad04a6f7df&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-03-01
fetch_date: 2025-10-06T21:58:51.001225
---

# pyd文件逆向

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseaTjx0tlSVdFDdY0yD62cM2rH4Cn575jQIYmlkZ3n3IicZUicMFxCiakUng/0?wx_fmt=jpeg)

# pyd文件逆向

mingyuexc

看雪学苑

## 手动编译

按照官方文档编译一个 pyd 文件：

python pip 安装模块cython

```
pip install Cython
```

编写一个hello.pyx 脚本, 里面随便写一个函数

```
def say_hello_to(name):    print(f"Hello {name}!")
```

在同目录编写一个 setup.py 脚本，里面的文件名为固定的内容，文件名为刚刚写的py脚本完整名称

```
from setuptools import setupfrom Cython.Build import cythonize setup(    name='Hello world app',    ext_modules=cythonize("hello.pyx"),)
```

在命令行执行命令,来编译这个文件

```
python setup.py build_ext --inplace
```

编译成果后会在同级目录下生成很多东西:

build 目录 存放一些编译生成的中间文件

xxxx.c py文件到c源码文件，中间包含了完整的c代码

xxxxx.cpyyyy-win\_amd64.pyd 编译好的文件xxxx 为py文件的命名 yyyy 为python的版本号 ，这个文件可只保留原始文件名和后缀.pyd 例如 bbbbb.cp312-win\_amd64.pyd -> bbbbb.pyd

> 如果两个文件在同时在同级目录下，python会优先选择带版本号的，如果没有再选择不带版本号的文件

如何调用?

在同级目录下，直接打开python使用 import xxxx 即可调用

```
import hellofrom hello import say_hello_to
```

查看xxxx.c

里面有非常多的结构，并且有python代码转换的c源代码，我们可以在这里看到cython的转换规则，和大体的逻辑

```
static PyObject *__pyx_pf_5bbbbb_say_hello_to(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_name) {  PyObject *__pyx_r = NULL;  __Pyx_RefNannyDeclarations  PyObject *__pyx_t_1 = NULL;  PyObject *__pyx_t_2 = NULL;  int __pyx_lineno = 0;  const char *__pyx_filename = NULL;  int __pyx_clineno = 0;  __Pyx_RefNannySetupContext("say_hello_to", 1);   /* "bbbbb.pyx":4 * * def say_hello_to(name): *  print(f"Hello {name}")             # <<<<<<<<<<<<<< */  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_v_name, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 4, __pyx_L1_error)  __Pyx_GOTREF(__pyx_t_1);  __pyx_t_2 = __Pyx_PyUnicode_Concat(__pyx_kp_u_Hello, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 4, __pyx_L1_error)  __Pyx_GOTREF(__pyx_t_2);  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 4, __pyx_L1_error)  __Pyx_GOTREF(__pyx_t_1);  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;   /* "bbbbb.pyx":3 * * * def say_hello_to(name):             # <<<<<<<<<<<<<< *  print(f"Hello {name}") */   /* function exit code */  __pyx_r = Py_None; __Pyx_INCREF(Py_None);  goto __pyx_L0;  __pyx_L1_error:;  __Pyx_XDECREF(__pyx_t_1);  __Pyx_XDECREF(__pyx_t_2);  __Pyx_AddTraceback("bbbbb.say_hello_to", __pyx_clineno, __pyx_lineno, __pyx_filename);  __pyx_r = NULL;  __pyx_L0:;  __Pyx_XGIVEREF(__pyx_r);  __Pyx_RefNannyFinishContext();  return __pyx_r;}
```

这里编译的没有带符号，所以逆向的话，ida载入，很多函数都是没有函数名称的.

## 手动编译1 带符号

在Linux下默认带有符号，Windows下默认不带符号，需要增加参数来生成详细的PDB，并ida加载PDB才能看到更详细内容。

我们可以通过修改setup.py 来编译一个带符号的。

```
from setuptools import setup, Extensionfrom Cython.Build import cythonize ext_module = [    Extension(        name="www",        sources=["www.py"],        extra_compile_args=["/Zi"],        extra_link_args=["/DEBUG"]    )] setup(    name = "www",    ext_modules = cythonize(ext_module,annotate=True))
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseaXWvLAYStd1LKCg41DbUYjntn7oBD0EubdRJUYtHWkQ2gxfBt0eAKHg/640?wx_fmt=png&from=appmsg)

也可以在命令行编译时，增加 --debug 参数，但需要在安装Python时勾选 Download debug binaries ，否则会提示 104: 无法打开文件“python312\_d.lib”

## 手动编译2 linux 不带符号

linux 默认情况下，编译出来带有符号，我们可以通过调整编译选项来编一个一个不带符号的pyd文件。

```
from setuptools import setup, Extensionfrom Cython.Build import cythonize  extensions = [    Extension(            sources=["xxx.py"],            name="xxx"            extra_link_args=["-Wl,--strip-all"]        ),] setup(    ext_modules=cythonize(extensions),)
```

#

# 各种表达式解析

## 函数

默认情况下, 对外函数，可以搜索名称, 因为是全局变量，所以，变量都会放在一起

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseaGPJc0ZyOIDp2Cqxh92b9s449SRto6AElegibFhMD4CVSSXoUQOSRtOg/640?wx_fmt=png&from=appmsg)

查找引用，可以发现结构体:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseakA8nP0icstYcFUWyPbiaR3sKbEiaJjwxd3fwfvv6LA7IicfqRTztRNiarWw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseaibqvkTJYYbaLibI1ll1TNoVMW0jV4iaJUHugJsUXJOFzicfBZIHup3OhtA/640?wx_fmt=png&from=appmsg)

windows 下会多出一层调用 pw -> pf ， pf 是真正的地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgsealFowcPlZ2lIsKR0TaU1L7ibiaibrqosjCSmWBsHAXpVIv9rTrZlb6wnmw/640?wx_fmt=png&from=appmsg)

Windows Release 版本也是一致: 就是符号没有这么明显，要稍微熟悉一点pyd的结构体。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9Kgsea31qfRJ4HsKLjWNsXlnGIibVZAsE2OSfyY57ic5TAJjsib26Omq42Xodgw/640?wx_fmt=png&from=appmsg)

Linux 默认情况下没有，可能被编译器优化掉 了，但c语言源码上基本一致，pw->pf 函数名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseaSyibJo7cJWPtfAlDWK4QRgOGexdibcfTHW9yDKOQEqRxJic98eEZzkHVA/640?wx_fmt=png&from=appmsg)

### 模块内函数/变量引用

函数的结构体大多都放在一起的，可以上下查找有没有其他的函数，直接搜索函数名，有时候可能会搜不到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseaOSRkRcCGLAcp36PnicPGZj6Zy0dDoCAFJcKclovYlrQpZibYEIVp4vNw/640?wx_fmt=png&from=appmsg)

```
def get_list():    return [1,2,3,4,991,776,229, 12.22] def get_list1(index,end):    a= get_list()        return a
```

在模块中调用模块的内容，会先调用 PyDict\_GetItem\_KnownHash 中获取，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9Kgsea1hBQXZtibKfS563jSEOvichIalMHgBfUlzU0KtEwAGQLT0QHlhO2WPvQ/640?wx_fmt=png&from=appmsg)

寻找引用，一般是在 pymod\_exec 完成初始化, xxxx+38) + 24

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseaUdic69280742rf85qEibpsxicmJl11ibIuK2Mp4Gjmdfk9ZLfysSSxZL4w/640?wx_fmt=png&from=appmsg)

可以看到确实是 get\_list 这个函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseaheicYV2XicoiczBQXzPEZhu9L3ufiaEWQUwvgdZ3UOIPtX0jeU03L1DzWw/640?wx_fmt=png&from=appmsg)

对比有符号的发现，+24 是 ob\_type v2 是函数地址

## 模块调用

```
import socketimport subprocess socket.socket(socket.AF_INET,socket.SOCK_STREAM)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseajKKpPoNbmcQSOclsB1iaU2Dpm8Evbx0Z5eia8Ny9Yko9szGbS5kYwv9Q/640?wx_fmt=png&from=appmsg)

调用后的模块地址在v6, 然后又传给v10， 就可以跟着v10，看看有没有发生其他动作 一般来说，会使用 PyObject\_GetAttr 来获取属性

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseaC4zrSFKXSLbXu47dw76KHVxdg79ZkJ17ltvyu5ibh83TQFCCXicsHNNA/640?wx_fmt=png&from=appmsg)

这种模块调用会有引用计数的特性, 可以看到 v17 为属性, 其中经过了 ob\_refcnt ，比较经典。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9Kgseal0ZL2VDyAYh44LNtiapDqw5cHyboMgj5IMLmfNCjrwauB3B5B0Rs3IQ/640?wx_fmt=png&from=appmsg)

再经过 Pyx\_PyObject\_FastCallDict 来调用，参数为 v21 v26

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseapAYCvmtw8rrMFuqR051Bo4sIUcqkUBANibjicggl7SmuXjoKPzK2eT3w/640?wx_fmt=png&from=appmsg)

有时候ida 可能识别的参数不对，数组大小不对，需要手动判别，更改。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseaMnmH47BwhW2rqeU3LpgsDWJKqMVCjE7zmoT5iaiaDLhVnElrk3j1QibsQ/640?wx_fmt=png&from=appmsg)

可以看到v21的具体内容为 AF\_INET

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9Kgsea7HkNd6j5YlFXENaqYkzg4ibRTwCC5HYlK0HAdXVr4Z3ZghVFyJP3GUg/640?wx_fmt=png&from=appmsg)

v26 的内容为 SOCK\_STREAM

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gy7AMcsiaib2Diazvfw9KgseaOjNCddmeq79DOtticxBWHqccmT2f2Y8rNyjsxuBXueBicwGuPOpYT25A/640?wx_fmt=png&from=appmsg)

基本上可以通过静态大致识别出一些关键代码

## 运算

### 加减乘除移位左移右移xor与或非

编写测试函数

```
def test_calc(a):    res = a + 1    res = res -10    res = res * 998    res = res / 100    res = res * 200    res = res // 30    res = res ** 3    res = res << 3    res = res ^ a    res = hex(res)[2:]    res = res + '00'    res = int(res, 16)    res = res >> 4    res = res | 0xf    res = res & 0x1f    res = ~rsa    return res
```

```
_typeobject *__fastcall _pyx_pf_5bbbbb_10test_calc(_object *__pyx_v_a, _object *__pyx_self, __int64 a3){  _typeobject *v3; // r12  _typeobject *v5; // rbx  _object *pyx_int_1; // r9  _typeobject *ob_type; // rax  unsigned __int64 ob_refcnt; // r8  __int64 v9; // rax  unsigned __int64 v10; // r8  const char *v11; // rsi  int v12...