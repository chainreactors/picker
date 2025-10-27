---
title: 雳鉴SAST：AI大语言模型加持 开启软件安全新篇章
url: https://mp.weixin.qq.com/s?__biz=MzIzODQxMjM2NQ==&mid=2247498389&idx=1&sn=03848418de9e5b32437f9da95b07bc10&chksm=e93b0db7de4c84a1dfda1fe859943286f5978abffe5ba56518354b06b2f588b3adf4ce2e49c9&scene=58&subscene=0#rd
source: 默安科技
date: 2024-05-07
fetch_date: 2025-10-06T17:18:24.287685
---

# 雳鉴SAST：AI大语言模型加持 开启软件安全新篇章

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PRUwRKvusicO0wjHEZv62pkw66O9n7TMoIW4ic7neyVV5D4K57DyibCAkxn5AdpGL2xlLt0sCicqGYQvGtBfF9bicpw/0?wx_fmt=jpeg)

# 雳鉴SAST：AI大语言模型加持 开启软件安全新篇章

值得信赖的

默安科技

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/PRUwRKvusicO0wjHEZv62pkw66O9n7TMosnS8TJ6G0P1vX8jsA7SuzqyR6HGyDw60l8b8tFOYAjwWGgOkt4LgCg/640?from=appmsg)

在软件开发的世界中，漏洞始终是悬在应用开发过程中的一把达摩克利斯之剑，SAST（静态应用安全测试）工具作为安全漏洞扫描的重要手段之一，却因为高误报而饱受诟病，不仅分散了开发人员的注意力，同时也降低了安全检测的效率。默安科技积极探索将大语言模型应用于SAST工具中，以更精准的漏洞识别和更高效的修复流程，开启软件开发安全新篇章。

**SAST工具的局限性**

与动态分析或运行时检测技术相比，SAST工具在编码阶段通过静态分析源代码提前识别潜在的安全风险，可以有效降低漏洞的修复成本并缩短漏洞的修复时间，同时由于其能够对源代码进行全面扫描，所以可以识别动态分析工具无法发现的安全问题。

但是，静态分析型工具自身的技术方案原因也导致其存在误报率较高的局限性，在OWASP（开放Web应用程序安全项目）基准测试中，SAST工具虽然检出率达到85%，但同时误报率也高达52%，其主要原因包括：

● SAST工具无法对源代码逻辑进行深入理解，为了防止漏报所以选择告警，最终导致较高的误报率；

● 为降低分析复杂度，SAST工具可能会对分析模型进行简化，造成上下文信息丢失，进而导致对象识别错误，误报增加；

● SAST工具依赖于已知的安全规则来识别漏洞，如果规则覆盖不全或更新不及时可能会导致漏洞误报数量的上升。

**雳鉴SAST + AI大语言模型**

默安科技对AI在安全领域的应用进行深入研究和跟踪，并将技术成果持续深入地应用于多个创新产品中。作为国内开发安全赛道的领导者，默安科技自主研发的雳鉴SAST是一款国内领先的静态应用安全检测产品，能够兼容信创环境、安全可控。随着AI技术的快速发展，默安科技积极探索将大语言模型应用于SAST工具中，以更精准的漏洞识别和更高效的修复流程，开启软件开发安全新篇章。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PRUwRKvusicO0wjHEZv62pkw66O9n7TMotlKPUjVruFRSPuX8wZg1kVLL3YQbyAX1pAj57vfibZMzfo3ChshiaEWA/640?from=appmsg)

图源：AI作图

雳鉴SAST引入AI大语言模型之后，实现了以下两大核心功能：

**功能一**

**误报识别：告别无效警报，专注真实威胁**

默安科技雳鉴SAST的AI大语言模型通过以下关键步骤来识别误报问题，主要包括：

**01**

数据流分析：大模型识别漏洞产生的数据流，提取所有相关函数；

**02**

过滤函数识别：深入剖析函数具体作用，判断是否为过滤函数；

**03**

漏洞利用分析：进一步分析已识别的过滤函数，验证是否能够抵御已知漏洞利用手段；

**04**

误报标记：如果过滤机制健全，大模型会将其标记为误报，避免不必要的困扰。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PRUwRKvusicO0wjHEZv62pkw66O9n7TMoFzzuRiaWgqmauIc4byl3bqChaeCPoU92EOJMHlT0kfYibWjRKAwyzIVg/640?wx_fmt=jpeg&from=appmsg)

图 雳鉴SAST AI大语言模型误报识别功能

**功能二**

**自动化漏洞修复：快速响应，精准修复**

除了可以识别误报问题，雳鉴SAST的AI大语言模型还能够自动化生成漏洞的修复代码，涉及的关键步骤如下：

**01**

上下文分析：模型通过分析漏洞发生的上下文，确定漏洞产生的根源；

**02**

修复策略生成：基于上下文分析结果，生成针对性的修复策略，确保修复措施的准确性和有效性；

**03**

代码生成：根据修复策略自动生成符合当前开发场景的代码修复片段；

**04**

用户交互协作：提供直观的用户交互界面，方便开发者对修复片段进行查看和反馈。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PRUwRKvusicO0wjHEZv62pkw66O9n7TMo16Vgu19OtbLUiaue6q0FmCycABjCB9qWhvfKc8adWUIxxAVe6VwwdFQ/640?wx_fmt=jpeg&from=appmsg)

图 雳鉴SAST AI大语言模型自动化漏洞修复功能

**引入AI大语言模型的收益和价值**

引入AI大语言模型，对企业安全团队能带来哪些收益和价值呢？

一是提升效率：自动识别误报，可大幅削减安全团队处理无效警报的负担，让安全扫描更快捷；

二是降低成本：自动生成漏洞代码修复片段，减少人工修复介入，有效降低安全防护的人力成本；

三是增强安全性：快速定位并修复漏洞，减少漏洞暴露时间，提高软件的安全性。

**结语**

默安科技雳鉴SAST AI大语言模型技术，以其创新的误报识别和自动化漏洞修复功能，为软件开发安全带来了全新的变革。它不仅极大提升了安全分析的效率，减轻了安全团队的负担，还通过自动化修复降低了人力成本，显著提高了软件的安全性。随着AI技术的进一步发展，默安科技将凭借在AI领域的持续研究与应用，以及自身在开发安全领域的优势，为软件开发安全领域的发展带来更多可能性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PRUwRKvusicO0wjHEZv62pkw66O9n7TMomsYsutsT9e5HMiaau0wD4bMDMNtu2u3F46ku5OibsO33OvVc2tNeX2vQ/640?from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PRUwRKvusicM3mp5V1Px2I3MicXWA4DM20ibEWeiaXn0LTl6KftPyLPSfiaJDDqhcwbzN8AlQ7uA7mLGAicxPSfpOflQ/0?wx_fmt=png)

默安科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PRUwRKvusicM3mp5V1Px2I3MicXWA4DM20ibEWeiaXn0LTl6KftPyLPSfiaJDDqhcwbzN8AlQ7uA7mLGAicxPSfpOflQ/0?wx_fmt=png)

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