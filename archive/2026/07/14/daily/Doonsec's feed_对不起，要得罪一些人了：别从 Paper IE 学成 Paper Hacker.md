---
title: 对不起，要得罪一些人了：别从 Paper IE 学成 Paper Hacker
url: https://mp.weixin.qq.com/s/BUyh50EcDVk1WOd2j9GIgA
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:44:59.849069
---

# 对不起，要得罪一些人了：别从 Paper IE 学成 Paper Hacker

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BXRyxzSJEtRicbpOAibkEvibwOFkYFIo18yW6ricSYAZbiaq4IyrpambsrQ8jsjIlwmCGI6icQW7hRzWl0kzsib95CUNMRpoO7R7ha6Z7yju0LnGoo/0?wx_fmt=jpeg)

# 对不起，要得罪一些人了：别从 Paper IE 学成 Paper Hacker

原创

Zero老Z
Zero老Z

SecLab安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近看到一个问题：

> 学网络安全一定要达到 NP 的知识水平吗？线下培训班都把 NA、NP 放在前面，能不能直接学渗透？

当然可以直接学。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BXRyxzSJEtRbny5krKNDaicjdwTwM7WJAXWNVSCJkKwPkdJySgkxK0bIwTrYDibDiakcCkTsVHICsncQ2hycANzicAF82jibf5DqoVw7s8gP8gLA/640?wx_fmt=webp&from=appmsg)

网络安全需要网络基础，但不要求每个人先学完 NA、NP。国内一些线下培训机构把厂商认证课程设成统一前置课，更像是课程销售需要，不是安全行业的硬门槛。

先把话说清楚：我不反对 NA、NP，也不轻视数通工程师。真正理解网络、看得懂数据包、遇到故障能独立排查的人，转安全往往很有优势。

我反感的是另一种流水线：

> 先用固定拓扑和标准命令培养一个 Paper IE，再用工具参数和漏洞步骤把他加工成 Paper Hacker。

课程学了不少，思维方式却没变。无非是放下第一套标准答案，又拿起第二套。

## 安全需要网络基础，不需要先考到 NP

学安全当然要懂网络。

你得知道数据包怎么传输，TCP连接怎么建立，路由、NAT和防火墙怎样影响通信。遇到问题时，也要会看抓包和日志。

但“需要网络基础”不等于“必须完整学完 NA、NP”。

NA、NP是面向数通领域的厂商认证体系，主要讲路由交换、设备配置、网络建设和故障排查。这些知识很有用，但不是所有安全岗位的统一入口。

SOC分析、主机安全、Web安全、漏洞管理和应急响应都要用到网络知识，可初学者通常不需要先掌握复杂的园区网设计、大量动态路由协议和成套厂商命令。

你要学的是网络如何工作，不是先拿某个证书给自己发入场券。

## 数通和安全看网络的角度不同

![不同角度看到不同图片-千图网](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BXRyxzSJEtTUU3hCDehnO1BBm3wiaAqJXfiaFvEgwoG5wCQ0HLJTIB03fQTXYtxN2ruPPCeak70QnwMaFLNMEUz63XFhpLiaV3DPG8B5zxeo38/640?wx_fmt=webp&from=appmsg)

数通工程师通常关心设备怎么连接、路由怎么配置、链路是否稳定，以及网络出了故障如何恢复。

他们解决的问题大致是：

> 怎样让数据正确、稳定地到达目的地？

安全人员还要多问几句：这是什么资产，承载什么业务，谁在访问谁，数据流向哪里，中间经过哪些安全边界，出了问题会有什么影响。

安全不只判断“通不通”，还要判断“该不该通”。

两台主机无法通信，数通工程师可能先检查接口、VLAN、路由、ACL和NAT。安全人员最好先问：

> 它们为什么需要通信？

如果没人能解释业务关系，“不通”可能才是正确结果。

所以，从数通转向安全，难点不在于多会配几台防火墙，而在于换一个观察角度。以前主要看设备和拓扑，现在还要看业务、身份、数据流和风险。

