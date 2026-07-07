---
title: 0181.我是如何在一个人工智能自由职业平台上找到绕过电子邮件验证的方法的
url: https://mp.weixin.qq.com/s/uOqPUBXj0aY4nSdhPyv8Qw
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:02:59.430646
---

# 0181.我是如何在一个人工智能自由职业平台上找到绕过电子邮件验证的方法的

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MW9pCm89BuuofZX6JGxDMibo65K6cbbzUn4t4cW7denbtQVdONkBxAMJNbIKmGat748kfzoqnic2P0XhcVbWERvuU7IdBQXsqjR7kfv9ZT1W4/0?wx_fmt=jpeg)

# 0181.我是如何在一个人工智能自由职业平台上找到绕过电子邮件验证的方法的

原创

Hangga
Hangga

Rsec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文章仅用网络安全研究学习，请勿使用相关技术进行违法犯罪活动。

声明：本文搬运自互联网，如你是原作者，请联系我们！

类型：电子邮件验证绕过

*一个简单的实现缺陷使得用户无需打开验证邮件即可完成电子邮件验证。*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuuVOujf8aRic58ia6gXAUO5B5XqlxvSsKR8BAkhlc2heictFibAyg9rrd05gLOZquvQQuH4orpTzD0Qceo05J5yYUVpHfF5dZLUD7c/640?wx_fmt=png&from=appmsg)

几周前，我在 LinkedIn 上浏览自由职业机会时，偶然发现了一个利用人工智能技术寻找自由职业者的平台。这个平台看起来很有意思，所以我决定注册一个账号，看看它是如何运作的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuvIOeR8URRAtRleXNsE46KNicbylRs2hyEzvZia4cqtuicojTscH3L8l8cCsibcnibv5DkwlAzIOtxEibkHibeVlQbUpwXDrRicwRjdRvM/640?wx_fmt=png&from=appmsg)

这并非一次漏洞搜寻活动。我只是以普通用户的身份注册而已。

话虽如此，我却有一个很难改掉的习惯。

每当我在新网站注册时，我通常都会打开 Chrome 开发者工具，观察网络流量。我这样做已经很多年了，一部分原因是出于好奇，另一部分原因是这有助于我了解应用程序的构建方式。

有时候我找不到任何有趣的东西。

有时我会学习应用程序的工作原理。

偶尔……我会发现一些开发者意想不到的东西。

事实证明，这正是其中一次。

## 负责任的披露

在深入探讨技术细节之前，先简单说明一下。

我已负责任地将此问题报告给了平台的安全团队。报告已得到确认，问题也已修复。

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BusZgvHGS1ZGBFhVmrkUnCxldf1w1GYghmDtoiaXEI98QCMKibyOzoouvSUnE1L3IhlTCb1iaGZfRsOHjKUXGx55pRQ31CLpb7cUco/640?wx_fmt=png&from=appmsg)

为了避免暴露受影响的平台，我在本文中隐去了其名称、域名、屏幕截图以及任何其他识别信息。

有趣的是，在调查这个问题时，我还发现了另一个安全漏洞。不过，那是另一个故事了。

## 查看注册流程

注册时，我使用了一个临时邮箱地址。我通常在尝试新服务时这样做，尤其是我不确定是否会继续使用它的时候。

在点击 **“注册”** 之前，我打开了 Chrome 开发者工具并切换到了 **“网络”** 选项卡。

更具体地说，是 **Fetch/XHR** 请求。

注册完成后，我开始审核应用程序生成的请求和响应。

大部分交通状况都和我预想的一样。

注册请求返回了基本帐户信息、一些状态字段和其他一些信息。

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BusTGhJQaG2QqAG1bWGdCnwN4sNia9jntjFCZicayZsjK9Yzx6rQiaPsTiaia3MGunhXDAcXyvrcNtugoHG79dtrNbeic7fb98ZNTNd38/640?wx_fmt=png&from=appmsg)

该 token 值显然是一个 JWT。

