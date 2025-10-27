---
title: 黑客利用 ProjectSend 严重漏洞攻击服务器
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521625&idx=2&sn=8a7741ed8a419b06a972294416323328&chksm=ea94a433dde32d256ddf003492c63581ae6e4ca796a7b7d06dfae15b7c1db0eaf3864e15b031&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-29
fetch_date: 2025-10-06T19:17:32.369377
---

# 黑客利用 ProjectSend 严重漏洞攻击服务器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQCtAHP0XRpyGjHOpxfTzo3RLDPGfEhecaibd9fOXFWNHTd4OdjmfoP9pBPEuuIFAjE98WPagteibjg/0?wx_fmt=jpeg)

# 黑客利用 ProjectSend 严重漏洞攻击服务器

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**威胁行动者们正在利用ProjectSend 中的一个严重认证绕过漏洞，上传 webshell 并获得对服务器的远程访问权限。该漏洞的编号是CVE-2024-11680，是一个影响 ProjectSend r1720 之前版本的严重的认证漏洞，可导致攻击者将特殊构造的HTTP请求发送给 “options.php” 来更改应用配置。成功利用该漏洞可导致黑客创建恶意账户、植入 webshell 并嵌入恶意 JavaScript 代码。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQCtAHP0XRpyGjHOpxfTzo3bTjyr4LtOZh26fbLoB8cX2iaqYNcg3KGUib3X92A8AI6Q4cqfQ1nrLsQ/640?wx_fmt=png&from=appmsg)

尽管该漏洞已在2023年5月16日修复，但直到昨天才被分配CVE 编号，导致用户未认识到它的严重性以及应用安全更新的紧迫性。

VulnCheck 检测发现，打补丁的情况不容乐观，99%的 ProjectSend 实例仍然运行的是易受攻击的版本。

**数千实例遭暴露**

ProjectSend 是一款开源的文件共享 web 应用，旨在简化服务器管理员和客户端之间安全、非公开的文件传输工作。

该应用在偏好自托管解决方案而非第三方服务如 Google Drive 和 Dropbox 的组织机构之间受欢迎。Censys 发布报告称，网络上共有约4000台公开的 ProjectSend 实例，其中多数易受攻击。具体而言，报告提到，从 Shodan 数据来看，55%的被暴露实例运行的是在2022年10月发布的 r1605版本，44%使用的是2023年4月发布的未具名版本，而仅有1%的实例使用的是已修复版本 r1750。

VulnCheck 报道称，发现对CVE-2024-11680的活跃利用，不仅是测试，还包括修改系统设置启用用户注册、获得越权访问权限以及部署 webshell 以维持对受陷服务器的控制。

这一活动自2024年9月起就呈活跃状态，因为当时 Metasploit 和 Nuclei 发布了该漏洞的公开 exp。报告中提到，“VulnCheck 注意到这些公开的 ProjectSend 服务器开始将登录页的title更改为长的、随机的字符串。这些名称符合 Nuclei 和 Metasploit 实现漏洞测试的逻辑。这两款利用工具均修改了受害者的配置文件，以随机值修改站点名称（以便修改HTTP的title）。”

GreyNoise 列出了与该活动相关的121个IP地址，表明它是大规模的尝试而单一来源。VulnCheck 提醒称，这些webshell 存储在 “upload/files” 目录中，其名称生成自 POSIX 时间戳、用户名的SHA1哈希以及原始的文件名称/扩展。

通过web服务器实现对这些文件的直接访问权限表明漏洞遭活跃利用。研究人员提醒称，鉴于攻击活动已大规模蔓延，因此应尽快更新至最新版本r1750。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[GitHub 将为提升开源项目安全提供资金支持](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521564&idx=2&sn=d554c5607b52083d41be8c732115d490&scene=21#wechat_redirect)

[开源客户端qBittorrent 修复已存在14年的RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521357&idx=2&sn=dc9695c878770ba5390c627bc3e3681a&scene=21#wechat_redirect)

[研究员在开源AI和ML模型中发现30多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521331&idx=1&sn=e13cd9f9dccd9d17953e551df9108205&scene=21#wechat_redirect)

[Python、npm和开源生态系统中的入口点可用于发动供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521093&idx=1&sn=7723bd7496e2f4b228e3013dd21765b4&scene=21#wechat_redirect)

[奇安信中标某大型国有银行开源组件评估项目](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520385&idx=1&sn=0f0f40c70b428655a0cc88f82c6baf69&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/hackers-exploit-projectsend-flaw-to-backdoor-exposed-servers/

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