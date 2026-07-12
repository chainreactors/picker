---
title: 轻轻松松实现账号接管
url: https://mp.weixin.qq.com/s/wWoXYjV8dk8pcljP4V6bYA
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:09:00.266807
---

# 轻轻松松实现账号接管

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/72I8gAalpPVQdaSx3J4jqnvWhlRdrRQEiagvcQQTBsSrZ1ELibJbUbw7rfolUUOibJ9ib9xvlW0Ggx78kRicHd3RibicrlTXC8v3pk8ibxKIJ6UMoDM/0?wx_fmt=jpeg)

# 轻轻松松实现账号接管

原创

pippybear
pippybear

安全无界

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

声明：请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。

这是一次挺有意思的登录绑定绕过，现在回想起来，还是觉得开发老哥这逻辑代码写的和开后门似的，话不多说，直接上正文。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPX7G5XvakZAfRNr1j5OAB3qFqHQgxicuePBrTIoSlFuuia3tlv6Lx0iarvvNMZqXGHERJaxibJxbibpsW1F7L7ykyS53C6VCQ20C11s/640?wx_fmt=png&from=appmsg)

开局是一个业务系统，系统登录方式支持微信绑定登录，emmmm，既然提出来，估计大家已经猜到本文的重点就是这个功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPXhiccpEFJdUnic13QFJkkU6yeczYAibdqBYmrroQfhlaCkDAsLibR13gljrjNcW0UMKXAtgewCI4D9iaE4qlILP2bwJHwOvGkjSShk/640?wx_fmt=png&from=appmsg)

直接使用微信扫描绑定登录，登录过程抓取到如下数据报，入参有3个，token、手机号和openid。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPWEH9Ml9XoMY9tOIBCUQB9cnDVM8Z81IZD8MJQJvA7R5ibsSCl4NXaDicQbXbG4l8h0Ky8FnoODiagdibBjcFvmbhjtg0ZJ556alSA/640?wx_fmt=png&from=appmsg)

任意修改openid再次发报，发现这个openid居然还真是系统给的身份绑定值，但是这个值似乎也忒简单了点吧，openid作为入参凭证能理解而且大部分情况也多数如此，但不能这么随意呀。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPVQX8Z9wcpD2ibHuAkdZJUibKdvVicGcIc9qVaCKASIU4SR5exryFQZg2S42gNKUbbsJXwqicUl2M6HSVJFS1zB1JJibfV4uxjaUols/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPVbeKfjGMaN3gNkicN83o2RQyRP8d8icIN9eGOLsmjs6Mq0xmmiaiaTiczic4NH8YAv7X86cGoXyiba9Hr47D3ibuCpUMVO6ap4pmmKS04/640?wx_fmt=png&from=appmsg)

通过遍历openid即可实现任意用户绑定，如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPXg6N3KWsj2fiaTicXwQkwrico9tZPNK9q9UKdk9ru8JU610f4kXLtvcJf5652rcRxUicsxIafkl3WBHryFqzgPCJJcwBI60KTwxqU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPWd0WCKvQqckx3w7c6S2jur0uibjz3f0Nr3HWIYL6P14jaYVwmX73F8O2VFY83IUMQ6wtdXfQXtQPz9FBiaGsNWIEicL0eQNGUjzA/640?wx_fmt=png&from=appmsg)

看起来是不是不可思议，其实类似场景还挺多，大部分情况下openid还是不易猜解的，不过总而言之，大家遇到类似场景可以多试试，说不一定就有大惊喜（不管是openid泄露还是可猜解）。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPVMcDwKpfcwOcHc6OufflQ2I9wIYY3ycVgMejoGnN0ibsdPXce3sF57T4n365uHS6XTiarOQg2gjzA8ck5cYddkWkKGM1IgCp95E/0?wx_fmt=png)

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