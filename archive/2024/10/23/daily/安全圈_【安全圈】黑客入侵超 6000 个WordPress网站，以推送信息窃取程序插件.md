---
title: 【安全圈】黑客入侵超 6000 个WordPress网站，以推送信息窃取程序插件
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065418&idx=4&sn=54b2785c3f2cf0adab1b10c7ef51ef5e&chksm=f36e62cac419ebdc60aa74380c4933297bd8d2ff531f60a01703a0908e0c0d051e980f7128e2&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-23
fetch_date: 2025-10-06T18:52:15.089570
---

# 【安全圈】黑客入侵超 6000 个WordPress网站，以推送信息窃取程序插件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhyYqxp8icDLic11UKaSMVQvvpUdcjrJ214zYMuZKTJAISC6mGeeehQKicMqhnfaQv7T8BYyzL7h22oA/0?wx_fmt=jpeg)

# 【安全圈】黑客入侵超 6000 个WordPress网站，以推送信息窃取程序插件

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网站漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhyYqxp8icDLic11UKaSMVQvvsOVvrvAuK8XhbXub8w7dRJ5h5bk6SupOXC81jicNEHPYTbpEicj3E8ug/640?wx_fmt=jpeg&from=appmsg)

WordPress 网站近日被黑客非法入侵并安装恶意插件，这些插件会推送虚假的软件更新和错误信息，从而推送窃取信息的恶意软件。
在过去几年时间里，信息窃取恶意软件已成为全球安全防御者的“心腹大患” ，因为被盗凭据通常会被用来入侵网络和窃取数据。
自 2023 年以来，一个名为 ClearFake 的恶意活动一直被用于分发虚假的 Web 浏览器更新横幅。2024 年，一种名为 ClickFix 的新活动问世，它与 ClearFake 有许多相似之处，但不同的是它会假装是软件错误信息，并附有修复程序。然而这些 “修复 ”都是 PowerShell 脚本，执行后会下载并安装信息窃取恶意软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhyYqxp8icDLic11UKaSMVQvv4JCE4BaVP7GXSn3PE804ujGhbPyjHbCcLlQQQ8XhVTHNJF0eBqI1lA/640?wx_fmt=jpeg&from=appmsg)

假冒 Chrome 浏览器错误的 ClickFix 叠加示例，来源：BleepingComputer

今年，ClickFix 活动变得越来越常见，一旦威胁行为者成功入侵网站，就会显示 Google Chrome 浏览器、Google Meet conferences、Facebook 甚至验证码页面的虚假错误的推送信息。

## 恶意 WordPress 插件

上周，GoDaddy 报告称，ClearFake/ClickFix 威胁行为者已经入侵了 6000 多个 WordPress 网站，安装恶意插件来显示与这些活动相关的虚假警报。

GoDaddy 安全团队正在追踪一种新的 ClickFix（也称 ClearFake）虚假浏览器更新恶意软件变种，该恶意软件通过虚假 WordPress 插件传播，GoDaddy 安全研究员 Denis Sinegubko 解释说。

这些看似合法的插件被设计成对网站管理员无害，但却包含嵌入式恶意脚本，会向最终用户发送虚假的浏览器更新提示。

这些恶意插件使用了与合法插件类似的名称，如 Wordfense Security 和 LiteSpeed Cache，而其他恶意插件则使用了通用的编造名称。

2024 年 6 月至 9 月期间，在该活动中出现的恶意插件列表如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhyYqxp8icDLic11UKaSMVQvv5rxic5ia4wEQ5RsS5cXMYsmGjUo4HricIoY4DjR1gcSwTMMRxD4Tg51xA/640?wx_fmt=jpeg&from=appmsg)

网站安全公司 Sucuri 指出，名为 “Universal Popup Plugin ”的虚假插件也是该活动的一部分。安装后，该恶意插件会根据变种关联各种 WordPress 操作，向网站的 HTML 中注入恶意 JavaScript 脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhyYqxp8icDLic11UKaSMVQvvanlRHxZ56AhGHOXM5eHU55dVxbp9gPVkD6vjQZZbicibRMeicHrv6OdnA/640?wx_fmt=jpeg&from=appmsg)

注入 JavaScript 脚本，来源：GoDaddy

加载该脚本后，该脚本将尝试加载存储在 Binance 智能链 (BSC) 智能合约中的另一个恶意 JavaScript 文件，然后加载 ClearFake 或 ClickFix 脚本以显示虚假横幅。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhyYqxp8icDLic11UKaSMVQvvNjcXIjuvSZMI0A3NflGTz7K5lsY2f6UKxPOvTIa6T4hxbNvwC9bb3w/640?wx_fmt=jpeg&from=appmsg)

伪造的谷歌更新横幅，来源：Randy McEoin

从 Sinegubko 分析的网络服务器访问日志来看，威胁者似乎是利用窃取的管理员凭据登录 WordPress 网站，并以自动化方式安装插件。

从下图中可以看到，威胁者通过单个 POST HTTP 请求登录，而不是首先访问网站的登录页面。这表明这是在已经获得凭据后自动完成的。

威胁行为者登录后，就会上传并安装恶意插件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhyYqxp8icDLic11UKaSMVQvvfDaUjtQ3Juped0kb6pxhcOebpYuspWafK2aOAo8FQIe1HZnwCH5ib0Q/640?wx_fmt=jpeg&from=appmsg)

显示 WordPress 网站如何被入侵的访问日志，来源：GoDaddy

虽然目前还不清楚威胁者是如何获得凭证的，但研究人员指出，这可能是通过以前的暴力攻击、网络钓鱼和信息窃取恶意软件获得的。

如果您正在使用 WordPress，并且收到了向访问者显示虚假警报的报告，您应立即检查已安装的插件列表，并删除任何非您自行安装的插件。

如果发现未知插件，也要立即将所有管理员用户的密码重置为仅在网站上使用的唯一密码。

参考来源：https://www.bleepingcomputer.com/news/security/over-6-000-wordpress-hacked-to-install-plugins-pushing-infostealers/

***END***

阅读推荐

[【安全圈】罗马法院要求Cloudflare分享盗版网站运营者信息 并永久禁止其注册新域名](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065399&idx=1&sn=dec2eb151c9b0f0077123a3318be0b24&chksm=f36e6237c419eb21a40648b41536ebd647e51215f36ce9173ad5d0cc0fda9fa8eb10c26b0398&scene=21#wechat_redirect)

[【安全圈】黑客团伙Anonymous Sudan被FBI重创，组织者被判终身监禁](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065399&idx=2&sn=a5694f5c85e2be9fd8b358c5e0120c0d&chksm=f36e6237c419eb21ba3c279c549d9311f5c7ab66bbd04a8f9a5b86a8f6b002c99be0c5dcdc3b&scene=21#wechat_redirect)

[【安全圈】ESET合作公司遭入侵，向以色列发送数据擦除程序](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065399&idx=3&sn=dacaf2f4ee866d214c7f7b0faa72c698&chksm=f36e6237c419eb2114883fd8867dd3cfd654f569b15b7cebaea0859b3f35e53cafe3a995117f&scene=21#wechat_redirect)

[【安全圈】微软运用欺骗性策略大规模打击网络钓鱼活动](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065399&idx=4&sn=5299976412ef6656de32b3865b26b921&chksm=f36e6237c419eb21b92b21e6bbaf14b330311ce75579668d26ce70e99c5aaec5141c924f5892&scene=21#wechat_redirect)

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