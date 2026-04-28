---
title: 【安全圈】超一万台 Zimbra 服务器易受持续 XSS 攻击
url: https://mp.weixin.qq.com/s/Cg_E7vnIRdaK8UyQkwU5JA
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:26:13.387678
---

# 【安全圈】超一万台 Zimbra 服务器易受持续 XSS 攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyETSbaThhBK72HAibzXqFsdAD5ILN4jh9O9QdKtg2SsOzlAnlb5HNxHYBNR7NKFaf1J0Tp3kzCH0wSseKVMvDZiaCK6m72nq7mjg/0?wx_fmt=jpeg)

# 【安全圈】超一万台 Zimbra 服务器易受持续 XSS 攻击

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客攻击

据非营利性安全组织 Shadowserver 称，**超一万台暴露在互联网上的 Zimbra 协作套件（ZCS）实例，因一个跨站脚本（XSS）安全漏洞**，正面临持续攻击风险。

Zimbra 是一款广受欢迎的电子邮件与协作软件套件，全球数亿人在使用，其中包括数百家政府机构和数千家企业。

该漏洞编号为 CVE - 2025 - 48700，影响 ZCS 8.8.15、9.0、10.0 和 10.1 版本。**未经身份验证的攻击者利用此漏洞，可在用户会话中执行任意 JavaScript 代码，进而获取敏感信息。**

2025 年 6 月，Synacor 发布安全补丁修复该漏洞，并警告称，利用 CVE - 2025 - 48700 的攻击无需用户交互，用户在 Zimbra 经典用户界面查看精心制作的恶意电子邮件时，攻击即可触发。

周一，美国网络安全和基础设施安全局（CISA）基于该漏洞已被主动利用的证据，将 CVE - 2025 - 48700 标记为在实际中被滥用的漏洞，并将其添加到已知被利用漏洞（KEV）目录中。

美国网络安全机构还责令联邦政府行政部门（FCEB）在三天内，即 4 月 23 日前，保障其 Zimbra 服务器的安全。

周五，互联网安全监督组织 Shadowserver 也发出警告，超 10500 台暴露在互联网上的 Zimbra 服务器仍未打补丁，其中大部分位于亚洲（3794 台）和欧洲（3793 台）。

虽然 CISA 未公布 CVE - 2025 - 48700 攻击的具体细节，但另一个 XSS 漏洞（编号为 CVE - 2025 - 66376，11 月初修复），自 1 月起被国家级支持的 APT28（又名 “奇幻熊”、“锶”）军事黑客，用于针对乌克兰政府实体的网络钓鱼攻击。

赛克雷特实验室（Seqrite Labs）的安全研究人员将此次网络钓鱼活动代号为 “幽灵邮件行动”（Operation GhostMail）。该活动还针对乌克兰国家水文局（隶属于基础设施部的关键基础设施实体，提供导航、海事和水文支持），当收件人在存在漏洞的 Zimbra 网络邮件会话中打开恶意电子邮件时，就会收到经过混淆的 JavaScript 有效载荷。

赛克雷特实验室当时表示：“该网络钓鱼邮件没有恶意附件、可疑链接或宏。整个攻击链都在一封邮件的 HTML 正文中，没有恶意附件。”

**Zimbra 的漏洞经常在攻击中被利用，近年来已导致数千台易受攻击的电子邮件服务器遭到入侵。**

例如，2023 年 2 月，俄罗斯 “冬季鼬”（Winter Vivern）网络间谍利用另一个反射型 XSS 漏洞，入侵 Zimbra 网络邮件门户，窃取与北约结盟的组织和个人（包括军事人员、政府官员和外交官）收发的电子邮件。

最近，在 2024 年 10 月，美国和英国网络机构警告称，与俄罗斯对外情报局（SVR）有关联的 APT29（又名 “舒适熊”、“午夜暴风雪”）黑客，正在 “大规模” 攻击易受攻击的 Zimbra 服务器，利用的安全漏洞此前已被用于窃取电子邮件账户凭证。

***END***

阅读推荐

[【安全圈】89TB数据灰飞烟灭！北京一科技公司工程师“删库”获刑5年](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076007&idx=1&sn=6a6eff1e09bd7d67b20d20ee06a2fd39&scene=21#wechat_redirect)

[【安全圈】男子利用公安内部系统卖个人信息 非法获利被判刑](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076007&idx=2&sn=09ae1d9ef07438cdb39cedb748421211&scene=21#wechat_redirect)

[【安全圈】装机必备的GPU-Z出事了！曝出严重安全漏洞：黑客可获取系统最高权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076007&idx=3&sn=7b7cd810015615c15d6232964cb06d5f&scene=21#wechat_redirect)

[【安全圈】美国家庭安防巨头 ADT 被黑客勒索，大量客户数据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075996&idx=1&sn=421380f14f3ee130f56c4f1cbcca9e6c&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

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