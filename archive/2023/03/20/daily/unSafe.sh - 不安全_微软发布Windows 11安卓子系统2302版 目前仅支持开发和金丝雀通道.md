---
title: 微软发布Windows 11安卓子系统2302版 目前仅支持开发和金丝雀通道
url: https://buaq.net/go-154171.html
source: unSafe.sh - 不安全
date: 2023-03-20
fetch_date: 2025-10-04T10:04:50.040052
---

# 微软发布Windows 11安卓子系统2302版 目前仅支持开发和金丝雀通道

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

![](https://8aqnet.cdn.bcebos.com/71fde314f2a5957ebd44306dc62400dd.jpg)

微软发布Windows 11安卓子系统2302版 目前仅支持开发和金丝雀通道

本周微软没有发布新的Windows 11开发版或金丝雀版，不过适用于上述通道的安卓子系统倒是迎来测试版。新版本是 Windows Subsystem for Android 2302.
*2023-3-19 16:13:40
Author: [www.landiannews.com(查看原文)](/jump-154171.htm)
阅读量:18
收藏*

---

本周微软没有发布新的Windows 11开发版或金丝雀版，不过适用于上述通道的安卓子系统倒是迎来测试版。

新版本是 Windows Subsystem for Android 2302.40000.6.0 版，用于改进稳定性、图形、音频和安全性。

如果你使用的是开发版/金丝雀版那可以在微软商店获取更新 ，若TPM不支持或地区不支持可以下载离线包。

[![微软发布Windows 11安卓子系统2302版 目前仅支持开发和金丝雀通道](https://img.lancdn.com/landian/2023/03/97960-2.png)](https://img.lancdn.com/landian/2023/03/97960-2.png)

**以下是更新日志：**

1. 图形方面：针对显卡选择方面的稳定性改进
2. 图形方面：更新安卓子系统设置提供显卡性能的选项
3. 显示方面：修复Windows 11安卓子系统与外部显示器的连接与取消连接问题
4. 音频方面：解决部分应用程序存在的音频缓冲区问题
5. 安全方面：集成Android 13最新安全更新

**如何离线安装或升级：**

以下方法支持所有国家和地区、支持所有Windows 11系统、不需要 CPU/TPM/SecureBoot 满足硬件要求。

打开这个网站：[https://store.rg-adguard.net](https://store.rg-adguard.net/) 在输入框左侧点击ProductID然后输入ID：9P3395VX91NR

在右侧通道选择Fast点击搜索按钮结果检索到离线安装包，下载页面最底部的1.34GB的**msixbundle**安装包。

将下载的文件重命名为 and.msixbundle 并剪切到C盘根目录，接着打开管理员模式的PowerShell执行命令

```
#进入C盘根目录
cd C:\
#执行安装或更新
add-appxpackage and.msixbundle
#没报错就是成功，之后可以打开安卓子系统设置检查版本
```

[![微软发布Windows 11安卓子系统2302版 目前仅支持开发和金丝雀通道](https://img.lancdn.com/landian/2023/03/97960-1.png)](https://img.lancdn.com/landian/2023/03/97960-1.png)

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/97900.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/97900.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)