---
title: Ubuntu 22中找不到libcrypto.so.1.1
url: https://mp.weixin.qq.com/s/oSTBkL9GbSY_ixtGXRjXcw
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:26:12.581967
---

# Ubuntu 22中找不到libcrypto.so.1.1

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h56Z2h4w7JkITYFVOmGicZtMl85NZhTxN2HzQbpNxXPNHq8NV9HvRsSWIvMNric9fS8mybzIDeXj6uh3ST1ibt2gJ4cgA13nAXP4YgrFwhA4V0/0?wx_fmt=jpeg)

# Ubuntu 22中找不到libcrypto.so.1.1

原创

沈沉舟
沈沉舟

青衣十三楼飞花堂

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

16.31 Ubuntu 22中找不到libcrypto.so.1.1

```
https://scz.617.cn/unix/202604291930.txt
```

Q:

当前系统是Ubuntu 22。执行wasm2c 1.0.36时，提示找不到libcrypto.so.1.1。用ldd查看，确实找不到。

```
$ ldd /path/wabt-1.0.36/bin/wasm2c
        libcrypto.so.1.1 => not found
```

但之前wasm2c 1.0.34无此问题。

A:

参看

```
Ubuntu的旧版OpenSSL
https://nz2.archive.ubuntu.com/ubuntu/pool/main/o/openssl/

OpenSSL源码
https://openssl-library.org/source/old/index.html
https://openssl-library.org/source/old/1.1.1/
```

wasm2c 1.0.36用到libcrypto.so.1.1，而Ubuntu 22用OpenSSL 3.0。

```
$ ls -l /usr/lib/x86_64-linux-gnu/libcrypto.so*
lrwxrwxrwx 1 root root      14 Feb  7  2023 /usr/lib/x86_64-linux-gnu/libcrypto.so -> libcrypto.so.3
-rw-r--r-- 1 root root 4451632 Feb  7  2023 /usr/lib/x86_64-linux-gnu/libcrypto.so.3
```

---

```
$ dpkg -S /usr/lib/x86_64-linux-gnu/libcrypto.so.3
libssl3:amd64: /usr/lib/x86_64-linux-gnu/libcrypto.so.3
```

---

```
$ apt-cache search libssl3
libssl3 - Secure Sockets Layer toolkit - shared libraries
```

---

```
$ apt-cache search libssl1
(无输出)
```

Ubuntu 22已无法正常安装libssl1。有人手工下载旧版libssl1.1\*.deb，再dpkg安装。比如

```
wget https://nz2.archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb
dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb
```

用dpkg安装旧版，太野了，并不推荐。较文明的办法是下载低版本OpenSSL源码，自己编译低版本，并设置环境变量。比如

```
mkdir /somepath
cd /somepath
wget https://www.openssl.org/source/openssl-1.1.1w.tar.gz
tar xvfz openssl-1.1.1w.tar.gz
cd openssl-1.1.1w
./config
make
mkdir /somepath/lib
cp /somepath/openssl-1.1.1w/libcrypto.so.1.1 /somepath/lib/
cp /somepath/openssl-1.1.1w/libssl.so.1.1 /somepath/lib/
export LD_LIBRARY_PATH=/somepath/lib:$LD_LIBRARY_PATH
```

前述几种办法我都没采用，因为Ubuntu 22的snap机制可能有libssl1，复用之。

```
$ ls -l /snap/core20/current/usr/lib/x86_64-linux-gnu/libcrypto.so*
-rw-r--r-- 1 root root 2954080 May 25  2023 /snap/core20/current/usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
```

---

```
$ ldd /snap/core20/current/usr/lib/x86_64-linux-gnu/libcrypto.so*
(略)
```

---

```
$ ln -s /snap/core20/current/usr/lib/x86_64-linux-gnu/libcrypto.so.1.1 /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
```

---

```
$ /path/wabt-1.0.36/bin/wasm2c --version
1.0.36
```

---

```
$ ldd /path/wabt-1.0.36/bin/wasm2c
(略)
```

---

AI时代，这些笔记已毫无意义，只是习惯性折腾过就记一笔而已。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPOa7YUszQ2zP2AFStE4UScicKMwhEqpde0j0FEheXVmbxSG8JFKDG3K8piaJjMHLjicL5zKemTibjvuQg/0?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPOa7YUszQ2zP2AFStE4UScicKMwhEqpde0j0FEheXVmbxSG8JFKDG3K8piaJjMHLjicL5zKemTibjvuQg/0?wx_fmt=png)

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