---
title: 【安全圈】PhishWP 插件劫持 WordPress 电子商务结账功能
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067220&idx=3&sn=b3641123d0bc84854504b30b4a1e8f93&chksm=f36e79d4c419f0c2e5556e086204515ecae46d8c2d09e94b434cec572067205ca2ea41584ff7&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-09
fetch_date: 2025-10-06T20:11:33.906533
---

# 【安全圈】PhishWP 插件劫持 WordPress 电子商务结账功能

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaGZya5Fue1ZicCVlowwoypOGUKicB1iae9c3fIu1BSbffU50P7aqgflkQk324dLklyJfrG3O4tWKmYA/0?wx_fmt=jpeg)

# 【安全圈】PhishWP 插件劫持 WordPress 电子商务结账功能

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaGZya5Fue1ZicCVlowwoypOByIHv8qrOBN3TGiawAnj5cTL0ib0T4ka6hvHT8v4mc8tukOGfDGhbf2w/640?wx_fmt=other&from=appmsg)

在俄罗斯网络犯罪论坛上发现的恶意插件会创建虚假的在线支付流程，将WordPress 网站变成钓鱼页面，这些流程会令人信服地冒充可信的结账服务。该恶意软件会伪装成 Stripe 等合法的电子商务应用程序，然后窃取客户的支付数据。

SlashNext 的研究人员在本周发布的调查结果中透露，这款名为 PhishWP 的 WordPress 插件是由俄罗斯网络犯罪分子设计的，具有极强的欺骗性。他们表示，除了模仿人们熟悉的合法在线交易支付流程外，它还有一个关键功能，即允许用户在支付过程中创建一次性密码 (OTP)，从而使交易的支付流程看起来安全。

然而，支付网关不会处理付款，而是在人们输入个人数据时窃取信用卡号、有效期、CVV、账单地址等信息，因为他们认为他们使用的是合法的支付网关。一旦插件的受害者按下“输入”，数据就会发送到网络犯罪分子控制的 Telegram 帐户。威胁者可以像使用任何 WordPress 插件一样使用该插件，要么将其安装在合法但被入侵的 WordPress 网站上，要么创建一个欺诈性网站并在那里使用它。

SlashNext 安全研究员 Daniel Kelley 在帖子中写道：“PhishWP 的功能可以让虚假的结账页面看起来真实，窃取安全代码，立即将您的详细信息发送给攻击者，并欺骗您认为一切正常。”

证书生命周期管理 (CLM) 公司 Sectigo 的高级研究员 Jason Soroko 指出，这种数据的立即转换“为网络犯罪分子提供了进行欺诈性购买或转售被盗数据所需的凭证 — — 有时是在获取数据的几分钟内”，这使得他们将插件用于邪恶目的可以快速获得投资回报。

## PhishWP 恶意软件的其他主要功能

OTP 劫持是该插件的主要功能之一，这些功能结合起来可以为攻击者提供劫持支付页面的交钥匙解决方案。其中包括上述可自定义的结帐页面，这些页面通过“高度令人信服”的虚假界面模拟常见的支付流程，Kelley 写道。

PhishWP 的另一个功能是浏览器分析，它捕获除支付信息之外的数据，以复制用户环境，以备将来可能出现的欺诈行为。这包括 IP 地址、屏幕分辨率和用户代理。

该插件还通过使用自动回复电子邮件向受害者发送虚假订单确认信息，为被劫持的结账流程增加了合法性，从而延迟了怀疑并因此延迟了对攻击的检测。如前所述，PhishWP 还与 Telegram 集成，可立即将窃取的数据实时传输给攻击者，以供潜在利用。

该插件还提供了模糊版本，以便隐身，或者用户可以使用其源代码进行高级攻击者自定义。最后，PhishWP 还提供多语言支持，因此攻击者可以在全球范围内攻击受害者。

## 基于浏览器的电子商务网络钓鱼防护

为 WordPress 网站创建恶意插件已经成为网络攻击者的一种家庭手工业，由于该平台的流行，这为他们提供了广泛的攻击面，据 WordPress 主题提供商 Colorlib 称，截至今天，WordPress 已成为大约 4.72 亿个网站的基础。

PhishWP（或任何恶意的WordPress 插件）如此危险的原因之一是，恶意进程直接内置于浏览器中，因此当它作为在线互动的合法部分出现时很难被检测到。

为了防御此类威胁，SlashNext 建议使用可直接在浏览器内部运行的网络钓鱼保护功能，以便在网络钓鱼网站到达最终用户之前发现它们。这些解决方案可在各种浏览器中使用，它们在浏览器内存中运行，可在用户接触恶意 URL 之前阻止它们。该公司表示，这提供了传统安全措施可能错过的实时威胁检测和阻止功能。

来源：https://www.darkreading.com/threat-intelligence/phishwp-plugin-hijacks-wordpress-e-commerce-checkouts

***END***

阅读推荐

[【安全圈】突发！美国国防部将华为、腾讯、长鑫、商汤等134家中国企业列入黑名单，6家被移出](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067202&idx=1&sn=97ab8cecb79ef8ef7f1b0f9e1f763a05&scene=21#wechat_redirect)

[【安全圈】12306崩了？官方客服：现在已陆续恢复](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067195&idx=1&sn=43161803d494ae048c39293a76429c49&scene=21#wechat_redirect)

[【安全圈】Kimi崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067195&idx=2&sn=37f830d2b9baded62b6af05e5a623f76&scene=21#wechat_redirect)

[【安全圈】Nikki-Universal 网络攻击 – 黑客声称窃取了 761.8 GB 的数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067195&idx=3&sn=146eb72a2193578816de50a7988608bc&scene=21#wechat_redirect)

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