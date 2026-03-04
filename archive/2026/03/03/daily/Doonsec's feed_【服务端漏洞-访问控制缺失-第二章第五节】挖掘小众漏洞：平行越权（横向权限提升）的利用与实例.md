---
title: 【服务端漏洞-访问控制缺失-第二章第五节】挖掘小众漏洞：平行越权（横向权限提升）的利用与实例
url: https://mp.weixin.qq.com/s/7l_SjdFgQ5nrzLVeAKc9mQ
source: Doonsec's feed
date: 2026-03-03
fetch_date: 2026-03-04T04:01:38.121881
---

# 【服务端漏洞-访问控制缺失-第二章第五节】挖掘小众漏洞：平行越权（横向权限提升）的利用与实例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qg1MKHx3jGFKvyYw2DzG3ZM7919wMnsh7iabkjxWDkiavILrUYMEBretLg5uYI3nBKg9yFy2DmCph8penSyuUqhSVMSldPyVGENFLKOz9xz3Q/0?wx_fmt=jpeg)

# 【服务端漏洞-访问控制缺失-第二章第五节】挖掘小众漏洞：平行越权（横向权限提升）的利用与实例

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

在前面章节中，这边分享了较多垂直越权的情况，有因为特殊文件泄露未限制路径导致的[【服务端漏洞-访问控制缺失-第二章第二节】别找了，高危漏洞有时就藏在最显眼的地方](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797878&idx=1&sn=20e404cd7640867d43ffc148c1dcf3d1&scene=21#wechat_redirect)、有因源码中泄露后台管理地址的[【服务端漏洞-访问控制缺失-第二章第三节】找不到敏感路径？试试这招，源码里可能写着答案](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797902&idx=1&sn=eb21005002736cd9feaba85824c9183c&scene=21#wechat_redirect)、也有因参数控制缺失导致的[【服务端漏洞-访问控制缺失-第二章第四节】开工大吉！分享一个“朴实无华”的越权思路：从false改到true就够了](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797911&idx=1&sn=4863f1391f97c349b21e9bd40b35da69&scene=21#wechat_redirect)。

今天这边就不分享垂直越权的情况了，今天给大家分享一些关于平行越权的情况。

首先，大概过一下什么是平行越权。

平行越权，也叫横向权限提升：

当用户能够访问属于其他用户的资源，而非自身同类型资源时，即发生横向权限提升。例如，若某员工既能查看本人记录，也能访问其他员工的记录，便属于横向权限提升。

横向权限提升攻击可能采用与纵向（垂直）权限提升相似的利用方法。例如，用户通过以下URL访问个人账户页面：

https://insecure-website.com/myaccount?id=123

若攻击者将id参数值修改为其他用户的标识，就可能获取他人账户页面及其关联数据与功能。

某些应用中，可利用的参数值并不具备可预测性。例如，应用可能使用全局唯一标识符（GUID）而非递增数字来识别用户，这能防止攻击者猜测或预测其他用户的标识符。但这些属于其他用户的GUID可能暴露在应用中引用用户的其他位置，例如用户消息或评论区域。

如果以上概念看起来有点模糊，结合以下的实际例子，应该能让你茅塞顿开~

这个系统，在登录A账号后，进入该账号的个人中心，是请求和返回如下内容的：

请求路径为：https://xxx.com/my-account?id=45cd1444-d16b-4bac-9236-0870961dcf4a

该个人中心是会返回个人的api key信息的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGELLx33ibSvsbtfKx2Xe7TDCuPVpzCalJibVYmq0VdqGeAtatg1fWd7nWzWmFw7o0L4wNGolhhopwvDOMNXANev12dJJoHvmemrU/640?wx_fmt=png&from=appmsg)

单独从以上内容来看，貌似系统也不存在什么问题，但当我们在查看系统的其他功能时，发现它在系统的已发布内容中，返回了对应文章发表者的ID，这个ID极有可能就是和个人中心的ID是一致的。具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGG4J02Wm5k96HpiaJTDso0oav7I27yHAW4icHS3QuXcGLNv11BPaGmDNv60ejCkO4Iorjdqa224ue0J5ns8mlLlgT5gZDVE6RnVo/640?wx_fmt=png&from=appmsg)

要验证想法就很简单了，直接将文章列表中返回的，其他人的ID拷贝过来，在个人中心替换请求路径中的ID，发现替换后请求，确实会直接返回对应用户的个人中心信息，包括他的 api key，这就实现了平行越权了。具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGE46yuFgQfjPNjSZhoibJuA2TQvt3Unl9pUibHmdesTZebiciaVRRnQaZjKUSeb4blf8ustxRGYTUbCaH9wSGBfFm4KLYmM7zC8DNI/640?wx_fmt=png&from=appmsg)

关于平行越权（横向权限提升），今天就分享到这了。后续这边还会继续分享有关服务端的更多漏洞原理、利用、挖掘方式，感兴趣的可以点点关注。

觉得文章对你有一丝启发或作用的话，一键三连（点赞、分享、关注），就是对我最大的鼓励，谢谢![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_64@2x.png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

升斗安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

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