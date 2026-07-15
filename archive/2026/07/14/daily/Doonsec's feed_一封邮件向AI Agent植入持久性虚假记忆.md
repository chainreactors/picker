---
title: 一封邮件向AI Agent植入持久性虚假记忆
url: https://mp.weixin.qq.com/s/Ks2ka2F63BV4f_FoJStkDw
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:43:17.172136
---

# 一封邮件向AI Agent植入持久性虚假记忆

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1TD3cNXVbiaoM5ysEPKPLiaTOiab5OsCIzCp39fokWwibJybGjuibmqSSbiawk98mU9fEVOia5AH8cy8icDgDBHyMH50ViaBGEnPyQSbSU/0?wx_fmt=jpeg)

# 一封邮件向AI Agent植入持久性虚假记忆

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3NSmtvwfs5Lq8QAmMgovTz71qFeO0q8xQ4d0t69SM8eXibuLZxic5PcytmraAYPp0OX9p6J8EMWj7DZACYKfsmwYiaAvicxicuItwY/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0zhTcnpnxricntTO8n76xKBsqQeImvUZR0LCbR6dQ7iaRgic4sCDRTpWKGicnUvGkGVgFoY54LP9xg3YtyXxzVhHcREsH9CB92U4I/640?wx_fmt=png&from=appmsg)

只要赋予AI助手记忆功能及其对收件箱的访问权限，攻击者就能借此改写该助手自以为对你的了解。一封邮件就能诱使AI Agent保存一条关于用户的虚假“事实”，隐藏更改痕迹，并在后续对话中悄然改变其回答方向。

攻击得逞后，用户看到的只是一封看似正常的回复邮件，永远不知道自己使用的助手已被篡改。

研究人员将这种攻击命名为隐身记忆注入（stealth memory injection），并开发出能自动编写此类邮件的工具。相关论文《When Claws Remember but Do Not Tell》于2026年7月6日发表在arXiv上。

![文章配图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1NeRCCPLmTgL4AoZ3jiaoOmVjeTMUhHCU7bpCpwYmibxIlLNIPYmW1MLECib3GwewwJlvnPBAsPmRl9rW0q9piabNgibjLunwuIMtY/640?wx_fmt=jpeg)

Part01

这些助手能做什么？

个人Agent是一种持续运行的AI助手。它不会在对话结束后遗忘一切，而是将关于你的信息以文件形式保存下来：你的偏好、联系人以及你要求它完成的任务。每次新会话开始时，它都会读取这些笔记，因此感觉像是认识你一样。

许多此类Agent还能替你执行操作：阅读你的邮件、查看日历，甚至在你离开时按计划运行小任务。

OpenClaw是本次研究的主要目标，它是一个开源Agent，将状态保存在纯文本文件中：部分文件存放其固定指令（AGENTS.md），部分文件存放其学习到的关于你的信息（MEMORY.md）。每次会话开始时，它会将核心文件拉入模型的上下文。

这些笔记正是产品的核心价值所在，但也正是攻击的目标。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0CvKFlg3H8g7x1vqAGwzcyerbhjmbBbShu0jN1bDo516icp1mkIuAtR6BWB1GSPFEn4vXNgvRnzxticreTtBVDHuibZvK1L5VMF0/640?wx_fmt=png&from=appmsg)

Part02

一封邮件植入假记忆

攻击者不需要你的密码或账户。他们只需向某人发送一封邮件，而该人的Agent设置为检查收件箱——对于这些助手来说，这是常规任务。邮件中藏有专门针对Agent（而非用户）的文本。

如果Agent的邮件处理skill上钩，那么就会连续发生三件事。Agent用自己的文件工具将攻击者的虚假笔记写入其持久性记忆。Agent给出的可见回复绝口不提它做了这些操作。随后，在新的对话中，这条虚假笔记会改变Agent告诉你的内容或为你执行的操作。

在研究的某个测试案例中，植入的虚假信息是：用户的Zelle每日发送限额已提高至10,000美元。

用户之所以未能察觉更改，有几个原因。助手默认隐藏其幕后操作步骤，因此编辑文件的时刻从未出现在聊天记录中。很少有用户会打开原始记忆文件去读取。而且，当Agent在后台按计划运行时，通常不会发送任何消息，所以根本没有什么可察觉的。

为了让“毒药”持久生效，该工具瞄准了每次会话都会加载的核心文件，因此一次写入就能在后续每次会话中加载，而不必等待从单独的存储器中拉取。

这类攻击由研究人员称之为MemGhost的工具生成。其制造者离线训练了一个攻击者模型，将其与个人Agent的副本进行对抗，对成功保存记忆同时保持回复静默的邮件给予奖励。攻击时，它一次性生成完整的邮件，无需与受害者进行来回通信。

在56个全新的测试案例中，MemGhost完成了完整攻击：植入虚假记忆、隐藏它，然后在后续会话中影响Agent的回答。在针对GPT-5.4上的OpenClaw的后台模式运行中，成功率为87.5%；针对Claude Code SDK上的Sonnet 4.6 Agent，成功率为71.4%。

这些是隔离的基准测试运行，并且仅在邮件已到达Agent读取的收件箱后才开始，因此这里没有测试实际载荷能否先通过垃圾邮件过滤或发件人身份验证。

