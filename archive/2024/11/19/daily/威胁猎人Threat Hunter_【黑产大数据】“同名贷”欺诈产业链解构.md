---
title: 【黑产大数据】“同名贷”欺诈产业链解构
url: https://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247498279&idx=1&sn=ef49c6e26ca1312d532279705b32c63d&chksm=eb12dc1cdc65550a23fcd24ed120fc22cd60a257dcd65bfad0e02edc27aa8419a82ff198a97f&scene=58&subscene=0#rd
source: 威胁猎人Threat Hunter
date: 2024-11-19
fetch_date: 2025-10-06T19:21:01.188870
---

# 【黑产大数据】“同名贷”欺诈产业链解构

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqFwIxFFMgT6P9RyR1F2GbST6QwRrs7dDDKDPsUKOWna5VZIajldm2ZxjOBicZGFibNibMe4PEAthGVZg/0?wx_fmt=jpeg)

# 【黑产大数据】“同名贷”欺诈产业链解构

原创

猎人君

威胁猎人Threat Hunter

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/4mAgZtBianqHwB5L4n1SdUaicvcFspoC5LC0sR6QhONHlmxKqJbr50j9XvHibLLDeVM6GzOPt57raMG2kxzAuFfoA/640?wx_fmt=gif)

早些年，因“同名同姓”莫名背上“贷款”的事件并不少见，那时候金融机构在做贷款人身份信息确认时还没有人脸验证等措施，黑产或一些不法分子通过一些违规操作，**利用“同名同姓”人的身份信息**为有贷款需求的人进行贷款并非难事。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFwIxFFMgT6P9RyR1F2GbSToCTdXaicC8Hw6ibWIfT9lhxPrQBf1veHnS64C5mhJ23m0Hqhia4BrJia5g/640?wx_fmt=png&from=appmsg)

近年来，随着金融机构审核机制的完善以及人脸认证措施的加入，黑产想直接套用“同名同姓”人的身份信息进行贷款已经没那么简单了，但“同名贷”并没有因此而消失，而是以另外一种欺诈形式活跃在黑产圈中。

威胁猎人研究发现，黑产团伙会招募**一些资质较差、有征信记录、有贷款意愿且姓名简单、大众化**的客户，再**勾结金融机构“内鬼”或利用金融产品规则漏洞**，**把资质好的“同名者”的资质信息套用在资质差的客户上**，给这些客户操作**信贷、企业贷**等业务，共同实施“同名贷”骗贷。

这种通过**套用资质信息的“同名贷”欺诈**已形成了成熟的产业链，参与“同名贷”的客户一般**还款意愿比较低，贷后逾期风险极高**，最后往往是放款金融机构承担所有的风险。

本文基于威胁猎人对**“同名贷”欺诈产业链**的研究，客观呈现“同名贷”欺诈中客户招募手法、欺诈流程、风险特征等，为银行等金融机构的贷款风控策略提供参考。

一、“同名贷”欺诈手法分析

二、“同名贷”风险特征总结

三、“同名贷”风险案例

四、威胁猎人金融贷款反欺诈服务

**一、“同名贷”欺诈手法分析**

***1.1*****目标客户招募**

威胁猎人研究发现，黑产一般会通过**黑产群、社交软件**召集多手黑中介招募姓名为**“大众化名字、姓名两个字、征信记录良好但资质较差**（如无稳定收入、无正常工作）”的客户操作非标“同名贷”，**涉及信贷、商户贷等场景**。

以下是黑产招募的广告信息和名单样本：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFwIxFFMgT6P9RyR1F2GbSTBzSbkN4eVV4DdS5SJ5E3zN6fFibjlj4MRwYsCvQqWc8VntB3oPgLhWg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFwIxFFMgT6P9RyR1F2GbSTfhQJUXAyNtoe9gQNTugt6yjLZ9rMuLjfGjEDEibYrrDmZ0RM4iaLkzicw/640?wx_fmt=png&from=appmsg)黑产/黑中介“同名贷”招募名单样本

***1.2*****“同名贷”欺诈流程**

在整个“同名贷”欺诈流程中，主要涉及三个角色：

