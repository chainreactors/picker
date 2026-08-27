---
title: CISA红队攻破关键基础设施，SOC与云安全盲区全面暴露
url: https://mp.weixin.qq.com/s/9tprh4L1lkBUjNmCpw5KLQ
source: Doonsec's feed
date: 2026-08-26
fetch_date: 2026-08-27T12:10:05.091524
---

# CISA红队攻破关键基础设施，SOC与云安全盲区全面暴露

# CISA红队攻破关键基础设施，SOC与云安全盲区全面暴露

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX3hPbhza5wTQibRibS5JUxFuu86mYI3sPnp0fTYfFgvaZkIS0yCibYsPFu5RKlKCmJoDTfL9sDgHIWVkX3nic3zibjLskIOOUK2jeR8/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX16dE0GdxZ8XpIGWBqXgzwlDrIYsWIw8kg2wdQCJnrIRHqKpOW3hcaRn5YdItc7K8LJ1WK7evjb2HmeicUuCZzKBNsqIBDZXpsc/640?wx_fmt=png&from=appmsg)

Part01

两家SOC攻防对比

CISA最新发布的一份红队咨询报告向关键基础设施运营方发出警示：即便安全系统投入巨大，仍可能失效。原因在于，有效响应告警离不开训练有素的分析人员。

该机构发布的《两个SOC的故事》报告对比了两次并行的红队演练：一次针对某政府服务与设施行业组织，另一次针对某水务与废水处理行业实体。两次演练使用了几乎相同的攻击手法，结果却截然不同。

在两次行动中，CISA红队人员都先通过网络钓鱼获取初始访问权限，随后利用Active Directory中的配置缺陷进一步扩大权限。其中包括默认启用的Machine Account Quota，以及配置不当的Active Directory证书服务模板。借助这些问题，攻击者得以完成权限提升，并在目标网络中横向移动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2iccxAmwjh1CSfJKMTTzwl08SFLYRFLb52XMiaBWpCDtfdojCshicXQtRSvxUg6xESbSiauBpJD06BgyyzMcwpoSrQWga5PRHjEpA/640?wx_fmt=png&from=appmsg)

Part02

CISA红队攻破关键基础设施

在A组织中，红队在完全未被察觉的情况下获得了域高权限，并触及了敏感业务系统和云资源，最终甚至能读取SOC人员的电子邮件，并在防御者自己的机器上部署键盘记录器，全程未触发任何响应。

B组织的情况则截然不同：其SOC在初始钓鱼载荷执行后的2到20分钟内就隔离了失陷工作站，切断了命令与控制通信，使入侵无法扩散。

由于B组织极快地发现了入侵行为，CISA转而采用“假设失陷”模式，由受信代理赋予红队相当于钓鱼攻击未被发现时本可获得的同等访问权限。

随后，红队再次利用相同的Machine Account Quota弱点提升权限，通过System Center Configuration Manager文件窃取明文凭据，并使用DCSync攻击获取域控制器凭据，其中包括用于伪造黄金票据的敏感账户krbtgt。

尽管面对如此深入的访问权限，B组织的防御者仍然隔离了运营技术隔离区中一台失陷的堡垒主机，并阻止了微软自动告警标记的一次可疑Azure登录。这表明即使在网络已被假定为失陷的情况下，分层检测仍然持续发挥作用。

Part03

SOC运营机制失效

CISA认为，A组织的盲区并非源于工具不足，而是运营机制失灵。该组织同时运行多个SOC和多套EDR平台，但跨团队之间缺乏沟通，日常业务活动产生的数千条误报告警将真正的入侵指标淹没。

此外，分析人员缺乏明确、标准化的可疑活动上报流程，能够采取的处置措施也十分有限。结果是，一些真实告警并没有得到及时处理。比如，一条与红队在SCCM服务器上活动相关的告警，仅仅因为防御人员无法确认该系统归属哪个团队，就被当作误报搁置。

该咨询报告的核心结论是：检测工具的有效性完全取决于其背后的人和流程。CISA敦促关键基础设施运营方修复常见的Active Directory弱点，例如不受限制的Machine Account Quota和存在ESC1漏洞的证书模板；对服务账户和云账户强制执行凭据过期策略；并针对工作负载身份采用条件访问，以封堵应用权限方面的缺口。

同样重要的是，组织需要建立文档化的上报流程、实现跨团队可见性，并赋予分析人员足够的处置权限。因为B组织的成功关键在于快速分诊和果断隔离，而非任何单一安全产品。

参考来源：

CISA Red Team Breaches Critical Infrastructure to Reveal SOC and Cloud Security Gaps

https://cybersecuritynews.com/cisa-red-team-breaches-critical-infrastructure/

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0grlwwcpsEQ5CIH725a7xAnwDLGFctXFohPibiaOVyzdqwaibKgD4x4enG6jhdgJQHziaqTMy1WR0Hibx4MceSVKd6C7HGGlA9zLibg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651344398&idx=1&sn=56c4e0d580e04a250d0e8c6cffd592b8&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3eRDUpH3UJicSe4tdw7nZYu9aa5PQ9KgkaP84oZz0bVYdBiaDt97VfDBLulDp3sWLgvzI4m0mc89MZ7feP2yfFAmcRWOlicWubZ4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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