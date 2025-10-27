---
title: Ubuntu 安装 XanMod 内核
url: https://buaq.net/go-173208.html
source: unSafe.sh - 不安全
date: 2023-07-30
fetch_date: 2025-10-04T11:50:58.675664
---

# Ubuntu 安装 XanMod 内核

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

Ubuntu 安装 XanMod 内核

XanMod是一个通用的Linux内核发行版，具有自定义设置和新功能。旨在提供稳定、响应迅速且流畅的桌面体验。提供响应迅速且流畅的桌面体验，尤其是对于新
*2023-7-29 22:36:0
Author: [blog.upx8.com(查看原文)](/jump-173208.htm)
阅读量:22
收藏*

---

**![](https://loukas.cn/wp-content/uploads/2022/03/image.png)**

**XanMod**是一个通用的Linux内核发行版，具有自定义设置和新功能。旨在提供稳定、响应迅速且流畅的桌面体验。提供响应迅速且流畅的桌面体验，尤其是对于新硬件。 XanMod 在 Linux 游戏、流媒体和超低延迟要求中很受欢迎，并且通常拥有最新的 Linux 内核，有多个分支可供选择，包括稳定版、边缘版和开发版。

支持所有基于 Ubuntu / Debian 的系统的最近x86\_64版本。

注意：目前专有的NVIDIA，VirtualBox，VMware Workstation / Player和其他一些dkms模块版本并不正式支持x86-64-v2 psABI（EDGE）和RT内核。

[XanMod 内核的主要特点](https://xanmod.org/#main_features)

#### **1.****导入GPG密钥:**

```
wget -qO - https://dl.xanmod.org/archive.key | sudo gpg --dearmor -o /usr/share/keyrings/xanmod-archive-keyring.gpg
```

```
echo 'deb [signed-by=/usr/share/keyrings/xanmod-archive-keyring.gpg] http://deb.xanmod.org releases main' | sudo tee /etc/apt/sources.list.d/xanmod-release.list
```

#### **3.更新软件包列表.****安装XanMod内核**

```
sudo apt update && sudo apt install linux-xanmod-x64v3
```

4.重启系统

`reboot`

稳定版：`sudo apt install linux-xanmod`

最新主线版: `sudo apt install linux-xanmod-edge`

长期支持版：`sudo apt install linux-xanmod-lts`

开发版：`sudo apt install linux-xanmod-tt`

文章来源: https://blog.upx8.com/3721
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)