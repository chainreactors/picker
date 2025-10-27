---
title: 电磁故障注入攻击影响大疆无人机
url: https://buaq.net/go-170948.html
source: unSafe.sh - 不安全
date: 2023-07-02
fetch_date: 2025-10-04T11:51:12.709203
---

# 电磁故障注入攻击影响大疆无人机

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

![](https://8aqnet.cdn.bcebos.com/99bd3d7b4dbdd9d8fcd2fc5ae3fa5464.jpg)

电磁故障注入攻击影响大疆无人机

导语：​电磁故障注入攻击大疆无人机固件更新
*2023-7-1 11:50:0
Author: [www.4hou.com(查看原文)](/jump-170948.htm)
阅读量:36
收藏*

---

导语：​电磁故障注入攻击大疆无人机固件更新过程，可接管无人机。

电磁故障注入攻击大疆无人机固件更新过程，可接管无人机。

近日，IOActive研究人员发布白皮书分析了无人机行业的安全态势。IOActive研究人员探索使用非入侵的方式在商用无人机上实现代码执行，比如电磁侧信道攻击和电磁故障注入攻击。

**无人机攻击面分析**

无人广泛应用于各个领域，如军事、商业。与其他技术一样，无人机也易受到各种类型的攻击。无人机的攻击面包括：（1）后端、（2）移动端、（3）无线频谱通信、（4）物理设备。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230629/1688023811613810.png "1688023712443491.png")

图 无人机攻击面

**电磁故障注入攻击**

考虑到非入侵的攻击本质，IOActive使用电磁辐射和电磁故障注入来实现攻击。在研究中，主要使用Riscure作为工具。

第一个方法是使用电磁辐射来窃取加密密钥，并解密固件。首先，使用强电磁辐射信号来找到无人机的PCB区域，以放置探针和记录信息以提取密钥。在获取最强信号位置后，研究人员分析如何绕过固件的签名验证。经过大量的测试和数据分析，研究人员发现绕过签名的成功率小于0.5%。因此，密钥恢复的可能性很小，无法用于现实攻击中。

第二个方法是使用电磁故障注入。Riscure提出使用glitch来使得一个指令变成另一个指令，并获得PC寄存器的控制权限。下图是攻击环境搭建：包括一个笔记本电脑、一个电源、Riscure Spider、示波器、电磁故障注入脉冲生成器。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230629/1688023812170006.png "1688023772155710.png")

图 攻击环境

在识别PCB上的区域后，研究人员修改的glitch的形状后，就可以得到成功的结果。目标进程被破坏，Payload出现在多个寄存器中。下图是分段错误发生的指令：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230629/1688023811165492.png "1688023811165492.png")

成功引发内存破坏后，下一步就是设计payload来实现代码执行。攻击者使用这样的漏洞利用可以完全控制目标设备、泄露所有敏感内容、实现ADB访问和泄露加密密钥。

白皮书下载地址：https://ioac.tv/3N005Bn

本文翻译自：https://labs.ioactive.com/2023/06/applying-fault-injection-to-firmware.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?xjJhFwnx)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/9355b6fec984c2ee8e7a111fa5672268.jpeg)

  电磁故障注入攻击影响大疆无人机](https://www.4hou.com/posts/9A3z)
* [![](https://img.4hou.com/images/1688011455207036.jpg)

  Andariel组织开始借助新的恶意软件发起攻击](https://www.4hou.com/posts/7yDB)
* [![](https://img.4hou.com/images/微信截图_20230629103317.png)

  美国两家航空公司发生了数据泄露事件](https://www.4hou.com/posts/ZGZg)
* [![](https://img.4hou.com/images/9a5108502e11c1a2ba0e261dd0662c01.png)

  【技术前沿】BlackHat USA 23 &DEFCON 31：利用LED闪烁恢复密钥](https://www.4hou.com/posts/NK78)
* [![](https://img.4hou.com/images/微信截图_20230627105840.png)

  微软承认6月发生了针对Outlook和OneDrive的黑客攻击事件](https://www.4hou.com/posts/wyEX)
* [![](https://img.4hou.com/images/e48a5e4ba3fa80b6055c4746db9f1381.jpg)

  如何提高电子邮件服务器的保护级别（下）](https://www.4hou.com/posts/rX54)

![]()

文章来源: https://www.4hou.com/posts/9A3z
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)