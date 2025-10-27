---
title: Centos 7 安装PyMuPDF
url: https://h4ck.org.cn/2024/08/17870
source: obaby@mars
date: 2024-08-22
fetch_date: 2025-10-06T18:01:27.655599
---

# Centos 7 安装PyMuPDF

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[Linux『Linux』](https://h4ck.org.cn/cats/xtxg/linux%E3%80%8Elinux%E3%80%8F)

# Centos 7 安装PyMuPDF

2024年8月21日
[33 条评论](https://h4ck.org.cn/2024/08/17870#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/WechatIMG1090.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/WechatIMG1090.jpg)

接引前文，昨天把代码写好测试 ok 之后，以为就万事大吉了。然而，今天往服务器上部署的时候，直接给整麻了。问题一个接一个，错误一堆接一堆。直接让人破防了。

对于 linux 的发行版，我并~~没有~~神马偏见，主要是用过的版本也不多，但是，不得不说那个 centos 是真烂，也不知道为啥那么多人喜欢用这个破系统。

直接 pip 安装，好嘛，这一堆错误：

```
[root@iZbp12k4fwg2euy5kkr9u7Z ~]# pip install PyMuPDF
Looking in indexes: http://mirrors.cloud.aliyuncs.com/pypi/simple/
Collecting PyMuPDF
  Using cached http://mirrors.cloud.aliyuncs.com/pypi/packages/9f/1d/032d24e0c774e67742395fda163a172c60e4d0f9875785d5199eb2956d5e/PyMuPDF-1.19.6.tar.gz (2.3 MB)
  Preparing metadata (setup.py) ... done
Using legacy 'setup.py install' for PyMuPDF, since package 'wheel' is not installed.
Installing collected packages: PyMuPDF
    Running setup.py install for PyMuPDF ... error
    ERROR: Command errored out with exit status 1:
     command: /usr/bin/python3 -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-8aqc9a1k/pymupdf_d5ebd12caf9445ab82d6a5af68229d72/setup.py'"'"'; __file__='"'"'/tmp/pip-install-8aqc9a1k/pymupdf_d5ebd12caf9445ab82d6a5af68229d72/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /tmp/pip-record-7fhkepkr/install-record.txt --single-version-externally-managed --compile --install-headers /usr/local/include/python3.6m/PyMuPDF
         cwd: /tmp/pip-install-8aqc9a1k/pymupdf_d5ebd12caf9445ab82d6a5af68229d72/
    Complete output (20 lines):
    running install
    running build
    running build_py
    creating build
    creating build/lib.linux-x86_64-3.6
    creating build/lib.linux-x86_64-3.6/fitz
    copying fitz/__init__.py -> build/lib.linux-x86_64-3.6/fitz
    copying fitz/fitz.py -> build/lib.linux-x86_64-3.6/fitz
    copying fitz/utils.py -> build/lib.linux-x86_64-3.6/fitz
    copying fitz/__main__.py -> build/lib.linux-x86_64-3.6/fitz
    running build_ext
    building 'fitz._fitz' extension
    creating build/temp.linux-x86_64-3.6
    creating build/temp.linux-x86_64-3.6/fitz
    gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -fPIC -I/usr/include/mupdf -I/usr/local/include/mupdf -Imupdf/thirdparty/freetype/include -I/usr/include/freetype2 -I/usr/include/python3.6m -c fitz/fitz_wrap.c -o build/temp.linux-x86_64-3.6/fitz/fitz_wrap.o
    fitz/fitz_wrap.c:2755:18: fatal error: fitz.h: No such file or directory
     #include <fitz.h>
                      ^
    compilation terminated.
    error: command 'gcc' failed with exit status 1
    ----------------------------------------
ERROR: Command errored out with exit status 1: /usr/bin/python3 -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-8aqc9a1k/pymupdf_d5ebd12caf9445ab82d6a5af68229d72/setup.py'"'"'; __file__='"'"'/tmp/pip-install-8aqc9a1k/pymupdf_d5ebd12caf9445ab82d6a5af68229d72/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /tmp/pip-record-7fhkepkr/install-record.txt --single-version-externally-managed --compile --install-headers /usr/local/include/python3.6m/PyMuPDF Check the logs for full command output.
```

按照提示看来是 gcc 报错了，错误原因是没有头文件，一通搜索：https://blog.csdn.net/u012140499/article/details/112798704 提供了解决思路，下载源码https://casper.mupdf.com/releases/安装。

直接下载最新版编译，又是一堆报错：

```
source/fitz/util.c: In function ‘fz_new_xhtml_document_from_document’:
source/fitz/util.c:866:2: warning: ‘new_doc’ may be used uninitialized in this function [-Wmaybe-uninitialized]
  return new_doc;
  ^
    CC build/release/source/fitz/warp.o
    CC build/release/source/fitz/writer.o
source/fitz/writer.c: In function ‘fz_new_document_writer_with_buffer’:
source/fitz/writer.c:305:2: warning: ‘wri’ may be used uninitialized in this function [-Wmaybe-uninitialized]
  return wri;
  ^
    CC build/release/source/fitz/xml.o
    CC build/release/source/fitz/xmltext-device.o
    CC build/release/source/fitz/zip.o
    CXX build/release/source/fitz/tessocr.o
/bin/sh: g++: command not found
make: *** [build/release/source/fitz/tessocr.o] Error 127
```

提示找不到 g++，嗯，再来解决 g++

```
yum search "gcc-c++"
```

就一个结果：

```
oaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.cloud.aliyuncs.com
 * extras: mirrors.cloud.aliyuncs.com
 * updates: mirrors.cloud.aliyuncs.com
======================================================================================================= N/S matched: gcc-c++ =======================================================================================================
gcc-c++.x86_64 : C++ support for GCC

  Name and summary matches only, use "search all" for everything.
```

安装 g++：

```
[root@iZbp12k4fwg2euy5kkr9u7Z mupdf-1.22.0-source]# yum install "gcc-c++.x86_64" -y
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.cloud.aliyuncs.com
 * extras: mirrors.cloud.aliyuncs.com
 * updates: mirrors.cloud.aliyuncs.com
Resolving Dependencies
--> Running transaction check
---> Package gcc-c++.x86_64 0:4.8.5-44.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

====================================================================================================================================================================================================================================
 Package                                                Arch                                                  Version                                                     Repository                                           Size
====================================================================================================================================================================================================================================
Installing:
 gcc-c++                                                x86_64                                                4.8.5-44.el7                                                base                                                7.2 M

Transaction Summary
====================================================================================================================================================================================================================================
Install  1 Package

Total download size: 7.2 M
Installed size: 16 M
Downloading packages:
gcc-c++-4.8.5-44.el7.x86_64.rpm                                                                                                                             ...