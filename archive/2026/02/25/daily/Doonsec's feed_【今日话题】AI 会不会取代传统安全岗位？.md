---
title: 【今日话题】AI 会不会取代传统安全岗位？
url: https://mp.weixin.qq.com/s/4OO9NYOfJBiSBj7u24h4Yw
source: Doonsec's feed
date: 2026-02-25
fetch_date: 2026-02-26T04:10:10.951107
---

# 【今日话题】AI 会不会取代传统安全岗位？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a3etiafIAYXEkJmPumJINp4GImgUjNh2fACqQfzqI0mMsmdZe7pX2XFrh4Xomg3edB1yK6Q5GXDAbW06IXUlIphQ78kIAIhK1asuXchWjXIE/0?wx_fmt=jpeg)

# 【今日话题】AI 会不会取代传统安全岗位？

原创

ChinaRan404
ChinaRan404

知攻善防实验室

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/a3etiafIAYXH4SovKwyzSycUc28ibF2Lw9ZTDqlTMGtfGGMaGOXvPvGiaddvaZkLITs22ayj0ky23JC0xN1oN8t7wHzHicZ8T0btV5icBfF4krj8/640?wx_fmt=gif&from=appmsg)

前言

![](https://mmbiz.qpic.cn/mmbiz_gif/a3etiafIAYXEGOAaumShEAwvH20Pia3b7Ungo2uAQP5ZWPjZmSoDFoibVicWtPv02gs4AlVvF4fomm0x4PTiaen9FIYuicv5piaBFTaW2rE5Kwvuq0/640?wx_fmt=gif&from=appmsg)

一直看各大安全群聊都在瞎吹 AI 替代谁谁谁的....

有时候真的很无语，那么下面，且听小编分析。

先说一下本人现在研究方向，最近在做 AI 应用、AI 渗透测试、AI 自动化攻击相关内容。

![](https://mmbiz.qpic.cn/mmbiz_gif/a3etiafIAYXEubzJeteat5Dz5tPzFick4icwD7TcqUXsyEiaiaIcy7jxczyIDmoJvlHD3hW5Cu4ctGoHNLPVJHp6NibCG9CiaL0VU3JdI7S2RCYIbY/640?wx_fmt=gif&from=appmsg)

论点 1，基于算力。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXH18jS2FiadO6UbntHVW6btKyxYZ2gYKpSH8QngA97iar1qsqNF1EA8ZbUL9GLva009X2haylCpx3IAMXzpicbFYeXicpVVRJKf6iaU/640?wx_fmt=gif&from=appmsg)

算力限制的死死的，只有慢，而且非常慢，目前水平完全达不到替代谁谁谁的......

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXHhXtusuaTVia7HfWMEbibrn3FMe9AqIjKcKHSaCOc5OYt9eYQrcU9efo7val5tYC6H6lNUrr37xw8IjpUC0NrNR7ibdgcSvUIt3o/640?wx_fmt=gif&from=appmsg)

论点 2，基于能力。

![](https://mmbiz.qpic.cn/mmbiz_gif/a3etiafIAYXEKud33c2GFMOCwzm418nKgHc2pqMgXgtwIb9RJDXwYCrn8yTeianibY8kXibicqibGQRGfu39ok82wuTXBWQxTIYQIDXndeXXybMCc/640?wx_fmt=gif&from=appmsg)

 我承认 AI 的能力非常强悍，基于静态代码审计也是非常的厉害，但是目前我还没有找到让AI 自动化挖反序列化RCE 的技能点，我目前实现的是“静态代码扫描”+“AI 判断”，这个可落地性很高，但是更深层次的漏洞 AI 审不出来，还得是一些大牛师傅审出来的权威。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXFxpqhvrCGAQlUEhkYF2iapwEfzzg60jesVyNKh0hPMTtIezZ5tSR1tdU7CrlH5cymHHhs6R23yJicy9ruIRfFcbVTDicW2cHtwlI/640?wx_fmt=gif&from=appmsg)

论点3，基于实战

