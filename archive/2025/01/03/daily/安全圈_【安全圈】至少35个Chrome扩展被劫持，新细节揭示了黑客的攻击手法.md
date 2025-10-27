---
title: 【安全圈】至少35个Chrome扩展被劫持，新细节揭示了黑客的攻击手法
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067095&idx=4&sn=6f97d873b84e125e9f9c5c98947bace2&chksm=f36e7957c419f0412b07eb498c174dea03fb3fba7d73eee2c7a42847e16f218f9895baa3c13d&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-03
fetch_date: 2025-10-06T20:10:07.083159
---

# 【安全圈】至少35个Chrome扩展被劫持，新细节揭示了黑客的攻击手法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgeDMicLOlDVtx02W5UwWKa6qCzT4FpZ5Yl1oqOhg9YEABLzHhKn1VKmahI95jaY0N4nkyWkbUdnvQ/0?wx_fmt=jpeg)

# 【安全圈】至少35个Chrome扩展被劫持，新细节揭示了黑客的攻击手法

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgeDMicLOlDVtx02W5UwWKa6GCeH4f417Aic8ackcndPubtThJHibuXu5PPEmRajOZM5bh7d6035zdxQ/640?wx_fmt=jpeg&from=appmsg)

据BleepingComputer消息，近期，黑客针对多个Chrome扩展程序进行了攻击，数十万用户受到影响。随着调查的深入，一些攻击活动细节也得到了披露。

根据最新调查，攻击导致至少 35 个扩展程序被植入数据窃取代码，较之前的初步怀疑数量直接翻倍，其中包括来自网络安全公司 Cyberhaven 的扩展。尽管最初的报道集中在 Cyberhaven 的安全扩展上，但随后的调查显示，这些扩展被大约 260 万人使用。

根据 LinkedIn 和Google Groups 上目标开发者的报告，攻击活动大约在 2024 年12 月5 日开始。然而，BleepingComputer 发现的早期命令和控制子域名早在 2024 年 3 月就已经存在。

## 一个欺骗性的 OAuth 攻击链

攻击始于直接发送给 Chrome 扩展开发者或通过与其域名关联的支持邮箱发送的钓鱼邮件。BleepingComputer 发现以下域名在此活动中被用来发送钓鱼邮件：

* supportchromestore.com
* forextensions.com
* chromeforextension.com

钓鱼邮件伪装成来自 Google官方，声称扩展违反了 Chrome Web Store 政策，并面临被删除的风险。

“我们不允许扩展包含误导性、格式不良、非描述性、无关、过多或不适当的元数据，包括但不限于扩展描述、开发者名称、标题、图标、截图和宣传图片，”钓鱼邮件中写道。

具体来说，扩展开发者被引导相信其软件描述包含误导信息，必须同意 Chrome Web Store 政策。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgeDMicLOlDVtx02W5UwWKa6nezuia3Xaeu5FTz8XWibhGuvjBUaI0ecISMRF82cCUh4tFnpc8A7QIoQ/640?wx_fmt=jpeg&from=appmsg)攻击中使用的网络钓鱼电子邮件

如果开发者点击嵌入的“前往政策”按钮以了解他们违反了哪些规则，他们将被带到一个 Google 域上含有恶意OAuth 应用程序的合法登录页面，该页面是 Google 标准授权流程的一部分，旨在安全地授予第三方应用程序访问特定 Google 账户资源的权限。

在该平台上，攻击者托管了一个名为“隐私政策扩展”的恶意 OAuth 应用程序，要求受害者授予通过其账户管理 Chrome Web Store 扩展的权限。在这过程中，多因素认证（MFA）并未帮助开发者保护账户，因为 OAuth 授权流程中不需要直接批准，而是默认用户完全理解他们授予的权限范围。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgeDMicLOlDVtx02W5UwWKa6ZgHib4If6OeuACZjhEeb8MagibEpRYuM2bjaECwfjfYvqcZVSlSQNiahQ/640?wx_fmt=jpeg&from=appmsg)权限审批提示

Cyberhaven 在事后分析中解释道，有员工遵循了标准流程，无意中授权了这个恶意的第三方应用程序。但员工启用了 Google 高级保护，并且账户覆盖了 MFA，且在过程中没有收到 MFA 提示，员工的 Google 凭证未被泄露。

一旦威胁行为者获得了扩展开发者账户的访问权限，便会修改扩展，加入“worker.js”和“content.js” 两个恶意文件，其中包含从 Facebook 账户窃取数据的代码。

这些恶意扩展随后作为新版本发布在 Chrome Web Store 。虽然 Extension Total 正在跟踪受此钓鱼活动影响的 35 个扩展，但攻击的 IOC 表明，目标数量远不止这些。

根据 VirusTotal 的数据，攻击者为目标扩展预注册了域名。虽然大多数域名是在 11 月和 12 月创建的，但 BleepingComputer 发现攻击者在 2024 年3 月就在对攻击进行测试。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgeDMicLOlDVtx02W5UwWKa6fMMcDbQuSeM6GxvVaXHkYJqZlbs33vXqwsjJySZibiaDR0qesZTG5Mzg/640?wx_fmt=jpeg&from=appmsg)网络钓鱼活动中使用的早期子域

## 针对 Facebook 商业账户

对受感染机器的设备显示，攻击者瞄准了恶意扩展受害者的Facebook 账户，试图通过数据窃取代码获取 Facebook ID 、访问令牌、账户信息、广告账户信息和商业账户。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgeDMicLOlDVtx02W5UwWKa62A8N7Y0WFicDeuj8pRLmWLNAOPticvU1C4xQsGicrySJe9PD9l5rlCZmA/640?wx_fmt=jpeg&from=appmsg)窃取Facebook数据的扩展程序

此外，恶意代码还添加了一个鼠标点击事件监听器，专门用于受害者在 Facebook.com 上的交互，寻找与平台的双因素认证或 CAPTCHA 机制相关的 QR 码图像，从而试图绕过 Facebook 账户的 2FA 保护并劫持账户。

被盗信息将与 Facebook cookie 、用户代理字符串、 Facebook ID 和鼠标点击事件一起打包，并外泄到攻击者的命令和控制（C2）服务器。

攻击者一直在通过各种攻击途径针对 Facebook 商业账户，以直接从受害者的信用卡窃取资金、发布虚假信息、执行钓鱼活动，或通过出售访问权限来获利。

参考来源：New details reveal how hackers hijacked 35 Google Chrome extensions

***END***

阅读推荐

[【安全圈】网络安全公司员工监守自盗：编写黑客代码窃取2.08亿条公民个人信息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067069&idx=1&sn=f3c972e235871147200f79b82f689d25&scene=21#wechat_redirect)

[【安全圈】捷某网络云平台漏洞曝光：50000 台设备面临远程攻击风险](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067069&idx=2&sn=516425f9b9c6da18a71ed20d3b724b4b&scene=21#wechat_redirect)

[【安全圈】黑客利用第三方SaaS服务成功入侵美国财政部系统](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067069&idx=3&sn=bd0876c49c1d286c84408344ea9a8bc8&scene=21#wechat_redirect)

[【安全圈】日本航空公司遭网络攻击导致全球瘫痪](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067033&idx=1&sn=3ae632fb4839dc14720917aa26fe469c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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