---
title: 暗网Dark Power 新勒索软件正席卷全球
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535771&idx=2&sn=668788db52b407c73510fc3af851b021&chksm=fa93fa5acde4734cf3b2a8a583f489b19440445fe983184b678182f51f9da4d6dc95cb98ab7d&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-28
fetch_date: 2025-10-04T10:53:39.066617
---

# 暗网Dark Power 新勒索软件正席卷全球

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lMOgNUe63dZVjeVYtwqN71hs9V6qicVKIEAwXF6hwedpvlf3HnKmibs1pDoEBnUWSZay8npSgaWeAw/0?wx_fmt=jpeg)

# 暗网Dark Power 新勒索软件正席卷全球

网络安全应急技术国家工程中心

近日，出现了一种名为“Dark Power”（暗网）的新勒索软件操作，它已经在一个暗网数据泄露网站上列出了第一批受害者，并威胁说如果不支付赎金就公布数据。

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6yuB1mM5P4uYWU0momoFX4Y3ic0evFrRxoqtKAYmnhBV1ib6zpD8xgQqEw3maSAXFJu5xulv6Rqv4Sg/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

勒索软件团伙的加密器的编译日期是 2023 年 1 月 29 日，即攻击开始的时间。

此外，该操作尚未在任何黑客论坛或暗网空间上推广；因此它可能是一个私人项目。

据分析 Dark Power 的Trellix称，这是一种针对全球组织的机会主义勒索软件操作，要求支付相对较小的 10,000 美元赎金。

**黑暗力量攻击细节**

Dark Power 有效载荷是用 Nim 编写的，Nim 是一种跨平台编程语言，具有多个与速度相关的优势，使其适用于性能关键型应用程序，如勒索软件。

此外，由于 Nim 现在才开始在网络犯罪分子中越来越受欢迎，它通常被认为是不太可能被防御工具检测到的利基选择。

Trellix 没有提供有关 Dark Power 感染点的详细信息，但它可能是一种利用、网络钓鱼电子邮件或其他方式。

执行时，勒索软件会创建一个随机的 64 个字符长的 ASCII 字符串，用于在每次执行时使用唯一密钥初始化加密算法。

接下来，勒索软件会终止受害者机器上的特定服务和进程，以释放文件进行加密，并最大限度地减少任何阻止文件锁定进程的可能性。

在此阶段，勒索软件还会停止其硬编码列表中的卷影复制服务 (VSS)、数据备份服务和反恶意软件产品。

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6yuB1mM5P4uYWU0momoFX4YDtDvA4dHISkKib4q3ZK6mYTEcpe3KX7YGDBXOkmMJRNw9RAicchqCcPg/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

终止的进程和服务

杀死上述所有服务后，勒索病毒会休眠30秒，并清除控制台和Windows系统日志，以防止数据恢复专家分析。

加密使用 AES（CRT 模式）和启动时生成的 ASCII 字符串。生成的文件被重命名为“.dark\_power”扩展名。

有趣的是，该勒索软件有两个版本在野外流传，每个版本都有不同的加密密钥方案。

第一个变体使用 SHA-256 算法对 ASCII 字符串进行哈希处理，然后将结果分成两半，使用第一部分作为 AES 密钥，第二部分作为初始化向量 (nonce)。

第二种变体使用 SHA-256 摘要作为 AES 密钥，并使用固定的 128 位值作为加密随机数。

DLL、LIB、INI、CDM、LNK、BIN 和 MSI 等系统关键文件，以及程序文件和网络浏览器文件夹，都被排除在加密之外，以保持受感染计算机的运行，从而使受害者能够查看赎金注意并联系攻击者。

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6yuB1mM5P4uYWU0momoFX4Y0mRnODoiaMUg10dPicmzUqz2FIoOY0DN5HjkY4iaKrFR1qI3Yfu5828Uw/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6yuB1mM5P4uYWU0momoFX4YKDdaKicgbCPIibicqNZVMGEh74VTov2TVjmST8Jl4ianAIXwMoB4frGiaeQ/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

从加密中排除的文件和文件夹

赎金票据最后一次修改是在 2023 年 2 月 9 日，它给受害者 72 小时的时间将 10,000 美元的 XMR（门罗币）发送到提供的钱包地址，以获得可用的解密器。

与其他勒索软件操作相比，Dark Power 的赎金记录很突出，因为它是一个 8 页的 PDF 文档，其中包含有关发生的事情以及如何通过 qTox 信使联系他们的信息。

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6yuB1mM5P4uYWU0momoFX4YnxWS8Y9b40b9Dg9erOT3LENWraFLdCKfOtG9OoX2ic0An8fOe3GQByQ/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

受害者和活动

截止到目前，Dark Power 的 Tor 站点处于离线状态。然而，随着与受害者谈判的深入，勒索软件门户定期下线的情况并不少见。

Trellix 报告说，它已经看到来自美国、法国、以色列、土耳其、捷克共和国、阿尔及利亚、埃及和秘鲁的十名受害者，因此目标范围是全球性的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/QmbJGbR2j6yuB1mM5P4uYWU0momoFX4YJFXK9z63XvoKeshtAAjDJJfDvfopWs8pVOY7hpdjQMH0xomBR9S2eg/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

Dark Power 组织声称从这些组织的网络中窃取了数据，并威胁说如果他们不支付赎金，就会公开这些数据，所以它又是一个双重勒索组织。

原文来源：E安全

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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