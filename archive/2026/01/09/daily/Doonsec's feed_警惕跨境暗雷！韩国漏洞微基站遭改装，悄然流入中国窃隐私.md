---
title: 警惕跨境暗雷！韩国漏洞微基站遭改装，悄然流入中国窃隐私
url: https://mp.weixin.qq.com/s/XKaWRWSjITR_gAmEicCXNg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:25:52.066998
---

# 警惕跨境暗雷！韩国漏洞微基站遭改装，悄然流入中国窃隐私

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7shpSHvVBqARf7QRyN0ia4icjgzOEcibvksfzhicianXYWiajdYjWp6pibtIbg/0?wx_fmt=jpeg)

# 警惕跨境暗雷！韩国漏洞微基站遭改装，悄然流入中国窃隐私

易云安全应急响应中心

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7iaaIjLH8CyicX6qHicphlNKE2svC1PGjVibOZ7QpG9samds0Tufsq8pNlw/640?wx_fmt=png&from=appmsg)

**点击蓝字 | 关注我们**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7Pt6RhagePc0KCd0vNBOhpQicqCt2Guck1mGOTibIQewNTb2IIP4Y4wsw/640?wx_fmt=png&from=appmsg)

韩国科学技术信息通信部近日披露了一起波及全国的重大网络安全丑闻：韩国电信（KT）部署的数千个家用微基站（Femtocell）因存在极其低级的安全缺陷，遭到犯罪团伙的大规模克隆与改装。这起不仅涉及数千万元的小额支付诈骗，更牵动着跨境敏感数据流向的恶性案件，揭示了电信基础设施在供应链安全与认证机制上的脆弱现状。

随着韩国科学技术信息通信部（MSIT）一份长达数页的调查报告出炉，一场潜伏在韩国电信基础设施深处的“溃疡”终于被公之于众。该国主要运营商韩国电信（KT）被证实部署了数千台存在严重安全隐患的微基站设备，导致大量用户通信内容被窃听，并引发了涉及跨境犯罪的复杂连锁反应。

**裸奔微基站变身伪基站**

微基站通常被电信运营商用于改善室内或移动信号盲区的覆盖，通过有线宽带连接回传至运营商核心网。然而，韩国电信部署的这批设备在安全设计上几乎处于“不设防”状态。

根据韩国信息安全专家、IEEE Fellow金容大（Yongdae Kim）教授的深度分析，这些微基站存在多项致命弱点：首先，数千台设备竟然共用同一个设备认证证书。这意味着一旦其中一台设备被攻破，整个微基站网络的信任体系将全面瓦解。其次，这些设备未设置Root密码，所有敏感密钥均以明文形式存储在本地，且默认开启了SSH远程访问权限。

攻击者可以像进入无人之境一般，通过网络获取这些明文证书，随后克隆出无数个“合法”的虚假微基站。由于该证书的有效期长达十年，这意味着非法设备可以在极长的时间跨度内持续接入核心网，而不会被系统拦截。

**从小额支付诈骗到深层监听**

这起安全危机最初因钱财流向异常而露出马脚。今年9月，韩国电信在审计用户账单时，发现368名用户的账户出现了异常的小额支付。调查显示，犯罪团伙利用克隆的微基站拦截了用户的验证短信，从而盗取了总计约1.69亿韩元（约合12.5万美元）的数字内容服务费。

然而，金容大教授认为，这笔数额并不足以匹配犯罪团伙所投入的技术成本。他指出，由于虚假微基站具有强制接入特性，受害者手机会自动连接到信号更强的伪造基站，从而使攻击者能够实时读取短信、获取通话记录以及手机位置信息。

“大规模的数据采集才是其核心目的，小额支付诈骗只是因为某个成员的贪婪而让整个行动提前曝光。”金容大表示，如果不是因为这笔“微不足道”的诈骗金，这套监听网络可能仍会在地下隐秘运行多年。

**跨境黑产：非法改装设备流向中国**

随着韩国警方的介入，案件背后的跨国犯罪链条逐渐清晰。警方在调查中发现，目前已逮捕的13名犯罪嫌疑人分工明确，不仅在韩国仁川机场等公共场所进行“战争驾驶”（War-driving）式的非法车载监听，还涉及精密的技术改装。

最令安全界警惕的是，警方在抓捕现场拦截了一批正准备出口至中国的改装硬件。据悉，这些设备已经过技术处理，集成了克隆的证书与破解的固件。犯罪分子试图将这些具有“合法外衣”的韩国电信设备运往中国，其潜在用途可能涉及跨境电信诈骗、敏感信息窃取或规避监管的秘密通信。

