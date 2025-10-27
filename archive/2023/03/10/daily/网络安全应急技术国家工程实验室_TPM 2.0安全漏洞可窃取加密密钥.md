---
title: TPM 2.0安全漏洞可窃取加密密钥
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535287&idx=3&sn=e347508d2b0b26476aeb9b5453a4fefb&chksm=fa93fc76cde47560a39c163459ac3ee95b4d38d58704dc7249aa321cd119023aba4654e8c37e&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2023-03-10
fetch_date: 2025-10-04T09:09:37.509291
---

# TPM 2.0安全漏洞可窃取加密密钥

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mh6Zx97hCPmCXVzKgBIibsafZcUYN6FqUEHuNhdlQKlwiahb2aRfibFxacgtHwZgll3zbEPdIRpWdsw/0?wx_fmt=jpeg)

# TPM 2.0安全漏洞可窃取加密密钥

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGoguPRJALJSib4gAMialdIfxQ1D8adC9eDRibWqgrauianBibNFhRIgbfzDcKTWCnoAWf3QOWleaKRrl5Iww/640?wx_fmt=png)

# **TPM**

TPM（Trusted Platform Module，可信平台模块）是一种基于硬件的安全技术，可以为操作系统提供抗修改的安全加密功能。TPM可以用来保存加密密钥、密码和其他重要数据。TPM对部分Windows安全特征来说是必须的，比如Measured Boot、Device Encryption（设备加密）、Windows Defender System Guard（DRTM，防护系统保护）、Device Health Attestation（设备健康度量）等。TPM可以帮助Windows系统增强安全，保护敏感信息和加密数据。

Windows 11系统中将TPM纳入必须，通过启动安全度量和确保Windows hello面部识别提供可靠的认证。Linux也支持TPM，但是目前操作系统中没有必须使用该模块。但Linux工具允许应用和用户确保TPM中的数据安全。

# **TPM 2.0漏洞**

近日，Quarkslab研究人员发现2个缓存溢出漏洞影响TPM 2.0规范，漏洞CVE编号为：CVE-2023-1017（越界读漏洞）和CVE-2023-1018（越界写漏洞）。攻击者利用这两个漏洞可以访问或覆写敏感数据，比如加密密钥。

漏洞产生的根源在于该规范处理部分TPM命令的参数过程中允许未经认证的本地攻击者发送精心伪造的命令来在TPM中执行代码以漏洞这两个漏洞。具体来说是传递给ExecuteCommand()入口点的的缓存后的2个字节的读写。根据TPM规范的开发者Trusted Computing Group（TCG，可信计算组织）的安全公告，攻击者利用该漏洞可以实现信息泄露或权限提升。

CERT称，可以访问TPM命令接口的攻击者可以发送恶意伪造的命令给TPM模块以触发漏洞。攻击者利用这两个漏洞可以对敏感数据实现读访问，或对TPM保护的数据实现覆写，比如加密密钥。

联想是少数发布关于这两个安全漏洞的安全公告的OEM厂商，称CVE-2023-1017漏洞影响了部分运行在Nuvoton TPM 2.0芯片上的联想设备。

漏洞的利用要求攻击者对设备具有认证的本地访问权限，但运行在设备上的恶意软件满足这一条件。研究人员建议用户将设备的物理访问限制为可信用户，只安装来自知名厂商的签名应用，并及时安全固件安全更新。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/new-tpm-20-flaws-could-let-hackers-steal-cryptographic-keys/

原文来源：嘶吼专业版

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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