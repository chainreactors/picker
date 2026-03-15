---
title: 苹果紧急发布iOS 15.8.7更新以防御“Coruna”漏洞利用工具包
url: https://mp.weixin.qq.com/s/VSZeNssieCssedz6Im4eLQ
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:26:15.390004
---

# 苹果紧急发布iOS 15.8.7更新以防御“Coruna”漏洞利用工具包

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2WLm1racibDz9ziaUUnCL7HcaEyWppotDq6kCPdMOyUCVJVzicia2kNmOTficKcNs2PmEuyUiaWgI1ze9PGNPm0GwO49QnAF0l7UWLk/0?wx_fmt=jpeg)

# 苹果紧急发布iOS 15.8.7更新以防御“Coruna”漏洞利用工具包

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX09XXBUf6sRTpaCssNP72vlicf9LkIgiaeyEbCGvmLDUiccPaEGaTDXbTyxATqVzRAUGkL40LeaQbjcVbDicSU7riaIKnDGTicWiaTqOs/640?wx_fmt=jpeg&from=appmsg)

##

## 苹果公司已紧急发布iOS 15.8.7和iPadOS 15.8.7安全更新，旨在保护旧款设备免受名为"Coruna"的漏洞利用工具包的严重威胁。

##

**Part01**

## ****关键安全补丁回溯****

2026年3月11日发布的这一关键补丁从较新的iOS版本回溯了修复程序，确保使用老旧硬件的用户不会面临高级网络攻击的风险。

Coruna漏洞利用工具包通过串联多个漏洞来入侵苹果设备。它同时针对设备的核心操作系统（内核）和WebKit浏览器引擎发起攻击。攻击者只需诱骗用户访问恶意网站，就能完全控制受影响的iPhone或iPad。

**Part02**

## ****历史漏洞被重新利用****

苹果曾在2023年7月至2024年1月期间为iOS 16和iOS 17修复了这些特定漏洞。然而，威胁行为者正通过Coruna工具包积极利用这些老旧漏洞发起攻击。苹果不得不采取必要措施，为无法升级到最新操作系统的旧设备推送这些关键补丁。

使用老旧苹果硬件的用户必须立即安装此软件更新以确保安全。受影响设备包括iPhone 6s、iPhone 7、iPhone SE（第一代）、iPad Air 2、iPad mini（第四代）和iPod touch（第七代）。

**Part03**

## ****修复的四个关键漏洞****

iOS 15.8.7更新修复了四个安全漏洞，这些漏洞都是Coruna漏洞利用工具包攻击链的关键环节：

内核漏洞（CVE-2023-41974）： 由研究员Félix Poulin-Bélanger发现，这是设备内核中的一个释放后使用内存问题。如果被利用，恶意应用程序可以执行具有最高系统权限的任意代码。苹果通过改进内存管理修复了此问题。

WebKit类型混淆漏洞（CVE-2024-23222）： 苹果网页渲染引擎中的这一漏洞允许攻击者在用户处理恶意制作的网页内容时执行任意代码。苹果通过实施更严格的验证检查解决了该问题。

WebKit内存损坏漏洞（CVE-2023-43000）： 这是WebKit中的一个释放后使用漏洞，在解析恶意网页时可能导致内存损坏。苹果通过增强的内存管理技术修补了该漏洞。

WebKit内存损坏漏洞（CVE-2023-43010）： 另一个由恶意网页内容触发的严重WebKit问题，同样会导致内存损坏。苹果通过改进整体内存处理协议解决了这一缺陷。

**Part04**

## ****高危攻击方式****

由于Coruna漏洞利用工具包利用基于网络的攻击方式，用户仅通过浏览互联网或打开短信中的链接就可能面临风险。WebKit漏洞用于初始访问，内核漏洞用于系统权限提升，这种危险组合使得该威胁极为严重。

强烈建议受影响老旧设备的用户立即前往设备设置下载iOS 15.8.7或iPadOS 15.8.7更新，以保护系统免受这些已知漏洞利用的攻击。

**参考来源：**

Apple Released Emergency Updates for iOS 15.8.7 to Thwart ‘Coruna’ Exploit Kit

https://cybersecuritynews.com/apple-released-emergency-updates/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3cSYwf9JzGtDoYs4CGx2ljpXcZ5TfjHRz5qAcyWh8toRsxBf4Ws4INjebjWXk6Qtea2QViaicbkU4heohT9o1D194ib91F38VGUY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1c65Y8TDXkbFibGXhdaEZzcUriaA8IqQF7iaTLhndBBN5vkfOyQdEibFsFOMJdZZ5pCfAhpPK4ibkibtPXkEygVQuokHrDAqoQ4Ecib0/640?wx_fmt=png&from=appmsg)

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