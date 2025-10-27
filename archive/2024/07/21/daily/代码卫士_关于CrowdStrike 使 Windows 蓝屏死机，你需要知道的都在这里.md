---
title: 关于CrowdStrike 使 Windows 蓝屏死机，你需要知道的都在这里
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520109&idx=1&sn=f70fb8a65546c2f9ad15c895357b4258&chksm=ea94be07dde33711cb8de08051d20315cae01150c1cce58af83248ce1933418d827a742b82ab&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-21
fetch_date: 2025-10-06T17:41:05.913311
---

# 关于CrowdStrike 使 Windows 蓝屏死机，你需要知道的都在这里

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSicZFHKPXTZpYqZfBGFiaSNL22BQpUTgR7Mm9RwTVyG1xnS4UbFZ9uoCWXQ6peYyaPb8ticcWYrfW2A/0?wx_fmt=jpeg)

# 关于CrowdStrike 使 Windows 蓝屏死机，你需要知道的都在这里

综合编译

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**一觉醒来，全球IT大宕机，应急服务、航空旅行、银行等各行各业无不受其影响。该宕机事件被指和网络安全公司 CrowdStrike 向客户推送的一次有缺陷的自动安全更新有关。**

**纵观历史，一行代码不断破坏全球计算机系统的事情仅发生过少数几次，包括2003年的 Slammer 蠕虫事件、俄罗斯针对乌克兰的 NotPetya 网络攻击事件、朝鲜的自传播勒索软件 WannaCry 事件。而像昨天发生的让全球互联网和IT基础设施都不堪其扰的数字化灾难事件并非由黑客发布的恶意代码引发，而是由本应阻止此类恶意代码的软件引发****。**

**0****1**

**到底发生了什么？**

本周五，全球数万台 Windows 计算机遭遇蓝屏死机，原因是网络安全公司 CrowdStrike 在客户端机器上推送了安全软件自动更新。

该更新中包含一个bug，导致接收更新的机器崩溃，出现蓝屏死机。由于该bug及其引发的系统崩溃，依赖于这些计算机的全球服务都无法使用。

**0****2**

**是网络攻击吗？**

不是。截至目前，未有证据表明这次全球宕机是网络攻击或黑客事件。问题根因是某些 Windows 计算机上使用的第三方网络安全软件更新中存在一个 bug。

**0****3**

**所有的 Windows PC都受影响吗？**

不是。值得注意的是，本次宕机时间并非因 Windows 本身存在漏洞导致，而是因为独立的网络安全公司 CrowdStrike 提供的 Windows 安全软件中存在缺陷导致的。

因此，只有运行受影响的 CrowdStrike 软件受影响，而非全球所有 Windows PC 受影响。CrowdStrike为数十家全球财富500强提供服务。

**0****4**

**哪些服务和业务受影响？**

全球大量业务和服务类型受影响，包括：

* 医院
* 航空
* 百货商店
* 银行
* 零售商店
* 紧急服务
* 大中小型企业

如上只是全球已报道的受某种程度影响的一些机构类型。并非所有国家的所有这些机构类型均受影响。在一些国家，受影响的医院不得不通过人工方式处理服务以维持运营。在很多机场，登机柜台无法处理登机服务。在很多零售店，自助服务机器无法运作。社交媒体上还报道称很多饭店和小型企业不得不停止使用支付终端，转为使用现金。

**0****5**

**CrowdStrike 公司是谁？**

CrowdStrike 控股公司是一家成立于2013年的上市公司，总部位于奥斯汀。

该公司提供端点安全软件，客户可将软件推送到所在公司的所有个人设备中，如员工的工作笔记本或零售商的PoS机。

**0****6**

**CrowdStrike 如何回应？**

CrowdStrike 公司总裁兼首席执行官 George Kurtz 在社交媒体证实此事件因 CrowdStrike 软件中的一个 bug 引发。他写道，“CrowdStrike 正在与客户沟通，他们受到为 Windows 主机进行的单个内容更新中的一个缺陷影响。这并非安全事件或网络攻击。问题已找到、隔离，修复方案已部署。“

**0****7**

**安全分析师认为的根因是什么？**