## 从 Paper IE 到 Paper Hacker

![](https://mmbiz.qpic.cn/mmbiz_jpg/BXRyxzSJEtQvB3MOJMMJh4nB3D1uqAUSGEVz6nzP0LT4zWE0GfESdeRAW1aibee1bCBcTq8peUMweImAsoK2ic2S5kqcpCUEvATZ13mibuYwzk/640?wx_fmt=webp&from=appmsg)

国内安全行业里，不少人来自数通、系统集成和网络运维。这本身没问题。

问题是，很多数通培训早已变成了考试训练。学员不太关心数据包为什么这样转发、网络为什么这样设计、故障又为什么发生，主要练的是另一套东西：

* 看到这种拓扑，就输入这组命令；
* 遇到这种题型，就套用固定配置；
* 反复练习考试里的标准实验；
* 记住答案，不必建立网络模型。

这就是 Paper IE。

证书有了，命令也会了。可一旦换个厂商、换种拓扑或者换一个故障现象，熟悉的剧本没了，人也跟着没思路了。

更麻烦的是，这种训练方法后来又被搬进安全培训。

以前是：

> 看到拓扑，套配置。

后来变成：

> 看到漏洞，套 Payload；看到告警，查 IP；看到策略申请，照单放行；看到扫描报告，导出表格。

学的东西变了，学习方式原封不动。一个 Paper IE 就这样转身成了 Paper Hacker。

这里说的 Paper Hacker 不只指渗透测试人员。它指的是一种空心化的能力：会操作设备，会运行工具，也会执行流程，但解释不了现象，看不懂业务，更不会独立判断风险。

做渗透只会复制 Payload，是 Paper Hacker。

做 SOC 只会查询威胁情报，然后机械关闭告警，也是。

做安全运维只会按照申请单开放策略，仍然是。

它不是一个岗位，而是一种学习留下的后遗症。

## 为什么培训机构喜欢这样教

因为这种教学容易展示成果。

![网络安全、数据监测、数据预警的可视化大屏_网络安全可视化大屏-CSDN博客](https://mmbiz.qpic.cn/mmbiz_jpg/BXRyxzSJEtQVKtqHpyiaDNRtic7MCSEFpNbCNWwpj9heVcOPErgW4NkKmTtt29iciccLGSS8ubF0Uwxe0p0UjibcicWdib6U4zddgwicOe4UticGY8QE/640?wx_fmt=jpeg&from=appmsg)

扫描器跑出一排端口，能截图；Payload执行成功，能截图；拿到Shell，当然也能截图。防火墙策略配好了，页面上有结果；告警工单关掉了，后台数字又少一个。

老师敲几条命令，屏幕马上有反应，学员很容易产生一种感觉：

> 我会网络安全了。

这种教学确实见效快。

给出固定拓扑，再告诉学生输入哪些命令，网络很快就通了。换成固定靶场，照着步骤运行工具、复制Payload，漏洞也很快复现。处理告警同样如此：查几个字段，填一段结论，工单关闭。

学生觉得自己学会了，老师也有成果可展示。

问题在于，这种速度来自对真实环境的删减。业务背景没了，资产差异没了，软件版本和数据流向也没人管。学员既不用选择分析方向，也不用判断结果是否可信。

他练习的不是解决问题，而是执行一份提前写好的答案。

## 它会影响一个人以后怎么工作

刚入行时养成的学习习惯，很容易延续到工作里。

如果一个人接受的训练一直是“看到问题就找模板，看到漏洞就找Payload，看到产品就翻操作手册”，那么进了行业以后，他多半还会沿着这条路走。

工作一年，多记一些命令；工作三年，多攒一些案例；工作五年，硬盘里多出一堆模板。

表面上经验越来越丰富，实际增长的只是标准答案数量。

他的处理方式始终是：

> 遇到一种场景，记住一种做法。

而不是：

> 建立一个模型，用它解释一类问题。

前一种方式刚开始进步很快，因为每学一个套路，就能解决一道熟悉的题。可环境一旦变化，原来的答案就未必管用了。工作时间越长，这种学习方式暴露的问题越明显。

## AI来了，还要跟它比赛背命令吗

以前，一个人记得更多命令、熟悉更多参数、看过更多案例，确实能形成职业优势。

别人需要查资料，他可以直接写出来。

现在，这部分优势正在快速缩水。

AI可以生成设备配置、解释命令、编写脚本、查询日志、整理漏洞信息，也能根据报错给出排障方向。AI Agent再往前走一步，还能读取告警、查询威胁情报、关联资产、生成查询语句、检查配置并输出处置报告。

如果一个人的主要能力只是背命令、记参数、套流程和找模板，那么他的竞争对手早就不只是其他工程师了。

和AI比记忆，没有多少胜算。

你见过几十个案例，AI可以在几秒内检索更多资料；你按照固定步骤处理问题，它可能做得更快，也不容易漏项。

Paper式培训最危险的地方就在这里：它仍在大量训练记忆、检索、模式匹配和标准流程执行，而这些事情恰好是AI的长项。

## 安全基础不是一张课程表

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BXRyxzSJEtR1hPlaiaZfAwYY4TEOTZl0FBBZXVm7D6CeycLkkDqX0CCgL4YZRu9PwwUjAvR9Etdibtacltfa2T1vMUSGouriaRHJr6WMibdPSrY/640?wx_fmt=webp&from=appmsg)

我习惯用“三驾马车”概括安全的技术基础：

> 系统是骨，网络是筋，编程是血液。

这个比喻不可能覆盖整个安全行业，但对初学者够用了。网络安全不是一套凭空出现的工具，它建立在计算机基础之上。

系统决定程序怎样运行、权限如何生效、日志如何产生；网络决定主机和服务怎样连接、数据如何流动；编程则帮助你理解软件怎样处理输入、漏洞为什么会出现，以及自动化如何实现。

技术之外，还要理解业务和数据。业务解释系统为什么存在，数据决定安全到底要保护什么。最后再根据证据判断风险，决定该做什么。

所以，学习安全不能只是先背一套网络配置，再背一套工具参数。面对真实场景时，应该习惯追问：

* 这个现象为什么会发生？
* 数据到底流向了哪里？
* 工具为什么会得出这个结论？
* 这项操作控制了什么风险？
* 环境发生变化后，原来的判断还成立吗？

命令要学，工具也得会用，流程同样不能不知道。但它们只能帮你入门，不能替你思考。

## 写在最后

标准化课程对零基础的人确实有帮助。它能降低入门难度，也可能让人更快找到第一份工作。

可如果一套培训只教人执行答案，不教他理解系统、业务、数据和风险，那么所谓的快速入门，很可能也会成为日后的天花板。

第一份工作也许能靠套路拿到，后面的职业生涯却很难一直靠套路维持。

安全行业真正缺的不是记住最多答案的人，而是遇到没有标准答案的问题时，仍然能看懂系统、检查证据并作出判断的人。

![DeepSeek vs ChatGPT vs Kimi vs Qwen Chat vs Gemini vs Grok ...](https://mmbiz.qpic.cn/mmbiz_png/BXRyxzSJEtTQe0Nkz8XaD1aS3SGG990zrFTKWMVvVKRoQmePe1N4AgO4icwdzFqwJ6Rp0mw9MGc0PribdN7KtAr3PNTFfmYPTy1SjP1OZ8D8E/640?wx_fmt=png&from=appmsg)

否则，培训机构今天把你从 Paper IE 教成 Paper Hacker，明天AI就会坐到你旁边，客客气气地提醒一句：

> 这些 Paper，我做得比你快。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Bvow4Cv9oZ3Niaq1oRhfNZdtUP37c59CqD0UQXxWYSo0Cl4TrNgFhApzDstFhlPtGI6BlPvU4Ttico80OWHDRJ2g/0?wx_fmt=png)

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