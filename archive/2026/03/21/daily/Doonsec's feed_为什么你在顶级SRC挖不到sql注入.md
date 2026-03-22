---
title: 为什么你在顶级SRC挖不到sql注入
url: https://mp.weixin.qq.com/s/EunSGK5QZxS8ctNplWuxIw
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:13:48.607140
---

# 为什么你在顶级SRC挖不到sql注入

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kCyqEeiaibbhBmbQGiaTlWMXhKreQw9IqppviaK9VD5r8jW26FCTO5f8Go1l79ca63HdZEaLIQFhdgutw4iao5dxRkY7AtSyyzicgk0d4PGxiax1Ck/0?wx_fmt=jpeg)

# 为什么你在顶级SRC挖不到sql注入

小乳酸
小乳酸

Z2O安全攻防

![]()

在小说阅读器中沉浸阅读

最近一直在测国外的 SRC，目前是 hackerone 第一季度中国区第四。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCyqEeiaibbhAuaGbTyicF3DTx3fiaBPJQ7MOMsxhjOWdtsYPicEueLEDZ5UGcQpXWJiag74QPBqyCD1Jia5p5jiabcFmtffniaHjwLCmViaHge8RHSFo/640?from=appmsg)

下面我分享三种挖掘SQL注入的方法：

0x01 Header 里的“隐身”注入：别只盯着 Body

很多人抓到包，改改参数没反应就放了。我第一件事就是去搓 Header。

尤其是 X-Forwarded-For、X-Real-IP 这些取 IP 的头。很多开发觉得 IP 是系统传的，肯定安全，拿来就直接往日志表里塞，或者进风控、黑白名单里做 SQL 查询。

我的操作： 永远用 ' 和 '' 成对去试。

0x02 路径里的注入

大家都习惯在 URL 最后的参数位 Fuzz。但我习惯在目录中间横插一杠子。

比如有个路径是 /a/b/c。 我会试：/a/' 对比 /a/''；然后再试 /a/b/' 对比 /a/b/''。

为啥要这么干？ 现在的后端路由五花八门。有些中间件会把 URL 里的某一段路径直接抠出来，拼进 SQL 去查权限或者查资源。

SRC案例：

![](https://mmbiz.qpic.cn/mmbiz_png/kCyqEeiaibbhD4DYLmUyRy1Rib8ibU0ypaDYcUUDjqph7580wiaLtQic8UicmCCPep8zxc2Oqjhndoh6dGnt06hKsVsmoA9529omuzD4pRT9LDbpG0/640?from=appmsg)

还有就是在目录中添加单引号可能会引发系统报错，若是泄露系统路径，国外src也会给个俩百刀左右。

0x03 隐藏参数：把 A 接口的参数“喂”给 B 接口

这是我最核心的一招：跨接口的参数。

假如我抓到一个正常接口是 /api/v1/user?limit=1&xxxid=100。 这时候我会从 JS 资产里提取所有接口，比如 /api/internal/config。

重点来了： 我会把 ?limit=1&xxxid=100 这一整串参数，强行拼到那个接口后面。 然后再去试：limit='&xxxid=' 和 limit=''&xxxid='' ，看返回包有没有差别。

实战逻辑： 很多后端函数是公用的。虽然前端代码里没传这些参数，但后端其实一直在“等”这些参数。这些隐藏参数因为没人调，开发往往忘了加过滤，直接裸奔进数据库。

总结
现在常规的sql注入几乎很难有了，还得是需要一些新的思路。我分享的这些思路大家可以让ai写burp插件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/JnmoqeNZZwRSCbmSiaerWcPS6u48RevH8IHoRlzeD3gxZmcbwTtj60AMKbMWicKuYvrrGibnqfS9qSvF6eg9P4ZoKLOCaBySrp5f8kv08BqgK0/640?wx_fmt=jpeg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

Z2O安全攻防

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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