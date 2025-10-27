---
title: Linux删除大文件后磁盘空间未释放问题
url: https://blog.upx8.com/3378
source: 黑海洋 - WIKI
date: 2023-03-30
fetch_date: 2025-10-04T11:07:49.037090
---

# Linux删除大文件后磁盘空间未释放问题

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux删除大文件后磁盘空间未释放问题

发布时间:
2023-03-29

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
16746

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
[root@i-3E5C86C8 ~]# df -h
Filesystem         Size  Used Avail Use% Mounted on
/dev/vda3           51G   34G   15G  70% /
tmpfs              7.8G     0  7.8G   0% /dev/shm
/dev/vda1          190M   38M  143M  21% /boot
/dev/mapper/vg-lv   92G  597M   87G   1% /disk1
You have new mail in /var/spool/mail/root
[root@i-3E5C86C8 ~]#
```

使用命令：du -sh \*，查看当前所在目录的各子目录磁盘空间占用情况

bash

```
[root@i-3E5C86C8 /]# du -sh *    #该命令可以列出当前所在目录的子目录所占空间大小
7.8M    bin
36M    boot
4.0K    cgroup
4.0K    Hello
```

依此类推，可以找到一些无用的大文件进行删除，删除后发现磁盘空间未释放，使用命令：**lsof | grep delete**

bash

```
[root@i-3E5C86C8 cloud]# lsof | grep delete
java       2873      root    1w      REG              252,3 6392907748    1575685 /home/cloud/test/nohup.out (deleted)
java       2873      root    2w      REG              252,3 6392907748    1575685 /home/cloud/test/nohup.out (deleted)
java       2873      root   53u      REG              252,3          0    1704161 /home/cloud/test/file:/home/cloud/test/test.jar!/BOOT-INF/classes!/flume/run/data/in_use.lock (deleted)
java       2873      root  185r      REG              252,3 1623704364    1704176 /home/cloud/test/file:/home/cloud/test/test.jar!/BOOT-INF/classes!/flume/run/data/log-14 (deleted)
java       2873      root  187u      REG              252,3 1147833050    1704194 /home/cloud/test/file:/home/cloud/test/test.jar!/BOOT-INF/classes!/flume/run/data/log-15 (deleted)
java       2873      root  262r      REG              252,3 1147833050    1704194 /home/cloud/test/file:/home/cloud/test/test.jar!/BOOT-INF/classes!/flume/run/data/log-15 (deleted)
[root@i-3E5C86C8 cloud]#
```

找到相应的进程号，删除即可。

bash

```
sudo kill -9 pid
```

[取消回复](https://blog.upx8.com/3378#respond-post-3378)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")