---
title: 【安全圈】思科安全设备ASA十年老漏洞正在被利用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066407&idx=3&sn=26ea707878614e9c3a2395f4334a3b4c&chksm=f36e7e27c419f731e6dac2fb2ce42e4931eb3dd86c6fa19bbeb2be2bb63870488d6f36224aed&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-05
fetch_date: 2025-10-06T19:38:54.632814
---

# 【安全圈】思科安全设备ASA十年老漏洞正在被利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgPwOGp0Z0tQfy1NqUD8SN8f9ItxVliceuo4IPQ7CKvepLCSJdRqYEzGbfFGZy0MIbrHO1FDkicFTMw/0?wx_fmt=jpeg)

# 【安全圈】思科安全设备ASA十年老漏洞正在被利用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

近期，思科系统公司（Cisco Systems）更新了关于CVE-2014-2120的安全公告，警告客户该漏洞已在野外被利用。CVE-2014-2120是一个影响思科自适应安全设备（ASA）软件的WebVPN登录页面的跨站脚本（XSS）漏洞。该漏洞最初于2014年披露，它允许未经身份验证的远程攻击者对WebVPN用户执行XSS攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgPwOGp0Z0tQfy1NqUD8SN8o2b4ZxYLNMklRVo6FNa7YKuyjpXEUM17SCO23HP2VNygNExypRJSIA/640?wx_fmt=jpeg&from=appmsg)

### 漏洞详情

CVE-2014-2120漏洞源于WebVPN登录页面对一个参数的输入验证不足，攻击者可以利用这一点构造恶意链接，当受害者访问这些链接时，会在其浏览器中执行任意脚本。这种攻击可能导致攻击者在用户的浏览器上执行恶意代码，从而窃取会话令牌、修改页面内容或重定向到恶意网站。

思科在其更新的安全公告中强调，利用此漏洞的攻击活动已经出现，因此迫切需要立即采取缓解措施。公司强烈建议客户升级到已修复的软件版本以修复此漏洞。然而，思科也指出，对于通过安全通知披露的漏洞，将不会提供免费的软件更新。客户需要通过常规支持渠道获取必要的软件升级。

此外，网络安全和基础设施安全局（CISA）已于2024年11月12日将CVE-2014-2120添加到其已知被利用漏洞（KEV）目录中，进一步强调了组织解决此漏洞的紧迫性。

### 具体漏洞利用手法

思科自适应安全设备（ASA）XSS漏洞的具体攻击手法如下：

1. 注入恶意脚本或HTML：远程攻击者可以通过向一个未指定的参数注入任意的Web脚本或HTML代码，利用该漏洞。

2. 利用用户输入：由于WebVPN登录页面未能正确验证用户输入，攻击者可以构造包含恶意脚本的输入，当这些输入被页面错误地作为脚本执行时，就可以实施XSS攻击。

3. 会话劫持和信息泄露：攻击者可以利用XSS漏洞窃取用户的会话令牌、修改页面内容或重定向用户到恶意网站，进而进行会话劫持和敏感信息泄露。

4. 脚本注入：攻击者通过将恶意脚本注入到网页服务器中，并在用户访问时执行这些脚本，达到攻击目的。这可以通过多种方式实现，如在输入框中提交恶意代码，或者构造特殊的URL以触发JavaScript执行。

5. 反射型和存储型XSS：反射型XSS是指攻击者诱使用户点击一个链接，该链接包含恶意脚本，当用户点击后，脚本会在用户的浏览器中执行。存储型XSS则是将恶意脚本存储在目标服务器上，如在论坛帖子或用户评论中嵌入脚本，当其他用户访问这些内容时，脚本就会被执行。

6. 利用Cookie和Session：攻击者可能会尝试通过XSS漏洞获取其他用户的Cookie，以此来冒充用户身份或执行其他恶意行为。

综上所述，CVE-2014-2120漏洞的攻击手法主要涉及在WebVPN登录页面注入恶意脚本，利用用户输入的验证不足，以及通过脚本执行窃取用户信息或执行其他恶意行为。

鉴于CVE-2014-2120漏洞已被证实在野外被利用，所有使用受影响版本的思科ASA软件的用户应立即采取行动，升级到最新的安全版本，以保护其网络不受此漏洞的影响。

***END***

阅读推荐

[【安全圈】知名开源监控系统Zabbix存在SQL 注入漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066393&idx=1&sn=ac63bf158d1e3e33b69fbab49a5ae214&scene=21#wechat_redirect)

[【安全圈】湖南网信办对某公司因数据泄露开出20万罚单](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066393&idx=2&sn=e4d7346c9f48f96841de32189c2af0d1&scene=21#wechat_redirect)

[【安全圈】因软件更新，丹麦第一电信运营商宕机超过24小时](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066393&idx=3&sn=4bd4e17312fffb19d18d2c8dd94b44f1&scene=21#wechat_redirect)

[【安全圈】新型恶意软件能利用LogoFAIL漏洞感染Linux系统](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066393&idx=4&sn=b1e7b15689fa221569f9a1cad7eff071&scene=21#wechat_redirect)

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

阅读原文

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