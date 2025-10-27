---
title: 侥幸or庆幸？俄罗斯黑客试图入侵北约某国的大型炼油厂未遂
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247533431&idx=3&sn=05cbf9496e4fc2fd6c5093ae26ca35bb&chksm=fa93f5b6cde47ca0e4b5843901c1c75bfa6a7f77d80384279b7cab5dc1867698318f5054c9bb&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-12-22
fetch_date: 2025-10-04T02:14:25.763447
---

# 侥幸or庆幸？俄罗斯黑客试图入侵北约某国的大型炼油厂未遂

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n4LR46rn4b29Aaiaatd21Bl57tXCaupWbQocoFGOna1ia0oQ6dFicJDbwugVafFjXa0iasPmRBoVsAzg/0?wx_fmt=jpeg)

# 侥幸or庆幸？俄罗斯黑客试图入侵北约某国的大型炼油厂未遂

网络安全应急技术国家工程中心

当地时间12月20日，PaloAlto下属的Unit 42研究团队发布报告称，自从他们在2月初发布了关于高级持续威胁(APT)组织Trident Ursa（又名Gamaredon、UAC-0010、Primitive Bear、Shuckworm）的博客文章以来，乌克兰及其网络域面临着来自俄罗斯的日益增加的威胁。Trident Ursa组织被乌克兰安全局归因于俄罗斯联邦安全局。随着地面进攻和网络空间的冲突继续进行，Trident Ursa一直作为专门的访问创建者和情报收集者运作。Trident Ursa仍然是针对乌克兰的最普遍、侵入性、持续活跃和重点突出的APT之一。鉴于当前的地缘政治形势和该APT组织的具体目标重点，Unit42研究人员继续积极监测其行动指标。为此，Unit 42绘制了过去10个月内Trident Ursa使用的500多个新域名、200个样本和其他入侵指标(IoC)，这些资源持续支持了Trident Ursa的不同网络钓鱼和恶意软件目的。在监控这些领域以及开源情报时，Unit 42发现了多项值得重视的线索，最关键的一个是8月30日，Trident Ursa组织企图破坏北约成员国内的一家大型炼油公司，但未成功。研究报告并未指明该公司的身份，属于哪个国家，是哪家炼油企业。该起入侵企图是通过鱼叉式网络钓鱼电子邮件实施的，使用包含“军事援助”等词的英文文件。另外，报告还披露了对一乌克兰安全研究人员的死亡威胁，一名似乎与Trident Ursa有牵连的人威胁要在初次入侵后立即伤害一名驻乌克兰的网络安全研究人员。

![](https://mmbiz.qpic.cn/mmbiz_png/ss7c5mF5JlSTibkNRsyB2ibtkajo2rWhyTSbBzTc7zkZXay2f4F3oZDcoz2uKg2UtyIbllSjibAdriawrWb84ckhJA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Trident Ursa也被称为Gamaredon、Actinium、Armageddon、Iron Tilden、Primitive Bear、Shuckworm和 Winterflounder，其历史主要是攻击乌克兰实体，并在较小程度上攻击北约盟国以获取敏感数据。Unit 42 研究人员在一封电子邮件中告诉 CyberScoop，尽管他们认为Trident Ursa由不到 10 人组成，但该黑客组织仍然是“针对乌克兰的最普遍、侵入性、持续活跃和集中的 APT”之一。

Trident Ursa在技术上并不复杂，而是依赖于诱饵和公开可用的工具。未遂的那次攻击中，攻击者投送了嵌入鱼叉式网络钓鱼电子邮件中的武器化附件，以在受感染主机上部署VBScript后门，该后门能够建立持久性并执行C2服务器提供的额外VBScript代码。

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n4LR46rn4b29Aaiaatd21BlqHPQHF6PIblL8NQhxTpNBIgic6vktAbiaGkuBRujeibKjrJWeGdwdmZuQ/640?wx_fmt=jpeg)

