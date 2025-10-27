---
title: SecMet#7期-苹果系统软件安全漫谈——由防御进化驱动的研究
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491507&idx=1&sn=4ca9f7c8c84cb635c3840c9a9f3ea191&chksm=fe2ee038c959692e85da4ada9efddc392954837ac1bd21beadbd5f08b0ba13a588edc819268e&scene=58&subscene=0#rd
source: 安全学术圈
date: 2025-01-03
fetch_date: 2025-10-06T20:09:46.454108
---

# SecMet#7期-苹果系统软件安全漫谈——由防御进化驱动的研究

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WHC9AQdiaZjyzRaqHCA2OFuPhVGTNNFvlCSRzRD5zbdia0AXAP4DTKxibAoeXag6VsLicN4XFU0gDuGJQ/0?wx_fmt=jpeg)

# SecMet#7期-苹果系统软件安全漫谈——由防御进化驱动的研究

原创

赵建国/曾雨潼

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WESYYBu1CibTUxkmBYXS9wLEIj6TxgYzLIic22V3NtLY6uqjkyZF2OjwQsK888zL2ibG0x0P7DmuCibWw/640?wx_fmt=jpeg)

[SecMet]是安全学术圈近期打造的一个线上线下结合的学术研讨模式，研讨会分为全公开和半公开模式，其中`半公开模式仅对安全学术圈内部交流群和特殊专题投稿人员参加`，每期主题根据领域主席（Primary Area Chair，下文简称AC）来拟定或者学术汇报者内容来拟定（`有兴趣组织或者汇报的学者可以发邮件secdr@qq.com，感谢！！！`）。

SecMet#7期主要为`学术汇报`方式进行，详细日程安排如下：

### SecMet期数：#7

* 报告类型：全公开
* 报告嘉宾：朱家迅
* 报告题目：苹果系统软件安全漫谈——由防御进化驱动的研究
* 报告时间：`2025年1月7日(星期二)上午 10:00(北京时间)`
* 线上：`腾讯会议（215-405-278）`
* 线下：`四川大学江安校区多学科交叉大楼805`

### 报告人简介：

朱家迅，浙江大学博士生，导师为申文博研究员，浙大AAA战队成员，TOAST研究小组成员（*https://www.toast-research.tech*），本科毕业于四川大学。他的主要研究领域包括终端设备的软件与系统等，曾深入研究苹果芯片的硬件防护机制，包括指针认证的实现与应用，以及苹果芯片异构计算单元（如NPU、GPU）的架构设计、使用场景及其分析，发现了多个苹果系统中的实际问题缺陷。他的研究成果发表于ACM CCS、USENIX Security等国际学术会议以及业界会议Black Hat USA，曾获全国大学生信息安全竞赛一等奖、苹果公开致谢等。

个人主页：*https://pricx.github.io/*

### 讲座内容简介：

随着苹果不断加强硬件层面的安全防护，诸如指针认证（Pointer Authentication, PA）等机制的引入极大提升了苹果设备的安全性。本次报告将围绕苹果安全防御的进化历程展开，探讨如何在这一背景下开展安全研究。首先，我们将深入剖析苹果PA的硬件实现和软件应用，包括其在苹果M系列芯片上的定制化设计、密钥管理，以及对抗跨域攻击的策略。通过静态与动态分析，揭示苹果在PA机制方面的独特设计与优势。在充分理解CPU防御机制的基础上，我们将视角转向非AP的异构计算单元（XPU），如GPU和NPU，探索其潜在的安全问题。随着人工智能技术的不断发展，XPU在苹果设备中扮演着日益重要的角色，但其安全防护却相对薄弱。本报告将分析XPU的架构设计与使用场景，针对性地设计新的工具，并结合其与CPU之间的跨XPU共享内存（Cross-XPU memory），尝试探索XPU固件中的缺陷。

### 相关文献：

* CrossFire: Fuzzing macOS Cross-XPU Memory on Apple Silicon. In Proceedings of the 2024 ACM SIGSAC Conference on Computer and Communications Security (ACM CCS 2024).
* Demystifying Pointer Authentication on Apple M1. In 32nd USENIX Security Symposium (USENIX Security 2023).
* Apple PAC, Four Years Later: Reverse Engineering the Customized Pointer Authentication Hardware Implementation on Apple M1. Black Hat USA 2023.

## 组办者

特别鸣谢本次SecMet主要组织者：

* 主办AC：黄诚 (四川大学)  https://chenghuang.org/、赵建国/曾雨潼 (四川大学)

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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