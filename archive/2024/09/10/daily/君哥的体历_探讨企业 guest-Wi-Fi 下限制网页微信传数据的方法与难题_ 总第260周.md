---
title: 探讨企业 guest-Wi-Fi 下限制网页微信传数据的方法与难题| 总第260周
url: https://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491425&idx=1&sn=b3f0daef4da06ab503762e70112de3b9&chksm=ea4bb526dd3c3c30a4df13aa3b84859c518d0e72b8dd6f46270afa98ee5f36a48eccaef3585c&scene=58&subscene=0#rd
source: 君哥的体历
date: 2024-09-10
fetch_date: 2025-10-06T18:28:01.220536
---

# 探讨企业 guest-Wi-Fi 下限制网页微信传数据的方法与难题| 总第260周

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwbW9icLn0HbnVSZEgHVcqU4d0HV4zzHygaG3p1YOdl9AUfibKTPR8FWoMiby5dBWvGhENlm4ia0icYkia0g/0?wx_fmt=jpeg)

# 探讨企业 guest-Wi-Fi 下限制网页微信传数据的方法与难题| 总第260周

原创

群秘

君哥的体历

‍‍

‍‍

![](https://mmbiz.qpic.cn/mmbiz_gif/yXsxtS2cfwYLicju4TyAeQhibftSnibn1R9dnxB7tCR0JyCicooUTh4rDmWsBv1wBniaFHVGdaNmMeJOl1hVIicPKkzg/640?wx_fmt=gif)

**0x1本周话题**

话题：跟各位大佬取取经，如何管控连接企业guest- Wi-Fi的情况下，限制使用网页微信传数据的呢？

***Q：这个目的是什么呢？能管控的住网页微信传输，你管不住手机拍照微信传呀，不能说管不住，而是没有一个好方法管住。***

A1：我猜是提供了guest，又不想让员工用公司电脑连。

A2：主要是因为没有DLP，只能从行为准则上约束员工，没法有技术管控和监控措施，所以有点头疼。如果传了什么信息出去也无从查起的。

A3：纯看技术的话，上网行为管理在出口处识别限制。全禁了就行。

A4：封域名简单粗暴。

***Q：guest 不过上网行为管理吧？***

A5：guest不过的，你懂的呀，唯一有的就是镜像流量给公安了。

A6：这个看具体网络怎么接的吧，如果实在不过，出口防火墙/IPS上封域名也可以考虑。guest网络也是组织提供的网络接入服务，网络运营者有必要依照网安法采取监测、记录网络运行状态、网络安全事件的技术措施，并按照规定留存相关的网络日志不少于六个月；所以还是建议接入上网行为管理。

A7：只是传数据你管控不了，你做不了mitm攻击怎么管控，你要说禁止登陆可以，上个上网行为管理。

***Q：这么做的原因是啥？你的需求是什么？或者你的场景是什么？***

A8：随便揣测一下，使用网页微信的场景下，估计是想让人能聊天，但不允许传文件。就怕收个木马啥的。

***Q：guest不是给非公司用户的么，为什么还要管人家传数据？***

A9：可能guest- Wi-Fi 大量内部人也在用。

A10：如果在意，上安全能力就行了，这都有比较成熟的处理方案的，还是个决心问题。

A11：是这个道理，guest任何内外部都能连接使用，所以除了DLP以外想不到其他好方法，然后DLP这个又是很tricky的点。

A12：点很多，比如在guest禁止wx.qq.com，在上网行为禁 但这不是核心矛盾，你的矛盾是数据在电脑上，那么除了网页微信，还可以是任何论坛，网盘，自建站点，终点是在终端下手。这个风险是固有风险，我们在任何一家公司，对这个问题都明明白白地告诉领导，能解决，但要看面对用户的怨言决心有多大，给方案直接给三个层级，第一级做做监控水印，不打扰，事后追溯，第二级上一些DLP，加很多管理审批动作，第三级直接三网分离，能上网的终端没数据，投入多少，用户需求调研情况，当前推荐方案几，说出来。千万不要让领导觉得禁两个网站就能防泄露了，泄露后锤安全，谁使用谁负责，嘴和手在别人身上，直接管理要先抓，我不走guest，回家不也能外发数据么，对吧，guest里防泄露是伪命题。

A13：我们已经在批量测试，笔记本离开公司网络后只能进行白名单访问，进入内网时候就靠防火墙拦截了，这样也防止了一些其他问题比如私用啥的。

A14：这个是靠谱的，只要能管理好业务需求。首先是数据链路。问题是链路中的一个风险点，要提炼出来。 比如笔记本上网是一个数据链路，guest并不是，guest是入网的一种。

A15：做数据防泄漏，不能说想到一个问题就打一个补丁，很被动的。

A16：所以还是传统的筑高墙比较好用，数据围起来，终端只用于云桌面登录。

A17：那也不是。我们vdi就也深坑，并不是所有公司都适合vdi。像我们这种多数业务都是乙方的话vdi上了之后就一直在缝缝补补。

A18：不用这个，安全确实很难做，疲于救火。其实有点羡慕，没VDI的话，乙方来做，更难控。

A19：Vdi、voi、终端dlp、网络dlp，甚至说零信任，不是说哪一个都适合自己，了解现在真的需求是什么再考虑上哪种手段。说最重要的，预算能不能覆盖所有员工。不能覆盖所有员工的话，进vdi和不进vdi是否会有交互以及未来是否可能有交互。

A20：可以装客户端，终端在公司环境下可以上互联网，在不是公司情况下客户端起送后所有流量走公司出口，不管在哪访问互联网要走公司出口，出口统一部署安全设备。

**0x2 群友分享**

**【安全资讯】**

[AI集体失智！9.11比9.9大？微软回应全球死机蓝屏事件：影响850万设备；OpenAI发布GPT-4o mini | Q资讯](http://mp.weixin.qq.com/s?__biz=MjM5MDE0Mjc4MA==&mid=2651213048&idx=1&sn=66ed882bb8df757021cc726fea0ebc04&chksm=bdbbb4ab8acc3dbde507d1d0fcc6692f54d178fcc769ca508a28b0203424ff7b20cec7ee9c22&mpshare=1&scene=21&srcid=0723SkcG7PWTHRqWsmjkvDgr&sharer_shareinfo=540a40e4246cc9a8d9af18a1ee32f74e&sharer_shareinfo_first=540a40e4246cc9a8d9af18a1ee32f74e#wechat_redirect)

[一文带你了解奇安信 深信服 360等25家网安公司现状](http://mp.weixin.qq.com/s?__biz=Mzg5MDgzNTI2Nw==&mid=2247514531&idx=1&sn=509c162d01ce199a9c498fa110ea985d&chksm=cfd4618ff8a3e89904ffce223a6241a2fe44977c81fccd8d7baf300c5c5bc45c32ed47b5900b&mpshare=1&scene=21&srcid=072514DiuSEVfa5hT2w0iPgV&sharer_shareinfo=5d3cc04cced8cfb14aaa8101f07faf1b&sharer_shareinfo_first=5d3cc04cced8cfb14aaa8101f07faf1b#wechat_redirect)

[公安部 国家互联网信息办公室关于《国家网络身份认证公共服务管理办法（征求意见稿）》公开征求意见的公告](http://mp.weixin.qq.com/s?__biz=MzAwMjU0MjIyNw==&mid=2651483197&idx=1&sn=3e2241364925398a13af9bef3d6f92fa&chksm=813613c1b6419ad7e5f77eb4eedd7d5d3138db4b79b5afa61cb2742bba7bb836e6a086c3fb7d&mpshare=1&scene=21&srcid=07266FaCIspPK2eMwTsRI6gb&sharer_shareinfo=9a5c413035aeb679274009f114d44e00&sharer_shareinfo_first=1844e42a4608afc8dc69ab3b3af1fa06#wechat_redirect)

[阿里因违规跨境传输用户信息被罚约20亿韩元](http://mp.weixin.qq.com/s?__biz=MzU1MzAzNzcwNw==&mid=2247491881&idx=1&sn=1e8201d1da852f2c1e7af69f445a884a&chksm=fbfa5bcdcc8dd2dbbf0da6c6a1489f002ec789640053a9979d1e8e451aa27af3a0dbb0a5efda&mpshare=1&scene=21&srcid=0725uzlokCgaeb7owKiO25it&sharer_shareinfo=c4ca3d260cde2514f2df9aac3954ceb0&sharer_shareinfo_first=98e2f6ec343caefe34e6413cec4b840a#wechat_redirect)

--------------------------------------------------------------------------

由于微信修改了推送规则，需读者经常留言或点“在看”“点赞”，否则会逐渐收不到推送！如果你还想看到我们的推送，**请点赞收藏周报，将****君哥的体历****加为星标或每次看完后点击一下页面下端的“在看”“点赞”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwYaBZeQPdr2gbHqon58JxAIpZTicPdU1I8I0lBV82ur0C278ycyU7FKAvOEibactZPNC8L1mu7zMZAQ/640?wx_fmt=jpeg)

【金融业企业安全建设实践群】和【企业安全建设实践群】每周讨论的精华话题会同步在本公众号推送（每周）。**根据话题整理的群周报完整版——每个话题甲方朋友们的****展开讨论内容——每周会上传知识星球**，方便大家查阅。

**往期群周报：**

[**探讨如何避免微软崩盘类事件及安全软件相关问题| 总第259周**](http://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491420&idx=1&sn=e23a04ed372bab4ed974734c125aed12&chksm=ea4bb51bdd3c3c0dbac1bb740ed2fd9345ac5ab74d569b2a5e0db905c54427156c4bd8cfafad&scene=21#wechat_redirect)

[**关于防爬虫及服务器漏洞扫描相关问题的探讨| 总第258周**](http://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491415&idx=1&sn=cc1950b3c5ac269c6a749c1ba9fbbf5c&chksm=ea4bb510dd3c3c06176c89f7d4c7bf17c260f4c964b99c1138cf90e3426f4ba55043f51b25e7&scene=21#wechat_redirect)

[**关于甲方安全管理及相关事务的讨论| 总第257周**](http://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491410&idx=1&sn=3394132f643c16a1cd788a8f8c2f768b&chksm=ea4bb515dd3c3c0333eabedf65a47f5bf0c8446fcf3ed026cf78e035600a4c454ca9d25c47b7&scene=21#wechat_redirect)

## **如何进群？**

**如何下载群周报完整版？**

**请见下图：**

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwbppZu5PBSictiaObD2Bnru4z5nSyfMrsqjPO0micwA8CsIDUxRb73kIPomrYtYpWuWqPwMU17LHAIpg/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/yXsxtS2cfwbbrvrPJc9bTvZFr7n5ZgdWsRKc2GvxcQNogPzLOcveKPP2vpaicqWsRiaASYeEsbAYNsDUWPQ6pyeg/0?wx_fmt=png)

君哥的体历

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yXsxtS2cfwbbrvrPJc9bTvZFr7n5ZgdWsRKc2GvxcQNogPzLOcveKPP2vpaicqWsRiaASYeEsbAYNsDUWPQ6pyeg/0?wx_fmt=png)

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