当时，一切看起来都没有什么特别可疑的地方。

许多现代应用程序会在用户注册后立即自动验证其身份，因此返回 JWT 并不罕见。根据应用程序的架构，这可能是一种完全合理的设计选择。

我只是把它记在心里，然后继续观察注册流程。

几秒钟后，验证邮件就到了。

和大多数验证邮件一样，这封邮件里有一个按钮，指向一个类似于这样的网址：

```
https://[REDACTED]/verify-email?token=<JWT>
```

```

```

一切正常。

直到我仔细观察了一下。

验证 URL 中的令牌看起来非常眼熟。

我返回到注册响应中，复制了这两个值，并将它们进行了比较。

它们完全一样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89ButeRNXMnaJBTG8Mu6u7nMJfqzPJ2p2Xgg5SpX5WiaibUkeRp0DUpnvxtL68tW5licdpW6GgLCNBUGW1KILVHVyF2uSeXOQEAPlEuA/640?wx_fmt=png&from=appmsg)

这立刻引出了一个简单的问题。

> ***如果我已经从注册响应中获得了此令牌，我还需要验证电子邮件吗？***

回答这个问题的唯一方法就是进行测试。

所以我注册了另一个账号。

## 检验假设

##

我没有点击邮件中的验证链接，而是决定使用另一个临时邮箱地址重新注册。

目标很简单。

我可以**在不打开验证邮件的情况下验证账户吗？**

注册第二个账号后，我再次查看了注册响应，并复制了 API 返回的 JWT。

这一次，我完全忽略了收件箱。

相反，我按照我在电子邮件中看到的相同格式，手动构建了验证 URL。

```
https://[REDACTED]/verify-email?token=<JWT>
```

我将网址粘贴到浏览器中，然后按了**回车键**。

账户已立即通过验证。

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuuyZcEfkRboYeAAYj2q2WXwRemxNNiaFI8IW6sOiaG07upcp3ZyibAVEd2ORIcEQD4ezbuHgRI8OskZJdy3tl4xV35ZY1F6nicK6CI/640?wx_fmt=png&from=appmsg)

至此，该假设得到了证实。

其实并不需要验证邮件。

只要注册响应中显示的 JWT 与验证端点使用的 JWT 相同，那么任何注册帐户的人都已经拥有验证帐户所需的一切。

邮件内容仅仅是客户已经收到的信息。

## 为什么会发生这种情况

需要指出的是，问题不在于 JWT 本身。

JWT（JSON Web Token）广泛应用于现代 Web 应用程序中，用于身份验证和在系统之间安全地传输签名信息。

注册后返回 JWT 本身并不危险。许多应用程序会在用户创建帐户后立即自动登录。

这个问题其实很简单。

该应用程序将同一个令牌用于两个不同的用途。

注册 API 返回的 JWT 也被电子邮件验证端点接受。

因此，验证邮件不再是信任的来源。

该应用程序没有验证邮箱的所有权，而是信任了注册时已提供的信息。

换句话说，电子邮件验证变成了一个可选步骤，而不是一项安全控制措施。

## 电子邮件验证应如何运作

电子邮件验证的目的很简单：

> ***证明创建账户的人确实有权访问注册的电子邮件地址。***

典型的电子邮件验证流程如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuvpzPVfKRBsrarKn9iaYmg2wWTUGVWQMjQM7KaZy6Sh6DTVpF0DenCCRMUcDNpnLWib39PO8eLlhvVJIJPKc7fqrfTtzpicbGDxEQ/640?wx_fmt=png&from=appmsg)

注意验证令牌的来源。

验证令牌的**唯一预期来源**是用户的邮箱。如果有人无法访问邮箱，他们就不应该能够获取令牌，因此也不应该能够验证帐户。

现在请将此与本案的情况进行比较。

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuvEGt6GbBmuGOjNE6UM9s35mvI5xObtoB12ek2eylYKmPkWN21hd5x5iaW8J9rOod21K3lyG5urrI4cze9yATWVjutqN3a5Zohw/640?wx_fmt=png&from=appmsg)

