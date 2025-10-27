---
title: 【安全圈】朝鲜 APT 在网络间谍攻击中绕过 DMARC 电子邮件策略
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064597&idx=2&sn=a3278f6d575dc09eb6874e7ec2d6bcdf&chksm=f36e6715c419ee0389ebda2affdd83addfd3cb93eaf29bb92ba15cb0fdb022e3ad9dbf4b2e59&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-23
fetch_date: 2025-10-06T18:24:40.116892
---

# 【安全圈】朝鲜 APT 在网络间谍攻击中绕过 DMARC 电子邮件策略

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgiaaXeNGKfYJo9KNnBhco0DcfMED8IrMRorAFyWWCNcPamT4joEUEGHIxgG14Ncv8btQUoj1WkX6Q/0?wx_fmt=jpeg)

# 【安全圈】朝鲜 APT 在网络间谍攻击中绕过 DMARC 电子邮件策略

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

网络攻击

随着地缘政治紧张局势的加剧，朝鲜网络间谍组织对美国及其盟友组织的网络攻击激增也就不足为奇了。然而，令人不安的是，一个名为 Kimsuky 的高级持续威胁 （APT） 组织通过将防御优势转化为弱点而取得了显著的成功——利用配置不佳的基于域的消息身份验证、报告和一致性 （DMARC） 策略来执行鱼叉式网络钓鱼活动以获得优势。

5 月 2 日 ，美国联邦调查局 （FBI）、国家安全局 （NSA） 和美国国务院的一份公告指出，Kimsuky 作为朝鲜侦察总局 （RGB） 的一个部门，一直在向知名智库、媒体、非营利组织、学术界和其他组织的个人发送欺骗性电子邮件。这些电子邮件是情报活动的一部分，旨在收集有关地缘政治和外交政策计划的信息，特别是与核政策、制裁和涉及朝鲜半岛的其他敏感问题有关的信息。

随着制裁的严厉打击，朝鲜已经发展出强大的网络犯罪能力，为该政权创造流动性。然而，在这种情况下，我们看到 Kimsuky 威胁行为者将他们的重点转移到情报行动上，以受信任方和知名组织持有的大量信息为目标。尽管正在进行的攻击活动具有复杂的地缘政治影响，但有效防御这些攻击从根本上取决于稳健、可操作且正确执行的网络卫生实践。

## DMARC 错误配置太常见了

Kimsuky 正在使用 DMARC 配置不当或缺失的受信任网络来欺骗合法域并冒充受信任的个人和组织。DMARC 协议的创建是为了阻止用户帐户的泄露，并阻止这里正在运作的社会工程类型。

它应该这样工作：DMARC 允许电子邮件收件人通过域名系统 （DNS） 验证电子邮件的来源，确保威胁行为者无法欺骗合法域。DMARC 会检查传入邮件的发件人策略框架 （SPF） 和域名密钥识别邮件 （DKIM） 记录，如果它看起来不合法，则告诉接收邮件服务器下一步该怎么做。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgiaaXeNGKfYJo9KNnBhco0Dr4y9Qha5HnpujmVqzrCskyLV4qQUMEFDdTeRZqbTo7n6Dhz80Xh84w/640?wx_fmt=png&from=appmsg "DMARC.png")

但正如 Kimsuky 的攻击所表明的那样，这只有在正确配置 DMARC 服务的情况下才能奏效。正如 IC3 公告所详述的那样，错误配置太常见了，或者域所有者对策略的定义很糟糕。对于一些组织来说，自我管理的 DMARC 似乎具有成本效益，但它也可能导致重大疏忽，包括增加漏洞、未能注意不断变化的威胁、缺少健全的合规性报告以及产生虚假的安全感。

## 朝鲜的攻击是什么样子的

Kimsuky 的鱼叉式网络钓鱼活动可能从来自看似可靠来源的无害电子邮件开始，在发送带有恶意链接或附件的后续电子邮件之前建立信任。然后，该组织利用成功的入侵手段，通过针对更高价值目标的更可信的鱼叉式网络钓鱼电子邮件升级攻击。

该组织将情报收集活动的重点针对韩国、日本和美国，目标是被认定为各个领域专家的个人。 根据网络安全和基础设施安全局 （CISA） 随后的公告，智库和韩国政府实体也成为目标。

