---
title: 损坏的前奏：微软发布修复方案解决HDD/SSD被识别为可移动磁盘
url: https://buaq.net/go-164750.html
source: unSafe.sh - 不安全
date: 2023-05-21
fetch_date: 2025-10-04T11:36:52.560939
---

# 损坏的前奏：微软发布修复方案解决HDD/SSD被识别为可移动磁盘

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

![](https://8aqnet.cdn.bcebos.com/611251cc733f55fbe3e1c962d9f12b78.jpg)

损坏的前奏：微软发布修复方案解决HDD/SSD被识别为可移动磁盘

微软在健康仪表盘中确认 Windows 11 系统也受 SATA 相关的古老错误影响，该问题会导致机械硬盘和固态硬盘(只影响 SATA SSD，不影响 NVMe SSD)被错误地识别为
*2023-5-20 21:52:20
Author: [www.landiannews.com(查看原文)](/jump-164750.htm)
阅读量:20
收藏*

---

微软在健康仪表盘中确认 Windows 11 系统也受 SATA 相关的古老错误影响，该问题会导致机械硬盘和固态硬盘(只影响 SATA SSD，不影响 NVMe SSD)被错误地识别为可移动磁盘。

这个错误与硬盘固件有关，受影响的硬盘都会在 Windows 托盘区中被识别为可移动磁盘，而且这个问题还可能是硬盘即将损坏或数据出现问题的前奏，所以如果你碰到了这个问题，建议使用硬盘检测工具对硬盘扫描和检测。

如果硬盘制造商有专门的工具，例如三星的魔术师，那可以使用制造商提供的工具进行检测和固件更新。

[![损坏的前奏：微软发布修复方案解决HDD/SSD被识别为可移动磁盘](https://img.lancdn.com/landian/2023/05/98715.png)](https://img.lancdn.com/landian/2023/05/98715.png)

这个问题影响 Windows Vista、Windows 7、Windows 8、Windows 8.1、Windows 10、Windows 11 以及对应版本的 Windows Server 服务器操作系统。

微软称是否会被识别为可移动磁盘取决于系统 BIOS 以及它如何标记主板上的各种 SATA 接口，开箱即用 (即系统自带的) 驱动程序可以直接检查 SATA 接口，并将连接到外部接口的设备识别为可移动磁盘，**并非所有驱动程序都会这样识别，但这可能是损坏或数据丢失的潜在原因。**

微软提供了一种基于命令行的解决办法，此办法适用于 Windows 8、Windows 8.1、Windows 10、Windows 11。

**以下是修复方案：**

```
#打开管理员模式的命令提示符并输入
devmgmt.msc
#展开硬盘驱动器，右键点击被识别为可移动磁盘的硬盘，选择属性
#在属性中可以看到 Bus Number 编号，例如 0 1
#在命令提示符中粘贴并执行下面的命令 (需要修改结尾的 X)
reg.exe add “HKLM\SYSTEM\CurrentControlSet\Services\storahci\Parameters\Device” /f/v TreatAsInternalPort /t REG_MULTI_SZ /d x
#执行命令前请将末尾的 X 修改为对应的 Bus Number 编号
```

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/98715.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/98715.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)