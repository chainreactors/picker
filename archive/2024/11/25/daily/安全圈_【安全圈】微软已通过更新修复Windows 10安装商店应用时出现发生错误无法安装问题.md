---
title: 【安全圈】微软已通过更新修复Windows 10安装商店应用时出现发生错误无法安装问题
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066203&idx=4&sn=fa5c5885a0aa428e589410762dd813ac&chksm=f36e7ddbc419f4cdd12380c085a00117007aeacb6e8ac0816c71f80f4a0aa82a15a7f149aff5&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-25
fetch_date: 2025-10-06T19:15:11.484264
---

# 【安全圈】微软已通过更新修复Windows 10安装商店应用时出现发生错误无法安装问题

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgicwSoN6OFceKicK0nlUjNuNLjBDwEalEvyfxIOw4k9NOicPJU9ibYmc1Dw7B2rp133QsQIGf2Q86cZw/0?wx_fmt=jpeg)

# 【安全圈】微软已通过更新修复Windows 10安装商店应用时出现发生错误无法安装问题

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

Windows

早前有用户发现在 Windows 10 上使用微软商店下载或更新应用程序时总是会出现错误，在提交反馈后微软确认这是某些必要的组件出现了问题。

根据微软在 Windows 10 健康仪表盘中发布的信息，此次问题的罪魁祸首是 WinAppSDK 1.6.2 版，该版本发布时间为 11 月 12 日。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgicwSoN6OFceKicK0nlUjNuNnuRVzXWXKtgQhy0sTZmbGAFR3ANjgsmaCaaAnrLeqsXwjNcHSjLnhA/640?wx_fmt=png&from=appmsg)

微软和其他开发商的部分应用程序都依赖 WinAppSDK，当执行下载安装或更新时微软商店会自动安装 WinAppSDK，由于这个组件出问题导致无法正常安装或更新。

甚至 IT 管理员通过 PowerShell 部署时也会出现部署失败和 0x80073CFA 等错误代码，所以这其实和微软商店也没有太大关系。

目前微软已经成功解决问题，微软表示已通过 11 月 21 日发布的预览版更新 KB5046714 进行修复，安装该更新后即可解决无法安装或更新的问题。

然而特别需要强调的是 KB5046714 为测试版更新，由于带有测试性质，除非用户主动检查更新否则不会安装，蓝点网也不建议用户安装测试版更新。

所以如果你经常通过微软商店下载安装应用那可以考虑安装该更新，否则应该等到 12 月 B 类稳定版更新发布，避免测试版更新安装后带来新问题。

最后微软还特地强调此问题并不是之前发布的累积更新带来的，所以也无法通过卸载更新的方式解决这个问题。

来源：https://www.landiannews.com/archives/106749.html

***END***

阅读推荐

[【安全圈】2024年10月涉国内数据泄露事件汇总](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066187&idx=1&sn=9cc9b36e4ddc3b1dc9c32f5d2235fec4&chksm=f36e7dcbc419f4dd7011a0a372ec2fb83585e6ae8913861e0b1ce62bcbf984c05d4992a32cb5&scene=21#wechat_redirect)

[【安全圈】被曝“发涉黄短信给准爸爸”，两家母婴APP公司回应](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066187&idx=2&sn=942b5fec79538a5d2fb8230633811d4a&chksm=f36e7dcbc419f4dd0e0ed1a36ee32cf749e3b64764ce18009ae0dfb577de8dfea3a7a0aa4500&scene=21#wechat_redirect)

[【安全圈】福特否认遭黑客入侵：车主信息安全](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066187&idx=3&sn=8313356546d83f1f3742bdc6675ac74c&chksm=f36e7dcbc419f4ddfd2a3baaae626b473388bf992926652b55854deeec81c156fd8cb954f488&scene=21#wechat_redirect)

[【安全圈】D-Link忽视旧款VPN路由器补丁更新，关键漏洞未修复](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066187&idx=4&sn=c4be9926d771d2293619bbe2dcc12b29&chksm=f36e7dcbc419f4ddb491db67e4fc6ec1515f6d7f688561be3515419ed7095a39ba6fc3b91bf9&scene=21#wechat_redirect)

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