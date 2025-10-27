---
title: 研究员利用ChatGPT制造出多态恶意软件Blackmamba
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515971&idx=2&sn=ff0c41c3c1c97f17f7831960c3252abf&chksm=ea948e29dde3073f190dc2684e4d43d3b9e7955a1598874702f220cb7c08f40ef56e9c7b48e7&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-21
fetch_date: 2025-10-04T10:09:20.980264
---

# 研究员利用ChatGPT制造出多态恶意软件Blackmamba

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRxp9icdIILIk8zmtIFl9Lia2qxGDKia6NiaiadibazSiaphTxNtX8T3H0u9AL7wTosQKQ9yjibDG2lrlUoFw/0?wx_fmt=jpeg)

# 研究员利用ChatGPT制造出多态恶意软件Blackmamba

DEEBA AHMED

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRxp9icdIILIk8zmtIFl9Lia2ZmG7KIVYwqHKhdbnyKg02tt0eaoNwxQJjoOcWoc6V76pyWGmrdc61Q/640?wx_fmt=png)

**HYAS 研究院的安全研究员兼网络安全专家 Jeff Sims 开发出一种新的受ChatGPT驱动的恶意软件 Blackmamba，它可绕过端点检测和响应 (EDR) 过滤器。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRxp9icdIILIk8zmtIFl9Lia28eSc5wx4LlaeazqEb1KyGNm4BSRwt9ap6D5G4PzIaRI13EqJzwh4jw/640?wx_fmt=png)

这一现象并不令人惊讶。就在今年1月份，CyberArk公司的研究员就报道了ChatGPT可如何被用于开发多态恶意软件。在调查过程中，研究人员能够使用命令语调，绕过ChatGPT中的内容过滤器，制造多态恶意软件。

HYAS研究院在报告中指出，该恶意软件可收集敏感数据如用户名、储蓄卡/信用卡卡号、密码和其它由用户输入的机密信息。一旦抓取到数据，Blackmamba就会利用MS Teams 将其传输到受害者的Teams频道，“被分析、在暗网出售或用于其它恶意目的”。

Jeff使用MS Teams的原因是，该软件可使他获得对组织机构内部来源的访问权限。由于与其它很多虚拟工具如Slack 连接，因此识别有价值的目标可能更易管理。Jeff 利用ChatGPT创建了多态键盘记录器，它可利用ChatGPT的语言能力，通过检查用户的输入随机修改恶意软件。Jeff 通过Python 3生成了该键盘记录器并通过每次调用ChatGPT时运行python exec()函数。也就是说，无论何时调用ChatGPT/text-DaVinci-003，它都会为该键盘记录器编写一个唯一的Python脚本。

这就使得恶意软件是多态的切无法由EDR检测到。攻击者可利用ChatGPT修改代码使其更加难以描述。之后他们甚至可以开发出恶意软件/勒索软件作者能够用于发动攻击的程序。

Jeff构造的恶意软件是可分享的、且通过auto-py-to-exe进行迁移、免费、开源的工具。这样Python代码转换到.exe文件可在多个系统上运行。另外，也可通过社工或邮件在目标环境中共享该恶意软件。

随着ChatGPT机器学习能力不断发展，毫无疑问这类威胁将继续存在且变得更加复杂又难以检测。自动化安全控制并非灵丹妙药，因此组织机构必须主动开发且执行网络安全策略，防御此类攻击。

**什么是多态恶意软件？**

多态恶意软件可在每次复制或感染新系统后修改代码和外观的恶意软件，因此传统的基于签名的杀毒软件难以检测并分析它。多态恶意软件一般通过使用多种混淆技术如加密、代码修改和不同的压缩方法实现其目标。这种恶意软件还能够通过生成新代码和唯一签名的方式实时修改，躲避安全软件的检测。

近年来，网络犯罪分子不断寻求绕过传统安全措施的创新方式，因此多态恶意软件业变得更加常见。这种恶意软件的合成能力和代码修改能力使得安全研究员难以开发出有效的防御措施，成为组织机构和个体的重大威胁。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[3·15特辑 | 少侠，可曾听说ChatGPT也有“食品安全问题”？](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515947&idx=1&sn=b56dd235a7b662303755b8335f83ec7b&chksm=ea948e41dde3075753ae1779a5395a0f4a4e4550aa2a86eb793e75e897e78c286efccd83e9cd&scene=21#wechat_redirect)

[学生利用“提示符注入”方法，攻破ChatGPT版必应搜索](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515534&idx=2&sn=e816e0c34f1deae1b5278e39c974e4ff&chksm=ea948ce4dde305f27ad16099811f247a67e25343957dfde04cb07203fa48927237f458d883d4&scene=21#wechat_redirect)

[攻击者已利用ChatGPT编写恶意代码](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515233&idx=3&sn=acc0f7a96702e65796637a360acf5510&chksm=ea948d0bdde3041dc094027cc96639bf548ab737e3da4cbb80f6cb46f6c3bad46bb7c78a2dc5&scene=21#wechat_redirect)

**原文链接**

https://www.hackread.com/chatgpt-blackmamba-malware-keylogger/

题图：Pexels License

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