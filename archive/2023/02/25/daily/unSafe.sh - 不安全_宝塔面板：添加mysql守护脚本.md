---
title: 宝塔面板：添加mysql守护脚本
url: https://buaq.net/go-150907.html
source: unSafe.sh - 不安全
date: 2023-02-25
fetch_date: 2025-10-04T08:02:37.926618
---

# 宝塔面板：添加mysql守护脚本

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

![](https://8aqnet.cdn.bcebos.com/24f2069c073d2b1ba7a50efc16fc7c88.jpg)

宝塔面板：添加mysql守护脚本

云服务器安装的宝塔面板，因为内存经常不足导致宝塔面板mysql经常停止，需要检测mysql进程是否停止，就像php守护程序一样，检测到mysql 进程禁
*2023-2-24 22:18:39
Author: [blog.upx8.com(查看原文)](/jump-150907.htm)
阅读量:26
收藏*

---

云服务器安装的宝塔面板，因为内存经常不足导致宝塔面板mysql经常停止，需要检测mysql进程是否停止，就像php守护程序一样，检测到mysql 进程禁止后，检测到mysql停止会自动启动。

## Mysql进程守护脚本 shell脚本一：

```
pgrep -x mysqld &> /dev/null
if [ $? -ne 0 ];then
        bash /www/server/panel/script/rememory.sh
        /etc/init.d/mysqld start
fi
```

## Mysql进程守护脚本 shell脚本二：

```
#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
pgrep -x mysqld &> /dev/null
if [ $? -ne 0 ]
then
echo "At time:$(date) :MySQL is stop .">> /var/log/mysql_messages
/etc/init.d/mysqld start
else
exit
fi
```

1、登录宝塔面板 >> 计划任务 >> 添加定时脚本

[![自动草稿](https://www.xpn.cc/wp-content/uploads/2022/11/52420a4b5a13ade.png "自动草稿")](https://www.xpn.cc/wp-content/uploads/2022/11/52420a4b5a13ade.png)

2、手动停止mysql后，执行守护脚本，确认可以正常启动mysql

[![自动草稿](https://www.xpn.cc/wp-content/uploads/2022/11/6e71e1d00a18e95.jpeg "自动草稿")](https://www.xpn.cc/wp-content/uploads/2022/11/6e71e1d00a18e95.jpeg)

文章来源: https://blog.upx8.com/3241
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)