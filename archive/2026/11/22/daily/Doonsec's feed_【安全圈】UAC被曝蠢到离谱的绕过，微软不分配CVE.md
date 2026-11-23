---
title: 【安全圈】UAC被曝蠢到离谱的绕过，微软不分配CVE
url: https://mp.weixin.qq.com/s/3eujcMNciVldpJVqugRjCQ
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:02:23.454995
---

# 【安全圈】UAC被曝蠢到离谱的绕过，微软不分配CVE

# 【安全圈】UAC被曝蠢到离谱的绕过，微软不分配CVE

安全圈
安全圈

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

UAC·提权

谷歌安全研究员詹姆斯·福肖（James Forshaw）在社交媒体上公开吐槽微软，称自己发现了一个"蠢得离谱"的 UAC（用户账户控制）绕过方式，并讽刺被利用的组件**像是 AI 编码的产物**。

截至目前，福肖**并未公布**具体受影响的组件、漏洞利用方式和受影响的版本。这一点很关键——在细节公开前，任何"你的机器已经可以被绕过"的说法都属于过度推断。

但这件事值得写，不是因为漏洞本身有多严重，而是因为它同时暴露了两个问题：**微软对 UAC 的定位**，以及**AI 生成代码进入系统组件后的审计盲区**。

## 先厘清：UAC 到底防什么

UAC 是 Windows 控制管理员权限的传统机制。管理员账户登录系统后，日常应用通常先以**受限令牌**运行；当需要安装软件、修改系统文件或更改重要设置时，系统弹出确认窗口，用户确认后才授予完整权限。

UAC 绕过意味着：**一个已经在本地管理员账户下运行的恶意程序，可以跳过弹窗确认环节，直接拿到完整管理员令牌。**

拿到完整令牌后能做什么？修改系统文件和注册表、关闭安全功能、安装需要更高权限运行的恶意组件。这些都不需要用户点"是"。

所以"UAC 被绕过"的实际含义，必须叠加一个前提：**攻击者已经能以本地管理员身份执行代码**。这不是远程边界突破，而是提权链上的一环。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGjsnpdMxZ0rUZ3bYY7Pib07nFiccEqGvsmpnYHAC8HVMyocUBSyYRziau5dibDcF8ICcsib9k5rQhHicBeSlfDwDSUiaXUs3R8v8od1Q/640?from=appmsg)

## 微软的立场：不是安全边界，就不算漏洞

微软将 UAC 定义为**纵深防御功能**，而不是必须隔离不同权限的安全边界。按微软的安全服务标准，**单独绕过 UAC 默认不满足安全更新或漏洞奖金的处理条件**。

这也解释了福肖在原始帖子里的态度——他直接说微软**不需要**考虑 UAC 绕过。这不是替微软辩护，而是在描述现实：按现行口径，这类问题不会被分配 CVE，也不会触发紧急安全公告。

微软仍可能在后续版本中修改被滥用的组件，但通常不会公开致谢或给出编号。**对于防守方，这意味着一个尴尬的处境：一个真实存在的提权捷径，在漏洞管理体系里"不存在"。**

## Administrator Protection 已经接棒

微软目前已经用 **Administrator Protection** 替代传统的 UAC 管理员批准模式。该模式可以抵御部分低级绕过方法——核心变化是：管理员权限不再通过"弹窗 + 令牌提升"授予，而是走独立的、受保护的授权通道。

福肖在 Administrator Protection 预览阶段就发现了 **9 种绕过方法**，这些问题**都已在正式版中修复**。这个数字本身就说明：新的授权模型在设计阶段被系统性攻击过，而不是上线后再补。

既然问题已修复，业界普遍预计福肖后续会发布博客，详细介绍漏洞成因并给出概念验证程序。届时才是真正的检验窗口。

## 两个更值得讨论的问题

### 问题一："AI 编码的产物"意味着什么

福肖的讽刺指向一个现实趋势：随着 AI 编码助手大规模进入工程流程，系统组件里出现了越来越多**"能跑但没人真正理解"的代码**。

这类代码的问题不在于一定会写出漏洞，而在于：

* **审计成本上升**

  ：评审者面对的是"看起来合理"的实现，难以判断边界条件是否被处理
* **责任链模糊**

  ：出问题时，是模型生成错误、还是开发者审阅失职，缺乏追溯机制
* **风格不一致**

  ：同一组件里混入多种编码习惯，异常路径更容易被忽略

这也是为什么"AI 生成的代码必须过同等甚至更严的安全评审"应当成为硬性要求，而不是可选项。

### 问题二：不分配 CVE ≠ 没有风险

对企业来说，漏洞管理的输入通常是 CVE 列表、厂商公告、扫描器结果。而 UAC 绕过这类问题**三条渠道全都不覆盖**：

* 没有 CVE
* 没有安全公告
* 扫描器不会报（因为这不是"缺失补丁"，而是"机制设计如此"）

结果就是：**一个真实可用的提权路径，长期存在于资产基线之外。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyE44I8cVhQgksXs96rBILyEr7pNjVKBATYbPjRYMmNaOSvsOnjjSfIfKSJ9WElfqzeVMuKbPdEykZnhxj2BxCO8NibD60lC1k0U/640?from=appmsg)

## 运维可落地的六条

不要指望"等微软发补丁"。这个问题的正确处置方式是**改变基线假设**：

1. **不要把"UAC 已开启"写进控制项。**

   它从来不是隔离边界。控制项应改为"日常账号是否为标准用户"。
2. **强制管理员与标准用户分离。**

   日常办公用标准账号，管理操作走独立的跳板或专用管理账号。这一条能抵消绝大多数 UAC 绕过——因为绕过需要"已在管理员组内执行代码"。
3. **尽快启用 Administrator Protection。**

   新模型的授权通道独立于传统弹窗，能抵御一批低级绕过。
4. **EDR 规则盯两件事：**

   令牌提升的异常来源、UAC 弹窗被抑制或自动确认的行为。后者在合法软件里几乎不会出现。
5. **把"无 CVE 的加固缺口"纳入基线库。**

   建议单列一类资产项：机制性弱点（UAC 绕过、自动播放、宏执行、LLMNR/NBT-NS 解析等）。它们的共同点是永远不会出现在补丁列表里，但每年都在被利用。
6. **对内做一次"AI 生成代码"的盘点。**

   不是禁用，而是标记：哪些模块由 AI 辅助生成、由谁评审、是否有对应的测试用例与边界用例。这是新版 SBOM 该有的字段。

## 结论

这起"蠢到离谱"的绕过，威胁等级不高，但它精准命中了三处工程软肋：**依赖纵深防御当安全边界、依赖 CVE 当风险全集、依赖人工评审兜住 AI 产出。**

前者是认知问题，后者是流程问题。认知可以靠一次复盘改，流程得靠制度。福肖的细节还没放出来，但该做的自查现在就可以开始。

***END***

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过