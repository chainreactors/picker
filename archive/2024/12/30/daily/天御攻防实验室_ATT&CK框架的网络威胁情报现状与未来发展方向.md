---
title: ATT&CK框架的网络威胁情报现状与未来发展方向
url: https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486210&idx=1&sn=4699dd13d1da4f89b5793fa94dd12b2d&chksm=fb04c86acc73417c894f56578a023d19480e4ed025a216cdfcd3b21edd904e86ba2aceccb01c&scene=58&subscene=0#rd
source: 天御攻防实验室
date: 2024-12-30
fetch_date: 2025-10-06T19:37:09.786305
---

# ATT&CK框架的网络威胁情报现状与未来发展方向

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBDjF4vvsojA1eD0ic8zJNOhXY5q5hicIMV4ibibwIpLHrSqSrHqvEm7hYhQ21n4rBF89kHWzqGLHHHrfQ/0?wx_fmt=jpeg)

# ATT&CK框架的网络威胁情报现状与未来发展方向

原创

天御

天御攻防实验室

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBAwZQYIRcMGdob0eTGKx525Ddp9DrwAwWLOGwL1HNIwiayA2mzhHsdiakoCUfBmN7fib078lq2yjXTMg/640?wx_fmt=other)

本文基于MITRE举办的第5届ATT&CKcon会议演讲内容整理而成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBDjF4vvsojA1eD0ic8zJNOhXvkv22NrLyXpcWkWd91kxAD7d6waQyuQhZzlyn3v8hpJSvFYy5L4aBg/640?wx_fmt=png&from=appmsg)

主要内容：

1. ATT&CK CTI（网络威胁情报）的基本构成

* CTI部分主要用于识别威胁行为背后的"谁"和"什么"
* **框架每年更新两次**，努力及时反映威胁态势
* 目前存在的不足：**北美地区过于集中，对电子犯罪(e-crime)领域覆盖不够**

2. CTI框架的三个基本对象

* 组织(Groups)：基于行为集群来识别威胁组织
* 软件(Software)：包括恶意软件和各类工具(如远程管理软件)
* **活动(Campaigns)：记录特定时间段内组织使用特定工具的行动**

3. 当前优先事项

* 继续跟踪新兴的国家级威胁
* 加强对电子犯罪组织的覆盖
* 改进对勒索软件家族的覆盖（尽管技术上相似度高）
* 关注重要的远程管理工具(RMM)
* 扩大对Campaigns对象的使用（目前不到40个，计划扩展到数百个）

4. 面临的挑战

* 威胁态势变化快，更新周期（半年）较长
* 电子犯罪生态系统复杂，难以准确区分不同组织
* 工具数量庞大，需要重点关注最重要的20%（可覆盖80%活动）
* 长期活跃的APT组织（如APT28）行为模式随时间演变，需要更细致的记录

5. 未来发展方向

* **打破北美地区局限，扩大地理覆盖范围**
* 加强对电子犯罪领域的关注
* 更好地利用Campaigns对象来准确反映活动变化
* **考虑如何处理合法云服务被滥用的情况**

就ATT&CK项目而言，想必大家都熟悉其作为一个由战术组织的技术及子技术集合的特点，这些技术反映了威胁行为体如何开展行动，即其实现目标的行为模式。

ATT&CK框架中的网络威胁情报要素旨在识别这些技术背后的行为主体和具体实施方式，即如何在实际环境中实施和捕获这些行为。因此，ATT&CK的网络威胁情报部分致力于及时把握相关威胁态势。

考虑到我们采用每年两次的更新周期，而威胁态势变化迅速，我们正在尽最大努力确保与实际情况保持一致，并始终致力于确保框架中反映最重要的要素。

然而，自本人于今年一月加入团队以来，观察到若干需要改进的领域，主要包括：扩大北美地区以外的地理覆盖范围，特别是加强对电子犯罪领域活动的记录。ATT&CK的网络威胁情报主要聚焦于高级持续性威胁或国家支持的行为体，这部分原因在于这类行为体的活动方式带来的挑战，但我们正努力使其更加符合行业观察到的情况，以及我们的利益相关方日常面临的实际情况。

