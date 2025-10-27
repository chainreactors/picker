---
title: 本周起，GitHub强制要求活跃开发人员执行2FA机制
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515900&idx=1&sn=7af020d3e088fab4b57a745603e09389&chksm=ea948f96dde3068079b9292ed144160bf188c1e4eae8b756deaec8121df464d81e8cde52e99d&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-14
fetch_date: 2025-10-04T09:30:43.998392
---

# 本周起，GitHub强制要求活跃开发人员执行2FA机制

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQibiadARKFNRDa4n6SDu6dsLQpHWagWMXFMXdtRqJTKGcRuFvjdJbmj6xhFHCzkOAkc9GJ8qoKoxrg/0?wx_fmt=jpeg)

# 本周起，GitHub强制要求活跃开发人员执行2FA机制

Eduard Kovacs

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQibiadARKFNRDa4n6SDu6dsLRy974P3g66LcqG1nnExuy9e3NSocyic50wcIyDa15NJxuy4CXjkKg2Q/640?wx_fmt=png)

**GitHub 要求，活跃开发人员自3月13日起在账户上启用双因素认证机制。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQibiadARKFNRDa4n6SDu6dsL50YMbAtCjfSE0v3AQGPhRianFkZu68ABBc4gJQMujqbUbJgXjibibI3xA/640?wx_fmt=png)

一旦扩展到GitHub 的整个用户库，该2FA要求将有助于保护超过1亿用户账户的安全。GitHub 将首先通过邮件通知一小部分管理员和开发人员，并在今年年底加快速度，确保无缝衔接以及用户有时间找到任何问题。

GitHub的部门产品经理 Hirsch Singhal 和产品营销主任 Laura Paine 指出，“GitHub 设计了试用性流程，用来将对用户的异常干扰和生产力损失最小化并阻止账户锁定。随着时间的发展，用户群体将被要求启用2FA机制，每组用户将基于他们所采取的措施或所贡献的代码被挑选。”如果用户账户被选定，则会收到一封邮件并在GitHub.com上看到要求参加2FA计划的横幅。之后，用户有45天的时间在账户上配置2FA机制，同时在此过程中可以照常使用GitHub账户，除了偶尔出现的提醒以外。

GitHub 将持续告知用户最后的启动期限，一旦超过该期限要求，将在访问GitHub.com时被提示要求启用2FA，否则将在访问某些特性时被拦截。

去年5月和12月，GitHub 要求所有在GitHub 上贡献代码的开发人员在2023年年底启用2FA。GitHub 已发布关于在账户上配置2FA以及在丢失2FA凭据的情况下恢复账户的详细指南。

开发人员可使用2FA或更多的2FA选项，如物理安全密钥、构建到智能手机和笔记本中的虚拟安全密钥、TOTP认证应用或GitHub 移动app。尽管在某些地方可选择基于文本信息的2FA，但GitHub 督促用户切换到安全密钥或TOTP应用，因为威胁行动者可绕过SMS 2FA或窃取SMS 2FA验证令牌，劫持开发人员的账户。

**保护软件供应链安全**

在GitHub账户上启用2FA，将通过拦截使用复用密码或被盗凭据的尝试，增强对账户接管的弹性。

这是GitHub 通过远离基于基本密码认证方式，保护软件供应链的最新举措。此前，GitHub 执行了基于邮件的设备验证并取消了为Git 运营认证设置账户密码。此外，GitHub 还在2020年11月通过REST API禁用密码认证并在2021年5月引入FIDO2安全密钥支持，保护SSH Git运营安全。

多年来，GitHub 已通过集成2FA、登入警报、拦截受陷密码使用和提供WebAuthn支持等方式增强其账户安全。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[供应链安全这件事，早就被朱元璋玩明白了](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515824&idx=1&sn=dab68a0c49b4d79f50b5c765c3bc2d89&chksm=ea948fdadde306cc2de185ca934b6c63d6e2e02e141f4612180b48e2c4ef56ec4da8bb826dd1&scene=21#wechat_redirect)

[美国发布新的国家网络安全战略：软件安全责任转移，重视软件供应链安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515818&idx=1&sn=b5311898cb66921b319dbcd3daaaca1f&chksm=ea948fc0dde306d6047987b8223144cc81342c436e80e04c4a2d0b01b5b9c6248f3bc47053a7&scene=21#wechat_redirect)

[奇安信总裁吴云坤：构建四大关键能力 体系化治理软件供应链安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515606&idx=1&sn=be020e0c8715a3f3b2c31a379ca01e0d&chksm=ea948cbcdde305aab8950259a837c775cd6fb12d0db8801e92776fcae41529ce655f3a18ff6c&scene=21#wechat_redirect)

[深度分析：美国多角色参与的软件供应链安全保护措施](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515534&idx=1&sn=32d0d289fcc99c859325f35101773d65&chksm=ea948ce4dde305f2309ea1b9ca9e601ef74b05fdc0b35935a43334c65bb8bc47ca179b818fa9&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/dozens-of-exploited-vulnerabilities-missing-from-cisa-must-patch-list/

题图：Pixabay License

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