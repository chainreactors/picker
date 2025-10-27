---
title: 微软：云服务大规模宕机因DDoS“防卫过当”
url: https://mp.weixin.qq.com/s?__biz=MzI2MzA3OTgxOA==&mid=2657165590&idx=1&sn=c7300daa813f95b0efcdfffb42def665&chksm=f1d4d3f3c6a35ae5e011e9a390d89f5ddd9327f94f6f9c4ad2b13a0dc2680a18bc1e01b7fca7&scene=58&subscene=0#rd
source: 暗影安全
date: 2024-08-02
fetch_date: 2025-10-06T18:03:17.462825
---

# 微软：云服务大规模宕机因DDoS“防卫过当”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PrTu58FA79ZMYWImAfWB3X7p811VBWkUPfcApVialZicviabHSvUvqzsVzWSh3hBbOH9PPukfmcg7etdJLbpXdhkg/0?wx_fmt=jpeg)

# 微软：云服务大规模宕机因DDoS“防卫过当”

暗影安全

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvY05ia3lwufEupm417vRQN75zoT41nhP5IsbckibITD8l5gouVPYibSGHdNnkxR8l4I5dF2xrY9wGRGg/640?wx_fmt=png&from=appmsg)

**杀毒软件导致全球蓝屏，DDoS防护导致云服务宕机，微软这家全球最大的网络安全公司，正在不断刷新人们对“安全威胁”的认知。**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/INYsicz2qhvY05ia3lwufEupm417vRQN75ZhEm3zVp7IHzSq9Z3iat6IU4foOahKuPTUpxicer2PNtR2ukv9sNhrRg/640?wx_fmt=gif&from=appmsg)

微软本周三晚间宣布，本周二全球范围内多个Microsoft 365和Azure云服务大规模长时间宕机事件的原因，是一次DDoS攻击触发了微软DDoS防护机制的“过激反应”。

此次宕机影响了多个微软服务，包括XBOX、Microsoft Entra、Microsoft 365及Microsoft Purview（包括Intune、Power BI和Power Platform）、Azure应用服务、Azure IoT Central、Azure日志搜索警报、Azure策略以及Azure门户。

**DDoS防护“防卫过当”**

在本周三发布的缓解声明中，微软表示，此次宕机的触发因素是一次DDoS攻击，但尚未明确追溯到特定的威胁行为者。

据安全研究机构CyberKnow透露，本周四凌晨黑客组织SN\_blackmeta在电报频道发布了实施微软DDoS攻击的证据（下图），此外还有其他黑客也参与了针对微软云服务的DDoS攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvY05ia3lwufEupm417vRQN75dciaz8bqegvv2BNhgicateMILlZicrOj5Dibwa0J18dnb9lXPrpiaNWlGAQ/640?wx_fmt=png&from=appmsg)

SN\_blackmeta是类似Anonymous Sudan的亲巴勒斯坦黑客组织，主要攻击目标是支持以色列的美国及其盟国的基础设施和企业，具备攻击微软的能力和动机。一周前，Radware曾发布报告称SN-blackmeta针对中东某金融机构发动了一次为期六天的峰值高达1470万RPS的超大规模DDoS攻击。

但是根据微软本周三的声明，真正导致微软云服务大面积长时间瘫痪的“罪魁祸首”，是微软自身的DDoS防护机制。微软表示：“初步调查表明，DDoS攻击触发了我们的DDoS防护机制，由于我们防御措施（例如故障转移）中的一个错误，不但没有缓解，反而放大了攻击影响。”

此前，微软在宕机事件的缓解声明中表示，该事件是由“意外的使用峰值”导致Azure Front Door（AFD）和Azure内容分发网络（CDN）组件表现低于可接受的阈值，导致间歇性错误、超时和延迟峰值。

微软计划在72小时内发布初步事故评估报告（PIR），并在接下来的两周内发布最终事故评估报告，提供更多细节以及从本周宕机中吸取的教训。

**微软云服务的“内忧外患”**

近一年来，微软的云服务饱受内忧外患的折磨，宕机事件此起彼伏。

7月早些时候，微软声称由于Azure配置更改的原因，成千上万的Microsoft 365客户经历了一次大范围的宕机。

7月中旬，CrowdStrike错误更新导致的全球850万台Windows设备遭遇蓝屏死机，被称为史上最大规模系统崩溃事件。微软云服务在该事件中也未能幸免，微软位于美国中部的Azure区域数据中心首先受到冲击，导致包括Microsoft 365在内的多项服务无法正常使用，影响范围从Office应用扩展至Xbox服务。

此前，2023年6月微软曾确认遭受了代号Anonymous Sudan（又名Storm-1359）的黑客组织发动的第七层DDoS攻击，使其Azure、Outlook和OneDrive门户无法访问，该黑客组织被认为与俄罗斯有联系（编者：该组织的意识形态和行为模式与此次宣称对微软DDoS攻击负责的SN\_blackmeta高度相似）。

2022年7月和2023年1月，Microsoft 365服务也分别因企业配置服务（ECS）部署故障和广域网IP变更而受到重大影响。

参考链接：

https://azure.status.microsoft/en-us/status/history/#incident-history-collapse-KTY1-HW8

https://www.radware.com/security/threat-advisories-and-attack-reports/six-day-web-ddos-attack-campaign/

文章转载来源：GoUpSec，如有侵权，请联系我们，我们会及时删除

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PrTu58FA79arIQGU74rJvbDtBoicQlQ8rMIzfax1Ol2RY5YnbsN82PLkvicB9FLHxFibrF5k7x2N7VXicectIVucibg/0?wx_fmt=png)

暗影安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PrTu58FA79arIQGU74rJvbDtBoicQlQ8rMIzfax1Ol2RY5YnbsN82PLkvicB9FLHxFibrF5k7x2N7VXicectIVucibg/0?wx_fmt=png)

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