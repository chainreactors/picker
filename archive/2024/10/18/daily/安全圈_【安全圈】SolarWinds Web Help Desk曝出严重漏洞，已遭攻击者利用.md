---
title: 【安全圈】SolarWinds Web Help Desk曝出严重漏洞，已遭攻击者利用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065297&idx=3&sn=763d27a5148619b21d8a21de71663c4c&chksm=f36e6251c419eb47fce614b9c2353cfdc1ca30e5dc890827e6e25466db25669bd30f6e9ca3b3&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-18
fetch_date: 2025-10-06T18:53:13.309696
---

# 【安全圈】SolarWinds Web Help Desk曝出严重漏洞，已遭攻击者利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt453MvE78MlocZJMuUq241icxlLVBmciczibaQJV4GYyoQL8p0hHb2kuQvw/0?wx_fmt=jpeg)

# 【安全圈】SolarWinds Web Help Desk曝出严重漏洞，已遭攻击者利用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

安全漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgibQUvRxkxymN5Yz2wmhU2AyfYWK2NK2VW2sEqZmBGwNwp53buK1rtv2Br94H1GicNKaTqtTtaia0mg/640?wx_fmt=jpeg&from=appmsg)

近日，CISA 在其 “已知漏洞”（KEV）目录中增加了三个漏洞，其中一个是 SolarWinds Web Help Desk (WHD) 中的关键硬编码凭据漏洞，供应商已于 2024 年 8 月底修复了该漏洞。

SolarWinds Web Help Desk 是一款 IT 服务台套件，全球有 30 万客户在使用，其中包括政府机构、大型企业和医疗机构。

SolarWinds 漏洞被追踪为 CVE-2024-28987，是由硬编码凭据（用户名为 “helpdeskIntegrationUser”，密码为 “dev-C4F8025E7”）引起的。这些凭证一旦被未经验证的远端攻击者利用可能会存取 WHD 端点，并不受限制地存取或修改资料。

Horizon3.ai 研究员 Zach Hanley 最早发现了该漏洞并随即报告给了 SolarWinds ，四天后该套件发布了热修复程序，并敦促系统管理员迁移到 WHD 12.8.3 Hotfix 2 或更高版本。

CISA 现已将该漏洞添加到 KEV 中，表明该漏洞正被用于野外攻击。

美国政府机构没有透露有关恶意活动的详细信息，并将勒索软件的利用状态设置为未知。预计美国联邦机构和政府组织将在 2024 年 11 月 5 日前更新到安全版本或停止使用该产品。

鉴于 CVE-2024-28987 正在被利用，建议系统管理员采取适当措施，在设定的最后期限之前确保 WDH 端点的安全。

另外两个漏洞与 Windows 和 Mozilla Firefox 有关，已知这两个漏洞都已在攻击中被利用。CISA 还要求联邦机构在 11 月 5 日前修补这些漏洞。

Windows 漏洞是一个内核 TOCTOU 竞赛条件，被追踪为 CVE-2024-30088，趋势科技发现该漏洞被主动利用。该网络安全公司将这一恶意活动归咎于 OilRig (APT34)，他们利用该漏洞将被入侵设备的权限提升到 SYSTEM 级别。

微软在最新发布的补丁包中解决了该漏洞，但目前还不清楚何时开始主动利用该漏洞。

Mozilla Firefox CVE-2024-9680 漏洞最早是被 ESET 研究员 Damien Schaeffer 于 2024 年 10 月 8 日发现，25 小时后该漏洞得以修复。

Mozilla 表示，ESET 提供的攻击链可以通过 Firefox 中 CSS 动画时间轴的渲染在用户设备上远程执行代码。

目前， ESET 仍在分析他们观察到的攻击活动，其中一位发言人称恶意活动似乎来自俄罗斯，很可能用于间谍活动。

参考来源：SolarWinds Web Help Desk flaw is now exploited in attacks (bleepingcomputer.com)

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt4wSsA1lCMJj8kpJR49clItiaZ6via2d4EQMQK0iaANicOS3lDagS6eZIAxw/640?wx_fmt=png)[【安全圈】腾讯云加强短信群发资质审核 需提交手持身份证拍照并按手印签署承诺书](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065278&idx=1&sn=b0c3e5421c3e014a3f925bc996b40b1e&chksm=f36e61bec419e8a8f9c79604909d3fcc614130a786bd2bd57e062b137a511429ba7b54b66505&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt43aXTBzRm2VyWol82jR5d3vYo6xzjHXrEkgu1ZT0jaEAORfVz8LNOgQ/640?wx_fmt=jpeg)[【安全圈】朝鲜黑客利用FASTCash恶意软件从多个国家ATM机中窃取资金](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065278&idx=2&sn=7eb9ab34e56b92451d197500dbbb7e2f&chksm=f36e61bec419e8a8410d2f446b260c1a7cc5d4421d20c19de7419bf2fd43c4ae8b617b059452&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt4YAToqxIZ5094NNvXncCfv5gYnBMDs9ia9Ardp5DX1r4fCKwd654rzAg/640?wx_fmt=jpeg)[【安全圈】可绕过安全防护！EDR Silencer红队工具遭黑客利用](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065278&idx=3&sn=bc5b1bf29ad416c8769d53bc5ad0a5a1&chksm=f36e61bec419e8a8507b9227e71141e2c883e704928a1d03fbf4d674f0462819da89fa7f1db7&scene=21#wechat_redirect)

[【安全圈】亚马逊宣布全面转向Passkey无密码登录 目前已有超过1.75亿用户使用通行密钥](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065278&idx=4&sn=0f4503b103b4040ca4305cfd95ba176c&chksm=f36e61bec419e8a8e9c04417233b5c37bae07dbf1583c88a4e7ca2c8a6ece24f7053b98ba981&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt4hHLCuf7R0qrgTpjPosbYY8NNPrmXia79zIrpnGR9tqjRZZLDpdJiaecw/640?wx_fmt=png) [【安全圈】亚马逊宣布全面转向Passkey无密码登录 目前已有超过1.75亿用户使用通行密钥](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065278&idx=4&sn=0f4503b103b4040ca4305cfd95ba176c&chksm=f36e61bec419e8a8e9c04417233b5c37bae07dbf1583c88a4e7ca2c8a6ece24f7053b98ba981&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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