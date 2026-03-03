---
title: 【服务端漏洞-访问控制缺失-第二章第四节】开工大吉！分享一个“朴实无华”的越权思路：从false改到true就够了
url: https://mp.weixin.qq.com/s/ILR5FRWLngoM04Uz6vsIJA
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:09:23.454434
---

# 【服务端漏洞-访问控制缺失-第二章第四节】开工大吉！分享一个“朴实无华”的越权思路：从false改到true就够了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qg1MKHx3jGG7cqiay7S1vQgThicU27zwYBAOkdibuQE3scmGTNNiaTx1icy2Zfd70LWdvkics63dmIOLibKI5aCuqBOVZRVdUgvWdpD5jScUNtJDAs/0?wx_fmt=jpeg)

# 【服务端漏洞-访问控制缺失-第二章第四节】开工大吉！分享一个“朴实无华”的越权思路：从false改到true就够了

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

大家新年好呀，因为过年期间忙于走亲戚啥的，所以就停更了一段时间。小编给大家说一句抱歉哈~

继续上一章节中[【服务端漏洞-访问控制缺失-第二章第三节】找不到敏感路径？试试这招，源码里可能写着答案](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797902&idx=1&sn=eb21005002736cd9feaba85824c9183c&scene=21#wechat_redirect)的内容，如果在特殊文件和源码中都找不到突破点的话，我们要如何深入呢？今天给大家分享另一个思路，就是检查基于参数的访问控制方法，从这里入手，也会得到意想不到的效果。

某些应用在用户登录时确定其访问权限或角色，并将此信息存储在用户可操控的位置。可能的存储位置包括：

* 隐藏字段
* Cookie
* 预设查询字符串参数

应用会根据用户提交的数值做出访问控制决策。例如：

https://insecure-website.com/login/home.jsp?admin=true

https://insecure-website.com/login/home.jsp?role=1

这种方式的缺陷在于用户可篡改数值，从而访问未经授权的功能（如管理功能）。

以下，这边结合一个实际的例子来给大家分享一下，如何利用系统的这种漏洞，越权获取到系统的访问权限。

这个系统在登录成功后，直接访问它的/admin 目录，是会直接返回该目录是只有admin账号才能访问的，其他账号是没有访问权限的，具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGFADqhAgkP0E6PYtqHVr8hUzOFKs0r2mjib2z56ewsicJdicIl9j3Ka0cFS3zHeicmFYyBDb3XZgaF6tydFt0b8G6kgPCXiaVFVTvyY/640?wx_fmt=png&from=appmsg)

使用burpsuite进行抓包，发现在请求该路径时，请求头中的cookie是有带是否为admin的标识的，具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGEsdAbCtMqQ3ZAonAjsoLR7hKMLEe3FGjIdLOI6pibFvud8Xg1asomuWGKpcH9ECReoc79sPNEBkzlLlXahicGbCHpBu5Iw8MLqw/640?wx_fmt=png&from=appmsg)

这种情况下，我们就可以直接将这个请求发送至burpsuite的repeater中，然后直接将cookie中的请求头进行修改为true，发现系统直接就返回了admin账号下的访问菜单路径，直接实现了越权。具体如下：

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGEicrdqq9VQo1fBib0mFXBiacmniaDpzhV3pmzH9JFtXQQEMXIxzkvmwUG3HzJ0JMzkAp9XTutAog86wNYkcydFMXno9ncicsSW7WDU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGGibHows8bW5c8GsB3uzvdFfmAyQklrEj8D1Xv9pb4b0eNZBw0lWwXpUXsgr3IpMz8fWicyUJKj1TdsPtZfWOz0BkSbtSUicfMFC0/640?wx_fmt=png&from=appmsg)

关于访问控制权限缺失的另一种挖掘方式，今天就分享到这了。后续这边还会继续分享有关服务端的更多漏洞原理、利用、挖掘方式，感兴趣的可以点点关注。

觉得文章对你有一丝启发或作用的话，一键三连（点赞、分享、关注），就是对我最大的鼓励，谢谢![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_64@2x.png)。

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