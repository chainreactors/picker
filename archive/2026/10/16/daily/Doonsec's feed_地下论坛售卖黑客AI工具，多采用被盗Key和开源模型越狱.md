---
title: 地下论坛售卖黑客AI工具，多采用被盗Key和开源模型越狱
url: https://mp.weixin.qq.com/s/qSlxNjiro2de-X5AWhgnMQ
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:27:53.369817
---

# 地下论坛售卖黑客AI工具，多采用被盗Key和开源模型越狱

# 地下论坛售卖黑客AI工具，多采用被盗Key和开源模型越狱

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX180ncnv7s5c6OZ3Utfm26yczJ3LuiaOcJb0jEc1QOkczWWx0TCSdPtZlaPwepKicAEbCR6ynmSnRC4pcO7rWsASNO9qmNkEHr5I/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1GKPUheHQ4rAUarU47xib82vWujz0Rr2wG0AQERy3LDMcq2icNic9PStoqW2LljmyXS1Hpsa66qb8tZiav0GzwUeJyT9SvIU2YovE/640?wx_fmt=png&from=appmsg)

某封闭式网络犯罪论坛近期出现一款自主黑客工具，卖家直接使用窃取的OpenAI、Anthropic和Google API密钥为工具提供模型能力。买家只需将盗取的密钥填入工具，就能利用这些密钥驱动自动化扫描，而产生的全部调用费用最终由密钥的真实持有者承担。

Bitsight威胁情报团队在2026年2月至8月期间持续追踪16个地下论坛的数千条帖子，发现与AI智能体、间接提示注入、模型上下文协议（MCP）有关的讨论量增长了67%。

这一变化让两类群体面临直接风险：一类是AI服务商密钥遭泄露的企业，攻击者可以利用这些密钥发动针对第三方系统的攻击，并将费用转嫁给密钥所有者；另一类则是从公开注册表获取AI智能体插件的开发团队，恶意软件可能伪装成正常工具混入其中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1hhG4NiaG4KL1QePQj5gqaVYrDMtXzU8FPsFuuiaOj2HWH1jFVGqYRmmymsAvW6TFwWssbLb2miavzu7Sibbvjmz2PUvUFKLxQo9E/640?wx_fmt=png&from=appmsg)

Part01

黑客工具盗用AI密钥

这款名为MONST3R-AI的工具以“自主渗透测试平台”的名义出售。使用者只需要将窃取的API密钥填入工具面板，设置预算上限，再指定目标列表，就可以启动自动化扫描。

与直接提供模型服务的模式不同，卖家并不托管任何AI模型，而是让买家自行提供API密钥。这种方式不仅可以避开模型服务商原有的安全防护和滥用检测机制，还会把扫描过程中产生的模型调用费用全部记在被盗密钥的账户上。

卖家声称，该工具已经针对199台主机开展扫描，并发现1072个安全问题。不过，这些数据来自卖家自己的控制面板，Bitsight无法独立验证其真实性。

即便其中只有一部分结果属实，这款工具也已经具备一定的自动化攻击能力。随着类似工具不断出现，被盗AI API密钥可能进一步成为黑客驱动自动化扫描和攻击工具的“免费算力”。

Part02

开放权重模型受黑产青睐

“越狱”仍然是地下论坛中最热门的AI安全话题之一，指的是通过特定方式诱导模型绕过自身安全限制、执行原本拒绝完成的请求。在统计周期内，相关讨论量增长了约四分之三。

与此同时，黑客的模型选择也在发生变化。GLM、DeepSeek等开放权重模型的讨论热度明显上升。这类模型可以直接下载并部署到租用的服务器上运行，不需要经过模型服务商的请求审核，也不存在因违规请求被封禁账号的问题。

部分中文和俄文论坛甚至会按照模型“服从恶意请求”的难易程度对不同模型进行排名。一些攻击者还会主动移除模型原有的安全限制，这种操作通常被称为“安全对齐移除”（abliteration）。

由于可以自行部署，这类模型的使用成本也相对较低。一家名为CloseRouter的分销商宣称，开放权重模型和商业模型的调用成本可以低至每百万词元10美分。其公布的GLM价格为每百万输入词元0.053美元，而官方API同等规模的调用价格为1.12美元。

“氛围编程”（vibe coding）的讨论量也增长了一倍以上。不过，在核心技术圈层中，这个词有时带有贬义，用来嘲讽那些高度依赖AI生成代码、却缺乏代码理解能力的开发者。

Part03

AI相关讨论热度上升

勒索软件话题量减半

地下论坛的讨论重点也正在发生变化。统计显示，AI相关话题的讨论量增长了45%，同期勒索软件相关内容下降49%，钓鱼相关内容下降8.5%。

勒索软件讨论热度下降，一部分与执法部门持续打击相关犯罪活动有关，另一部分则是犯罪团伙逐渐转向更加私密的加密通信渠道。随着黑产关注点向AI技术转移，两类话题之间的热度差距进一步扩大。

WormGPT、FraudGPT等曾经受到关注的犯罪聊天机器人，相关讨论量也下降了8.7%，降幅与钓鱼话题接近。今年早些时候，WormGPT遭到攻击，约1.9万名用户的邮箱、支付信息和订阅等级等数据因此泄露。

Part04

AI驱动攻击案例频发

目前，地下论坛中已经出现针对FakeGit攻击活动的技术拆解。该活动由攻击者Water Kurita发起，通过约7600个恶意GitHub仓库传播SmartLoader恶意软件，其中超过800个仓库伪装成AI技能或MCP服务器，包括仿冒的“Docker MCP Gateway”，试图让恶意组件进入公开AI工具注册表。

其他帖子还展示了更具实战性的攻击方式。例如，有攻击者演示如何让AI智能体调用IDA Pro反汇编工具，自动寻找缓冲区溢出漏洞并编写漏洞利用方案；还有攻击者利用浏览器自动化智能体入侵企业Notion账号。

面对这类风险，企业首先需要全面检查暴露在公网环境中的AI服务API密钥，并将AI密钥泄露与云服务凭证泄露放在同等重要的位置进行处置。

对于MCP服务器和AI智能体插件，则需要逐一核验来源和代码安全性，避免将恶意组件引入开发环境。运行在本地的代码智能体也不应默认拥有敏感目录和系统命令的访问权限，执行高风险操作前应经过人工审批。

此外，还可以针对Notion、Slack、GitHub等平台建立正常人工登录行为基线。通过无头浏览器运行的AI智能体，其访问频率、操作间隔和行为模式通常与真人操作存在明显差异，这些异常特征可以作为识别自动化攻击活动的辅助信号。

参考来源：

Stolen AI API keys are paying for hackers' autonomous scans

https://www.theregister.com/2026/10/16/stolen\_ai\_api\_keys/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0YicFBBV16wQdPW4H8cTibDhNEfda7XWQYxJejxMQXMkmUHx6wDDLARUIbdeicO6WQyTRZN8jBRKSbL2bT8srvaRb0FMGv7DXJU8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651348384&idx=1&sn=b0d043fbf6f272983df964e3f249232e&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3mETrvTp1xSWg4nsaY8jdaRdeta9l692aSBiaWUg95sD0gVn7BiaQ6bng5NuFFmERdoTibOtYlCXD4z0Fsus60Vbx1ExXibLicvq4s/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

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