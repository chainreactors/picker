---
title: UnitedHealth勒索软件攻击事件应吸取的六个备份教训
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651133749&idx=1&sn=6ddc70f36c5e65e6b3cdae03f5a62a87&chksm=bd15a7e68a622ef0a9f2148bdeb082577040dfbe3df2355d2e00c9ba88f27252ad9ccb56b628&scene=58&subscene=0#rd
source: 安全牛
date: 2024-12-04
fetch_date: 2025-10-06T19:38:21.289049
---

# UnitedHealth勒索软件攻击事件应吸取的六个备份教训

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkB4iaEu0v9ujZiaju3r0cTRjNM5Aibvr8ufxe2MBM3qPiaeoDnk9o2ApD2uDygiaHUpFDUExZ0IpJt89mA/0?wx_fmt=jpeg)

# UnitedHealth勒索软件攻击事件应吸取的六个备份教训

安全牛

今年早些时候发生在美国UnitedHealth的勒索软件攻击，堪称医疗保健行业的最重大的网络安全事故之一，同时还被认为是近年来最重大的医疗数据泄露事件，并导致整个美国医疗保健系统的重大运营中断。UnitedHealth为此支付了2200万美元赎金来防止被盗数据泄露，而且在文件解密后，仍不得不对其系统进行完全重建。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkB4iaEu0v9ujZiaju3r0cTRjN8c5zZj2YcsIX44AwGDx8OyrcUOFHyjI8kbbeSgp7Bpc4N4pWyrpAvg/640?wx_fmt=jpeg)

这次泄露事件引发了对医疗机构网络安全措施的严重关注，特别是关于过时技术和关键系统缺乏多因素认证（MFA）等不足安全协议的问题，甚至引发了美国国会听证会、立法者审查和潜在立法。

在针对该事件的两次听证会上，UnitedHealth首席执行官Andrew Witty在证词中承认，公司的备份系统缺乏网络分段或基础设施隔离，导致攻击者也能锁定这些备份，阻断了从初始攻击中恢复的所有途径。

如此也揭开了一个残酷的现实：**备份系统已经成为网络犯罪分子最有利可图的目标。**因为这些**攻击者已经意识到，成功入侵备份环境是决定组织是否会支付赎金的最重要因素。**

一些勒索软件组织（如BlackCat、Akira、Lockbit、Phobos和Crypto），已经开始完全绕过生产系统，直接攻击备份系统。这迫使组织重新审视其安全体系中的潜在漏洞，重新评估其备份和恢复策略。

过去，很少有首席信息安全官会特别关注到备份系统，但现在的情况已经完全不同了。早在UnitedHealth遭受攻击之前，很多首席信息安全官就已经发现，面对勒索软件攻击，做好备份和恢复策略与防护同样重要。

从UnitedHealth勒索软件攻击事件来看，我们应该从中吸取六个备份教训：

1

实施网络分段和空气隔离备份

在此次遭受的勒索软件攻击中，UnitedHealth承认其备份缺乏网络分段或基础设施隔离，导致攻击者能够锁定备份，阻断了从初始攻击中恢复的途径。

网络分段可以大大减少勒索软件攻击的影响。通过将网络分成较小的独立区域，即使一个区域被攻陷，恶意软件的传播也会被限制。

确保备份存储在离线状态并且已加密，可以减少在勒索软件攻击期间备份被破坏的风险，因为攻击者通常会针对连接的存储系统。实施隔离解决方案可以通过将备份与主网络隔离进一步增强安全性。

2

采用多因素认证（MFA）

MFA的缺失是UnitedHealth勒索软件攻击的核心问题。黑客利用被盗凭证入侵了缺乏MFA的公司系统。可以采用诸如StorageGuard这样的解决方案来审计和验证MFA在所有备份系统中的实施和执行情况。确保MFA的一致性应用有助于保护敏感数据免受未经授权访问，即使用户凭证被盗也是如此。

