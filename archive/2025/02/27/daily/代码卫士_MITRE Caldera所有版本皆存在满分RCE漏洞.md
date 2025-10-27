---
title: MITRE Caldera所有版本皆存在满分RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522340&idx=1&sn=857f619293015f92aad6d9622d926c9b&chksm=ea94a94edde320585b86625a84d36857679e8f005ff31ac322eea8d3c6e5a0a2530f060326a1&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-27
fetch_date: 2025-10-06T20:36:08.834419
---

# MITRE Caldera所有版本皆存在满分RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS060BUvo5zreiacrMvfpZicgUU5YljccJciaGCBx3oDFcoIejTvFNVX1CrlkcL2q8gicdLn8OO0MGTQA/0?wx_fmt=jpeg)

# MITRE Caldera所有版本皆存在满分RCE漏洞

Jai Vijayan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**MITRE Caldera 所有版本受一个CVSS评分为10的RCE漏洞影响，最早可追溯至第一个版本。**

只要运行 Caldera 的服务器上出现Go、Python和gcc，则攻击者可触发多数 Caldera 默认配置中的该RCE漏洞。

**易于实施的攻击**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMS060BUvo5zreiacrMvfpZicgoNnfxXptkonoOckibam9priaibataWUzyjWdib66QiaeA1vtq4f4X0tIVFg/640?wx_fmt=gif&from=appmsg)

报送该漏洞的独立安全研究员 Dawid Kulikowski 表示，“Caldera 完全运作需要所有这些依赖。在很多分发版本中，gcc 是 Go 的一个依赖，也就是说这个漏洞极其容易被攻击者获得。”

该漏洞的编号是CVE-2025-27364，CVSS评分为满分10分。MITRE已将该漏洞评估为“极易利用”，无需用户交互或特殊权限即可遭利用。MITRE建议所有 Caldera 用户“立即安装”Caldera 最新版本（Master 分支或v5.1.0+）。

很多组织机构、政府机构和安全专业人员都通过MITRE Caldera 进行红队演练，以测试其安全产品的可靠性并通过ATT&CK模型来复现敌对行为。能够利用该漏洞的攻击者可在网络获得可信任访问权限、提升权限、横向移动、开展侦查活动、修改安全测试结果、甚至将真实的恶意活动伪装成模拟演习。而这并非威胁人员首次尝试利用红队工具攻击该工具的所属组织。去年，趋势科技报道称威胁行动者在执行攻击时，利用EDRSilencer来识别和禁用16家厂商的EDR产品。

Kulikowski 表示该漏洞与Manx 和 Sandcat有关，而两者是Caldera 中的插件或代理，为敌对模拟和红队演习提供各种功能。Sandcat 是Caldera 进行敌对模拟的主要默认工具，而Manx为Caldera 提供反向 shell 功能以执行分配的命令。

这些代理支持动态编译特性，可使用户自定义他们如何在特定环境中运行。用户可使用HTTP标头来定义内容，如他们在和 Caldera 服务器沟通时希望代理使用的通信方法、代理用于加密通讯的加密密钥以及接受指令的服务器地址。

Kulikowski 提到，“这些代理在运行中被编译，而这些参数被传递给代理以纳入随后的二进制中并控制代理运行的方式。”

**命令注入漏洞**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMS060BUvo5zreiacrMvfpZicgoNnfxXptkonoOckibam9priaibataWUzyjWdib66QiaeA1vtq4f4X0tIVFg/640?wx_fmt=gif&from=appmsg)

然而，负责处理该动态复杂性的Caldera 服务器上缺少正确的认证机制，导致攻击者能够在运行这些代理的系统上注入恶意命令。Kulikowski 还开发了概念验证利用，不过已经做了一些调整，以阻止脚本小子利用。

Qualys 公司威胁研究部的安全研究经历 Mayuresh Dani 提到，该漏洞存在的原因是对 Caldera 代理编译流程中的安全限制和输入清理的实施不充分。他表示，“该漏洞存在于植入编译端点中，可被未认证威胁行动者通过一个简单的curl命令轻松触发。”

Dani 补充表示，“成功利用该漏洞可导致未认证威胁行动者在运行 Caldera 的服务器上执行任意代码，从而导致系统遭完全攻陷。”由于组织机构中使用 Caldera 是已知且经过批准的，因此利用该漏洞可能是不被监控且可导致攻击者从受陷网络内发动攻击。他还表示，虽然利用代码需要进行一些修改，但并不难。

Salt Security 公司的网络安全策略总监 Eric Schwake 提到，作为安全研究人员、红队和威胁建模和漏洞评估安全专业人员使用的一款广泛工具，MITRE Caldera 服务器的安全性至关重要。他表示，“在最坏情况下，攻击者可获得对服务器的完整控制权限，可能会攻陷敏感数据、影响测试结果、甚至利用该平台对组织机构内的其它系统实施进一步攻击。这种场景凸显了该漏洞应立即修复的紧迫性。使用 Caldera 的组织机构必须优先升级至最新版本并执行MITRE建议的任何其它安全措施。”

Kulikowski 计划在未来几周内为该漏洞发布完整的 Metasploit 模板，而这也凸显了立即修复该漏洞的重要性。MITRE Caldera 团队发布文章提到，“因此应修复你的实例，或者更好的方法是不要将其暴露到互联网。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[MITRE 公布2024年最严重的25个软件弱点](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521564&idx=1&sn=276695070e4ac7650f6b447dc191e2d6&scene=21#wechat_redirect)

[MITRE 发布 ATT&CK v14，改进检测、ICS和移动内容](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518049&idx=1&sn=7d78d83bf8f1ff46a0445859944e28e8&scene=21#wechat_redirect)

[MITRE 发布2023 CWE Top 25 榜单](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516897&idx=1&sn=238df262541684ada9df5ea0656c57b8&scene=21#wechat_redirect)

[MITRE发布5G 网络对抗威胁模型FiGHT](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514090&idx=1&sn=02f1c298c1c76219ea9e84a4bafaec16&scene=21#wechat_redirect)

[MITRE 发布2022 CWE Top 25 榜单](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512629&idx=2&sn=7088e1e32ca38f9d2589e88d3b6a360d&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/application-security/max-severity-rce-vuln-all-versions-mitre-caldera

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