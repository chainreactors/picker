---
title: Pipecat 语音代理可遭严重 RCE 漏洞利用劫持
url: https://mp.weixin.qq.com/s/W446pdxEzlFNJgAa4zfzqw
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:09:28.944580
---

# Pipecat 语音代理可遭严重 RCE 漏洞利用劫持

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfUF5nBTsI62eBCS772EqxSLCJMzdglTlybD8HMO1I7o6icsRiczMABF0g0fDTrLBvTUr17iaXjs4Zicsj5EXyeC2TSqduy1xPV16Ss/0?wx_fmt=jpeg)

# Pipecat 语音代理可遭严重 RCE 漏洞利用劫持

DDoS
DDoS

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**用于构建语音及对话代理的热门开源 Python 框架Pipecat 中存在一个严重漏洞CVE-2025-62373，CVSS 评分高达9.8分，可导致远程代码执行（RCE）后果。**

该漏洞出在一个已弃用且无文档记录的组件LivekitFrameSerializer 上，为面向网络的应用中不安全的反序列化操作敲响了警钟。该漏洞的核心在于 Python 的 pickle 模块。该模块虽然功能强大，但序列化与反序列化的方式也以不安全著称。LivekitFrameSerializer 原本用于转换音频帧以实现与 LiveKit 的集成。然而，其 deserialize() 方法被指会直接将来自 WebSocket 客户端的不可信数据，未经任何校验便传入 pickle.loads() 函数中。

技术摘要解释称该类的 deserialize() 方法对从 WebSocket 客户端接收到的数据直接使用了 Python 的 pickle.loads()，未进行任何验证或清理。这意味着恶意 WebSocket 客户端可以发送特殊构造的 pickle 载荷，从而在 Pipecat 服务器上执行任意代码。

由于 pickle 能够实例化任何 Python 对象，并在反序列化过程中执行代码，攻击者可构造恶意的二进制对象。一旦该对象被“反序列化”，攻击者就能以 Pipecat 服务所拥有的权限，完全控制宿主系统。

虽然 LivekitFrameSerializer 并未默认启用，但任何为支持 LiveKit 而显式选择使用该组件的开发者，都面临着极高的风险。位于同一网络，或是服务暴露于公共互联网中的情况下，攻击者只需发送一条恶意消息，即可实现完整的远程代码执行，从而能够：

* 执行任意操作系统命令
* 安装恶意软件或勒索软件
* 横向渗透至组织网络内的其他敏感系统

Pipecat 维护者已在 0.0.94 版本中正式修复了该漏洞。有漏洞的类已被弃用，取而代之的是更安全的 LiveKit Transport 方法。

建议开发者：

* 立即升级：迁移至 Pipecat 0.0.94 或更高版本，以完全消除风险。
* 消除不安全反序列化：彻底停止使用 LivekitFrameSerializer。
* 采用安全格式：使用 JSON、Protocol Buffers 或 MessagePack 等在解析时不会执行代码的标准化格式。
* 网络加固：尽可能将服务绑定到本地回环地址（127.0.0.1），并对所有 WebSocket 连接实施强认证与授权机制。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Anthropic MCP 设计漏洞可导致 RCE，威胁 AI 供应链安全](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525820&idx=1&sn=43dddbdd81acc2370c91e72867508c0f&scene=21#wechat_redirect)

[Axios 严重漏洞可导致 RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525768&idx=2&sn=b8967ced3022f4f88a311a652e635650&scene=21#wechat_redirect)

[Marimo 高危预认证 RCE 漏洞已遭活跃利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525746&idx=2&sn=777605c08e8d6f2e0dbad63e8f408da4&scene=21#wechat_redirect)

[开源平台 Flowise 中的满分 RCE 漏洞已遭在野利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525680&idx=1&sn=5dbab9da81c7d42eda6c2082c7f2ac03&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/pipecat-rce-vulnerability-cve-2025-62373-pickle-deserialization/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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