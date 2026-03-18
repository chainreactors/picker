---
title: 有效载荷勒索软件利用 Babuk 式加密攻击 Windows 和 ESXi 系统
url: https://mp.weixin.qq.com/s/iNvTtJhITvBHMEwRfR6k_g
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:18:56.312639
---

# 有效载荷勒索软件利用 Babuk 式加密攻击 Windows 和 ESXi 系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PjfelyrLur6icYpst8dZpOicwIhEz7PoqbONVs67pVTYsyzvvLz9WqrIampcOHKHyBdQrjHc3MDDu2xFNicUNmUtuAje3JCFcsX8/0?wx_fmt=jpeg)

# 有效载荷勒索软件利用 Babuk 式加密攻击 Windows 和 ESXi 系统

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

一种名为 Payload 的新型勒索软件正在迅速崛起，对 Windows 和 VMware ESXi 环境构成严重威胁，它结合了 Babuk 式加密、激进的反取证技术和有效的双重勒索模型。

该组织声称至少从 2026 年 2 月 17 日就开始活动。它已经对多个行业和国家的中大型组织造成了影响。

该医院与来自七个国家的其他 11 个受害者一起，据称从房地产、能源、医疗保健、电信和农业等行业的组织（主要位于新兴市场）共计 2,603 GB 的数据被盗。

3 月 15 日，Payload 组织在其 Tor 泄露网站上列出了巴林皇家医院，声称已窃取 110 GB 敏感数据，并设定 3 月 23 日为支付赎金的最后期限。

此次攻击遵循了现在标准的双重勒索策略：数据窃取、文件加密，并通过专门的泄露博客进行公开羞辱。

## **有效载荷勒索软件**

对 Windows 二进制文件进行逆向工程，发现其包含一个完整且实现良好的 Babuk 风格加密方案。

有效载荷使用 Curve25519 ECDH (curve25519-donna) 进行密钥交换，使用 ChaCha20 进行文件加密，每个文件的密钥对和随机数通过 CryptGenRandom 生成，并在每个文件处理完毕后从内存中安全擦除。

从操作员的公钥导出的共享秘密直接用作 ChaCha20 密钥，没有证据表明存在弱化参数、逻辑错误或嵌入式恢复密钥；如果没有操作员的私钥 Curve25519，加密数据实际上是无法恢复的。

一个显著的特点是，每个加密文件都会附加一个 56 字节的页脚，该页脚仅使用 RC4 加密，密钥为三字节的“FBI”。

可以确定的是，它具有双平台功能：一个是使用 MSVC 编译的大型、功能丰富的 Windows PE，另一个是面向VMware ESXi 主机的精简版 ELF ，通过 vmInventory 解析和多线程 VM 磁盘加密实现。

该密钥出现在 ChaCha20 sigma 常量附近的内存中，在 Windows 版本中形成“expand 32-byte kFBI”，在 Linux/ESXi 版本中形成“FBIthread-pool-%d”等痕迹，这些痕迹具有很强的检测特征，但没有实际的加密弱点。

## **双平台存储：Windows 和 ESXi**

安全遥测数据显示，目前许多引擎将 Payload 错误地标记为 Babuk，这反映了这两个引擎家族之间大量的代码重用和结构相似性。

然而，目前还没有公开证据表明 Payload 背后存在完整的勒索软件即服务生态系统，例如联盟面板或共享构建器，因此 RaaS 品牌仍未得到证实。

在 Windows 系统上，Payload 完全离线运行，扫描本地和网络驱动器，将文件重命名为 .payload 扩展名，终止备份和安全工具，删除卷影副本，并可选择擦除Windows 事件日志，同时修补 ETW 功能以实现盲 EDR。

该二进制文件通过 NTFS 备用数据流技巧删除自身，并使用名为“MakeAmericaGreatAgain”的互斥锁，从而凸显了清晰的操作者特征。

勒索信嵌入在二进制文件中，并使用 RC4 加密，指示受害者使用独特的凭证访问基于 Tor 的协商门户，并提供有限的免费解密作为能力证明。

另一个 Tor 泄露网站托管着带有倒计时的文件树和完整的数据转储，截至 2026 年 3 月中旬，这两个网站均已确认可访问。

对于医疗保健等行业而言，强大的 Babuk 式加密、针对 ESXi 虚拟机管理程序的攻击以及可信的泄露威胁相结合，会显著增加业务和安全影响，使 Payload 成为防御者在 Windows 和虚拟化基础架构中监控和搜寻的首要威胁。

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