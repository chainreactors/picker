---
title: 科罗拉多大学博尔德分校 | TLS在审查规避中的使用
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491379&idx=1&sn=cb353c09c933eb1a0f0f530405f99c85&chksm=fe2ee0b8c95969aec5786c80c4e3f2bd2cb5d94302df28b7c0bdba0e08008afb42903cc6531a&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-11-16
fetch_date: 2025-10-06T19:18:10.560881
---

# 科罗拉多大学博尔德分校 | TLS在审查规避中的使用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WEYyicKFo4kgZQCWjRj3FKdK4aHRicHq6xJQhnfrRDS8cquJ6NiaDEcddYHyMmmf2D5l9fBaO0dAkxAQ/0?wx_fmt=jpeg)

# 科罗拉多大学博尔德分校 | TLS在审查规避中的使用

原创

宋坤书

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEYyicKFo4kgZQCWjRj3FKdKXywM6giccPsjJ51l7vib2DVkfqRy2tsvOgS89mqzA4YVctheauQqcB9Q/640?wx_fmt=png&from=appmsg)
> *原文标题：The use of TLS in Censorship Circumvention*
> *原文作者：Sergey Frolov, Eric Wustrow*
> *原文链接：https://dx.doi.org/10.14722/ndss.2019.23511*
> *发表会议：NDSS*
> *笔记作者：宋坤书@安全学术圈*
> *主编：黄诚@安全学术圈*

### 1、研究背景

TLS协议已成为互联网上保护网络通信的主流协议，随着越来越多的网站和服务转向TLS，其采用率不断上升。为了逃避审查，规避工具开始利用TLS作为传输协议。然而，由于TLS握手的第一个消息（Client Hello）以明文方式发送，包含加密功能、密钥交换算法和扩展的支持等信息，审查者仍能轻易识别和封锁工具，如Tor和meek等。因此，单纯使用TLS并不足以实现有效的规避。

本文研究了真实世界中的TLS握手，并对比了几种规避工具的握手特征。通过收集超过110亿个TLS连接数据，并生成基于Client Hello的指纹，作者将相同实现的TLS连接分组以便分析。结果显示，诸如Signal、Lantern、Snowflake等工具的握手中存在易被识别的问题，而Psiphon和meek虽然问题较小，但也未完全规避审查。

### 2、TLS协议概述和关键拓展

TLS协议通过在客户端和服务器之间进行握手来建立安全的通信。握手过程的第一步是客户端向服务器发送Client Hello消息，其中包含TLS版本、支持的加密套件、压缩方法等信息。通过这些信息，服务器能够确认客户端的加密能力，并进行相应的响应。重要的TLS扩展包括：SNI（服务器名称指示）、支持的加密群组、签名算法、ALPN（应用层协议协商）等，它们不仅影响TLS连接的建立，也成为审查系统用来识别特定客户端行为的关键特征。

为了避免在使用TLS时遭到检测，反审查工具（如Psiphon、meek、Signal等）会通过模仿主流TLS客户端（如Chrome、Firefox）的指纹，来混淆其流量。然而，由于这些工具的TLS握手常常生成独特且稀有的指纹，审查系统能够通过指纹库识别并阻止这些流量。TLS握手过程如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEYyicKFo4kgZQCWjRj3FKdKZMXW1EzKKG9lpH3wFMU8Uk4mwe8AU05YOjY5BESRh9nfIzOb4PyiaUQ/640?wx_fmt=png&from=appmsg)

### 3、研究方法与数据集

研究者在10 Gbps校园网络上设置了一个数据包监控系统，使用配备双端口Intel 10GbE网络适配器的单台服务器，捕获并过滤TCP 443端口上的TLS连接数据。研究团队用Rust编写了数据包处理代码，识别并解析TLS Client Hello消息，成功率达到96.7%。数据收集基础设施设计如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEYyicKFo4kgZQCWjRj3FKdKqOfFSt6LiaFMLjLDgtTJcQgp4wZ7b22mCgsglvjAh7T3Be7qxaYdFhQ/640?wx_fmt=png&from=appmsg)

本文收集了三类数据：唯一Client Hello指纹的计数和粗粒度时间戳；每个唯一Client Hello的SNI样本和匿名连接特定元数据；以及Server Hello响应数据。通过哈希算法为Client Hello消息生成指纹ID，并将连接数存储在PostgreSQL数据库中。此外，记录了部分连接的目标服务器IP、SNI和匿名客户端IP信息，用于识别指纹的来源。

为更好地匹配指纹，本文还使用BrowserStack平台进行了200多个浏览器/平台组合的自动化测试，并收集了超过270个唯一指纹。研究发现一些浏览器（如Chrome）会根据扩展项和请求大小生成多个指纹，而GREASE扩展会随机添加项，为避免产生过多指纹，研究团队对其进行了标准化处理。

### 4、主要发现

