---
title: NSA提醒称朝鲜黑客正在利用薄弱的DMARC邮件策略
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519419&idx=2&sn=2bf4ebf6392d40174b31ed1eb866cb87&chksm=ea94bdd1dde334c7bcc430b56eed6790831e607ff3ae1f75e6e7007dbbaa5a57e477d02a058e&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-05-08
fetch_date: 2025-10-06T17:16:49.798887
---

# NSA提醒称朝鲜黑客正在利用薄弱的DMARC邮件策略

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQABdhUfeeJmcJwiaIU7Bka0RQibjwCVNyetRAKey1ia8Vvhp8iaVHuwcZD04hUw2iabDhMUkTQboyanBg/0?wx_fmt=jpeg)

# NSA提醒称朝鲜黑客正在利用薄弱的DMARC邮件策略

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**NSA和FBI提醒称，和朝鲜存在关联的黑客组织 APT43 利用薄弱的DMARC 策略实施鱼叉式钓鱼攻击。**

NSA和FBI 联合美国国务院提醒称，攻击者滥用配置不当的 DMARC 策略发送遭欺骗的邮件，而这些邮件似乎源自可信来源如记者、学术界和其它东亚事务专家。NSA提到，“朝鲜利用这些鱼叉式钓鱼攻击，通过获得对目标私密文档、研究和通信的非法访问权限，收集地理政治事件情报、对手的外交政策战略以及影响朝鲜利益的任何信息。”

受美国制裁的朝鲜军方情报组织机构侦察总局 (RGB) 被指是情报收集和间谍活动的幕后黑手，被指至少活跃于2012年。RGB的目的被指是利用美国、韩国和其它利益相关国家的情报支持朝鲜的国家情报目标并阻断威胁朝鲜安全稳定的政治、军事或经济威胁。

正如NSA和FBI去年披露的那样，APT43组织假冒记者和学术界发动鱼叉式钓鱼攻击，自2018年起攻击位于美国、欧洲、日本和韩国的智库、研究中心、学术机构和媒体机构。公告提到，该黑客组织的“任务是通过攻陷策略分析师和其他专家，向朝鲜政权提供被盗数据和有价值的地理政治信息，成功攻陷进一步使他们构造更可信和有效的鱼叉式钓鱼邮件，之后用于攻陷更敏感、价值更高的目标”。

**缓解措施**

该黑客组织在攻击中利用的是缺失的 DMARC 策略或配置 “p=none” 的 DMARC 策略即告知邮件接收服务器对于未通过 DMARC 检查的信息不采取任何措施。这就导致 APT43 组织通过社工的鱼叉式钓鱼邮件和此前受陷的内容触及目标的邮箱。

为缓解该威胁，FBI、NSA和美国国务院建议防御人员将DMARC 安全策略更新为使用 "v=DMARC1; p=quarantine;" 或 "v=DMARC1; p=reject;" 配置。第一个配置指示邮件服务器清理未能通过DMARC的邮件并将它们标记为“潜在垃圾邮件”，第二个配置要求它们拦截所有未能通过 DMARC 检查的邮件。

这些机构表示，“除了设置 DMARC 策略中的字段 ‘p’，这些机构建议组织机构设置DMARC策略的其它字段，如设置为 ‘rua’ 接收关于来自该组织机构域名的邮件信息 DMARC 结果的聚合报告。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[微软：APT28 利用由NSA报送的 Windows 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519350&idx=2&sn=c98c01499f531e3ceed8f1597c30c578&chksm=ea94bd1cdde3340a7c757c539d7f708d85af2ff07df6f7ceeb2c4755fea809a41f36f2e1ab53&scene=21#wechat_redirect)

[NSA承认购买敏感数据监控美国公民](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518768&idx=1&sn=e2580ef28e29b1e69a98c2d5b0a25a4f&chksm=ea94bb5adde3324ca571dfc3d000c70d5f96bcd859fdf0d43446b2a97535d3a9ba37918b7ef1&scene=21#wechat_redirect)

[CISA、NSA等联合发布关于SBOM的软件供应链安全保护新指南](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518114&idx=1&sn=fc054c7175c91a0884dd651f6f50d979&chksm=ea94b6c8dde33fde6f7e4daf2b5d2667ce13135554b2b3e871158dca1999c5b1a93fc84cd6b0&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/nsa-warns-of-north-korean-hackers-exploiting-weak-dmarc-email-policies/

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