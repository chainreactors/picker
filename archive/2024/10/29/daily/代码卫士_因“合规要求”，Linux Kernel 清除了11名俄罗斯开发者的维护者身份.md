---
title: 因“合规要求”，Linux Kernel 清除了11名俄罗斯开发者的维护者身份
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521303&idx=2&sn=a8f19bf98fa3d8e84ee9c612d1f1d98c&chksm=ea94a57ddde32c6b67f8d71669e3990a30e0de997265420914d11525fb6480bc56dcfa1515f0&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-29
fetch_date: 2025-10-06T18:51:26.665703
---

# 因“合规要求”，Linux Kernel 清除了11名俄罗斯开发者的维护者身份

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQiadzhZU8L1ToyibztB8NGkxjmbZCGAicGRS3v3o0FMjKEqk1dzOmXNwVyaq1cT3QQogsynF84kCxRg/0?wx_fmt=jpeg)

# 因“合规要求”，Linux Kernel 清除了11名俄罗斯开发者的维护者身份

DO SON

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Linux Kernel 社区正在热议11名开发人员被从子系统维护人员清单中除名一事。这些开发者一般与俄罗斯公司之间存在关联。稳定分支维护人员 Greg Kroah-Hartman 提起了这项变化，表示“多种合规要求”是此举原因，但并未给出具体详情。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTgicnicddUYKiaW0UuECmnFcFlY6jh2ohhKS6mKUND9VdhQzDb2hjRvIFib6KZ0BJXbfmjI9zO4fykOQ/640?wx_fmt=png&from=appmsg)

这种缺乏透明度的做法引发一些社区成员的担忧。一名卓越的 Linux 开发人员 Geert Uytterhoeven 对这份语焉不详的发布提出质疑。他强调了内核开源的本质并督促澄清这些合规要求以及需要重申的文档。Uytterhoeven还提醒称，因未明确定义清除维护人员的规则而导致未来可能发生滥用情况。

这些被清除的开发人员之前负责维护大量驱动和子系统，如适用于 DVB 系统、ARM/CIRRUS LOGIC 处理器、PPTP和GRE解复用器、EMSENSING MICROSYSTEMS 传感器、UFS 文件系统、Alpha 架构移植、ACER ASPIRE 控制器、BAIKAL-T1平台支持、多种MIPS系统驱动、LIBATA PATA 和 SATA驱动、RENESAS 以太网驱动以及MICROCHIP POLARFIRE FPGA驱动等。

虽然这一变化已经融入 6.12-rc4 分支，但它绕过了Linux开发流程通常的审查步骤。对 MAINTAINERS 文件的更新被塞入无关驱动修复方案的 pull 请求并且并未在 linux-next 分支中得到审计或测试。

这一事件引起人们对平衡合规要求以及Linux内核开发的开放和协作精神之间的关注。缺乏透明度和任意删除的可能性可能会对全球的开发人员贡献造成负面影响。社区正在等待 Kroah-Hartman 的澄清并希望这一问题得到快速解决。

受影响的开发人员如下：

* Abylay Ospan
* Alexander Shiyan
* Dmitry Kozlov
* Dmitry Rokosov
* Evgeniy Dushistov
* Ivan Kokshaysky
* Nikita Travkin
* Serge Semin
* Sergey Kozlov
* Sergey Shtylyov
* Vladimir Georgiev

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[@开发：不必太自责，连 Hackerone 平台都差点因 RFC2142合规问题栽了](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247488906&idx=1&sn=8565c86017b96116a101726585f190f1&chksm=ea9724e0dde0adf69c2076bff8a140f1b4a95be9dbab807a81c569228192d97f1ce7aaab61a8&scene=21#wechat_redirect)

[观点|GDPR 合规等同于安全吗？](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247487235&idx=3&sn=448a1684f6d1a41bddae3e300c69574f&chksm=ea973e69dde0b77f9f7d9007867cacdb2cb7609f841f4939c4fa78ec5efb7159217a8f054221&scene=21#wechat_redirect)

[微软将接受俄罗斯的合规调查](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485814&idx=5&sn=05610487e37e4f5575bc4b6aa837fd9c&chksm=ea97381cdde0b10a8024633c2a72df8dee730c6cde51df1e0ae773ecf672b146f161fde691ae&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/11-russian-linux-kernel-developers-lose-maintainer-status-due-to-compliance-requirements/

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