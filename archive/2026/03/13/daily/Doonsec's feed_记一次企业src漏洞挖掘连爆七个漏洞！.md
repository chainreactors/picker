---
title: 记一次企业src漏洞挖掘连爆七个漏洞！
url: https://mp.weixin.qq.com/s/2QDd_lNpsYjG16wxxWteKg
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:11:00.118515
---

# 记一次企业src漏洞挖掘连爆七个漏洞！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2I159AwKj54eoicnsY5m8ic95WdYF4jUXAxXM8u72nZWcwSw2FLVtygKhYKwaXXfsnY1hHCkLCBSbkpwhYQuqM7KarIBHHEOuDicicoFNyYT15I/0?wx_fmt=jpeg)

# 记一次企业src漏洞挖掘连爆七个漏洞！

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器中沉浸阅读

自从上一篇作者开发的yakit漏洞自动检测插件介绍后，作者又开启插件进行了企业src的漏洞挖掘之旅，此次挖掘竟然连爆7个漏洞，作者自己都没想到插件竟然这么给力！

接下来就详细介绍作者是如何通过yakit启动自研插件挖出七个漏洞的！

第一步——代理设置，开启插件     （会的师傅们可以跳过）

浏览器设置好代理，使用浏览器插件 SwitchyOmega 设置代理为 127.0.0.1：8080 ，让浏览器的流量经过本机8080端口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavFvxSwLtq95l4MqrheH21re34kOn05icKXK5XchfcGMIw4VUa2NgCIHw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

浏览器插件安装：浏览器右上角三点——扩展——应用商店——搜索框搜索SwitchyOmega——安装

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavDHEiaviatR2ic0MH6TYr0y65nKeguGmxS5vYWSkl6ichbOCC2icK93yDUwQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

第二步——yakit开启监听

yakit中创建一个项目打开，在如下界面设置监听本机8080端口——点击启动劫持

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaav8ehRYDiaA6iaT718wYoOmGPutlE4rfO8lCKofWH1EibQSZlufS5WFGP8g/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

来到抓包界面——选中作者的插件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavyMrMyh78pmQseTG13X6jTbMJSA3RerOQfu5E6okjo8BO8tVElniaJcg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

此时即可开始漏洞挖掘，对目标做信息收集，然后在浏览器“点点点”目标网站的功能点触发流量，yakit获取流量后插件就会对所有流量进行漏洞检测。

漏洞检测结果会展示在此处

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaav9oFljhSXVAHbEBuyLHwVeWmsGSZZytIBFU3CKia3BUWiabmfpa6enhpA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

七大漏洞！

一、被动目录扫描插件发力——登录接口弱口令

被动目录扫描插件爆出了一个登录接口，于是尝试test/test成功返回token。目前已修复

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavHibqkX54q87pjeEweVXWa86bG9eSgXxKwYSfFSrJIrSaXRj58LDvuxw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

提交通过

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavsrf6kfNXm7cMjkGtAR8fXyMrt2KSFic2hL2MztyqKlht6W4FwrRKf9Q/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=6)

二、fuzz立大功——管理员账户创建接口（已修复）

上一个漏洞发现接口\*\*\*/\*\*\*/login  就思考会不会存在其他接口于是对 /login 进行fuzz，成功爆出创建管理员接口：\*\*\*/\*\*\*/RegisterManager

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavXwOYlWKiap5OjW042BIMLKoPOLtT0GTQ39zMSan7X2Uedmhvr5T9lqw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=7)

成功创建管理员

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaav8dnZvodMJamwfaAwISoSicpwyWeaaQTsgibracYMWXRwJhmkN2ndqSfg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=8)

三、被动目录扫描插件再现奇迹——swagger接口泄露，可控制所有接口！（已修复）

查看漏洞结果发现/swagger/index.html目录泄露

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavsrm4xHfXueAbDNzEQtsQRTQxFicvQWozcxxRibCDgJjxlUiaFlibhpKn8g/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=9)

访问发现里面有所有接口泄露，且全部可控。如：创建管理员、登录、获取用户数据等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavPW7vKHvM6t1RZmic7XxGlyqribwgBzFBkxr8Ca8OAzf9D05WrbTXRRwQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=10)

最后因为无法找到接口对应网站功能点，严重级别的漏洞只给了中危，我tm哭死

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavaA8MsD6bObtAuMGWSYDtFXeP0ibl4gPPHmicW95vVozibm665WGJvgVlQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=11)

四、被动xss扫描插件展现神力——反射型xss

就是复现一下，就不细说了。全靠插件发力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavIu9hkYMgCvb2dAbe8GCAkoK5tUlGx8LFnKUOYhxNZoicJM6SJlfHE7g/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=12)

成功通过

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavtzDPaxIm6PXM8IuzuAB6ViceOVwpEMvHH403GNQp59nju2Q49TvqOpg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=13)

五、作者发出神力——url重定向

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavUj312ms3rBmaN22ia3sgS2YkicqCwckLnbn841Bkg8503Xu6lE7Qf2LQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=14)

成功得吃

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavjrwd2KYxZbzYV6UD5WicjNQWep1dmEShpOm7WjiaAwtwwXDxyMuKluMg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=15)

六、被动sql注入检测插件奇迹再现——两个sql注入！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavnCCS1cr279cicsBRRWCNuN2l1Ecoqic6wYwjY0yPyibNqNo4qBXTqQakw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=16)

复现成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavjgqboaZqXWhGAm1dBFTibUKaBAlywPoFITjfY9BIrUZcOeIq8TmQNNA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=17)

得吃

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9ibb0kbHCImmI8E9Zf6JqGRia9JWljiaavFZTFpskKstp5ez3yTuSCr6n73OTuPu6odgSibIWkhvhF92EOo7bPykQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=18)

以上漏洞都是不需要任何技巧的，作者只是开启插件在目标网站用鼠标“点点点点”就挖掘出这么多漏洞，完全“零基础”“零成本”挖洞目前一共开发了四个插件：

被动sql注入检测

被动xss扫描优化版

被动目录扫描好人版

被动ssrf及log4j检测

插件使用教程：https://mp.weixin.qq.com/s/vQ9r86AwmxKAyZnb3t1FLw

内容来源：小黑子安全，侵删

![图片](https://mmbiz.qpic.cn/mmbiz_gif/VwaIJp80uug4IfOOz8QDT8hlhwrxRjonkLYs9zAzodxhicEqQFaVRO6RZJ6pjx3x9752hoicFhHlmld2znUIqmSA/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

3月技能成长计划

🌱 3月技能成长计划，今日重磅开启！

🔥 7天限时狂欢，三重好礼等你来拿！

🎁 报名即享：最高立省4700元，加赠实战专题课 + 钻石学习卡 + 京东卡/瑞幸卡（二选一）

🎁 直播福利：免费领取《2026面试宝典》，助你职场先人一步

🎁 推荐有礼：邀好友报名，得大额京东卡，多推多得！

⏰ 活动时间：3月12日-3月18日

👉 立即私信老师，锁定好礼名额！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2I159AwKj54EmMJ7PQzS4yUxQpvvTX80y4DRdCuv67jibfJvLgbVkyFkgnnnmvj2SjAWrS9SSYkh0Offonm6HM5WfQkgQRebeNVibzuib2b9Ww/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnzUZSPvXhVfSqMdycgzQNticibKVKkmlzZLP2DUgwGgOicCNjooP2mY2cSjhia7tW2SPpJ14Ued1q6eg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

马哥网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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