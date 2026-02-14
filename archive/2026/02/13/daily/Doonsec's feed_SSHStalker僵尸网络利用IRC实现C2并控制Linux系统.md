---
title: SSHStalker僵尸网络利用IRC实现C2并控制Linux系统
url: https://mp.weixin.qq.com/s/E6J54n1tyRqM-swiQNJH1w
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:05:57.209355
---

# SSHStalker僵尸网络利用IRC实现C2并控制Linux系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX27c4kPAUbD9BAe7UKDLJhveEhm5z8UANVQJIRGJBXFPA7fe4ZicASNcAkibrc2NuWe8Y7kQhNdQKnPkk0HQpmRyianLI6VMNR15w/0?wx_fmt=jpeg)

# SSHStalker僵尸网络利用IRC实现C2并控制Linux系统

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0Nmo7TCZVNRUbFET3xULPkL2MhStyNCUzjHvtX8rq4UImJ0P3brsEYvG2dZjgOGGdrgRYGFrfqDAjQ8ukTFMFvNWYynWhUbic8/640?wx_fmt=jpeg&from=appmsg)

网络安全研究人员披露了一个名为SSHStalker的新型僵尸网络攻击活动细节，该网络依赖互联网中继聊天（IRC）协议实现命令与控制（C2）功能。

网络安全公司Flare表示："该工具集结合了隐蔽辅助程序与旧版Linux漏洞利用技术：除了日志清理工具（篡改utmp/wtmp/lastlog）和rootkit类组件外，攻击者还保留了大量2009-2010年间针对Linux 2.6.x内核的漏洞利用代码（CVE编号）。这些漏洞对现代系统价值有限，但对'被遗忘'的基础设施和长期遗留环境仍然有效。"

**Part01**

## ****自动化攻击与持久潜伏特性****

SSHStalker将IRC僵尸网络机制与自动化大规模入侵操作相结合，通过SSH扫描器和其他现成扫描工具将易受攻击系统纳入网络，并将其注册到IRC频道中。与其他通常利用此类僵尸网络进行分布式拒绝服务（DDoS）攻击、代理劫持或加密货币挖矿的短期攻击活动不同，SSHStalker被发现会维持持久访问权限而不进行后续攻击行为。

这种潜伏特性使其与众不同，表明被入侵基础设施可能被用于攻击准备、测试或战略保留以供未来使用。

**Part02**

## ****技术实现细节****

SSHStalker的核心组件是一个Golang扫描器，它会扫描22端口寻找开放SSH的服务器，以蠕虫式传播扩大攻击范围。攻击还会投放多个有效载荷，包括IRC控制bot变体和Perl文件bot，后者会连接至UnrealIRCd服务器，加入控制频道并等待执行洪水流量攻击和控制其他bot的指令。

攻击还通过执行C程序文件清理SSH连接日志，消除恶意活动痕迹以降低取证可见性。此外，该恶意工具包包含"保活"组件，确保主恶意进程在被安全工具终止后60秒内重新启动。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3uPlZubTNDogZ8RYL30pLGlib9YJ7kO3xtiaxe6ObWY7Vpj3hxFuib16wt96BIkMXgZiarVMAjiap0ibk0uOxdiamuicFYMicxZYDQROmQ/640?wx_fmt=jpeg&from=appmsg)

**Part03**

## ****利用的漏洞与攻击工具库****

SSHStalker的显著特点是结合了大规模入侵自动化技术与16个影响Linux内核的漏洞利用代码，其中部分漏洞可追溯至2009年。漏洞利用模块使用的缺陷包括（CVE-2009-2692）、（CVE-2009-2698）、（CVE-2010-3849）、（CVE-2010-1173）、（CVE-2009-2267）、（CVE-2009-2908）、（CVE-2009-3547）、（CVE-2010-2959）和（CVE-2010-3437）等。

Flare对攻击者基础设施的调查发现了大量开源攻击工具和已公开的恶意软件样本，包括：

* 用于实现隐蔽和持久化的rootkit
* 加密货币挖矿程序
* 可执行名为"website grabber"二进制文件的Python脚本，用于从目标网站窃取暴露的亚马逊云服务（AWS）密钥
* 具有C2和远程命令执行功能的IRC bot——EnergyMech

**Part04**

## ****攻击者背景分析****

由于IRC频道和配置词表中存在"罗马尼亚式昵称、俚语模式和命名惯例"，研究人员怀疑该攻击活动幕后黑手可能来自罗马尼亚。其操作特征与名为Outlaw（又称Dota）的黑客组织高度重合。

Flare指出："SSHStalker似乎不专注于新型漏洞利用开发，而是通过成熟的实现和编排展示操作控制能力，主要使用C语言编写核心bot和底层组件，shell脚本负责编排和持久化，Python和Perl仅限用于攻击链中的辅助自动化任务和运行IRCbot。该威胁行为体虽未开发0Day或新型rootkit，但在大规模入侵工作流、基础设施循环利用以及跨异构Linux环境的长期持久化方面展现出强大的操作纪律。"

**参考来源：**

SSHStalker Botnet Uses IRC C2 to Control Linux Systems via Legacy Kernel Exploits

https://thehackernews.com/2026/02/sshstalker-botnet-uses-irc-c2-to.html

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2W4PauSPeWFzibFnIaueGohexvlxGHlyQqibmSVMWnic1pgOiclspWRg4QB7OUqibzIeV7g8PQScBQcTOX8rGTGrk6t1tVfKCicKqZ8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1QWGTwJ4jnO2icEhSqbRNdWd3iaVBKjlfTsWSdDBiayVW1jWahKjlggw6mzYnEo5D6PMvFzRX6fEpVEic5NqQoVDFCWvHlh48OxrA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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