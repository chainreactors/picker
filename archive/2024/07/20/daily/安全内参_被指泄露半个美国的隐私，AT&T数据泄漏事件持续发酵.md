---
title: 被指泄露半个美国的隐私，AT&T数据泄漏事件持续发酵
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512208&idx=2&sn=ad8fca1fa944c31ee539d2f2085c20e1&chksm=ebfaf7b0dc8d7ea63507feede1cb9a7d34a80e603e8f8d6b8f3cd3585639ede9e55abe092882&scene=58&subscene=0#rd
source: 安全内参
date: 2024-07-20
fetch_date: 2025-10-06T17:43:02.573060
---

# 被指泄露半个美国的隐私，AT&T数据泄漏事件持续发酵

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7s1SYibjXYqnXuniaOQsibQrVXXHV2AFA4GILu0VyHvuHfOwraksUb40wCpN9ANSs9XSFlIfSK655XDg/0?wx_fmt=jpeg)

# 被指泄露半个美国的隐私，AT&T数据泄漏事件持续发酵

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvbWT3zYbYjGmZia46m0uvtoCct8VHkCS7EDhINv765icmVfyakokzgvhn0v49s61vk3HTqiaHTQnNbGQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

美国电信巨头AT&T近日陷入数据泄露风波。该公司上周披露，其客户数据在第三方AI数据云平台发生大规模泄露，超过1亿条用户数据被黑客获得，涉及几乎所有AT&T移动客户的通话和短信记录，半个美国的个人隐私面临威胁。

涉事平台Snowflake近期因大量客户（缺乏基本的安全控制措施）遭黑客攻击而饱受质疑，AT&T是众多受影响的企业之一，票务巨头Ticketmaster也在此事件中受到波及。

**被指非法存储分析用户数据**

美国参议员理查德·布卢门撒尔（Richard Blumenthal）和乔什·霍利（Josh Hawley）昨日向AT&T及Snowflake发出质询信函。作为参议院司法委员会隐私、技术和法律小组委员会的主席和高级成员，他们要求AT&T首席执行官约翰·斯坦基（John Stankey）回答一系列问题，**包括为何AT&T会长时间保留客户通信的详细记录，并将这些敏感信息上传至第三方分析平台。**

AT&T和Snowflake均未在向客户和美国证券交易委员会（SEC）的披露中解释Snowflake的使用方式。Snowflake官网称，其云平台为全球企业提供合作和数据共享的机会，其独特架构几乎可以连接任何规模的业务，将数据和工作负载汇集在一起。Snowflake市场简化了数千个数据集、服务和整个数据应用的共享、协作和货币化，从而创建了一个活跃且不断增长的AI数据云。

对于为何将用户数据上传到第三方数据云，AT&T首席数据官安迪·马库斯（Andy Markus）表示：“Snowflake数据云赋予了我们利用和整合数据以获得洞察力的能力，这推动了收入增长，提高了成本效益，最重要的是，（数据上云）改善了客户体验。”马库斯表示，之前的内部系统使得与其他公司的合作变得困难。“在使用Snowflake之前，我们有一个非常复杂的本地数据环境，”马库斯说：“这导致我们的的运营环境非常低效。”

在回应参议员关于其使用Snowflake的问题时，AT&T表示：“像大多数处理大量数据的公司一样，AT&T经常使用专用的可信云服务平台集中处理大量数据。通常，AT&T会将数据副本放在第三方平台上，用于与业务相关的分析。例如分析历史客户数据，用于网络规划、容量利用以及开发新服务和优惠。”

AT&T并未透露保留用户数据的具体时间，只是含混地表示：“我们根据个人信息的类型、运营业务或提供我们的产品和服务所需的时间，以及是否受到合同或法律义务的约束来设定数据保留期限。这些义务可能是正在进行的诉讼、强制性数据保留法律或政府为调查而保存数据的命令。”

**半个美国社会的隐私或被拍卖**

AT&T表示，被盗的通话和短信记录还包含与AT&T手机号码互动过的（其他运营商的）电话号码。尽管客户姓名、社会安全号码和通信内容并未泄露，但AT&T承认，犯罪分子可能会找到与特定电话号码相关联的姓名。

AT&T表示，它不认为被盗的用户数据已经公开泄露。据报道，AT&T曾向黑客支付37万美元以删除记录（并收到黑客发来的证明数据被删除的视频）。然而，布卢门撒尔和霍利并不相信AT&T的保证。

此前，网络犯罪集团ShinyHunters已经泄露了Ticketmaster客户的记录，并打算出售从Snowflake其他客户那里窃取的数据，参议员们在信中指出：“没有理由相信AT&T的敏感数据不会被黑客拍卖并落入犯罪分子和外国情报机构手中。”

参议员们AT&T客户的位置数据被泄露表示担忧：

*虽然记录没有直接包含姓名和地址，正如AT&T的SEC文件所指出的，被盗数据包括位置信息，很容易找到与电话号码相关联的姓名。结合起来，被盗信息可以很容易地为网络犯罪分子、间谍和跟踪者提供AT&T客户几个月的通信和活动日志，包括这些客户的生活和旅行地点——这对用户隐私构成严重威胁。*

参议员们要求AT&T在7月29日之前解释黑客如何获得对其Snowflake工作区的访问权限，并“全面说明从AT&T被盗的数据类型以及这些数据如何威胁客户隐私”。

参考链接：

https://arstechnica.com/tech-policy/2024/07/after-breach-senators-ask-why-att-stores-call-records-on-ai-data-cloud/

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：GoUpSec

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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