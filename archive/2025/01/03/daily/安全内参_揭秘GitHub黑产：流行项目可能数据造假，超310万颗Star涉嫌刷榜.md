---
title: 揭秘GitHub黑产：流行项目可能数据造假，超310万颗Star涉嫌刷榜
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513415&idx=1&sn=67784cb766efc250d0dc5f9f2f3814d5&chksm=ebfaf267dc8d7b71b9ae3bd6a084f9919989ef05da89dd36e95ec173107b2d367ea1ca79473f&scene=58&subscene=0#rd
source: 安全内参
date: 2025-01-03
fetch_date: 2025-10-06T20:09:38.981957
---

# 揭秘GitHub黑产：流行项目可能数据造假，超310万颗Star涉嫌刷榜

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tbIHSMu8fLHGlBicjPs3k1LPD1gZCNor0Td9gPadAUJibibZyz1W9gVvBHic1asjcI1GSsjJTMVAvFgw/0?wx_fmt=jpeg)

# 揭秘GitHub黑产：流行项目可能数据造假，超310万颗Star涉嫌刷榜

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tbIHSMu8fLHGlBicjPs3k1Ltp7BWSmzssojriaVYbooFibg0iaHCkg0jIgvUfHHSCZgiaW1NV8yOzCg3A/640?wx_fmt=webp&from=appmsg)

**虚假Star星标削弱了用户对GitHub平台和托管项目的信任，欺骗性代码库在GitHub上已非常普遍，各类攻击者都在尝试利用该问题；**

**用户选择开源软件项目时，不应仅依赖星标指标，还应进一步评估项目活跃度和质量，尽可能审查代码。**

前情回顾·**网络黑产动态**

* [ChatGPT黑产出现：每100次收费37元，还能修改恶意软件代码](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507930&idx=2&sn=fd626066f1b821095fd199c426772c12&scene=21#wechat_redirect)
* [俄罗斯黑客劫持美国机场出租车调度系统搞黑产](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507284&idx=1&sn=deed8954a69e29a3aa114af4c73a7f6f&scene=21#wechat_redirect)
* [为数千非法网站提供域名防封技术，云南破获全国首例域名黑产犯罪案](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247506963&idx=1&sn=abf1d5f74ca3d524b443fac69ae4f617&scene=21#wechat_redirect)
* [为境外“黑灰产”网站提供链接服务还拒不整改？网站负责人被刑拘](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247502967&idx=3&sn=71086d1d22eb176edcb14e2e3d3a7f38&scene=21#wechat_redirect)

安全内参1月2日消息，GitHub目前正面临一个严峻问题。大量虚假“星标”（Star）被用来人为抬高诈骗性和恶意软件代码库的受欢迎程度，从而吸引更多毫无防备的用户。最新研究显示，近五年GitHub上至少有310万个星标涉嫌刷榜。

星标类似于社交媒体中的“点赞”按钮，GitHub用户可以用这个功能来标记他们感兴趣的库。GitHub将星标作为全球排名系统的一部分，同时向用户推荐它认为可能感兴趣的相关内容。

GitHub解释称：“您可以通过为库或主题加星标，发现GitHub上类似的项目。当您为某个库或主题加星标时，GitHub可能会在您的个人控制面板上推荐相关内容。”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tbIHSMu8fLHGlBicjPs3k1Lib7bXc2iaPp42icSTuVpZ2tDSgKbEiaiaEibsxjrp2UALZiblvTHKHyriaIvuw/640?wx_fmt=jpeg&from=appmsg)

*图：获最多星标的库，拥有40.8万个星标*

这一问题此前已被披露过。例如，2024年7月Check Point曾发现一个名为“星标幽灵网络”（Stargazers Ghost Network）的恶意软件分发服务。该服务通过一个广泛的虚假用户网络为恶意项目增加星标，以推广信息窃取型恶意软件。

即使是非恶意项目，有时也会利用虚假星标提升其受欢迎程度，以扩大覆盖范围，吸引更多合法用户的关注、真实星标以及采用率。

由Socket、卡内基梅隆大学和北卡罗来纳州立大学研究人员联合开展的一项新研究，让我们更清晰地了解了问题的规模。研究表明，GitHub上疑似虚假的星标总数高达450万。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tbIHSMu8fLHGlBicjPs3k1LFWlwIFVuVyWicHMVegVnUwgzU9XBGsF6iaJkxuCkRKe4m5rQQkKbl61A/640?wx_fmt=jpeg&from=appmsg)

*图：GitHub星标服务列表*

**寻找虚假星标**

研究人员开发并使用了一款名为StarScout的工具，对来自GHArchive的20TB数据进行了分析，以定位虚假星标。

GHArchive包含自2019年7月至2024年10月期间超过60亿条GitHub事件元数据，涵盖3.1亿个库的6050万用户行为以及6.1亿个星标。

StarScout能够识别GitHub上的极不活跃用户，例如仅为单个库加星标的用户，或表现出机器人或临时账号活动模式的用户，以及在短时间内为同一库加星标的协调账号群组。

该工具的方法基于“CopyCatch”算法，这是一种专门用于检测社交网络中欺诈行为的算法。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tbIHSMu8fLHGlBicjPs3k1Lgjzmfe6UrTEuiaOMSoanmx4opLYFMTAiaTTwDmFGzic0v3MrX5Tc9Btow/640?wx_fmt=jpeg&from=appmsg)

*图：StarScout数据处理流程*

**450万星标被怀疑为虚假**

通过对数据应用低活动和同步特征的算法以识别可疑星标，研究团队发现共有453万疑似虚假星标，由132万个账号为22915个库提供。

为提高检测结果的可信度，研究人员过滤了潜在误报，仅分析那些单月内出现显著异常加星活动的库，并且虚假星标占总星标比例超过10%的情况。

经过筛选，最终确认310万虚假星标，由278000个账号为15835个库提供。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tbIHSMu8fLHGlBicjPs3k1Le5OLhsicrw2R80enb1KibZurJmrnLXtQ3phR3rnmep2JPBw9LTTCWzDQ/640?wx_fmt=jpeg&from=appmsg)

*图：虚假模式识别（如聚集行为）*

截至2024年10月，大约91%的受影响库以及62%的疑似虚假账号已被删除。这一结果证明了StarScout工具的准确性。

研究还显示，虚假星标活动在2024年迅速激增，其中7月期间超过50个星标的库中约有15.8%涉及此类恶意活动。

研究人员在2024年7月向GitHub报告了StarScout识别出的虚假库和账号，GitHub随后将其全部移除。然而，研究团队仍在评估和报告2024年11月发现的其他聚集行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tbIHSMu8fLHGlBicjPs3k1LgdhYnF2Q2ObCu82ezZfsuVz79uV0HHoqvOKyGRp8KFOxrlpWics9JEg/640?wx_fmt=other&from=appmsg)

*图示：虚假星标库的词云（已删除与现存）*

**虚假星标的影响**

虚假星标对GitHub及其用户的影响是多方面的。总体而言，这一问题削弱了用户对平台及其托管软件项目的信任。

用户在选择库时，应避免仅依赖星标数量作为判断标准，而是进一步评估库的活跃度和质量，仔细阅读文档、检查内容和贡献记录，并尽可能审查代码。

欺骗性GitHub库的存在已非常普遍，甚至一些国家支持的行动也曾利用该平台。因此，在从GitHub下载软件时需格外谨慎。

外媒BleepingComputer已联系GitHub以了解其更多应对虚假星标问题的措施，但截至目前尚未收到回复。

**参考资料：bleepingcomputer.com**

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