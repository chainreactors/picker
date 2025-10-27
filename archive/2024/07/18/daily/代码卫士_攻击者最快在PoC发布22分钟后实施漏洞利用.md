---
title: 攻击者最快在PoC发布22分钟后实施漏洞利用
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520084&idx=1&sn=011fff146cf764aa7cd74c6ce7c7fee4&chksm=ea94be3edde337289cc63b9bda937c13e46e7db1daa495e49f84c43a4d1d73f78bca1024bfe3&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-18
fetch_date: 2025-10-06T17:45:06.943319
---

# 攻击者最快在PoC发布22分钟后实施漏洞利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRuyPCCn03PoqjFg1NPW9MqUXsIqzHcaVp0ic9bicRV0RDzxuiaQWVQYwUC3zH91dpCibkjwP4b7wPU2A/0?wx_fmt=jpeg)

# 攻击者最快在PoC发布22分钟后实施漏洞利用

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**威胁行动者在实际攻击中利用已有 PoC exp的速度很快，有时在 exp 公开发布22分钟后就实施利用。**

这是Cloudflare 公司在《2024年应用安全》报告中提到的。该报告覆盖的时间范围为2023年5月至2024年3月，提出了新型威胁趋势。Cloudflare 目前每秒平均处理5700万个 HTTP 请求，仍然看到已披露CVE漏洞的增强扫描活动，其次是命令注入和武器化已有 PoC 的尝试。

在审计期间，最常被针对的漏洞是Apache 产品中的CVE-2023-50164和CVE-2022-33891、Coldfusion 中的CVE-2023-29298、CVE-2023-38203和CVE-2023-26360以及MobileIron中的CVE-2023-35082。

武器化速度加快的一个典型案例是CVE-2024-27198，它是位于 JetBrains TeamCity 中的一个认证绕过漏洞。Cloudflare 公司观察到，就在该漏洞 PoC 发布22分钟后，攻击者就部署了利用，导致防御人员根本没有修复机会。该公司表示，对抗这一利用速度的唯一方法是应用AI助手，快速开发有效的检测规则。

Cloudflare 公司在报告中提到，“已披露CVE漏洞的利用速度一般要快于人类可以创建WAF规则或创建并部署补丁缓解攻击的速度。这也适用于我们公司内部负责WAF 管理规则集的安全分析师团队，这些规则集促使我们结合利用人类编写的签名和基于机器学习的方法，实现低误报和快速响应之间的最佳平衡。”

Cloudflare 公司表示，造成这种情况的部分原因是专注于某些CVE分类和产品的某些威胁行动者深刻了解如何快速利用新的漏洞披露。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRuyPCCn03PoqjFg1NPW9MqG7FqG86xGYb7w62wkvEoWSx8nBQd7qMFDFM0wBc7Jr8M02icgDHh6Dw/640?wx_fmt=gif&from=appmsg)

**6.8%的互联网流量是 DDoS**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRuyPCCn03PoqjFg1NPW9MqM8GHLZicibQZM91CjXlh48t08bQSsNZiafaicolu8YYL7wtu4zWHmLxOAg/640?wx_fmt=gif&from=appmsg)

Cloudflare 报告提到另一个令人震惊的发现是，在所有的日常互联网流量中，6.8%是分布式拒绝服务流量，旨在渲染合法用户无法使用的在线应用和服务。相较于过去12个月（2022-2023）期间的6%，这表明DDoS 攻击的整体规模在增长。

Cloudflare 公司表示，在大型的国际攻击事件中，恶意流量可能占所有HTTP流量的12%。Cloudflare 报告指出，“仅关注 HTTP 请求，Cloudflare 在2024年第一季度每天平均拦截2090亿次网络威胁（同比增长86.6%），比去年同期有了巨大增长。”

另外，报告还为防御人员提供了相关建议以及对所编写数据的更多洞察。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Exim 严重漏洞绕过150万台邮件服务器上的安全过滤器](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520065&idx=3&sn=21cb4f355ee0bab1701bb08f51762ec4&chksm=ea94be2bdde3373dfc868593abd771ecbb459d693ae8380f13889033e7ee376363a3f81dfdae&scene=21#wechat_redirect)

[谷歌系统和应用的最高漏洞奖励提升至5倍，达151k美元](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520048&idx=1&sn=b45bc25ca26f3d26e25a19aee6ea8983&chksm=ea94be5adde3374c9d5414f997b3638d7d79da17552a9b352f161c5b61fcf33781d778fbdfb6&scene=21#wechat_redirect)

[VMware 修复Aria Automation 中严重的SQL注入漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520038&idx=1&sn=c47470c41eba485c6761c101be23ab04&chksm=ea94be4cdde3375a05493cfa38283ce2ea210148cf20f12ae01666d4ae7d06828b0073a00526&scene=21#wechat_redirect)

[GitLab 又爆新的CI/CD管道接管漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520065&idx=2&sn=2dfd0b72bc28e69fa94a19fdb4828ace&chksm=ea94be2bdde3373d1294a08d90375f52d1f101e29fb038fd092aa8b03a83c90099f9a89ab166&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/hackers-use-poc-exploits-in-attacks-22-minutes-after-release/

题图：Pexels License

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