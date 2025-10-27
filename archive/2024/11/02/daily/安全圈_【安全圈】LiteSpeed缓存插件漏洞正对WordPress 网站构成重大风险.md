---
title: 【安全圈】LiteSpeed缓存插件漏洞正对WordPress 网站构成重大风险
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065645&idx=3&sn=77a3bd1b9376d22214d1764a39ccbcfb&chksm=f36e632dc419ea3bc182f81324976058181f1909b7d1d7eaf616f592b4eb130862a2bf5c8242&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-02
fetch_date: 2025-10-06T19:17:53.455533
---

# 【安全圈】LiteSpeed缓存插件漏洞正对WordPress 网站构成重大风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhg5zYLLv7B6zRhpLQO8FXjFjcpT9HXyVXXd2Hzq9lO9VaJxWv0lITgEctshtZxHOJJVjHLWPus2Q/0?wx_fmt=jpeg)

# 【安全圈】LiteSpeed缓存插件漏洞正对WordPress 网站构成重大风险

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

WordPress 一款流行插件LiteSpeed Cache 的免费版本最近修复了一个高危的权限提升缺陷，该漏洞可能允许未经身份验证的网站访问者获得管理员权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhg5zYLLv7B6zRhpLQO8FXjm4E8iamY5H7u8HhWBw0052U7ABE6Wj7lOkxVotDNVsqGdDnnuc9TNTA/640?wx_fmt=jpeg&from=appmsg)

LiteSpeed Cache 是一个缓存插件，被超过 600 万个 WordPress 网站使用，有助于加速和改善用户浏览体验。

新发现的被跟踪为 CVE-2024-50550 的高严重性漏洞是由插件的“角色模拟”功能中的弱哈希检查引起的，该功能旨在模拟用户角色，以帮助爬虫从不同的用户级别进行站点扫描。

该功能的函数 （'is\_role\_simulation（）'） 使用存储在 cookie 中的弱安全哈希值（'litespeed\_hash' 和 'litespeed\_flash\_hash'）执行两个主要检查。但是，这些哈希值的生成具有有限的随机性，因此在某些配置下是可预测的。

要使 CVE-2024-50550 可被利用，需要在爬网程序中配置以下设置：

1. 运行持续时间和间隔设置在 2500 到 4000 秒之间。
2. 服务器负载限制设置为 0。
3. 角色模拟设置为 administrator。

Patchstack 的安全研究员称，尽管哈希值有 32 个字符长度，但攻击者可以在 100 万种可能性的集合中进行暴力破解。

成功利用此漏洞的攻击者可以模拟管理员角色，这意味着他们可以上传和安装任意插件或恶意软件、访问后端数据库、编辑网页等。

10 月 17 日，供应商 LiteSpeed Technologies 在插件的 6.5.2 版本中发布了针对 CVE-2024-50550 的修复程序，提高了哈希值的随机性，并使暴力破解变得几乎无效。但根据 WordPress.org 下载统计数据，自补丁发布以来，大约有 200 万个网站进行了升级，仍有 400 万个网站暴露在漏洞中。

## LiteSpeed 的安全难题

今年对于 LiteSpeed Cache 及其用户来说是多事之秋，因为这个流行的插件出现了多个关键漏洞，其中一些漏洞被用到了实际的攻击事件中。

2024 年 5 月，黑客利用具有未经身份验证的跨站点脚本缺陷 （CVE-2023-40000） 的过时版本的插件创建管理员帐户并接管站点。

2024年 8 月，研究人员发现了一个关键的未经身份验证的权限提升漏洞 （CVE-2024-28000），警告其很容易被利用。在披露后的几个小时内，攻击者就发起了大规模攻击，Wordfence阻止的恶意尝试次数达到了5万次。

2024年9月，该插件还修复了一个漏洞（CVE-2024-44000），该漏洞能导致未经身份验证的帐户接管。

参考来源：LiteSpeed Cache bug exposes 6 million WordPress sites to takeover attacks

***END***

阅读推荐

[【安全圈】Elasticsearch开源仓库被员工误操作导致404，star数降至200](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065627&idx=1&sn=61e47ac47c9242c637c2aa9b44d51b93&chksm=f36e631bc419ea0dcf3e8fa63adebc61d821b335b96559939e9877b257949339fd5b29f4f12e&scene=21#wechat_redirect)

[【安全圈】俄罗斯对谷歌罚款达35位数美元](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065627&idx=2&sn=4fe87be42db4f7bd6c120220c63b3789&chksm=f36e631bc419ea0d6d03219698da5af032f854fc534c15d1fad24232fbe7ff5d8df1a3a0e461&scene=21#wechat_redirect)

[【安全圈】能伪造通话界面，FakeCall恶意软件变种在安卓手机中传播](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065627&idx=3&sn=926f2a6b02eef61e44cd08f8b9f22c6f&chksm=f36e631bc419ea0d1c7712878321bfaa133b49e743351111cb64d7c9e7e24dcf2e222e84435f&scene=21#wechat_redirect)

[【安全圈】遭勒索攻击后，秘鲁国际银行承认数据泄露](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065627&idx=4&sn=8a3d913bcc8725a32a125c6d89267811&chksm=f36e631bc419ea0d3ad4b4e311f88b3b4f899a989e780ec4027898600d3a2f8f3ed743836bf8&scene=21#wechat_redirect)

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