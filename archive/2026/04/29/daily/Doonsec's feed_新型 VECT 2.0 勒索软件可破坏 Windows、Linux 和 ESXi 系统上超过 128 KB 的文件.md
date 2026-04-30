---
title: 新型 VECT 2.0 勒索软件可破坏 Windows、Linux 和 ESXi 系统上超过 128 KB 的文件
url: https://mp.weixin.qq.com/s/rp85FK3zKX3GPpIOGcdMJA
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:26:21.395292
---

# 新型 VECT 2.0 勒索软件可破坏 Windows、Linux 和 ESXi 系统上超过 128 KB 的文件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7OEiawpjfk4TZMEFRza97C59O7icoUXjjKL4uXcvLZVTLJeQhxxd8aSNjF9mLQ1ohOPvxYFbq8Klb57LNLcveK1ttYiaLgDh188fE/0?wx_fmt=jpeg)

# 新型 VECT 2.0 勒索软件可破坏 Windows、Linux 和 ESXi 系统上超过 128 KB 的文件

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一种名为 VECT 2.0 的新型勒索软件因其设计中存在严重缺陷而引起了网络安全界的广泛关注。

与典型的勒索软件锁定文件并要求支付赎金才能解密不同，VECT 2.0 会永久销毁任何大于 128 KB 的文件，即使受害者支付赎金也无法恢复。

VECT 勒索软件于 2025 年 12 月首次出现在一个俄语网络犯罪论坛上，以勒索软件即服务 (RaaS) 程序的形式运行。

该组织于 2026 年 1 月声称其首批两名受害者，并于 2026 年 2 月发布了 2.0 版本，将其影响范围扩大到 Windows、Linux 和 VMware ESXi 系统。

2026 年 3 月，VECT 宣布与 TeamPCP 建立合作关系，该恶意软件因此获得了更多关注。TeamPCP 是一个威胁行为体，其通过供应链攻击将恶意软件注入到广泛使用的软件包中，包括 Trivy、Checkmarx KICS、LiteLLM 和 Telnyx，从而影响了大量下游用户。

Check Point Research 的分析师通过 BreachForums 帐户访问构建器面板后，识别并分析了所有三个 VECT 2.0 变体。

他们的调查发现，VECT 还与 BreachForums 本身建立了合作关系，让每个注册论坛成员都能免费以联盟成员的身份部署勒索软件。

这种开放式联盟模式取消了通常的审查流程，大大降低了经验不足的攻击者加入行动的门槛。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7O5XoS47ibDgGLgBiaFDFjsuGpD22qzDmITAdBsqHc5G8tjnK7icVqGhzK6dF2yhCdHkalLIYjo9qP21R4sRZbBooFYUzdLlNDtjY/640?wx_fmt=png&from=appmsg)

该勒索软件使用 C++ 编写，并通过静态编译的可执行文件攻击所有三个平台，这些可执行文件共享一个通用代码库。

每个变种都使用 libsodium 加密库中的 ChaCha20-IETF (RFC 8439) 密码，并将加密文件重命名为 .vect 扩展名，在每个受感染的系统上留下一个名为 !!!READ\_ME!!!.txt 的勒索信。

尽管其构建面板设计精美，但其技术执行远不及专业开发的勒索软件工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7P47Rn9VIGDJGugVevecXyYdjyACwAGoUvHqMk3ueYo6OwXtVU2nHn8CeVjUbRK89pMyHlFnPOInMsMnSpwfAY0jeW2hzptvicI/640?wx_fmt=png&from=appmsg)

VECT 2.0 最令人担忧的方面是其存在一个严重的编码缺陷，该缺陷实际上使其变成了一个数据擦除器。

任何超过 131,072 字节（128 KB）的文件都不会被正确加密，而是永久无法恢复，这针对的是组织赖以维持运营的资产。

## **导致大型文件损坏的随机数处理缺陷**

问题的核心在于 VECT 2.0 在文件加密过程中处理加密 nonce 的方式存在根本性错误。

当恶意软件处理一个大文件时，它会将文件分成四个部分，并使用新生成的随机 12 字节 nonce 对每个部分进行加密。

所有四个加密调用都将它们的 nonce 写入同一个共享内存缓冲区，这意味着每个新的 nonce 都会覆盖前一个 nonce。

加密完成后，只有第四个也是最后一个数据块中的 nonce 值会保留下来，并写入磁盘上的加密文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7MglOosf1UHHhjQORBPFcnptRVoXYic5Jlx42dhFOialV6cFhoaV2e32CZ0IrbTlyX8oibNKiapxSNZPUzKQxibzPjJn8X844uNvBy0/640?wx_fmt=png&from=appmsg)

由于 ChaCha20-IETF 解密需要加密密钥和精确匹配的 nonce 才能还原每个数据块，因此任何大文件的前四分之三都是任何人都无法恢复的。

在所有三种勒索软件版本中，被丢弃的随机数都不会保存到磁盘、存储在注册表中，也不会发送到攻击者的服务器。即使受害者全额支付赎金，攻击者也无法提供有效的解密器，因为解密所需的随机数在缓冲区被覆盖的那一刻就永久丢失了。

这个阈值仅为 128 KB，几乎可以捕获所有有意义的文件类型，从 VM 磁盘映像和数据库到备份、电子表格和电子邮件存档。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7OtaVfAGzWpuZ2AbNGq6EnzibtoxHxHTicPmtj279ibUjB8EKTz4uGej71oicWsmD6NdXichtxkhsjHjXc5z8PcLlaYeUE1AZJhWauY/640?wx_fmt=png&from=appmsg)

Check Point Research 证实，所有三个平台变体中都存在此缺陷，并且该缺陷早于 2.0 版本发布，在早期部署中就已存在，但从未得到修复。

组织应保留离线、物理隔离的备份，这些备份无法通过网络共享或横向移动访问。

监控批量进程终止、突然删除卷影副本以及批量将文件重命名为 .vect 扩展名，可以及早发现活跃的感染。

鉴于 VECT 与 TeamPCP 的合作关系，验证第三方软件依赖项的完整性也是一个至关重要的步骤。

安全团队应注意通过 PowerShell 禁用 Windows Defender、清除事件日志活动以及异常的安全模式启动配置更改，所有这些都是此勒索软件的关键行为指标。

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