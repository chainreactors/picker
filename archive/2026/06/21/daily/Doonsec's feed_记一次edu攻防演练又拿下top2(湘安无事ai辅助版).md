---
title: 记一次edu攻防演练又拿下top2(湘安无事ai辅助版)
url: https://mp.weixin.qq.com/s/pupfhqB0rOMqDRQHDQtJ_Q
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:15:52.037283
---

# 记一次edu攻防演练又拿下top2(湘安无事ai辅助版)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tlibgKYKL9EvxenicZicqkwLsAQRibgwQabH8azoIWsv8CrLQO1swpzCliaEYLgCVeqOohHtPzriao09qKIDOzWGCy1N2747flJTDxJMdeus7TIxY/0?wx_fmt=jpeg)

# 记一次edu攻防演练又拿下top2(湘安无事ai辅助版)

原创

湘南第一深情
湘南第一深情

湘安无事

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**声明：****由于传播、利用本公众号湘安无事所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。如有侵权烦请告知，我们会立即删除并致歉。**

## **前言**

去年受邀edu教育漏洞平台参加魔都的教育攻防演练，也是浅浅的拿下了top2。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EstwFA5zWQsMQo5AAhm1fNvhpgK1hyBiaVbAVaNKzFwGyyXZVcK5ibcBQsufymgETN2rQ3mI4VMnDV8YN8Rj0lnoa3EX857ibvaicw/640?wx_fmt=png&from=appmsg)

差不多和学员成员们一起打了4w分，也是拿下了奖励2w块。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tlibgKYKL9EttohP2G08hK6Z27Gr3Eic9xYgXlgaVtwblRy3gZZicicib0WIrGia07xWtuyhfENh1foXlEvnU93hbRfmMbJF5ExrtqllTuicKzoQTA/640?wx_fmt=jpeg&from=appmsg)

## php审计拿下7000分

这里有个案例比较值得分享，起初是一姐丢了一个源码过来让我审计。差不多10分钟就出rce，很简单直接上了两个学校的shell冲内网了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Eub9WxHbjclUR7LeA0NggVNvibvFJuqbd8zXOTlak4Qnc3KYJXfWBpSzwHhZXYJP1z9O7iaYM5HzVb9DSzYypjbpTR3hTrFCyHWI/640?wx_fmt=png&from=appmsg)

打开就是tp框架的很简单，mvc的路由，第一步肯定先看上传（这时候还没有ai）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvJMy333SDU6YjXfib5GRib1KlCShpeCgjtzibMnp3qSMeqqD3ial8ibUdUXicE5dSUic7lgib1LQprmJkBeUSQC8XiaY6IA9umeY2ECaiak/640?wx_fmt=png&from=appmsg)

定位到Eframe目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EtV8fpM8VAUcztsdSTrEqfEltQ4Lib3W42BvwovCh87tHeP0cicmISExI1hKNdNJmTib5bmWmT62FibMGUSG1sjbaqsVnQC2pwKNWY/640?wx_fmt=png&from=appmsg)

Eframe下面的控制器的Uploadweb的方法实现的上传

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EuZI9vZXaMvu7UCqHKXx4ibW3ciaETkiaCXiadUy6Rt6Brvq3gnkLX5M4wsww0m1bSzgv6xibnsbhlZJ6AYuJamO9d6x7OPEWteEJiaw/640?wx_fmt=png&from=appmsg)

发现源码没有文件名限制，因为是base64上传

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Ev52HhbLXS5W3iaVX2WdMmz3jTr4LyvsRGhic6MJmsibnefpb9N7DABFHno4GG3zFhTtlHA6EqJfxJXqdGicW5qAPW0lX9aVVhner0/640?wx_fmt=png&from=appmsg)

直接poc上传 先传正常图片

