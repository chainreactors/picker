---
title: PyPI 恶意包窃取Discord 开发人员的认证令牌
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522124&idx=2&sn=98991414f4675f83bbb4a3935a2f16e1&chksm=ea94a626dde32f3016b9b39f894f63db177129413333eaf003c2ded003a435725967bc152c92&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-21
fetch_date: 2025-10-06T20:10:56.510516
---

# PyPI 恶意包窃取Discord 开发人员的认证令牌

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMR6ZOFfCoxsatfJYRKOJRvxG9UeCLICic2IDibb5UevjCegZLqUffl5TJBeTBqJAtSwGLZcqCogRtPw/0?wx_fmt=jpeg)

# PyPI 恶意包窃取Discord 开发人员的认证令牌

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**PyPI平台上的恶意包 “pycord-self” 窃取 Discord 开发人员的认证令牌并在系统上植入远程控制后门。**

该恶意包模拟的是非常热门的包 “discord.py-self”，后者下载量近2800万次，允许与 Discrod 的用户API进行通信并可视化开发人员从程序上控制账户。该包通常用于消息和自动化交互，创建 Discord 机器人，编写自动化主持、通知或响应，并在无需机器人账户的情况下从Discord运行命令或检索数据，而恶意包 “pycord-self” 甚至会提供该合法项目的功能。

代码安全公司 Socket 表示，该恶意包在去年6月被纳入 PyPI 平台，目前为止的下载量达到885次。在本文发布之际，该包依然可用，而其发布者的详情已获得平台验证。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMR6ZOFfCoxsatfJYRKOJRvxLnh6dhEw0rYqg3Vxe7pmmLYelOEdyHSmS3Bp5r0euUSjpBKpO2aRZg/640?wx_fmt=png&from=appmsg)

**窃取令牌，获得持久访问权限**

Socket 公司的研究人员分析该恶意包发现，pycord-self 中包含的代码可执行两个操作。第一个是窃取受害者的Discord 认证令牌并将其发送给一个外部URL。攻击者可利用被盗令牌劫持开发人员的 Discord 账户而无需访问凭据，即使双因素认证防护措施为活跃状态也不例外。

该恶意包的第二个功能是，通过端口6969创建与远程服务器的持久性连接，设置隐秘的后门机制。研究人员提到，“根据操作系统的不同，它会启动一个shell（Linux 系统上为 bash，Windows 系统上为cmd），使攻击者持续访问受害者的系统。该后门在一个单独线程中运行，因此当该包仍然看似正在运行时，难以被检测到。”

建议软件开发人员在安装程序包之前先查看该官方作者的代码，尤其如果该包是热门包的话。验证该程序包的名称也可降低受害者遭 typosquatting 攻击的风险。

在与开源库进行协作时，建议先查看代码中的可疑函数，避免使用任何看似混淆的函数。另外，使用扫描工具也有助于检测和拦截恶意包。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[PyPI 包窃取击键并劫持社交账号](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521893&idx=2&sn=b8ab43380cd434651d9fb5b279b4e78e&scene=21#wechat_redirect)

[PyPI攻击：通过 Python 库传播 JarkaStealer](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521578&idx=2&sn=54734e7515c71beca1602a65e343a991&scene=21#wechat_redirect)

[恶意PyPI 包窃取AWS密钥](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521454&idx=2&sn=b633886fd9fb660b4f61e571a43cbad6&scene=21#wechat_redirect)

[“复活劫持”供应链攻击威胁2.2万个PyPI包的安全](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=2&sn=18f9b633ae22eab04a32ea14664dde07&scene=21#wechat_redirect)

[恶意 PyPI 包伪装成答案，滥用StackExchange 进行传播](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520319&idx=2&sn=360f04eb666396afc086ba0444d3574a&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/malicious-pypi-package-steals-discord-auth-tokens-from-devs/

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