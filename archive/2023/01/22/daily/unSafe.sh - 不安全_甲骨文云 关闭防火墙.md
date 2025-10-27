---
title: 甲骨文云 关闭防火墙
url: https://buaq.net/go-146459.html
source: unSafe.sh - 不安全
date: 2023-01-22
fetch_date: 2025-10-04T04:32:21.636124
---

# 甲骨文云 关闭防火墙

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

甲骨文云 关闭防火墙

彻底删除防火墙甲骨文云提供的系统镜像开启了系统防火墙，为了方便使用通常会先关闭防火墙。命令如下：# centosyum remove iptables
*2023-1-21 23:39:53
Author: [blog.upx8.com(查看原文)](/jump-146459.htm)
阅读量:21
收藏*

---

## 彻底删除防火墙

甲骨文云提供的系统镜像开启了系统防火墙，为了方便使用通常会先关闭防火墙。

命令如下：

```
# centos
yum remove iptables* netfilter-persistent* -y

# ubuntu
apt autoremove iptables* netfilter-persistent* -y
```

## 放行所有端口

如何直接删除iptables会导致某些服务无法使用，例如CF的一键脚本等无法获取到ipv4的ip，因此更建议使用下面的方式。

命令如下：

```
# ubuntu
apt autoremove netfilter-persistent* -y
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -F
```

文章来源: https://blog.upx8.com/3195
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)