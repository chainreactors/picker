---
title: 安全公司Tenable插件更新有bug，全球Nessus 代理皆宕机
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521996&idx=1&sn=96013ce25046ff02b2d52d5d4a7a3423&chksm=ea94a7a6dde32eb03c9e0ae326ac24d3ea0ac56bae50ee72d4c8421594196fd6010e0ca953f6&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-08
fetch_date: 2025-10-06T20:10:44.417619
---

# 安全公司Tenable插件更新有bug，全球Nessus 代理皆宕机

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRK3GwH5ZhTcSkMz3aVNdyqibmuibBP8UrDR09RvGtoUo1ibZs06n4ia2AXeF94gAgT7AKFO3bN0hrjWg/0?wx_fmt=jpeg)

# 安全公司Tenable插件更新有bug，全球Nessus 代理皆宕机

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全公司 Tenable 表示，客户必须手动升级软件，重新启动因插件增量更新问题导致宕机的Nessus 漏洞扫描器代理。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRK3GwH5ZhTcSkMz3aVNdyqiaHX8stXkCqFrYWOcZLUeamk0NR6ibxZkzJ2Y1GMFbeh2t8zOwbanWFQ/640?wx_fmt=gif&from=appmsg)

Tenable 公司停止该插件更新以阻止其影响更多的系统，并在一份事件报告中指出，对 “在所有站点上的某些用户”而言，这些代理全部宕机。这一事件影响位于美洲、欧洲和亚洲的更新至 Nessus Agent 10.8.0及10.8.1的客户。该公司已经拉取这些有问题的版本并发布了 Nessus Agent 10.8.2修复了导致代理宕机的问题。

Tenable 公司在最新发布的动态中提到，计划在今天前恢复插件下载内容。该公司在Nessus Agent 10.8.2的发布备注中提到，“一个已知问题可导致 Tenable Nessus Agent 10.8.0和10.8.1在触发一个增量插件更新时宕机。为阻止这一问题，Tenable已披露为这两个代理版本准备的插件更新。另外，Tenable 已禁用 10.8.0和10.8.1版本阻止更多问题的发生。”

**手动升级**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRK3GwH5ZhTcSkMz3aVNdyqGmMibOQDHVH5oQ7rNtf6icK0RbuDJ62ibuFb39EAHDgLvTKBIFgbL1X4w/640?wx_fmt=gif&from=appmsg)

受影响客户必须升级至10.8.2版本或降级至10.7.3版本让 Nessus 代理重新恢复正常，如果代理配置用于升级或降级，则还另需重置插件。

然而，修复该问题需要手动升级使用 Tenable Nessus Agent 10.8.2安装包的代理，在必要时，首先应该使用脚本（已在发布备注中分享）或nessuscli 重置命令重置代理插件。

[2024年7月曾发生一起影响更严重的类似事件](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520213&idx=1&sn=315d12b373fb85e4b9c485117694c9ba&scene=21#wechat_redirect)。CrowdStrike 公司 Falcon 更新问题导致大面积宕机事件发生，影响全球很多组织机构而后服务，包括银行、航空公司、机场、电视台以及医院等。该事件导致全球 Windows 系统出现蓝屏死机事件，导致数十万企业宕机。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[CrowdStrike 宕机后，微软拟让EDR厂商在内核模式外”运行](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520848&idx=3&sn=4a3ec7b673c6f5a5650610d98d80b076&scene=21#wechat_redirect)

[CrowdStrike：测试软件中的bug导致Windows蓝屏死机](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520213&idx=1&sn=315d12b373fb85e4b9c485117694c9ba&scene=21#wechat_redirect)

[我们仔细分析了使数百万Windows 蓝屏死机的CrowdStrike代码](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520194&idx=1&sn=8b7005cae90d257d5bb3feff7e6a7434&scene=21#wechat_redirect)

[微软：是欧盟把Windows 内核的密钥交给了 CrowdStrike，触发蓝屏死机](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520167&idx=1&sn=8e80c74dda2ec337dca9a0451873c7bc&scene=21#wechat_redirect)

[关于CrowdStrike 使 Windows 蓝屏死机，你需要知道的都在这里](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520109&idx=1&sn=f70fb8a65546c2f9ad15c895357b4258&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/bad-tenable-plugin-updates-take-down-nessus-agents-worldwide/

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