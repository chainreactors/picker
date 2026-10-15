---
title: 一个skill让哥斯拉Bypass D盾HOOK
url: https://mp.weixin.qq.com/s/HRrAKDwQi-57KFLmZAMbTg
source: Doonsec's feed
date: 2026-10-14
fetch_date: 2026-10-15T06:43:08.741371
---

# 一个skill让哥斯拉Bypass D盾HOOK

# 一个skill让哥斯拉Bypass D盾HOOK

原创

Joy
Joy

安全很忙

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 背景

在实战攻防中，部分目标Web应用服务器安装了D盾并开启了防护，导致webshell无法正常连接，即使连接成功，也无法执行命令及文件浏览。

本文主要演示让agent使用skill来bypass D盾的命令执行、文件浏览防护，仅供技术交流。

skill请从星球内部获取

![](https://mmbiz.qpic.cn/mmbiz_png/icEiaxZSAJibhnWWCgKC7f9O20iaPrzpovp9p45cgkZJ5n80E9rhohIHVFSFlrSAcW5koF2ldTibUxdCyaeD71xJ13gn2gYUImAwfibv7JWrNafhU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icEiaxZSAJibhkXib0SqM3vzAqPt8Giaq0E2j0FNworNg1z2sAwicu3CicBicqZ1Z2Go2bPO8K0fospVczRjd7kkM0yic0kY2DNQD5xrAEa0lfEwy25g/640?wx_fmt=png&from=appmsg)

# 安装Skill

首先，我们让agent安装skill。这里以Zcode作为演示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icEiaxZSAJibhmV6rqEmBPHmypkWww8EM8gHq6W128aibXT5QoFVrpJ34xWGRHiaNNXRXY6CpbAZ7biax54YG0x6q0GSNuqDvrFS462HJyltADLUg/640?wx_fmt=png&from=appmsg)

安装后，需要重启Zcode才能使用这个skill

![](https://mmbiz.qpic.cn/mmbiz_png/icEiaxZSAJibhlzctN7JZR1A5gJugVS3J7w509JdhibqfdecqTZgR1x90AuV84fWUaibpmFpnia8qg6j6WsclticuPypgEKZvQmY31c6RKsG41oDSw/640?wx_fmt=png&from=appmsg)

# 修改代码

重启Zcode后，通过命令“/d-safe-bypass”指令让agent修改哥斯拉的payload代码，实现Bypass

![](https://mmbiz.qpic.cn/mmbiz_png/icEiaxZSAJibhmjrAmics3y3E15vOr1vXADLzqdXPyjwqia1ObE2EBPGPrZpia1E6UJALKBVDT6kHNia8tMXnYbiciaeOzEJRYS5k9WkThyzVWHraIVQ/640?wx_fmt=png&from=appmsg)

agent读取skills并开始修改代码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icEiaxZSAJibhkmDZB8mHeJkDL8f8srib4uhRoObH6slJZicicEumNETllnmnia1Cf6LMPzqTSwnxwEx8P7zQdXa7Sg6QGOHxLNkovO9OZBYNSKiaU4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icEiaxZSAJibhkmQNposcalH5U7LmIpPvrfgfFV9NWEmicJl5oGwFhMTDJ85iaSCert3VyFeQwoX5Z3CqrWXmhONmBTBnmft2051XSNqUVFr44XM/640?wx_fmt=png&from=appmsg)

# 效果测试

通过观察D盾日志，发现记录了webshell的命令执行POST请求，但是并没有拦截，因此Bypass成功。

![](https://mmbiz.qpic.cn/mmbiz_png/icEiaxZSAJibhnL8icichkvacy6JOnGZo0n6uSeubgGsTVdKXIxpaVN2Z1CLaffHQiaOrkDrVxtOSJKB6juFiaTRu3via86iatdfImYXT1rJ8483EicHE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icEiaxZSAJibhl4Cicoqesq5NSqeQ5TKz4Uf8e7viajPp10KJvfibxtAP8yY1gTMWkquJjkOvMwuGHBuCp39ulT9gvrgwKxjruv8e5VrfS7gu6pJk/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZoMH8QJVDfOZxDG0a7Y9rnnQhswjACn0U57PWMdATS0TSJLO0ZKNRibYILiaYl5ns7WB1VaXhWTHphEGOIIaVeLQ/0?wx_fmt=png)

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