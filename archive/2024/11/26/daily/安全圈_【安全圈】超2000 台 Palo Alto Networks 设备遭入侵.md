---
title: 【安全圈】超2000 台 Palo Alto Networks 设备遭入侵
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066218&idx=4&sn=8b68cb431919cf30facf1ad47ba67cfe&chksm=f36e7deac419f4fc3367b395a9f8c389115bbb268e13e5c20043a80e6bd609114bc592566e48&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-26
fetch_date: 2025-10-06T19:20:42.844091
---

# 【安全圈】超2000 台 Palo Alto Networks 设备遭入侵

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj1onmGQXCMYucl4PTjFia23RHSd5XymleMBsAO2vQ2FcibNZcPEyOSMgSMfRst7kmwcmiaeOc2qJx1g/0?wx_fmt=jpeg)

# 【安全圈】超2000 台 Palo Alto Networks 设备遭入侵

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

据相关结果显示，大约有2000台Palo Alto Networks设备在一场利用新披露的安全漏洞的活动中被入侵，这些漏洞正在野外受到积极利用。根据Shadowserver Foundation提供的统计数据，大多数感染报告来自美国（554例）和印度（461例），其次是泰国（80例）、墨西哥（48例）、印度尼西亚（43例）、土耳其（41例）、英国（39例）、秘鲁（36例）和南非（35例）。Censys本周早些时候透露，他们已识别出13,324个公开暴露的下一代防火墙（NGFW）管理界面，其中34%的暴露位于美国。需要注意的是，并非所有暴露的主机都必然会受攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj1onmGQXCMYucl4PTjFia239eA3Ur3ukfyHwt8xxBvNyfgPWSzbugEOsCvnHoMQOOeX9Viaxl80CibQ/640?wx_fmt=jpeg&from=appmsg)

有问题的缺陷CVE-2024-0012（CVSS 评分：9.3）和 CVE-2024-9474（CVSS 评分：6.9）是身份验证绕过和权限提升的组合，可能允许不良行为者执行恶意操作，包括修改配置和执行任意代码。

## 何为更有效的应对措施

Palo Alto Networks 表示正在以 Operation Lunar Peek 的名义跟踪最初对漏洞的零日漏洞利用，他们正在被武器化以实现命令执行并将恶意软件（例如基于 PHP 的 Web shell）投放到被黑客入侵的防火墙上。

网络安全供应商还说，针对安全漏洞的网络攻击可能会在将它们组合的漏洞利用可用后升级。为此，以中等到高度的置信度评估链接 CVE-2024-0012 和 CVE-2024-9474 的功能性漏洞是否公开可用，这将允许更广泛的威胁活动。此外，他们已经观察到手动和自动扫描活动，用户需尽快应用最新的修复程序，并根据推荐的最佳实践部署指南安全访问管理界面。尤其包括限制仅受信任的内部 IP 地址的访问，以防止来自 Internet 的外部访问。

## 用于丢弃Sliver 和Crypto 矿工的PAN 缺陷

Palo Alto Networks 最新披露，受感染设备的实际数量小于报告的数量，因为后者仅显示暴露于Internet 管理界面的防火墙。除了与受影响的客户合作外，其大多数客户已经遵循行业最佳实践并保护其管理界面，只有不到 0.5% 的防火墙具有暴露于互联网的界面。

云安全公司 Wiz透露，在一周前发布有效的概念验证POC 漏洞后，在野外的漏洞利用尝试“急剧增加”，并且观察到威胁行为者将漏洞武器化，以投放 Web shell、Sliver 植入物和加密矿工。

参考资料：https://thehackernews.com/2024/11/warning-over-2000-palo-alto-networks.html

***END***

阅读推荐

[【安全圈】太空技术巨头 Maxar 证实攻击者获取了员工数据](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066203&idx=1&sn=81e535202f431485c12dac88cf705ffe&chksm=f36e7ddbc419f4cdfa6b93222991880723ead5b1224f5aea3c430d89ee2ad3f9ea5556553fc9&scene=21#wechat_redirect)

[【安全圈】微软公司推出 “Windows 恢复能力计划”](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066203&idx=2&sn=6d88527a3838dd59d8bbccb332540518&chksm=f36e7ddbc419f4cd51a855d822237f84592f66ad951174261234f7641e5c6bb1e6cd2cfcacca&scene=21#wechat_redirect)

[【安全圈】苹果解决了两个被积极利用的零日漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066203&idx=3&sn=98b7c0046c725ff8299a89a706c8ee43&chksm=f36e7ddbc419f4cdfd1a5b1325eeaa6a76fad3e86c3a04d39a3c93255a412bb3e8ee77745d9d&scene=21#wechat_redirect)

[【安全圈】微软已通过更新修复Windows 10安装商店应用时出现发生错误无法安装问题](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066203&idx=4&sn=fa5c5885a0aa428e589410762dd813ac&chksm=f36e7ddbc419f4cdd12380c085a00117007aeacb6e8ac0816c71f80f4a0aa82a15a7f149aff5&scene=21#wechat_redirect)

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

阅读原文

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