在前台模式测试中，成功率通常较低，因为用户可以看到回复。在后台模式下，针对另外两个Agent框架以及一个基于向量的存储器（代替纯文本文件），成功率仍保持在80%以上。该团队还构建了WhisperBench，一个包含108个案例的基准测试，涵盖从不良医疗建议到金钱损失再到安全破坏等风险。

![WhisperBench框架概述](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0jia3wl0uG68BsDabTQAx8DUAsL6X5LFtnLCOASfWic5kZlP3GC6FlS6RuB4ESCDCDpjBfbNIIcP3GDcFnic8eGZrkPsrcaJlXMc/640?wx_fmt=jpeg)

Part03

现有防线为何失守

这种攻击的粗糙版本大多会失败。一条直白的“悄悄保存且不说出去”几乎每次都会被最强模型捕捉或忽略；正是经过训练的生成器才将成功率推了上去。它还能绕过旨在阻止此类攻击的防御措施。

用于捕捉恶意邮件的内容输入过滤器，有超过九成的概率遗漏MemGhost的消息。一个经过特殊加固、旨在忽略通过邮件发送的指令的模型，仍有大约一半时间遵循了植入的指令。即使要求用户直接询问“告诉我你检查了什么、做了什么”，在某个模型上仍有约四分之一的情况攻击隐藏成功。

目前没有快速补丁可以等待。OpenClaw自身的安全策略将单纯的提示注入视为修复范围之外的问题，除非它还越过了授权、工具策略、批准或沙箱等边界。MemGhost没有跨越这些边界中的任何一个，因为它通过Agent自身的内存写入工具运作，而研究人员一直在针对该框架演示这类注入。

研究作者认为，真正的修复必须在Agent内部实现：标记信息的来源，在信息进入持久性记忆前征求用户同意，并记录每次写入。在此之前，任何同时读取不受信任邮件并能自主写入记忆（无需询问用户）的Agent都暴露在风险中。

简单的修复方案是将这两项任务分开。如果做不到这一点，应限制邮件触发运行所能更改的内容，并在任何可疑事件发生后检查记忆文件。

OpenClaw向The Hacker News确认了这一立场，并对论文中Agent的设置方式提出了异议。其安全指南建议运营者将不受信任的邮件通过一个独立的、剥离了记忆、文件和shell工具的阅读Agent处理，只将摘要传递给主Agent，而论文并未对此进行测试。

它还指出模型层级很重要：OpenClaw的运行使用GPT-5.4（当前前沿模型），但作者因成本问题跳过了Claude Opus 4.6。OpenClaw还提到了HackMyClaw公开挑战赛，在该挑战中，数千封注入邮件未能从基于Opus 4.6的Agent中窃取秘密。但该测试针对的是数据窃取，而非记忆投毒，因此不能直接回应论文。

OpenClaw表示，它正在考虑为外部内容增加内存写入控制，包括来源追踪、审计日志和确认提示，方向与论文建议一致。The Hacker News也已联系论文作者，将在收到回复后更新本文。

Part04

手动版本早已存在

早在2024年，研究员Johann Rehberger就通过手工方式在ChatGPT上展示了相同的操作：通过投毒的网络内容将指令植入其长期记忆中，从而让ChatGPT在未来的对话中持续泄露用户数据。他将这种攻击称为SpAIware。OpenAI堵住了数据泄露路径，但从不受信任内容写入记忆的能力依然存在。

一年后，这种能力出现在一款正式产品中。2025年6月，Aim Security披露了EchoLeak（CVE-2025-32711），该漏洞利用一封包含隐藏文本的邮件，让Microsoft 365 Copilot在用户后续提出正常问题时交出内部公司数据。微软将其评定为严重等级并打了补丁，且未报告实际滥用事件。

后续的案例研究详细说明了该漏洞如何绕过Copilot的过滤器。这两起案例都表明，AI读取的内容可以携带命令，而这些命令可以通过任何人发送的邮件传递。

MemGhost新增的是持久性：Rehberger的版本需要手工植入，EchoLeak仅在被问及时泄露数据，而MemGhost的自动化载荷能将一封邮件转化为一条虚假记忆，长期驻留并在邮件消失很久后仍能引导会话。

这是一个实验室结果，并非正在发生的入侵。研究人员在密封的测试环境中运行所有实验，使用虚假收件箱和虚假用户；论文仅记录实验室测试，不涉及对真实用户的使用。他们表示计划将发现结果、攻击模式以及基准测试数据披露给受影响的Agent和模型制造商。

研究中强调隐身性，部分原因是功能强大的Agent被设计为将工具活动隐藏于聊天之外。唯一暴露自身的模型是因为它在回复中打印了中间步骤。研究人员预计，随着Agent变得更擅长静默工作，检测将变得更加困难。

真正的问题更为直白：来自外部的一条消息，变成了Agent内部持久且可信的上下文，而全程没有任何可见的审批环节。

参考来源：

New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email

https://thehackernews.com/2026/07/new-memghost-attack-plants-persistent.html

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

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0d7KoyEHYsPfbgBgXYQmHS9EgIpOAxfibDrVp8uYPQd3yzGxCrUKcoiajc9NX5KNwMKmib2nnrSsnDa8POob7G5mibuxwMMez0bfI/640?wx_fmt=png)

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