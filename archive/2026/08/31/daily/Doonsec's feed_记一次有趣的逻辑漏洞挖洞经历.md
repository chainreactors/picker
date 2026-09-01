---
title: 记一次有趣的逻辑漏洞挖洞经历
url: https://mp.weixin.qq.com/s/2WTRR76u-OTCRCTQT5uI6g
source: Doonsec's feed
date: 2026-08-31
fetch_date: 2026-09-01T06:57:12.720952
---

# 记一次有趣的逻辑漏洞挖洞经历

# 记一次有趣的逻辑漏洞挖洞经历

小安
小安

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
原文作者:小安原创链接:https://xz.aliyun.com/news/13055
```

## 前言

前几天在网上冲浪的时候无意间看到了一个Edu的站点，是一个很常见的类似MOOC的那种在线学习系统，对外开放，同时有注册和登录功能。对于我这种常年低危的菜鸡来说，这是最愿意看到的，因为一个Web网站有了登录功能，就代表其网站必须要有权限划分，而有了权限划分，在这里的开发就容易出现很多问题，越权便是一种常见的问题。经过测试，发现这个站点就存在越权的问题，例如A账号可以通过发包更改B账号内的数据，但这些数据不是密码，个人信息等数据，而是平台上的评论，收藏，和点赞的数据。尽管这些数据或许不是那么敏感，危害听起来不大，但是也算是水平越权的一种了，因此最终这个漏洞提交EduSRC后被评为中危。接下来我将回到当初的视角，与大家一起复盘，分析这次挖洞经历。

## 发现过程

1. 访问网站之后，看起来就是一个常见的在线平台首页(各位师傅请原谅我厚码，因为这个首页banner就是这个学校的全景，哈)

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQX9nTwJlkXibTic4jR5h7jBS4xLpOXYYC3lwfSpdiclubhlZKdytvsZFlF04biaU566yjsk8ibJIJ3RFViaMxN84jLCoaayxlnZO3nM/640?wx_fmt=png&from=appmsg)

   右上角可以发现有登录，注册功能，于是果断注册一个账号上去看一下都有什么功能，从个人信息修改部分进行一些常规的XSS测试，看看是否能构成存储XSS；在头像上传部分可以进行文件上传的测试，看看是否存在任意文件上传，说到这里不知道为什么，感觉现在的新系统里很少有任意文件上传了。在侧面可以看到有一些“点赞”，“收藏”，“评论”，“笔记”等功能。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSRYzfIoyXbpqGmG8QBS0AgXuia9P9dv1axYVagElLNNyaAKpoq9VC8BWgvTnbJicw4sWiaBdpAzPX6iaGYeRnwmrNIiaE6UbLsBIwg/640?wx_fmt=png&from=appmsg)

点到随意一个视频，可以看到视频的右下角有一个记笔记的功能，我们随意写一点东西，添加一个笔记，此时我们在Burp里面观察分析一下这个笔记是怎么创建的，同时分析一下返回包里面的数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSxFOpjlNCXKfZxc7HDd5aTqhczic0bsq627pLDANvzQwpq4F776nByHRh3ic8f6SMjrq6YJWxia1hzgLyk5BzXIibtVyP6uAFABFE/640?wx_fmt=png&from=appmsg)

抓到的包内容如下，可以看到是json形式进行传输的，请求中三个参数，第一个是笔记内容，第二个是资源id，第三个是视频的id，返回包内容则是返回留言成功与否和时间戳，其中令人疑惑的就是第二个"resourceld"，这个参数不是从1开始的，而是直接跳到133，于是怀疑当用户记笔记的时候，这个id就会自动加1，跟用户是谁无关，只是根据全站的笔记数自动+1，同时这个参数也是用户笔记的“标识码”。此时我马上进入个人中心，测试了一下删除笔记功能。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS293NpOCgPqxpVSPeLSD35yDBgQjnhHNiaByzYHOh1ANgM480f02MibDnjC2WGOsfaRdG04B9xTIflC3vt7YyUofZpYajXVt2d0/640?wx_fmt=png&from=appmsg)

抓包内容如下，也是对一个接口进行的POST请求，数据格式为json，可以发现删除功能的请求包内容确实存在与创建笔记功能请求包中相同的内容，但是多了一个"id"参数，这是怎么回事？这篇笔记是我账号的第一篇笔记，但是id却不是从1开始的，结合刚才分析，这个id看起来更像是一个全站所有用户的笔记数总数，每次用户一旦创建笔记，这个id就会加一，但是这个id似乎只有在删除的时候抓包才能看到。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTTqeRDmyGukDYX7J39n4Y0kXFpT0ybGgVPpC7UMzkHtbjY0jiblpGyt17WukHMA9r0NUUcqwgmxf7A5WPibMjgthr5nFrxdQj84/640?wx_fmt=png&from=appmsg)

1. 综合以上的分析，发现在删除的时候参数中没有判断权限的参数，只是一些删除内容相关的参数，经过测试我们发现若是更改id发包，响应包与删除成功的响应包一致，因此判断可能存在越权问题。观察其他功能的请求包，发现跟上面两个都类似，在删除时差不多都是POST请求表单携带id即可实现删除。
2. 开始验证！再注册一个账号，暂且叫他B账号，我们用B账号发表一个评论。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSlpT9C9e10hkuxm8h2HXz30ahHWibuVzo9oP2alibzicq9COmI8tRe7ehLb7stXNicAib5EiaHMlm1OWuA1yf2xr6URfEwmeAQ4DnuQ/640?wx_fmt=png&from=appmsg)

为了方便测试，此时我们到个人中心里面查看已发表的评论，抓包观察这个评论的id是46。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR6GDsDFW7hFSrjfyIU4NX9Aqev4F1IzUBWVFUictRSsIEfUBhoictQA9KEMQbrHC1HnVPcGBSG8ia5cAb3Uv0ayQrVKP1fOqOXmg/640?wx_fmt=png&from=appmsg)

直接再到Repeater里面，这里还是之前测试用A账号删除评论时的请求包，直接更改id为46，发包，从返回包看可知删除评论成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTGEaq4yqyXjUyJiciaLr6zLI4KmHkhib0ab1AZyuLib2pM70SGnAaKqR3pzDO7NlIpfGr8RWGsTLIfJLibt1TTMMEUX3COH6d4Bgy4/640?wx_fmt=png&from=appmsg)

此时登录B账号，点进个人中心，发现之前发送的评论和笔记已经都被删除

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRgFcU5SRGJJRVUlZpaufH71pa3eYs9LpePScbUODrlvNF60DiboTZSMTS7v2sttia7f5QloWME4XmEqHP6vic26cEjFtRxiaujib0s/640?wx_fmt=png&from=appmsg)

## 成因分析

综合请求包和返回包的内容来看，以笔记为例，可以猜测出背后的创建和删除逻辑分别是:

1. 创建: POST请求接口，直接携带内容，同时后端会给这个笔记直接定义一个id，这个id跟笔记是哪个用户发布的没有关系，不可控，直接强制是全站笔记数+1，比如A账号发布了，这个笔记的id是47，那么无论下一个笔记是谁发的，笔记的id都是48。
2. 删除: POST请求接口，携带要删除的笔记id，其实从上面的请求包我们可以看到，评论的删除确实是POST请求只携带了id，但是笔记的删除请求中是携带了“笔记内容”和“视频id”这类参数，但是测试可以发现，这个参数后端根本没有判断，后端拿到id后就直接对相应的笔记执行了删除操作，没有进行鉴权。因此只要从id向下遍历到0，也就把全站所有用户的笔记都删除了。

## 总结复盘

在这之前我也挖掘过类似的逻辑漏洞，那个漏洞是越权删除图片库中其他用户上传的图片，实际与此次的成因大同小异，都是因为没有对平台用户的个人“资产”没有进行鉴权而导致的问题，在类似平台的开发过程中，很多开发者为了方便，后端会直接处理请求中的关键信息(例如上面笔记的"id")，从而直接对其执行操作，不会再比较其他的数据，这就导致了水平越权问题的出现。作为安全人员，我们也可以多多关注资产中这类功能点，测试其存在的问题。

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**skill+grok辅助挖掘某企业sr****c****实战效果，能出但是重复多。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQwyn779TTwY7vZkePQCL8k3K8dYxNdyzfgADL4dJcNUvpmodLeDVCZ6xDC4RJXEBmO2tcWqgUNdTVicKTW0jpdsg7X6xwP5gIQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQnIqagDL2A4BUIXrib9YVmATWuaIDqETqYd9ToHib52mDyoMyqc6Wzh733FRnbsDsGgey7B8s8jr72UtkPY6ich58niaPJqoItKcE/640?wx_fmt=png&from=appmsg)

**企业src边缘&核心资产实战效果&&有重复但是证明好模型+AI确实够用**

**（图片仅供参考，我出不等于你出，见识**到**ai神力即可，多去用AI!!!）**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT1YNI9U6r6NMO4UMUBROoWeC4XQC4Dge94ODZ7tXY6tbxqb3IJoghve0u1SfkygE5UJ5HTdUBvLZKrn5ps13F71piax5dlHnOE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTGjdxKy4nllaLXIznTvRqicichITccuB8psYFRYakw6ViauCk6iccziahfPw4fnrqhyCp7Zkq7lRI0DOicyrZlNyicYibTVibfGFZVaG0c/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中!!!)**

```
信息收集(主域名信息收集,子域名信息收集等&会永久提供fofa-key助力)弱口令漏洞&未授权访问漏洞挖掘任意文件读取&删除&下载&上传漏洞sql注入漏洞url重定向漏洞csrf&ssrf漏洞挖掘XSS&XXE漏洞挖掘等等常见漏洞cors&目录遍历&越权漏洞挖掘EDUSRC(证书站挖掘案例分享&edusrc挖掘技巧分享)CNVD挖掘技巧分享&实战案例报告编写公益漏洞挖掘（公益src挖掘漏洞分享&提供补天1权重资产）SRC挖掘实战(针对各种常见功能总结的常见测试思路等快速提升)经典常见Nday漏洞(常见中间件&以及各种常见框架)复现云安全相关漏洞挖掘（云key扫盲&云存储桶&快速识别云环境&云攻防）AI相关学习（AI基础&AI代码审计实战测试&webLLM攻击等）APP&小程序漏洞挖掘等各模块不在一一介绍
```

信息收集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTu9DGyTubluhYicFynwVBKa4V06sDfEVKOyk5Q4ghZzLMDAuLb1M1oR4RJumGWrADPapFjTrOjpksKQ8q0YYCnl3ZWLof8Knzg/640?wx_fmt=png&from=appmsg)

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR45bibbJEb28a1gS5yth3r5HyOsgPiaOUHHYriahZyIyrk0LMOsHW4VoDibyBRibTNzptGiaLWX62UwykicwvbxCJPopvklqiaxML8lS8/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRjVmJn3g5b23ur9E6Cx3O68f0hXVjCiaj8J4RYeTGBecqf1k99phG0ice2wtd5lKgR46OeqeLQfMpk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRbZ1HYm7R7YEiaxRVQibGWyricx9l7HpGjS4ZfWRdlft8iacwkpzYyZfmYEkWdJgYRORPkNFR6dADR5MyE524tWX6cAwN8MmrCZu0/640?wx_fmt=png&from=appmsg)

edusrc

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQVVlTXhibjR8UiakZBQicXRZrQ7hdoOz5G8MQrcuDBGbqJdO0kIz6R9IU4ObAeOiabT8pr6lc7jibdIkKoTjiaXNHPLAwAB3BV2UvLM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCrvarBbzP4L9kS6P0LVH9JMdmcbFDKiaicHqMFgTxq3x4iatjDJQicmc7NPC14C9Fk3icFjrouSgNVaN8Byuf0C0Iq9O6D1XPvFvY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRALwXmgZ4mh2LW0RdicrKjBCP7P1iaF14G0Eq2v3KRnTJORpwXZlF58WEz6QicxLJpyJaA5iah5CF2rHjBz4JzOELFRaZTAKOQ2tQ/640?wx_fmt=png&from=appmsg)

经典nday复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRu8Gf849iaCkSBxLL8IlzJTRs185QicEe9l5UGI1dEVKISt2IGGveZynXBW9tIUsxNsz4adSTib7rib50uSJdjNfTvVRFrbPJhzL4/640?wx_fmt=png&from=appmsg)

云安全&AI安全

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ9qiavETNjaaX162czpNCqpw3uJqVpicbI15AXzhf5x8icmHxBdTGOgRgzNPGF3Aw2gglT4Fx09JGXYibQC6U7CQKVmoH08l3meia4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQgcsjiaZ4S26TWowHfpBkhSeHf2pjrcDyicJuia3uqvRBauLEOicibibEMqibnBMtjopFL8No7UXNibbURvzeJ3dQHTibvGxRQGnorb4co/640?wx_fmt=png&from=appmsg)

**陌笙安全漏洞库介绍**

```
最新漏洞查看1day&0day分享EDU学校相关漏洞Web应用漏洞CMS漏洞OA产品漏洞中间件漏洞云安全漏洞人工智能漏洞其他漏洞
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTFBRMa8XwYxfcZMyXicx94xSKxawPcqFia2rJKOL7fSLYXiccwHc868XxNGIQ5z7ibiaI1MNAGRrK7U6wXJTsZOCAu2I5XV1boTAL4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mm...