分析结果表明，现有的审查规避工具普遍面临TLS指纹易被识别的问题，尤其是在Client Hello消息中生成的特征与主流浏览器不一致时。具体而言，Signal、Lantern、Snowflake等工具由于生成稀有且独特的指纹，易于被审查系统识别和封锁。而Psiphon和meek等工具尽管存在一定的指纹问题，但相较于其他工具，风险较小。然而，Psiphon的部分指纹在未发送SNI时更容易暴露，因此仍面临被审查的风险。研究团队向工具开发者反馈了指纹检测风险，部分开发者（如Psiphon和Lantern）已通过引入uTLS库调整指纹控制，提升隐蔽性；Signal则因禁用域前置规避了被检测风险。

### 5、uTLS库的设计与改进

为了帮助规避TLS指纹识别，本文开发了一个TLS库——uTLS，它允许开发者轻松模仿任意的Client Hello消息，并在多个反审查工具中得到了应用，如Psiphon、Lantern和TapDance。uTLS库作为Golang原生TLS库（crypto/tls）的一个分支，增加了2200多行代码，提供了低级别的握手访问，使开发者能够定制TLS特性，如加密套件、压缩方法、客户端随机值、扩展等。

#### 5.1 uTLS的特点和功能

1. 低级访问与模仿能力：uTLS允许开发者访问Client Hello消息的各个字段，并提供了预设的Client Hello消息模板（如Chrome 64、Firefox 58和iOS 11）来进行模仿。虽然模仿可能存在误差，但uTLS已验证能够有效模仿流行的客户端。
2. 随机指纹：uTLS支持生成随机指纹，避免被审查系统识别和封锁。尽管这些指纹可能不会与流行实现匹配，但这使得审查者很难建立全面的指纹白名单。
3. 多指纹切换：uTLS支持多个指纹的切换，确保即使某些指纹被封锁，工具也能继续运行。uTLS会在重新连接时自动重试最新的有效指纹，从而最大限度减少无效尝试。
4. 自动代码生成：uTLS提供自动生成的代码，允许开发者轻松配置和使用特定的指纹。这使得工具开发者能够及时跟进指纹的变化。
5. 伪造会话票据：uTLS支持发送伪造的会话票据，帮助减少连接中断和被封锁的风险，特别是在开发者控制服务器的情况下。

#### 5.2 支持的指纹（可以模仿的）与TLS 1.3支持

uTLS支持21940个指纹（约占所有TLS连接的9.3%），若启用弱加密套件，则支持22616个指纹，涵盖了37.3%的连接。通过增加支持更多TLS扩展（如ChannelID扩展），uTLS能够进一步扩展其支持的指纹数量，提升工具的隐蔽性。

随着TLS 1.3的普及，uTLS也已支持该协议，能够模仿Firefox和Chrome的TLS 1.3握手，并计划继续扩展对更多TLS 1.3特性的支持。TLS 1.3的加密证书和加密SNI（ESNI）等新特性有望为规避审查提供额外帮助。

总体来说，uTLS提供了强大的工具，使得反审查工具能够更有效地规避TLS指纹识别，尽管仍存在一定风险。随着TLS协议的发展和浏览器/操作系统的更新，uTLS将继续适应这些变化，保持反审查工具的有效性。下图使用uTLS库和标准TLS库远程服务器进行连接并发送数据的对比，体现了uTLS的便利性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEYyicKFo4kgZQCWjRj3FKdKybmBAoHRdE8fbxpfzmr8rTSWBVP8r7qEs26tMEEgugAcA3vSpjxfqw/640?wx_fmt=png&from=appmsg)

尽管uTLS在规避审查中取得了一定的成功，但其仍需不断更新，以应对TLS协议及浏览器实现的变化。例如，TLS特性的更新可能导致某些指纹的过时，因此反审查工具必须不断调整其指纹以保持隐蔽性。此外，工具的成功还依赖于是否能够合理模拟流行的TLS客户端，以降低因不一致而被封锁的风险。

### 6、结论和贡献

本研究通过深入分析TLS协议中的指纹识别机制，揭示了现有审查规避工具面临的指纹识别与封锁风险。特别是，当工具未能成功模仿主流浏览器或生成与流行指纹一致的TLS握手时，其流量容易被审查系统识别和封锁。通过uTLS库的开发与应用，反审查工具能够更好地控制TLS指纹，实现更高效的规避策略。未来的研究应继续关注如何通过改进TLS指纹的模拟与随机化策略，提高反审查工具的隐蔽性，并不断应对新的审查技术和TLS协议的变化。

本文主要贡献如下：

1. 收集和分析了超过110亿个TLS Client Hello消息，以及59亿个TLS Server Hello消息；
2. 分析了现有的使用或模拟TLS的审查规避项目，发现许多项目在实践中很容易识别，并且有被审查者阻止的潜在风险；
3. 开发了一个库uTLS，它允许开发人员轻松地模仿流行实现的任意TLS握手，允许审查规避工具更好地伪装自己免受审查。同时，使用收集到的数据来增强uTLS，允许自动模拟流行的TLS实现；
4. 通过网站 https://tlsfingerprint.io 发布收集到的数据集，允许研究人员浏览流行的TLS实现指纹，搜索对密码、扩展或其他加密参数的支持，并比较由他们自己的应用程序和设备生成的TLS指纹。

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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