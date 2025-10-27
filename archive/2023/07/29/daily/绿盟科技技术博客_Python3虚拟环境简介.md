---
title: Python3虚拟环境简介
url: http://blog.nsfocus.net/python3/
source: 绿盟科技技术博客
date: 2023-07-29
fetch_date: 2025-10-04T11:53:52.749102
---

# Python3虚拟环境简介

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

# Python3虚拟环境简介

### Python3虚拟环境简介

[2023-07-28](https://blog.nsfocus.net/python3/ "Python3虚拟环境简介")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")

阅读： 1,303

## 一、最简用法

参[1]，以Linux中Python 3.10.6为例，不考虑Windows环境，后者有便携版方案，不需要本文技术方案。低版本Python3不支持本文演示的某些参数，以相应版本官方文档为准。

python3 -m venv /home/scz/src/Python3Venv

这将创建名为Python3Venv的子目录，有”mkdir -p”的效果，沿线目录不存在时自动创建。

进入虚拟环境:

source /home/scz/src/Python3Venv/bin/activate

退出虚拟环境:

deactivate

删除虚拟环境:

rm -rf /home/scz/src/Python3Venv

在虚拟环境中pip安装模块，局限于其中，不影响外部环境。反过来，本小节创建的虚拟环境看不到外部环境安装的模块，只有缺省模块(pip、setuptools)。

后续操作假设已在虚拟环境中

$ python3 -m pip list
Package Version
———- ——-
pip 22.0.2
setuptools 59.6.0

升级这几个模块

python3 -m pip install –upgrade pip setuptools

$ pip3 list
Package Version
———- ——-
pip 23.2.1
setuptools 68.0.0

这几个模块在虚拟环境中:

$ python3 -m pip show pip | grep Location
Location: /home/scz/src/Python3Venv/lib/python3.10/site-packages

$ python3 -c “import pip;print(pip.\_\_file\_\_)”
/home/scz/src/Python3Venv/lib/python3.10/site-packages/pip/\_\_init\_\_.py

$ python3 -c “import sys;print(sys.path)”
[”, ‘/usr/lib/python310.zip’, ‘/usr/lib/python3.10’, ‘/usr/lib/python3.10/lib-dynload’, ‘/home/scz/src/Python3Venv/lib/python3.10/site-packages’]

虚拟环境的要点是sys.path，在虚拟环境中pip安装的模块位于:

/home/scz/src/Python3Venv/lib/python3.10/site-packages

Python3虚拟环境主要处理sys.path，对文件系统没有虚拟化，与chroot无关，不要假设这是沙箱。

1) 判断当前Python环境是否为虚拟环境

activate之后，有个明显的前导提示符，表示位于虚拟环境中。此外，有个环境变量被设置:

$ echo $VIRTUAL\_ENV
$ python3 -c “import os;print(os.getenv(‘VIRTUAL\_ENV’))”
/home/scz/src/Python3Venv

若想在some.py中判断是否为虚拟环境，用下列技术方案:

python3 -c “import sys;print(sys.prefix);print(sys.exec\_prefix);print(sys.base\_prefix);print(sys.prefix!=sys.base\_prefix)”

假设在虚拟环境中，上述命令输出

/home/scz/src/Python3Venv
/home/scz/src/Python3Venv
/usr
True

假设在外部环境中，上述命令输出

/usr
/usr
/usr
False

显示True时在虚拟环境中，原理是虚拟环境的sys.prefix不同于sys.base\_prefix。

2) 并非必须用activate进入虚拟环境

为进入虚拟环境，可以不用activate脚本，直接执行虚拟环境中的Python3解释器即可。

$ /home/scz/src/Python3Venv/bin/python3 -c “import sys;print(sys.prefix);print(sys.exec\_prefix);print(sys.base\_prefix);print(sys.prefix!=sys.base\_prefix)”
/home/scz/src/Python3Venv
/home/scz/src/Python3Venv
/usr
True

此法不会设置VIRTUAL\_ENV环境变量:

$ /home/scz/src/Python3Venv/bin/python3 -c “import os;print(os.getenv(‘VIRTUAL\_ENV’))”
None

故，若VIRTUAL\_ENV有值，在虚拟环境中；若VIRTUAL\_ENV无值，无法判断在何种环境中。还是”sys.prefix!=sys.base\_prefix”靠谱。

## 二、从虚拟环境访问外部环境安装的模块

有时出于各种原因，想从虚拟环境访问外部环境安装的模块，比如为了节省空间。这是可行的，下面分述几种方案。

1) 手工调整虚拟环境sys.path

假设已按「最简用法」创建虚拟环境，缺省无法从虚拟环境访问外部环境安装的模块。为达目的，手工调整虚拟环境sys.path即可。

后续操作假设已在虚拟环境中

python3
import sys
sys.path.extend([‘/home/scz/.local/lib/python3.10/site-packages’, ‘/usr/local/lib/python3.10/dist-packages’, ‘/usr/lib/python3/dist-packages’])
print(sys.path)
import hexdump
print(hexdump.\_\_file\_\_)

顺利的话，最后一行代码输出:

/usr/local/lib/python3.10/dist-packages/hexdump.py

若未调整sys.path，导入hexdump模块失败。

2) pyvenv.cfg

vi /home/scz/src/Python3Venv/pyvenv.cfg

「最简用法」生成的该文件内容如下:

————————————————————————–
home = /usr/bin
include-system-site-packages = false
version = 3.10.6
————————————————————————–

将其中的false改成true:

————————————————————————–
home = /usr/bin
#include-system-site-packages = false
include-system-site-packages = true
version = 3.10.6
————————————————————————–

重新进入Python3解释器，sys.path已自动调整成:

[”, ‘/usr/lib/python310.zip’, ‘/usr/lib/python3.10’, ‘/usr/lib/python3.10/lib-dynload’, ‘/home/scz/src/Python3Venv/lib/python3.10/site-packages’, ‘/home/scz/.local/lib/python3.10/site-packages’, ‘/usr/local/lib/python3.10/dist-packages’, ‘/usr/lib/python3/dist-packages’]

编辑pyvenv.cfg与是否在activate状态无关。

3) 创建虚拟环境时使用特殊参数

python3 -m venv –system-site-packages –symlinks –upgrade-deps –prompt Virtual /home/scz/src/Python3Venv

————————————————————————–
–system-site-packages

让pyvenv.cfg中出现”include-system-site-packages = true”

–symlinks

虚拟化时尽可能使用符号链接，对于Linux这是缺省选择

–upgrade-deps

创建虚拟环境时自动升级pip、setuptools模块，这是3.9开始支持的参数

–prompt Virtual

就上例而言，若不指定该参数，进入虚拟环境后前导提示符是(Python3Venv)，若指定该参数，进入虚拟环境后前导提示符是(Virtual)
————————————————————————–

参考资源

[1] Creation of virtual environments https://docs.python.org/3/library/venv.html

[2] Virtual Environments and Package https://docs.python.org/3/tutorial/venv.html

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/metaverse/)

[Next](https://blog.nsfocus.net/smartbi-4/)

### Meet The Author

scz

C/ASM程序员

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)