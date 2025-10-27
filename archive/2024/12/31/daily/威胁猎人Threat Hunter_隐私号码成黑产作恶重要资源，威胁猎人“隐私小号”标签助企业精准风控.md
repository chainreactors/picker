---
title: 隐私号码成黑产作恶重要资源，威胁猎人“隐私小号”标签助企业精准风控
url: https://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247498346&idx=1&sn=e0ef4a5b3cd70756e993e4e4dc845f87&chksm=eb12dc51dc65554765314a43cc4f0ac6dc1c8150e1b830f78ad2f5d7cb51dc7d7a38b31048b1&scene=58&subscene=0#rd
source: 威胁猎人Threat Hunter
date: 2024-12-31
fetch_date: 2025-10-06T19:41:49.921879
---

# 隐私号码成黑产作恶重要资源，威胁猎人“隐私小号”标签助企业精准风控

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqHhGrIyBOOjYic023dUAldhUmRvnZBe5q3bmYNvKB0lkoFWpudvoSobvoXicvEZJA1Diax6JluzucGdg/0?wx_fmt=jpeg)

# 隐私号码成黑产作恶重要资源，威胁猎人“隐私小号”标签助企业精准风控

原创

猎人君

威胁猎人Threat Hunter

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/4mAgZtBianqHwB5L4n1SdUaicvcFspoC5LC0sR6QhONHlmxKqJbr50j9XvHibLLDeVM6GzOPt57raMG2kxzAuFfoA/640?wx_fmt=gif)

随着人们对个人隐私的重视程度不断提高，对通信隐私的需求也日益增长，同时，相关法规政策对隐私保护的要求越来越严格，“隐私号”应运而生。

**“隐私号”**即隐私保护号码，又称虚拟号、隐私中间号、隐私安全号等，**是一种通过技术手段生成的临时、随机且加密的号码**，主要是为了解决在**外卖、快递、网约车、金融、医疗等服务行业**客服场景中，**隐藏用户和服务提供人员之间交换真实号码而导致的隐私泄露或滥用问题**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqHhGrIyBOOjYic023dUAldhUtNBftHBcsf52RYialjWL1OibxDNSot3yJxVPicw3Mds4VlicqoHdzCkbGw/640?wx_fmt=png&from=appmsg)

图源：百度百科

**正常情况下，这些号码不会出现在普通的用户使用环境中，如平台注册、参与活动等。**

然而，威胁猎人近年来陆续发现，**不少黑灰产开始利用隐私号进行营销欺诈**，但**隐私号码数量庞大，且一些号段分布特征、在网状态等跟正常号码分布无差异**，一直以来是很多企业风控的难点。

本文基于威胁猎人对隐私号服务的研究，客观呈现被黑产恶意利用的隐私号的基本情况、作恶方法、作恶情况等，为企业的恶意隐私号风控策略提供参考。

**隐私号码获取便利**

**多家云厂商均有提供服务**

**隐私号服务**是基于基础运营商公共电话网（PSTN）提供的服务，企业在不新增SIM卡的情况下，利用隐私号服务实现临时号码中转呼叫，既能享受优质的通话和短信等服务，又能隐藏真实号码，保护个人及企业数据安全。**目前主要应用场景为网约出行、物流、外卖、中介客户、O2O服务等**。

**基础运营商较少直接对外提供隐私号服务，更多是通过代理商对企业提供服务**，目前各大云服务厂商均有相关产品提供：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqHhGrIyBOOjYic023dUAldhU58BD1TGIknGBgFynyEyhxgmlQxQKRHGHQ23BibsXZVhelVLUFCJw0ZQ/640?wx_fmt=png&from=appmsg)

“隐私号服务”是面向企业的服务，一般不支持个人购买或使用。威胁猎人情报人员调研发现，**已经有接码平台可提供隐私号给黑灰产使用，而接码平台则是通过伪造企业身份向云厂商申请“隐私保护号码”服务，进而大量“开卡”**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqHhGrIyBOOjYic023dUAldhUPtty5u2m3qMWXXic62T49icIDDxPUG09iamd3XSeDSibjCO2xyY5ib6RHhg/640?wx_fmt=png&from=appmsg)

威胁猎人捕获到一个专供“隐私保护”的接码平台，该平台使用黑产200余人，平台资金高达100万，截至目前从该平台捕获到隐私号码62300余例。

**隐私号作恶隐蔽性强，风控难度大**

威胁猎人情报人员针对近期捕获的一起营销欺诈事件流量进行分析，基于威胁猎人风险手机号算法以及溯源技术，**发现有10%的作恶账号是隐私号码，约23万个**。

从号码隶属运营商、号段、在网情况等维度进一步分析，这23万余个号码隶属于基础运营商，**号码归属地分布在全国各地的大中型城市，如北京、深圳、郑州、福州等地，混杂于正常号码的号段中**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqHhGrIyBOOjYic023dUAldhU1w8x8bngKzjmlTko7I3WlH3l0miaSS3ibhibgTJQoejDdricLOmam8rxYg/640?wx_fmt=png&from=appmsg)

同时，从号码在网状态和在网时长分析，**这些隐私号的在网状态显示“正常在网”，在网时长基本是一年以上，和普通手机号相仿**。

此外，结合第一部分提到，隐私号是面向企业的服务，不支持个人购买，**实名信息并非实际的真人，而是企业或运营商，所以很难定位到具体作恶的黑灰产人员**。

**威胁猎人推出“隐私小号”风险标签**

**协助企业快速风控隐私号作恶行为**

黑产滥用“隐私保护号码”逐渐成趋势，厂商需要及时了解其作恶流程和细节，依托全网多渠道监测黑卡情报数据，从“被动防范”转向“主动防御”。

**威胁猎人风险手机号画像产品**已覆盖隐私保护号码相关黑产平台，掌握隐私号相关风险特征，推出“**隐私小号**”风险标签，风险等级为risk2，协助企业快速识别此类号码。

威胁猎人建议客户结合自身业务场景建立更精准的风控规则进行针对性防御：

**1.** 若少量命中“隐私小号”的号码的流量，可通过标记后放行通过，这是存在一定的可能性为企业用户将之作为“小号”使用，但仍需注意其是否用于爬取数据或恶意引流；

**2.** 若大规模持续命中“隐私小号”的流量，则建议直接拦截。

威胁猎人手机号风险画像产品基于威胁猎人黑灰产情报体系及特有的蜜罐技术，全面分析手机号的行为及属性，对手机号的风险类别进行综合评价，精确赋予手机号对应的风险标签，如猫池卡、拦截卡、隐私小号、账号卡等，辅助企业风控决策，提升企业风控效率。

更多“隐私小号”风险详情

请咨询威胁猎人安全专家

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqHhGrIyBOOjYic023dUAldhU70RU9gVRK1c4DRK6q0kic38SULVrdsOl32DmBuk8N82bjibI4BWPw1Ew/640?wx_fmt=png&from=appmsg)

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