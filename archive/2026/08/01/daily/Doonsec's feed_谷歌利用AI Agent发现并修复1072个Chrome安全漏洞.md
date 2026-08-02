---
title: 谷歌利用AI Agent发现并修复1072个Chrome安全漏洞
url: https://mp.weixin.qq.com/s/Lguy_F9oFuRPzlLUKMOrWA
source: Doonsec's feed
date: 2026-08-01
fetch_date: 2026-08-02T05:08:57.437669
---

# 谷歌利用AI Agent发现并修复1072个Chrome安全漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0p3qDU0J3Nia5bDgiaF22D1hFNFCPicIJTvKXYMLrNUeykZdgkdyBeNugrDCUg9VCldqakibBAF2IHzlRnPakLfW5pjEy9ibR7Q7bA/0?wx_fmt=jpeg)

# 谷歌利用AI Agent发现并修复1072个Chrome安全漏洞

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX02pshW7Gwz0dBtef5Xg52AyibgRycLZh32XHC2yZuyyBzsOKTsXnzvQ7cEap4IhXZxAicZvYicdSrVVDm1icQbql3400OHzpPG95Y/640?wx_fmt=gif)

![谷歌利用AI Agent发现并修复Chrome安全漏洞](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1df59vibtibQxE6VFEVq8Dj0CqFzPYpzCIytib2s608sEpJ1Zy4JplUEmnLuoMGYH9946qdyxA9NVuLHpWT7exXGHjsJToAYU3d8/640?wx_fmt=jpeg)

Part01

AI Agent规模化发现漏洞

谷歌正在扩大人工智能（AI）Agent在Chrome安全生命周期中的使用范围，用以识别源代码弱点、测试补丁，并加快向用户推送安全更新的速度。

Chrome安全团队表示，AI系统目前正在帮助发现更广泛Chromium代码库中的漏洞，而不再仅限于协助执行模糊测试（fuzzing）等有限任务。

该公司开发了一个基于Gemini及其他模型的Agent框架，配备了专用工具、内部知识库以及专为安全代码分析设计的防护机制（guardrails）。

一次AI辅助扫描发现了一个潜伏在代码库中长达13年以上的Chrome沙箱逃逸漏洞。该漏洞可能允许已被攻陷的渲染进程绕过沙箱限制，诱骗浏览器读取本地文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX33OdHA4alWyzlruBZrxTsW8fZVPb3bS6mibKr8prprRygHkkvu0s8NYSTxInFFA43pELUElXhSxrpkP8eDO5hDIp572iaeGqDck/640?wx_fmt=jpeg)

谷歌表示，其AI Agent在审查Chrome代码时会使用多种上下文来源，包括浏览器的Git历史、此前披露的CVE、安全文档以及特定组件的SECURITY.md文件。

这些信息有助于AI理解各个Chrome组件的信任边界、预期行为以及威胁模型。

Part02

自动化漏洞分类与修复

此外，该公司还引入了“评审”Agent（critic agent），用于独立审查报告的漏洞和拟议的修复方案。这一多Agent流程旨在降低误报率，并在开发人员评估结果之前提升修复建议的质量。

![近期Chrome稳定版发布里程碑中修复的安全漏洞数量（图片来源：谷歌）](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3Yzw6UZdYofmLlc73ZHicjWdHyibESX7KZsVtBIekpJfMnupPlDxpazeic2Hc15ibh7IPicNSeEjaR1uJuZccOAfKNNzUhm2Q5zpfY/640?wx_fmt=jpeg)

AI还被用于自动化漏洞分类（triage）。传统上，审核一份安全报告可能需要5到30分钟以上的时间。

Chrome的自动化流水线现在可以过滤掉重复和无效的报告，检查PoC，并在受影响的平台上复现漏洞。该系统还会分配严重性评级、添加相关元数据，并将漏洞分派给负责的开发人员或团队。

据谷歌称，这一自动化工作流程每月为开发人员节省数百小时。这些时间可以重新投入到更复杂的安全调查、缓解措施开发，以及对高影响发现的手动验证中。

![Chrome安全自动化流程](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX36xicjYKVF0vk2K9H1pxFhzKJ7Ja5P8GpiaqZ6oyX9YqXz8cTCexnAPHHOKtZEPbHcvxTqk7ADwvOZNz9E7pJiaibNF7znc7SyjQ0/640?wx_fmt=png)

在修复环节，AI修复Agent会生成多个候选补丁。随后，评审Agent会评估这些补丁的正确性、编码规范以及与Chromium约定的兼容性。

测试编写Agent还可以在Chrome支持的操作系统和配置上创建并验证回归测试。

Part03

加速补丁交付与强化内存安全

谷歌表示，来自DeepMind和Project Zero的工具（包括Big Sleep和CodeMender）已集成到Chrome的持续集成环境中。

这些系统持续运行，每24小时运行一次以响应代码变更。该公司报告称，仅在5月份，这些工具就阻止了20多个漏洞进入生产环境，其中包括一个严重级别（critical）问题。

该公司还在着手解决“补丁空窗期”（patch gap），即公开源代码修复与部署到用户之间的一段时间间隔。

谷歌计划转向每周发布两次安全更新，并正在研究动态补丁技术，该技术或将允许在不完全重启浏览器的情况下更新某些Chrome进程。

除了AI驱动的漏洞发现之外，Chrome还持续投入内存安全防护。具体措施包括强化C++防御、采用std::span、加强堆（heap）加固，以及在安全敏感组件中更多地使用Rust。

参考来源：

Google Uses AI Agents to Find and Fix 1,072 Chrome Security Vulnerabilities

https://cybersecuritynews.com/google-ai-fixes-chrome-vulnerabilities/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0nXONQBCVFHia6FsokxUfNXFA2xtbAx9B82cWPTI3sjXjQOqQCSr8zbDKglPCTA8ThPYVetbPgOK37fQL3M6936tsnADQpT4ic0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651343233&idx=1&sn=38d25b1a7d8fda53a5c5a91e20cdd8b1&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2LdBrtrDOMc6A1AZD2zhADpPiaLtxvxbib90tL2ulibWP6yFE2licTo0DB1iabtNGTQQD1NGaA7fuFzW0Pia7LcVQCaPv7HicNAlKh7Q/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

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