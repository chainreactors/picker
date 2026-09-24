---
title: 【喜报】1篇研究成果被国际顶级会议NDSS 2027录用
url: https://mp.weixin.qq.com/s/_bHQGBqL5ZVtrOijZVAHcg
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:02:47.321564
---

# 【喜报】1篇研究成果被国际顶级会议NDSS 2027录用

# 【喜报】1篇研究成果被国际顶级会议NDSS 2027录用

星图实验室
星图实验室

奇安信技术研究院

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# Windows 代码签名证书合规性及安全风险分析

      本篇论文是由奇安信技术研究院和清华大学合作完成的关于代码签名证书合规性及安全风险分析的工作。论文题目为《Standards-to-Surface: A Comprehensive Evaluation of Windows Code-Signing (Non)Compliance》，这项工作由清华大学和奇安信联合培养的卓越工程师计划博士研究生赵汉卿主导完成，导师为段海新教授(清华大学)和应凌云博士(奇安信星图实验室)。其他作者分别为张一铭(清华大学)、游子权(清华大学)、刘保君(清华大学)、张书豪(奇安信星图实验室)、金虎权(奇安信星图实验室)。这篇论文也是我们继《Understanding the Status and Strategies of the Code Signing Abuse Ecosystem》(NDSS 2026)之后的第二项代码签名 PKI 研究工作。 [【论文分享】被滥用的信任：Windows 代码签名滥用测量研究](https://mp.weixin.qq.com/s?__biz=Mzg4OTU4MjQ4Mg==&mid=2247489016&idx=1&sn=0e14a2da0f4d916c8759c197335bd855&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QSjGzxHEMdsriceUMFWJJPFyibMlVXDqdqr7j3Suh52HzC1aP5SVk6xRcA0B3q5s7xLY1mQlHQLnFAboCdE85J64jSfibD5SpKnsnv4LiafHXwc/640?wx_fmt=png&from=appmsg)

      近年来，软件供应链安全事件频发，为了保护软件真实性与完整性，代码签名机制应运而生。代码签名主要依赖公钥基础设施 PKI 技术，旨在确保软件来自真实来源且软件内容未被篡改。IETF 和 CA/B Forum 等标准化组织对代码签名证书颁发制定了一系列标准规范，CA 通过遵循这些标准规范来确保代码签名 PKI 生态系统的安全稳定运行。然而，当前代码签名生态封闭而不透明，且缺乏专门的合规性检查工具，导致实际的证书颁发实践难以被独立审计。

      为此，本工作首次对公共 CA 生态系统中的代码签名证书合规性进行了大规模测量分析。我们开发了CSLint，一款专用于代码签名证书的合规性检查工具，包含 192 条 lint 规则。我们从 40,462,203 个真实软件中提取了 215,592 张证书，构建了迄今为止最大的代码签名证书数据集，涵盖了来自 158 个国家/地区的 145 个不同 CA 颁发的证书。我们的测量结果表明，代码签名证书误颁发现象普遍且严重，6.28% 的叶子证书和 18.97% 的根证书触发了“错误”。我们还构建了 AuthentiCheck，用于分析这些不合规证书对 9 种终端验证实现的真实影响，揭示了身份欺骗、非授权证书使用以及撤销检查失效等安全风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QSjGzxHEMdudyNYicAYVoPI1R0kQ49zZoQDF5WP4EGPyMpPnHNYEeJRtS1plxRPhzulOX7AjeHf9vCzg7n0mBwR6fdKlFjYicurHJqE8fz2qQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lG0evzxL96k3J9EIwMqhiacpDHibsxFTCugUuHF9VUnGG5ceic7dILO41pMNfer7OzCyIviaBYAWAZicicVfocuO8HKw/0?wx_fmt=png)

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