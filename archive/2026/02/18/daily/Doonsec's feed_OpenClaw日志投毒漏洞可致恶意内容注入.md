---
title: OpenClaw日志投毒漏洞可致恶意内容注入
url: https://mp.weixin.qq.com/s/gb5E44ld_p4a4d-pboPCrw
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:14:08.223137
---

# OpenClaw日志投毒漏洞可致恶意内容注入

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1yuJNKDsCiazveibGelZCwXNOXZLzLnZPePE1rCXVDKnT0fHrcuTERicuJrLcbAaNXv5kIgvkAZ091sYbeaQfk8Pw9OSWibL3THbs/0?wx_fmt=jpeg)

# OpenClaw日志投毒漏洞可致恶意内容注入

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1NmaBicGXGIVnCpte6wdabQ9Cvy2MBhD98Mk9vp4VSAQomKPL33xqKgdpf5uUYZqqDuIPicDiadhwjUVg24EjkscyLCy5pZ18Pl4/640?wx_fmt=png&from=appmsg)

OpenClaw 作为一款快速崛起的开源 AI 助手，用于连接消息服务、云服务和本地系统工具。OpenClaw 近日修复了一个"日志投毒"漏洞，远程攻击者可利用该漏洞将恶意用户控制的内容注入日志，而这些日志后续可能被 AI Agent 读取。该问题记录在 OpenClaw 安全公告中，影响 2026.2.13 之前的所有版本。

**Part01**

## ****漏洞本质与风险****

该漏洞的核心风险并非传统的远程代码执行，而是一种间接的提示注入式攻击：不受信任的输入被写入日志文件，而 AI Agent 后续可能将这些日志视为可信的故障排除上下文。

根据 Eye Security 发布的公告，受影响版本的 OpenClaw 会记录某些 WebSocket 请求头（包括`Origin`和`User-Agent`），但未进行充分清理。如果攻击者能够访问 OpenClaw 网关接口，就可以发送精心构造的请求头值，这些值会原封不动地嵌入日志行中，形成持久性的"投毒"日志记录。

![漏洞示意图](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0kZZV06Rhgzib80ctk6AiaIBvBJLdSrUZWr6vzslLqiaibkG9icNRtnOZdxzuiaUn88ygxxZLZX7RwnAezIj5BnuesVb5OBzn2ugs2E/640?wx_fmt=jpeg&from=appmsg)

**Part02**

## ****实际影响与攻击面****

实际影响取决于日志在下游的消费方式，特别是在操作人员要求 Agent 诊断错误，而 Agent 将近期日志纳入其推理上下文的工作流程中。在这种情况下，注入的内容可能被误解为操作员指令、可信系统消息或结构化记录，从而可能引导故障排除步骤、影响决策或操纵 Agent 对事件的总结方式。

通过在 Shodan 上搜索 OpenClaw 的默认端口（18789），可以发现互联网上暴露了数千个实例，这表明攻击面正在不断扩大。即使利用该漏洞需要"依赖上下文"，日志投毒仍然具有吸引力，因为它可以低成本地反复实施，且针对的是 AI 层的解释机制，而非单一的内存损坏漏洞。

**Part03**

## ****缓解措施****

OpenClaw 已在 2026.2.13 版本中修复该问题。公告明确指出 2026.2.13 之前的版本均受影响。运行 OpenClaw 的团队应优先升级至 2026.2.13（或更高版本），然后检查网关暴露情况，确保服务在缺乏严格访问控制的情况下无法从公共互联网访问。

防御者还应将 Agent 可读取的日志视为不受信任的输入通道，并应用标准加固措施：

* 在记录前清理或编辑用户控制的头字段
* 限制头字段大小以减少有效载荷空间
* 将"人工调试日志"与"Agent 推理输入"分离，使模型默认情况下不会读取原始的、受攻击者影响的遥测数据

在可能的情况下，应实施对异常头字段模式和 WebSocket 连接失败激增的监控，因为这些可能是投毒尝试的早期指标。

**参考来源：**

Critical “Log Poisoning” Vulnerability in OpenClaw AI Agent Allows Malicious Content Injection

https://cybersecuritynews.com/openclaw-ai-agent-log-poisoning/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2W4PauSPeWFzibFnIaueGohexvlxGHlyQqibmSVMWnic1pgOiclspWRg4QB7OUqibzIeV7g8PQScBQcTOX8rGTGrk6t1tVfKCicKqZ8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibzefibicmDdQl5gbj0kdRbbL9PLvNj4Fx7nTwB10Y86ibaau2wMNuvs9xibztEUaON1ehhL0XgD8G5iaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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