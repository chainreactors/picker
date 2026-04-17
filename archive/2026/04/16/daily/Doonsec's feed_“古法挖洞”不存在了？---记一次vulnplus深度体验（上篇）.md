---
title: “古法挖洞”不存在了？---记一次vulnplus深度体验（上篇）
url: https://mp.weixin.qq.com/s/d6etfN_1jFCCjwsCaJFckQ
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:42:38.998698
---

# “古法挖洞”不存在了？---记一次vulnplus深度体验（上篇）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9UFagAZOGD90mWA3xibo3nYwQoj6NbTMwlcTO0gvqoRjqgcSK1Jb6sLT9AyEIavxqIIyhmBiaiau9cCia1A7FGGdvicJFGjicEpqV5bgJhgia8IiaMo/0?wx_fmt=jpeg)

# “古法挖洞”不存在了？---记一次vulnplus深度体验（上篇）

原创

Fisherwithfish
Fisherwithfish

愚者sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**“V**ulnplus真能替代红队？必须细品一下才知道了**”**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGD9EcVibtchdmJcmj4klwwDZWaiaOnFdMia2icElO0PAc91pVrOX4agVaSpFib0lXyhBNqSuOUeE7vYkB1rOjtMbxV1icicHBhYbe8QdkQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9UFagAZOGD9rXsBJkWEDfaXnSVObFA6NEicMmZQmXaLeCvq3n3LPOMSWBib2o8U80DklC5Wa69dRpNFuoiaSR86MUs6r5XriaoRtqbGhdYmxQ0s/640?wx_fmt=png&from=appmsg)

01

—

账号申请

官方还是给机会了的，直接朋友圈集赞即可。发朋友圈，集赞，一气呵成，赶紧整个号来玩玩看。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/9UFagAZOGDibNpbpm5FGNCXwVibj2tKEVur3YlxT2SYrOFMicyfE7mQWBzarn5icTNfib4duTLK2QaqC9v3QvK7jiaMsz3Sdvas8PffuicjaaGeibt0/640?wx_fmt=png&from=appmsg)

下面是产品的公众号，详情大家可以直接去看看就知道怎么操作了

    这是官网地址 https://vulnplus.dasctf.com/ ，集赞成功后，去官网直接申请即可（唯一对于学生or个人研究者来说不好的点就是必须得有企业邮箱）

    拿到给我们的账号密码之后，直接体验即可（这里必须要用企业账号才行）![image.png](https://mmbiz.qpic.cn/mmbiz_png/9UFagAZOGDibxpxOelG8gTWic25iaqEzgFxr77CDqrRiajdAneHuwYQHn1b1rSVbVaM6HVBtQibCzxZMgXB10jX9FMwHZr4W6tDHmAbZ0tibF8MhY/640?wx_fmt=png&from=appmsg)

02

—

简单看看前端页面

众所周知，很多产品/工具，都是能力很强，但是页面不好看，不优美，不舒服，然后导致了这个产品不温不火，最终成为所谓的“宝藏产品”，但是这个页面看着还是整体感觉很舒服，没有那么多花里胡哨的功能，该动的动，不该动的没动，字体也相对比较稳定，整体感觉前端完成度还是蛮不错

![image.png](https://mmbiz.qpic.cn/mmbiz_png/9UFagAZOGDicnYdXeAuLTFVInX3V6Jwt7FTX9YKpvI9vpiceTgmmaUXSJXfBLWoMxrwb6KC3SC2zV2s7awGVt54IqSic9tZLLH3l0PibUjEFMGo/640?wx_fmt=png&from=appmsg)

这里是需要先创建工程，然后再去在工程里面去实施一些具体的工作内容。简单看了下所有的功能，大致应该是这个流程创建工程-->环境搭建-->任务调度-->产出漏洞-->多轮复测-->生成报告这里需要注意的是，黑盒测试必须要有授权书才可以， 所以我这里找了一套开源代码来做白盒审计。

03

—

创建工程

基本也是比较无脑了，因为是白盒，所以直接上传源码就行。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGDibCfEbZibaCNjMOPcQcHCViaglkJKYqFqBTlQ369aXg7rcgCCnQ8rZhoVBGfoSMFzbibO8hM6N8zib6B4xEaQV18PFT27pXH5zKRVs/640?wx_fmt=png&from=appmsg)

需要注意的是，在上传源码的时候，不能上传jar包这种的（防止被黑客利用吧可能是）

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGD9eXx7QjVO1ugVz2ibprFdOwGSaoyxVHAjuHdmPrlB8Ue3AJso7ambVP2KAviaKdEXwZKNSqgb5mTwx7RQRWQZsU7D5ZQYsAFia0k/640?wx_fmt=png&from=appmsg)

