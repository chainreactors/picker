---
title: Safe{Wallet}基础设施被注入恶意代码，Bybit遭供应链攻击损失15亿美元
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522342&idx=1&sn=8521c4624968b5c9a8d08e2a8af23490&chksm=ea94a94cdde3205ad200f61e3311b075c8589b84e47a3d91b3e17103cbe66dca64d78510faf2&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-28
fetch_date: 2025-10-06T20:38:15.570630
---

# Safe{Wallet}基础设施被注入恶意代码，Bybit遭供应链攻击损失15亿美元

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSia6g9ibXm81W2NhfYicjuNlFOMmgqqwicSLhBOGE37xqS6n9omYWJ8q70yUczEae4xTHSWPF4W7RrVQ/0?wx_fmt=jpeg)

# Safe{Wallet}基础设施被注入恶意代码，Bybit遭供应链攻击损失15亿美元

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**继Bybit 密币交易所的首席执行官 Ben Zhou与“Lazarus 宣战”后，美国联邦调查局 (FBI) 正式将Bybit被盗创纪录的15亿美元事件与朝鲜黑客关联在一起。**

FBI 提到，朝鲜从Bybit盗走了虚拟资产，将其归咎于被FBI追踪为 “TraderTraitor” 的特定组织，该组织也被称为 “Jade Sleet”、”Slow Pisces” 和 “UNC4899”。

FBI 提到，“TradeTraitor 组织行动迅速，已经将其中一些被盗资产转为比特币和散落在多个区块链数千个地址上的其它虚拟资产了。预计这些资产会被进一步洗钱并最终转换为法定货币。”

值得注意的是，TraderTraitor 组织此前曾在2024年5月被日本和美国当局控诉从密币公司 DMM Bitcoin 盗取价值3.08亿美元的密币。该组织因针对Web3行业企业而为人所知，它们通常会诱骗受害者下载受恶意软件感染的密币应用以便于偷盗。它们还会结合工作主题的社工活动部署npm恶意包。

而ByBit 已启动一项漏洞奖励计划，帮助恢复被盗资金，同时呼吁密币交易所拒绝与该黑客组织合作并帮助冻结资产。FBI提到，“被盗资金已被转账到无法追踪或无法冻结的目的地，如交易所、混币器、桥或者转为可被冻结的稳定币。我们要求所有涉及方与我们合作，要么冻结资金要么提供它们的动向，以便我们继续追踪。”

Bybit 公司还共享了由 Sygnia 和 Verichains 开展的两项调查所得出的结论，它们将该入侵事件与 Lazarus 组织联系在一起。Sygnia 公司表示，“对三个签名人主机的取证调查显示，此次攻击的根因是源自 Safe{Wallet}基础设施的恶意代码。”Verichains 公司提到，“app.safe.global 的非恶意 JavaScript 文件在2025年2月19日15:29:25（UTC时间）似乎已被恶意代码所取代，具体针对的是 Bybit 的以太坊多钱冷钱包，”以及“这起攻击设计为在Bybit 下次交易时激活，即2025年2月21日 14:13:35（UTC时间）。”

AWS S3或CloudFront 账号/Safe.Global 的API密钥疑似可能被泄露或受陷，因此为这起供应链攻击铺平道路。

多签钱包平台 Safe{Wallent} 单独发布声明称， Safe{Wallet} 开发者机器受陷，影响了由 Bybit 运行的一个账号。该公司还表示已执行额外的安全措施以缓解该攻击向量。该公司提到，这起攻击“通过攻陷 Safe{Wallet}开发者的一台机器，发起伪装的恶意交易实现。Lazarus 是受国家支持的朝鲜黑客组织，因为对开发者凭据实施复杂的社工攻击，有时还伴随0day利用而为人熟知。”

目前尚不清楚该开发者系统是否已受陷，不过Silent Push 发布最新分析指出，Lazarus 组织在2025年2月20日22:21:57即就在密币被盗的几小时之前注册了域名 bybit-assessment[.]com。WHOIS的记录显示，该域名是通过邮件地址trevorgreer9312@gmail[‘]com 注册的。该邮件地址此前被判定为由Lazarus组织在另一起攻击活动 “Contagious Interview” 中所用。分析提到，“Bybit时间似乎由朝鲜威胁组织TraderTraitor （也被称为“Jade Sleet”和“Slow Pisces”）发起，而该密币访谈欺诈是由 Contagious Interview （也被称为“Famous Chollima”）牵头的。它们一般通过 LinkedIn 接触受害者，通过社工诱骗他们参加虚假的工作面试。这些面试是针对性恶意软件部署、凭据收割和进一步攻陷金融和企业资产的入口点。”

朝鲜黑客组织自2017年起，被指已盗取价值超过60亿美元的密币资产。上周发生的Bybit 15亿美元被盗事件打破了该组织在2024年从47密币攻击中盗取13.4亿美元的最高记录。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMR7vxDugjW11BDCcF3ftA1QeibsYQic7dLqiaYUOBmfDP7rpiakeStycBQfn02HKia2xnrJnYsv5SWJxEQ/640?wx_fmt=jpeg)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[在线阅读版：《2024中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520484&idx=1&sn=8a845b39720a318c297075e98f5fe5e0&scene=21#wechat_redirect)

[在线阅读版：《2023中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517225&idx=1&sn=8154b433ae2be87ccbae15bc0fb09a00&scene=21#wechat_redirect)

[在线阅读版：《2022中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513174&idx=1&sn=e474d1ea23ed7cce10e2ae2f872fc003&scene=21#wechat_redirect)

[LottieFile 供应链攻击使用户密币钱包易被盗](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521357&idx=1&sn=59e85c17b04d58d9bf269db28b3f7104&scene=21#wechat_redirect)

[Solana 区块链平台疑遭供应链攻击，价值数百万美元的密币遭洗劫](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513397&idx=1&sn=00d12c4f1e09226bc9a484c7b74542aa&scene=21#wechat_redirect)

[软件供应链投毒 — NPM 恶意组件分析](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518377&idx=1&sn=9504988637a30aee727161562a17cd5a&scene=21#wechat_redirect)

[软件供应链投毒 — NPM 恶意组件分析（二）](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519078&idx=1&sn=eec7bf30c2e7abec80f62c022aa099c5&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2025/02/bybit-hack-traced-to-safewallet-supply.html

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