**黑产：**也是主要操作方，利用金融机构内部关系收集名字简单、大众化的优质客户信息资料形成信息库（大众化、两个字姓名的人在全国范围内存在同名同姓的概率较高，更容易匹配），再把“同名贷”产品化，同步给黑中介进行目标客户招募，最后通过“同名信息套用”的方式把优质好的同名者信息套用在资质差的目标客户上，完成大额贷款申请。

**黑中介：**在各种社交软件、中介群等发布招募广告，招募符合条件的意向客户（即目标客户）。

**目标客户：**有贷款意向的客户，但因资质差无法贷款，在黑产的帮助下获得“好资质”，共同完成“同名贷”，这类人往往做好了成为失信人的打算。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGMdJ8c0yeO1s23l2yuqvCRhgjLMGkrZRuU3JdJibTWbE6zCHNuuIcRDtGvputIfDl126mib44Y0ymA/640?wx_fmt=png&from=appmsg)

“同名贷”欺诈流程图

**二、“同名贷”风险特征总结**

威胁猎人情报研究员通过对黑产欺诈手法、流程等进行风险分析，对“同名贷”套用他人信息操作信用贷、企业贷等贷款的风险特征做出概况总结，主要涉及本案件风险画像，具体情况如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFwIxFFMgT6P9RyR1F2GbSTd8bbDH6rvbWjJBcwWZRia58koW0LJ4jwu6D0lfn8421yKrB4kIoPxnA/640?wx_fmt=png&from=appmsg)

**三、“同名贷”风险案例**

***3.1*****信贷风险案例**

某黑产主营业务为非标“同名贷”业务及房企背债业务及背债不良资产包等业务。其非标“同名贷”招募的客户画像为“年龄25-49岁，男女不限，姓名两个字，征信良好，当前没有逾期，负债最高在50万内，客户操作贷款后，其黑产公司会帮客户代还一年利息，总贷款额度80-130万”，以下为黑产在黑产群的招募广告：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGMdJ8c0yeO1s23l2yuqvCR0MPt6XmySicXtqIp12Y4Pp2A6ml2ehmWaicicZzg7O9ibYtiblSItM1ygWg/640?wx_fmt=png&from=appmsg)

黑产“同名贷”招募广告

该黑产表示，主要通过操作银行线下**信贷业务**，**操作城市为河南省郑州市**，如果客户资质差的则套用同名对应的优质信息去申请，**因其上游操作方有某银行行口关系，往往很容易成功申请多笔大额贷款**。

***3.2*****商户贷风险案例**

某黑产主营背债业务、非标“同名贷”、信贷欺诈等业务。该黑产召集全国范围内召集“年龄25-50岁，户籍不限，征信有过信用记录（如有过房贷、车贷、信用卡3N等记录）、大数据干净、做过某某银行贷款的也可以，做的是纯线上业务，智商不全、残疾均可办理，一人可操作2-5笔贷款，单笔最高金额100万”。以下为黑产在黑产群的招募广告：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFwIxFFMgT6P9RyR1F2GbSTwicnI9HLQOwdbbSx5qsAVQTndB8WGEfTz6Hqbls8iaGJicK5ricodTau1g/640?wx_fmt=png&from=appmsg)

黑产“同名贷”招募广告

该黑产表示，主要做的是企业商户贷模式，“同名贷”**操作城市主要在河南省郑州市及广东省某地区**，操作方可以给目标客户使用同名者名下的营业执照去申请线上**商户贷**，这种商户贷主要为套用他人的企业信息，因此并不需要给企业刷流水数据也不需要花时间去养护这个企业。

**四、威胁猎人金融贷款反欺诈服务**

“同名贷”涉及金融机构用户信息泄漏，接受“同名贷”的客户往往**还款意愿和能力都比较低****，贷后逾期风险极高**，最后只能是放款的金融机构承担风险。

威胁猎人聚焦金融黑灰产攻防对抗领域，通过覆盖各类情报渠道源，主动获取大量信贷黑产/黑中介数据，基于欺诈特征分析模型自动化提取目标欺诈群体特征，同时结合数字风险应急响应中心（DRRC）专家的深入分析，为金融机构构建从**最新欺诈风险感知、业务/风控策略指引、到恶意贷款群体定位**的信贷反欺诈闭环。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFwIxFFMgT6P9RyR1F2GbSTbmWfsdC2eBUj0cICiamdiciaezXuUqKIkav2ruRW5ib9OLNSB5QexZoqQA/640?wx_fmt=png&from=appmsg)

