---
title: Anthropic员工失误导致Claude Code源代码泄露
url: https://mp.weixin.qq.com/s/T0S-XVkIlbGHs5_JVzb28w
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:26:45.644783
---

# Anthropic员工失误导致Claude Code源代码泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/E08BHTj0T137grRVKgEDuwJbiaRhUXibvpJ7Ry6eVAfyGHFYXIiaAsFSGicN2MlxP038KfJYWVl3Ml4IZ7ROLBH8iaLRHS2jwxrfjwQDywI7oVcI/0?wx_fmt=jpeg)

# Anthropic员工失误导致Claude Code源代码泄露

华盟信安

![]()

在小说阅读器中沉浸阅读

## 事件概述：npm源映射文件暴露专有代码

![一名困惑不安的用户正盯着电脑屏幕。惊讶紧张的男人看着笔记本电脑。计算机系统错误。](https://mmbiz.qpic.cn/mmbiz_jpg/E08BHTj0T13m6iaQKTz0IbwhuGWAtXZB4Fm2wIjRzeElNKpvmmHgsCl08b1zxJqCBBuKQsdGxCAXMOzh3lia6bG9iaxpDzOicTcHuic05PEia5ZZs/640?wx_fmt=jpeg&from=appmsg)

Anthropic公司一名员工在npm公开注册账户发布的AI编程工具Claude Code版本中意外包含源映射（source map）文件，导致该工具的完整专有源代码暴露。AI专家指出，这种失误存在重大安全风险。

"被泄露的源映射会带来安全隐患，"美国网络安全与AI专家Joseph Steinberg表示，"攻击者可利用源映射重构原始源代码并[了解]其工作原理。代码中的任何机密信息——例如有人编写的API密钥——都将面临风险，所有逻辑实现也同样如此。攻击者可能发现逻辑中的漏洞并加以利用。"

Anthropic发言人向CSO回应称："事件不涉及敏感客户数据或凭证泄露。这是人为错误导致的发布打包问题，并非安全漏洞。我们正在实施措施防止类似事件再次发生。"但据《财富》等媒体报道，类似情况上月已发生过一次。

## 源映射文件的安全隐患

开发者不应在开源注册表发布的最终代码版本中保留.map文件，这些文件可能成为攻击者的情报来源。开发者Kuber Mehta在其博客中指出：当向npm发布JavaScript/TypeScript包时，构建工具链常会生成源映射文件。这些文件是压缩/打包后的生产代码与原始源代码间的桥梁，用于在生产环境出现崩溃时，将堆栈跟踪指向原始文件的实际代码行而非难以理解的引用。

"这些文件包含什么？每个文件、每条注释、每个内部常量、所有系统提示——全部以JSON格式存储，npm会向任何执行npm pack或浏览包内容的人提供这些数据，"Mehta解释道。他补充说："错误几乎总是相同的：开发者忘记在.npmignore中添加\*.map，或未配置打包工具跳过生产构建的源映射生成。以Bun打包工具（Claude Code所用工具）为例，除非明确关闭，否则默认会生成源映射。"

Steinberg将源映射比作显示压缩代码功能的人类可读文件："例如，它能表明可执行代码特定部分正在执行源代码某片段中的指令。"他补充说，源映射有助于调试——没有它，许多错误只能被定位到大段代码范围，而无法精确定位。

本周二凌晨，安全研究员Chaofan Shou在X平台发文"Claude Code源代码通过npm注册表中的map文件泄露！"并附文件链接，事件由此曝光。

## 开发者的常见失误

安全编码培训师Tanya Janca指出，在包中遗留源映射文件是"开发者常犯的典型错误"，"鉴于涉及知识产权的极高价值，加之恶意分子可直接分析源代码寻找漏洞而无需逆向工程，本次事件的严重性远超一般情况。"

Janca建议开发者强化构建环境，避免将调试信息/功能混入生产版本：

* 在构建/打包工具中禁用源映射
* 在.npmignore/package.json文件中显式排除.map文件，即使其被意外生成
* 在CI/CD环境中将.map文件排除在发布产物列表外
* 若存在差异，需严格区分调试构建与生产构建——甚至注释都可能包含敏感信息

## 关键架构层的暴露风险

Arctic Wolf技术和服务总裁Dan Schiappa评论称，任何源代码或系统级逻辑的暴露都意义重大，因其揭示了控制机制的实现方式。"在AI系统中，这一架构层尤为关键。编排逻辑、提示词和工作流实质上定义了系统运行方式。若这些内容暴露，攻击者更易识别弱点或操纵结果。考虑到攻击者仍在探索利用AI的最佳方式，任何可能被攻破的工具背后，都可能潜伏着网络犯罪分子。"

**参考来源：**

> Anthropic employee error exposes Claude Code source

文章来源：freebuf

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kZ8oAGNeUuj6mOI5YlyeqpmfFDmlWrhDUPtdowLH0Fe1bbFYw5foqQqLA333icDSHCp2490tNgrcOArofX5wjWw/0?wx_fmt=png)

华盟信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kZ8oAGNeUuj6mOI5YlyeqpmfFDmlWrhDUPtdowLH0Fe1bbFYw5foqQqLA333icDSHCp2490tNgrcOArofX5wjWw/0?wx_fmt=png)

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