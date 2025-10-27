---
title: 国际ERP软件大厂云泄露超7亿条记录，内含密钥等敏感信息
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512264&idx=1&sn=007a6b7fc1c0993ea3eafb858aaf53ad&chksm=ebfaf7e8dc8d7efe449dd29e4d528bbe65c01f92ad9bbce15a1711cc208faa0c170b0169c1c6&scene=58&subscene=0#rd
source: 安全内参
date: 2024-07-26
fetch_date: 2025-10-06T17:43:04.436668
---

# 国际ERP软件大厂云泄露超7亿条记录，内含密钥等敏感信息

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7voquSCVLY9QCAiacW04cp3eqXfKbwluejMLrKIG6BUjxT4KiaJL0P6xuWia6oP9c0KcSPic0aU0HLBAw/0?wx_fmt=jpeg)

# 国际ERP软件大厂云泄露超7亿条记录，内含密钥等敏感信息

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tOiaW1QLOL6usmkMDCU0wCorXE2Of8aL4MtmOXyIJN3QTQfibQL7gcTL5GS4FMQr1A7MqyaUTXmRkA/640?wx_fmt=jpeg)

**ClickBalance一个云数据库暴露在公网，导致7.69亿条记录泄露，其中包括API密钥和电子邮件地址等信息。**

前情回顾·**数据泄露狂潮**

* [重大事故！美国电信巨头AT&T几乎所有用户的电话记录泄露](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512164&idx=1&sn=1a0299e7986765bdace20e6bb07e2335&chksm=ebfaf744dc8d7e525f52e457f336a57da63b115d9d078166fee6d4be325ddfda220d7b781d98&scene=21#wechat_redirect)
* [国家医保系统泄露超4200万用户数据，这家国企高管遭议会公开质询](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512142&idx=1&sn=3c286423f92f527b8f0bbd495f923935&chksm=ebfaf76edc8d7e78226e45b1f9af650ebb5a5a3c53875d27b2cf77b4eb896a54c166a25c30e0&scene=21#wechat_redirect)
* [迪士尼泄露1TB敏感数据，黑客称为艺术复仇](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512187&idx=2&sn=7c926821bfd405e34b63d916153ef954&chksm=ebfaf75bdc8d7e4d4485f6a7713e0d99d8f7c33da35067f520c0778ec549ae83fa82141128d9&scene=21#wechat_redirect)
* [超十亿规模！2024年上半年全球重大数据泄露事件盘点](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512081&idx=1&sn=0c9e23a67a9e03357923354256ca0d12&chksm=ebfaf731dc8d7e27d60653ea0e94e56451ff137853dd6f5f131cb817394d2166792c7eafb224&scene=21#wechat_redirect)

安全内参7月25日消息，根据安全研究员Jeremiah Fowler的最新发现，ERP软件提供商ClickBalance拥有的一个包含7.69亿条记录的云数据库未设置任何密码或安全认证，恶意威胁行为者可以轻而易举地访问这些数据。

ClickBalance是墨西哥最大的企业资源规划（ERP）技术提供商之一，提供可以从任何设备访问的ERP工具。ERP工具负责管理和自动化各部门的业务流程，涵盖财务、人力资源、供应链、制造和销售等部门。

Fowler向WebsitePlanet报告了这一问题。该报告指出，该数据库包含了潜在的敏感信息，如访问令牌、API密钥、密钥、银行账号、税号和381224个电子邮件地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7voquSCVLY9QCAiacW04cp3eMJqzKrhHGPnt3Iibs2fZZRz5DiaxyxzHibAMqicZ1hR3kEGFK2frQ0icDcg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7voquSCVLY9QCAiacW04cp3eumpAcAobTtCwqKXQR1aX1pfTrUsDNrL086YdNUmUpTNaWogs7sKnXw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7voquSCVLY9QCAiacW04cp3eNGa2eSdUUOMUD7iaGHUicrTL1JMs7PQCibwKNygaX5ia3ZqTzMkG9oAAEg/640?wx_fmt=jpeg&from=appmsg)

*图：泄露记录的截图（来源：Jeremiah Fowler）*

API和密钥的暴露非常令人担忧，因为网络犯罪分子可能利用这些数据未经授权地访问关键系统和敏感数据，进而引发数据盗窃、账号接管、未经授权的交易和服务中断。

电子邮件地址的暴露也带来了潜在的风险。相关风险不仅限于垃圾邮件，因为91%的网络攻击始于钓鱼邮件。犯罪分子可以创建欺骗性电子邮件以窃取个人信息、财务数据和登录凭证。网络犯罪分子获取业务相关的电子邮件地址之后，可能发动有针对性的钓鱼攻击。

目前尚不清楚数据库暴露了多长时间，也不清楚是否有其他人访问过。不过，Fowler指出，对于管理着大量客户、员工和终端用户数据的科技公司来说，数据保护是一大难题。为此，他们设计了企业资源规划（ERP）、客户关系管理（CRM）和持续诊断与缓解（CDM）系统，方便跟踪和管理这些数据。然而，数据泄露可能暴露敏感信息，带来长期的运营和战略风险。

好消息是，Fowler发送了负责任的披露通知，几小时后该数据库限制了公共访问。尽管如此，为了防范这些风险，组织应更改密码并启用双因素认证（2FA）。

同样重要的是，要警惕未经请求的电子邮件和可疑的信息请求。通过访问控制和安全存储实践保护密钥、令牌和其他管理凭证也至关重要。

**参考资料：hackread.com**

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