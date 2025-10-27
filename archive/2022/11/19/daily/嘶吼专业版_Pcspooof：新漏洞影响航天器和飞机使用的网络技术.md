---
title: Pcspooof：新漏洞影响航天器和飞机使用的网络技术
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247553953&idx=1&sn=1bb691ecd45e87668ba75673e17c1e0f&chksm=e915c39bde624a8d17aa3f4a5f8cfbda701d441da884fcfd62dd547f2a8b092d1505dfe15587&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-11-19
fetch_date: 2025-10-03T23:15:20.713579
---

# Pcspooof：新漏洞影响航天器和飞机使用的网络技术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28l1Y323O7vFdoqJ4ibMiclI5456sTnWAPouPcNvbLJTfsoL11j5o9yCV2UbWscwKGI7Um9Iew9ZBSw/0?wx_fmt=jpeg)

# Pcspooof：新漏洞影响航天器和飞机使用的网络技术

布加迪

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28l1Y323O7vFdoqJ4ibMiclI5XKunVazlBccXtAMribZHYFUt4MLPXq16Vvm5eHEELsicwnUia8gwXiajQQ/640?wx_fmt=png)

近日研究人员披露了一种针对时间触发的以太网（TTE）的新型攻击方法，这种关键的技术被用于安全性至关重要的基础设施，可能会导致航天器和飞机的核心系统出现故障。

来自密歇根大学、宾夕法尼亚大学和美国宇航局约翰逊航天中心的一群学者和研究人员将这种攻击技术称之为PCspooF，该技术旨在违反TTE的安全保证，诱导TTE设备在长达1秒的时间内失去同步，这种行为甚至会导致航天任务中出现不受控制的动作，并威及到机组人员的安全。

多种联网技术组成了所谓的混合关键网络，而TTE是其中之一。在混合关键网络中，定时和容错要求各异的流量共存于同一个物理网络中。这就意味着实现航天器/飞机控制的关键设备和用于监测和数据收集的非关键设备都可以共享同一个网络。

这种方法的一个明显优势是，由于仅仅依赖一种技术，所以重量和功率方面的要求比较低，开发和时间成本也较低，但它也有自身的缺点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28l1Y323O7vFdoqJ4ibMiclI5pu0ic1BBCVibdiaO3ibmVXVEjbjYqYB03QPic8mGdMCuicMeUpob9ViagFg5w/640?wx_fmt=png)

图1

这项研究报告的第一作者Andrew Loveless告诉The Hacker News网站，这种混合关键方法给网络设计在提供隔离机制方面带来的压力大得多。鉴于关键系统和非关键系统可以连接到同一台交换机，网络协议和硬件就需要做额外的工作，才能确保总是能够保证关键流量成功且准时传输。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28l1Y323O7vFdoqJ4ibMiclI5jwkboZAPddBCnbNZ8GEqHNF1wBs3Ty4oImmg5C1RLN0DE0ye61mricA/640?wx_fmt=png)

图2（图片来源：欧洲航天局）

除此之外，虽然网络中的关键设备要经过彻底全面的检查，但非关键设备不仅是商用现成（COTS）设备，还缺少同样严格的流程，从而导致供应链可能被攻击的途径，随后攻击者只要将未经授权的第三方组件整合到系统中，就可以激活攻击。

这时候混合关键网络派得上用场，帮助确保：即使COTS设备是恶意的，也无法干扰关键流量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28l1Y323O7vFdoqJ4ibMiclI5SYUBn9zrjBysjyibKn8qKzmibicwfou0QYZwd5rzmWr4a2oT1ZHfEMEiaQ/640?wx_fmt=png)

图3

密歇根大学电子工程和计算机科学系的助理教授Baris Kasikci表示，研究团队在PCspooF中发现了一种方法，可以让恶意的非关键设备违反TTE网络中的隔离保证。

反过来，这可以通过使用恶意设备经由以太网电缆向TTE交换机注入电磁干扰（EMI）来实现，实际上欺骗交换机发送看起来真实的同步消息（即协议控制帧或pcf），并使它们被其他TTE设备接受。

这种生成“电噪声”的电路在单层印刷电路板上仅占2.5cm × 2.5cm的空间，只需要极小的电力，并且可以隐藏在best-effort设备中，整合到TTE系统中，不会引发任何危险信号。

提到缓解措施，研究人员建议使用光耦合器或电涌保护器来阻止电磁干扰，检查源MAC地址以确保它们是真实有效的，隐藏关键PCF字段，使用像IEEE 802.1AE这样的链路层验证协议，增加同步主程序的数量，并禁用危险状态转换。

研究人员指出，研究结果表明，在一个旨在提供严格隔离保证的系统中使用通用硬件有时恰恰会破坏那些保护机制，应该以类似的方式认真检查混合关键软件系统的添加，以确保隔离机制万无一失。

Kasikci表示，TTE协议非常成熟，并且经过了严格审查，许多最重要的部分都得到了正式验证。

从某种程度上来说，这正是这种攻击令人关注的地方：研究人员能够弄清楚如何违反协议的一些保证，尽管它很成熟。但要做到这一点，又得另辟蹊径，搞清楚如何让硬件以一种协议未曾料到的方式运行。

参考及来源：https://thehackernews.com/2022/11/pcspoof-new-vulnerability-affects.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28l1Y323O7vFdoqJ4ibMiclI5snLUV1k5deeqiaaF1gZaZNt4DHZtX3ibf81Zc9coSQUzCCeRajP4KQGg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28l1Y323O7vFdoqJ4ibMiclI5l22h7G0ice1q4hWSu2vp7UBxv3nZoyhJdAGLK3kPrANJ9elR3ZcWxUg/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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