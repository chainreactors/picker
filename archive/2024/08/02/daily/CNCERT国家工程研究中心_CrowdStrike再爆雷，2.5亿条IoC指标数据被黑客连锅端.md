---
title: CrowdStrike再爆雷，2.5亿条IoC指标数据被黑客连锅端
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546142&idx=2&sn=3bed13ee51a8137bde19c7e538440b5d&chksm=fa9383dfcde40ac998bfc6776e4fb9538966e2799b636740a7c88ac9a05728ba34e16eaee551&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-02
fetch_date: 2025-10-06T18:03:57.623515
---

# CrowdStrike再爆雷，2.5亿条IoC指标数据被黑客连锅端

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176m2qTjVgj5dk8hichkDl1YR2wlnG9Fictl2AiaOeBJiaTQibvdBTvxdUGltvAnG6mRF2UPC6EQR3xWpGFw/0?wx_fmt=jpeg)

# CrowdStrike再爆雷，2.5亿条IoC指标数据被黑客连锅端

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176m2qTjVgj5dk8hichkDl1YR2xcOy1GeiazsDmAiaUZEniaZCYWfBJYcriaoRlBLEYrGcZDwZInUu5BQl0g/640?wx_fmt=png&from=appmsg)

从事件性质来看，此次IoC指标大规模泄漏暴露了CrowdStrike自身的管理问题，其对品牌和客户信任的伤害可能还要远大于导致全球系统大规模崩溃的“意外”事件。

全球大规模系统崩溃的灾难性事件尚未完全平息，CrowdStrike近日再爆大雷。

知名黑客USDoD近日宣称窃取了CrowdStrike全部攻击指标（IoC）数据，共约2.5亿条，并在Breach Forums上发布了其中10万条IoC数据作为样本，该事件立即引发了安全业界广泛关注。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvaqjIJ6apJkxgWztRNHa4wdnO65Yk17GDibEeorwZRLZLxdJXSnww4teQXYbsqL92FzGxm6QKShvUg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

研究者发现，这些IoC指标样本含详细的威胁情报信息，其中包括Mispadu恶意软件和SAMBASPIDER威胁行为者的关键细节。

具体泄漏了哪些信息？

USDoD，曾因入侵FBI的InfraGard安全平台而闻名，宣称此次在Breach Forums上发布的只是他掌握的CrowdStrike IoC数据的冰山一角。首批泄漏数据为一个大小为53MB的CSV文件，包含了10.3万行IoC指标信息。

Hackread研究团队分析泄漏样本后发现，其中包含与Mispadu恶意软件相关的多个IoC指标的详细信息。这些指标包括多种哈希值（如MD5、SHA-1和SHA-256），用于识别特定的恶意文件。所有数据均与SAMBASPIDER威胁行为者相关，涉及网络攻击的“投放”和“安装”阶段，具体如下：

1. 哈希和恶意软件信息：CSV文件包含各种哈希类型，例如MD5、SHA-1和SHA-256，用于识别与Mispadu恶意软件相关的特定恶意文件。
2. 威胁行为者：泄露的样本数据中的所有条目似乎都与威胁行为者SAMBASPIDER有关。
3. 杀伤链阶段：数据突出显示了网络杀伤链的“交付”和“安装”阶段，提供了对恶意软件在目标系统上交付和安装的阶段的深入了解。
4. 置信度级别：每个条目都标有高置信度级别，表明威胁情报的可靠性。
5. 威胁类型：威胁分为多种类型，包括银行威胁、犯罪威胁和模块化威胁，突显了Mispadu 恶意软件的多面性。
6. MITRE ATT＆CK技术：泄漏的IoC指标映射到几种MITRE ATT＆CK技术，例如：

* 执行/用户执行
* 发现/系统检查
* 凭证访问/输入捕获
* 凭证访问/凭证转储
* 命令与控制/数据混淆
* 防御规避/混淆的文件或信息

研究者发现，每个IoC指标都标记为高置信度，表明这些威胁情报的可靠性。威胁类型包括银行、犯罪和模块化等多种类别，展示了Mispadu恶意软件的多面性。

