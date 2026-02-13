---
title: 不只是WAF、会拦路的还有很多（SQL注入）
url: https://mp.weixin.qq.com/s/sxzX431S6RwOPK0vhNqEQQ
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:15:38.878340
---

# 不只是WAF、会拦路的还有很多（SQL注入）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KvrEnQiahoiaAsscCzgJUfuuicgkVEua2KZ0k7DKyLJV3jXmrPQckhfPXMWK54KzJROJ3aeTvndQ6f6HdGbNJWHSW1oESgwdIfU8mRwWEO5Ocs/0?wx_fmt=jpeg)

# 不只是WAF、会拦路的还有很多（SQL注入）

原创

kingman
kingman

kingman安全

![]()

在小说阅读器中沉浸阅读

声明:

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。同时所有相关行为均已取得授权，未经作者同意禁止转载

常规SQL注入：发现注入点-》SQLmap启动-》失败就自己写脚本

遇waf就绕绕过不过就G

如下案例均有授权、未经授权严禁非法渗透

# 0X00奇怪的注入

---

前期通过对靶标系统的一系列渗透拿到了需要的源码

代码结构如下

![](https://mmbiz.qpic.cn/mmbiz_jpg/KvrEnQiahoiaBgpePylSsuw4PRum0a8UMBcb5JKibdHyX3VAFiberhYAVsluEuFiar6ez2wQOjJcbIHYlyzP0h9Y975lr3Sj9InwNub3xCguFysk/640?wx_fmt=jpeg)

python-web.png

虽然之前从来没有审过python的源码，但大同小异吧

先看路由、鉴权类

在\_init\_.py中找到对应逻辑

根据源码可知哪些路由需要鉴权

![](https://mmbiz.qpic.cn/mmbiz_png/KvrEnQiahoiaBSKxlCUXaIRXGqGp6xzSeFGCEcVLcicQZgDG9g8iaA8y0aPErtx3WwBHg5C7sP371yuCZGCNNTboGJIXDTTPLJnoNCMMZKl2N2E/640?wx_fmt=png&from=appmsg)

路由.png

根据对应的路由去查看功能

本文故事的主角是/cms/api/init\_category

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaCpBOEoadrhLIUeZly3QKxKZibu1Q3x7aDLia0UJ4AIbUmKg8LlmhfcMgaPvbY19MU7MAObahyicCttT66mCiaiaw18XMxEBukIBEjc/640?wx_fmt=png&from=appmsg)

init\_category.png

post格式传入json数据中的bot\_id处直接拼接sql语句

明显的sql注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaCZiabn4b1FSUfMl9PDjaRVticjSAcuEHejkyXfib4E78p50JVQicruGCckgkfalZY0ILembxz6xHgyO86qxNibdKEk46V1phDenqq4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaA5FzFDRXcStoicQUGHhiaby6KXXcda7KNVk998K0JN8ptLtoib2LkuvAyhibNuibV3ZPNIxfbWkRRoGzK7aY67ZtOm95jXCN9w4BjU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaA832sW5ZxX2Qxx7AleLhebuwrDEHSPupF8ZRBuaRWftzHSzwIWznWK71AaccBIsI2IzhZH40cIcpFNyFiaDB9yOVScYUJLD7Xo/640?wx_fmt=png&from=appmsg)

时间延迟.png

至此理论上来说我们SQLmap必然成功

可往往博主遇到的都不会一帆风顺

![](https://mmbiz.qpic.cn/mmbiz_png/KvrEnQiahoiaBom5YqRO632YicKv1PZDRQ52PtZqhlWqIWtde7iaHJDaYVRL5mTQhBgJ2ibicIVUgqQj0rSCjY6ic4dQ5bBnUIMpt9mkQ6WAXlFhicw/640?wx_fmt=png&from=appmsg)

fail.png

一般碰到这样的情况下一步的解决思路就是手搓脚本

常规到这基本能解决了、可还是失败

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaBZGiazPnaDgqhJojnhfoGwFxxBPdbDk1KRAibU0eBK4UG3hicsrKUvDfOEaK1QwtG1wUBV09gAfdplHQjgX9yY7YjtQWdUdM3yvo/640?wx_fmt=png&from=appmsg)

?.png

那这就很古怪了

没有waf->代码层面有注入->验证存在但无法成功？

看着burpsuite的history陷入沉思

复盘时

发现了一定的问题

发送同样的包、结果会不同

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaAea9Uwx2EU3uumFAtlDmKhEz5gliat8btdMDqmqvgI8UibBc5Xxd1OGAKUFLL72DugabcHA2uNItaM1LYicIu9icBmnibkWtmk8vgQ/640?wx_fmt=png&from=appmsg)

？？？？？？？

# 0X01问题的发现

---

放心不是遇到了什么不干净的东西

可能眼尖、或者做过开发的小伙伴能秒懂问题的出处

问题的罪魁祸首就是在

性能优化

（为了优化性能减小开销->将常调用的数据库查询做缓存)

貌似我从来没在SQL注入的文章中看到过这一点

缓存能不能被绕过的关键在于查询是否重复以及代码逻辑的实现

# 0X02绕过的手法

---

# 增加长时间延迟

![](https://mmbiz.qpic.cn/mmbiz_png/KvrEnQiahoiaDMMgzzLqjDNrUyqU55kyTRsOTbhm8INpy9fTlIIBgC2ws2qepiaXPvsBiaDib4GbM86EIgJTtCxHZQKiaGvJAibCOOGvuspHf1uxNE/640?wx_fmt=png&from=appmsg)

bypass.png

至于能不能通过增加查询语句|修改请求路径|修改参数伪造不同用户这类的绕过方法还是取决于后端代码的写法

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk33j31ajLZ0yloe8cj2zYIaKaL9mGiaX3eEzZ0Y6HH1J15GyY5F0hLZ5GMlILlw81dcxNLoK3hq5cQ/0?wx_fmt=png)

kingman安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk33j31ajLZ0yloe8cj2zYIaKaL9mGiaX3eEzZ0Y6HH1J15GyY5F0hLZ5GMlILlw81dcxNLoK3hq5cQ/0?wx_fmt=png)

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