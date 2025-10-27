---
title: 俄黑客组织 RomCom 被指利用火狐和Windows 0day攻击用户
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521617&idx=1&sn=cc6372f588d0fbc52027797f7d23ae53&chksm=ea94a43bdde32d2d7788140cbef334c7440a1777d309ce9d91bac48e50624f4f067938c35f6f&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-28
fetch_date: 2025-10-06T19:20:22.429870
---

# 俄黑客组织 RomCom 被指利用火狐和Windows 0day攻击用户

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRpkFZpBQfl02AnNia2QQCFcvQU7zHujsZnyY2NWy1iasnBib725gOGyU8ll8haT8xtDBiaVc9rhiaVSvA/0?wx_fmt=jpeg)

# 俄黑客组织 RomCom 被指利用火狐和Windows 0day攻击用户

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**俄罗斯网络犯罪团伙 RomCom 最近组合利用两个0day漏洞，攻击位于欧洲和北美的火狐和Tor浏览器用户。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRpkFZpBQfl02AnNia2QQCFc0hROv47rYJoQw4kmwRjCO1CBKCvLaPSpUGRYsY5D87odXzqIibOn0tw/640?wx_fmt=png&from=appmsg)

第一个漏洞CVE-2024-9680是位于火狐动画时间线特性中的释放后使用 (UAF) 漏洞，可导致在该web浏览器的沙箱中执行代码。Mozilla 在2024年10月9日即收到 ESET 公司报送的一天后修复了该漏洞。

第二个遭利用的是位于 Windows Task Scheduler 服务中的提权漏洞CVE-2024-49039，可导致攻击者在火狐沙箱外执行代码。微软在本月初即11月12日修复了该漏洞。

RomCom 组合利用这两个当时是0day状态的漏洞，在无需用户交互的情况下获得远程代码执行权限。他们的目标只需访问受攻击者控制和恶意构造的网站即可，之后该网站就会下载并执行系统上的 RomCom 后门。

从攻击中所用的其中一个 JavaScript exp (main-tor.js) 来看，该团伙还攻击了 Tor 浏览器用户（版本12和13）。

ESET公司的研究员 Damien Schaeffer 提到，“该攻陷链由一个虚假的网站构成，该网站将潜在受害者重定向至托管该exp的服务器，当exp成功时就会执行shellcode，从而下载并执行 RomCom 后门。虽然我们不了解该虚假网站的链接是如何分发的，但如果通过一个易受攻击的浏览器访问该网页，则无需用户交互即可释放 payload 并在受害者计算机上执行。”一旦在受害者设备上部署该恶意软件，则攻击者可运行命令并部署其它payload。

ESET公司提到，“组合利用两个0day漏洞，导致 RomCom 能够利用无需用户交互的 exp。这种复杂度表明该犯罪团伙将且目的是获取或开发隐秘能力。”此外，通过受害者设备上部署 RomCom 后门的成功尝试次数，ESET公司认为这是一次大规模的攻击活动。该公司提到，“从ESET的遥测数据来看，潜在目标的数量从每个国家一个受害者到250个受害者不等。”

这并非RomCom 首次利用0day漏洞发动攻击。2023年7月，其操纵者利用Windows 和 Office 多款产品中的一个0day漏洞 (CVE-2023-36884) 攻击在立陶宛首都维尔纽斯市举办的北约峰会的组织机构。

RomCom（也被称为 “Storm-0978”、”Tropical Scorpius” 或 “UNC2956”）一直以来以经济利益为目标，并组合利用勒索敲诈和凭据盗取攻击（可能为了支持情报活动）。该威胁团伙还被指发动“工业间谍”勒索攻击，而之后该攻击转为Underground 勒索攻击。

ESET公司提到，RomCom团伙正在攻击位于乌克兰、欧洲和北美地区的组织机构，对多种行业如政府、国防、能源、医药和保险行业发动间谍攻击。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[火狐修复神秘的严重漏洞，同时影响Chrome 浏览器](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247499209&idx=3&sn=8918330d97c1466dd0cbdb7269b05fa7&scene=21#wechat_redirect)

[这个 bug 可劫持同一 WiFi 网络上所有的安卓版火狐移动浏览器](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247495106&idx=2&sn=1b0fe939237e5dcc8a2b5feede9e847c&scene=21#wechat_redirect)

[Mozilla 加大火狐浏览器漏洞奖励力度](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247492867&idx=4&sn=ac78df4573d153307142ae9d56f4056a&scene=21#wechat_redirect)

[两年了火狐仍未修复某 0day，不料又一个新0day出现仨月了](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247491548&idx=3&sn=338a16f3cc8ce91d89cb756f7eae7a13&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/firefox-and-windows-zero-days-exploited-by-russian-romcom-hackers/

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