最后，作为本人为团队设定的目标之一，这也与前任提出的建议相一致，我们希望更好地利用网络威胁情报框架中相对被忽视的活动(campaigns)对象，以更准确地反映活动随时间的演变。

## **框架构成**

ATT&CK网络威胁情报对象包含三个基本要素：

1. 组织(Groups)：指代这些行为体的身份或性质。关于"谁"的问题涉及复杂的归因问题，我们通常基于行为模式集群来关联组织，这更接近钻石模型而非取证分析直接指认具体责任人。当然，在可能的情况下，我们也会进行具体归因，但这种情况相对少见。
2. 软件(Software)：组织为实现目标和完成技术要求而使用的工具，不仅包括恶意软件，还包括如远程克隆或远程管理维护软件等工具，这些都用于促进行为体达成目标。
3. 活动(Campaigns)：组织在特定时间段内针对特定目标使用特定工具的离散行动。这记录了某一组织从时间A到时间B期间，使用特定工具针对特定目标的活动快照。

## **优先事项**

在高级持续性威胁或国家支持的威胁方面，我们将继续记录新出现的国家主导威胁。就时间而言，这与近期情况略有不期而遇：我们下周将发布更新，而最近几周新闻中频繁出现的"Typhoon"相关报道表明，有时更新周期与实际情况难免存在时间差异。

然而，我们致力于尽可能多地记录这些情况，确保ATT&CK继续作为权威参考标准，不仅在于识别相关行为体，还在于提供参考资料，使研究人员能够追溯特定威胁行为体的信息来源，支持他们开展研究和分析。

## **未来发展方向**

我们将在保持现有工作重点的同时，加强对电子犯罪领域的关注。这一点在最近的ATT&CK更新中已有体现，我们正努力扩大这方面的工作，包括尽可能记录电子犯罪组织。鉴于勒索软件即服务(Ransomware-as-a-Service)等软件生态系统带来的挑战，这项工作存在一定难度，但我们正努力区分组织、软件和活动之间的关系，这也解释了为什么您可能会看到某些组织与特定软件相关联，而该软件可能同时被其他实体使用。

在软件方面，我们将继续关注恶意软件，确保记录重要的独特恶意软件，并扩大对信息窃取软件和中间件工具的覆盖。然而，考虑到现有软件的庞大数量，我们需要作出取舍，确定最相关的记录对象。

关于勒索软件，这是一个特殊问题。我们希望改进对勒索软件家族的覆盖，但从技术角度而言，勒索软件的行为相对单一：加密文件、访问进程等。从科研或研究价值角度看，记录每一个独特的勒索软件变体的意义有限，但对于使用软件库进行映射和参考的机构而言，这些信息具有重要价值。

对于在入侵活动中使用的工具和实用程序，如远程管理维护工具，这是一个颇具挑战性的领域，因为此类工具数量众多，且行为体已经利用了相当数量的此类工具。虽然我们无法覆盖所有工具，但我们将努力覆盖最重要的工具，确保ATT&CK遵循80-20原则，即记录负责80%或更多活动的20%工具集。（笔者注：过于关注ATT&CK的覆盖率没有太大意义）

## **关于活动(Campaigns)对象**

根据最新统计，在下一版本发布之前，我们的活动对象数量不足40个，而实际上我们应该拥有数百个。这一情况将得到改变，包括将社区提交的内容适当修改为活动主题。

这一变化源于业界反馈。例如，有关方面在查看APT28的活动时发现，其几乎覆盖了整个ATT&CK矩阵。这带来了模拟难度的问题。实际上，对于长期活跃的实体如APT28、Sandworm、APT5等，它们的行为模式随时间不断演变，将所有这些记录合并在一个条目中会扭曲我们的观察视角。

