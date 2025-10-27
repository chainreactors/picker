---
title: SecMet#5期  智能代码审计：机遇、挑战与解决方案
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491039&idx=1&sn=1c7aad358d4c0cc2f595b0beafc92b1b&chksm=fe2ee254c9596b42ffcbfeb003fbff602f17f23303f3907cb1c8bd9cdf0fe0a0035459e071c2&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-07-08
fetch_date: 2025-10-06T17:41:16.102401
---

# SecMet#5期  智能代码审计：机遇、挑战与解决方案

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WF0ANHh1UUiaXFiaMSaMY2NapukQicwzNcNbibGzA44holkH2apTHfvG96Mn5aGBJcaiaVGXHICcymQm8A/0?wx_fmt=jpeg)

# SecMet#5期 智能代码审计：机遇、挑战与解决方案

原创

孙宇强（NTU）

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WESYYBu1CibTUxkmBYXS9wLEIj6TxgYzLIic22V3NtLY6uqjkyZF2OjwQsK888zL2ibG0x0P7DmuCibWw/640?wx_fmt=jpeg)

[SecMet]是安全学术圈近期打造的一个线上线下结合的学术研讨模式，研讨会分为全公开和半公开模式，其中`半公开模式仅对安全学术圈内部交流群和特殊专题投稿人员参加`，每期主题根据领域主席（Primary Area Chair，下文简称AC）来拟定或者学术汇报者内容来拟定（`有兴趣组织或者汇报的学者可以发邮件secdr@qq.com，感谢！！！`）。

SecMet#5期主要为`学术汇报`方式进行，详细日程安排如下：

### SecMet期数：#5

* 报告类型：全公开
* **报告嘉宾：孙宇强（NTU）**
* **报告题目：智能代码审计：机遇、挑战与解决方案**
* 报告时间：2024年7月15日(星期一)上午 10:00(北京时间)
* 线上：腾讯会议（600-207-733），加入密码：0715
* 线下：四川大学江安校区网安大楼822房间

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WF0ANHh1UUiaXFiaMSaMY2NapAZoGdib3vPkXBMqMUM6NApEECbvJ8ScGI2GfpJfdiaf1b9XbVcjfy3Rg/640?wx_fmt=jpeg)

### 报告人简介：

孙宇强，新加坡南洋理工大学博士三年级学生，指导老师为刘杨教授。在攻读博士学位之前，他曾于2021年在四川大学网络安全学院取得学士学位，指导老师为黄诚教授。他目前主要研究方向为`自动化代码审计、漏洞检测，以及自动程序修复`。同时，他还对`软件供应链和开源治理`相关的研究有较高的兴趣。他的研究发表在`ASE，ICSE，Usenix Security`等顶级会议上。

个人主页：*https://aboutme.izaiahsun.com/*

### 讲座内容简介：

代码审计一直是维护软件安全的重要措施，通过合适的代码审计，可以提前发现软件中存在的漏洞和缺陷。传统的基于静态分析的代码审计方式有着高效、高召回率和高可解释性等优势。但是也伴随着很高的误报率，难以拓展到新的漏洞类型，缺乏对代码的理解等问题。然后，越来越多的漏洞，难以通过死板的规则来描述，特别是在一些跟业务逻辑紧密相关的代码上，例如智能合约项目。随着大语言模型和代码摘要等相关技术的兴起，程序一定程度上可以理解待检测代码的语义。如何将相关技术应用到自动化代码审计和漏洞检测上，成为了一项有挑战性的题目。

在这次讲座中，主讲人将会分享他们在智能合约漏洞检测方面的五项研究，包括：

1. 第一个结合大语言模型和静态分析进行逻辑漏洞检测的工具，GPTScan。
2. 关于如何使用in-context learning提升大语言模型的漏洞检测能力的实证研究。
3. 使用微调以及多个专家模型，来提升大模型的漏洞检测能力。
4. 使用大语言模型生成形式化验证规则，进而检测代码中的漏洞。
5. 收集实践中安全和不安全的代码模式，来进行漏洞检测。

### 相关文献：

1. GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis
2. LLM4Vuln: A Unified Evaluation Framework for Decoupling and Enhancing LLMs’ Vulnerability Reasoning
3. Combining Fine-Tuning and LLM-based Agents for Intuitive Smart Contract Auditing with Justifications
4. PropertyGPT: LLM-driven Formal Verification of Smart Contracts through Retrieval-Augmented Property Generation
5. Using My Functions Should Follow My Checks: Understanding and Detecting Insecure OpenZeppelin Code in Smart Contracts

## 组办者

特别鸣谢本次SecMet主要组织者：

* 主办AC：黄诚 (四川大学)  https://chenghuang.org/、韩家璇 (四川大学)、赵建国 (四川大学)

## 历史SecMet

* [SecMet#4期 大模型辅助静态分析的智能合约逻辑漏洞检测](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247490557&idx=1&sn=3e65c53edc67c5c4d72913896c2aff27&chksm=fe2ee476c9596d60ce77e943ad0976c6b82e8352108419eb2a8b7ad75fe9d7cc144398834d65&scene=21#wechat_redirect)
* [SecMet#3期 提示学习(Prompt Learning)的隐私泄漏风险分析](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247490363&idx=1&sn=10b877e7bc46c5e54e7549daeec93da1&chksm=fe2ee4b0c9596da61f52adaabbf9401bcab7ebcaa51896c00185db429a78cef06bf6f5a9cff2&scene=21#wechat_redirect)
* [SecMet#2期 基于提示词工程的大模型安全](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247489943&idx=1&sn=6d1d0f4101d7216403ba1151efe0c557&chksm=fe2ee61cc9596f0a4c08e00217a0c01ba3fd8727cd21841da62dae012844a30bc2c877501977&scene=21#wechat_redirect)
* [SecMet#1期 理解和度量大模型的安全问题](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247489705&idx=1&sn=6b021d9849188463d7b2b23c133bbde8&chksm=fe2ee722c9596e342e334a7aee1aa55957fda28ed7845e7540a3d38f47268c250c8cb9213f7c&scene=21#wechat_redirect)

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

阅读原文

修改于

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