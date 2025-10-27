---
title: 身份安全巨头Okta源代码泄露
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507271&idx=2&sn=a3ddcad7cb0e56d608550e0ce567392b&chksm=ebfa9a67dc8d137168246229dee8f7063f951b896ec3288292d238ce63afcaa4d71e695de885&scene=58&subscene=0#rd
source: 互联网安全内参
date: 2022-12-23
fetch_date: 2025-10-04T02:20:43.270824
---

# 身份安全巨头Okta源代码泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7t4vL9q0l3olhnjiaRcQYfNojkXeUwib9ohLqNrm5dsCsVM7GyjB4rqY7mszGGXY923rwE0mDh39YKg/0?wx_fmt=jpeg)

# 身份安全巨头Okta源代码泄露

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvZ6ejgA6eOdU20jXkLMZh4cWx4lNrg3fKP31ZRhVPzF8ogYIxIgzoCnPhrwHBicXERJxVVgj8v26Zg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

著名身份验证和IAM解决方案提供商Okta本周三披露其私有GitHub存储库本月遭到黑客攻击，源代码遭泄露。

![](https://mmbiz.qpic.cn/mmbiz_gif/INYsicz2qhvZ6ejgA6eOdU20jXkLMZh4cjViazClWibvglf2hvfLcf5V5PYLlfdEia8QVibptYVkFwbdJEsDDHldHQg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**源代码被盗，客户数据不受影响**

据BleepingComputer报道，Okta在周三晚间已通过电子邮件给客户发送安全警报，已确认多个来源（包括IT管理员）已收到此电子邮件通知。

本月早些时候，GitHub曾提醒Okta其代码存储库遭可疑访问。

“经调查，我们得出结论，这种非法访问被用来复制Okta代码存储库。”该公司首席安全官（CSO）David Bradbury在电子邮件中写道。

Okta表示，尽管黑客窃取了Okta的源代码，但并未访问Okta服务或客户数据。Okta的“HIPAA，FedRAMP或DoD（国防部）客户”不受影响，因为Okta保护服务的手段“不依赖其源代码的机密性”。因此，无需其客户执行任何操作。

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvZ6ejgA6eOdU20jXkLMZh4cqtn1r53ic6tZgJbricc6zA8tGLXSUvxSBR8yB7icYcha4icukjL5HibxruQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

根据Okta的电子邮件通知内容，该数据泄露事件似乎与Okta Workforce Identity Cloud（WIC）代码存储库相关，但与Auth0客户身份云产品无关。

邮件通知的其余部分内容摘录如下：

在获悉可能存在可疑访问后，我们立即对访问Okta GitHub存储库设置了临时限制，并暂停了所有GitHub与第三方应用程序的集成。

此后，我们审查了最近对GitHub托管的Okta软件存储库的所有访问，以了解暴露的范围，审查了最近对GitHub托管的Okta软件存储库的所有提交，以验证我们代码的完整性，并轮换了GitHub凭据。我们还通知了执法部门。

此外，我们已采取措施确保此代码不能用于访问公司或客户环境。Okta预计不会因此事件而对我们的业务或我们为客户提供服务的能力造成任何中断。

注意：安全事件与Okta劳动力身份云（WIC）代码存储库有关。它与任何Auth0（客户身份云）产品无关。

在该“机密”电子邮件的结尾，Okta表示本周四将在其博客上发表声明。

**2022是Okta的灾年**

对于Okta来说，2022是多灾多难的一年，遭遇了一系列安全事件。

今年9月，Okta旗下的Auth0曝出类似的源代码泄露事件。根据Okta的说法，较旧的Auth0源代码存储库是由“第三方个人”通过未知方式从其环境中获取的。但是，Okta的问题由来已久，今年一季度遭受黑客攻击后的披露过程就已发生违规行为。

今年三月，勒索软件组织Lapsus$在Telegram上发布被盗Okta数据的屏幕截图，声称它可以访问Okta的管理控制台和客户数据。

在宣布调查该事件后，Okta很快承认遭受黑客攻击，且攻击实际上发生在2022年1月下旬，影响其2.5%的客户。考虑到当时Okta的客户数量超过1.5万，业界估计约有375个Okta客户受到事件影响。

同一周，Okta承认在延迟披露这次黑客攻击方面“犯了一个错误”，该公司表示，这次黑客攻击源于其第三方承包商Sitel（赛克斯）。

4月，Okta澄清说1月份的黑客攻击仅持续了“25分钟”，影响范围明显小于最初的预期：仅限于两个客户。

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