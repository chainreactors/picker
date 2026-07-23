---
title: Gemini 3.5 Flash Cyber，可自动化快速完成漏洞挖掘与补丁生成
url: https://mp.weixin.qq.com/s/fvWnDvAx0aKRKlgW_RR9VQ
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:06:46.948406
---

# Gemini 3.5 Flash Cyber，可自动化快速完成漏洞挖掘与补丁生成

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2DEeWIudyD39ALHRQR3gZiamRqiaib8BIFz8GPZLSmfIZcj6Vs9BceibSMSicw2GlAmQGibScQUkHlGFDMGrkCIH7ydsFdmKic1QEUYc/0?wx_fmt=jpeg)

# Gemini 3.5 Flash Cyber，可自动化快速完成漏洞挖掘与补丁生成

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX31HGfvKZdoMvyziaPKo3Y95icdSCxlmmvRnOulGtzAbicAeuTmab14C0gz1BBZFuMfc3vdL6DxMd75CVTic8jVsZnD4QWho6khRIw/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3j2ChiaYtLvQK8JF1X1mnicNx0ujkgQJyASpHGhXbTGvpvleYCnZYXicrSKD6DTlHbguY3uSiaDIqshkkPZoAr0QnOcicPRuic6skk4/640?wx_fmt=png&from=appmsg)

Google正式发布了Gemini 3.5 Flash Cyber，这是一款专门面向网络安全的模型，经过微调后能够比主线Gemini Flash模型更快速、更高效地发现、验证并修复软件漏洞。此次发布标志着Google在自动化安全研究领域的重大扩展，其基础工具包括CodeMender——该公司自主开发的AI驱动代码安全Agent。

随着AI Agent发现漏洞的能力日益增强，防御者面临一个严峻挑战：攻击者找到漏洞的速度可能比安全团队修复漏洞的速度更快。Google的应对方案并非采用更大的模型，而是更智能、更经济的模型。

基于Gemini 3.5 Flash基础模型，3.5 Flash Cyber以牺牲原始规模换取速度和成本效率，使其适用于大规模部署。这一点至关重要，因为漏洞狩猎本质上是一个搜索问题：扫描庞大的代码库意味着要探索海量的执行路径，而依赖单次昂贵的大模型调用会导致瓶颈。

CodeMender通过多次调用3.5 Flash Cyber来解决这个问题，让子Agent并行分析更多代码路径，然后整合成一份高质量漏洞报告。这种设计让该模型非常适合频繁扫描、时间敏感的上线流水线以及大规模提交级扫描。

Part01

Gemini 3.5 Flash Cyber性能表现

Google对该模型进行了广泛测试：

* CyberGym基准测试：每个报告最多使用五次调用，采用3.5 Flash Cyber的CodeMender与体积更大、成本更高的网络安全模型相比取得了具有竞争力的结果。
* Big Sleep评估：在Chrome和Safari等复杂代码库上，3.5 Flash Cyber的表现显著优于主线3.5 Flash和3.6 Flash。
* Chrome生产环境提交扫描：针对未公开漏洞（确保无数据污染）进行测试，该模型相比主线Flash的成功率大幅提升。
* V8 JavaScript引擎测试：3.5 Flash Cyber发现了55个独立确认的问题，而主线3.5 Flash发现了47个，Claude Opus 4.6发现了36个，其中包括两个竞品均未发现的10个问题。

Google指出，较弱的模型往往会反复报告同一发现，而像3.5 Flash Cyber这样更强的模型能覆盖更广的范围，并随着调用次数的增加持续发现新漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0NgkTFuj0Caiao43tYhHn0sUicatkhGnAkzwW4ctZdiclPegJ8NYrYHE8bIWWkZpoRqsCwFOrx4SiaEotqpPmOnIg1Ivw7pZFXpEk/640?wx_fmt=png&from=appmsg)

Part02

Gemini 3.5 Flash Cyber实际应用

除基准测试外，3.5 Flash Cyber已在Google内部代码库中投入使用，包括Chrome、Android、Cloud、Ads和YouTube。一个典型案例是，Google云漏洞研究团队使用该模型仅在两小时内就发现了公共API中的远程代码执行漏洞，以及一项敏感生产服务中的内存损坏漏洞。随后，该模型生成了一个完全可靠的RCE利用程序，能够绕过ASLR和W^X等保护机制。

鉴于其潜在的滥用风险，Google正谨慎部署3.5 Flash Cyber。初始阶段将通过CodeMender以有限访问试点形式向政府和可信合作伙伴提供，后续逐步扩大开放范围。此外，CodeMender的核心功能也通过Gemini Enterprise Agent Platform面向企业客户提供。

Google的优势源于数十年的安全基础设施积累：OSV.dev（收录超过70万个开源漏洞的数据库）以及10年以上的OSS-Fuzz测试结果，这些数据为训练AI模型学习真实安全专家的实际操作方式提供了高质量的素材。

参考来源：

Gemini 3.5 Flash Cyber With Automated Faster Vulnerability Detection and Patch Capabilities

https://cybersecuritynews.com/gemini-3-5-flash-cyber/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3M5qLVTGP6jiaibktDcXOic6E1x1CNbVhdStkk8micFrCq9q4Hp2oH9WnQ229S3ziaeHPACAgicCRKZjic3pV1CTArGRs1KdhccugdUw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651342454&idx=1&sn=30ae51eba566ed3187493e4e817d3124&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX38DqtZUv5FjJ2NibZ3wlLba7jpicoInsIGFnVouGN6kbudJyTf7yhkPM5z8JBrkOVNnialq3PeHX0JzJ9vkBXoUwAdicH70OSf4Wc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3vp7Nh5SN03lJzkelia9oMl3rDgBcDgQuSu66GUobMfu7PibWYZsgcVfAuZ1aAVwMiatGia3JO3kthfNotNqKQC8uiaS9Za2ky2BVI/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1ptPNnRL9ln6TVtKnqhFaD6lZpyAbLwIM5Fj1m89oyZLopZfbJiaJygvkmWZnicUqiaMDPQFh7zAOptwmFmtCGTNSDFbCOaUfcYc/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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