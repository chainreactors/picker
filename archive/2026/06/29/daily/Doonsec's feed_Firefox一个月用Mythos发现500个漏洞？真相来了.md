---
title: Firefox一个月用Mythos发现500个漏洞？真相来了
url: https://mp.weixin.qq.com/s/hBWz_UfaA76F5efiF0MRQA
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:06:17.583954
---

# Firefox一个月用Mythos发现500个漏洞？真相来了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xKicFZ2TIFtibibtNxVjvERic6vM6kB3uQKnDkrcmBlqewjdOHkialemfkYvtZ60v377VicbDOeSl5FPWwOxrQYULe2FYLXCZBibJ3bAh6Zmhv4Pwc/0?wx_fmt=jpeg)

# Firefox一个月用Mythos发现500个漏洞？真相来了

原创

玄月调查小组
玄月调查小组

玄月调查小组

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近期，Firefox的漏洞数量，掀起了轩然大波。

单月修复 423 个漏洞，连潜藏 15 年的历史老漏洞，都挖了出来。

外界最初都将这波漏洞发现能力爆发，归功于 Anthropic 的Mythos。

但 Mozilla 资深工程师Brian Grinstead 在一档播客中点明：模型只占一半功劳。

真正的核心是他们自研的 Agent 框架 ——AI 直接接入工程系统，读代码、跑测试、复现崩溃、验证漏洞全流程自动化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFtibRIBv5ZRWIpFk8TeQKeg2pl54gia5ib03D17vQaavoZhcJnibsSXlbgzaEEtjicFRJr4NJ4XmoYibRiaBHQmvJ4ZNAHKvbAgibMEHLbI/640?wx_fmt=png&from=appmsg)

## 历史漏洞被 AI 激活，安全攻防进入双边 AI 时代

Firefox 作为兼容二十年网页标准的浏览器，代码规模达数千万行。

上万个源文件，大量内存安全问题隐藏在 XSLT 解析、HTML 元素渲染、DOM 节点内存管理等深层路径中。

人工审计受限于精力与成本，很难覆盖所有边缘场景，部分漏洞甚至在代码里潜藏了 15 年，历经多轮排查都未被发现。

![](https://mmbiz.qpic.cn/mmbiz_png/xKicFZ2TIFt8eZSyMpQYibrEQq1yibfbia24OTCaybDO1ocnjtSdTKdbV82VjiaEudss2ltcFHmcjA1WvoXeElicYQBtseWPPauY792WFIvBo47ibo/640?wx_fmt=png&from=appmsg)

此前行业普遍担忧：攻击者会借助 AI 批量挖掘漏洞，大幅放大安全风险。

但 Mozilla 的实践给出了防守端的答案：

只要把 AI Agent 接入成熟的工程体系，就能实现从扫描、验证到修复的全流程自动化，主动批量清除存量风险。

那具体要怎么落地？

直接让 Agent 扫描整个代码库显然不现实 —— 成本高、效率低。

Mozilla 给出的第一步答案，是先给目标做优先级排序。

## 优先级排序：别让AI漫无目的乱扫

Mozilla没有把Agent丢进Firefox整个仓库，然后祈祷奇迹发生。

Brian说，这根本不现实。

Firefox太大了。

上下文不够，成本也不允许。

所以第一步是优先级排序。

他们做了一个大模型裁判。

这个裁判会像安全专家一样看文件。

提示词核心内容是：

> 你是一名安全专家。以下是我们要审查的不同类型文件：C++文件、IPDL 文件、Web IDL 文件。以下是每种文件的详细信息……现在，请给出两个评分。第一个评分是：你认为存在内存安全问题的可能性有多大？第二个评分是：从网页端访问此内容的难易程度如何？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFticY466nKicydibdeZW8uKxxD0r7rq62rGr6G9Kgxy1YI9yhZh5EPnO04JI8ajiaRePVBsX9jCLSQSERLNtLZU0iaFQicMiacsibVhfaHk/640?wx_fmt=png&from=appmsg)

它要给两个分。

第一，这个文件里出现内存安全问题的可能性。

第二，这段代码被恶意网页触达的难易度。

这两个分，直接决定Agent往哪里打。

比如document.cpp，文件巨大，又直接被网页内容访问。

这种目标，就应该优先进入扫描队列。

AI不是无限的，也不是免费的。

你不能没有优先级。

越是大代码仓库，越要先学会给战场排序。

## 狩猎：让Agent死磕目标

第二步是狩猎。

Mozilla把Agent放进一个受限问题里。

