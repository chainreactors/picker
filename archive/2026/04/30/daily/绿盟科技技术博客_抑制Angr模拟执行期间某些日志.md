---
title: 抑制Angr模拟执行期间某些日志
url: https://blog.nsfocus.net/%e6%8a%91%e5%88%b6angr%e6%a8%a1%e6%8b%9f%e6%89%a7%e8%a1%8c%e6%9c%9f%e9%97%b4%e6%9f%90%e4%ba%9b%e6%97%a5%e5%bf%97/
source: 绿盟科技技术博客
date: 2026-04-30
fetch_date: 2026-05-01T05:38:17.473959
---

# 抑制Angr模拟执行期间某些日志

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

# 抑制Angr模拟执行期间某些日志

### 抑制Angr模拟执行期间某些日志

[2026-04-30](https://blog.nsfocus.net/%E6%8A%91%E5%88%B6angr%E6%A8%A1%E6%8B%9F%E6%89%A7%E8%A1%8C%E6%9C%9F%E9%97%B4%E6%9F%90%E4%BA%9B%E6%97%A5%E5%BF%97/ "抑制Angr模拟执行期间某些日志")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 25

### Q:某Angr脚本中有如下代码片段

logging.getLogger( ‘angr’ ).setLevel( logging.ERROR )
logging.getLogger( ‘angr.project’ ).setLevel( logging.ERROR )
logging.getLogger( ‘angr.sim\_manager’ ).setLevel( logging.ERROR )
logging.getLogger( ‘angr.engines.successors’ ).setLevel( logging.ERROR )

这些主要用于抑制Angr模拟执行期间某些INFO级别的日志输出。在具体实践中，即使
已启用上述代码，仍有其他日志输出，比如

[INFO] Mapping cle##tls at 0x900000 (loader:\_map\_object)
[INFO] Created extern symbol for dlsym (\_\_init\_\_:make\_extern)
[INFO] no PT\_LOAD segments identified (elf:\_\_init\_\_)

想抑制它们，如何下手？

### A:可在Python的site-packages目录下查看相关目录，比如

angr
archinfo
bitarray
bitstring
cachetools
capstone
cart
cffi
claripy
cle
Crypto
cxxheaderparser
elftools
keystone
msgspec
networkx
ordlookup
psutil
pycparser
pydemumble
pypcode
pyvex
rich
setuptools
sortedcontainers
unicorn
z3

当时用”pip3 install angr”安装的，不知装了这么多依赖模块。这次先看angr子目
录的修改时间，再获取修改时间与之精确匹配的所有子目录名，得到上述列表。

powershell -Command “$t=[datetime]’2026-01-19 13:49′; Get-ChildItem -Directory | Where-Object { $\_.LastWriteTime -ge $t -and $\_.LastWriteTime -lt $t.AddMinutes(1) } | ForEach-Object { $\_.Name }”

这些目录下的py中可能含有这种代码片段

l = logging.getLogger(name=\_\_name\_\_)
log = logging.getLogger(name=\_\_name\_\_)

用下列方式输出日志

l.info(“Using builtin SimProcedure for %s from %s”, …)
log.info(“Created extern symbol for %s”, name)

这是INFO级别的日志，其他级别的有相应函数，比如

log.debug
log.warning
log.error

### 接下来处理具体案例

### 案例1

[INFO] Mapping cle##tls at 0x900000 (loader:\_map\_object)

这种，大概率有格式串，合理猜测有行代码会出现

.info(“Mapping

然后”Find in files”，找到

cle\loader.py
def \_map\_object
log.info(“Mapping %s at %#x”, obj.binary, base\_addr)

没看明白实际日志中”(loader:\_map\_object)”是怎么加进去的，可能是log.info取调
用栈回溯信息，加上去的。这提示我们，下次看到这种日志，搜lorder.py，搜
\_map\_object函数。

现在可知抑制上述日志的代码

logging.getLogger( ‘cle.loader’ ).setLevel( logging.ERROR )

### 案例2

[INFO] Created extern symbol for dlsym (\_\_init\_\_:make\_extern)

从案例1的经验中可知，去找某个\_\_init\_\_.py中的make\_extern函数

cle\backends\externs\\_\_init\_\_.py
def make\_extern
log.info(“Created extern symbol for %s”, name)

抑制方案

logging.getLogger( ‘cle.backends.externs’ ).setLevel( logging.ERROR )

### 案例3

[INFO] no PT\_LOAD segments identified (elf:\_\_init\_\_)

去找elf.py中的\_\_init\_\_函数

cle\backends\elf\elf.py
class ELF
def \_\_init\_\_
log.info(“no PT\_LOAD segments identified”)

抑制方案

logging.getLogger( ‘cle.backends.elf.elf’ ).setLevel( logging.ERROR )

楞搜特征字符串时，要注意格式串的可能形式，避免漏报。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/waf%E9%98%B2%E7%BA%BF%E5%91%8A%E6%80%A5%EF%BC%9F%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E5%B7%B2%E6%8F%90%E5%89%8D%E9%94%81%E5%AE%9A%E5%B9%BD%E7%81%B5%E6%AF%94%E7%89%B9%E4%BD%8D/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)