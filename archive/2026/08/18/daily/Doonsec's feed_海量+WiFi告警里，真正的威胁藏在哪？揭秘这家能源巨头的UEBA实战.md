---
title: 海量+WiFi告警里，真正的威胁藏在哪？揭秘这家能源巨头的UEBA实战
url: https://mp.weixin.qq.com/s/0yOhPQESeRGR4QZSM-S8iQ
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:55:45.031968
---

# 海量+WiFi告警里，真正的威胁藏在哪？揭秘这家能源巨头的UEBA实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QsTClNuIiapFvlOGvepcuMN2shUbbIxyy8b5TroMlvBvDAb1CQnSePkYAAn1Dp19EWnYtrxLM4obn85TI9OVWorVDuRJpbZQXSJNAzyIRicv4/0?wx_fmt=jpeg)

# 海量+WiFi告警里，真正的威胁藏在哪？揭秘这家能源巨头的UEBA实战

安恒信息

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icVz8RbowK3zzWCaicK1LPbSTJDDcicxleNaqXXSxYPFppNTsB1z02AlkKRMHgtzdCselqbaOWGGfYJPqibodouxRQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

2026年，网络安全领域有个不容忽视的趋势：AI赋能的攻击正在让漏洞响应窗口从“数日”压缩到“秒级”。

随着AI快速发展，网络攻击已进入智能化新阶段，AI伪装渗透、智能钓鱼、自动化批量攻击等新型威胁层出不穷。这类攻击能够精准模仿用户正常操作行为，隐蔽性强、变异速度快、溯源难度高，可针对性渗透工控设备、无线网络、办公终端，突破传统边界防护体系，冲击企业数智化网络安全，新型AI网络威胁已成为企业安全防护的重点难点。

此外，攻击者的目标正在从“攻破边界”转向“潜伏内部”。巴基斯坦石油有限公司遭遇勒索软件攻击、1TB核心数据泄露的事件犹在眼前——能源行业作为关键基础设施，早已成为高级威胁组织的“猎物”。

同时，国家能源局《能源行业数据安全管理办法（试行）》于2026年7月1日起正式施行，能源行业数据安全已从“选做题”变为“必答题”。

当外部攻击变得“更快、更隐蔽”，监管要求变得“更严、更具体”，传统边界防护已难以支撑。如何在内部网络的海量访问行为中，精准识别那些藏在合法流量里的“潜伏者”？

某大型能源公司全面升级网络安全防御体系，携手安恒AiLog UEBA，探索出了一条从“被动响应”到“主动发现”的实践路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QsTClNuIiapHH0zTGqgpKUIYD6gbrBKibCJNvdib1qviao8zicBakWYqN2JItjFYibkzxnSgJJQdplU8M5icXrY8GLKmxouydyYPAcWUlicB4db96GY/640?wx_fmt=jpeg)

**01**

一个扎心的现实：你的SOC团队，正在被告警“淹没”

在能源行业数字化转型过程中，企业内部网络规模持续扩大，终端、服务器、业务系统之间形成了日益复杂的访问关系。传统安全体系主要依赖网络边界设备、安全规则和威胁特征进行检测——防火墙拦截外部攻击、IDS匹配已知特征、杀毒软件查杀恶意文件。

这套“守边界、打补丁”的模式，在应对以下场景时却力不从心：

* 内部设备之间的异常横向访问；
* 未知资产突然访问核心服务器；
* 终端首次访问从未接触过的业务资源；
* 服务器访问关系突然偏离历史规律；
* AI伪装登录、隐性渗透绕过传统特征识别。

当攻击行为未被传统安全设备识别——比如攻击者利用AI技术精准模仿用户正常操作、利用合法凭证在内网横向移动，或者供应链企业通过外包通道潜入核心系统——安全运营团队往往面临着“告警堆成山、风险看不见”的尴尬局面。

世界经济论坛与埃森哲联合发布的《2026年全球网络安全展望》报告指出，能源部门对异常检测技术的需求尤为突出，高达69%的能源企业将异常检测视为安全建设的重点方向。

这一数据背后，折射出整个行业的共识：仅靠边界防御已经不够，必须深入内部网络，从行为视角重新审视安全。

**02**

破局思路：从“边界检测”到“内部行为分析”

传统安全设备更多关注外部攻击行为、已知攻击特征和网络边界威胁，无法有效识别AI伪装攻击、隐性渗透等新型智能威胁。而UEBA（用户与实体行为分析）的核心理念在于：不依赖攻击特征，而是通过建立“正常行为模型”，识别偏离历史基线的异常。

