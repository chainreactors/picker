---
title: 【安全圈】数据泄露蝴蝶效应！外卖平台惨遭黑手
url: https://mp.weixin.qq.com/s/bcUdDBcrYQt_xs0f0c7BVQ
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:23:05.533596
---

# 【安全圈】数据泄露蝴蝶效应！外卖平台惨遭黑手

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaCsB1l4EmPicJP43icFBaRAOFMibWD5qoEYiceozibXumUxoP9pdQso0vnUBWdtdjtpKqibsCwPiaKuJib0g/0?wx_fmt=jpeg)

# 【安全圈】数据泄露蝴蝶效应！外卖平台惨遭黑手

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

数据泄露

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaCsB1l4EmPicJP43icFBaRAOKUNNiap7LibicUlPNFmF8hjJSJJ1dMjwOpJeTqeYVpdvDIWLiaiaOiaUh8NA/640?wx_fmt=png&from=appmsg)

食品配送平台Grubhub确认在黑客入侵后发生了数据泄露事件，消息人士告诉BleepingComputer，该公司目前正面临高价勒索。

“近期，我们获悉有未经授权的个人从Grubhub某些系统下载了数据”，Grubhub告诉BleepingComputer。“我们迅速展开调查，阻止了该活动，并正采取措施进一步加强自身的安全防护体系。本次事件未涉及财务信息、订单记录等敏感数据。”

Grubhub拒绝回应关于此次泄露事件的任何进一步问题，包括事件发生时间、是否涉及客户数据、或是否遭到勒索。不过该公司证实，目前已与第三方网络安全公司展开合作，并已向执法部门报案。

上月，Grubhub也曾卷入从其b.grubhub.com子域名发送的一波诈骗邮件，邮件以 “比特币投资可获十倍回报”为诱饵推广加密货币骗局。

当时Grubhub曾表示已控制住事态，并采取措施防止未授权邮件的再次发送，但同样拒绝就该诈骗事件的更多细节作出回应。目前暂无法确认这两起事件是否存在关联。

### ****黑客勒索施压****

尽管 Grubhub 拒绝透露更多细节，但多个消息来源已告诉BleepingComputer，此次事件的幕后黑手是网络犯罪团伙 ShinyHunters，该团伙正以此对 Grubhub 实施勒索。

据消息人士透露，威胁行为者要求支付比特币赎金，否则就将公开两份数据：一份是 2025 年 2 月该公司发生的 Salesforce 系统数据泄露事件中被盗取的历史数据，另一份则是本次新泄露的 Zendesk 平台数据。Zendesk是Grubhub的线上客服聊天平台，该平台主要用于处理订单咨询、账户问题及账单相关服务。

### 攻击路径

目前此次数据泄露的具体时间仍不明确，但BleepingComputer透露，黑客利用了近期 Salesloft Drift 数据失窃事件中被盗取的机密信息和登录凭证实施了本次攻击。

2025 年 8 月 8 日至 18 日期间，黑客利用窃取的 Salesloft 公司 Salesforce 集成功能 OAuth 令牌，发起了一轮大规模数据窃取行动。

Mandiant的报告显示，被窃取的数据随后被用来收集凭证和密钥，以对其他平台进行后续攻击。

“GTIG观察到UNC6395以敏感凭证为目标，例如亚马逊网络服务访问密钥、密码和Snowflake相关的访问令牌，”谷歌报告称。

谷歌方面指出：“谷歌威胁情报团队观察到，黑客组织 UNC6395正紧盯各类高敏感凭证信息，包括亚马逊云服务访问密钥、各类密码，以及雪花云数据平台相关的访问令牌。”

ShinyHunters当时声称是此次泄露事件的幕后黑手，表示他们从760家公司的“账户”、“联系人”、“案例”、“商机”和“用户”Salesforce对象表中窃取了约15亿条数据记录。

威胁行为者滥用先前窃取的Salesforce数据来实施后续攻击，所有受到Salesloft Drift数据泄露事件波及的企业，若尚未更换相关访问令牌及机密信息，应立即完成更新操作。

***END***

阅读推荐

[【安全圈】株洲查处一起非法架设GOIP设备案件，2人被抓](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073727&idx=1&sn=f7fee0bb4647564f8820ccbca505f204&scene=21#wechat_redirect)

[【安全圈】微软Copilot曝一键式漏洞：攻击者可悄无声息窃取敏感数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073727&idx=2&sn=e0c8016ed9626a7cec7c2b600f592b4d&scene=21#wechat_redirect)

[【安全圈】Apache Struts 2曝高危漏洞：攻击者可窃取敏感数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073727&idx=3&sn=4e4471fde2273c957d656e6532c405b0&scene=21#wechat_redirect)

[【安全圈】伪装慈善网站钓鱼！乌克兰国防军遭遇 PLUGGYAPE 网络攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073727&idx=4&sn=3565d9dfc911b8d73f40e2f36bb5b189&scene=21#wechat_redirect)

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