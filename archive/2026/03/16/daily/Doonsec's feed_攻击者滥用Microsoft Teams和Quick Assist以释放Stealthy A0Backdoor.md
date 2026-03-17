---
title: 攻击者滥用Microsoft Teams和Quick Assist以释放Stealthy A0Backdoor
url: https://mp.weixin.qq.com/s/wmClg7S8Wqpx09QR80k7Ew
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:13:14.410421
---

# 攻击者滥用Microsoft Teams和Quick Assist以释放Stealthy A0Backdoor

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PTcMYPpGhnPKAFreiavRThzfiaUvH9toD6Udk1Jd4fAxlE1uuZE6ibKmX4xmfJyKrlomSeniabccUx30IHxicp5sg2C5iayiapQGKZicg/0?wx_fmt=jpeg)

# 攻击者滥用Microsoft Teams和Quick Assist以释放Stealthy A0Backdoor

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

一个名为A0Backdoor的新发现的后门已经出现，作为滥用Microsoft Teams和Windows远程辅助工具Quick Assist的计算社会工程活动的一部分。

该威胁组在Blitz Brigantine、Storm-1811和STAC5777等别名下被跟踪，并与Black Basta勒索软件网络有联系。

该活动至少从2025年8月开始活跃，一直持续到2026年2月下旬，以日益完善的攻击链针对金融和医疗保健部门的专业人士。

攻击始于数千封垃圾邮件充斥目标的收件箱，造成混乱和紧迫感。

然后，威胁组通过微软团队联系受害者，冒着IT支持人员，并主动提出帮助解决电子邮件问题。

受害者认为他们正在与公司支持部门交谈，通过Quick Assist（一个内置的Windows工具）允许远程访问，允许一台计算机由另一台计算机控制。

有了该通道的保障，攻击者迅速植入自己的工具，并在受损的机器上建立持久的立足点。

BlueVoyant分析师确定了与该活动相关的两起独立事件，并发现交付给受害者的软件伪装成合法的微软应用程序，包括Microsoft Teams和名为CrossDeviceService的实用程序。

这些软件包以数字签名的MSI安装程序文件的形式到达，使它们看起来像是真正的软件更新。

研究人员还指出，自2025年7月以来，至少使用了三份代码签名证书，这表明该集团几个月来一直在悄悄地构建其自定义工具集。

这种攻击的后果远远超出了最初的远程会话。A0Backdoor收集系统详细信息，如用户名和计算机名称，在联系其操作员之前对受感染的主机进行指纹识别。

该通信通过DNS隧道传输到1.1.1.1等公共解析器，因此受感染的机器避免与攻击者控制的服务器进行任何直接连接，使流量更难标记。

调查中确定的受害者包括一家加拿大金融机构和一家全球卫生组织的专业人员。

## **感染如何占据：DLL侧载和A0Backdoor**

A0Backdoor背后的感染机制表明，该小组在多大程度上完善了其技术方法。

当攻击者将恶意的MSI软件包丢弃到受害者的机器上时，它会安装一个看起来很合法的微软应用程序以及一个名为hostfxr.dll的篡改文件。

通常是一个值得信赖的。由微软签署的NET托管组件，此文件与证书名称MULTIMEDIOS CORDILLERANOS SRL签名的恶意副本交换。

当合法的可执行文件运行时，它会加载这个假DLL——这种方法被称为DLL侧载——让恶意软件在受信任进程的掩护下无声运行。

一旦加载，恶意的hostfxr.dll会解密隐藏在自己代码中的数据，并将执行转移到shellcode有效负载中。

为了使分析复杂化，加载器发出过多的CreateThread调用，这些调用可能会在运行时崩溃调试器。

shellcode通过查询字符串“QEMU”等沙盒指示器的固件表来检查它是否在虚拟环境中运行，并使用基于时间的密钥系统，其中解密密钥大约每55小时移动一次。

在该窗口外执行恶意软件会产生错误的密钥，使有效负载永久锁定。

最终的A0Backdoor有效负载通过DNS MX记录查询连接到其运营商，使用高熵子域，这些子域融入到普通网络流量中。

运营商没有注册可能引起标志的新域名，而是重新注册了较旧的、过期的域名，通过调整的检测工具来发现新注册的或算法生成的域名。

组织应限制整个企业环境的快速辅助使用，并实施阻止未经请求的远程访问会话的政策。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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