***4.1*****及时感知并预警最新信贷欺诈风险**

威胁猎人全面监测金融机构的信贷业务以及各业务环节，信贷欺诈情报专家针对全网信贷风险线索进行主动运营，**及时感知黑产/中介的最新的欺诈风险，包含欺诈手法、欺诈场景等，如涉及房产信用/企业/车/现金/装修/消费贷/美容贷等贷款业务的欺诈风险监测**。

***4.2*****结合群体画像提供业务风控应对策略**

威胁猎人信贷欺诈情报团队深入不同的信贷欺诈场景，以攻击者的视角分析并复现欺诈全流程，包括为金融机构提供指定作弊环节的手法分析，如**获客手法、包装手段、业务操作流程**等，通过不同场景分析报告为金融机构建立欺诈人群的业务行为特征等，为风控策略提供可解释的依据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFwIxFFMgT6P9RyR1F2GbSTADttGWWnFHEhf5Qhp0Zeen4vbqDFAmNg5RR8orvRWMAR9XUhLBSRww/640?wx_fmt=png&from=appmsg)

***3.3*****基于有效标签等数据定位恶意欺诈人群**

基于对信贷欺诈产业链的持续监测及关联分析，威胁猎人可获取大量有效欺诈团伙的群体特征信息，可帮助金融机构在大数据模型等安全检测措施的基础上，基于恶意特征标签进行关联分析，精准定位欺诈人群。

**金融贷款欺诈相关报告**

**1.**[【黑产大数据】汽车贷款欺诈产业链解构](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247498178&idx=1&sn=cea1e2823de9287b8abf9112aa7e373e&chksm=eb12dff9dc6556efdca100fbc186e08f9b803504596bbc9908bc254b1512d9e0ba6350d63136&scene=21#wechat_redirect)

**2.**[威胁猎人发布《信贷欺诈虚假流水研究报告》](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247497917&idx=1&sn=2b5feeb429711a453088abc3325d47c9&chksm=eb12de86dc6557903c11679e11fd0cfd748973a5ae07aeb8e6d8f0d7f22295b65d14d95f7018&scene=21#wechat_redirect)

**3.**[2024年上半年信贷欺诈风险态势报告](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247497661&idx=1&sn=87078c84009dc76cc9df8ff496add874&chksm=eb12d186dc6558909bf949d0326deb0fd7253a2350926ddf5520a1ae52bc4499d144142c6447&scene=21#wechat_redirect)

**4.**[【黑产大数据】金融欺诈中的亡命之徒](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247497256&idx=1&sn=4e3b94429e5b3d485cfbb8894219da01&chksm=eb12d013dc6559059dec88dd1743b92d7614e27f374dd6650d305975efa3427bf7c64de6bfcb&scene=21#wechat_redirect)

**5.** [金融欺诈手段持续升级，威胁猎人信贷反欺诈产品助力识别金融欺诈风险](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247497706&idx=1&sn=f543aa6cf3aee8ffe27c94230977c812&chksm=eb12d1d1dc6558c7908815bc8ed8d1b7d8b13e0dd3bcd13c40ff0ef0054bab9a1eb99e559124&scene=21#wechat_redirect)

**更多金融信贷欺诈风险**

**请与威胁猎人联系**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFwIxFFMgT6P9RyR1F2GbST3amQaGzhNAIYudhkfVpLrwzFqM6W3Clu1UdCGxVyiaicKHViaDUiaXVnuQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGDp3b1qusRgNYCaq1lycmp28Q0cv0o7PkrKW7vib649ZeWmvKLOeORSibaKichArtBFCF8e1LPpxYZw/0?wx_fmt=png)

威胁猎人Threat Hunter

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGDp3b1qusRgNYCaq1lycmp28Q0cv0o7PkrKW7vib649ZeWmvKLOeORSibaKichArtBFCF8e1LPpxYZw/0?wx_fmt=png)

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