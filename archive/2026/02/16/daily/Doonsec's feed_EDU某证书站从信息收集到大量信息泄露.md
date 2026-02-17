---
title: EDU某证书站从信息收集到大量信息泄露
url: https://mp.weixin.qq.com/s/G5BnSXSa-UTdSiMY_m9cFA
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:17:55.736471
---

# EDU某证书站从信息收集到大量信息泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibeMgKhFUfbSUrVcprodTG6Ougw1zFjVbGazQTal8oKSRErO96HyibrDUvysmtwPeql3rfQckttUeumYVaO4z0XYRibKpMz5A9QLe9m04zZsdk/0?wx_fmt=jpeg)

# EDU某证书站从信息收集到大量信息泄露

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于狗窝集团
，作者Mave

![](http://wx.qlogo.cn/mmhead/XxT9TiaJ1ibf0qZutX7PMqWFGhumvzI9C7lpC2SZYlVm2AkPQzOvHh3sNNxg9FicJibu1PWdKUva4Ig/0)

**狗窝集团**
.

漏洞挖掘学习+MimIdoGo-\_- 狗窝集团官方账号，EDUSRC年榜第一团队，不定期技术分享，欢迎关注。

**春节快乐**

**狗窝集团祝大家**

新春快乐✨ 祝大家：马年护网顺顺利利，0day挖到手软，CTF冠军拿到不停，漏洞无处藏，荣誉常相伴！

**引言**

在多数edusrc挖掘中，核心的资产大部分已经被大手子挖掘干净，如果我们想捡漏，则需要根据目标的边缘资产下手。这句话我相信大家已经听腻了。 大家可能更会想，到底什么叫边缘资产？怎么去发现边缘资产？本例给大家举一个简单的例子，大家可以一举反三，多多思考。

**Part.1：如何去寻找边缘资产？**

此例我们是在公众号里发现的一个资产，我们以北京大学举例；打开天眼查，我们可以看到知识产权-微信公众号里，有众多的资产可以去测试。当然，根据时间，一些公众号可能会过期无法再搜索/使用到

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbRB4LG09GAyhOEdHVJP8ibJ73RHpckNia47UKbAoEibnWy7x2ianCjIQqv60lZDm6KRAHpmMmRF3fd4kTSy6maa7MQTq80ibTNY2APo/640?wx_fmt=png&from=appmsg)

然后我们再打开企查查，发现比天眼查资产还要多。还有众多类似的软件，我们可以进行查漏补缺。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbT1gjxJVI493MftBYp72vOdRcoHJzy72tm0qNgmeiaDAEC6Fmz23GqiaauEyl9L8iaIRwPjG2rLDmx5vbAWPXeynadkb9VygR9USU/640?wx_fmt=png&from=appmsg)

icp查询：这里可以查询到所有北大备案的网站以及app/小程序等

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbTZLyGuAsapVqfGInjEycs9V0ibW33jTJpYQeFKL2AK7AiaALAscQI3cicDibMXsE01aMn4iarKOBxz52CjvaWvz1RGA7GmLN9RO3vg/640?wx_fmt=png&from=appmsg)

**Part.2：对目标进行测试**

找到资产后，由于我们没有学生的账号密码，所以我们要去观察数据包，以及去尝试有哪些功能点可以在未登录的情况下进行使用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbSUrxibEFY8PlU0GOtFxP9Vxn4qGHaYNnOqBKTHMC9vpczlM3sR9LEk6vMWeib5yKo8nGOQ2jlDzoXSnfaRibCn1ChibiabL2yUakTw/640?wx_fmt=png&from=appmsg)

发现了泄露管理员的手机号（但目前找不到利用方式，所以先记一下手机号）

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbTGye7DrdXF0gcE0EDDEgpGd8b2mgribbvcNZf8YeOrx5vy8rEjvHAZIiagibQo3gx54C8Kia5Iia0OppI4B2AibhZpEddD4gPhledmI/640?wx_fmt=png&from=appmsg)