![](https://mmbiz.qpic.cn/mmbiz_png/QsTClNuIiapHgq9XnicicJo6TXfo8xEiax8ias8oF8gYLEDAgMh6kkaLTdS2EiaeCchicEcDCwnoOk6ejYYTUzZRsUwvVfib0k1PrbupyHpZK7NxVWY/640?wx_fmt=png&from=appmsg)

为有效抵御AI智能化网络攻击，该大型能源公司完成全厂态势感知节点全覆盖建设，落地UEBA用户实体智能行为分析系统，打破传统安全设备无法识别AI伪装攻击、隐性渗透的防护瓶颈。公司整合全网设备、无线登录、终端操作等全量日志数据，完成数据标准化治理，依托机器学习构建全域用户与设备行为基线。系统可自主学习正常访问行为，精准识别AI伪装登录、异常资源访问、非常规时段操作等隐性攻击行为，实现未知智能威胁主动发现、精准预警，解决了传统防护被动滞后、新型攻击难以识别的问题。

项目建设的第一步，是完成企业内部资产的全面梳理与分类：

* 终端资产——办公电脑、笔记本等用户设备；
* 服务器资产——核心业务系统、数据库、应用服务器；
* 未知资产——未登记、未归属的网络节点。

结合资产使用者、所属部门等信息进行统一管理后，项目团队对网络访问日志进行自动富化，将原始的IP对IP访问记录，转换为可分析的行为数据：

谁访问了谁？是否符合历史规律？是否首次出现？是否偏离正常访问模式？

最终形成企业内部网络访问行为的动态画像——每一个资产、每一次访问，都有了“正常”与“异常”的参照系。

![](https://mmbiz.qpic.cn/mmbiz_png/QsTClNuIiapEicCYkEvo6O4LjMFuibqQ2LdE9oibic72RSic7LQuxA3fqAC9pcp1cRcw72rlPBAb4NZP8nJGstOxBNpDwx8yx5HQ7ibcvFTJheOrz4/640?wx_fmt=png&from=appmsg)

扫码获取免费试用

**03**

16类风险规则：让“未知威胁”浮出水面

基于资产类型和访问关系，AiLog UEBA构建覆盖8类核心访问关系的行为模型：

1. 终端 → 终端
2. 终端 → 服务器
3. 终端 → 未知资产
4. 服务器 → 终端
5. 服务器 → 服务器
6. 服务器 → 未知资产
7. 未知资产 → 终端
8. 未知资产 → 服务器

针对每一类访问关系，系统分别建立两种检测机制：

首次访问检测

发现历史从未出现过的新访问关系。例如：某台办公终端突然首次访问核心数据库服务器；某个未知IP首次接入内部业务系统。

访问关系偏离基线检测

发现与历史行为模型不一致的访问。例如：某台服务器过去长期只访问固定的业务系统，突然开始频繁访问陌生资产。

8类访问关系 × 2类行为检测 = 16条UEBA风险规则，实现对内部异常访问行为的持续、全面发现，让AI伪装渗透、智能钓鱼等隐蔽威胁无处遁形。

**04**

从100万+误报到精准风险发现

项目运营过程中，AiLog UEBA并非上线即开启全部规则，而是首先进入基线学习阶段。

这一阶段至关重要：通过持续学习企业正常的业务访问模式，系统逐步建立稳定的访问关系模型。正常业务访问带来的“误报”被有效过滤，异常发现的准确率持续提升。

从“百万级告警”到“可运营风险”——传统安全设备每天产生海量告警，安全运营团队淹没在噪声中；而UEBA通过行为基线筛选，将真正偏离正常的风险行为精准呈现，让安全团队从"人工筛查告警"中解放出来，转向“行为驱动的风险研判”。

在稳定运营后，UEBA发现的异常行为进一步联动态势感知与SOAR自动化处置平台，建成“智能监测、AI研判、自动处置、闭环防护”的一体化防御模式，形成：

`异常发现 → 风险分析 → 自动响应 → 闭环运营`的完整链路，实现新型网络威胁分钟级封禁拦截，推动安全运营从“人肉看告警”迈向“智能防风险”。

**05**

实战成效：筑牢对抗AI新型威胁的安全防线

此次智能安全体系升级，补齐了该企业应对AI新型网络攻击的防御短板，构建了主动智能的全域防护体系。上半年，公司累计抵御AI衍生高频攻击15万余次，高危攻击占比达95%，全程实现网络运行零中断、安全事件零发生，筑牢了对抗AI新型威胁的安全防线。

**06**

实践价值：为能源行业安全运营带来哪些改变？

此次实践验证了UEBA在能源行业内部网络安全场景中的切实价值：

* ✅ 从安全设备告警视角，扩展到用户与实体行为视角——不再局限于“有没有攻击特征”，而是关注“行为正不正常”；
* ✅ 从已知攻击检测，扩展到未知异常发现——能够识别AI伪装渗透、智能钓鱼等绕过传统规则的隐蔽威胁；
* ✅ 从海量告警堆积，转向高价值风险运营——让安全团队聚焦真正需要关注的风险；
* ✅ 从人工分析，迈向自动化风险闭环——“智能监测、AI研判、自动处置、闭环防护”一体化模式为规模化安全运营奠定基础。

2026年的安全行业，有一个共识正在形成：身份认证已成为新边界，持续行为分析是阻止横向移动的关键。

对于能源、制造、金融等关键行业而言，网络边界正在模糊化（云化、移动化、IoT化），未来的安全运营，需要理解业务、理解行为、理解“什么是正常的”。

AiLog UEBA 将持续结合行业特点，沉淀更多用户实体行为分析实践，帮助企业构建面向未来的主动安全防御能力。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6Ppczr1X4OOTmbg4rENrqwqbYqRtgl3icicic9an9TicNrOnKOT4t2icSyx7w/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

**点点赞**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6P0OFJt7aruYwYjIWic5WCu7iaE9ZYWmW6TKPcvrib6Itmpc0dnMqlANmow/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

**点分享**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6PwKHSiaCHQrj4D3mJJZ7QGPX1zbt3rJEKjhdBkX12A8r5L47fI28upaA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

**点喜欢**

点击下方名片立即关注

不走丢哦！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6PzUETDErlviazPRtpVtc98iasfL8RCCib8yzmeGJ9HrBlJASFn5qz95QwQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6Pb2aOfdTZnZZbozL1mvicIWsdWicdDcibz2SAuHblLHicWQc8CmX6WT6OMA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6PBQVNtt5ynIG7UjUHbRJFvFXgKjZW6mzjjhlxfjwtXfrdJyPgroKWQA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

**往期****精彩****回顾**

[动态数据安全和静态数据安全，区别在哪？不妨从“治水”说起](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650651596&idx=1&sn=b7ebeb65d9a8951818ff0fff8b7f4a90&scene=21#wechat_redirect)

2026-08-17

[![](https://mmbiz.qpic.cn/mmbiz_jpg/QsTClNuIiapEUe7I4OZ9iaB7S9wLDVCHV7lMQxYxf1PwUJ2HtStc0m8JxbKvMP3S1JQdrE33ez5bz1ApgdCdVaeMExlYia2rZgYU4VCnHE6XtE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650651596&idx=1&sn=b7ebeb65d9a8951818ff0fff8b7f4a90&scene=21#wechat_redirect)

[Sorry勒索软件再拉警报：恒脑能替代逆向工程师吗？](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650651580&idx=1&sn=23c0ccb87685ac9ec8cedbad23bd2f97&scene=21#wechat_redirect)

2026-08-14

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QsTClNuIiapFlsMb3wpIQeoG8evY99KHejzRe8Zy9BnUaxibN2icdKPUpiaWVrVQAKVT2V78DFrjJAq0EwFwKAO0Wib15hVZCicicnYj98PKFjxYjU/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650651580&idx=1&sn=23c0ccb87685ac9ec8cedbad23bd2f97&scene=21#wechat_redirect)

[从好奇到好评<1个月｜恒脑AI代码审计智能体刷新最快复购记录](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650651536&idx=1&sn=a066110dfa537330ad8f6bb344292de0&scene=21#wechat_redirect)

2026-08-13

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QsTClNuIiapHn91umZkgibShibDj9jOPp7rQLLzcQPrAib4icebpg315705qnOeUE0EeaXRTJJGgQcgPTlXvb117koVbnCiappgwcLAXjWicjsPIg8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650651536&idx=1&sn=a066110dfa537330ad8f6bb344292de0&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3wm5VicXg2ibVyMsjPZ3OJSzTwdeSU207GIcBicQDzkDVgFNvXD0npWKhFtBb2VtiaczibVqM8HE0vRoNw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=14)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/cbge2dLXia4bbQyBibIkuZz7hZVFlib5Oib5VZCiacheOLBHzKc88VEQYkXdC7BfdzLSVml0HWO6RjrP7FHL8oL0ONw/640?from=appmsg&wxfrom=5&wx_lazy=1&wx_fmt=other&tp=webp#imgIndex=43)

法律声明

本文数据均来自内部统计、媒体报道、公开信息整理等，仅供信息分享，可能存在统计口径差异或误差，敬请理性看待，我们不对其准确性承担责任。股市有风险，投资需谨慎。阅读者在作出任何投资决定之前，应当咨询各自的顾问。本公众号发布内容仅代表内容创作视角，不构成任何投资建议或投资依据。在任何情况下，本公众号及运营主体不对任何人的投资结果承担法律责任。本公众号原创内容，欢迎合法合规复制、转载，转载时请务必注明出处，不得断章取义、以偏概全或进行有悖原意的引用。

预览时标签不可点

内容含AI生成图片

阅读原文

修改于

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3yb7qoZWcKSwhTB3uxkfjDibSNP8lzqckKw2hXiarlP61qbUia2RUibZ15gV3hiabWypl17tkwrW7SaWOg/0?wx_fmt=png)

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