---
title: TLSxa0早期证明（Early Attestation）的证据真的属于这条连接吗？
url: https://mp.weixin.qq.com/s/dWq3C4iisYNpgLogz7za-g
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:53:30.284137
---

# TLSxa0早期证明（Early Attestation）的证据真的属于这条连接吗？

# TLS 早期证明（Early Attestation）的证据真的属于这条连接吗？

原创

破天KK
破天KK

KK安全说

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#

    设想你要把一批敏感数据交给一个机密计算服务。TLS 握手顺利完成，服务端出示的远程证明也通过了签名验证。发送数据之前，还有一件事需要确认。

**出具这份证明的运行环境，真的是你正在通信的那个对端吗？**

这就是Muhammad Usama Sardar等 在预印本《EarlyAttestationTschüss（EAT）》中研究的问题。

## 有效证明如何被跨连接转用？

远程证明让客户端检查对端是否运行在符合预期的可信执行环境中。所谓**早期证明**，是把这份证据放进 TLS 握手，让客户端可以在握手期间检查它。

麻烦出在证据和连接的对应关系上。在论文设定的攻击条件下，部分绑定机制允许攻击者把连接 A 里的有效证据转到连接 B 中。证据的签名仍然有效，连接 B 的客户端却可能误以为是自己的对端生成了它。这就是**跨连接中继**。

## 研究发现了什么？

研究用 ProVerif 比较了 **9****种证据绑定机制**，覆盖两份 IETF 个人草案。较早的 TLS Attestation 第 10 版已标注撤回，另一份是研究所分析的 SEAT Early Attestation 第 09 版。

研究涉及的多个实现项目中，已有 **9****项漏洞获得公开****CVE****编号**，CVSS v4.0 基础评分均为 9.1。论文还讨论了所分析的 Edgeless Systems Contrast 版本和 Meta Private Processing 公开设计中的绑定风险。

## 有些项目已经调整了证明流程

研究团队按协调披露流程向维护者提交了报告。相关项目随后采取了不同的措施。

· **Privasys** 归档了用于早期证明的 Go 和 rustls 分叉仓库，转向握手后证明。

· **Ultraviolet CoCoS** 在 v0.9.0 引入了握手后绑定。

· **Edgeless Systems Contrast** 增加了可信硬件标识的配置项，用于缓解中继风险。

· **机密计算联盟（CCC）证明兴趣组**归档了用于 TLS 早期证明的概念验证仓库。

## 握手之后，证明怎么绑定？

论文讨论了一种做法。双方先完成 TLS 握手，再用从这条连接导出的密钥材料构造证明绑定值，并在验证通过后放行应用数据。

对于需要向机密计算服务交付敏感数据的客户端，放行前要回答两个问题。**这份证明是否有效？它是否绑定了我即将用来发送数据的那条连接？**

## 预印本与 CVE 记录

阅读预印本《EarlyAttestationTschüss（EAT）》：https://www.researchgate.net/publication/417343302\_EarlyAttestationTschuss\_EAT

· **Privasys** CVE-2026-108265、CVE-2026-108266、CVE-2026-108267、CVE-2026-108268、CVE-2026-108269、CVE-2026-108362

· **Ultraviolet CoCoS** CVE-2026-119344

· **Edgeless Systems Contrast** CVE-2026-100835

· **CCC Attested TLS****概念验证** CVE-2026-112377

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/niaMibh6Pic6RZBtYmiaJBItDCOn2HTsEH2xPkboCfSdwRIptZeQ8cVhB2Yicund3DyiaO2mc2mibrPJ2F4G6k00icDMZQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过