---
title: Tech时间 |病毒，壳和火绒虚拟沙盒
url: https://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247513997&idx=1&sn=744b805bdb584c936a77f89dbab2129a&chksm=eb7069b2dc07e0a44ced1173d37e0fecb8db23ff6a75b66509b3d97c49cbf7671ba1a3c3d562&scene=58&subscene=0#rd
source: 火绒安全
date: 2023-03-31
fetch_date: 2025-10-04T11:15:46.439946
---

# Tech时间 |病毒，壳和火绒虚拟沙盒

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz619RJbF0eJnGTNOHyzNS2ibuzWIz4uzFTg510wFibeRuTbG1TXO5qQUDJv0cVCUoW0dHRLURceDoZQ/0?wx_fmt=jpeg)

# Tech时间 |病毒，壳和火绒虚拟沙盒

原创

火绒安全实验室

火绒安全

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz619RJbF0eJnGTNOHyzNS2ibcRicka6WAhnh2dwibF8sriadBy86TXtCiaCZVyEQTQlmVb3rvhXroe7tpg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz619RJbF0eJnGTNOHyzNS2ibfxzYfN474eXPZs4NeiautxTbfOB4V8SMvrd7GNuH9xZZB1KtqVpHBLg/640?wx_fmt=jpeg)

为了躲避查杀，计算机病毒会通过某些手段伪装自己。

用自然界生物举个例子：如果寄居蟹躲进一只海螺壳中，仅从表面的“壳”看很难判断它到底是海螺还是寄居蟹。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz619RJbF0eJnGTNOHyzNS2ibEAwHTSmjbNIcuUATJI4fHqibziaiclIH3X4LUj5BQnHo7gV7n7R8pVlBQ/640?wx_fmt=png)

**0****1**

**躲在“壳”里的病毒**

在病毒与安全软件的代码对抗过程中，“壳”一直扮演着重要的角色。“壳”本身无关好坏，软件会使用“加壳”（软件加密）技术来保护自身版权。

但计算机病毒会像寄居蟹一样，躲在这些壳里——病毒特征（代码和数据）被改变（压缩、加密等），伪装成正常程序，试图躲过反病毒引擎的查杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz619RJbF0eJnGTNOHyzNS2ibYjT10ZKJeDF7M4DjvSVeCloMic9WqtUYdkJDc1ULib2KPksuUG6FRpfQ/640?wx_fmt=png)

后来出现专门对抗安全软件的“壳”，安全圈称之为“[病毒混淆器](http://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247513467&idx=1&sn=dcc2182d42f4ca003917065cac4413fe&chksm=eb706b44dc07e252634ac85a433032bc8b0a30e72d4eafe4b8246dfe32dbe3813069de8b1b34&scene=21#wechat_redirect)”。

病毒制造者在“壳”的帮助下，可以在短时间内、批量生成数以万计的变形（加壳）病毒样本，并迅速传播。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz619RJbF0eJnGTNOHyzNS2ibAibbhU8UXnyglJlXNDoHZwFD4NIWp1l9hzN3EJkRybdeAvC9CusiaJaQ/640?wx_fmt=png)

这使得传统反病毒引擎“认壳”才能“脱壳”的机制变得很低效。面对这种情况，火绒反病毒团队决定通过“火绒虚拟沙盒”技术，让病毒“不攻自破”。

**0****2**

**火绒虚拟沙盒：高度还原操作系统环境，让病毒不攻自破**

“形兵之极，至于无形。无形，则深间不能窥，智者不能谋。”（《孙子兵法》虚实篇）

火绒虚拟沙盒针对性地模拟了真实的操作系统环境，用“有形”的设计，达到“无形”的感知——让置身于虚拟沙盒的病毒毫无察觉异样，主动卸下“壳”并执行恶意行为，此时，病毒核心特征（代码、数据、行为）便暴露无遗，即可对其精准查杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz619RJbF0eJnGTNOHyzNS2ibm2aQy6vemhpWicbwj25SYqZz4BA2fQic2s880fO6QwVlwVF0PIDcC6WA/640?wx_fmt=png)

