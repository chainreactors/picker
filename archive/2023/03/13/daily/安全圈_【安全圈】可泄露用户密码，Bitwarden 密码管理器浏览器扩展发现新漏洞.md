---
title: 【安全圈】可泄露用户密码，Bitwarden 密码管理器浏览器扩展发现新漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031340&idx=3&sn=73911b694d2e53db282bfe93cef755de&chksm=f36fe52cc4186c3a007f7f3c136204f30ef44e3ceb2759c8263e96fbc618ed02036a25237da9&scene=58&subscene=0#rd
source: 安全圈
date: 2023-03-13
fetch_date: 2025-10-04T09:25:37.787358
---

# 【安全圈】可泄露用户密码，Bitwarden 密码管理器浏览器扩展发现新漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdeviciaEnavPMeic0zELr31fLoicCCG7L3zqiaC97HicPxvAiaDiaWSajsmskCicaRA/0?wx_fmt=jpeg)

# 【安全圈】可泄露用户密码，Bitwarden 密码管理器浏览器扩展发现新漏洞

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgSxa9I02IBd3bgLEhwfJCeRibw3LEjMujeAhD2CvyiaVCZJVHGHODbkPx3pViaX0sAibZsDun6sicUzdQ/640?wx_fmt=jpeg)

**关键词**

泄露密码

3 月 11 日消息，根据安全机构 FlashPoint 官方博文，在密码管理器 Bitwarden 的浏览器扩展程序中发现了一个高危漏洞，可以泄露用户的密码信息。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdevicmFNZdIFHvgYzVI2f49uGICsnKfQ6p0ScTl4P04iaYwKsAJHguhoiaT5A/640?wx_fmt=jpeg "可泄露用户密码，Bitwarden 密码管理器浏览器扩展发现新漏洞")

恶意网站可以利用该漏洞，在受信任页面中嵌入 IFRAME 代码。用户访问这些恶意网站，并使用 Bitwarden 自动填充之后，就可以获取用户的凭证信息。

IT之家从博文中获悉，导致这个漏洞的关键是 Bitwarden 以非典型方式处理网页中的嵌入式 iframe。

浏览器通过同源策略，分开 iframe 嵌入页面和父页面。也就是说，iframe 嵌入页面和父页面应该是互相隔离的状态，无法访问其内容。目前包括 Firefox、Chrome 等主要浏览器均采用了这个安全概念。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaZsw4TlOII3OcgaLcCdevicx3TYlZCPBthMJfCht9wnAgaibDODnu7yKicnj5fdkgYOnuZwsozrShDQ/640?wx_fmt=jpeg "可泄露用户密码，Bitwarden 密码管理器浏览器扩展发现新漏洞")

Bitwarden 浏览器扩展还在通过 iframe 嵌入来自其他域的第三方内容的页面上使用自动填充功能。通过 iframe 嵌入的网页无权访问父页面的内容。

但安全研究人员写道无需进一步的用户交互，该页面可以等待登录表单的输入，并将输入的凭据转发到远程服务器。

Bitwarden 文档确实包含一条警告，即“受感染或不受信任的网站”可能会利用此来窃取凭据。安全研究人员表示，如果网站本身受到威胁，扩展几乎无法阻止窃取凭据。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgwpW04ibSvlmWjNp8eUM0KFHibf3ZAicuClNcV7HhVGBuOIWU8T01j8cLWMOpR8icprkLkdSPgjALNzA/640?wx_fmt=jpeg)[【安全圈】“帮信罪”正式成为我国第三大罪名，大量学生涉案](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031256&idx=1&sn=fff4bbbf1ca96280bf5794293e1e3288&chksm=f36fe558c4186c4ee4c48bcd624b01cf312a57f6c3dab75118e4936afbf05c45ae61a7361b79&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgwpW04ibSvlmWjNp8eUM0KFnib6B33c71phvzw56Tb9sibaPu7GMicI0yJSoYKSXQ6y5etN704yXfSibQ/640?wx_fmt=jpeg)[【安全圈】可绕过 UAC，微软 Win10 / Win11 系统中发现高危漏洞：可安装执行恶意软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031256&idx=2&sn=8cb3a0990860352ef0335b43b556dc4b&chksm=f36fe558c4186c4e66969bb745657d7543dc5e5f0a05b8777fbd8612e77288657f8e4fd9521e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgwpW04ibSvlmWjNp8eUM0KFHVD4HNSdHNvdsnjc12fI6FMtBhWK1NfgNvQmhMb2zXRBUDlQZe1Iww/640?wx_fmt=jpeg)[【安全圈】已对 Linux 服务器发起攻击，针对 Win10 / Win11 的勒索软件 IceFire 出现新变种](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031256&idx=3&sn=bd432c9dc0e56d5a649853c38afbb35f&chksm=f36fe558c4186c4edb19d958a91a31a116849adfc5c67934ff96a6e0d0723fcde9ef62d1ed70&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgwpW04ibSvlmWjNp8eUM0KFfL4qFa1Wx5XAe7SkFqoqic8Hqv6S3gZTYfIWC9AauDQUVVfZia6kiaR9g/640?wx_fmt=jpeg)[【安全圈】被指与谷歌形成“双头垄断”，苹果辩称英国监管机构已无权发起调查](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031256&idx=4&sn=7448fdfd960f1f740ac53593c365dedc&chksm=f36fe558c4186c4e4b69ab3de74151c60ade89dd81141d8b01ad591e326a775787b9db4b3387&scene=21#wechat_redirect)

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