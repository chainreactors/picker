---
title: 一次渗透学员母校捡漏通杀？
url: https://mp.weixin.qq.com/s/itoWbHHrelIkj4fVkfUQKA
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:15:28.585400
---

# 一次渗透学员母校捡漏通杀？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9oWrrCB9rlwtwoel76ACJic9eeEvdat2s2bicWBVQ1N5f3f61pK9wGLEkJGNgohDypBNF69sCavTA6eQMla5kXicjqjGpYVKDoIib2iaL2XnTCRc/0?wx_fmt=jpeg)

# 一次渗透学员母校捡漏通杀？

原创

只会弱口令
只会弱口令

只会弱口令

![]()

在小说阅读器中沉浸阅读

**免责声明**

---

本文仅用于网络安全技术学习与交流，严禁将文中技术用于任何非法入侵、未授权测试、数据窃取等违法违规行为。因擅自使用本文内容进行非法操作、或传播本文所造成的一切法律责任与经济损失，均由使用者自行承担，与本公众号及作者无关。如有内容侵权，请及时联系我们处理

---

前言

当时学员还以为我早就挖过他母校的洞了，结果并没有。既然如此，那必须带着学员狠狠干一波。毕竟，没测过自己母校的漏洞，人生总感觉少了点什么。

![](https://mmbiz.qpic.cn/mmbiz_png/9oWrrCB9rlxQogcQ1sytjibySvd5ia6VVLwzbgf4z8Kiarodbnickna28yOcF769B2V7cJg0z59vHbwyHWuzxcicWQo7fjj1PShnWicWECzuF6kuk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9oWrrCB9rlwfLNCWLicWMHZ0u97y3jCeD5vpTtMgfEpCImOWwPblXOYwY8VEEc1y9FiaXtBbUKuZiaCNvU5tNS6tMLpwKytp2B3Bub4QseNqiak/640?wx_fmt=png&from=appmsg)

测试过程

1.资产收集到一个某支付平台，可正常注册账号，因此直接注册一个测试账号，避免后续再次花时间收集可用账号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9oWrrCB9rlzukeurSzz4JibWtiazHIL0rw0dZlDh0qEMKorPmtCYicRZhdKRYowQicS2b6gwsNJibvgib2xZYIIou7hMfIkVJr1PUb1ymOVJm3Jiac/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9oWrrCB9rlzoDLynJ2zwrJdvtJf5GWF6iaaIn5MmjexIERtoFEPpc5ic60ybwekcdGVrx4GKHV9MU9VvXsYU7pwII5muXbMdtchBwz1aZQmr4/640?wx_fmt=png&from=appmsg)

2.注册进去之后，先把能点的地方全点一遍，顺手看看有没有信息泄露、SQL 注入这类常规洞。

![](https://mmbiz.qpic.cn/mmbiz_png/9oWrrCB9rlxKa5fez6E6ia3P2160icbe0vRwCvibK7hNB0YrnHK5wlQcjT3kFpTW8U8HtNfJ226pOjEluY0DiaFJ94yNeFSuiaswOhme5jOhdSJw/640?wx_fmt=png&from=appmsg)

结果你说巧不巧，缴费查询这个功能点，就感觉这地方大概率有 SQL 注入。大概如下

```
year=' --报错year='' --正常
```

小小SQL注入直接塞入大大payload，拿下当前用户长度，达到edusrc测试SQL注入标准

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9oWrrCB9rlwCGfFSiaQmibibkUmj6Os02ibCPvpjaE9vwvTpZZB4KTzC6uFYFQvtW2EPUib4ZneacbeibV8v8JfomGxLHLUzftLeMXwSNggzh6mf8/640?wx_fmt=png&from=appmsg)

这就结束了吗？那肯定不可能，一个系统一旦暴露出 SQL 注入问题，意味着系统肯定还会在其它功能点存在SQL注入。

