---
title: 内存取证-练习
url: https://mp.weixin.qq.com/s/d1zY9qkBUdalzt4C0Xlotg
source: Doonsec's feed
date: 2026-10-20
fetch_date: 2026-10-21T06:47:40.655473
---

# 内存取证-练习

# 内存取证-练习

原创

内存余响
内存余响

内存余响

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#

挑战描述

我们从情报局部门收到了这个内存转储。他们说，这些证据可能隐藏着黑社会黑帮大卫·本杰明的一些秘密。这个内存转储是从他的一名员工那里拿走的，本周早些时候被 FBI 逮捕了。您的工作是检查内存转储，看看是否能找出一些东西。FBI 还表示，David 通过互联网与他的员工进行了交流，因此这可能是一个不错的起点。

注意：本次挑战赛由 1 个flag组成，分为 2 个部分。

根据题目提示通过互联网进行交流

首先查看操作系统

vol.py -f MemoryDump\_Lab6.raw imageinfo

得到profile

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibicEY6HR10cR1icnTSia2aZPdIrd2LYbORUmFCnqKLRVNZKbelkGVxOL5p18vwNk1mibUjGxoadbibyzIhjp48MKicoKgrttmDBgUpzU/640?wx_fmt=png)

查看网络连接，发现开了很多浏览器

vol.py -f MemoryDump\_Lab6.raw --profile=Win7SP1x64 netscan

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibibicqLJr1Tn0x59Vaw4yKdksDbyCDWGmY6T75qz8R9qCor89qZy5oDHJKOo7CZzAL7p8MzW0BCNQGaXQia5fqCy5EPhIndSPfibOA/640?wx_fmt=png)

查看浏览器历史记录

vol.py -f MemoryDump\_Lab6.raw --profile=Win7SP1x64 iehistory

发现桌面上有一些flag这种压缩包之类

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibibUVeMf5ibHj4kF3dRW3qmrmt3s9cic8VRIaKibEribTDAII8xHqEpdibP6fC42jJas4mrq8PXrzykCa9bYJb0M0DqHvR27Uk2yeWPg/640?wx_fmt=png)

vol.py -f MemoryDump\_Lab6.raw --profile=Win7SP1x64 dumpfiles -Q 0x000000005fcfc4b0 -D dump

下载下来里面有一张图片但是需要密码

在查看环境变量，可以发现

vol.py -f MemoryDump\_Lab6.raw --profile=Win7SP1x64 envars

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib9ccksYjibS8tYlYicoYRcx0Ufg7vzXNWvEv6ibAYxiamibehz0WnUZVgw05KfLZhJeSdSZv0wgPrLEIibYwHxxWuOibIcF0TnicKyevNo/640?wx_fmt=png)

找到rar的密码

得到后半部分flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibibs2u94uQk9KNRWHaKx2UX4EgxuCtH2FSuUYtENqf3LRSPoKf6Z5ZUbrQ9rjs9f3wxQmhsz7ibk3exf0RrGmgCxrjrABENaib9zQ/640?wx_fmt=png)

查看chrome浏览器的历史记录，我们可以发现

vol.py -f MemoryDump\_Lab6.raw --profile=Win7SP1x64 chromehistory

有一个可疑的网站

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib8rLQ6eGNVpP6rgc1bOIFXxUk1qhlesp00uewX9ffO76a8NtpkE5dVGROQ4cuyexJHJzegMDnHe6jVrD8G2osEIQ0ss19982gA/640?wx_fmt=png)

我们要找到这个key，还在里面找到一个网址http://mega.nz

在镜像里面搜索一下

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibibmtAvZJKel8KbPqLAHEZkxI3ic6fBwoW1U6xicasbrqIUfEofibCedFEbqj0DWGVq9CYyFSuoEX59B0h8ibiahVublyKqG4h01Qsc4/640?wx_fmt=png)

找到key，填入key之后得到一张照片但是打开不了

010查看一下发现iHDR应该是IHDR修改之后即可得到前半部分flag

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic4YfldibtqMVhOo0ez7bhNzzvcKGfFIlhFKFvlSN3VmFvNUVyibvMYJP3SR60w6t9GFkzGY4yrGNrvk2DZYQ5lbJQppuHpG1VfI/0?wx_fmt=png)

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