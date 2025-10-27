---
title: CPython逆向实战分析
url: https://www.secpulse.com/archives/205557.html
source: 安全脉搏
date: 2024-12-18
fetch_date: 2025-10-06T19:38:11.339285
---

# CPython逆向实战分析

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# CPython逆向实战分析

[内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-17

11,734

Python代码转换为C代码的时候，将会大大增加框架代码量。

[基础教程 | Cython 官方文档中文版(gitbooks.io)](https://moonlet.gitbooks.io/cython-document-zh_cn/content/ch1-basic_tutorial.html)

## 1、正向py->c

先有正向，再有逆向

```
pip install cython
```

写一个简单的pyx文件

.pyx 文件是由 Cython 编程语言 "编写" 而成的 Python 扩展模块源代码文件

```
print("hello")
```

写一个 setup.py文件

```
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("test.pyx")
)
```

使用命令开始编译

```
python setup.py build_ext --inplace
```

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530565.png)

生成如下文件

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530566.png)

打开test.c发现有几千行代码

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530567.png)

单纯的一行python代码，生成为c代码就几千行

调用so文件

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530568.png)

## 2、逆向分析

#### 2.1 字符串类型

\_Pyx\_CreateStringTabAndInitStrings

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
v8 = _mm_unpacklo_epi64(&qword_28A98, "AttributeError");
v9 = 15LL;
v10 = 0LL;
v11 = 0x100;
v12 = 1;
```

就代表这是一个`{&qword_28A98, "AttributeError", 15, 0, 1, 0, 1}`的`__Pyx_StringTabEntry`，也就是说`qword_28A98`中将要初始化一个内容是`"AttributeError"`的字符串对象的地址，在后续调用中，调用到AttributeError字符串的地方都会用`&qword_28A98`指代

### 2.2 整数类型

> `_pyx_pymod_exec_chal`

```
qword_29170 = PyLong_FromLong(113LL, v9, v244, v245);
if ( qword_29170 )
```

`qword_29170`中将存储一个值为`113`的整数类型的Python对象。

```
qword_29600 = PyLong_FromString("2654435769", 0LL, 0LL);
if ( qword_29600 )
```

大数会用`PyLong_FromString`函数来初始化，这里`qword_29600`中将存储一个值为`2654435769`的整数类型的Python对象，后续用到2654435769的地方将使用`qword_29600`。

### 2.3 import写法

```
v539 = _Pyx_ImportDottedModule_constprop_0(random);
if ( PyDict_SetItem(_pyx_mstate_global_static, random, v539) < 0 )
{
```

``` 导入``random``模块，同``import random ```

## 3、实战分析

这里提供一道自己出的题目，采用了RC4加密，流程很简单。

让我们开干

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530569.png)

把提供的so文件拖进IDA中

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530570.png)

而且这个函数 \_Pyx\_CreateStringTabAndInitStrings() 非常大，不能反编译

目前不知道这个函数的加密，我们先打印其相关的属性，看看能不能找到蛛丝马迹

```
import test
dir(test)
```

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530571.png)

发现是RC4加密，这样逻辑就清晰了

所以现在的目标是获得RC4的秘钥和密文咯，假设RC4没有魔改

刚才我们在函数\_Pyx\_CreateStringTabAndInitStrings 找到了非常类似密文的值

```
9d7422eabf8baf369c09121f02e940099d9c6b538d88e30aac08
```

但是没有找到 秘钥，说明秘钥可能就不是字符串，而是byte类型！

我们先搜索RC4相关函数

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530572.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530573.png)

发现代码非常多，暂时先不去分析RC4算法

看看哪里调用了我们的RC4算法

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530574.png)

函数：\_pyx\_pymod\_exec\_test

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530575.png)

但是byte类型怎么初始化呢？

我们编写一个demo，然后反编译去查看初始化方式即可

demo.pyx

```
key = b'mykekekeke'
en_flag = b'12312312312312'
```

demo\_setup.pyx

```
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("demo.pyx")
)
```

运行命令

```
python demo_setup.py build_ext --inplace
```

先看看c文件

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530576.png)

还是很清晰的，直接IDA分析so文件

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530577.png)

发现byte类型也存储在函数\_Pyx\_CreateStringTabAndInitStrings

所以我们再翻阅一下，成功找到类似key的代码

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530578.png)

```
DASCTF{cpython_is_so_easy}
```

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410251530579.png)

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205557.html**](https://www.secpulse.com/archives/205557.html)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![记一次有点抽象的渗透经历](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2025/01/VCG41N1195673150.png)

  记一次有点抽象的渗透经历](https://www.secpulse.com/archives/205044.html "详细阅读 记一次有点抽象的渗透经历")
* [![浅谈内联钩取原理与实现](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/06/VCG211415001580-210x140.jpg)

  浅谈内联钩取原理与实现](https://www.secpulse.com/archives/205124.html "详细阅读 浅谈内联钩取原理与实现")
* [![浅谈进程隐藏技术](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2025/01/vcg.png)

  浅谈进程隐藏技术](https://www.secpulse.com/archives/205188.html "详细阅读 浅谈进程隐藏技术")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/logo-white.png)](https://www.secpulse.com/newpage/author?author_id=37244aaa) | [蚁景网安实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=37244) | |
| 文章数：402 | 积分： 877 |
| 蚁景网安实验室（www.yijinglab.com）网络安全靶场练习平台，涉及CTF赛前指导、职业技能训练、网安专项技能提升等。 | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](htt...