![](https://mmbiz.qpic.cn/mmbiz_png/9oWrrCB9rlwpy84fCZAM0ib05SZ9FicoM2DT8Po0VUekVg9SFlAuzkdicFOAEMUxftkjaWRLJdqNEWpqHiaFxVAEC4o5j8viaRwnuzR5u8siagKNw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9oWrrCB9rlzEUZoJ5yc4eHyCZfdoZ4nhbpZHM1aYicauLCWwqxxJZTicfvTjFx8ibsYmjCDzd0iaEPQRrEaarYRpZs3WzBZe6616FpX127UgLa0/640?wx_fmt=png&from=appmsg)

后续也找到了5处SQL注入点，不过edusrc同一个站点不同接口SQL注入只收3个。

因为支付类的系统一般大概率是一个通用的系统，通过查询icon也只有几个资产。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9oWrrCB9rlywRlCB3MguMRib7pdhYZE0fIarKMsf3IvkFOd37XE8ZC2qAChv8icibgVQfy9TzvY83KMGS1XYVC6Gl8El4laZ0gPkHbvyCkbOZI/640?wx_fmt=png&from=appmsg)

这里也可以使用系统标题搜索其它单位资产，这里是智慧财务，找到对应厂商

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9oWrrCB9rly3jFmUOPFLIgyLPBY4lfdxApyvuFkohWQ5ic2nlmsnXAJUd07E31JF6lPuRsqYF5cFK64Y6Gicosk6z5oicoDwOiaUXVUWO1GXzTE/640?wx_fmt=png&from=appmsg)

找到其它单位资产剩下就可以一一测试了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9oWrrCB9rlz8FueO4bLuGTmIkEOE5iabSZTdHdR8InTGXw0HsVFiblV8Vu7IkpSSHdZgickQDHqpSRY0DxaIyy6xHypiaTR6BxNm7FzyZrUMeu0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9oWrrCB9rly5szUt4KFYdSG1IdibDhLVEf2SMax8YGNGmqKHBdTYX26ia5IUE09CTAMm1iaZfQicdIWzlOPkRsgaw3Q8DgMEiaCBeblG6eiacJNCs/640?wx_fmt=png&from=appmsg)

在我为此高兴的的时候，万万没想到，测试了几个单位都没开放注册接口，这不玩了吗？通杀的好机会，上大分的好机会就这么没了？

![](https://mmbiz.qpic.cn/mmbiz_png/9oWrrCB9rlzDW7sAdq84bM3NubxllTtFBicLuPCpuzLnCnVZPXyvNogddSg0pFAjiadYSl3ag5EEFNCuDRqH8TCUbmGDNt3NDn9n18iaq50dJw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9oWrrCB9rlxYxzXGAJ4VDCdOYSjHgiaib8ibCBiavNSvVEesoGMupZLDdFq5QNzQhBIPCFwTMIvolNJJ7ygbibaicqnkJyicF6kdDIvn3mYAEKtaTs/640?wx_fmt=png&from=appmsg)

灵机一动，拿之前的jwt在其它单位使用，不是哥们？真可以？？？？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9oWrrCB9rlw2U11B28xR1sUnLnr7y8qdJxOq8N7lhOIXzNrBSLJqTI4YFx0Na2VhemlcpzhQMpotgSe8QFyRcJ03enyIVzGe4anmB0jIKrY/640?wx_fmt=png&from=appmsg)

没想到意外捡漏，竟然存在通用凭证漏洞。最后就是一个token通杀10几所大学。

![](https://mmbiz.qpic.cn/mmbiz_png/9oWrrCB9rlxwPRlRujibSQjaAOMN7F4XH25iaopHTbDTIABAmx0SS9n0CqceDayW26retAc7AMvNoTHaticJ3rsgUIttqHlfb9AyBTTs0sZUrw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Bdrzd6gibGfspRlRPNgAlqSFccHic3SUtvPk6ouv0YW7tqDtrzrzfEn7z0jTN2BGUsSlEgZiaSalkzEmlObw8LCTg/0?wx_fmt=png)

只会弱口令

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Bdrzd6gibGfspRlRPNgAlqSFccHic3SUtvPk6ouv0YW7tqDtrzrzfEn7z0jTN2BGUsSlEgZiaSalkzEmlObw8LCTg/0?wx_fmt=png)

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