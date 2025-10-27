---
title: VeraCore 两个0day漏洞被用于实施供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522257&idx=2&sn=9b28d0ae22a8aee011365d83bbe3e244&chksm=ea94a6bbdde32fad583ad06bb5abe8c191b454c50e40661e1fbba804d5ae0e3a6d9cc4164ad8&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-19
fetch_date: 2025-10-06T20:47:19.947556
---

# VeraCore 两个0day漏洞被用于实施供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSia6g9ibXm81W2NhfYicjuNlFOMmgqqwicSLhBOGE37xqS6n9omYWJ8q70yUczEae4xTHSWPF4W7RrVQ/0?wx_fmt=jpeg)

# VeraCore 两个0day漏洞被用于实施供应链攻击

Rob Wright

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**研究人员在仓库管理软件平台 VeraCore 中发现了两个遭活跃利用的0day漏洞。Intezer 和 Solis Security 公司的安全研究员发现网络犯罪团伙 XE Group 利用这两个漏洞，早在2020年就攻陷制造和分销行业的供应链。**

VeraCore 遭利用的两个0day漏洞是CVE-2024-57968和CVE-2025-25181。CVE-2024-57968是一个严重的上传验证漏洞，CVSS评分为9.9，CVE-2025-25181是一个中危的SQL注入漏洞，CVSS评分为5.8。这两个漏洞是研究人员在2024年11月5日从XE Group 发动的攻击中发现的。

攻击者攻陷了托管 VeraCore 仓库管理系统软件的互联网信息服务 (IIS) 服务器，进一步分析发现该服务器在2020年1月首次经由当时还是0day漏洞的SQL注入漏洞攻陷。

XE Group 部署了自定义 webshell，而研究员认为它们是“高度多用途”的工具，可维持对受害者环境以及SQL查询的持久访问权限。在受攻陷的IIS服务器案例中，XE Group 复用了早在四年前就植入的一个 webshell。

Intezer 和 Solis Security 网络安全公司提醒称，XE Group 正在利用制造和分销行业中的供应链。虽然XE Group 因信用卡盗刷行为为人所知，但研究人员提到该组织已增强了其能力。这两家公司在博客文章中提到，“XE Group 从信用卡盗刷到利用0day漏洞体现了其适应性和不断增加的复杂性。他们维持系统持久访问权限的能力，即在初始部署数年后重新激活webshell的行为，凸显了该组织致力于长期目标的目的。”

研究人员提到，Advantive 公司为CVE-2024-57968发布了临时修复方案，删除了 VeraCore 的上传特性。不过目前尚不清楚CVE-2025-25181是否被修复。Advantive 的一名发言人提到，“目前，尚未发现针对VeraCore 软件的已知活跃威胁。Advantive 持续评估并增强安全措施，以阻止越权访问并确保满足最高网络安全标准。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[在线阅读版：《2024中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520484&idx=1&sn=8a845b39720a318c297075e98f5fe5e0&scene=21#wechat_redirect)

[在线阅读版：《2023中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517225&idx=1&sn=8154b433ae2be87ccbae15bc0fb09a00&scene=21#wechat_redirect)

[在线阅读版：《2022中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513174&idx=1&sn=e474d1ea23ed7cce10e2ae2f872fc003&scene=21#wechat_redirect)

[新型 “whoAMI” 攻击利用AWS AMI 名称混淆实现远程代码执行](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522246&idx=2&sn=fbca692993726f368c05fa16b80eb5a8&scene=21#wechat_redirect)

[Google Cloud 依赖混淆漏洞影响数百万台服务器](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520848&idx=4&sn=5dd6c8f2b2d48123ef978d8ef1b071ff&scene=21#wechat_redirect)

[什么鬼？我能通过依赖混淆攻击在 Halo 游戏服务器中执行命令，微软不 care？！](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247506074&idx=1&sn=40b66f0cbedbc7f81a5e8ea6b5f96000&scene=21#wechat_redirect)

**原文链接**

https://www.cybersecuritydive.com/news/veracore-zero-day-vulnerabilities-exploited-in-supply-chain-attacks/739784/

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