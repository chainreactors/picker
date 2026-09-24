---
title: FBI疑似发生重大数据泄露，所有警员数据外泄
url: https://mp.weixin.qq.com/s/zcSO93Bg8aW6wRSB3HdXMQ
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:00:09.597767
---

# FBI疑似发生重大数据泄露，所有警员数据外泄

# FBI疑似发生重大数据泄露，所有警员数据外泄

安全内参编译
安全内参编译

安全内参

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FzZb53e8g7vpWwsFqA6BCdYdybrUSDj7dXClIjL98tqlYVOXlPVxYSHK8y7QzM8x9NK3GvyhnxpIb4ddfIwBAQ/640?wx_fmt=png)

为报复FBI披露成员身份信息，数据勒索组织ShinyHunters声称攻破了FBI的招聘网站及AWS政府云设施等，窃取了所有警员的数据，以及2-3TB数据；

该组织放出的警员样本数据经验证真实，FBI回应称正在调查中；

如果此事属实，将是AWS政府专有云罕见的严重安全事件，专有云并不因专有而更加安全，依然需要完善的安全防御措施。

前情回顾·数据泄露狂潮

* [国家级身份认证平台疑似数据泄露：涉1.5 亿余条公民证照 暗网可实时查询](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516535&idx=1&sn=bec163c257d8069d2d35090bfc01d25e&scene=21#wechat_redirect)
* [英国最大机场集团发生数据泄露，近900万客户数据失窃](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516508&idx=2&sn=f3a6a279f951f559c6f41ad1af2d451b&scene=21#wechat_redirect)
* [医疗巨头遭勒索攻击，2.84亿条患者隐私数据疑泄露](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516499&idx=1&sn=110f85e410f7ed9ef824c28c591c2aec&scene=21#wechat_redirect)
* [政务系统泄露全国大半民众数据，某国主管部门管理层全部辞职](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516460&idx=1&sn=28cfb5bd92fb01efff40c45a296535d2&scene=21#wechat_redirect)

安全内参9月23日消息，知名黑客组织ShinyHunters声称，已入侵美国联邦调查局（FBI）的多个系统，并窃取了“所有FBI员工和申请人的数据”。该组织向外媒404 Media透露，被窃数据包括FBI探员姓名、家庭住址、电话号码以及配偶信息。

此次数据泄露后果可能极其严重，并可能引发一系列国家安全和反情报问题。此前，与ShinyHunters同属一个黑客生态圈的犯罪分子曾利用窃取的电话记录等数据，追踪、恐吓和骚扰正在调查他们的FBI探员。如此敏感的数据也可能成为外国情报机构的重要情报来源，帮助他们进一步了解FBI的运作方式。

FBI是美国最重要的执法和情报机构之一。如果这些数据落入更多犯罪分子手中，FBI探员及其配偶的人身安全也可能面临严重威胁。

攻击者放出高置信度样本警员数据

该组织告诉404 Media：“我们黑进了FBI。我们掌握所有FBI员工和申请人的数据。”

该组织还向404 Media提供了一份样本。据称，样本涉及5000名FBI员工的个人信息，如疑似住址、电话号码、出生日期，以及部分人员的配偶信息。

404 Media把样本中的部分电话号码输入开源情报工具OSINT Industries查询，发现这些号码确实对应样本文件中所列姓名的人员。404 Media还用网络安全公司District 4开发的泄露数据查询工具Darkside检索了部分记录。结果显示，其中一些电话号码与美国司法部工作人员有关联。

FBI招聘网站也被篡改成恐吓公告

ShinyHunters在昨天还篡改了FBI招聘网站。被篡改的页面显示：“本网站已被ShinyHunters接管。”这明显是在模仿FBI及其他执法机构查封网站后经常发布的公告。

![](https://mmbiz.qpic.cn/mmbiz_jpg/wT9KAyOic0NDXPkiaFJBIkpt9FxicjTxYGnSWCw7PibbeXJ5nJemy32iaowfiacgeufWN4vjB4VoEvmXnhLUgCv3eTeNzlrVbYGIt5f3dHWQdg9es/640?wx_fmt=jpeg&from=appmsg)

ShinyHunters于周一晚间实施了此次攻击。截至报道发布时，FBI招聘网站显示：“Apply.fbijobs.gov和特工申请门户目前无法使用。”

被篡改的页面还写道：“所有FBI数据均已遭泄露，包括现任和离任FBI员工的个人身份信息和受保护健康信息（PII/PHI），以及所有申请人信息。我们掌握的数据远比这里声称的更多。”

这份声明最后还顺带嘲讽了美国政府，模仿特朗普在Truth Social上的发帖风格写道：“感谢您对此事的关注。”

FBI尚未立即回应置评请求。

攻击者或利用零日漏洞进入AWS政府云，

称窃取了2-3TB数据

ShinyHunters利用Oracle产品PeopleSoft中的一个零日漏洞发起攻击，随后进入AWS GovCloud服务器并下载数据。据透露，被窃取的数据总量在2至3TB之间。

ShinyHunters通常会先入侵目标，随后尝试勒索。该组织会威胁受害机构或企业：不支付高额费用，就公开更多窃得的数据。FBI显然不可能支付这样的赎金。

当被问及是否会勒索FBI时，ShinyHunters表示：“我们计划采取的行动，我不会称之为勒索，也许应该叫胁迫。”

该组织补充说：“这并非出于经济利益。”

**参考资料：bleepingcomputer.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

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