实际操作中，当未知文件通过用户下载软件、解压缩文件、接收邮件、插入U盘等渠道进入电脑时，都将会运用到火绒“虚拟沙盒”进行判定，保障用户的安全。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz619RJbF0eJnGTNOHyzNS2ibpRT4ovtL7MicmyOoRgN3w33QZ8jiaRejnibJwQ8dGfUh8CrUb1ks0MK9A/640?wx_fmt=png)

过程看似复杂，但用户却无需等待过长时间。因为火绒虚拟沙盒使用了独有的自研技术，可以在有限时间内还原尽可能多的病毒核心特征，高效地查杀潜在病毒威胁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz619RJbF0eJnGTNOHyzNS2ibk2LcLc1YmwqSicFxyZEU6ExE4Wgu4kH0YuIrlpndF0yoq3XN5d2rhzg/640?wx_fmt=png)

此外，火绒虚拟沙盒还会跟踪和记录这些病毒行为，为火绒工程师减少特征库中的冗余数据做支持，即一条记录可查杀更多样本，从而降低了资源占用。

因此，火绒虚拟沙盒这一技术使得火绒反病毒引擎在做到“精准查杀”、“全面防御”同时，又保证了用户良好的使用感受。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz619RJbF0eJnGTNOHyzNS2ibjYl4HTBnJxU9jVkLcM9K6bMQFYWJ51WTibmVBH18PogQLJMbbYyibmqg/640?wx_fmt=png)

2022年底，[火绒虚拟沙盒正式支持64位虚拟环境](http://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247511237&idx=1&sn=3295bd6b09b0237a829a36ae3b593b72&chksm=eb7072fadc07fbec94e254043dc3da00c21711a57d98f7429cd2c80574e022824107c5ef7576&scene=21#wechat_redirect)，提高了火绒安全产品对日益增长的64位病毒的检出能力。以64位虚拟沙盒环境为例进行演示：

（视频内容仅用于展示火绒”虚拟沙盒”中的执行效果，火绒引擎在扫描样本过程中会自动完成虚拟执行流程并完成病毒监测。）

目前，火绒虚拟沙盒技术已支持Windows x86/x64、Linux x86/x64、Mac OS X x86/x64操作系统平台，且深度适配统信、鲲鹏、深度、神州网信、中科方德、中科红旗、中标麒麟等一众国产操作系统。

在终端攻击日益精进、网络病毒变化无常的互联网环境下，火绒安全坚持“以不变应万变”，通过打磨虚拟沙盒等自主研发技术，牢抓病毒威胁本质，不断筑起稳固的终端防护高墙。

**互动环节：**

**说说你看完文章后理解的火绒虚拟沙盒，截至****4月3日****，在全部留言区中抽取****3位高质量解读的小伙伴****，送出火绒定制礼品一份。**

*规则：*

*\*由于公众号精选留言数量限制，会出现中奖者的中奖信息没有在精选区中展现的情况。*

*\*中奖者中奖后需在2个工作日之内将自己的中奖信息以及中奖截图私信发给绒绒，逾期作废哦~*

更多阅读：

[火绒虚拟沙盒白皮书](http://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247513996&idx=1&sn=33cecac4d77796d3b39e8c00fe57ed82&chksm=eb7069b3dc07e0a542bbae2a816f505a1091a99adc5b6d785286094eb5344b99a51e676d2363&scene=21#wechat_redirect)

[火绒反病毒引擎白皮书](http://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247513972&idx=1&sn=fc81a502b51c5365bfedfbb010a9bcd5&chksm=eb70694bdc07e05dc9bba683daa292d0479b7aa93c8bc8873b0e5076286b1e39214d73136163&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz619RJbF0eJnGTNOHyzNS2ibrrnoyA0PuULjYe0AAx55ia4SsuVdANRl5oAleibQ8gwibtMia4PwD9v4Sg/640?wx_fmt=jpeg "公众号二维码.jpg")

扫码关注

了解更多安全干货、资讯、以及火绒安全大事记

分享收藏点赞在看

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

火绒安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

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