---
title: WIHscan二次开发内部版本上线，支持自定义js敏感信息扫描规则
url: https://mp.weixin.qq.com/s/KRFBDsc0u-hDFgF5pNWwDg
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:02:02.597024
---

# WIHscan二次开发内部版本上线，支持自定义js敏感信息扫描规则

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/niasx7fyic9CPn6IIc7TXGzqulafHCsibCiaJeJOpXDe5vR8m7ScPf1j3X4CSFDafoRVrZWCicq4icQyDBFr06icGHaB9lvLyHuCRCn7ibTmHUPibSgs/0?wx_fmt=jpeg)

# WIHscan二次开发内部版本上线，支持自定义js敏感信息扫描规则

原创

油漆工
油漆工

C4安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前言

做 Web 安全久了，你会发现一件很现实的事：很多真正有价值的线索，它们就藏在最不起眼的前端资源里，尤其是各种 .js 文件。js中的敏感信息往往特别有用，而且经常是渗透测试中的突破口

但是问题也恰恰在这儿，JS 敏感信息扫描这件事，说简单也简单，说麻烦也麻烦，爬取js功能又得接爬虫，匹配敏感信息的规则少了，又容易遗漏敏感信息

所以我基于开源的 WIHscan 敏感信息收集工具二次开发，结合了爬虫工具katana，爬取js并识别敏感信息

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNHkUgeUhDDhSkZkIxVsLGF2soTzQsvf21tHhEgTseUEesAtYR5yhx9JPJ3YYNMp1wzScnIZviasmsXmfM2lzw1jS98XxglbicibY/640?from=appmsg)

功能

WIHscan依赖同目录下的katana工具进行爬取数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CNIiaX53WiaL87ib24b8qibtOLEFrkKDmfibtydUAmY004Ob0ic85btRu2heqct1g0ZZS0r9sOyK45s0kuyR8BNwHvHgJxvL9WoKSOicQ/640?from=appmsg)![]()

工具使用命令如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPhRSdNj5mYRD56JJwViabahtIPsGrxIrmg3ia0YN4icibQ27BPEzLaMu7kU5ZohyJibutNB5XQLEDVbg3F3caRrh1L4RFKD5R0nqcg/640?from=appmsg)![]()

现在 WIHscan 支持直接带 -k 走这条链路：

1. 先用 katana 去爬取网站。
2. 从爬取结果里提取 .js 资源 URL。
3. 再把这些 JS 自动交给原来的规则引擎去扫描

示例：

```
.\WIHscan.exe -u https://example.com -k
```

效果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPmC60pUuNj1OPWnY6Z1bm2yhaPiceL5ekNfoJWJeo9RUdz23J6XqibP5IzouZKZ2Q4La5mWicePV6YmEdSiaaGZY5H3W87JR9D8MA/640?from=appmsg)![]()

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMEulw7u5Nz5vS6aY5HOZibfAc826sxPNUqnMZ95QRdUlOgTShO9ysACwlNMbxgMT9CAnSBvTZ6r3n6zuSCQic1VfgJTQP6ibdnY4/640?from=appmsg)![]()

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CMANBon9CiasjB4oE8ov2SDMIZDuRxTlfdWX4N4ecuKzc6SQv3RvwZR08oic84X8ckf18Q0ooXEzHuLrfQuSlH9dBgjNDfrwdvsk/640?from=appmsg)![]()

目前工具支持的功能如下：

```
支持并发控制，默认线程数比较高，批量扫的时候不会像老脚本那样慢吞吞
支持代理，联调 Burp 或走代理链都方便
支持超时设置
支持自定义规则文件路径，也就是说你完全可以维护自己的一套规则，而不是只有工具的默认规则
支持 debug 模式，规则报错、请求异常时，排查起来会很容易
支持结果输出到文件，默认就是 result.txt，日常输出扫描结果到文件中
```

js敏感信息检测的规则在config文件夹的rules.yaml中，可以自行维护：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPAeg0r9IJqlZK9Nr4uAzjVg7RlMPSpTjia8m5zpwXTB8iaQr6UFNCbHAtCWDsN5CialO8pYFjzkyuINX29TdNicSI3bn3JIJb7xO0/640?from=appmsg)![]()

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPvwcjqIIHY5YTSgicWVHyiaUdqj1xSEfiapA2BeLJSiaN0PMYSqtA3RU9iaWaysHTXRYuwbcJJBX6BOY4p3jvK9Gr0ZYJBh9lbJWcc/640?from=appmsg)![]()

工具已分享到内部社区当中：

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMIM8q0iaPKvc4uMKia65btdGvHVYaEC35oP0bgtkDkr3YtOmzZzFKeTjicdMjkOxjXxJu5jeuIaARENqibB8yketUiaQxMticE9VNkk/640?wx_fmt=png&from=appmsg)

---

内部CTF课程上线，总课程30+小时，优惠折扣中！

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CMld5K1l7CBke79UO7dC3hgOP2eHATAFZuAibb0y7XfmkMOibGYWwXa4MaO9B0grDSicgt4c9X35msl5kAeKcQJAWLnicODh5EZcKw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=14)](https://mp.weixin.qq.com/s?__biz=MzkzMzE5OTQzMA==&mid=2247490286&idx=1&sn=7f8f80578014db3187bc3be58c0df737&scene=21#wechat_redirect)

帮会简介

《安全渗透感知》是FreeBuf知识大陆的重量级帮会，帮会致力于漏洞POC/EXP、红队攻防实战，是系统化从基础入门到实战漏洞挖掘的教程社区，包含团队自整的挖掘注意点和案例，还包含分享的渗透经验、SRC漏洞案例、代码审计、挖洞思路等高价值资源。

内容框架（持续新增中）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CMCpnOqvibQh9B467VSQoRtibrF3CdricQhVRJwEodF2GhiapIISMVWMgIYMdCcKDJlfwBqwm4zia4icyt2ZUQHYqVZvPhlV2QwFNpZU/640?from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=15)

目前已有「630+」小伙伴加入了帮会

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CNAJT98cuHhzSxuT8Ag73paNReHsV1ZdCvrcvYTbpbNuzXjG3RTlYRYufZ9pSfJKXL4ZXlFDM2FziaDicExYbfPjnOY5nJ75bGQk/640?from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=17)

加入方式目前帮会成员630+人，永久会员优惠后只需69.9元。

随着人数的增加及资源的积累，之后永久会员将涨价至99元。

有意向的师傅们可以扫码加入我们，共同进步。

如何加入帮会？→ 安卓/苹果用户可扫码使用优惠券↓↓

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CN8UtNXh6iaCViboDwn94lFFlJE1AO7nvasqGOxlQnd56h5afw1l4hzMIWxQia3EibO2yHTvD2rtfhKQJhkrHa9u31jSMhWqgjiatCs/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=16)

→ PC端用户可复制此链接到浏览器↓↓

https://wiki.freebuf.com/societyDetail?society\_id=184

已加入帮会的小伙伴

可以加帮主进帮会内部交流群

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/EXTCGqBpVJQtiakQ6okzRrdlfK4mC8pfvo5S48opk7Cd6OmuTgGysOdnia3vnbDBYeP4ahh3292l2rfZxY3ianYKg/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=21)

请备注：帮会

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

C4安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

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