创建成功后，在右边即可看到相应的工作空间了

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGDicS8HCyJ7Iplx2VceO9B9mour1V2e468ERWXMfGp6iaibAavImOcgh8AguLIYOJwYmB9vibfO3IVpH7SfQ2W3COpZAhHh1u2RdN6s/640?wx_fmt=png&from=appmsg)

04

—

环境搭建

基本也是比较无脑，但是我觉得超级好评，因为很多时候不是漏洞挖不到，是环境搭建过程中要调试各种各样的问题（尤其是不太懂开发框架的），直接让ai帮你把环境搭好，大概30min左右（至少比我这个新手快多了）就能自动把环境跑出来

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGD8xURu0TJvWZ1KkzmeKGXmtp95eicRWk5icWIh4IvnUeBgVic70ozibPZ9xldLZyGFaiaE2J2icW4eqWibhggke6q23pYIU7H2Ebibklibg/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGDibxy7YfdEQBa8CbLjr0cic2niaIib9Q5P2214UZXjD8P6QLRrgveicBhhqnib6EPtKkrcuLQHEZRglvGl4qMyl8Q9G9MfR51rfuMJHA/640?wx_fmt=png&from=appmsg)

点击详情还是能看到很多信息的，万一搭建不成功也能看看日志到底怎么了（虽然我们没有办法介入进去）

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGDicSgxic3nbCfK08Gy94Vv84NFeDUZBxvSF1MECXicibzico5dZrIDHcwybFAicq3EGaID1xicFibyzY5mTlfMAwlZGy0PYq9ohYF52Nww/640?wx_fmt=png&from=appmsg)

05

—

任务调度

搭好环境就可以开始干了，这里没打开任务调度还以为就只是做做代码审计，没想到这么全，不仅有web应用安全，还有系统安全和移动与客户端安全，这意味着这工具c/s架构的也能直接自动化测试（老实说之前完全不知道c/s架构怎么测，后续有机会可以深入测试下这些功能）

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGD8ic2WNSySjsicAI0iaNtLBfgrn5FiaEqXQQp1KA4Sh0Im4v5DOibiaVOpI6GaAl8VghQ6Kz3lupn7R86vrQspTC3vrbwSA4zm0BTocE/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGDibyGdL2VlQKpWEibYvGswGe8tiaEpEfw5IRb0rBGlicy80NcUSe0M7gRCvrPAicd0oEvQXW0ibJdkD2u5K9gIkedOtxFIZZAibg5aBdY/640?wx_fmt=png&from=appmsg)

简单配置一下，选择全部漏洞（只管量大！管饱！）

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGD9L6CbWFLDvicChEJUGrU5lfsJE4xWpAtCbicfPY4LgYia5cPuGmwE91MqCwYeYH13Ib5wA1PZ3s6YNIShda3SLKJ1Gf7Iuhxliaxs/640?wx_fmt=png&from=appmsg)

最后就是坐等结果了

![image.png](https://mmbiz.qpic.cn/mmbiz_png/9UFagAZOGDibOJB8PmTUNaUu5Lph9XqRPcUhPvGOWt9PD5FBf2ZGHMy3oNlILias1HONgRtBo9IMwia5GBWAWE45ib6iae24RPqN0CZ2Ql9gfibp4/640?wx_fmt=png&from=appmsg)

05

—

漏洞验证

### 默认验证码（严重）

大概三四十分钟之后吧，出现了一个漏洞，说什么验证码可以预测，简单看了下，本地开了个站开始复现（本来就存在弱口令，登陆进去找到管理员手机号，直接开始复现）

![image.png](https://mmbiz.qpic.cn/mmbiz_png/9UFagAZOGD83iaW89RahcmZD50dD5FWqTR7zReI1EXU6oIIdmQpWAUJuy1CibTwJeiayOXEqSf4laCcrNfkibCNF6kicfrJnJ7G8hib5V0YSF2KbM/640?wx_fmt=png&from=appmsg)

大概意思就是只需要知道手机号，即可直接登录进去（这tm不就是默认验证码吗）登进去拿到手机号后，尝试用短信验证码登录，输入管理员手机号，点击发送验证码，然后输入默认验证码，居然登录成功了

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGD9z7k2pHROMFiblh3icgmxRiamvGRnWXR1NQiaGW8BibfUcfMlu5GROibfP9FuwjL6T3Wx0DEHhawGpoMUBNbQicS0ySh9wOCDq05TYCA/640?wx_fmt=png&from=appmsg)

在bp里面可以看到确实登录成功了（md坏了，要失业了），也就是说，这里只需要知道目标的用户的手机号，即可直接登陆进去

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGD9NM1MUZib30qrpUm3eoqmMic0IoGmKibAUxEz2BYymLA9bROegULiaWBgpctc9FsgyLmopcOibxduKdez1leooKU26rbSGyBMHmG9k/640?wx_fmt=png&from=appmsg)

