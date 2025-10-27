---
title: Ivanti 修复Endpoint Management 软件中的严重RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520759&idx=2&sn=1fc5e0f7a15b2f6ee85191294e7148e0&chksm=ea94a09ddde3298b03f1d93d760c4ebe1bbf0831c2823c5d15bdc98a012ee7662c48075afa5d&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-12
fetch_date: 2025-10-06T18:28:48.362525
---

# Ivanti 修复Endpoint Management 软件中的严重RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRWuYWT1NicoibrNJCs8OQZMb8uDAIDhQvKv3NpuWsXfZu9VovXr2AibrG2kv4rQfUFdkjuC8ZjreTGA/0?wx_fmt=jpeg)

# Ivanti 修复Endpoint Management 软件中的严重RCE漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Ivanti 修复了位于 Endpoint Management (EPM) 软件中的一个CVSS 满分漏洞，可导致未认证攻击者在核心服务器上获得远程代码执行权限。**

Ivanti EPM 帮助管理员管理运行多种平台如 Windows、macOS、Chrome OS 和 IoT 操作系统的客户端设备。该漏洞CVE-2024-29847是因代理门户中不受信任数据反序列化弱点引发的，后者已在 Ivanti EPM 2024热补丁和Ivanti EPM 2022 Service Update 6 (SU6) 中修复。

Ivanti 在今天发布的安全公告中提到，“成功利用该漏洞可导致对EPM 核心服务器进行未授权访问。”Ivanti 公司百世，“在披露之时并未发现这些漏洞遭利用的整局。目前并未发现对可用于提供IoC清单的该漏洞的公开利用。”

Ivanti 公司还在今天修复了近24个高危和严重漏洞，它们位于 EPM、Workspace Control (IWC) 和 Cloud Service Appliance (CSA) 中。这些漏洞在被修复前均未遭在野利用。1月份，该公司还修复了位于 Ivanti EPM 中的另外一个类似RCE漏洞 (CVE-2023-39335)，它可被用于访问核心服务器或劫持已注册设备。

**安全性增强，已披露和修复漏洞增多**

Ivanti 公司表示，已在最近几个月升级内部扫描、手动利用和测试能力，同事正在着手改进负责任披露流程来更快解决潜在问题。

该公司指出，“这引发发现和披露量激增，我们认同CISA关于负责任发现和披露CVE的声明是‘健康代码分析和测试社区的一个标志’。”这一声明出现在近几年 Ivanti 多个0day漏洞遭在野利用发生之后。例如，Ivanti VPN 设备自从2023年12月开始就被通过组合利用CVE-2024-21887命令注入和CVE-2023-46805认证绕过0day遭攻击。该公司还在2月提醒称第三个0day漏洞CVE-2024-21893遭利用，可导致攻击者绕过易受攻击ICS、IPS和ZTA网关上的认证。

Ivanti 公司在全球拥有7000多个合作伙伴，超过4万家企业通过其产品管理IT资产和系统。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Ivanti 修复Endpoint Manager 中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519584&idx=3&sn=2aa72d7f1d783c31f298fa9a0f01f07f&chksm=ea94bc0adde3351c1cf417917d51eb468cc181088b1cf49ea4d38cc9f05da775e3aa19c6dd05&scene=21#wechat_redirect)

[Ivanti：注意！Avalanche MDM 解决方案中存在多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519303&idx=2&sn=e86decfa003bf7ebcb19d43552440c7f&chksm=ea94bd2ddde3343b1eba25473eb57c432ce40d7ded22623619060fbc6c299c461dc0087f1d1b&scene=21#wechat_redirect)

[产品中又现4个漏洞，Ivanti 宣布安全大检修](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519242&idx=1&sn=6c9094b038e67aea0f2968fffbb125e0&chksm=ea94bd60dde334764a9154d61f5809e1fd0a977ba3617a96d698def9b968b04b3039d7ecc3b2&scene=21#wechat_redirect)

[Ivanti 修复由北约报送的严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519117&idx=1&sn=cde689326429491acd44848ceeacab57&chksm=ea94bae7dde333f1f0011d550d4f6a0c206cfdb62dda27f77ba6e432c6883a80c8ff30be2a51&scene=21#wechat_redirect)

[Ivanti 披露两个新0day，其中一个已遭利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518800&idx=2&sn=81cdaabe53353075dd5badd918a3e0cd&chksm=ea94bb3adde3322ca6046c2aa9cb37dedf686efcdd6be90bd63248f23ad20dcc4015a3007149&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/ivanti-fixes-maximum-severity-rce-bug-in-endpoint-management-software/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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