---
title: GitHub Codespaces 可被滥用于托管和传播恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515363&idx=1&sn=7bedb454246d2014c51601f6e2bc3f59&chksm=ea948d89dde3049fa0c32a8f6d377ca5f9e53fca118252965167e2d8ad5fa884a2c586a2e81f&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-21
fetch_date: 2025-10-04T04:29:25.845506
---

# GitHub Codespaces 可被滥用于托管和传播恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTemklgaj68k6nObQicJq7m7VctjiagvWBUIichHbVj7ic3S1y8uu8GuKNunib66dyEpXgUNhPU2QQz3Eg/0?wx_fmt=jpeg)

# GitHub Codespaces 可被滥用于托管和传播恶意软件

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**研究员说明了威胁行动者如何滥用 GitHub Codesapces 的“端口转发”特性来托管和传播恶意软件和恶意脚本。**

GitHub Codespaces 可使开发人员在虚拟化容器中部署托管在云上的IDE平台，在web浏览器中直接编写、编辑并测试/运行代码。自2022年11月推出以来，它在开发人员群体十分受欢迎，可用于预配置、基于容器的环境中，并配备项目所需的所有必要工具和依赖关系。

**0****1**

**将GitHub Codespaces 作为恶意软件服务器**

趋势科技在报告中指出，研究人员展示了如何可轻易将GitHub Codespaces 配置为web 服务器，传播恶意内容并避免对来自微软的流量的检测。GitHub Codespaces 可使开发人员将TCP端口转发给公众，因此外部用户可测试或查看应用程序。在Codespace VM中转发端口时，该特性将生成访问在该端口上运行的app的URL，端口可配置为非公开或公开。

非公开端口转发要求通过令牌或cookie的方式认证，以访问该URL。而任何人可访问公开端口而无需任何认证。该特性使得开发人员在代码演示方面具有灵活性，但研究人员指出当前攻击者可轻易滥用该特性托管恶意软件。

从理论上来讲，攻击者可运行简单的Python web服务器，将恶意脚本或恶意软件上传至Codespace，在虚拟机上打开web服务器端口并将其可见性分配为“公开”。生成的URL之后可用于访问这些托管文件，或用于钓鱼攻击或用于托管其它恶意软件下载的恶意可执行文件。而这正是攻击者滥用可信任服务如Google Cloud、Amazon AWS和微软Azure 传播恶意软件的方式。

报告指出，“为了验证我们对威胁建模滥用场景的假设，我们在端口8080上运行了一台基于Python的HTTP服务器，公开转发并暴露该端口。在此过程中，我们轻松发现了该URL以及认证无需cookie的情况。”

报告指出，虽然Codespaces端口转发系统默认使用HTTP，但开发人员可将其设置为HTTPS，从而增加了对URL安全性的错觉。由于GitHub是一个可信空间，反病毒工具不太可能发出警报，因此威胁行动者可以最小代价躲避检测。

**0****2**

**更多的攻击场景**

分析人员还探索了滥用GitHub Codespaces 中的开发容器（Dev Containers）以更有效地传播恶意软件的情况。

GitHub Codespaces 中的“开发容器”是一个预配置容器，包含特定项目所需的所有必要依赖和工具。攻击者可通过该容器进行快速部署，和他人分享或者通过VCS进行连接。攻击者可使用脚本转发端口、运行Python HTTP服务器并在Codespace内下载恶意文件。之后将端口的可见性设为公开，从而创建具有开放目录的webserver，将恶意文件传播给目标。

报告创建了相关PoC，使用的是在URL访问后web服务器被删除之前的100秒延迟。BleepingComputer 复现了通过Codespaces创建“恶意”webserver的场景，耗时不超过10分钟且无需对该特性拥有任何经验。

报告指出，“通过这类脚本，攻击者可轻松滥用GitHub Codespaces 通过codespace环境中公开暴露的端口，快速传播恶意内容。由于所创建的每个Codespace都具有唯一标号，因此所关联的子域名也是唯一的。这就使得攻击者能够创建不同的开放目录实例。”

GitHub的策略是，不活跃的codespace 会在30天后删除，因此攻击者可在一个月的时间内使用相同的URL。虽然目前尚不存在针对GitHub Codespaces 的已知滥用情况，但报告强调了一种现实的可能性，因为威胁行动者一般偏向于选择同时被安全产品信任的“免费使用”平台。

GitHub回应称已注意到该报告，计划增加提示，提醒用户连接到codespace时确认是否信任该所有人。另外，建议用户根据使用指南维护开发环境安全并使风险最小化。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Slack 的GitHub 私有仓库被盗](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515211&idx=2&sn=ea83798dec9f775057da596197259c09&chksm=ea948d21dde30437eefcc70696a4351308e9af4223c2e3e75e8a13058ca04dceaa6b21f37d88&scene=21#wechat_redirect)

[GitHub Actions 漏洞可导致攻击者投毒开发管道](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514872&idx=2&sn=99f948eba89e5ef6fd054c745dfde955&chksm=ea948b92dde30284a5e685e93453fec9d40647f629a76e60c63121549900e3970308a1fce8b7&scene=21#wechat_redirect)

[GitHub 为公开仓库设立非公开漏洞报告渠道，保护开源软件安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514622&idx=4&sn=c7a348f09266e1cc2c26a0cd4b79187f&chksm=ea948894dde30182d3c3c7adad2a502d1fa5fa66dad088160b687abc84cbc2dbe6df101d3840&scene=21#wechat_redirect)

[微软GitHub Copilot 被诉违反开源许可条款和侵犯开发人员权益](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514414&idx=1&sn=a937561278e4afeadc5816a57d8be22c&chksm=ea948844dde301521c4b577e4e0e5e3292436a79499f9b3e00726bd0f3a03f3400c521010ded&scene=21#wechat_redirect)

[GitHub账户重命名可引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514352&idx=1&sn=7105ffba7a58b1c73df803461e6ca7ef&chksm=ea94899adde3008cbc9d8ee004890757957a4b7b7c5ada48418a5c0efd8425cad376d4679fdd&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/hackers-can-use-github-codespaces-to-host-and-deliver-malware/

题图：Pexels License‍

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