**安全和IT分析师认为，事件与CrowdStrike Falcon 软件的“内核驱动”更新有关。**内核驱动是使应用与Windows 最底层即操作系统的核心（内核）进行交互的软件组件。这种高度敏感的访问级别使安全软件所必需的，这样它能够在任何恶意软件安装在系统并访问系统任何部分以植入代码之前进行运行。由于恶意软件已严谨，因此推送防御软件要求持续连接和更广泛的控制。

这种更深入的访问权限引入了更高的可能性，即安全软件及其更新将导致整个系统崩溃。在操作系统内核层运行恶意代码检测软件相当于进行一次“心内直视手术”。

曾在卡巴斯基工作了23年的研究员Costin Raiu 表示，因此，内核驱动更新引发此类大规模的全球计算机崩溃事件也就不足为奇了。他提到，在卡巴斯基工作时，Windows 软件的驱动更新会在推送前进行长达数周的密切审查和测试，而且他们还要求微软也对代码进行审查并加密签名。也就是说该事件表明微软可能也未注意到 CrowdStrike 公司的 Falcon 驱动中的bug 触发了此次宕机时间。他提到，对驱动更新付出如此多的注意力仍然发生了此事件，令人惊讶。一个驱动就能让一切宕机。

微软的一名发言人指出，CrowdStrike 更新时导致全球大量IT系统宕机的罪魁祸首，微软并未监督CrowdStrike 在系统中推送的更新，但并未进一步解释微软是否检查并签名了内核驱动更新。

Raiu 认为即使如此，CrowdStrike 并非因驱动更新触发 Windows 崩溃的唯一一家安全公司。卡巴斯基的更新甚至Windows 自身的内置杀毒软件 Windows Defender 在过去也曾触发类似蓝屏死机情况。他提到，世界上的每个安全解决方案都经历过 CrowdStrike 时刻，并非新鲜事，而区别在于规模大小。

**0****8**

**Mac 和 Linux 计算机受影响吗？**

不受影响。CrowdStrike bug 仅影响运行接收了该软件更新的 CrowdStrike 软件的 Windows PC。

**0****9**

**修复方案何时发布？**

CrowdStrike 公司表示已找到并发布了相关修复方案。

但似乎过程并不顺利。一些蓝屏死机的 Windows PC可能需要手动重启到安全模式或者Windows 恢复环境来执行修复方案。也就是说需要手动访问某些受影响的PC。

对于拥有大规模自研IT团队的企业和组织机构，这种情况会制造很多麻烦，不过至少他们有足够的人力来推进。然而，很多中小型企业背靠第三方IT支持，而这些支持常常还是远程进行的。

这些支持公司可能需要让IT技术人员驻场来修复每台PC中的问题。但鉴于这些支持公司的个人客户端数量不少，因此可能需要等待。

**0****10**

**华尔街的反应如何?**

CrowdStrike 公司的股票表现不佳。截至本文发布之时，该公司的股票下跌超过14%，每股大约为294美元。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[SolarWinds 访问审计解决方案中存在严重的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517960&idx=2&sn=859ca4a50e7e9df4867d1973b7bba390&chksm=ea94b662dde33f74e25d02181f9fc202ee23b91008de4d26acf0d79bd3e0385d608d23bb1245&scene=21#wechat_redirect)

[SolarWinds 事件爆发前半年，美司法部就检测到但未重视](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516392&idx=1&sn=03805ab2d377a6823689c8e9df44946b&chksm=ea94b182dde33894b955bb4519df38c455bcbfff727ec9d3034f4272590e649e51f90426748a&scene=21#wechat_redirect)

[SolarWinds 平台修复两个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516335&idx=2&sn=7714c02477242110c20958d13327c558&chksm=ea94b1c5dde338d3aea7cd488e25f4d59825e633deebe43bb64963f20d6336a81cf4016641f1&scene=21#wechat_redirect)

[SolarWinds 公司：Web Help Desk 实例正遭攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510991&idx=4&sn=90944cad89a7c454178edd41a21c5652&chksm=ea949aa5dde313b3d6c2c7960809d44226a88ed78a7ae795f0ffd4835a5357e4d93d64e6012c&scene=21#wechat_redirect)

**原文链接**

https://www.fastcompany.com/91159356/windows-crowdstrike-outage-update-blue-screen-death-list-services-down-today-fix-timeline-fix

https://www.wired.com/story/crowdstrike-outage-update-windows/

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