---
title: 【安全圈】苹果曝严重漏洞，可窃听用户与Siri对话
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652022381&idx=3&sn=d2bae64116e1ce9e3718607b683615a4&chksm=f36f8a2dc418033b8be6bc5ad4499c98a7e24cee411d21ba4a616b25f494b90b8d1cb50c096b&scene=58&subscene=0#rd
source: 安全圈
date: 2022-10-29
fetch_date: 2025-10-03T21:14:36.319798
---

# 【安全圈】苹果曝严重漏洞，可窃听用户与Siri对话

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgMgezksqZqUa9FQvY8HoQuXwOfic9huu8GWYmSpjqle50a1FnOzs3T9CdmMHFrFOR9KcVnicqqpTnA/0?wx_fmt=jpeg)

# 【安全圈】苹果曝严重漏洞，可窃听用户与Siri对话

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgMgezksqZqUa9FQvY8HoQukdmkLBPibmB8PfibicphI8fOJKGgjcGmleXiblQxWJ2zt238xoT1Hia6CPw/640?wx_fmt=jpeg)

**关键词**

苹果

据The Hacker News 10月27日消息，在苹果近期披露的漏洞中包含了名为SiriSpy的 iOS 和 macOS系统漏洞，使具有蓝牙访问权限的应用程序能够窃听用户与 Siri 的对话。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgMgezksqZqUa9FQvY8HoQuY33k4CIU0ngyAKqnB8ukjOuVX9O5OASqxGZ78PdibHttF54t7USYawA/640?wx_fmt=jpeg)

应用程序开发人员 Guilherme Rambo 在 2022 年 8 月发现并报告了该漏洞，编号为 CVE-2022-32946。

Rambo表示，在使用 AirPods 或 Beats 等设备时，只要请求访问蓝牙权限的都可以记录用户与Siri的对话。而该漏洞与 AirPods 中一项名为 DoAP 的服务有关，该服务用于支持 Siri 和听写功能，从而使攻击者能够制作可通过蓝牙连接到 AirPods 并在后台录制音频的应用程序，且不会显示麦克风的访问请求。

而在 macOS 系统上，该漏洞可能被滥用以完全绕过TCC用户隐私保护框架，这意味着任何应用程序都可以记录用户与 Siri 的对话，且无需请求任何权限。

Rambo表示，造成这一漏洞的原因是由于缺乏对 BTLEServerAgent 的权利检查，BTLEServerAgent 是负责处理 DoAP 音频的保护程序服务。

目前该漏洞已通过系统更新补丁得到修复，涉及的产品包括iPhone8及之后的所有机型；所有的iPad Pro；iPad Air 第 3 代、标准版iPad 第 5 代、iPad mini 第 5 代及后续机型。

来源：FreeBuf

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgMgezksqZqUa9FQvY8HoQuh5alS6nMne9wKBKeX2n3GvnfQNHqgVHTxmm9Tzr06pgTqz0sm0vUyQ/640?wx_fmt=jpeg)

# [【安全圈】程序员与同事吵架一气之下删代码离职，被判赔公司6万元！](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652022235&idx=1&sn=5e79780f6554ffd0580d056e177176a4&chksm=f36f899bc418008d1bda77be3a9556022fe253dbe0166762eaabc2ad271d859bd3bcefee9140&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgMgezksqZqUa9FQvY8HoQuoI3fKtOUgI2ibNp7Sp5nrguDhw9Eh065LYNDG1SuYNibD1m7yKQlVeCw/640?wx_fmt=jpeg)

# [【安全圈】云南网安部门打击一批营业厅“内鬼”](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652022235&idx=2&sn=47df439116fd32e28a932daad55057f1&chksm=f36f899bc418008d4a70302a35eb55d763bc5ffca57b7c7de63f198e60191da169016f38f7ec&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgMgezksqZqUa9FQvY8HoQuUOKeC6XtxeqjGLK42QXh3nMiaN8YAXPOOn0Osa3XJGcX6ic2jLY3GYnA/640?wx_fmt=jpeg)

# [【安全圈】专家披露 SQLite 数据库中存在 22 年的高严重性漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652022235&idx=3&sn=6193cb3add4ce6fae699a6771918e483&chksm=f36f899bc418008d47f3d6b0344e66837093e2c867432e869bb29bb1fd8075e3e4ff59ebe310&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgMgezksqZqUa9FQvY8HoQu2FbPzbuhWWOyhVcTv8ty3ic9tiaSMpv2xlTFtTdRNdjWz6doMbc9ha9A/640?wx_fmt=jpeg)

# [【安全圈】研究人员披露了 Windows 事件日志漏洞：LogCrusher 和 OverLog](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652022235&idx=4&sn=cfb34301af1f19c07a8acd30accd2c26&chksm=f36f899bc418008d23243738a5e4f1d460e754e57813111e2360aa1d95209b6cc66d5ca5b76a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

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