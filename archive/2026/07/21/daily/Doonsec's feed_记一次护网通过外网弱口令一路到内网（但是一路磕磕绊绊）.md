---
title: 记一次护网通过外网弱口令一路到内网（但是一路磕磕绊绊）
url: https://mp.weixin.qq.com/s/VxJfWQbyLJZi9Osv_M25Zg
source: Doonsec's feed
date: 2026-07-21
fetch_date: 2026-07-22T05:01:03.897486
---

# 记一次护网通过外网弱口令一路到内网（但是一路磕磕绊绊）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ianpxKPnLHoKwJe5ae8yHPSeXPxsTDCnbB9sWspOnCI85Pk3ibEzA23ibqwBGib6aLcIHe5W5QuNeCLrUvekSvj5FaIZibZGxQsO9lEic6ozAy76Y/0?wx_fmt=jpeg)

# 记一次护网通过外网弱口令一路到内网（但是一路磕磕绊绊）

zkaq-石英
zkaq-石英

掌控安全EDU

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - 石英**投稿**

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn  **）****

## 文章中涉及的敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打码处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行承担！

又是年底护网季，地市护网有玄机，一路磕磕又绊绊，终是不负领导盼。

扯远了-\_-!!，年底来了一个地市级护网，开头挺顺利的，口子很简单找到了，归属也很好定位，但是中间突破的过程就是困难重重。

因为是小地市，加上主办方年底也想出点成绩，所以对目标没太多限制，是这个地市的企业基本都算，备案能归到就行。

## 资产收集

那就简单多了，直接quake：city:”城市名” and is\_domain:”true”，大概好几千，数量还行，但是时间不多，总共打三天
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoILx1qoFdjpfSnnu8oUhKYcg5zBeLgvcZZrdyW1Jic8yJeJpXhr4rLPH65W5xlib9tw2Op3rkbicGJkAQASPMkWKTSyNvtUsq4PG4/640?wx_fmt=png&from=appmsg)

## 前期打点

先是找到了个某个企业的企业微信管理系统（伏笔），经典弱口令admin/123456进入
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIorOk4qZicEpjOtfyIgwZ7VOtD15YTpMTcnBXlkKhVrXYzhD00j4Zufic5CpsNWGLmNASePeJ94jY5UibFFl3X5dicPD1fWyUH2aM/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoImljPwianJBSEyVrMjqhohZ4o40EcGUk2AHYzGYtT9vjtPOdvSdNr4ibdGrfW0GEhTIBHRiam676icU99D76p9QZicYK1ZLBZY6GN4/640?wx_fmt=png&from=appmsg)
因为是护网，也就没开被动扫描慢慢找注入点了，直接奔着上传功能就去了，在素材管理处找到了上传点
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJicZCWSDCo7B6gpTn5HCQeic6mLqRTYktoE0qs6F15KHYVmxKNP0dVK2GXLu76PM5jsShW0ytw5ibxzhfEEsu0xka92Aic6O6QwKg/640?wx_fmt=png&from=appmsg)
经典的前端校验，所以直接抓到上传包改上传包的文件名就完事了
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKs3ia4zWtUU9mO1121kajo54hZgmoKxUr8K4qrTA6B3ia9U6jLzErvBuvVlic4rHBE5JRrtibiavTGTfuljfr1akkOb9UbSdCJnGGg/640?wx_fmt=png&from=appmsg)
甚至返回包贴心的给了链接（谢谢啊）
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIg5OS8kdlSBhQWXL71QOLlVm365fx8hIlIs6zENS2d2BAA2Hic26sD7nZV0PnO3NOxKRlBL5lt3NzSBaQY2pVu7EBM4HInSo20/640?wx_fmt=png&from=appmsg)
到这觉得这不结束了吗，已经想象到传里fscan跑内网，翻翻配置文件写写报告不就可以交了吗？
但是很明显我想多了，先是传普通马直接一剪梅的朋友-落地没，然后没办法传了个免杀的大马进去，执行了下tasklist发现有def，然后又whoami看了眼权限（伏笔回收）
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIibiabdVicdB5Gy6jiamGJhPSd0YGN5eRYDdquek0WLQJcxtAehFJdlDuDoHSqiaKorekia9kHKjR2YsZAkrU1WwsYkzVR0tdh6RrqE/640?wx_fmt=png&from=appmsg)
当时我的表情一定很精彩，这权限真的头一次见
然后这里我的思路进入了误区，就一直在想怎么把def干掉，之前有用过一些一键击溃def的工具
找了之前用过的，又找了一些新的，大概是因为权限太低或者太久远的原因，都失败了，都没能成功把def干掉
然后同事说里面有向日葵，嗯？有这好事？当即用上我写的读内存的工具读id和密码，失败，然后找了其他大佬的，依旧失败，猜测还是权限问题。
然后又传了gotohttp进去，好消息，连接上了，坏消息，黑屏，啥也干不了（https://gotohttp.com/goto.12x）

## 突破

