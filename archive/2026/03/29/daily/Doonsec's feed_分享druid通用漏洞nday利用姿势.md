---
title: 分享druid通用漏洞nday利用姿势
url: https://mp.weixin.qq.com/s/KVCBM9ozbhMak8PaXSPsDw
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:44:10.796556
---

# 分享druid通用漏洞nday利用姿势

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QVllOZY32NdLMs7liczkqt1OKyOtRa2c65ZvynlO4Lwmg46s9PunetqndAHFyBIyN5M2cSdXxH276ozzzpWGChDcnepoBAibNBYA/0?wx_fmt=jpeg)

# 分享druid通用漏洞nday利用姿势

原创

神农Sec
神农Sec

神农Sec

![]()

在小说阅读器中沉浸阅读

课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。

#

01

0x1 分享druid通用漏洞nday利用姿势

## 0x1 druid资产搜索

Druid monitor页面渗透技巧是一个非常好用的数据库连接池

有URL Session Spring监控

Druid是阿里巴巴数据库事业部出品，为监控而生的数据库连接池。Druid提供的监控功能，监控SQL的执行时间、监控Web URI的请求、Session监控。当开发者配置不当时就可能造成未授权访问。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUtib4rILeH8nhGJTTZlzpb5a79e3iaHTFpNJOeGgyWDwlWSbHXoQytCLUfnxaUkOclLFHmmps4PBTzLMibcNBxCekyKjkYvATfHE/640?wx_fmt=png&from=appmsg)

img

| 目标 | 推荐 FOFA 语法 |
| --- | --- |
| 通用 Druid 监控 | `title="Druid Stat Index"` |
| Apache Druid 实例 | `title="Apache Druid"` |
| 未授权访问检测 | `inurl:"druid/index.html" && title="Druid Stat Index"` |
| CVE-2021-36749 影响范围 | `title="Apache Druid" && body="Load data"` |
| CVE-2021-25646 影响范围 | `title="Apache Druid" && body="0.20.0"` |

```
body="druid" && country="CN" && title="druid"
title="Druid Stat Index"
```

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWEqsyvWM1Odjz8MoUr5zWHiaprKicuibrJdkgdVZ8s1gcXyYUyzGib5OL2a38V1bmxerDABJAIGGZe5CVg1UQrIv0HVtSKrZZkCIY/640?wx_fmt=png&from=appmsg)

img

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUK7nPaVPLz9cGkfEo4G1TUSsqPXWEmQrvR4479rqib3EKTSStyeof4icHcVNOj2rk43rHdc39UJRQEvR1R9YvHxUH4qyQ9MmVlQ/640?wx_fmt=png&from=appmsg)

img

一些CVE漏洞的poc，直接上网搜索即可，通过对上面搜索资产，导出，批量测试挖掘

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXZj2txhfNY4Libm8VBLggjeu58HtibHIE8fDUFJFMIW5BQrmUkaDxFicib2vgBIwZlb2BcDcxic5SuM6rib52rsEt5RWiczYskDZic1WI/640?wx_fmt=png&from=appmsg)

img

## 0x2 druid漏洞案例分享

### 一、未授权访问漏洞

如果网站无需登录，则可利用未授权访问漏洞，直接访问下面的springboot常见报错界面404直接拼接**常见路径(可构造未授权拼接尝试):**

```
html:
ip/druid/index.html        ##Druid Index
ip/druid/sql.html          ##Druid sql监控页面
ip/druid/weburi.html       ##Druid Web URI监控页面
ip/druid/websession.html   ##Druid Web Session监控页面

json:
ip/druid/weburi.json       ##Druid Web URI json
ip/druid/websession.json   ##Druid Web Session json

Druid 登录接口：
ip/druid/login.html        ##Druid登录认证页面
```

这个登录界面就是Druid登录认证页面，我看着十分熟悉，要是经常打若依框架网站的师傅，应该在若依里面是老朋友了，第一次搞Druid的cms框架还是edusrc某证书站边缘资产上的，当时就是直接弱口令admin:123456进去的。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVzHuuTuQ1dVG08Pxnqxrob5hO5dfqiaaGVjwickB0xCMp0hXHicmoP5b0xH47fLVzEh7hSZ4nYkSyoOajA90pT24hDvyNgibHb2X8/640?wx_fmt=png&from=appmsg)