```
https://www.lddgo.net/convert/imagebasesix
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EtIqiaE9hYruO2gQCWc9nZTtuoaI9NAH4etedaiaqgY5nxnUXbVVM0ESSXJibbKad4A5KFW2xUkswSBsPvwvsk6zTm7icshEdicojkA/640?wx_fmt=png&from=appmsg)

这里的路由就是符合mvc的

Eframe/Uploadweb/saveclipimg

```
Exxxx/Uploadweb/saveclipimg.html文件名/控制器名字/函数名字
```

卧槽，直接rce了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsTLs6AiaolQ1rHGnEeia12StaziaYxm7nURlZZzVUbKyJIVRT5NebFGZPAykeGQOKPzP3pXpF6GT8AjXia4XxvKkEWDGFyVxIOEMk/640?wx_fmt=png&from=appmsg)

把png改成php

```
PD9waHAgZWNobyJoZWxsbyB3b3JsZCI7Pz4=
```

上传发现解析了

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Euk43cIKKJAQrsbPNYRtIGkGfbUlvXtrWDjxEul3YibvruicA2qF8thbSb1BTjdh3rb6zQl1icO6yjeKavCunibricJLeSYtATsRN9c/640?wx_fmt=png&from=appmsg)

接下来就是猛猛打内网了，很可惜我拿的靶标内网毛都没有，一姐那个打了7000分

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tlibgKYKL9EtVqbMBH819Vca69X5O29ULxhXAlmS2GKibnOnebX2ibh2iaDZwbJnKLRicElJJ8R4PibokaUUQnDoMTc2MBlKfB7ncfSicXznOnZwp0/640?wx_fmt=jpeg&from=appmsg)

我的只有450分，被其他同行打过了。。。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EuylZ1DnPuFuE2hJ7BogxvYcEk74nu7kIWdNJfUPWUzx47JT2sbQwO67FM0nNsicR6a5uqIkduzozNabdO8fL7kc2RfI9YwNl3w/640?wx_fmt=png&from=appmsg)

拿到shell第一步可以去看数据库里面有多数据。tp框架的数据库配置文件都再config下面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsjzqJwgObV6eJu049sEuTaXoEFEYeskuDMwiabCDwTOvoZD6GjJhLpQ57Ia6H7S8jp12NicdQbdq4cDSl64xmIG5Riakbu2n2nVg/640?wx_fmt=png&from=appmsg)

找到管理员账号密码了，直接登录平台查看有多少数据。3w条用户信息，差不多3500分吧。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsxtxCCoibwkO1dENCCfdD9taygGbIYhiaQecEkWSuPlO7E382a11t4s6ib9zHJ6PS0liaias2ia1ryBrkhavzibbJicEBHibjeTrvfrHEg/640?wx_fmt=png&from=appmsg)

密码也被抓出来了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsMBDjSACQtXPxXBnOKwLBKI4zOuZtnAHrKHacEdWeuLaXH5IKmOyzgsEYCHgBQTxOtKXfwB5NgymVdDAiaqQpomfYTyWfpYmhQ/640?wx_fmt=png&from=appmsg)

直接rdp上去了，桌面有数据库链接工具直接上去看看数据库有多少数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EtE4QOtnGlop2h2YecvDVzogfjpqRO83MiaMib09x94onJjib8EuKicBWEfqITVNNH5gaUr4P03ng7HfiaCw8DNoukCo6XN2zXeemsY/640?wx_fmt=png&from=appmsg)

零散散加起来10w的数据吧，应该有3000分了

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EsHpibnjhLbLiciaiaa0GRolS0gduqn1RQnib6bapy7uasKDcADknGfert7FC6JEFkXdx1fGuvrcdTXxicSmnacIic8tvWosIaOuPlwJk/640?wx_fmt=png&from=appmsg)

后面全是内网一些数据库弱口令+ssh弱口令+win弱口令，上限了不然可以打1w分，fscan一把梭哈的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvuA2laLRFY9qibW012NaNZUqSVGterBMAiaccCA6vKnDNNL7zPVO6SEqgGvgV5PZfwCx4WiaicqFLEicM9aXAibMnkia3z8klBC8dQDQ/640?wx_fmt=png&from=appmsg)

## ai辅助审计再次拿下1w分

今年不是又受邀教育漏洞平台参加这个攻防比赛，然后这次又和学员一起打。这次又是第二名，但是有个单位上限了，导致差第二名300分卧槽，气死了，结束的时候我看还是第二名的，今天我去看第三名了。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tlibgKYKL9EtWIviaiaorNxsRyxnWWNB9Ams533WSUicrBR4OBAGvNwuvyjS6s5yNvMlk8jqcrdRnj8j6Z2CnZSmjfo3prtibMJHtOscqmJd8tA0/640?wx_fmt=jpeg&from=appmsg)

这次不是跟上次一样的目标嘛，上次通过这个源码拿下了7000，我想着让ai根据上次的poc帮我再审计一下害有没有漏洞，没想到又rce了，竟然拿了1w分！！！

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EvjO4LcVgQnk2haQicLMLlE5hiaicobRZ6H58ZLmTuJcdyFH9ZibRxh5ljun68Z4tEocxicndPTuGHumnjAqBQI8j9QVIZ5iaX78QBkk/640?wx_fmt=png&from=appmsg)

我是直接把poc给ai让他再给我审计一样的漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsuicCtH1dFoD1E02zeWXh26zfVwZdDgjOGM1JbJ5kMK5G0G1BU0utsOytruZxpRUtRQ4e0ey0WSH455cicT1ux74GgbJmC6ePV4/640?wx_fmt=png&from=appmsg)

然后就直接rce???不得不感慨ai确实nb了很多呀

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Eskg4WwXpia1l8BBGOAHDqjG3s9lxUhKsmvz3dztLwqib5GefsKRcaRWHL9cCAX6GgjzoXSqsNQ2F2aaAZyicaiaEmdHdgxjqL7TFs/640?wx_fmt=png&from=appmsg)

不太信，我就自己复测了一下，真传上去了我也没招了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Ev7kN8gyRib7nNB8TnzqfArAedibndLXBPu8pljLGSvYb8OP4zDroKUhAFUUhEib6gb3OXhIZ9rvriad9OuRoflhgx5ZlnQzmUH7Kw/640?wx_fmt=png&from=appmsg)

直接哥斯拉找配置文件翻数据库了，跟以前一样的

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EukEnGcenzmnhT4bGJkAT1Gt2tPkpGWEwY1AVcnqn1py7reMtiayFhwxogFPOjfgrLYAyoI9YZuvyZUT3LnoDbXeOrrsgNlB69w/640?wx_fmt=png&from=appmsg)

内网唯一要说的就是这台服务器用哥斯拉连上去，只能看D盘，我也不知道为什么，然后fscan用管理员扫描半天了，一个漏洞都没有以为被隔离了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tlibgKYKL9Etias0JO88D8xjct6o2OjfhWszZaXhOIjibaHYDhm3PGRqMRwpFC5lh8umJmOLJ4dVCiaeSL2e1HX6V9KJR3O5XXFkiane1qFfxoUQ/640?wx_fmt=jpeg&from=appmsg)

后面上冰鞋了，发现可以读到桌面的文件了，直接提权酷酷扫描，因为之前打过，如鱼得水，拿下1w分不是梦。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsCHwe7OpQsRBOGe1WNwdVHoREImJaaNJbLuR13PWgibyaEyUj1oTx3NTndG38S1rbIlBibJ0qGePPTfM2pYyOAicKvLTiamNed28Y/640?wx_fmt=png&from=appmsg)

现在ai都可以自己打内网了，不得不感慨ai发展太快了，要学会用ai，而不是成为ai的奴隶，当然ai的各种模型价格都好花钱妈的。内网说实话要自己多打就会了，还是得实操。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EshudMELWHiasslPkYhNFhp3Tl4zETmjzhrvNBTKuzQmcsUFTdg1fo7fBZ8F28EMIsT7IR37PnGHnO3RTw4xmnD8wbSS6ywCPBs/640?wx_fmt=png&from=appmsg)

往期文章

[2026最新版burp破解教程+ai操作burp挖洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495278&idx=1&sn=37563ab9c3aa7dbd0032d668c444579c&scene=21#wechat_redirect)

[湘安无事首推的0基础web安全课程](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495233&idx=1&sn=c213276f0a0e3114fadb2ee693967c5b&scene=21#wechat_redirect)

[学员挖掘母校实战案例+4月湘安漏洞库平台优秀实战案例](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495226&idx=1&sn=964c5d38716a725c251affa609579d9c&scene=21#wechat_redirect)

[从逆向加密逻辑到一键明文改包：我的 Yakit Hotpatch Skill 实战](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495182&idx=1&sn=c00c7fed753d2eb5c28c7609ce1706e6&scene=21#wechat_redirect)

["深入探究JWT：解锁身份验证的挖洞小技巧"](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495180&idx=1&sn=6d13c243db60ec14db5c9e8dae12b8b0&scene=21#wechat_redirect)

[敏感信息泄露漏洞总结：深情哥提醒你aksk正在“裸奔”](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495067&idx=1&sn=47d93faf7fa2632bdedef8da9396bf04&scene=21#wechat_redirect)

[985–edu证书案例之有意思的报告](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495097&idx=1&sn=dcb8c4a665b2030bf0e86d042f687ef6&scene=21#wechat_redirect)

[五一弯道超车！深情版Edu+SRC培训限时低价，文末免费抽奖(两份kfc+五个无影激活码)](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495149&idx=1&sn=9250a9e7ac52ec71c4a492ec77645426&scene=21#wechat_redirect)

[记母校漏洞测试一次waf绕过经历](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494963...