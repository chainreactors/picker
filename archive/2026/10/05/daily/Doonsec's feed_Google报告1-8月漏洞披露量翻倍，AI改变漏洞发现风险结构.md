---
title: Google报告1-8月漏洞披露量翻倍，AI改变漏洞发现风险结构
url: https://mp.weixin.qq.com/s/_x1pvunVsjvnwdD0yNq_Zg
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:20:33.462292
---

# Google报告1-8月漏洞披露量翻倍，AI改变漏洞发现风险结构

# Google报告1-8月漏洞披露量翻倍，AI改变漏洞发现风险结构

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX0eQrPQhqUqE9hyUBS2dQx44ysv3icOdcNaIx0sg0Oaic1KfaHb6gnAcRYmLJSvOBXv3tyk1ibib6wq9xBfwC1IuAbj31uU5XMSysQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3ATMUj1bznWZfjyBuwF2WNKlK5V80FEtlDnbBMHQTVklyiaibeQicvRYhot5iblETwtSiamKicNqpupV5xp12DtSToaB8w52Pr2ck1o/640?wx_fmt=png&from=appmsg)

Part01

1-8月漏洞披露量翻倍

Google威胁情报组（GTIG）今日发布最新报告。今年1月至8月，全球软件漏洞月度披露量持续攀升，8月单月达到10,740个，较1月的5,045个翻了一倍以上。与此同时，AI正在改变漏洞发现格局，在GTIG识别出的AI Agent发现漏洞中，约一半具备远程代码执行风险。

不过，单看原始披露数量容易高估实际威胁水平。开源生态广泛采用自动化标识符分配机制，会显著推高漏洞记录数量。例如，今年描述中包含“Linux Kernel”的漏洞记录约有5,000条，但其中没有任何一个对应的0Day漏洞曾遭到野外利用。

按照GTIG的风险评级标准，同期高风险漏洞披露量增长了167%，8月达到350个，其中包括Oracle季度补丁更新披露的128个漏洞，以及Linux内核网络驱动相关安全公告。

从实际利用情况来看，今年1月至8月已有141个新披露漏洞遭到野外利用，已经超过2025年全年的127个。不过，相对于总披露量，这一比例仍然很低，平均每431个披露漏洞中才有1个被攻击者利用。单一厂商的集中披露周期，或一次规模较大的攻击活动，都可能明显改变某个月的利用数据。

0Day利用数量同样有所上升。今年截至目前，平均每月约发生11起，高于2025年的月均8起。前7个月单月0Day利用量基本维持在8至12起，8月则升至22起。在141个遭野外利用的漏洞中，62%属于尚未发布补丁的0Day漏洞。不过，本轮整体利用数量增长更多来自nDay漏洞，也就是已经公开、通常已有补丁可用的问题。

一种值得关注的趋势是，攻击者可能正在借助大语言模型对比不同产品版本和补丁差异，更快将已知漏洞转化为可实际利用的攻击代码。今年遭野外利用的高风险漏洞已达到75个，远高于2025年全年的28个。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2eVbelSFXzuCibBUoZZnpCo9cTAfrEJQ0SuydqbiajXoJoWuRVYXmibicSPUBqQE9FKWCX24qic7lY5RXiaPDFwemLblECeAM2lpdvk/640?wx_fmt=jpeg)

Part02

AI发现漏洞风险偏高

报告随后将重点转向AI自主发现漏洞的特征。现有公开漏洞数据库很可能低估了这类漏洞的真实数量，一方面是因为漏洞库目前缺乏统一的AI辅助发现标签，另一方面，大型云服务商和SaaS厂商通常会直接在生产环境中修复AI发现的问题，不一定申请公开漏洞标识符。这类标识符更多用于需要用户自行安装补丁的软件。

在GTIG识别出的高概率由AI发现的漏洞中，58%属于中危级别。相比之下，人工和常规扫描器发现的漏洞中，中危漏洞占比只有这一比例的一半左右，同时有69%被归为低危。造成这一差距的一个重要原因，是研究人员往往会主动让Agent聚焦关键基础设施、敏感权限边界等高风险目标。

漏洞类型上的差异更加明显。在其他渠道披露的漏洞中，只有26%存在远程代码执行风险；而AI发现的漏洞中，这一比例达到50%。Agent在挖掘C、C++代码中的深层内存损坏、逻辑绕过等问题时具有一定优势，而这些问题往往容易被传统静态分析工具遗漏。

目前，GTIG将AI发现漏洞遭到实际利用视为一种早期风险信号。CVE-2026-1731就是典型案例。该漏洞影响BeyondTrust的Privileged Remote Access和Remote Support产品，未授权攻击者可借此注入操作系统命令，最初由Hacktron AI研究Agent自主发现。

漏洞在今年2月公开后仅4天，GTIG就监测到一个威胁集群开始尝试利用，一周内又新增5个攻击集群。后续攻击中，攻击者成功提升权限并窃取数据，同时投放SNOWLIGHT、SPARKRAT恶意软件以及加密货币挖矿程序。

Part03

AI软件漏洞激增

编排框架与推理服务成重灾区

报告最后还关注了AI软件自身的安全问题。自2025年初以来，GTIG已经追踪到2,076个AI相关软件漏洞，其中超过1,500个出现在今年。Flowise、Langflow等Agent编排框架贡献了其中约一半的漏洞。

这类可视化工作流构建工具通常包含能够执行代码的节点，攻击者可以通过提示注入或构造恶意工作流文件来访问这些功能。与此同时，vLLM、Ollama、LiteLLM等推理和服务软件共披露212个漏洞。经GTIG核实，其中接近四分之一与未授权API端点或服务端请求伪造有关。

截至目前，针对AI基础设施的0Day利用仍未被监测到，只有少量已经公开的漏洞遭到野外攻击。其中包括LiteLLM的Model Context Protocol服务器预览端点命令注入漏洞，以及Langflow的两个漏洞。今年7月，Sysdig还记录到一起自主勒索软件攻击，攻击者正是利用Langflow此前披露的漏洞完成入侵。

Part04

GTIG预判风险攀升

从中短期趋势来看，漏洞发现和实际利用数量仍可能继续增长，而当前攻击重点依旧集中在边界设备以及直接暴露在公网的企业服务。

在防御策略上，企业需要逐步摆脱缺乏优先级的批量补丁模式，转而结合威胁情报判断修复顺序，并在网络边缘部署更有针对性的防护措施。

软件厂商则可以在代码上线前引入Agentic AI进行安全审查，Google自研的CodeMender就是可选工具之一。如果这类做法逐渐成为行业标准，越来越多漏洞可能会在进入生产环境前被提前发现，公开漏洞披露量的增长速度也有望随之放缓。

参考来源：

Google finds vulnerability disclosures doubled as AI changes which flaws get discovered

https://siliconangle.com/2026/09/30/google-finds-vulnerability-disclosures-doubled-as-ai-changes-which-flaws-get-discovered/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bRSnFgE3WPnpU3s0eVp7QdRn9fI63ymmlhTHpsMBL2VnRMPZQy9DhvZasynJV1ia534sF84uxxKKulzDlBibjrQ7ylDiaickrCIY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651347479&idx=1&sn=1cf9c858a30d0b7af06d196002bd2913&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yychgqrdWpeazfdwAxHj4T9ILWI3fl6IUFOJEIcOHVC5ia3VjkrzuJLbJ4krtMqID23cDDy61ykbbic6NSXcVHRBvrW1jxxOU4/640?wx_fmt=png&from=appmsg)

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