img

这次我找到的这个Druid框架网站也不例外，也是直接admin:123456登录进去了

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWa9icDC0AFf7w7ydic3IEL6Xz29ykpqWxLDIq9JXicUib3R9rLic1u0Nq4ticW8zgHuDxSWKRIPSU69whNptBcTTsShaL7S6OlvvaFE/640?wx_fmt=png&from=appmsg)

img

其实像对于Druid框架熟悉的话别的功能点的信息泄露没什么利用的价值，主要就是开头讲的URI**监控、Session监控、Spring监控**这三个功能点

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWXibdXTFlusCO1Zs91Y6qAY2nHicic2mF827aKEHNMc8oPM6icaFwAjfwamiaVP1VbdFA5NwZRmYEreqetbcAuKDia5wbfCfvw7x2uc/640?wx_fmt=png&from=appmsg)

img

1、首先我们可以点击URL监控进行查看

可以看到下面显示了很多的URL，其中就有网站的版本信息，还有/actuator目录，这个目录熟悉的师傅们就知道这个是spring boot全家桶的一个常见的接口信息泄露的一个目录

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QU0icScIKfCwyx5GsxNvian4urtuxTxPslqVGtCysC4BMZt0bTD17KgeDVykxExAvxib3OIgc3yM6obORcRmCfhCxw17Doicg4hJuI/640?wx_fmt=png&from=appmsg)

img

直接这样请求，这里报错，那么下面我们尝试使用bp抓包，然后更改下请求方式

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXtUgdvd7NGJITMXLr9pt2LH2rAVYMltcicMciaSYT3ZLLOZ1ISF7mznb5DXB4kcdSRgzT3EANDMKVbsubspaAvOgpk6jEBNmA58/640?wx_fmt=png&from=appmsg)

img

但还是没有什么信息回显出来

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVDNZXR58ibsSuHfK6yxOXRr8XGtzmqfOTaF0daGgGjThEwVmhHTMHh1FgvP8DDhwfyoPeqDv7rd629lIHmj1rX1SD5OHwuMsAU/640?wx_fmt=png&from=appmsg)

img

/actuator目录，我们可以看到下面暴露出来了好几个接口，感兴趣的师傅们可以尝试下swagger接口泄露，使用swagger插件进行测试下

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVqsicJwbfmJRj7zldouUkr8wJYx7Q0jux8QYpChhNiaiaHjMQiaGjbDZsJ4PhMzsjHzuG0f1PULcjWKZJYY2VJDBCfz2Lcib5VMPGk/640?wx_fmt=png&from=appmsg)

img

2、我们接下来点击这个session监控的位置，可以看到下面有两个session值，那么我们就可以想一下了，有session值，那么我们不就可以尝试下未授权访问嘛，直接先保存这两个session值，然后再利用 \*\* /druid/login.html\*\* 接口进行测试爆破session值，然后看看能不能直接利用session值登录的

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXFtcVPdVggKHYPortyy6OSZaeWqPjUwB2m10icjoYzicicncZldxegwn4PiaWnicuSRUO0sibOBdyvAYZfE8pUTlVjDKlVsskIzibCDE/640?wx_fmt=png&from=appmsg)

img

这里直接抓登录页面的数据包，然后利用bp爆破（思路，因为要是session泄露特别多）这里泄露的少，其实也可以手测

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUhGKemfYNibMbLGTzggIGN1J92PPLickNfib8lAIBJBiaekiao5dPSJzEsu1KwPvYXFAC5GIe4qtgLD9uBgZrQ9oicXxcL8GlGrF91s/640?wx_fmt=png&from=appmsg)

img

可以看到session值爆破成功了

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWVIiclNT3mPNuMMyicdjvoArTebuyT5ocLMnkY9OcqNYT4trliciaUdhIayO4CauqpRIKvYqY3AhQJmkg65Q0TmW2DyBs2KBKTwck/640?wx_fmt=png&from=appmsg)

img

