---
title: Z3r0：全流程自动化渗透/挖洞智能体协作平台
url: https://mp.weixin.qq.com/s/u9tLt_Zn1xz1MbOgvrQzTA
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:58:55.688005
---

# Z3r0：全流程自动化渗透/挖洞智能体协作平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/niasx7fyic9COxASJX1RpnwToTe2xQmAXR78lZrDDhUEiahoAk81BBKFy9pmQayQp72gvt9laoa5Oy2bHX3654l7Kk3KfmiaHfIM8pch1xaKr9Q/0?wx_fmt=jpeg)

# Z3r0：全流程自动化渗透/挖洞智能体协作平台

喻灵yv1ing
喻灵yv1ing

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

文章作者：喻灵yv1ing

文章来源：https://linux.do/t/topic/2203989

项目简介

最近在做的一个项目，想解决 Agentic 工具在网络安全实际工作中的协同和控制问题，把**任务拆分、情报搜集、渗透测试、逆向工程等收敛到一个受控的安全工作台里**：既可以由 Agent 驱动完成自动化情报收集、渗透测试、逆向分析等任务，也可以由人工追踪任务、接管流程。

基于 Docker 的沙盒集成了 Nmap、Sqlmap、Ghidra 等安全工具，并提供终端、VNC、文件管理器便于人工接管沙盒，实现与 Agent 专家团队协同工作。

项目地址：https://github.com/yv1ing/Z3r0

项目截图

工作台

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CO1HjtQITll7yOevHHSqXrasSoXlDYFQvE3Hz2wDibablJKcCvlY519AptibOzmECMM3bBica4Vnfiaj62Iy2tdvFCCGUnnFAmFYq8/640?wx_fmt=png&from=appmsg)

解决 Web 题

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPJHWBNgueNJtPkJRXcFqXYO4nZzHuFXGjZxRicaxPnwzHhjL3Ecy0PBVVF1cpAB2jDTNNzAwSibgr5NRHoSVwPSibYp1ialQ9aLBg/640?wx_fmt=png&from=appmsg)

解决 Reverse 题

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMdfOzrXESS0EuVBjbOG7iavrV72uEbMYSJkqME2tUSkiaIdMgydV6oHyJF7lia3yvwCFth869kffzJrJnHaT4H2gru2BAZxLpf4I/640?wx_fmt=png&from=appmsg)
正好这两天有场 CTF 比赛，于是就去报了个名，自己全程只把题目信息丢上平台，过一会就能给出 flag 了，体验下来还是不错的，**花了大概 2 个小时就 AK 了。**

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPG9icSMJRuxJbQMpmFyDJAaXbMlegwiaASt6fdkzhNXjMdLn6yjAPhnJDxGYUoRAj1scSkln4JH1tpen9NnyVIQ4Mqb32OxdeKQ/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CN77s6vtVHwibKrluC1Skb01LCyap1YucK1cxwRDwu4kDJKAHgwibGf3txndGSWCaWOzejdPJd9ibX7jLIRH0WDY6SVXqTlayWDyA/640?wx_fmt=png&from=appmsg)
**但 Z3r0 想做的并不只是把扫描、测试、报告串成流水线的机械式操作，而是按照真实的红队协作方式，由情报搜集、代码审计、渗透测试、逆向工程和密码学等多个领域专家共同协作，形成一条从边缘逐步触及核心的攻击链路。**

为了做到这点，Z3r0 不再使用线性的清单来记录任务流程，而是通过图结构来承载整个行动的过程。具体来说，在 Z3r0 的内部版图中：

```
点是资产实体
边是资产关系
```

由资产实体和资产关系构成的图，就是信息搜集得到的目标架构。在这张图的基础上，Agent 团队逐步探索分析，标记可用的点和边，最终形成一条可达的攻击链路，而附加在点和边上的 findings，将作为审计和追踪的证据留存。

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMlsdhlKApnxY7wLtibjEHpkluvtbnWBQmZ9OaoZHDdt98wJhEso24I1wVe8Q2pbdCMYr1REX1TCl3Sgl4DGdAJoRTR9hUbwRyY/640?wx_fmt=png&from=appmsg)
初步引入 **Loop Engineering** 之后，想检验一下效果是否有提升，所以今天找了个靶场，开局一个网站入口，从信息搜集开始，一步步完成外围打点、程序逆向和内网横向，最终环境里的 11 个 flag 里成功获取到了 8 个。

唯一的遗憾是内网的 Shiro 受限于没有使用 VPS，webshell 没法很好地发送 payload，加上钱也快烧没了，就没再继续深入了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COHwZwliawr6C9OcZxSibvdGgzWWyGNfplJP57vF0bu31icKWibCXDTQBzC6CicYrmgQuNicgFw5pr7rXoPbslVFmHGIsynfgMIuxy4Y/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9COjxo8fMia5RKpTEubBShe0yGO9WWJIQFQjVZLwicMBhrNoDeYX9HcCl0iaib5GvHx9vicEN2q37j39EAzgPQTayCSpe3EYrtle1uc4/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPYFzKZBuyAKRVvakTWicicWS0ibF6yOQEz8bia6yelVZOBpOIxISUz0x02QtPkftUgtON6EfVNfjEpq9uGPiaTJh2ejjH83QPPUlI8/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CMF30VicMibSpfDibsfA3RdF4cWHWOyjy3c9pR4iaYr8IQfqEN6zM7qzCOcEjKh2q11oJD81sYe8DN2lCcIyhVsHmfYwxnupz9icDbo/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CM7GriawscoiaHkqlmRicBp4BgtFomV2vqE9FvFJbNl6WgPWMBicibL4J3eMx2FnABBdSFWsJ49ce2KLXf0mCG4sIXI29jFucPlAUD8/640?wx_fmt=png&from=appmsg)

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