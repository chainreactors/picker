---
title: AI漏洞挖掘：我的一些感想
url: https://mp.weixin.qq.com/s/9GljM5jXaRDKFCxHLyMGPA
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:41:15.315937
---

# AI漏洞挖掘：我的一些感想

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7AnuFAq7GcNibRLwYdgUTpuL3Rt0NnwpWD8ibx3ymDpTeicBT9BlWzRVrKkiaRwhaTCSv6US7ibTtTFD6qgXJyomfz09XzeTicFAz2ibvQpPRa0u5E/0?wx_fmt=jpeg)

# AI漏洞挖掘：我的一些感想

EnhancerSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

首先，我先抛出我的观点：大家都可以尝试利用AI去辅助进行漏洞挖掘，会有不一样的收获。当然这篇文章仅个人观点，欢迎转发及留言讨论

不管是在和学员及企业负责人交流的时候，我都说，可以去尝试AI辅助漏洞挖掘，可以尝试但要小心，最好在测试环境中进行。但今天不谈一些利用方式、操作手法，我自己操作了哈，因为精力问题没有操作过多。（没有一点点时间）

![](https://mmbiz.qpic.cn/mmbiz_png/7AnuFAq7GcNyZE7Mqh6cULEHTCeXxtpLhDMXlepq8gDNyWOWtrWKm7DnhzAStC2KQNe9mpobiba0pLWCibVLnrsX2FSC7Mq0vviatfSBnEjlgI/640?wx_fmt=png&from=appmsg)

今天谈谈AI漏洞挖掘边界的问题及这个时代抛弃基础就靠AI了吗？

1. 目前大多数的学员尤其是学生，都会问我如何通过AI进行漏洞挖掘？我反问，你的目的是什么—拿赏金还是就业，如果他的目的是拿赏金我便告诉他方法及注意事项，当然如果是就业，我会劝他，把AI当成学习的工具，丰富你的知识库，要知道，面试的时候可没有AI帮助你，再换句话说，如果你连什么是漏洞都不知道就只靠AI，那最好是希望能够靠AI挣到你几十年的钱。说说漏洞挖掘吧，早期纯手写的工具Sqlmap，也听闻16年有大佬利用Sqlmap一晚上挖了十几万（对了，他前两年还在某公司任职），但写出这个工具的人，不可能对Sql注入不了解，后来的ARL、Xray、Goby，同样也有人挖得风生水起，也挖了不少，相同的，开发者不可能对漏洞挖掘流程不清楚，依稀记得有个QingScan，当时搞的流水线，还没弄明白啊哈哈哈，再到AI时代，也是类似的，希望是做开发工具的人，还是使用工具的人，看个人，也抱不准未来几年内还有比AI更牛逼的工具，你是选择到处要工具，还是选择依据自己的知识库创造/赋能工具？有的人挖漏洞是因为兴趣，有的是因为谋生，举个例子，我在上海，我如果要安家，100平需要500万，你怎么才能挣到这个钱，反之，之前和某个学员交流，一样是全职，他一年挖的钱差不多能够买他生活的城市一套房，而我如果挖得一样的话，我需要3-4年才能够买房，全款的情况下，包括个人的消费习惯，也有的学员，年入10W+在上海照样过得风生水起，这个大家根据自身真实情况去选择，有计划，比漫无目的来得更好，所以至此，应该能够让大家明白到底怎么选吧？
2. 关于AI漏洞挖掘边界的问题，我觉得未来token肯定会是便宜的，大家觉得给AI设立边界有用吗？我觉得有用，但效果可能只能达到70%，你的话术再怎么牛逼，你都没办法达到百分百，就跟你设立一块牌子，禁止吐痰，难免还是会有人吐痰，可能到这儿大家还不知道这里的意思，举个例子，之前在金融甲方的时候，记得有位小伙伴违规操作，就暂停了两三秒，损失几百万吧，这谁来负责呢？举个例子，自己有个学员利用AI进行挖掘的时候，设立了边界，访问了某接口，结果导致该厂商所有网盘数据丢失，这个站点厂商是没有备份的，附上之前有人中sorry木马后，没有备份，不是任何一个厂家都有能力备份的

   ![](https://mmbiz.qpic.cn/mmbiz_png/7AnuFAq7GcNzKsqYoFOGibDbVeV2PP2GjibStsznYicssxMIcBGUShKJA1ibljktXmmYl10AibWYbUWgMSObvic77OduKSZQicNbLib1A0mXCNUAiayo/640?wx_fmt=png&from=appmsg)

   ![](https://mmbiz.qpic.cn/mmbiz_png/7AnuFAq7GcP2g4KmbN0LsnraeKxPYRRt3yjKwdbsDc81XssUyP3fxyvXJsUoKKYN29NicOuNp5gqLFIBiaWCRqWjicYwvnXtwLQjNK2wW47WOY/640?wx_fmt=png&from=appmsg)

   这个师傅事后说的，再也不用AI挖了，过了半个月后继续还是用起AI了

   ![](https://mmbiz.qpic.cn/mmbiz_png/7AnuFAq7GcOxdMSa1MWibWdFb093yib1NUiaOA2ClhicjcoWxaNvwog4ecticBvFyHbkHyK0S8B7enceqicGIfV8fNQ6WhjiaiaXpqWph2ZejGibIib4A/640?wx_fmt=png&from=appmsg)

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/7AnuFAq7GcMgSfsf7l5zE3mK6tpzOO6IyD2xx5UMNdK3KaibvG8wFokV8c0ibccRXluMjGk3uQQziaoC7l9EIM2dbzLPDiaJZUUVcmDHAUXRkUM/640?wx_fmt=png&from=appmsg)

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/7AnuFAq7GcMyOS5fu1rjOvicA6R0yFI1Ww4k48EzLPOibC6wPKt1vOHiaFXz55WQb5UleWiacwzJn0UL7B6WoWYibStvMttZn49fqy5nRvjb2U0w/640?wx_fmt=png&from=appmsg)

   举个例子，最近的某src群里发的通告，他们家的src运营人美心善，负责任，不愿看到这个事情发生的，可还是发生了

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/7AnuFAq7GcNDud3TB9b7xwzYnCjXb9CWQpSCxdibOzQAjfKygeUNkOmGGPhfRWyJZ8v2UjynlAcnuHpLLoNSzZ1y8nhicia4Unpa7DiaXXtTVbQ/640?wx_fmt=png&from=appmsg)

   不清楚这次有没有设立边界，但敬畏边界，敬畏红线，所以你们自己定夺呢？
3. 那AI漏洞挖掘能做什么呢？最近看了很多大佬出了很多框架，我觉得都不错，无论是面向workflow、subagent，我认为大家可以做一些不影响服务端正常运行的，客户端或者测试环境，完全没问题，但我还是会继续用到挖掘一些服务端漏洞上，当然仅个人观点，读者们的行为概不负责

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/DLnxHnM3icnJEfbGsKGNhbFWODg7EKH8rTRHJqtff6Cosq0hWxGicicE3lzIkTHxv0EDSaUU2v1kdBGNDHlR1wa6g/0?wx_fmt=png)

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