FBI-NSA 公告中的一个真实示例的主题行是：“[邀请] 美国对朝鲜的政策会议”。这条信息似乎来自一所知名大学，开头是：“我希望您和您的家人度过一个美好的假期和一个宁静的季节。我很荣幸邀请您为由 [合法智库] 主办的私人研讨会发表主题演讲，讨论美国对朝鲜的政策。作为进一步的诱惑，该电子邮件还提供 500 美元的演讲者费。

另一封电子邮件的主题是“关于朝鲜的问题”，作者冒充合法媒体的记者要求采访，然后概述了朝鲜的核活动。

在大学示例中，该电子邮件收到了 SPF 和 DKIM 检查的“通过”，这表明攻击者获得了对大学合法电子邮件客户端的访问权限。尽管 DMARC 返回“失败”，因为发件人的电子邮件域与合法来源的 SPF 和 DKIM 记录不同，但组织的 DMARC 策略未设置为采取过滤操作，因此邮件被投递。在第二种情况下，不存在 DMARC 策略，允许攻击者欺骗记者的姓名和新闻机构的电子邮件域。

## 为什么 DMARC 很重要

美国政府的公告为组织保护其数字资产提供了令人信服的理由。Kimsuky 并不是 APT 中唯一一个，更广泛地说，也不是以营利为目的的网络犯罪分子：他们分享了经验教训，并且都越来越擅长针对错误配置和弱点。

保护和正确配置 DMARC 是关键，因为它可以改善组织的网络卫生，并广泛抵御无处不在的威胁，如商业电子邮件泄露和勒索软件电子邮件攻击。

值得注意的是，行业或法规要求可能已经使 DMARC 成为您组织的要求。截至 2024 年 2 月，谷歌和雅虎已要求发送大量电子邮件的组织使用 DMARC，据报道，Microsoft 正计划效仿。此外，PCI DSS 4.0 需要实施 DMARC。根据 BIMI Radar 的数据，自 FBI 5 月 2 日发布公告以来，截至 6 月 17 日，全球 DMARC 的采用率已从 374 万个组织增长到 571 万个组织。

工作中还有一个商业要务。组织必须优先考虑网络卫生，以保护其数字资产、防止数据泄露并防范不断演变的网络安全威胁。DMARC 应该是您组织网络态势的一部分。如果管理得当，它不仅可以确保更好的送达率，提供针对网络钓鱼和商业电子邮件泄露 （BEC） 的保护，并支持部署用于消息识别的品牌指标 （BIMI），还可以帮助关闭打击民族国家间谍活动和网络犯罪的大门。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhAK7Fv8oWpNiaXrhevHW8p6kdV6HyKu4P3iatdHBicGce4lg5vw9qxMJRvnoFwx4Dm5EZAqNNWZC3dQ/640?wx_fmt=jpeg&from=appmsg)[【安全圈】速更新！GitLab发布更新修复CVSS满分漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064581&idx=1&sn=a8d25f47e9142354cddaccee15a9e264&chksm=f36e6705c419ee130f4d3f0e49710c74c10402ee7aa922bcf4c208d71d1956c64caa923497ee&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhWaD223ARVtJuibmk6sDanjyOZS5Kk0TGsv1JzicUqOfHsp2yK3LP3kXUNleGsywC3B2PQsOX1fdYA/640?wx_fmt=jpeg&from=appmsg)[【安全圈】遭受 Medusa 勒索软件攻击，1TB护照、驾驶执照泄露](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064581&idx=2&sn=cc2983b9d05d015a0f637bceb468f01d&chksm=f36e6705c419ee13ca8b24c68f94deeeacf830cf6d2652b28a978286ea96b2e562962312ae52&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgiaaXeNGKfYJo9KNnBhco0DpbEBKQIluVUGMEuBiaVuYxcOEkDyMZOR1cjqDxE2EibDicuN4x1Ib7tjQ/640?wx_fmt=jpeg)[【安全圈】迪士尼宣布弃用 Slack 平台](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064581&idx=3&sn=83152847e2afad70f1324f5da5de3b7a&chksm=f36e6705c419ee139a7eb75252f0506a83e391436f819a10b3ae2739680efe9a3f58c30584c3&scene=21#wechat_redirect)

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