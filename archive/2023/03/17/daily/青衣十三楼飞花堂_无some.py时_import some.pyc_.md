---
title: 无some.py时"import some.pyc"
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247486549&idx=1&sn=b18b8f94cb61ecacde2fcd4caec104b1&chksm=fab2cf6acdc5467ce3f047f8a6711f759a8f01fd05313298d97be863fabbb84a25fd53269ca4&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2023-03-17
fetch_date: 2025-10-04T09:51:51.842918
---

# 无some.py时"import some.pyc"

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPNP4iciaCk6R9IkjLXzbwNFd5lSnWYCPg0J8nibRBmHJqG8eAEAOb0xrUFehEe8MON8jGCWict25ibydjQ/0?wx_fmt=jpeg)

# 无some.py时"import some.pyc"

stackoverflow

青衣十三楼飞花堂

26.29 无some.py时"import some.pyc"

```
https://scz.617.cn/python/201309251607.txt
```

Q:

现有is\_prime\_pub.pyc，没有is\_prime\_pub.py，此种情况可以直接执行pyc

python is\_prime\_pub.pyc 59

想进一步，在other.py中"import is\_prime\_pub"，并调用is\_prime\_pub中函数。

A: falsetru@stackoverflow 2013-09-25

参看

```
Import arbitrary python source file. (Python 3.3+)
https://stackoverflow.com/questions/19009932/import-arbitrary-python-source-file-python-3-3
```

至少有三种写法，用Python 3.9.0测试无误

```
import importlib.machinery
import importlib.util

#
# Load the compiled module from the .pyc file
#
loader          = importlib.machinery.SourcelessFileLoader( 'is_prime_pub', 'is_prime_pub.cpython-39.opt-2.pyc' )
spec            = importlib.util.spec_from_loader( loader.name, loader )
is_prime_pub    = importlib.util.module_from_spec( spec )
loader.exec_module( is_prime_pub )

#
# Call a method in the module
#
low_prime       = [2,3]
low_prime      += [x for x in range(5,2047,2) if is_prime_pub.rabin_miller_test(x,b=2,rounds=1)]
print( is_prime_pub.is_prime( 59, low_prime, 5 ) )
```

或

```
import importlib.machinery
import types

#
# Load the compiled module from the .pyc file
#
loader          = importlib.machinery.SourcelessFileLoader( 'is_prime_pub', 'is_prime_pub.cpython-39.opt-2.pyc' )
is_prime_pub    = types.ModuleType( loader.name )
loader.exec_module( is_prime_pub )

#
# Call a method in the module
#
low_prime       = [2,3]
low_prime      += [x for x in range(5,2047,2) if is_prime_pub.rabin_miller_test(x,b=2,rounds=1)]
print( is_prime_pub.is_prime( 59, low_prime, 5 ) )
```

用的是SourcelessFileLoader，不是SourceFileLoader，用后者时报错

```
ValueError: source code string cannot contain null bytes
```

无some.py直接加载some.pyc时，解释器会检查pyc首部"magic number"，必须匹配当前解释器版本，否则报错，比如

```
ImportError: bad magic number in 'is_prime_pub': b'a\r\r\n'
```

或

```
import importlib.machinery

#
# Load the compiled module from the .pyc file
#
loader          = importlib.machinery.SourcelessFileLoader( 'is_prime_pub', 'is_prime_pub.cpython-39.opt-2.pyc' )
is_prime_pub    = loader.load_module()

#
# Call a method in the module
#
low_prime       = [2,3]
low_prime      += [x for x in range(5,2047,2) if is_prime_pub.rabin_miller_test(x,b=2,rounds=1)]
print( is_prime_pub.is_prime( 59, low_prime, 5 ) )
```

load\_module()已废弃，不建议使用，会有警告，但在Python 3.9.0中仍可用

```
DeprecationWarning: the load_module() method is deprecated and slated for removal in Python 3.12; use exec_module() instead
```

不要问为何有此需求

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

青衣十三楼飞花堂

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过