验证邮件并没有起到电子邮件所有权证明的作用，而是简单地重复了注册过程中已经公开的信息。

一旦这种情况发生，验证过程就无法回答最初的安全问题了：

> ***“该用户是否实际控制了注册邮箱？”***

相反，它变成了：

> ***“该用户是否还保留着注册时已返回的 JWT？”***

这是两种截然不同的安全保障措施。

## 安全影响

乍一看，这似乎是一个很小的实现错误。

毕竟，攻击者只是在验证自己的账户而已。

然而，真正的问题是信任模式的破裂。

一旦应用程序接受了用户已拥有的验证令牌，它就不再验证电子邮件地址的所有权。

根据平台如何使用已验证的电子邮件地址，这可能会产生多种后果。

例如：

* 用户无需访问注册邮箱即可验证帐户。
* 虚假或一次性电子邮件地址的使用变得更加容易。
* 任何假定已验证电子邮件属于其所有者的功能，都不能再依赖这种假定。
* 基于“已验证”状态构建的未来工作流程将继承同样的不信任模型。

最终影响取决于具体应用。

部分平台仅使用电子邮件验证来减少垃圾邮件。

其他人则将其用作密码恢复、身份验证、邀请、金融交易或访问敏感功能的先决条件。

无论具体实现方式如何，其根本保证始终不变：

经过验证的电子邮件地址应意味着用户已证明其拥有该邮箱的所有权。

在这种情况下，该保证已不复存在。

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuspNRAc7lxSwAwIbml4MgL3FOlRXXZrKxnor9l3pUsgvceU5jg3UdFA87g8aeib7AGiafZBTHAcVYWfdDNjnlPY1eWCmq8v2IUqo/640?wx_fmt=png&from=appmsg)

## 经验教训

应用安全领域最吸引我的一点是，有趣的发现并不总是来自复杂的技术。

这并非自动扫描的结果。

它不是通过 Burp Suite 扩展、自定义工具或模糊测试发现的。

事实上，我只使用了以下工具：

* 网络浏览器
* Chrome 开发者工具
* 临时电子邮件服务
* 好奇心

该漏洞并非隐藏在数十个请求或复杂的身份验证流程背后。

它就明摆着。

只需要放慢速度，观察应用程序的运行情况，然后问一个简单的问题：

> ***我真的需要验证邮件吗？***

这个问题导致了业务逻辑上的缺陷，使得电子邮件验证成为可选功能。

这提醒我们，应用程序安全并不总是关于发现巧妙的有效载荷或绕过复杂的过滤器。

有时候，关键在于理解某个功能应该实现什么目标，然后验证其实现是否真正提供了安全保障。

## 最后想说的话

作为开发者，我们常常关注某个功能是否有效。

作为安全研究人员，我们还需要问它是否**安全可靠**。

在这种情况下，注册流程似乎运行完美。

用户收到了一封验证邮件。

验证链接有效。

账户已通过验证。

从功能角度来看，一切似乎都没问题。

然而，从安全角度来看，这封电子邮件已经失去了其最初的用途。应用程序信任的令牌已经在注册过程中泄露，这使得收件箱与验证过程无关。

这就是为什么业务逻辑漏洞如此容易被忽视的原因。

一切正常，没有出现任何崩溃。

未出现任何错误信息。

没有扫描仪发出警报。

该应用程序运行完全符合预期——直到有人质疑该功能背后的安全假设是否仍然成立。

感谢阅读！

如果你是一名开发者，我希望这篇文章能鼓励你不要只关注某个功能是否有效，还要思考它应该提供什么样的安全保障。

如果您对漏洞赏金或应用程序安全感兴趣，请记住，您并不总是需要高级工具才能找到有意义的漏洞。

有时候，Chrome 开发者工具、仔细观察和一点好奇心就足够了。

祝你破解愉快！🚀

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

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