因此，我们将努力更好地记录这些实体在特定入侵活动中的表现，使ATT&CK框架的使用者能够确定这些实体在最近时期或针对特定部门的行动中的具体表现。

此外，电子犯罪领域多个行为体之间的关系往往较为模糊，这使得活动记录比明确的组织划分更为适用，特别是在仅有特定信息窃取工具或勒索软件变体的情况下。

## **问答环节**

问：是否计划在工作中使用RMM项目？

答：我们当然会参考补充使用。我们欢迎其他方面开展的工作。但考虑到远程管理维护软件数量众多，我们的资源有限，无法全面覆盖。我们将尽最大努力记录最重要的内容，但对于较小的对象，除非其具有独特或有趣的特点，我们可能无法覆盖，因为新的工具不断出现。我们感谢社区的贡献，但确实需要在实际可行的范围内开展工作。

问：关于合法云服务的使用情况...

答：对于合法云服务被滥用的情况，这确实是我们希望记录的内容。我们看到各种云服务提供商的服务被用于不当目的。然而，这在ATT&CK框架整体中造成了一定的张力，特别是在基础设施领域，因为从行为角度很难将这些捕获为具体动作。可能存在其他方案来记录这些情况，我们会保持关注，但目前尚未有明确答案。

**ATT&CK框架主要局限性：**

1. 更新周期的滞后性

* 框架仅每半年更新一次
* 而网络威胁态势变化迅速
* 正如演讲者提到的"Typhoon"事件，往往出现新威胁时无法及时反映在框架中

2. 地理覆盖范围不均衡

* 过度聚焦于北美地区
* 缺乏对其他地区威胁行为体的充分覆盖
* 这可能导致对全球威胁态势的认知偏差

3. 威胁类型覆盖的不平衡

* 主要关注APT（高级持续性威胁）和国家支持的威胁行为体
* 对电子犯罪（e-crime）领域覆盖不足
* 特别是在快速发展的勒索软件即服务（RaaS）生态系统方面存在盲点

4. 对活动（Campaigns）对象的利用不足

* 现有Campaign对象不到40个，远低于实际需求
* 难以准确反映长期活跃威胁组织（如APT28）的演变过程
* 无法有效展示特定时期或特定目标行业的具体威胁特征

5. 工具覆盖的挑战

* 面对大量合法工具被滥用的情况（如远程管理工具RMM）
* 无法完整覆盖所有相关工具
* 只能采用80-20原则，重点关注最常用的20%工具

6. 分类和归因的困难

* 在电子犯罪领域，组织、软件和活动之间的关系模糊
* 难以准确区分不同组织，特别是在勒索软件即服务环境下
* 取证分析和具体归因的难度较大

7. 合法云服务滥用问题的处理

* 难以在现有框架中准确描述合法云服务被滥用的行为模式
* 在基础设施层面缺乏有效的行为描述方法
* 这反映了框架在处理"灰色地带"行为时的局限性

**推荐阅读**

**闲谈**

