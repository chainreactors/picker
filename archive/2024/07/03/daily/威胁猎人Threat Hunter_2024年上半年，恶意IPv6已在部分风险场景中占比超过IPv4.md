---
title: 2024年上半年，恶意IPv6已在部分风险场景中占比超过IPv4
url: https://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247497366&idx=1&sn=96fba95b4d98dc214ebb1f4b503572c4&chksm=eb12d0addc6559bb83f3ffd8edb9ed3699eedd3e69b5b828f684e276028c971586f651e18740&scene=58&subscene=0#rd
source: 威胁猎人Threat Hunter
date: 2024-07-03
fetch_date: 2025-10-06T17:45:25.314378
---

# 2024年上半年，恶意IPv6已在部分风险场景中占比超过IPv4

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqFia99nQVaVP9Jrzogg1ibJLiaiagKJeDx6bvb0prK2juwpbO6cM5sX6cYql5Py6bQ4YpRKaJo4ew3nHg/0?wx_fmt=jpeg)

# 2024年上半年，恶意IPv6已在部分风险场景中占比超过IPv4

原创

猎人君

威胁猎人Threat Hunter

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/4mAgZtBianqHwB5L4n1SdUaicvcFspoC5LC0sR6QhONHlmxKqJbr50j9XvHibLLDeVM6GzOPt57raMG2kxzAuFfoA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**IPv6将逐渐成为黑产作恶的主流资源**

**随着企业更多业务从IPv4迁移到IPv6，基于IPv4的攻防战场势必会向IPv6转移。**事实上，互联网黑灰产已经开始运用上了IPv6这一底层资源，并凭借IPv6数量庞大的特性，在互联网业务安全攻防中占据了优势地位。

威胁猎人针对已命中风险IP的IPv6和IPv4进一步分析发现，在某些作恶场景中，近两周的风险IPv6数量占总IPv6查询量的比例（2.27%）超过了风险IPv4数量占总IPv4查询量的比例（0.83%），即**IPv6作恶的比例高于IPv4作恶的比例**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqEYGT7d4e4wD6VI8ickAfUsG2H1ojHNHlSy3Q0undEJxaMVGxMFE1R65ibo1HZqISV1chCD9ftreicsw/640?wx_fmt=png&from=appmsg)

注：IPv6作恶比例=风险IPv6数量/IPv6查询总量；IPv4作恶比例=风险IPv4数量/IPv4查询总量

此外，**从整体风险****IP****情况来看，风险****IPv6****的占比也一度超过风险IPv4。**以下是某企业平台某风险场景中近两周风险IPv4和风险IPv6占比：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqEYGT7d4e4wD6VI8ickAfUsGRlUibcn5O2pqVjcsLpDDe2U4nItXfO0tRjt3D78GIYPqwg4uDf0XoNQ/640?wx_fmt=png&from=appmsg)

**IPv6****已逐渐成为黑产作恶的重要资源，**IPv6安全攻防战已开启，但当下企业在IPv6风识别上仍存在很大的挑战。

**当下黑名单检测机制在海量的IPv6面前基本完全失效**

众所周知，IPv6地址空间几乎接近无限，被十分形象地称为可以为全世界的每一粒沙子分配一个地址，这也意味着**黑灰产掌握的IP资源体量将无限扩大**。

威胁猎人对捕获到的IPv6进一步分析，**IPv6地址被黑产重复使用2次及以上的比例不会超过10%** ，同比IPv4地址重复出现的比例可达90%。这种情况下，**当下主流基于黑名单的检测方式在IPv6风险检测上则完全失效**。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqFia99nQVaVP9Jrzogg1ibJLiatdbC77kRhd9gBWWPiaDmrM1ezdI2HZTuW7Sb92wLlBY7XbCtOD6A9dw/640?wx_fmt=jpeg&from=appmsg)

**威胁猎人IPv6风险识别引擎助力企业精准定位IPv6风险**

威胁猎人很早就开始关注到IPv6的相关风险，并逐步启动对其风险识别能力的研究。

威胁猎人通过对IPv6地址分配规律以及大量IPv6黑产数据的分析研究，总结出风险IPv6的行为规则，形成一套精准有效的**IPv6风险识别算法**，可以有效帮助企业**精准检测出业务流量中IPv6流量在活跃时间内的风险值**。

**目前该引擎在多个头部客户的业务场景进行测试，识别准确率可达100%，召回率能达30%-35%。**

某互联网企业提供1000条IPv6纯黑样本，经过风险识别引擎识别出295条高风险IPv6，识别准确率100%，召回率是29.5%，样本流量集中在Top8城市，均在监测的地区范围内。

目前IPv6风险识别引擎还有待继续完善，后续我们会持续跟进对全网黑产使用的IPv6资源地区的覆盖，消除识别算法的盲区，进一步提升检测率，以便更精准、更及时地定位IPv6风险。

如果您的业务中也有发现可疑IPv6

欢迎使用威胁猎人IPv6风险识别引擎

进行**IPv6风险定位**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqFia99nQVaVP9Jrzogg1ibJLiahmZl7fz5tpQuw27axWghWFXibsm8tCzBVItn5u8t8XN73R0fzj2QdWA/640?wx_fmt=png&from=appmsg)

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