---
title: 休眠的 GitHub 账户帮助攻击者在映射企业组织时融入其中
url: https://mp.weixin.qq.com/s/gdCnkIckEMbqgBb9XvbahA
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:57:21.752130
---

# 休眠的 GitHub 账户帮助攻击者在映射企业组织时融入其中

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADs8Ia3UlUSy4iaxSfmic9QicDgY0ibm9xpLW9ia3mRgcFDeUmgKUQOXB0ibRJicDk3MCejRfpzoleOibd9iasVpT1VQTpZj4qOp2VX6Gqxw4/0?wx_fmt=jpeg)

# 休眠的 GitHub 账户帮助攻击者在映射企业组织时融入其中

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADsibuyP5N7BHRibETs2nTJr40icQEfcsn7cAWfDBiae96ToVcQkicFkSpcvKlUwj8twgLq7eyWbgojaPs6x23ia7omNIPL8kxkVsYOia8Q/640?wx_fmt=jpeg&from=appmsg)

Datadog安全实验室对“几个重叠的活动”发出警告，这些活动通过GitHub API系统地枚举企业GitHub组织、存储库和用户帐户。

Datadog的高级安全工程师朱莉·艾格尼丝·斯帕克斯（Julie Agnes Sparks）表示：“运营商依赖于带有定制或合法用户代理的自动抓取工具，利用GitHub的‘幽灵’账户，这些账户通常已有多年的历史，或者来自合法用户的OAuth令牌和个人访问令牌（pat）受到破坏。”

虽然该活动在大多数情况下涉及针对公共数据，但选择实例已经超越了公共信息枚举，成功地克隆了私有存储库。

该活动使用了自动扫描工具，超过50个休眠帐户和数十个合法帐户，这些帐户无意中暴露了个人访问令牌（pat）或通过其他方法受到损害，以方便枚举。

值得注意的是，这些“幽灵”账户是在两到五年前创建的，在将其用于跨多个组织发出API流量之前，它们故意长时间处于不活跃状态。这种技术是战略性的，因为它旨在避免引起任何危险信号，并将活动伪装成合法的，而不是创建新账户并立即使用它们进行抓取。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADs9XAl8HckxtJ9Va14oKySaStgx6CN1pVPxkYoy4T7rpzZ9mdfOCGjEPhd6W3Px3mS1LgI1urRQ1TWXF1Ijka7yuA0pFAA2v7IM/640?wx_fmt=jpeg&from=appmsg)

由于GitHub的API表面的很大一部分无需身份验证即可访问，因此枚举查询返回必要的数据，同时融入正常的API使用。其中包括

* 列出组织的公共存储库
* 遍历用户的关注者和关注列表
* 列举专家、带星号的仓库和组织成员，以及
* 对公共对象运行GraphQL查询

威胁参与者可以使用这些信息进行侦察，并以编程方式绘制组织的github相关活动，例如其公共存储库、其成员、这些成员关注的对象以及他们修改的项目。

在一些情况下，数据访问已被证实，攻击者采取措施克隆属于单个组织的私有存储库。

单独来看，这些请求中的大多数都是不起眼的。它们到达公共端点，干净地验证或根本不验证，并返回成功的响应，”Datadog说。“问题在于聚合：一组账户在公司的GitHub组织中同步移动，版本化的定制工具迭代数周，在最坏的情况下，参与者停止枚举并开始克隆。”

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

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