然后拿到爆破成功的session值，去下载一个**小饼干插件EditThisCookie**，使用这个小饼干插件

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QX42KW0IRbcbdZ45Ficz9jzIKEj64wgh65QBd6RiapgFhe2pQ3h62LZepjngZm4rJLpnib50bvvHwOJel2k5w1AWeSUh4NEA2Vkxo/640?wx_fmt=png&from=appmsg)

img

在开始的登录页面，需要我们输入账号密码，且没有session key值，那么我们下面直接把刚才爆破成功的session值替换上去，然后再选上下面的勾，然后再刷新，就可以直接免密码登录了

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXIezHRaCILCI80ISYPzg0AW6wsk0VI3KUcWKox79sU4zhiakTFg0qPY8olcc4vBCa481bE5yaDnHiazby76SqAEAhqTWwVVjFYs/640?wx_fmt=png&from=appmsg)

img

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVqCfNppYIfcKWJkwZ14zMVk66W8jib9zubuLW2eQM5icia31Sq6933kYcSKGbwq5S1YQCNFGCeicxthffO9MQoiaiceibjT3srwynDSA/640?wx_fmt=png&from=appmsg)

img

### 二、/swagger-resources接口

这里还可以访问这个接口，说不定存在一些接口泄露，未授权访问，存在敏感信息泄露漏洞：/swagger-resources

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QV0aLbTqnUwicl5GKmdicO3mOUgUlsarxfzj0GZtl2s8icj0fFsiaIB9ulnlmY18rIHFDIXhdY7xH1m9adSia3Us8EMY3kPRKQSUeMA/640?wx_fmt=png&from=appmsg)

### 三、常见的druid 登录后台页面拼接URL

```
常见路径(可构造未授权拼接尝试):
/druid/index.html
/druid/login.html
/prod-api/druid/login.html
/prod-api/druid/index.html
/dev-api/druid/login.html
/dev-api/druid/index.html
/api/druid/login.html
/api/druid/index.html
/admin/druid/login.html
/admin-api/druid/login.html
```

要是碰见登录页面登录不了，可以使用bp爆破目录的方式进行未授权访问测试

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUf1Wiaj9yUibaDnJgWyPS8Pe3T0JxmqAOB2E40wugHmLxNgZBKDDBIDzJ6ic2bd6gXqEibBHBogA4UYb1nibKbOp0ZLiabArlYegrqc/640?wx_fmt=png&from=appmsg)

02

0x2 培训课程介绍

26

**SRC漏洞挖掘培训课程**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6cIuvSQkkicOHhYFkQLTibYAMUR9rfZ9eUrI78toIC4V2304G909O6s6CnVrAGiaYLEJM9XuUARhzNfxCtYKQfQ83wfPSlqpshSScfoYzSKzgY/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=wxpic#imgIndex=4)

**1.课程价格目前是425（后面也会随着人数越多，涨价）🌟师傅们还可以上车补票，冲冲冲！**

**2.报名成功送知识星球一个，拉内部小圈子交流群+SRC直播通知群！✨**

**3.一周2节课程，直播+录播形式，课程内容大家可以看课表，目前是第一期，一次报名永久无限听课！❤️**

**4.目前是第一期课程，后面比如说开了二、三期，都是不用在花钱的！**

**5.上课结束后，会把视频录播+课件笔记一起打包发直播群！**

**6.哔哩哔哩SRC课程公开课，链接🔗直达：**

**https://space.bilibili.com/642258933**

SRC课程详情🔎：[神农SRC 漏洞挖掘实战课：从 0 到 1 成](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247503167&idx=1&sn=2654bb0ed9382199d7480aba559ea490&scene=21#wechat_redirect)[‍](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247503167&idx=1&sn=2654bb0ed9382199d7480aba559ea490&scene=21#wechat_redirect)[为赏金猎人](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247503167&idx=1&sn=2654bb0ed9382199d7480aba559ea490&scene=21#wechat_redirect)

内部小圈子知识星球详情🔎：[强烈推荐一个永久的SRC挖掘、渗透攻防内部知识库](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247501608&idx=1&sn=5eb836122ac222ca9767a7bbc3c4521b&scene=21#wechat_redirect)

欢迎关注微信公众号：神农Sec，报名咨询添加微信：routing\_love

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QVcCkxIUpaBmNic17zibGfXMWrr9z89gE0DFtbOu...