目前的调查结果显示，部分被克隆的密钥竟然源自2019年部署在韩国军事基地的一台基站设备，该设备于2020年报失。此外，警方怀疑该团伙可能通过2022年发生的BPFDoor恶意软件攻击获得了部分运营商核心网的技术参数，那次攻击曾导致韩国电信数据泄露长达三年之久。

**安全警示：电信基础设施的结构性风险**

目前，韩国政府已要求韩国电信允许受影响用户无条件解除合同。然而，此案引发的行业反思远未结束。

从供应链安全的角度来看，微基站作为电信网络的“末梢神经”，其安全性长期被低估。同一证书的滥用、明文密钥的存储以及缺乏多因素验证的接入机制，共同酿成了这起长达数年的安全事故。

*安全专家TUNNY指出，随着这一批带有“合法认证”的改装设备流向海外，其安全威胁已从单一国家的电信欺诈演变为复杂的跨境网络安全挑战，针对关键基础设施的攻击正在向“低成本、高隐蔽”的方向演进，运营商必须对其部署的所有终端设备实施零信任架构，而非仅仅依赖十年有效的静态证书。*

目前，此案的幕后主使仍然在逃，韩国政府已通过国际刑警组织发布红色通缉令。对于中国及周边国家的安全机构而言，防范这类来自邻国、带有合法电信特征的“改装黑产设备”入境，正成为当下技术防范的新课题。

**文章来源：GoUpSec**

免责声明

本文素材(包括内容、图片)均来自互联网，仅为传递信息之用。如有侵权，请联系我们删除。

**END**

![图片](https://mmbiz.qpic.cn/mmbiz_png/6aVaON9Kibf6qHRdibQTh7Bic33HXRicZowtjiavqOsjjNTNWNtssMJtfSYn6uT1PgnaWWnMlSPevI96XXRdM4tibYqQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**淮安易云科技有限公司**-******网络安全部**

我们致力于保障客户的网络安全，监控事件并采取适当措施，设计和实施安全策略，维护设备和软件，进行漏洞扫描和安全审计,团队协调处理网络攻击、数据泄露等安全事故，并负责安全服务项目实施，包括风险评估、渗透测试、安全扫描、安全加固、应急响应、攻防演练、安全培训等服务，确保客户在网络空间中的安全。

**易云安全应急响应中心**

专业的信息安全团队，给你最安全的保障。定期推送漏洞预警、技术分享文章和网络安全知识，让各位了解学习安全知识，普及安全知识、提高安全意识。

![图片](https://mmbiz.qpic.cn/mmbiz_png/US10Gcd0tQHDte6ZzXiclrYUTCQHiak0k38kaD0O6NSfpyrRicr2rspyQicXCp6I4iagSbNbaKt2IiboYfRyUpnDZrtQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7oAq9B6tbfCpcDvtYfWPlG03Hr87Tsf9j4zaRb1j2ibulJYCgoqtKEXQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gMiabmiaticAtSia0prnfkWIj7vlIkbFPGibN2sUrBbqFSpgHDHhz9s0ic6smsEy0Dae8bnOUPibYNuuj4gwOyqjiac9ow/640?wx_fmt=jpeg&from=appmsg)

**扫码关注**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7mPyXcR4CK7icjm5Clrknfjk8FtgROsooicPv4Fn0j86Y1JSd4HpZCpBg/640?wx_fmt=png&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ74J64EPqEoKhW1SL84NWmdpWnqiafIGB7QfXbI66RRMfg4yxrsyXxM4w/640?wx_fmt=png&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7Zp2MmPiaPx4KBhq65h82Eu6Qra2YJdiawRaHZflNZMxo6hfU7VLjlfzw/640?wx_fmt=png&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7fiarX4RzpFNDFpoEbQuuADrspNGrBrupPjTX4iasHwzuetrWRJZzAuzA/640?wx_fmt=png&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtQNic2Y9ibWKk80qFIHFdG7FjqbiajSPgxjqbTRFvXArqibRHTqKwnW5MFTdpMlh3kVuz7V7452xJ6Z8g/0?wx_fmt=png)

易云安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtQNic2Y9ibWKk80qFIHFdG7FjqbiajSPgxjqbTRFvXArqibRHTqKwnW5MFTdpMlh3kVuz7V7452xJ6Z8g/0?wx_fmt=png)

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