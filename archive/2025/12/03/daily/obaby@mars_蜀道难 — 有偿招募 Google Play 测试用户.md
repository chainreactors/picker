---
title: 蜀道难 — 有偿招募 Google Play 测试用户
url: https://h4ck.org.cn/2025/12/22107
source: obaby@mars
date: 2025-12-03
fetch_date: 2025-12-04T03:17:08.585361
---

# 蜀道难 — 有偿招募 Google Play 测试用户

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

黑客程序媛 / 逆向工程师 / 人工智能学徒 / 用爱发电的独立开发者

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# 蜀道难 — 有偿招募 Google Play 测试用户

2025年12月3日
[32 条评论](https://h4ck.org.cn/2025/12/22107#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/12/微信图片_20251203133112_418_42.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/12/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20251203133112_418_42.jpg)

懒惰，有时候带来的负面效果，后期想要修复的时候，要付出的代驾比当时处理要复杂的多。更恐怖的是，哪怕付出了这么多的代码，依然无法达到最开始的效果。

当 google playstore 开发者给我发邮件提示账号快过期的时候，并没有太留意，后来就给忘了。当然，gmail 的邮箱已经收到了数次提醒，但是由于那段时间不怎么翻墙，导致并没有看到这些邮件，等看到邮件的时候账号已经被用了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/12/Jietu20251203-091933.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/12/Jietu20251203-091933.jpg)

看到这个停用的原因，真的是让人崩溃，这 tmd，当时但凡翻墙了，也就是点几下鼠标的事情。现在好了，重新注册账号依然面临一系列的问题。appid 被占用，旧应用无法下架，无法转让。现在连上线发布都需要面临另外一个问题，那就是需要开启封闭测试，只有封闭测试通过之后才能有发布正式版的权限。

