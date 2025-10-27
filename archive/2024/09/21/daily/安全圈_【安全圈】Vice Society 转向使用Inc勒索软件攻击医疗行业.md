---
title: 【安全圈】Vice Society 转向使用Inc勒索软件攻击医疗行业
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064540&idx=4&sn=1d416047980c19c49eceea05617f5a37&chksm=f36e675cc419ee4aa029f875bc3e6d1e5addee2686971bf195423c3957253ccb130d6cf463b5&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-21
fetch_date: 2025-10-06T18:27:42.107457
---

# 【安全圈】Vice Society 转向使用Inc勒索软件攻击医疗行业

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljk1M1TckpYzeyQIHEFbzTQMwYT7FvDBI8TmN6Hv41j4w9tMicHc1MiawU8IqMujcOibynNIMT22HAlw/0?wx_fmt=jpeg)

# 【安全圈】Vice Society 转向使用Inc勒索软件攻击医疗行业

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

勒索软件

Inc勒索软件正在兴起，其中一个知名的威胁行为者最近使用它来针对美国的医疗保健组织。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljk1M1TckpYzeyQIHEFbzTQCatVuDL7vljPVaJYUuoR8mrUAKEwmssPJQDD3UPfv6mMZpULfNcqWw/640?wx_fmt=jpeg&from=appmsg)

Vice Society（微软追踪其为Vanilla Tempest）自2022年7月以来一直活跃。在这段时间里，这个讲俄语的团伙利用了各种家族的勒索软件来辅助其双重勒索攻击，包括BlackCat、Hello Kitty、Quantum Locker、Rhysida、Zeppelin——包括他们自己的变种——以及以其自身命名的程序。

在X平台上的一系列帖子中，微软威胁情报中心(MSTIC)指出了该团伙最新的武器：Inc勒索软件。

MSTIC的高级威胁情报总监Jeremy Dallman表示：“Vanilla Tempest是我们跟踪的最活跃的勒索软件操作者之一。虽然我们已经看到他们针对医疗保健行业有一段时间了，但这里值得注意的变化是他们在利用更大的勒索软件即服务生态系统时使用了Inc勒索软件载荷。”

## Vice Society 进军医疗保健领域

Vice Society涉足多个行业，包括IT和制造业，但它最为人所知的是针对教育和医疗保健部门的活动。

在这方面，它与更广泛的威胁形势是一致的。根据Check Point Research的数据，医疗保健是勒索软件攻击者最常瞄准的行业。显然，其他类型的网络犯罪分子也喜欢这个行业，全球医疗保健机构平均每周遭受2,018次攻击，比去年增加了32%。

Check Point美洲区CISO Cindi Carter警告说，这是合乎逻辑的。除了受制于过时的传统技术和官僚体制之外，“医疗保健组织捕获、创建和分享的数据对于网络犯罪分子来说具有很高的价值。”她说，“你的医疗记录是你除了指纹之外最具标识性的数字信息。”

在最近利用医疗保健领域固有弱点的活动中，Vice Society获得了之前已被Gootloader后门加载器感染的受害者的初始访问权限。然后它部署了工具，包括Supper后门、AnyDesk的远程监控和管理(RMM)解决方案以及MEGA的数据同步工具，后两者都是合法的商业产品。该团体使用远程桌面协议(RDP)在网络中横向移动，并滥用Windows管理规范(WMI)提供程序主机来投放Inc勒索软件。

## Inc 勒索软件的崛起

自去年夏天开始活跃以来，Inc勒索软件即服务(RaaS)运营因其对特别大型组织的入侵而获得了大量头条新闻——其中包括施乐公司和苏格兰国家医疗服务系统(NHS)等。GuidePoint Security的威胁情报顾问Jason Baker表示，它的运作模式符合其野心的范围。

“特别是Inc联盟成员之所以脱颖而出的原因在于，他们在谈判过程中有一种非常结构化的工作方式。没有即兴发挥。没有随口说出的话。刺激和威胁保持在相对最低的程度，”他从第一手经验中回忆道。

“这就像是有人抢劫银行和有人在小巷里抢劫的区别。你可以看出有人对[攻击]进行了思考并且知道自己在做什么，”他说。

正如Dark Reading上个月报道的那样，Inc的恶意软件泄露了关于其数据加密性质和成功的信息。尽管这可能会给防御者在补救和潜在的与联盟成员的谈判中带来优势，Baker警告说现实更为复杂，尤其是在医疗保健方面。

他指出：“如果一个组织知道它可以恢复，并且不需要解密器，那么这会大大减少他们觉得需要支付赎金的感觉。但问题在于现代的双重勒索，尤其是当涉及到敏感的个人健康信息(PHI)或敏感的知识产权时。双重勒索方法之所以能够长期存在是有原因的：它确实在某种程度上克服了即使能够恢复的能力。”

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgFjLgEspOZUQtsh00n9cLHrxgjjfMPXxoqKdfEz3Z9f32fBLYMJaia8HhLGERnG3nHic9dyBqegb1w/640?wx_fmt=jpeg)[【安全圈】黎巴嫩再发生爆炸事件，这次是对讲机](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064524&idx=1&sn=e19e457b99625444d2c6db745d8eecc1&chksm=f36e674cc419ee5af5719eb9602d03de297a482a04198bb5e857862378e7b482579b2e960c2f&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgFjLgEspOZUQtsh00n9cLHia15IAKE7x1svRiaia0jvDslofCEC33ISPgEAO8gqp1Ggs4yMtEYq9dbw/640?wx_fmt=jpeg)[【安全圈】随着欧洲刑警组织关闭加密聊天应用程序 Ghost ，全球犯罪受到打击](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064524&idx=2&sn=5729c92061978d9d5375532e5bb22754&chksm=f36e674cc419ee5a972a7e6b918c08a67651775d0cef25587a4ca85d3a12a36988b6857bd76e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgFjLgEspOZUQtsh00n9cLHCmyEKbw5ek76hVbm5P0icl3AicwvsMGCA2ibqwwiaoyttWCsgPb8LPv68w/640?wx_fmt=jpeg)[【安全圈】建筑行业会计软件Foundation遭受攻击，威胁行为者利用MSSQL漏洞进行入侵](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064524&idx=3&sn=ac02f46258dacbf415152fe2bad17d2e&chksm=f36e674cc419ee5aebd784b2bec5e460e41f1df53702204b3d3abd741b7d28e67b64223ab4db&scene=21#wechat_redirect)

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