![](https://mmbiz.qpic.cn/mmbiz_gif/a3etiafIAYXHh0yibOVHdHcq874YsCXjJxgF7CgokJ3GkrkNjXWic40tOWTTnMPc3mb7icovspYKnt4YPgmcPJANkib44xJSPEfB6In1Erib2gHN0/640?wx_fmt=gif&from=appmsg)

漏扫+渗透无非是调度工作流，让 AI 知道什么环节用什么工具，其实我对这个非常无语......我看了几个 AI 自动化渗透的项目简直是拉爆了....甚至说与实战毫无关联。漏扫无非就是“信息收集”+“nuclei”+“爬虫漏扫”,固定死工作流，比如一些商业化漏扫已经做的很完美了，非得让简单的事情复杂化吗？真正在意的应该是自动化利用阶段，比如自动化 WAF 绕过，某些小众漏洞自动化深度利用探测，然而这些目前水平已经是非常非常简单的事情了。

还有一些逻辑上的漏洞需要大脑进行思考，那么就需要照顾一下上下文.....那么就避不开 Web 流量，那么请随便点开一个网页查看一下有多大。

![](https://mmbiz.qpic.cn/mmbiz_gif/a3etiafIAYXHNW203ogYcxwzDQVyhThDlAFsIgx3bqVMabv8t2ouNze15txLNYWsX4LNhrpQAyIAFWH4uRHdaR1UBbax5cofVmt8gHjryTuM/640?wx_fmt=gif&from=appmsg)

论点 4，基于入职

![](https://mmbiz.qpic.cn/mmbiz_gif/a3etiafIAYXGaL8yFxf5nicXHMOjCu7JpVQ9UGeBQ9x5trxUBNN1jnzuQuGpuWQLibdIshmOAO1UsQIEIrzoRQOhJib3W3uXpYp73oK6vrLFlpA/640?wx_fmt=gif&from=appmsg)

bro 真的不会以为什么都不用学吧....等你面试的时候，面试官问你会不会 XXX，你说 AI 会=我会

嘿忒！

![](https://mmbiz.qpic.cn/mmbiz_gif/a3etiafIAYXGnvvOh4YrAkbz3a4icicnuA2kyjftI2TNvI25pYQt9K7wx4SLJRmDDoH9rZEUJicyjoNQLKFGadlC95FsYqPdzgS5E1l1E4F5TVc/640?wx_fmt=gif&from=appmsg)

论点 5，基于媒体宣发

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXGbJ2sfWYkbWusQwGiblhEUa8Diay9gbyxiaQbd5sZq0M83DoELicWAMgiaMkc5Cib72xgMN5wwt1sz4j1iaQnNzKKJ1KEc31q1hxd9F0/640?wx_fmt=gif&from=appmsg)

有些人真的是试都不愿意试，看到哪个媒体说 xxx 模型多厉害就觉得天塌了。（这类人群占大多数）

等你实际去用一下的时候就知道什么叫过于自信了....

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXGzotxkV66J6j3vWcyHoib2KBVGRkiamx8v72rhXek2wiaicrA812Lgn9QDUaR1zoscKlsn0ueIL7JDDmpV9SCibfumZKQNAibkRIWwQ/640?wx_fmt=gif&from=appmsg)

论点 6，安全性

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXHJbNEqFiaNFocreiaP02QhYvT3c682gzmMg19d0w5luAhWUr9XO0xINKlxQj6ibiapDxu06WV3cYc4dMZ3YHXqap2l6XVFSbtdJqs/640?wx_fmt=gif&from=appmsg)

AI 删除，见多不怪了

如果 AI 不能替代你坐牢，那么你的岗位不会被 AI 替代。

![](https://mmbiz.qpic.cn/mmbiz_png/a3etiafIAYXHafjnx0cY1tiaOk8o3GRCIm23fCp60NicfHEOoWSsT3TW4lewWicTsyUFRzeczeFIY7tUtRtppl2NSDoHhAgQAYic0REYuYhRjOSw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/a3etiafIAYXHwodzcgusFh7FlDribW73giaVPyyoUq9V9cvh3a3ZbWoLgHETmcdicgRVib7TEDnWMd8QnlNTxIYTIYuhvquTLCicjxy8dxnrHXPWE/640?wx_fmt=gif&from=appmsg)

个人结论

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXE5F7NZPzEGQVELZfoYfhGRuAezGj7hr67tvVsVWAJCE3z4RQibpJKXTu7pWKEPALia4SFbwhuCv1kLtP9A7ZTwTkNroSVt8Y83E/640?wx_fmt=gif&from=appmsg)

替代你的永远不是 AI，而是会用 AI 的人。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXFx9lIUF16IXNUnqpeprib7smYpia8AApNciaucOc8bmHhCsYJ4JOt1Ts0W7biaCfQt4Ad2tayjnGVjLggmhJ5HqAbD6U4Qd46t4oM/640?wx_fmt=gif&from=appmsg)

最后

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXE8C6t0sBo30oukEicrgR1ArZMXooJpwyrnEn4du0YpibbKSAemSHHK2dibPbkfRgXVypPlVnsgRcLhYgCc0pjibbcicqtyeuZ15CT4/640?wx_fmt=gif&from=appmsg)

信我是秦始皇还是信 AI 代替人类。欢迎留言区讨论。

交流群

![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vpZg1GJFRr5FfOWiceYib55FMIz0pobrCALAgwmoq0631MRPhZQFO3ia4UbTIibDPMIQ66KEHxib3RUbsw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vpaa3t1HRmibZdUyUIV26B2MicC0Pdssk9I8XMhaLthiakFkJoPdL4fwjibWEOuTdXxu4VibxgqQ7yl6yg/0?wx_fmt=png)

知攻善防实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vpaa3t1HRmibZdUyUIV26B2MicC0Pdssk9I8XMhaLthiakFkJoPdL4fwjibWEOuTdXxu4VibxgqQ7yl6yg/0?wx_fmt=png)

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