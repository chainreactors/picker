---
title: 苹果紧急修复被用于“极其复杂”攻击中的0day漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522200&idx=2&sn=a8084137286ce6cbebda935ab8c0d5c2&chksm=ea94a6f2dde32fe49daed48eb8edd329d603e903408e746f6d6d111473da1914de662d214989&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-12
fetch_date: 2025-10-06T20:36:44.868708
---

# 苹果紧急修复被用于“极其复杂”攻击中的0day漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRiaKj8s9xwrEGde6wdNEGMqQA4qEaF9nqOF3ibRRDnmQKnK7Ip1HLFQWJlVzmXCN2N2vLiabStj8W0g/0?wx_fmt=jpeg)

# 苹果紧急修复被用于“极其复杂”攻击中的0day漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**苹果公司推出紧急安全更新，修复了已被用于针对性的“极其复杂的”攻击活动中的一个0day漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRiaKj8s9xwrEGde6wdNEGMqJfyRiaicibmc6zkL7HYZPqg1wCsMKvtvDXyb9pc8mJAsNUuiaAFARKN9UQ/640?wx_fmt=gif&from=appmsg)

苹果公司在一份安全公告中提到，“一场物理攻击可能禁用被锁定（iPhone 和 iPad）设备上的 USB 受限模式。苹果了解到该漏洞可能已被用于一次极其复杂的针对特定个体的攻击活动中。”

USB受限模式是一个安全特性（大约在7年前引入 iOS 11.4.1），可拦截USB零件在设备被锁定时间超过1小时的情况下创建数据连接。该特性旨在拦截取证软件如 Graykey 和 Cellebrite（通常用于执法部门）从被锁定的 iOS 设备中提取数据。

去年11月，苹果公司引入另外一个安全特性（被称为“不活跃重启”），在长时间闲置之后重启iPhone设备，以重新加密数据，使取证软件更难以提取。

该0day漏洞（CVE-2025-24200，由公民实验室的研究员 Bill Marczak 发现）是授权问题，已由苹果公司通过改进状态管理，在 iOS 18.3.1、iPadOS 18.3.1和iPadOS 17.7.5中修复。

该0day漏洞影响的设备包括：

* iPhone XS及后续版本。
* iPad Pro 13英寸、iPad Pro 12.9英寸 第三代及后续版本、iPad Pro 11英寸 第一代及后续版本、iPad Air 第三代及后续版本、iPad 第七代及后续版本以及 iPad mini 第五代及后续版本。
* iPad Pro 12.9英寸第二代版本、iPad Pro 10.5英寸 和iPad 第六代版本。

尽管该漏洞仅被用于针对性攻击中，但苹果公司仍然强烈建议用户立即安装今天发布的安全更新，拦截正在进行的攻击尝试。

虽然苹果公司并未提供关于该漏洞的在野利用情况，但公民实验室的安全研究员常常披露被用于攻击高风险个体如记者、反对党和异见人士的针对性监控软件攻击中。公民实验室曾披露苹果公司在2023年9月紧急修复的两个0day漏洞（CVE-2023-41061和CVE-2023-41064），它们被滥用于两点几利用链（被称为BLASTPASS），通过NSO集团的商业监控软件 Pegasus 感染完全修复的 iPhone 设备。

上个月，苹果修复了2025年已遭利用的第一个iPhone 0day漏洞（CVE-2025-24085）。2024年，苹果公司共修复6个已遭利用的0day漏洞，而在2023年，该公司修复了20个0day漏洞。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[苹果紧急修复已遭利用的两个0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521533&idx=1&sn=1ab7c5da3e583e48ee67d6f50fd4d97e&scene=21#wechat_redirect)

[苹果紧急修复已遭利用的两个新 iOS 0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519003&idx=1&sn=87b2f80deede9f2cb8e1092e9732820f&scene=21#wechat_redirect)

[苹果修复2024年遭利用的第1个0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518729&idx=1&sn=022dec20b1d19ed71466fd78c5c9b7c1&scene=21#wechat_redirect)

[苹果紧急修复两个 iOS 0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518251&idx=1&sn=b501407684b48f59fb89d2d77570a27c&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/apple/apple-fixes-zero-day-exploited-in-extremely-sophisticated-attacks/

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