针对USDoD的泄漏声明，CrowdStrike采取了谨慎的回应态度，并未完全否认黑客的说法。该公司分析了部分泄漏数据样本，根据其中“LastActive”日期大致判断数据泄漏可能发生在2024年7月。CrowdStrike认为，USDoD有夸大其词的历史，建议公众对其声明保持怀疑态度。

**IoC指标泄漏的五大危害**

此次大规模IoC数据泄漏可能对CrowdStrike的用户造成严重而深远的不利影响。GoUpSec分析师FunnyG表示，IoC指标信息可能被攻击者利用以规避检测，改进攻击工具和方法，暴露客户安全防御弱点等，具体如下：

**1、攻击者规避检测**

泄漏的IoC数据包含了CrowdStrike用于检测恶意活动的具体指标，如恶意文件的哈希值、恶意IP地址等。这些数据一旦被攻击者获取，他们可以修改或规避这些已知的特征，以逃避安全检测。例如，攻击者可以改变恶意软件的哈希值或使用不同的IP地址，从而避开安全系统的侦测和拦截。

**2、增加客户的安全风险**

客户依赖于CrowdStrike提供的威胁情报来保护其网络安全。泄漏的IoC数据可能包含尚未公开的威胁信息，这些信息对保护客户系统至关重要。如果这些数据被广泛传播，攻击者可能更容易找到和利用客户系统的漏洞，导致潜在的安全事件增加。对于使用这些威胁情报保护网络的企业，可能需要重新评估其安全策略并更新防御措施。

**3、信息误用和安全情报滥用**

IoC指标数据通常包含与恶意软件和威胁行为者相关的详细信息，这些信息对于安全研究人员和企业至关重要。然而，一旦这些数据泄漏，恶意行为者也可以使用这些信息来研究和改进其攻击手段。特别是涉及Mispadu恶意软件和SAMBASPIDER威胁行为者的详细情报，可能帮助攻击者更好地理解安全系统的检测机制，从而进一步精细化其攻击策略。

**4、信任危机和声誉损害**

此次泄漏事件可能导致客户对CrowdStrike的信任危机。客户依赖于CrowdStrike提供安全保护，而此次事件显示了其在数据安全管理方面的不足。长远来看，这可能影响客户对CrowdStrike服务的信任度，进而影响公司的市场声誉和客户保留率。

**5、法律和合规风险**

如果泄漏的IoC数据中包含敏感的客户信息或违反了数据保护法规，CrowdStrike可能面临法律和合规风险。公司可能需要面对监管调查和潜在的法律诉讼，这不仅会导致财务损失，还可能影响公司在行业中的地位。

值得注意的是，这些泄漏的IoC指标对于（其他厂商的）网络安全研究人员和专家也可以利用这些数据，加强对抗Mispadu恶意软件和SAMBASPIDER的安全机制。

**CrowdStrike的黑色七月**

CrowdStrike经历了公司历史上最黑暗的七月。IoC指标大规模泄漏之际，CrowdStrike正忙于响应不久前导致全球系统崩溃的灾难性事件。后者不仅导致大量Windows设备崩溃，还引发了假冒补丁的恶意软件传播，进一步感染了更多设备。这一连串的安全问题，无疑给CrowdStrike带来了巨大压力。

从事件性质来看，此次IoC指标大规模泄漏暴露了CrowdStrike自身的管理问题，其对品牌和客户信任的伤害可能还要远大于导致全球系统大规模崩溃的“意外”事件。因为IoC指标的泄漏不仅增加了CrowdStrike客户面临的直接安全威胁，还可能导致更广泛的安全情报滥用、信任危机以及法律和合规风险。

当前，CrowdStrike尚未对最新的泄漏事件发布新的声明，业界正在密切关注此事件的发展及其对网络安全领域的潜在影响。

**参考链接：**

https://www.crowdstrike.com/blog/hacktivist-usdod-claims-to-have-leaked-threat-actor-list/

原文来源：GoUpSec

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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