[![](https://h4ck.org.cn/wp-content/uploads/2025/12/Jietu20251203-092243-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/12/Jietu20251203-092243.jpg)

google play开发者给出的答案是：

```
针对新创建的个人账号的测试要求简介
测试是应用开发流程中不可或缺的一环。通过持续对应用运行测试，您可以在公开发布应用之前验证其正确性、功能行为和易用性。这能让您及时解决发现的技术问题或用户体验问题，最大限度地降低这些问题对用户的影响，从而确保您在 Google Play 中发布的是应用的最佳版本。如果开发者在发布应用之前经常使用 Play 管理中心的测试工具进行测试，他们的应用将能够带给用户更优质的使用体验，从而在 Google Play 上赢得更高的评分，取得更大的成就。

为了帮助所有开发者确保提供高品质的应用，我们提出了新的测试要求。如果开发者使用的是 2023 年 11 月 13 日之后创建的个人账号，则其应用需要先经过测试，然后才能在 Google Play 上发布和分发。若应用未经过测试，系统会停用 Play 管理中心内的部分功能，例如正式版（测试和发布 > 正式版）和预注册（测试和发布 > 测试 > 预注册），直到开发者满足相关要求为止。

测试要求概览
如果您使用的是新创建的个人开发者账号，则必须对您的应用运行封闭式测试，且至少有 12 名测试人员在过去至少 14 天内选择持续参与测试。满足上述条件后，您便可以在 Play 管理中心的信息中心申请正式版发布权限，以便最终在 Google Play 上分发您的应用。申请时，您需要回答一些问题，帮助我们了解您的应用、测试流程及正式版发布准备情况。

下文详细介绍了不同类型的测试轨道和相关要求，以及关于申请正式版发布权限的更多详情。

了解不同的测试轨道和相关要求
Play 管理中心提供不同类型的测试轨道，以便您逐步扩大测试范围并改进应用，力求达到适合面向数十亿 Google Play 用户发布的水平。

内部测试：在完成应用设置之前，您可以自行将 build 快速分发给少量可信测试员。这有助于您排查问题并收集早期反馈。通常，build 被添加到 Play 管理中心几秒钟后，就会向测试人员开放。虽然内部测试并非强制性要求，但我们建议您从这里开始。
封闭式测试：利用封闭式测试，您可以与由您控管的众多用户分享应用。这样一来，您可以在发布前修复问题，并确保应用符合 Google Play 政策的要求。您必须先运行封闭式测试，然后才能申请发布正式版应用。当您申请正式版发布权限时，必须至少有 12 名测试人员选择参与您的封闭式测试。他们必须在过去 14 天内选择持续参与。完成应用设置后，您即可启动封闭式测试。
开放式测试：让您可在 Google Play 中发布测试版应用。进行开放式测试时，任何人都可以加入您的测试计划并向您提交非公开反馈。请先确保您的应用和商品详情已经准备好在 Google Play 上架，然后再选择该选项。如果您拥有正式版发布权限，则可以使用开放式测试。
正式版：让您可通过 Google Play 面向数十亿用户发布应用。您需要先运行符合我们条件的封闭式测试，然后才能申请将应用发布为正式版。在申请时，您还需要回答一些与封闭式测试相关的问题。当您申请正式版发布权限时，必须至少有 12 名测试人员选择参与您的封闭式测试。他们必须在过去 14 天内选择持续参与。
```

**如果开发者使用的是 2023 年 11 月 13 日之后创建的个人账号，则其应用需要先经过测试，然后才能在 Google Play 上发布和分发。若应用未经过测试，系统会停用 Play 管理中心内的部分功能**

### 测试要求概览

如果您使用的是新创建的个人开发者账号，则必须对您的应用运行封闭式测试，且至少有 12 名测试人员在过去至少 14 天内选择持续参与测试。

**重要提示：向测试人员强调，他们需要选择持续参与至少为期 14 天的封闭式测试。**

说实话就是现在google 的做法是越来越看不懂了，关键是很多操作也不知道后续该如何操作。这就很蛋疼了，这种事情当然更好的办法是去咸鱼之类的找个专门做测试的。

测试资格需要加入这个 google 群组（需要加入群组之后才能参与测试）：guimiquan@googlegroups.com

<https://groups.google.com/g/guimiquan>

我也没咋用过这个东西，不清楚怎么去处理这个破玩意儿。有时候感觉老外设计的东西，的确是不怎么符合自己的使用习惯。

ap测试地址：

<https://play.google.com/apps/testing/gma.dayi.app>

app商店地址：

<https://play.google.com/store/apps/details?id=gma.dayi.app>

网上依然能找到这种测评服务了，价格大约 200+。

[![](https://h4ck.org.cn/wp-content/uploads/2025/12/微信图片_20251203131921_417_42-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/12/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20251203131921_417_42.jpg)

现在的问题在于重新注册开发者账号话费了 30 美元，现在不上架恶心，上架也恶心。既然如此那还是折腾一下吧，不过鉴于自己手上没那么多的设备，想请各位宝子帮帮忙测试一下，想参与的加一下 google 的群组。需要 12 名测试人员，根据提供的测试账号数量，在测试完成后给于相应的报酬，如果有时间，或者闲着没事的希望可以板帮我哦。

目前我自己还在修改一些问题，希望大家除了加下 google group，顺便加下群哦，QQ群：777692924[![obaby@mars](https://pub.idqqimg.com/wpa/images/group.png "obaby@mars")](https://qm.qq.com/cgi-bin/qm/qr?k=6nfJTxZLHdK-XmQEOaO_Pm7ozYuYtVW0&jump_from=webapi&authKey=XsC0+YLYPsw6+bCyaMidAXTLc1eUYrV66iCEVV9lWJbeGMHIGDHni4K3kdKBRCJp)

需要大家开始帮忙测试了会统一通知一下的。

都说蜀道难，现在发版比蜀道还难，蜀道难都是看得到的难，而这发版，完全是不知道的陷阱。

最后说下测试报酬哈，鉴于价格大约都是 200+，12 个账号，按照每个账号 20 元红包来计算（提供几个测试账号，会获得相应账号数量的红包）。~~如果不想要红包的，可以寄写真照片（3 张），如果喜欢的话。~~

如果种种原因，到时最后测试没通过，红包依然会发放，不过金额就变成 10 元了哈。毕竟不想让大家白费精力，这个钱属实不多。聊表心意，主要是这个应用也没啥盈利能力，全靠用爱发电，小女子先行写过啦。

---

[![闺蜜圈 APP](/wp-content/uploads/2025/11/guimiquan-ads2.jpg)](https://sj.qq.com/appdetail/ma.dayi.app?&from_wxz=1)

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《蜀道难 — 有偿招募 Google Play 测试用户》](https://h4ck.org.cn/2025/12/22107)
\* 本文链接：<https://h4ck.org.cn/2025/12/22107>
\* 短链接：<https://oba.by/?p=22107>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Google](https://h4ck.org.cn/tags/google)[测试](https://h4ck.org.cn/tags/%E6%B5%8B%E8%AF%95)

[Next Post](https://h4ck.org.cn/2025/12/22098)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年11月14日

#### [双 11](https://h4ck.org.cn/2023/11/14268)

2023年2月9日

#### [停掉了亚马逊的服务器](https://h4ck.org.cn/2023/02/11131)

2025年3月17日

#### [后知后觉](https://h4ck.org.cn/2025/03/19828)

### 32 comments

1. ![](https://gg.lang.bi/avatar/c8b1c4e066955840427abd9f454b9fb9569d4480ec1b84bb78c8b210d91893d8?s=64&d=identicon&r=r) **爱看**说道：

   [2025年12月3日 13:45](https://h4ck.org.cn/2025/12/22107#comment-130450)

   ![Level 6](https://badgen.h4ck.org.cn/badge/亲密度/Level 6/red?icon=codebeat)

   ![Google Chrome 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 109") Google Chrome 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   坐一个韩系温暖灵妹妹的沙发

   [回复](#comment-130450)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年12月3日 21:41](https://h4ck.org.cn/2025/12/22107#comment-130468)

      ![公主](https://badgen.h4ck.org.cn/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.h4ck.org.cn/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 142](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 142") Google Chrome 142 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      来帮忙测试~~

      [回复](#comment-130468)
2. ![](https://gg.lang.bi/avatar/19a53855a6616e2ead18670b736d1917a8b5dbe3f22d629e637d9e3f384e451f?s=64&d=identicon&r=r)

   [2025年12月3日 14:44](https://h4ck.org.cn/2025/12/22107#comment-130451)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![Level 6](https://badgen.h4ck.org.cn/badge/亲密度/Level 6/red?icon=codebeat)

   ![WebView 4](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/android-webkit.png "WebView 4") WebView 4 ![Android 16](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 16") Android 16 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   坐一个韩系温暖灵妹妹的板凳

   [回复](#comment-130451)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年12月3日 21:41](https://h4ck.org.cn/2025/12/22...