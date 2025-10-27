---
title: 数据泄漏论坛发生数据泄漏：20万BreachForums会员曝光
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512247&idx=2&sn=21edea8e44da4114218c684d97be943f&chksm=ebfaf797dc8d7e814750d0fce596baaff87435a2c6b5b862ec68f11433ba5f081a449baafa87&scene=58&subscene=0#rd
source: 安全内参
date: 2024-07-25
fetch_date: 2025-10-06T17:43:42.575849
---

# 数据泄漏论坛发生数据泄漏：20万BreachForums会员曝光

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7u8Y20vOhbVib6FRts9DJxD4lFiaNPslxjYeggS5vqpzPdabaoOubdibzpg45qfF3TTStLDNmiaicuqmoQ/0?wx_fmt=jpeg)

# 数据泄漏论坛发生数据泄漏：20万BreachForums会员曝光

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvaTR4SjBfgwIDJZg4lvHO6bxKfRwZCa91b2p0w3pfziagE7HtbH6YALpKNNlNGPcOeE4V74mo1hxHg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

在网络安全领域，最讽刺的事莫过于一个以数据泄漏和交易为主要“业务”的黑客论坛，其自身用户数据遭到泄漏。2022年成立的BreachForums v1黑客论坛的私密会员信息近日在网络上被曝光，为威胁行为者和研究人员提供了深入了解该论坛用户的机会。

**规模最大的暗网数据集市**

BreachForums是规模最大最知名的数据泄漏平台这一，但该论坛并非单一实体，而是多个以数据收集者和威胁行为者社区为依托，进行数据交易、销售和泄露的论坛的统称。这些论坛的鼻祖是RaidForums，但在2022年被FBI查封后，名为Pompompurin的威胁行为者推出了BreachForums（亦称为Breached），以填补市场空缺。

BreachForums迅速崛起后，其成员泄露了大量被盗数据，包括美国国会医疗保健提供商D.C. Health Link、RobinHood和通过暴露的API泄露的Twitter数据。然而，在D.C. Health Link数据泄露后不久，论坛所有者Conor Fitzpatrick，即Pompompurin，在2023年3月被FBI逮捕。

此后，该论坛的多个版本被创建并被执法部门查封。最新版本由ShinyHunters（现已转交给新管理员）推出，至今仍在运营。

**20多万论坛会员信息曝光**

我们所称的BreachForums 1.0，即Fitzpatrick在2022年最初创建并最终在2024年被FBI查封的网站，其数据最近遭到泄漏。知名威胁行为者Emo上周泄露了BreachForums 1.0的212,414名成员的个人信息。

据Emo称，这些数据直接来自Fitzpatrick，他据称在2023年6月试图以4000美元的价格出售这些数据，当时他正在保释中。Emo表示，这些数据最终被三名威胁行为者购买。

Fitzpatrick在2024年1月因违反其审前释放条件（包括使用未受监控的计算机和VPN）再次被捕。目前尚不清楚这是否与他试图出售BreachForums数据有关。

2023年7月，一个名为'breached\_db\_person'的人士试图在黑客论坛上以10万至15万美元的价格出售论坛数据库。卖家还与Troy Hunt分享了出售的数据，Hunt透露，这些数据包括Emo泄露的数据和其他数据库记录。Hunt随后将这些信息添加到了Have I Been Pwned数据泄露通知服务中。

Emo告诉BleepingComputer，这些数据来自2022年11月的BreachForums数据库备份，是上传到Fitzpatrick的MEGA账户中的最后一个备份。

泄露的数据包含论坛成员的用户ID、登录名、电子邮件地址、注册IP地址以及最后一次访问网站的IP地址。BleepingComputer分析了数据库，并确认它包含了许多在原始BreachForums上有账户的研究人员的准确信息。

**泄漏数据可用于追踪不法分子**

这些泄漏数据似乎是手动导出的，不是MyBB论坛数据库格式，而是用制表符分隔值导出。尽管数据库很可能在论坛被查封后已经落入执法部门手中，但这些数据对于安全研究人员创建威胁行为者画像仍然有用。

利用泄露的电子邮件地址和IP地址，研究人员和执法部门可以将BreachForums成员与其他网站、他们的地理位置以及可能的真实姓名联系起来。

同样，2023年5月，RaidForums论坛47.8万名成员数据的数据库也被泄露到网上。

**参考链接：**

*https://www.bleepingcomputer.com/news/security/breachforums-v1-hacking-forum-data-leak-exposes-members-info/*

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