---
title: Python模块注入技术简析
url: http://blog.nsfocus.net/python-2/
source: 绿盟科技技术博客
date: 2023-04-01
fetch_date: 2025-10-04T11:22:21.131994
---

# Python模块注入技术简析

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

# Python模块注入技术简析

### Python模块注入技术简析

[2023-03-31](https://blog.nsfocus.net/python-2/ "Python模块注入技术简析")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")

阅读： 1,017

有人在推特上提供了一段神奇的Python代码

https://twitter.com/David3141593/status/1640115094255198208

————————————————————————–
unused=b’\x50K\3\4’+b’\0’\*26+b’+(\xca\xcc+\
\xd1P\xcfHL\xceNMQ\xc8\xc9\xcfQ\xd7\4\0PK\1\2’+\
b’\0’\*6+b’\1’+b’\0’\*9+b’\x15’+b’\0’\*7+b’\13’+b’\0’\*17+\
b’\_\_\x6da\x69n\_\_.\x70y\x50K\5\6’+b’\0’\*8+b’9\0\0\0003\0\0\0′
i=\_\_import\_\_
i(“runpy”).run\_path(i(“py\_compile”).compile(\_\_file\_\_))
————————————————————————–

假设将上述代码置入test.py，以Python 3.8及以上版本执行之，输出”hacked lol”。

$ python3 test.py
hacked lol

PoC出场后有两位第一时间揭密

https://twitter.com/AstraKernel/status/1640255265382735873
https://twitter.com/c3rb3ru5d3d53c/status/1640191261435985920

下面是我的分析

PoC执行时，将自身编译成pyc再加载，在此过程中用到了zipimport模块。zipimport模块”意外地”将pyc co\_consts中的unused值识别成zip文件，用\_read\_directory()对其中的\_\_main\_\_.py进行解析，后来又用\_get\_data()返回解压后的\_\_main\_\_.py字节码。最后由runpy.run\_code()执行\_\_main\_\_.py字节码。

David3141593在twitter上提供PoC时，刻意做了些混淆；unused最前面4字节是zip文件的magic number，他故意不以可打印字符显示；unused中部有”\_\_main\_\_.py”，他故意不以可打印字符显示。PoC中unused是个畸形zip文件，作者故意的，实际此处可以是任意有效zip文件。最简方案是，将想执行的代码放入\_\_main\_\_.py，再压缩成zip文件，将zip文件的bytes表示赋给unused变量即可。不过作者后来提了issue，讲了不少细节。

https://github.com/python/cpython/issues/103051

zip文件格式参看

https://en.wikipedia.org/wiki/Zip\_%28file\_format%29

Python 3.10.6的调用栈简介

————————————————————————–
runpy.run\_path(py\_compile.compile(\_\_file\_\_))
importer = pkgutil.get\_importer(path\_name) // runpy.py:279
// 返回zipimporter
importer = path\_hook(path\_item) // pkgutil.py:421
// path\_hook等于zipimport.zipimporter
zipimport.zipimporter.\_\_init\_\_(path\_item) // 处理test.cpython-310.pyc
files = zipimport.\_read\_directory(path) // zipimport.py:95
// zipimport.\_read\_directory()从pyc尾部倒着搜索”PK\5\6″
// 幺蛾子出在zipimport.\_read\_directory()中
code = runpy.\_get\_main\_module\_details() // runpy.py:302
runpy.\_get\_module\_details(“\_\_main\_\_”) // runpy.py:238
code = loader.get\_code(“\_\_main\_\_”) // runpy.py:157
// 调用zipimport.zipimporter.get\_code()
code = zipimport.\_get\_module\_code(self, fullname) // zipimport.py:196
data = zipimport.\_get\_data(self.archive, “\_\_main\_\_”) // zipimport.py:752
// zipimport.\_get\_data()返回解压后的\_\_main\_\_.py
runpy.run\_code(code,…) // runpy.py:306
exec(code,…) // runpy.py:86
\_\_main\_\_.py // test.cpython-310.pyc
————————————————————————–

我这是用gdb调试Python解释器得到的调用栈回溯，实际情况有些微妙，后面是小侯的研究结论。

cpython-3.10.6\Lib\zipimport.py
cpython-3.10.6\Python\importlib\_zipimport.h
cpython-3.10.6\Programs\\_freeze\_importlib.c

\_freeze\_importlib.c将zipimport.py编译成pyc，再序列化到importlib\_zipimport.h，后者内容形如

const unsigned char \_Py\_M\_\_zipimport[] = {99,0,0,0,…,19,12,15,}

Python源码提供zipimport.py，同时也提供预编译好的importlib\_zipimport.h。编译Python源码时，缺省用importlib\_zipimport.h，之后修改zipimport.py并不影响解释器。

参看

cpython-3.10.6\Makefile.pre.in

编译源码时可用如下命令强制重新生成importlib\_zipimport.h

make regen-importlib

这是老版定义frozen module的位置

https://github.com/python/cpython/blob/3.8/Python/frozen.c

————————————————————————–
static const struct \_frozen \_PyImport\_FrozenModules[] = {
/\* importlib \*/
{“\_frozen\_importlib”, \_Py\_M\_\_importlib\_bootstrap,
(int)sizeof(\_Py\_M\_\_importlib\_bootstrap)},
{“\_frozen\_importlib\_external”, \_Py\_M\_\_importlib\_bootstrap\_external,
(int)sizeof(\_Py\_M\_\_importlib\_bootstrap\_external)},
{“zipimport”, \_Py\_M\_\_zipimport,
(int)sizeof(\_Py\_M\_\_zipimport)},
/\* Test module \*/
{“\_\_hello\_\_”, M\_\_\_hello\_\_, SIZE},
/\* Test package (negative size indicates package-ness) \*/
{“\_\_phello\_\_”, M\_\_\_hello\_\_, -SIZE},
{“\_\_phello\_\_.spam”, M\_\_\_hello\_\_, SIZE},
{0, 0, 0} /\* sentinel \*/
};
————————————————————————–

这是新版(3.12.0)定义frozen module的位置

https://github.com/python/cpython/blob/60bdc16b459cf8f7b359c7f87d8ae6c5928147a4/Programs/\_bootstrap\_python.c#L36

————————————————————————–
static const struct \_frozen bootstrap\_modules[] = {
{“\_frozen\_importlib”, \_Py\_M\_\_importlib\_\_bootstrap, (int)sizeof(\_Py\_M\_\_importlib\_\_bootstrap)},
{“\_frozen\_importlib\_external”, \_Py\_M\_\_importlib\_\_bootstrap\_external, (int)sizeof(\_Py\_M\_\_importlib\_\_bootstrap\_external)},
{“zipimport”, \_Py\_M\_\_zipimport, (int)sizeof(\_Py\_M\_\_zipimport)},
{0, 0, 0} /\* bootstrap sentinel \*/
};
————————————————————————–

搞清楚原理后，可以自制这样的PoC，放一个正常zip到unused变量即可，也可以放畸型的，比如hello.py。

————————————————————————–
unused=b’PK\3\4’+b’\0’\*26+\
b’+(\xca\xcc+\xd1P\xf7H\xcd\xc9\xc9W\x08\xcf/\xcaIQT\xd7\4\0PK\1\2’+\
b’\0’\*6+b’\1’+b’\0’\*9+b’\x17’+b’\0’\*7+b’\v’+b’\0’\*17+b’\_\_main\_\_.py’+\
b’PK\5\6’+b’\0’\*8+b’9’+b’\0’\*3+b’5’+b’\0’\*3
i=\_\_import\_\_
i(“runpy”).run\_path(i(“py\_compile”).compile(\_\_file\_\_))
————————————————————————–

$ python3 hello.py
Hello World!

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/sudocve-2023-22809/)

[Next](https://blog.nsfocus.net/%E4%BA%91%E5%AE%89%E5%85%A8%E6%8A%80%E6%9C%AF%E5%8F%82%E8%80%83%E6%9E%B6%E6%9E%84%EF%BC%88%E7%AC%AC%E4%BA%8C%E7%89%88%EF%BC%89%EF%BC%88%E4%B8%8A%EF%BC%89/)

### Meet The Author

scz

C/ASM程序员

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)