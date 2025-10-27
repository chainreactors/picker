---
title: CrowdStrike 宕机后，微软拟让EDR厂商在内核模式外”运行
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520848&idx=3&sn=4a3ec7b673c6f5a5650610d98d80b076&chksm=ea94a33adde32a2c9f0b967cd2294a242caed01121b37069e0b77bf6c815551da98fd0d49ad9&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-19
fetch_date: 2025-10-06T18:25:51.276078
---

# CrowdStrike 宕机后，微软拟让EDR厂商在内核模式外”运行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT7lctusib0CJe6kmfLUSPUw8eXu72rM9hAbQx4X5QwcREvfUMgHt2hHe0kCicJlAzHfficMv7KaCIWA/0?wx_fmt=jpeg)

# CrowdStrike 宕机后，微软拟让EDR厂商在内核模式外”运行

Ryan Naraine

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**CrowdStrike 更新导致全球IT宕机事件后，微软计划重新设计杀毒产品与Windows 内核的交互方式。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMT7lctusib0CJe6kmfLUSPUwffoqp44kZ7BSibPFbNZyhCdngYicKiauxY4cDvXjKp8BydaPibyEWzYHVg/640?wx_fmt=png&from=appmsg)

虽然这些变化的技术详情尚未公开，但微软指出将在 Windows 11 中提供“新平台能力”，使安全厂商“在内核模式外”运行，实现软件可靠性。

在为期一天的微软与EDR厂商峰会上，微软副总裁 David Weston 表示这一变化是保持弹性和安全目标的长期步骤的一部分。Weston 在峰会后提到，“我们基于在 Windows 11 中进行的安全投资，探索了微软将在 Windows 中推出的新平台能力。Windows 11 提升后的安全态势和默认安全能力使它能在内核模式之外微解决方案提供商提供更多的安全能力。”

重新设计旨在避免 CrowdStrike 软件更新错误导致 Windows 系统崩溃进而造成全球数十亿美元的损失事件再次发生。Weston 引用 CrowdStrike 事件强调了EDR厂商采用微软所述的“安全部署实践 (SDP)”同时推出Windows大型生态系统更新。

Weston 表示，SDP的一个核心原则包括“向客户发送的渐进式和阶段性的更新部署”，以及使用“具有多种端点的精确运行”，以及在必要情况下停止或回滚更新的能力。他提到，“我们讨论了微软及其合作伙伴如何增加对关键组件的测试、改进多种配置中的联合兼容性测试、推动在开发中和市场中产品健康的更好的信息共享以及通过更紧密的协调和恢复程序提升事件响应的有效性。”

在峰会上，Weston 表示，微软及其合作伙伴讨论了在内核模式外进行运行的性能需求和挑战、安全产品反篡改防护的问题、以及未来平台的安全传感器要求和设计安全目标。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[CrowdStrike：测试软件中的bug导致Windows蓝屏死机](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520213&idx=1&sn=315d12b373fb85e4b9c485117694c9ba&chksm=ea94bebfdde337a9f3363ba26a417ed880bf76dfe5272e2a144943353fd1efa9eb8002fe613a&scene=21#wechat_redirect)

[我们仔细分析了使数百万Windows 蓝屏死机的CrowdStrike代码](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520194&idx=1&sn=8b7005cae90d257d5bb3feff7e6a7434&chksm=ea94bea8dde337be4a06359bee3c3f03fbe5d237fc4b37d86075295fbe2ce7932397fb5fbae4&scene=21#wechat_redirect)

[微软：是欧盟把Windows 内核的密钥交给了 CrowdStrike，触发蓝屏死机](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520167&idx=1&sn=8e80c74dda2ec337dca9a0451873c7bc&chksm=ea94becddde337dbdaf65d39b9eb60cb90bd15bc0a6dabb0defc375c80975c52f344d6b5405f&scene=21#wechat_redirect)

[关于CrowdStrike 使 Windows 蓝屏死机，你需要知道的都在这里](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520109&idx=1&sn=f70fb8a65546c2f9ad15c895357b4258&chksm=ea94be07dde33711cb8de08051d20315cae01150c1cce58af83248ce1933418d827a742b82ab&scene=21#wechat_redirect)

[NSS 实验室以反托拉斯名义起诉赛门铁克 CrowdStrike 等巨头](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247488136&idx=6&sn=5730e02fbc8893758828952b4df94fec&chksm=ea9723e2dde0aaf4274477a06677d4cc93a93309d670a459611b3919556b1450f2a2da2c2c18&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/post-crowdstrike-fallout-microsoft-redesigning-edr-vendor-access-to-windows-kernel/

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