正苦于无法突破，手里又没有好的免杀马的时候，突然想到，既然他只有def，那理论上Unicode混淆应该能过，所谓Unicode混淆，就是把木马中某些字段用Unicode编码替换掉，在替换了两三个单词之后，果然成功连上了哥斯拉
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJl47g4O2YZN2UcvE0Ha3PQ1rxfUMLjTcJSY1icrrqFqHMWP7SDEe919vao95n8yVOPogAq3mX8ktCuUFAYOf8kuOpw6hQnIVRE/640?wx_fmt=png&from=appmsg)
本来想着事情应该会简单些了，直接用哥斯拉插件提权就是了，没想到烂土豆用不了，执行失败，传里的fscan莫名其妙的执行不了，读向日葵的工具也是用不了，本来想着搭个代理挂着代理扫，然而甚至连frp和neo都搭不起来，我感觉我要发飙了，真是一步一个坎。
既然不让我方便，那我就只能暴力一点了，3389开了吗？开了！
直接petitpotam提权到系统权限创建Administer组用户
创建用户:net user 用户名 密码 /add
加入组:net localgroup Administrators /add 用户名
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIo6kPHcuPD6qchHicGGK5siaULBibMx5RvfniaFBwJjtkmSDKRAEnictHOD60sja0g0lpekxCyTM2rPkqTEiaP3groV34Mibt9icaBPmo/640?wx_fmt=png&from=appmsg)
然而到这一步，在frp和neo都用不了的情况下，那只能请出代理新秀，suo5！然而也用不了
再请新秀！grs!然而这次，这次可以用了。
grs用起来比较复杂

```
grs简单使用方法
使用时首先需要生成配置、客户端、用户端：grss gen www.qq.com:443 127.0.0.1:443
参数说明：www.qq.com:443 是被模拟的目标127.0.0.1:443 是服务器监听地址，这里要填写公网IP，端口最好和模拟目标一致若SNIAddr或ServerAddr不指定，则会尝试加载已有配置文件，默认生成3个不同id文件名的客户端，可通过-c参数指定
命令生成后会有三种软件
grss(Golang Reverse SOCKS5 Server) 服务端，需要有公网IP的机器上
grsc(Golang Reverse SOCKS5 Client) 客户端，需要运行于想要穿透的内网中机器上
grsu(Golang Reverse SOCKS5 User) 用户端，需要运行于用户机器上，提供socks5服务

简单来说就是grss在vps里，grsc传到靶机里，grsu在本地执行
启动服务端：grss serv
启动客户端：grscX
启动用户端：grsu -id 0 这里id参数对应了grsc的id，不同id会连接不同的grsc，默认生成三个
```

## 完结

至此，胜利的方程式已经集齐了！代理可以用了，用户已经创建好了，def，咱俩该算账了！
rdp挂上代理直接连上，桌面还看到了向日葵，还是全用户安装的，不过现在已经不重要了，直接把def关掉！
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJCnr5Fcu5muajDSWLMZsljoTn0t8Y3mG6faV2ZAevKlvIPiakQBnDicRibJMXndFjNOkg9x7YdhBaXlWsYTCxgsUlVRSrpNRicJl4/640?wx_fmt=png&from=appmsg)
传入fscan，上线cs！
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKgwic3jqsWodhTNjA0kZajUax7XxNUuIPR1Lt7OxPIStiaKC2CDbvrLLzXR6PQqicibWibKUIMQicb7uFfueONa6tSxzrQtb4ExuGrY/640?wx_fmt=png&from=appmsg)
几台17010，怕打蓝屏就没打了，还有一部数据库，不客气，连上直接上线cs
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIbaFicNW8We5osxPwibGly4h9hr4NE2XDqq62IwozkS3Y45LerE1kichViaeArDfxZEV0l8P9O4VhYN2icBF4hQeb7kwJfMgFNkjfI/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoL3xxfHOCt0B4WWUjqZicbxCTYQDZqBIxofDPn46hhbM8siaibYv8gySORxknuBVw5SManJNSVNI7FoPyDXcpfF5XFwUZZ59POafU/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoL93UOCKt0pgzOPjcqWyChibplfO0CCEJpU3nxAYz9cyLAUkUdlRK5jpwYuvpDYJib2sKJg6RjW3HxrBLicIIicicFxQgh23Qo0tUibQ/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLxDNibz7DPYbI8rHvgJmlOETOqTYSO3V38lb4IMvOrpLzlNewb9ZicmFwNkXbHmib864vwOjWdwcIoa9esnKMJuugqwOniazX5fW8/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJDl8sHgxXY5ibrKG38R1X6micw8z6S1r0n0tLp6rsaClYt8YG6FYbDdUn58Vo1PamzAbe8N1Y8OeydDIkw1vGbiaE6nH6KXKxG40/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIpojicqxpp8sy5tq9CWhyBooxvCU4auyIm0UfNfeheMhiceiau5F7zicric7gXcK4ZPiaKneuoaI147bYIvo0sA8z6zkDic4VVVcRd2M/640?wx_fmt=png&from=appmsg)
又在数据库这台里面的浏览器中发现了OA系统的地址和账户口令，还是管理员的
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoK56SzzNyNUE7OhVX8AKfAdQmrLbWH7o2HNtoD6VAOhwFIwic0YOn5Wlm3aNkwic4hyCr5iaiaD5W5muf6PuEWlXKAZy9uVSIxeUfU/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKn1wDticESRy8NZGExN3f7M7EBaBECfXicVR3Lp1fpThmSSicgapkVCF8TetKBQfzjG9URT01WyKuf1X3icfahqFJEkDLEfxpPduo/640?wx_fmt=png&from=appmsg)
剩下的就是一些rdp和ftp的弱口令了，截图我就不放了

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=34)

**没看够~？欢迎关注！**

**分享本文到朋友圈，可以凭截图找老师领取**

上千**教程+工具+交流群+靶场账号**哦

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=35)

**分享后扫码加我！**

**回顾往期内容**

[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)

            [文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)

[重生HW之感谢客服小姐姐带我进入内网遨游](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247549901&idx=1&sn=f7c9c17858ce86edf5679149cce9ae9a&scene=21#wechat_redirect)

[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)

[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)

## [代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247503462&idx=1&sn=0b69...