给它Firefox代码库副本，给它目标文件，给它工具，再告诉它：我们知道这里有安全漏洞，你必须找到。

它开始推理攻击路径。

从Web IDL找到C++实现。

从网页输入构造状态。

生成HTML测试用例。

用浏览器评估器跑特殊Firefox构建。

借助AddressSanitizer判断有没有内存安全问题。

失败就重试。

![](https://mmbiz.qpic.cn/mmbiz_jpg/xKicFZ2TIFt9QcYEnpPcp1sBQFSWvCLenWePCQMwdBIyvu7rTzmC3F5ibibsa1sybhM4oWa6wVqttPmPTh9plcj56faA3MQTucc4OLSOQxicc3o/640?wx_fmt=jpeg)

legend元素案例里，它试了14次。

前13次失败。

第14次命中。

这就是Agent最不像人的地方。

人类面对第13次失败，可能已经开始怀疑方向。

Agent只会继续尝试。

在安全领域，这种不知疲倦的的努力，就是新的武器。

靠不知疲倦的迭代，Agent 能挖出很多人类找不到的深层漏洞，但目标导向的 Agent 也会出现 “为了赢而作弊” 的问题。

要让结果真正可用，就必须补上验证。

## 验证：AI也会为了赢而作弊

但Mozilla没有天真到相信Agent的每一次结果。

Brian说，Agent会做很奇怪的事。

它可能设置真实用户不会开的测试偏好设置。

也可能修改代码，自己制造漏洞，再利用漏洞来完成目标。

所以第三步必须是验证。

Mozilla加了验证子Agent。

它负责检查主Agent的发现是不是真实漏洞。

检查复现条件是否合理。

检查Agent有没有作弊。

检查输出能不能进入后续流水线。

![](https://mmbiz.qpic.cn/mmbiz_jpg/xKicFZ2TIFticGxsVt8EzQN78kkXthSCgRxE7Zph1Yply9gxlMdH4fQJw1nyXp20bibTHPt5aSh599tkrl5k7Xiaj0yLzrgiap1Qv5g7eIFHxgUE/640?wx_fmt=jpeg)

这一步，是AI安全工具从玩具走向生产的分水岭。

没有验证，Agent会把幻觉包装成成果。

有验证，Agent才可能成为工程系统的一部分。

## 修复：让AI提出补丁，但不把方向盘交出去

验证通过后，修复Agent会生成一个可信代码补丁。

系统应用补丁，重建Firefox，再跑原先触发崩溃的HTML测试用例。

如果崩溃没了，说明这个补丁至少对当前case有效。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xKicFZ2TIFtib0L5JD4hzTSicw5dNTgjKMEHKb1HKUibXmGWlUfW6SgYIibH4xvdsaKM3IzrDX0T6Y9tUHhIrKUUul4VoYmtmTQ7hw7zPZTjicAMY/640?wx_fmt=jpeg)

但Mozilla没有让 AI 自动驾驶。

补丁和报告仍然进入标准漏洞处理流水线，由人类工程师审查。

Brian说，他们距离让Firefox这种规模和复杂度的项目自主开发还很远。

Mozilla仍然要求有人写代码、有人审查代码。

## 工程基建能力决定 AI 落地的真实上限

播客里用了一个说法：开发者体验团队的复仇。

过去，开发者工具、自动化、Fuzz、构建系统、漏洞处理流水线

这些东西常常被视为“基础设施成本”。

现在，它们突然变成Agent的武器库。

模型是可替换的组件，而沉淀完善的工程系统、设计合理的 Agent 工作流，才是真正难以复制的壁垒。

与其纠结模型够不够强，不如先问自己：我们的工程系统，做好被 Agent 调用的准备了吗？

![](https://mmbiz.qpic.cn/mmbiz_jpg/xKicFZ2TIFticNAkocTsPciantwQoTx1enOCLRHInic6xDMJOfO0kn48pwJdoOtZUuGg7g2NNjLvAicicyF73zIIcvPIjbyOpTv2HElfSiayuGOGfU/640?wx_fmt=jpeg)

*参考资料：https://www.chatprd.ai/how-i-ai/how-mozilla-fixed-500-security-bugs-with-mythos https://www.lennysnewsletter.com/p/how-claude-mythos-found-a-15-year*

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnI1oJLbNAr5LvueJmHqk3QP6T1rCyj8yXXaemcJSs1BunLaQO6icn0ZdKPFHRria6ocSZQEwunKTmZQ/0?wx_fmt=png)

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