### 任意用户的token伪造（伪造）

浅浅看了下，又找到了一个这个，属于未授权的任意用户身份伪造，相当于我可以直接登陆进去了。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/9UFagAZOGD99ljYyia6VUmfgFaUnROj0U7r8CkS6AAB8hYPg4l4JjbvkMCHduSNE4uurXlLPYAJtmG9tDTyb6sd8ZYvibOppNtkCOEXp8pkmY/640?wx_fmt=png&from=appmsg)

浅浅看了下poc（这里暂时不公开，后面会发代码审计的文章另外写）

![image.png](https://mmbiz.qpic.cn/mmbiz_png/9UFagAZOGD9dEKtd5DDRcw0kEBnE61D4gJjHX9sVicyicdiaLcanBecbUDbua2fD7jcG1xjc9X9G9GJUHz1LcKTRb9PVF61H2SZCnqr1KThRicY/640?wx_fmt=png&from=appmsg)

大概的意思就是，来个userid，直接就可以登陆进去，同样拿出自己搭建的网站开始测试

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGDicXrb9A3t6686FFnOaXCp9yx8NhnJ1mkW7eIu9NamYq2QnVn9r6ov3RfhdwoqyQHqz9qSsctoZf26IbibibAu34FMPibNsFODib9b4/640?wx_fmt=png&from=appmsg)

放入认证头后，成功未授权访问拿到手机号，甚至这个token可以直接使用其他功能（这里先不展示了）

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/9UFagAZOGD9FNDlHx9Qt26QbBicqHh1KTU6ASxicdoKJG5v254vg1LrtSCZ92ybb1icxnML2DhzXnibicHZCNicKEicfibhxSuchHBu0n0dIFokZYB8/640?wx_fmt=png&from=appmsg)

一直到这，我们就发现，可以先通过这个任意用户的token伪造先拿到手机号，然后通过默认验证码直接登入到后台中，其实大家可以发现，整个流程里面，没有任何明显的攻击特征，完全不像sql注入，文件上传，rce那样的明显特征，隐蔽性极高，最关键的是，除了第一个默认验证码我可能会测到以外，另一个这个伪造token，我在平常测试里面几乎不会去尝试。

**而发现这些漏洞，都是基于vulnplus对业务流程的深入理解，不得不再次感叹，太猛了！**

06

—

总结&预告

体验了一把vulnplus，个人感觉是大受震撼，从环境搭建到最后的漏洞发现，基本上是没有太多的人工投入，ai会自动把环境搭建好，然后直接帮你做测试，最后产出漏洞进行复现，甚至最后还支持报告导出，人工需要做的只有漏洞复测与复现了。

缺点也很明显，首先就是官方送的token有点不太够用hhhhh。其次对其他ide工具或者cli工具的适配不算太好，如果在平台用完了所有的token，想把工作流移植到本地codex或trae上，依然是会出现不太自动化的感觉的，且很容易就会把context window（上下文窗口）拉满，然后导致模型失忆，要压缩之后再重新对话。

这里只是理论实现，那么问题来了，这种东西怎么去对真实场景产生影响呢？这篇文章只是上篇，我们还会有一个下篇，展现长期渗透最终获得的成果，拿下某双一流的整个访客平台。或许就是明天或者后天就会发出来。

或许在不远的未来，“古法挖洞”，只会存在于某些特定的应用场景了。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/lSBGaTZnvRG2fw1YwsdhhChHwVurZPiaM5jHsN2S0OhgfFvgmNElYk3wLFufmqzNZgRPqxawSWsKib16A9BvbpsQ/0?wx_fmt=png)

愚者sec

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/lSBGaTZnvRG2fw1YwsdhhChHwVurZPiaM5jHsN2S0OhgfFvgmNElYk3wLFufmqzNZgRPqxawSWsKib16A9BvbpsQ/0?wx_fmt=png)

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