研究人员还观察到Gamaredon感染链利用地理封锁将攻击限制在特定位置，并利用释放器可执行文件启动下一阶段的VBScript有效负载，随后连接到C2服务器以执行进一步的命令。地理封锁机制起到了安全盲点的作用，因为它降低了威胁行为者在目标国家之外的攻击的可见性，并使其活动更难以追踪。

其他值得注意的方法包括使用Telegram页面查找命令和控制 (C2) 服务器，以及使用快速通量DNS在短时间内轮换多个IP地址，从而使基于IP的黑名单和删除工作变得更加困难。

除了网络攻击之外，更大的安全社区据说还收到了一名据称是Gamaredon同伙的威胁性推文，强调了对手采用的恐吓技术。被威胁的目标是基辅的研究员Mikhail Kasimov 等人。Unit 42的报告称，值得称赞的是，被威胁的研究人员毫不畏惧，并在这些威胁发生后的几周内在推特上发布了更多的Trident Ursa组织的IoC。

![](https://mmbiz.qpic.cn/mmbiz_png/ss7c5mF5JlSTibkNRsyB2ibtkajo2rWhyTqy9nDa5K1sJeomAFXtGT6FBQg6at1gbGWibgT7eCvuAdtp7zkWUhh8g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

12月20日，周二，Mikhail Kasimov在接受The Record采访时称，该威胁是偶然的——仅发生在俄乌战争的早期，此后没有任何后续行动——并指出该用户自2月26日之后再就没有活动。为maltrail项目做网络IoC检测的Kasimov继续分享一系列与Gamaredon 相关的域，并将样本上传到VirusTotal。“无论如何，当有人试图威胁你的生命时，这总是令人不快……幸运的是，我还活着并且健康，”Kasimov说。

此前，美国国家安全局网络主管罗伯.乔伊斯曾发出警告，俄罗斯国家支持的黑客可能会在未来几个月内瞄准北约国家的能源部门。乔伊斯说，这些攻击可能会对乌克兰的邻国产生“溢出”影响，比如波兰。微软也曾警告说，俄罗斯支持的黑客加强了对波兰物流业的攻击，而物流业是乌克兰战争努力的关键推动力。

10月，挪威首相警告称，在Nord Stream I和II管道被怀疑遭到破坏以及对俄罗斯天然气进口实施制裁后，俄罗斯对该国的石油和天然气行业构成了“真实而严重的威胁”，这使挪威成为最大的出口国。

最近针对欧洲石油和天然气行业的大多数网络攻击似乎都是出于经济动机并由勒索软件团伙实施，但FSB历来与俄罗斯地下网络犯罪分子有关——特别是在Maksim Yakubets的案例中，一名被指控的网络犯罪分子还被控窃取机密信息并将其提供给俄罗斯当局。

Unit 42的报告总结道，Trident Ursa仍然是一种敏捷且适应性强的APT，在其操作中不会使用过于复杂的技术。在大多数情况下，他们依靠公开可用的工具和脚本——以及大量的混淆——以及例行的网络钓鱼尝试来成功执行他们的操作。该组织的行动经常被研究人员和政府组织发现，但他们似乎并不在意。他们只是添加额外的混淆、新域名和新技术，然后再试一次——通常甚至重复使用以前的样本。至少从2014年开始，Trident Ursa一直以这种方式运作，并且在整个俄乌战争期间没有放缓的迹象，并且继续取得成功。由于所有这些原因，它们仍然是乌克兰的重大威胁，乌克兰及其盟国需要积极防御。

**参考资源：**

1.https://unit42.paloaltonetworks.com/trident-ursa/

2.https://thehackernews.com/2022/12/russian-hackers-target-major-petroleum.html

3.https://www.cyberscoop.com/russia-hacking-ukraine-nato-energy/

4.https://therecord.media/russian-hackers-targeted-petroleum-refining-company-in-nato-state/

原文来源：网空闲话

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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