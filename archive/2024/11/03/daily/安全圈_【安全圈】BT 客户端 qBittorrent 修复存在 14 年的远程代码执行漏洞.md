---
title: 【安全圈】BT 客户端 qBittorrent 修复存在 14 年的远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065679&idx=3&sn=837c6f8a05d0deea042a4571a86897f5&chksm=f36e63cfc419ead9175f76caac71a824f76895371f4158517fdb542330ffeab1b09ddf1652de&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-03
fetch_date: 2025-10-06T19:15:57.558311
---

# 【安全圈】BT 客户端 qBittorrent 修复存在 14 年的远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljJdXPf2sIfkicUOFUC21J3XibhA028fGNmh6icoleIf6QdffGQVSmT6sQjdrUtUb9FHmz26f9PwgiaZA/0?wx_fmt=jpeg)

# 【安全圈】BT 客户端 qBittorrent 修复存在 14 年的远程代码执行漏洞

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

科技媒体 bleepingcomputer 于 10 月 31 日发布博文，报道称知名 BT 下载客户端 qBittorrent 修复了已存在 14 年的中间人劫持 / 远程代码执行漏洞。

该漏洞最早可以追溯到 2010 年 4 月 6 日，官方于 2024 年 10 月 28 日发布的最新版本 5.0.1 中修复，时隔超过 14 年。

注：该漏洞是由于应用程序的 DownloadManager 组件未能验证 SSL / TLS 证书所导致的，而该组件负责管理整个应用程序的下载。

虽然漏洞已修复，但安全研究公司 Sharp Security 指出，qBittorrent 团队未能向用户充分通报此问题。

Sharp Security 指出，未验证 SSL 证书的情况引发了多项安全风险，主要包括以下 4 个风险：

* 恶意 Python 安装：在 Windows 上提示用户安装 Python 时，攻击者可替换为恶意安装程序。
* 恶意更新链接：通过硬编码的 URL 检查更新时，攻击者可替换更新链接，诱导用户下载恶意软件。
* RSS 订阅被篡改：攻击者可拦截 RSS 订阅内容，注入伪装的恶意链接。
* 内存溢出漏洞：qBittorrent 自动下载的 GeoIP 数据库可能被伪造服务器利用，导致内存溢出。

安全研究员指出，中间人攻击在某些地区可能更为常见，用户应尽快升级到最新版本 5.0.1，以确保安全。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljJdXPf2sIfkicUOFUC21J3XlZsxzKjwmSzkrCT3YKbznjIdiaZ7NhmiauSzlQD01CLEfTNttPQqptDA/640?wx_fmt=jpeg&from=appmsg)

***END***

阅读推荐

[【安全圈】涉案金额超1.2亿元！四川南充仪陇公安破获一起黑客犯罪案件，打掉4个团伙](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065645&idx=1&sn=2fb1b8f5f82f536755b355cb879a8c73&chksm=f36e632dc419ea3b4800e39a56293b3ca75b526c377128094b9be6b4248c627bf71ad270c7c3&scene=21#wechat_redirect)

[【安全圈】热门摄像头曝零日漏洞，黑客借此入侵政府部门](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065645&idx=2&sn=77c5717f51ce4ad0db60c17c295d7d49&chksm=f36e632dc419ea3be15c455ff9750d3f460e878279abe47483f01b516b7e909fe59e89ff21b7&scene=21#wechat_redirect)

[【安全圈】LiteSpeed缓存插件漏洞正对WordPress 网站构成重大风险](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065645&idx=3&sn=77a3bd1b9376d22214d1764a39ccbcfb&chksm=f36e632dc419ea3bc182f81324976058181f1909b7d1d7eaf616f592b4eb130862a2bf5c8242&scene=21#wechat_redirect)

[【安全圈】新型修狗网络钓鱼工具包横扫英国、美国、日本和澳大利亚主要领域](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065645&idx=4&sn=c2a9b2d48e0a7adc5f381ff3efb11771&chksm=f36e632dc419ea3b671836b99abecba9d7b9a30e7ed68d964cbe890a22b90e0841ac8048ddf8&scene=21#wechat_redirect)

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