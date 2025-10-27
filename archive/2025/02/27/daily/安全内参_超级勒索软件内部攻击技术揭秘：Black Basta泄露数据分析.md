---
title: 超级勒索软件内部攻击技术揭秘：Black Basta泄露数据分析
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513835&idx=1&sn=514f5b8c2e5316d4a9d48dfe4ae3d830&chksm=ebfaf1cbdc8d78ddfe11edf5a3b4af60d7bc7f53fe3dfda309d9e4c54cdaa9378ecff20143ab&scene=58&subscene=0#rd
source: 安全内参
date: 2025-02-27
fetch_date: 2025-10-06T20:36:16.393455
---

# 超级勒索软件内部攻击技术揭秘：Black Basta泄露数据分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tgHlT5PFXLfJ5DNA6VicKur5mGl1TxC25Pl5U8FVIFsK6YBdYoWG3SjJEXfcebj4CMoVITibbYRs9Q/0?wx_fmt=jpeg)

# 超级勒索软件内部攻击技术揭秘：Black Basta泄露数据分析

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7vQ0NWEgFIdmPL2ygumbOpeRexqoCv4H6dhDYVmicDwKHOQWXHnlibrzNOO8RZLjg6PicDEzsIrW8L0w/640?wx_fmt=jpeg)

**泄露聊天记录揭示了该团伙的攻击技战术和运作内幕，为防御方提供了宝贵情报。**

前情回顾·**打击勒索软件动态**

* [11国联合执法：勒索软件之王LockBit遭受毁灭性打击](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247511020&idx=2&sn=2132ce877f82a70a0b4b840642e884b6&scene=21#wechat_redirect)
* [伊朗勒索软件组织攻击美国企业，遭美政府溯源真实身份并制裁](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247505955&idx=1&sn=4728c591454ff573e359236bba8f45fa&scene=21#wechat_redirect)
* [“最成功勒索软件团伙”如何运营武器库：Conti泄露数据分析](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501920&idx=2&sn=a60d8c07d0ebeff8877bf16fa48c4d00&scene=21#wechat_redirect)
* [俄乌冲突引发网络武器库泄露：Conti泄露数据全面分析](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501703&idx=1&sn=e05a11061c61796d1f5c2581b61217e2&scene=21#wechat_redirect)

安全内参2月26日消息，全球最活跃的勒索软件组织之一Black Basta近一年多的内部通信在网上公开，泄露了其成员的战术、商业机密和内部裂痕。

据分析，这些通信记录是Black Basta成员在2023年9月至2024年9月期间，通过Matrix聊天平台相互发送的20多万条信息。发布这些信息的人说，此举是为了报复Black Basta针对俄罗斯银行的行为。泄密者的身份尚不清楚，也不清楚泄密者是组织内部人员还是组织外部人员以某种方式获取了这些机密日志。

**泄露通信记录暴露勒索团伙技战术**

研究人员在筛查Black Basta泄露的通信记录时，发现了该团体偏好的工具和技术的详细信息，包括定制的恶意软件加载器、泄露指示器、加密货币钱包以及与该团体附属成员相关的电子邮件地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tgHlT5PFXLfJ5DNA6VicKuriaeKLpiblFjic8yVWmYOkfQAPaicVEYbgzyPlKGWNkOgtuWuNc3Liab0U4w/640?wx_fmt=jpeg&from=appmsg)

多位网络犯罪分析专家将此次泄漏的重要级别，与2022年Conti勒索软件团体内部消息的大规模曝光相提并论。Black Basta大约在同一时期出现，是Conti的一个分支。

Recorded Future威胁情报分析师Allan Liska表示：“我们经常看到小团体的信息泄露，但根据我们能收集到的情报量来看，除了Conti，其他团体的泄露都无法与之相提并论。”

威胁情报研究人员将泄露的Black Basta消息上传到ChatGPT，以便快速分析数据并将其应用于威胁狩猎工作。

微软高级安全研究员Thomas Roccia在独立分析数据时，发现这近20万条俄语消息涵盖了截至2024年9月为期一年的时间。Roccia提取了潜在的泄露指示器，包括Black Basta附属成员聊天中提到的IP地址、域名、凭证和文件名。

还有研究人员总结了该团体如何获得初步访问受害环境并躲避检测的技术细节。

Prodaft首席情报官Halit Alptekin在邮件中表示：“防御者可以根据威胁模型，检查威胁行为者的战术、技术和程序。这也让他们有机会从攻击者的角度了解网络犯罪活动。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FzZb53e8g7tgHlT5PFXLfJ5DNA6VicKuribmxO6JfBR7emNPqrgDibd5je0DN4HbJZqF6ZKkGQwYzYgWj4ibNQLDSw/640?wx_fmt=png&from=appmsg)

*图：Black Basta勒索软件团伙积极利用的10个漏洞（Qualys）*

虽然最具可操作性的情报可能包含在聊天记录中发现的泄露指示器中，但Alptekin表示，随着Black Basta附属成员关闭系统，这些基础设施很快将变得过时。

Alptekin表示：“从威胁情报和执法角度来看，这种类型的泄露极为宝贵。它们提供了该团体使用的服务、战术、技术和程序、威胁行为者之间的内部关系、运营工作流程以及通信方法的洞察。这种情报对于破坏网络犯罪网络并了解它们不断发展的策略至关重要。”

**勒索软件团伙的运作内幕揭秘**

Black Basta的内部运作揭示了一个充满内部冲突的网络犯罪团体。然而，这个臭名昭著的勒索软件即服务组织的附属成员，却在全球范围内给多个组织带来了巨大破坏。

根据美国网络安全和基础设施安全局（CISA）的数据显示，在两年的时间里，这种勒索软件变种被用于加密和窃取至少12个关键基础设施部门的数据，影响了500多家组织。

Elliptic与Corvus Insurance的研究发现，截至2023年底，该团体通过勒索支付至少获得了1.07亿美元。

Alptekin表示，Black Basta的泄露发生在今年初，团体活动有所减少，原因是其关键成员跳槽到其他网络犯罪组织，如Cactus勒索软件团体。他说：“这次曝光进一步破坏了该团体的稳定性，影响了其成员之间的信任。”

Rapid7在去年10月初观察到，与Black Basta运营者相关的社交工程攻击回升，但该团体今年大部分时间处于不活跃状态。

谷歌威胁情报组网络犯罪分析主管Genevieve Stark表示，从其他勒索软件团体之前泄露的聊天记录中获得的情报，包括与Conti操作相关的聊天，揭示了他们运作中使用的基础设施、命令和非法服务的细节。

Stark在邮件中表示：“防御者可以利用这些信息来优先处理检测和狩猎工作。”她补充道，这些消息还可以支持研究人员的归因工作，揭示交易工件、组织层级、网络犯罪分子之间的关系以及他们所扮演的角色。

Stark表示，Conti聊天泄露“揭示了谁开发了特定的恶意软件家族，某些威胁行为者的所在位置，还有信息表明，这一活动的子集并非出于财务动机，而可能与俄罗斯情报机构有关。”

此外，Black Basta的内部通信反映了网络犯罪分子在合谋者中间过度分享和自夸的倾向。

Liska表示：“如果说勒索软件团体有什么特点，那就是他们非常喜欢聊天。虽然他们是超级大犯罪分子，但在保密这件事上做得不好。”

**参考资料：cyberscoop.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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