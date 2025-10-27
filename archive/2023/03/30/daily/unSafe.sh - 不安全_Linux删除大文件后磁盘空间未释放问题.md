---
title: Linux删除大文件后磁盘空间未释放问题
url: https://buaq.net/go-155960.html
source: unSafe.sh - 不安全
date: 2023-03-30
fetch_date: 2025-10-04T11:06:00.606309
---

# Linux删除大文件后磁盘空间未释放问题

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Linux删除大文件后磁盘空间未释放问题

前言工作中经常遇到Linux系统磁盘空间不足，但是删除后较大的日志文件后，发现磁盘空间仍没有被释放，有点摸不着头脑，今天博主带大家解决这个问题。思路1、
*2023-3-29 20:27:43
Author: [blog.upx8.com(查看原文)](/jump-155960.htm)
阅读量:34
收藏*

---

前言

工作中经常遇到Linux系统磁盘空间不足，但是删除后较大的日志文件后，发现磁盘空间仍没有被释放，有点摸不着头脑，今天博主带大家解决这个问题。

思路

1、工作发现磁盘空间不足；

2、找到占用磁盘空间较大的文件进行删除；

3、删除文件后，查看磁盘空间使用情况，未释放；

4、找到相应delete进程，杀掉即可，问题解决。

具体操作

**查看服务器磁盘空间使用情况**

bash

```
[[email protected] ~]
Filesystem         Size  Used Avail Use% Mounted on
/dev/vda3           51G   34G   15G  70% /
tmpfs              7.8G     0  7.8G   0% /dev/shm
/dev/vda1          190M   38M  143M  21% /boot
/dev/mapper/vg-lv   92G  597M   87G   1% /disk1
You have new mail in /var/spool/mail/root
[[email protected] ~]
```

使用命令：du -sh \*，查看当前所在目录的各子目录磁盘空间占用情况

bash

```
[[email protected] /]
7.8M    bin
36M    boot
4.0K    cgroup
4.0K    Hello
```

依此类推，可以找到一些无用的大文件进行删除，删除后发现磁盘空间未释放，使用命令：**lsof | grep delete**

bash

```
[[email protected] cloud]
java       2873      root    1w      REG              252,3 6392907748    1575685 /home/cloud/test/nohup.out (deleted)
java       2873      root    2w      REG              252,3 6392907748    1575685 /home/cloud/test/nohup.out (deleted)
java       2873      root   53u      REG              252,3          0    1704161 /home/cloud/test/file:/home/cloud/test/test.jar!/BOOT-INF/classes!/flume/run/data/in_use.lock (deleted)
java       2873      root  185r      REG              252,3 1623704364    1704176 /home/cloud/test/file:/home/cloud/test/test.jar!/BOOT-INF/classes!/flume/run/data/log-14 (deleted)
java       2873      root  187u      REG              252,3 1147833050    1704194 /home/cloud/test/file:/home/cloud/test/test.jar!/BOOT-INF/classes!/flume/run/data/log-15 (deleted)
java       2873      root  262r      REG              252,3 1147833050    1704194 /home/cloud/test/file:/home/cloud/test/test.jar!/BOOT-INF/classes!/flume/run/data/log-15 (deleted)
[[email protected] cloud]
```

找到相应的进程号，删除即可。

bash

```
sudo kill -9 pid
```

文章来源: https://blog.upx8.com/3378
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)