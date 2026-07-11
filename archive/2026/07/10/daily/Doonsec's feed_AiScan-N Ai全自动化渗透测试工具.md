---
title: AiScan-N Ai全自动化渗透测试工具
url: https://mp.weixin.qq.com/s/5zi8VJP-soq97hTRAaW10g
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:00:50.929783
---

# AiScan-N Ai全自动化渗透测试工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/niasx7fyic9CMwKsN6MJzOpFFEuXLBNhliahicGv5ORB002aBXULO1L5OOrnIw8cbmTX2MEHlEAaSjqBq5ou7GNYRnlLaDrHFWjfZP7qVn2Vn00/0?wx_fmt=jpeg)

# AiScan-N Ai全自动化渗透测试工具

Yhsec
Yhsec

C4安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

CTF课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/niasx7fyic9CMs6pyt2xl3Ng0QWByv0oD67COatsbL7SbcLetqC6mr3bFalmibIID1ricPHNl6xHHrqjmb0vLc7Sm0ficuiaroLKTJrNDibIPJwoBk/640?wx_fmt=jpeg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=1)

#

专注于漏洞挖掘、系统化从基础入门到实战漏洞挖掘，包含团队自整的挖掘注意点和案例、渗透经验、SRC漏洞案例、代码审计、挖洞思路等高价值资源。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有优惠券。

#

文章作者：Yhsec

文章来源：https://www.cnblogs.com/Yhsec/p/20186763

前言

这是一款基于人工智能驱动的Ai自动化网络安全（运维）工具，专注于网络安全评估、漏洞扫描、运维、应急响应、渗透测试自动化

AiScan-N项目地址：
https://github.com/SecNN/AiScan-N
![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMSwbDe3iaXZ8dYpsuwvpNZw9TcLcjfbs0GGqq5pC7TZWZC2eB476ywhkIflr3LWkibe6fE0eHwGcOh8u611j1J7eVcibMUXMNSGw/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CMwTYb3z1BEmACO85iayjmdw5iazFsNRSrPl7ESY6fxxC3nYXry5TzSupK9uoibHcVmOVTssialnmrBWeTdj2ZEeCmniarcicghkXwT4/640?wx_fmt=png&from=appmsg)

使用

这是用kali启动之后的界面
![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMZkOF45vMPXm5zlm4233vB7VIs6v5jMzpbzMJVl5Aoganm8UHwkibjAAoJCU7CZMOz90Q5n65HkL3Sw6jJoT97xUibO1ibVHC1FA/640?wx_fmt=png&from=appmsg)
工具需要通过mcp工具被调用来使用，按说明操作就好了。我这里用的是cherry studio调用的mcp
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPOm6jzeQfwGMMyZfKCOs8KHJPdTa3hMniaUaIHmYwPS9pFT3C68fZPWObZPiaKTgSkClgSVboWBzzXG71YOks9uaKH4AibsAbUCw/640?wx_fmt=png&from=appmsg)
官方也有给测试的题目网址，但是为了更真实一点，我选择了2024御网杯的题目进行了测试，我用的模型是gpt-5.5

题1：bluetooth
我们将蓝牙流量包下载下来，放在kali桌面
自己手工用wiresahrk看一下流量包，发现有个flag的压缩包
然后 开蹬！！！！

```
提示词：这是一道CTF题目，调用wireshark对该蓝牙流量包进行分析，流量包路径为~/Desktop/bluetooth.pcapng，
请帮我提取出其中的flag。提示：这个流量包里有个flag的压缩包
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CMNdxoOKKp1VUKDP9sib8uG4D0TxrVCABlLNLOMYSEvZUtUChEXCmaibJRiaqQWBdXwttFyKRpYz8bW8xyfbGkbVz2DttibREwYOBM/640?wx_fmt=png&from=appmsg)
很快它就调用kali里的Aiscan-N进行解题，并找到了压缩包，发现要得到flag还需要编码转换和异或操作。最后拿到flag
![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNSoulDfbHia7RZTNZrNic37AQwy4BbuCE779iawKficoq0y2qX9OVtvY5iaBiaeeAaiaJ0rD4mxol45ia3yd2sW5BDlpgaEjnSn678LCQ/640?wx_fmt=png&from=appmsg)
题2：ARM
这是一道简单的逆向题目，跟上一题一样，我们写好提示词之后直接开蹬！！！
![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPzwI4Dfpjv4qyibmn30icJTsWD0UTnekBiaTxtFFQ3PBp3hQl8V8ibpUXXPCPoTZrcBTEMxkCoibMdHV6icpMFXj2k50cVYvJq4LemM/640?wx_fmt=png&from=appmsg)
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CN3cDPH7sZkvrpIlGBGhmSbhBccGRzcGGQicAG8LWKjoOT4QH0DMcicSe58LbupQ5z3MPuZBdVvDQCKZ61fpnQJmlaOibPTJqKNTA/640?wx_fmt=png&from=appmsg)
大概花了5分钟的时间就拿到了flag并给出了解体的思路过程

此外，他还支持渗透测试：

```
初始侦察：识别目标系统和开放服务
漏洞发现：发现ping.php存在命令执行漏洞
权限提升：利用命令执行获取系统访问权限
横向移动：获取数据库凭证和其他敏感信息
漏洞利用扩展：测试文件上传和XSS等其他漏洞
```

---

---

**内部CTF课程上线，总课程30+小时，优惠折扣中！**

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COmTqWiaO3MWicicQJbYDnl4VtJ8A6fkm0tBKFYBxbeKj9d35HJcpgSf7moVawMYwluFS6omJiaTIxPOSM9Fx6qLLZTXhU6sydlZ4A/640?wx_fmt=png&from=appmsg)

**帮会简介**

《**安全渗透感知**》是FreeBuf知识大陆的重量级帮会，帮会致力于漏洞POC/EXP、红队攻防实战，是系统化从基础入门到实战漏洞挖掘的教程社区，包含团队自整的挖掘注意点和案例，还包含分享的渗透经验、SRC漏洞案例、代码审计、挖洞思路等高价值资源。

**内容框架（持续新增中）**

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COd1ITgnGXHdVfC79DficTDDlYBibvNAC2VSwy3LDNBdxsgqbx8lUH5uUwjicLYYf1Ee2a8bmKlC8NnvYDtzfmfia7PoC6ytYX05u8/640?wx_fmt=png&from=appmsg)

**目前已有「700+」小伙伴加入了帮会**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CN9CVSeMYUIpW50058icjreeNHRMK7jEabMtshNf15j1IHvicDotNG4ZnfrQcwHDroAooj6kMIonH8FWgcu9bUjN7n6aEXyQHrFo/640?wx_fmt=png&from=appmsg)

**加入方式**

目前帮会成员**700+**人，**永久会员优惠后只需****69.9元****。**

随着人数的增加及资源的积累，**之后永久会员将****涨价至99元****。**

有意向的师傅们可以扫码加入我们，共同进步。

**如何加入帮会？→****安卓/苹果用户****可扫码使用优惠券↓↓**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CM6ibbnnP7rXgGwYFRYlibVVT4XXhCuXXUpn5qfC3MHudTZhYiaomgeFjopTUxkMnRs05icfPEH8DFgb4o8RMxTHtJNlUFBiaufCtSU/640?wx_fmt=png&from=appmsg)

**→ PC端用户可复制此链接到浏览器↓↓**

https://wiki.freebuf.com/societyDetail?society\_id=184

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

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