---
title: Marimo 高危预认证 RCE 漏洞已遭活跃利用
url: https://mp.weixin.qq.com/s/5ML_O5M58UWCvKt8Vc9IGA
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:41:53.426722
---

# Marimo 高危预认证 RCE 漏洞已遭活跃利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfX1RCGUc1icOgmZROwsymB4RWq0EPvWEiaUIrOeo9jbxXg9uGyw7bSGia5utJaGgYSm5fxcyS6g4YCok4iagNa5ho4BOFb0FdPTzmA/0?wx_fmt=jpeg)

# Marimo 高危预认证 RCE 漏洞已遭活跃利用

Bill Toulas
Bill Toulas

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**开源响应式 Python 笔记本平台 Marimo 中存在一个严重漏洞CVE-2026-39987（CVSS评分9.3），攻击者无需认证即可实现远程代码执行 (RCE)，影响 Marimo 0.20.4及之前版本。该漏洞在公开披露10小时后即遭利用。**

云安全公司 Sysdig 的研究人员提到，攻击者根据开发者公告中发布的信息构造了一个利用，并立即开始窃取敏感信息。Marimo 是一个开源的 Python 笔记本环境，通常供数据科学家、机器学习/人工智能实践者、研究人员和开发人员构建应用或仪表盘。该项目热度很高，在 GitHub 平台获得2万个 star和1000多次 fork。

CVE-2026-39987是因 WebSocket 端点 “/terminal/ws” 在没有进行适当认证检查的情况下暴露一个交互式终端造成的，可导致任何未认证客户端进行连接。这就导致攻击者可访问完整的交互式 shell，以与 Marimo 进程相同的权限进行运行。

Marimo 在今年4月8日披露了该漏洞，并在近日发布0.23.0版本修复该漏洞。开发人员注意到该漏洞影响那些将所部署 Marimo 当作可编辑笔记本的用户，以及在编辑模式下使用 –host 0.0.0.0将 Marimo 暴露到共享网络的用户。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXibheZ8YbRFdgjhweBibtfDS4DKyYPzLejaGUlNMzL5ensuFPxjXjEQ6f5mib7pTGwwWkrp1yM8gxmmwbdNPKicfdoibniaqcSJL6W8/640?wx_fmt=gif&from=appmsg)

**已遭在野利用**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXRHr8ZHicvXt6H7icOLJhxLM1uicAGhd88DA1sl70eibpFo8KJGWP8KA3LRtEYyEMVC7fwIvNEyN2pD629848MpBI3AfD2kHgqibE8/640?wx_fmt=gif&from=appmsg)

研究人员提到，在该漏洞详情被披露的12小时内，已有125个IP地址开始实施侦查活动。在公开披露不到10小时后，研究人员在凭据窃取攻击活动中实施的首次利用尝试。

攻击者首先连接到 /terminal/ws 端点来验证漏洞是否存在，执行了一段简短脚本以确认可远程执行命令，并在几秒内断开连接。不久之后，攻击者重新连接并开始手动侦查，执行pwd、whoami 和 ls 等基本命令以了解环境，随后尝试进行目录遍历，并检查与 SSH 相关的路径位置。

接着，攻击者将重点转向凭据窃取，立即定位 .env 文件并提取其中的环境变量，包括云服务凭据和应用密钥。随后，他们尝试读取工作目录下的其它文件，并继续探查 SSH 密钥。上述整个凭据访问阶段在不到三分钟的时间内完成。

大约一小时后，攻击者再次返回，使用相同的漏洞利用序列进行了第二次入侵。研究人员指出，这起攻击背后似乎是一位“有条理的操作者”，手法偏向手动操作而非依赖自动化脚本，目标明确，主要集中在窃取 .env 凭据和 SSH 密钥等高价值资产上。攻击者并未尝试安装持久化后门、部署加密货币挖矿程序或植入其它木马，这表明它是一场快速且隐蔽的窃密行动。

建议 Marimo 用户立即升级到 0.23.0 版本，同时监控指向 ‘/terminal/ws’ 的 WebSocket 连接，通过防火墙限制外部访问，并更改所有已泄露的密钥。如无法升级，则可通过完全拦截或禁用 “/terminal/ws” 端点的方式，有效缓解该漏洞。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[开源平台 Flowise 中的满分 RCE 漏洞已遭在野利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525680&idx=1&sn=5dbab9da81c7d42eda6c2082c7f2ac03&scene=21#wechat_redirect)

[开源项目mcp-remote 中存在严重漏洞可导致RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523555&idx=2&sn=04a84283c9d2100a95736c652525dcd8&scene=21#wechat_redirect)

[开源客户端qBittorrent 修复已存在14年的RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521357&idx=2&sn=dc9695c878770ba5390c627bc3e3681a&scene=21#wechat_redirect)

[开源库 libcue 中存在内存损坏漏洞，Linux 系统易遭RCE攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517824&idx=1&sn=6df44200db86a65be854d61f6381c0d1&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/critical-marimo-pre-auth-rce-flaw-now-under-active-exploitation/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

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