在请求包中发现了一个uid=1，这里尝试了越权、注入等。都没有漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbQibOWzDKKwcd9gcZ1RsmflBZCFcUhg3zhovXjHcZMMZE25zdXFZ2SMo4t2wOXlqU3NVZATaDQo2t9wC1RnT0SeIBuoO4XzZgzk/640?wx_fmt=png&from=appmsg)

这种情况我们可以试一下置空参数里的内容，置空以后，发现了非常非常长的数据包，甚至bp都卡死了。而且是经过base64编码的内容。

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbRf7z70iarCYu0EWuGplUgWJiajwG8uAlWqyWCGqj8N2FKZhVEOmic1LZvBeVuDntPIP7fn0RlRkZEibLNoI7doZBxRB2GypDegCGs/640?wx_fmt=png&from=appmsg)

由于数据太过于庞大，所以随便先复制一小段，去解码。

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbTCgreaomn8haWOs1FCbyWFjdTVmC1NhrcXvQcssmZ2ibfLLM4dffNaTqYxFlPQcnibYLX0BjicND3GvsFic7O3TpDicibicibKjicKicCqo/640?wx_fmt=png&from=appmsg)

还记得我们第一步记住admin的手机号吗。我们去尝试一下。

至此拿下泄露7w sfz数据。

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbRmfzrqLicy0dt98twPOiau7Ay72KO5p92J0PxZS1uJfBmibe1U68UhbDSDhoA9gvl1tvCtK1ANGHpEwiapM99LxbKGGIy1xONmkz4/640?wx_fmt=png&from=appmsg)

**Part.3：对已有信息进行利用**

数据包中存在类似于用户cookie的信息段，所以我们尝试登录时，是否能替换信息，达到越权登录。

内容里还有guid，经过抓包替换后。成功越权，此界面为两个管理员

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbT9Wib1SIIMdXibk78UDaIAnC7Uw52tGEnmqyVlupx9Tib1GyShic9zuX0ia0Y4uZQnpdkTXGF6Ax79rJyiajhicUc9iaY2ApWnLryicOaE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbSv1EtU4kf0Q3U3MRZzEqJKlIHEkdibCdEh257xOj7ia4klSKl4t1w0lM1icyYWZGWialc79tKJRsI8LyZGRcLye9Wlj5sLic5pheDs/640?wx_fmt=png&from=appmsg)

上传头像这里我们可以尝试看看对上传点有没有限制

可以上传，但是无法解析。访问后直接就成下载到本地了。

既然对后缀名没有限制，那么我们可以尝试上传标签事件，看一下是否能解析确认能解析再尝试xss语句

（忘截图了，数据包还存着）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbT8btyCfVx5ibz962LgrztYXlWsbO5sP2faHAZklluzHqvcYOVvXRggEMSsHiaMkHuZR3wlBXeCvia81RkK78bEwzMkE4mwEjlqQE/640?wx_fmt=png&from=appmsg)

可以解析。所以上传xss

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbT5puSMzpJnMX9YKrkV9VV9OicafAlKUvjN4jEejtia3Cl9ibp3mWMpD5MRQQwgK6KRAuOKYO0vWIAQXLTqooOS9ibTIV8dHwRfJKg/640?wx_fmt=png&from=appmsg)

上传成功后再访问，成功弹窗（羊肉串真好吃）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbSkeHzgMibg63IPsXYicLibuZSUWsPR3kfh8NwUibfNhlJqgGsRyAudWqciagzkWU2uV9xN0aMLetXmvMZFXuyUlAA5a4zEuMeHaH9o/640?wx_fmt=png&from=appmsg)

---

最后找了一个小目标，id可以遍历，但单独不收，打包一下加进去

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbQBeSV812ckTpTY92UKRpbkeBe3GOzdLbSN7iaTTVdutq8HUgr59sh0LA45qbQYEIqcxLWiczvSC7juiczrJu1OUblyxPBzY3rnAc/640?wx_fmt=png&from=appmsg)

最后也是成功的拿下了7RANK高危。

**END**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

sec0nd安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

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