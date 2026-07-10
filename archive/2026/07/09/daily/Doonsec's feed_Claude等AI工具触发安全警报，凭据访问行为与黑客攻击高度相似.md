---
title: Claude等AI工具触发安全警报，凭据访问行为与黑客攻击高度相似
url: https://mp.weixin.qq.com/s/qq_lHOL5tmdVeT7IFKQQVw
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:56:26.573429
---

# Claude等AI工具触发安全警报，凭据访问行为与黑客攻击高度相似

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3tylrEXgN9vAPtaa8IJwJBDhcClawmNtyFTg4nKfZSq028wce6GlbjQc9SVqE6MicGvBrDB3jHyzK8y0w655CVzsnC9HIdOatY/0?wx_fmt=jpeg)

# Claude等AI工具触发安全警报，凭据访问行为与黑客攻击高度相似

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX33ico5KIBWlOMicqRnhgrAD4qeu4tCduTJodC8YNic9ib0Wfiaib9FgLKic0ibZq53BPak5d3poTwmQgSEC1Zhe0ndEmn0eySUWjhRM0E/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3x6typ9jEYAB0ME6oE614HZRWUdqucvHEH9ThDJ64eJvYrqcUZLlk4GMwgdMicuFdId88icnIIaR0kHtiaO2rY98kvqwNwBsJn3k/640?wx_fmt=png&from=appmsg)

Claude Code、Cursor 和 OpenAI Codex 等 AI 编程 Agent 正越来越多地出现在企业环境中，最新遥测数据显示，它们会无意间触发与凭据访问和合法二进制文件滥用（LOLBins）相关的安全检测规则。

Part01

AI工具模糊了

自动化与攻击行为的界限

Sophos CIXA 行为引擎的最新分析表明，这些工具模糊了良性自动化与通常与攻击者相关联的活动之间的界限。研究结果基于 2026 年 6 月收集的为期七天的 Windows 终端遥测数据。检测数据显示，映射到 MITRE ATT&CK 框架中凭据访问和执行等战术的规则触发了最多警报。

虽然观察到的所有活动均未被确认为恶意行为，但其中大部分与已知攻击者技术高度相似。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX00JCeYhZdPwMuPpicTU4Yqehryzb26GaqP1bwvXZCun8NnrFD75lszNPZpCOxq1iamYy9cfuWEnTKZwOMTsWibIicmmh9YnOhe2zg/640?wx_fmt=png&from=appmsg)

Part02

凭据访问行为触发大量警报

检测警报中有很大一部分来自凭据访问行为。最常触发的规则之一是 Creds\_3b，该规则会检测使用 Windows 数据保护 API（DPAPI）解密浏览器存储凭据的进程。当 AI Agent 使用 GStack skills 等工具执行浏览器自动化任务时，研究人员多次观察到这种行为。

![凭据访问检测](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3P4Vgic2E0u30WFzS0pa0b3D2ymmP3WKvpl70IRGpWnT8Bda7YIVcHHGvkS9WFIb7gZibKmfYorNgjsTbKQxeISoZicyPwmjTsZo/640?wx_fmt=png)

例如，/browse 功能会启动一系列进程，最终调用 PowerShell 来解码受保护数据。在观察到的某条命令中，PowerShell 使用 .NET 加密函数解码 Base64 输入，并在当前用户上下文下使用 DPAPI 进行解密。

Sophos 研究人员指出，虽然这种活动对浏览器自动化来说是合法的，但它使用了众所周知的窃密技术，导致检测规则即使面对良性目的也会正确标记。

Part03

其他高风险行为模式

其他与凭据相关的警报涉及 AI Agent 生成的 Python 脚本。在某些情况下，Agent 会先用 taskkill 终止浏览器进程，再执行访问存储凭据的脚本。

![高风险行为](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0rMxbvxFmg69vMOdPSS08jsURaavoqTEFawiczetNib9ORHWYn6ZkibWXfpUMF4RyADicS052PKge6IhKMIongsEMbgictFKRP34o0/640?wx_fmt=png)

此外还观察到使用 Windows 内置的 cmdkey 工具枚举保存的凭据等命令。此类行为，特别是与 "--dangerously-skip-permissions" 等标志结合使用时，通常会触发安全运营中心的立即调查。

![安全检测](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3te08zymicLKeGxDW3LfxyBWcxLsddy0HcwibvbtbhEfjP8ROXaY9t7VRUHQK3OHicI7Br5OKjSFxzP0rReZUZibxKE8RHUQ31YhQ/640?wx_fmt=png)

Part04

LOLBin滥用与持久化机制

除凭据访问外，AI Agent 还触发了与命令行混淆和 LOLBin 滥用相关的警报。一个例子是 OpenAI Codex 尝试使用 certutil.exe 从官网下载 Python 安装程序。当被阻止时，Agent 转而使用攻击者常用的另一个原生 Windows 工具 bitsadmin.exe。这种重试逻辑模拟了攻击者的键盘操作行为。

研究人员还观察到持久化机制。在某个案例中，Cursor 使用 PowerShell 脚本将 VBScript 文件写入 Windows 启动文件夹，这一操作被持久化检测规则标记。虽然意图似乎与应用程序设置相关，但在受信任安装程序之外的位置写入启动项仍是高风险行为。

遥测数据还包括"干扰"（Disrupt）类别的检测，代表自适应攻击防护（AAP）事件。当 AI Agent 尝试执行低信誉二进制文件时就会触发这些事件。虽然这些文件未被确认为恶意，但由于缺乏全球声誉而被自动阻止。

Part05

安全团队面临的新挑战

总体而言，数据显示 AI Agent 正在重塑终端上的基线活动。曾经被认为是入侵强指标的行为现在正由合法的自动化工具执行。然而这些行为的风险特征并未改变——解密凭据、使用 LOLBins 下载以及修改持久化位置本质上仍是敏感操作。

这种转变为检测工程团队带来了挑战。安全控制措施必须发展进化，在不削弱防护的情况下区分受信任的 AI 驱动自动化与真实威胁。随着 AI Agent 自主性越来越强，组织需要制定明确的策略来定义这些工具的允许操作范围，并提高对其行为的可见性。

参考来源：

Claude, Cursor, and Codex Trigger Endpoint Security Rules Used to Catch Hackers

https://cybersecuritynews.com/claude-code-cursor-and-codex-trigger/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3y34M5GAibwcktqAsbKu2ibamWeibVrPpa709ynHMljYolGiaw7cPCyW5sCvL9sRS4lJVTOahlPKkMD7YuL5JjW6tibNyibD9QErkrc/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1mP5l1EuNKhxEBfV7Pib0NBoPy1gRRFbZoBrlic0HJgw38b2H2OWOIA5oMMDrrl6KqsiaWgnrKF4a6BoqOKcgRmydooUhNqtQDOE/640?wx_fmt=png)

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