1. [中国网络安全行业出了什么问题？](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485457&idx=1&sn=d45cc35242cdc83e98b124531ea7c093&chksm=fb04cb79cc73426f21801f35912b626bf515dc2b9d85b3da578f8087d0a2960396ef1e6347bc&scene=21#wechat_redirect)
2. [国内威胁情报行业的五大“悲哀”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484999&idx=1&sn=485863f4e66a62f55aa69334c787e6f3&chksm=fb04c52fcc734c3919fc28c61a9b13488b89efe4c1ba5cb16f8f00f0c6e996c7f1df47984463&scene=21#wechat_redirect)
3. [对威胁情报行业现状的反思](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486063&idx=1&sn=11e005a726ced95e872e2ce7fb228ba2&chksm=fb04c907cc734011310b2cc58a4a6f1ac764ece04c7d7ca9f3e93f0849f92c5e891b32e4c58f&scene=21#wechat_redirect)
4. [安全产品的终局](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484846&idx=1&sn=35bab89f917f5043919e40893268d576&chksm=fb04c6c6cc734fd05c0423dc971a0578eb8b951ef1764be0a99e2bdd1c26b736d64cf61b6d77&scene=21#wechat_redirect)
5. [老板，安全不是成本部门！！！](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485908&idx=1&sn=b6cff013a1e9a9599bdde63ce56ecec0&chksm=fb04cabccc7343aac55b3c43020c855bade147461fece597f730bc0460e65c5610dd0f5d988b&scene=21#wechat_redirect)

**威胁情报**

1.[威胁情报 - 最危险的网络安全工作](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485331&idx=1&sn=0857185a1bc7ed04c2d1edc60cb93a34&chksm=fb04c4fbcc734dede0fd243984c30250ff7859f68a265b1a278ac72a5761ac0ccaf0038537ec&scene=21#wechat_redirect)
2.[威胁情报专栏 | 威胁情报这十年（前传）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484880&idx=1&sn=c2b5730f2a7011959096526ff775c8ac&chksm=fb04c6b8cc734fae9f6d2e0693cecd5fd594a01694d8e38bd95926cb88a0f627c3d5b2f36ea2&scene=21#wechat_redirect)
3.[网络威胁情报的未来](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485003&idx=1&sn=76253d23e51dde8dbf4d675b79ab43cf&chksm=fb04c523cc734c352490ca37f55f1c3a989d55807298cb308aa3c126e24816d6fda11a8766f1&scene=21#wechat_redirect)
4.[情报内生？| 利用威胁情报平台落地网空杀伤链的七种方法](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485042&idx=1&sn=afd1212b585f30bccdece8471fadd31d&chksm=fb04c51acc734c0c9fd0d1d388b7672defbe5ce17a10af58d3a5d336ba21fa21398b4ad860e2&scene=21#wechat_redirect)
5.[威胁情报专栏 | 特别策划 - 网空杀伤链](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484709&idx=1&sn=649a27516ca01baab49ce750e3502cc3&chksm=fb04c64dcc734f5becd252686228f6c3c2bd00bff52041e9dae6fde2008e1a43057989b9d16f&scene=21#wechat_redirect)
6.[以色列情报机构是如何远程引爆黎巴嫩传呼机的？](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486027&idx=1&sn=7d9215cbf71327fccda006c6c29938a3&chksm=fb04c923cc734035c661d4e3b93ad1e631fd55ee5a4ba7cd855c7e37bc513ca071860fdfb9b9&scene=21#wechat_redirect)
7.[对抗零日漏洞的十年（2014～2024）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486036&idx=1&sn=52131d932e8fe4f24db3d7bdf41625a0&chksm=fb04c93ccc73402a24144d8262153a73bc18c2098109a9885d2413dba9a33af83f8d664bc317&scene=21#wechat_redirect)
8.[零日漏洞市场现状（2024）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486041&idx=1&sn=1c9dc7508ba7d09c8f7c88f3018bae1d&chksm=fb04c931cc734027d17b83f774416085b6c492306ccf49f76cb99fa1fbf8b03c7ff6af23a781&scene=21#wechat_redirect)

**APT**

1. [XZ计划中的后门手法 - “NOBUS”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485524&idx=1&sn=aa2b7b0d57b250e5cc101e5dcbebbca6&chksm=fb04cb3ccc73422a9fe22937b801eceb205ceaf8bf3b76a92143d575d55e5fd2eef5adfacb36&scene=21#wechat_redirect)
2. [十个常见的归因偏见（上）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484868&idx=1&sn=3d65e81115c967b165fa16021a211967&chksm=fb04c6accc734fba7c760fd14caaaf9a2d7991acc2557ee340e772ccbb805b30f1a46c793e8a&scene=21#wechat_redirect)
3. [抓APT的一点故事](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485237&idx=1&sn=9152fcb5f5b1f884e6da97ba9b04f69a&chksm=fb04c45dcc734d4bd8fbede2ae93dc52feeaaa11e215a3240bca32f3d43444a2c909e01a2814&scen...