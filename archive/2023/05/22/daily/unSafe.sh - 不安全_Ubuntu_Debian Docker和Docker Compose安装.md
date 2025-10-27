---
title: Ubuntu/Debian Docker和Docker Compose安装
url: https://buaq.net/go-164987.html
source: unSafe.sh - 不安全
date: 2023-05-22
fetch_date: 2025-10-04T11:36:55.182093
---

# Ubuntu/Debian Docker和Docker Compose安装

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

![](https://8aqnet.cdn.bcebos.com/38b6715423740666bd31680be440de7e.jpg)

Ubuntu/Debian Docker和Docker Compose安装

一、Docker安装步骤以下安装步骤使用的是Ubuntu 20.04操作系统。（必须是在root用户下进行）1、更新系统组件及安装必要软件
*2023-5-21 22:7:42
Author: [blog.upx8.com(查看原文)](/jump-164987.htm)
阅读量:39
收藏*

---

## 一、Docker安装步骤

* 以下安装步骤使用的是Ubuntu 20.04操作系统。（必须是在root用户下进行）

### 1、更新系统组件及安装必要软件

```
 apt-get update -y && apt-get upgrade -y
 apt install curl socat wget sudo iptables vim -y
```

### 2、安装Docker

```
 sudo apt install docker.io -y
```

### 3、启动Docker服务

```
 systemctl restart docker
```

#### 验证Docker是否安装成功

```
 docker --version
```

##### 显示Docker version XXXX则为安装成功

![](https://img.imgdd.com/f210f3.10845773-ff8e-4874-86c5-5a6575a1ee01.png)

文章来源: https://blog.upx8.com/3569
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)