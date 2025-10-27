---
title: PRoot漏洞可劫持Linux设备
url: https://buaq.net/go-140384.html
source: unSafe.sh - 不安全
date: 2022-12-18
fetch_date: 2025-10-04T01:51:18.679852
---

# PRoot漏洞可劫持Linux设备

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

![](https://8aqnet.cdn.bcebos.com/4e88b56bb129d6126493265e9486f56f.jpg)

PRoot漏洞可劫持Linux设备

导语：攻击者利用 PRoot隔离文件系统漏
*2022-12-17 11:0:0
Author: [www.4hou.com(查看原文)](/jump-140384.htm)
阅读量:39
收藏*

---

导语：攻击者利用 PRoot隔离文件系统漏洞可劫持Linux设备。

攻击者利用 PRoot隔离文件系统漏洞可劫持Linux设备。

BYOF (Bring Your Own Filesystem)攻击是指攻击者在其自有的设备上创建一个恶意文件系统，而该设备上含有用于发起攻击活动的标准工具集。然后将该文件系统下载和挂载到被入侵的机器上，为下一步入侵Linux系统提供一个预配置的工具集。

PRoot是一款Linux 开源工具，融合了'chroot'、'mount --bind'、'binfmt\_misc'命令，允许用户在Linux系统中搭建一个隔离的root文件系统。近日，Sysdig研究人员发现有黑客滥用Linux PRoot工具来发起BYOF攻击活动，影响多个Linux发行版。

默认情况下，PRoot进程活动范围局限在隔离的guest文件系统中。但QEMU模拟可以用来混合host主机和guest程序的执行。此外，guest文件系统中的程序也可以使用内置的mount/bind机制来访问host系统的文件和目录。

Sysdig研究人员发现攻击者利用PRoot在受害者系统中部署恶意文件系统，包括网络扫描工具"masscan"、"nmap"，以及XMRig加密货币挖矿机以及对应的配置文件。

文件系统中包含了用于攻击的所有内容，类似于一个包含了必要依赖的GZIP压缩文件，从DropBox这样的可信云托管服务直接释放。由于包含了所有的依赖，因此无需执行额外的配置命令。

![The malicious guest filesystem](https://www.bleepstatic.com/images/news/u/1220909/Linux/filesystem.png)

图 恶意guest文件系统

由于PRoot 是静态编译的，不需要任何依赖，攻击者只需要从gitlab下载预编译的二进制文件，执行下载的文件提取出文件系统，并挂载到系统上就可以。

研究人员发现在攻击活动中，攻击者将文件系统解压到'/tmp/Proot/' 目录，然后激活XMRig 加密货币挖矿机。

![Launching XMRig on the guest filesystem to mine using host's GPU](https://www.bleepstatic.com/images/news/u/1220909/Linux/xmrig.png)

图 使用host CPU在guest文件系统上启动XMRig加密货币挖矿机

Sysdig指出，攻击者通过PRoot可以下载除XMRig 加密货币挖矿机之外的其他payload，对被入侵的系统引发更加严重的后果。

攻击者通过使用预配置的PRoot 文件系统可以实现跨操作系统配置，而无需将恶意软件修改为特定架构，也无需包含特定依赖和工具。

更多技术分析参见：https://sysdig.com/blog/proot-post-explotation-cryptomining/

本文翻译自：https://www.bleepingcomputer.com/news/security/hackers-hijack-linux-devices-using-proot-isolated-filesystems/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?ixWagZPS)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/242192f892fd0ce563064d62db453ebc.png)

  PRoot漏洞可劫持Linux设备](https://www.4hou.com/posts/l6w1)
* [![](https://img.4hou.com/images/1670286541136741.png)

  勒索软件攻击迫使法国医院转移病人](https://www.4hou.com/posts/2JZA)
* [![](https://img.4hou.com/images/02b0b5c1c565bf75ea5a25b9aa581b2a.jpg)

  谷歌公开安卓私有计算核心PCC技术细节](https://www.4hou.com/posts/MBGm)
* [![](https://img.4hou.com/images/1670809065207384.png)

  小心使用健身追踪设备和应用程序的几大安全风险](https://www.4hou.com/posts/oJzL)
* [![](https://img.4hou.com/images/1669732783727522.png)

  重要发现！SRW应用伪装成计算器实施跑分长达2年之久，至今仍高活迭代](https://www.4hou.com/posts/gX4j)
* [![](https://img.4hou.com/images/be2466d6130d469229ccc786383dad20.jpg)

  勒索软件团伙攻击了100多个组织，获利超过6000万美元](https://www.4hou.com/posts/wg1r)

![]()

文章来源: https://www.4hou.com/posts/l6w1
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)