3

限制管理访问权限

限制管理权限是可靠备份安全战略的重要组成部分，因为这些权限往往是攻击者的主要目标。实施严格的访问控制可以最小化未经授权的用户篡改或删除备份数据的风险，这在网络事件中维护数据完整性至关重要。

具体措施包括：

* 为不同的用户和用户组定义明确的角色，确保只有真正需要的人才能获得组织备份的管理访问权限；
* 对管理接口应用IP访问控制列表；
* 为关键备份更改设置双人规则。

4

提供不可变备份

确保至少一个备份副本存储在不可变存储上。这将确保备份数据不会被恶意行为者（包括勒索软件）更改、删除或加密，并保证网络恢复所需的备份数据的完整性和可用性。

5

定期测试备份

定期进行测试，以验证备份档案和流程的功能。这包括扫描备份以查找恶意软件，并确保可以无问题地恢复。定期测试有助于在实际事件发生之前识别潜在的漏洞。

6

建立安全配置基线

根据DORA最近的要求和NIST此前的规定，为备份和存储环境建立安全配置基线，并使用工具检测基线偏差至关重要。建议定期审计备份系统的安全性，验证备份平台是否经过加固，并防止篡改和未授权访问。

审计应包括：多因素认证、不可变性最佳实践、CISA #StopRansomware指南、关键更改的双重授权、受限管理访问、日志记录最佳实践、账户锁定设置、备份隔离、NAS安全指南、安全快照、加密，以及对NIST、ISO、NERC CIP、HIPAA等标准的遵守。

实施这些策略并利用安全态势管理工具，可以确保备份系统保持安全、可靠，并能够抵御不断演变的网络威胁。

**关于UnitedHealth勒索软件攻击事件**

今年早些时候，UnitedHealth子公司Change Healthcare遭受的勒索软件攻击已成为美国历史上最大的数据泄露事件之一，影响超过1亿人。

2月21日，Change Healthcare发现了勒索软件攻击，该攻击发生在2月17日至20日期间。攻击被归因于ALPHV/BlackCat勒索软件组织，该组织声称窃取了约6TB的敏感数据。3月初，UnitedHealth支付了2200万美元赎金以取回数据。然而，在付款后不久，ALPHV组织实施了"退出诈骗"，带着赎金消失，留下了被盗数据；4月22日，UnitedHealth承认泄露可能影响了"相当大比例"的美国人，估计多达三分之一的美国人口的健康信息可能被泄露。

此次攻击扰乱了美国各地的基本医疗服务，影响了依赖Change Healthcare处理账单和保险理赔的药房和医院。这导致了重大运营挑战，包括患者护理延误和医疗服务提供者的财务损失。报告显示，94%的医院受到不利财务影响，许多医院因系统中断每天损失超过100万美元。

UnitedHealth在2024年应对网络攻击的总成本预计将达到23亿至24.5亿美元，包括收入损失、紧急IT措施和其他相关费用。到2024年10月，UnitedHealth正式确认超过1亿人的个人信息在这次事件中遭到泄露。被窃数据包括敏感的健康信息，如医疗记录、医疗保险详情、个人身份信息（如社会安全号码），以及账单和支付信息等。

对Change Healthcare的勒索软件攻击对UnitedHealth和整个医疗系统都产生了深远影响，凸显了关键基础设施部门网络安全实践中的脆弱性。

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

相关阅读

[瑞数信息马蔚彦：“防”“反”并重，告别亡羊补牢式反勒索](https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651133388&idx=1&sn=ada082df5da6e361467b3c1452a48b04&scene=21#wechat_redirect)

[如何保护数据备份服务器远离勒索软件攻击](https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651121272&idx=2&sn=0ec1f16184e4be98d7c7c93c5a090f66&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMnicXSRCtG4URyLibbqPegjnnibfRB0z4zIzwghbLOkV5fqGYM8vhuQdqw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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