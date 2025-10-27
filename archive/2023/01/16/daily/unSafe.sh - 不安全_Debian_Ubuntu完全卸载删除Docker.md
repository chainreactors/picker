---
title: Debian/Ubuntu完全卸载删除Docker
url: https://buaq.net/go-145610.html
source: unSafe.sh - 不安全
date: 2023-01-16
fetch_date: 2025-10-04T03:58:44.723600
---

# Debian/Ubuntu完全卸载删除Docker

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

Debian/Ubuntu完全卸载删除Docker

卸载Docker，同时删除Docker镜像、容器、数据卷等文件。Docker自17.03版本开始分为两个版本Docker CE和Docker EE：D
*2023-1-15 14:59:0
Author: [blog.upx8.com(查看原文)](/jump-145610.htm)
阅读量:33
收藏*

---

卸载Docker，同时删除Docker镜像、容器、数据卷等文件。

Docker自17.03版本开始分为两个版本Docker CE和Docker EE：

* Docker CE：Docker Community Edition，即Docker社区版
* Docker EE：即Docker Enterprise Edition，即Docker企业版。

卸载Docker的命令如下：

```
sudo apt-get purge docker-ce

sudo apt-get purge docker-ee

sudo rm -rf /var/lib/docker
```

在完成这些操作之后，运行以下命令检查系统中是否还存在docker文件：

```
sudo find / -name '*docker*'
```

可能仍然存在一些docker文件。这个时候，你可以执行一下删除方式，再次进行卸载。

删除安装时自动安装的所有包

```
sudo apt-get autoremove docker docker-ce docker-engine docker.io containerd runc
```

查看删除docker其他有没有没有卸载干净的包

```
dpkg -l | grep docker
```

卸载相应的包

```
sudo apt-get autoremove docker-ce-*
```

删除docker的相关配置&目录

```
sudo rm -rf /etc/systemd/system/docker.service.d
sudo rm -rf /var/lib/docker
sudo rm /etc/apparmor.d/docker
sudo groupdel docker
sudo rm -rf /var/run/docker.sock
```

确定docker卸载完毕

```
docker --version
```

确定docker卸载完毕

最后可以再执行一遍检查：

```
sudo find / -name "*docker*" -exec `rm -rf` {} +
```

删除所有相关文件即可。

文章来源: https://blog.upx8.com/3189
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)