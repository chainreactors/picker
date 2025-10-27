---
title: Ubuntu 安装 XanMod 内核
url: https://blog.upx8.com/3721
source: 黑海洋 - WIKI
date: 2023-07-30
fetch_date: 2025-10-04T11:53:21.628348
---

# Ubuntu 安装 XanMod 内核

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Ubuntu 安装 XanMod 内核

发布时间:
2023-07-29

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
18319

**![](https://loukas.cn/wp-content/uploads/2022/03/image.png)**

**XanMod**是一个通用的Linux内核发行版，具有自定义设置和新功能。旨在提供稳定、响应迅速且流畅的桌面体验。提供响应迅速且流畅的桌面体验，尤其是对于新硬件。 XanMod 在 Linux 游戏、流媒体和超低延迟要求中很受欢迎，并且通常拥有最新的 Linux 内核，有多个分支可供选择，包括稳定版、边缘版和开发版。

支持所有基于 Ubuntu / Debian 的系统的最近x86\_64版本。

注意：目前专有的NVIDIA，VirtualBox，VMware Workstation / Player和其他一些dkms模块版本并不正式支持x86-64-v2 psABI（EDGE）和RT内核。

[XanMod 内核的主要特点](https://blog.upx8.com/go/aHR0cHM6Ly94YW5tb2Qub3JnLyNtYWluX2ZlYXR1cmVz)

## 通过终端安装

#### **1.****导入GPG密钥:**

```
wget -qO - https://dl.xanmod.org/archive.key | sudo gpg --dearmor -o /usr/share/keyrings/xanmod-archive-keyring.gpg
```

#### **2.添加存储库:**

```
echo 'deb [signed-by=/usr/share/keyrings/xanmod-archive-keyring.gpg] http://deb.xanmod.org releases main' | sudo tee /etc/apt/sources.list.d/xanmod-release.list
```

#### **3.更新软件包列表.****安装XanMod内核**

```
sudo apt update && sudo apt install linux-xanmod-x64v3
```

####

4.重启系统

`reboot`

#### **PS:安装XanMod内核**

稳定版：`sudo apt install linux-xanmod`

最新主线版: `sudo apt install linux-xanmod-edge`

长期支持版：`sudo apt install linux-xanmod-lts`

开发版：`sudo apt install linux-xanmod-tt`

[取消回复](https://blog.upx8.com/3721#respond-post-3721)

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