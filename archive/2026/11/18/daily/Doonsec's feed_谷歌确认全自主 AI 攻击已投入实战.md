---
title: 谷歌确认全自主 AI 攻击已投入实战
url: https://mp.weixin.qq.com/s/SOpos0HOa-EIqLW24y5O1Q
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:45:48.855769
---

# 谷歌确认全自主 AI 攻击已投入实战

# 谷歌确认全自主 AI 攻击已投入实战

原创

大白
大白

知白守黑1024

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

11 月 16 日，谷歌威胁情报组（GTIG）发布了新一季 AI 威胁追踪报告。两个月前的上一期里，他们的说法还是没有在实战中观察到完全自主的攻击管道。这一期的标题换成了另一句话：智能体威胁活动，跨过了一个重要门槛。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1h51ZRgNlbLZSEp9JnYXI66HNECTXDoI5zeJdzp8SfFSs7YsLGibAIaRk6ju0p0a47XlIdDISHgAicPEYaDEM2tLu6TVZsG4LMyE/640?wx_fmt=jpeg&from=appmsg)

exploit\_agent 的工作循环

转折点是一台暴露在外的中转服务器。GTIG 在上面发现了一套多智能体攻击框架，代号 exploit\_agent。它接入多个前沿大模型和本地托管模型，持续盯着流行 Web 应用的安全补丁：对比打补丁前后的代码差异，推断出被修复的漏洞，起草利用代码，然后自动发起攻击。整个链条里没有一个人类参与。服务器上同时存放着受害者的数据，这台机器不是研究项目，是现役装备。

被它攻击的目标里，有法国的媒体和教育类网站。GTIG 在报告里算了一笔账：补丁的源码材料是有限的，攻击者把大模型对准这些已经公开修复的 n-day 漏洞，比费力挖掘零日漏洞划算得多。这句话对防御方的分量在于，厂商发布补丁的那一刻，同时就是攻击的发令枪。

在 exploit\_agent 之外，GTIG 还点名了四个被真实威胁行为者用于入侵的开源框架：ARTEX、CAIRN、CyberStrikeAI 和 PentAGI。这些项目原本的用途是授权渗透测试，现在被拿来在真实入侵里自动执行侦察、突破和横向移动的各个阶段，目标包括半导体供应商、国防承包商，以及跑着 LiteLLM、Dify 这类组件的 AI 应用基础设施。

![](https://mmbiz.qpic.cn/mmbiz_jpg/j7ZnQr1RD1jcXSVExXdQtrCE0jIhfVMQ3TNSRNViacwrAtO9UIcticoiarsiawIItEtQc7gppiaH7L00OReT2tytz6S5sVN79EUnHNPQnMSRLrCU/640?wx_fmt=jpeg&from=appmsg)

谷歌报告原图：编排智能体协调五个攻击阶段（来源 GTIG）

公网上的规模两个月前就有数字。Unit 42 在 11 月 11 日的报告里统计过，仅可直接访问的 CyberStrikeAI 主机就有 1323 台，ARTEX 有 609 台。当时这些框架还需要攻击者下达一行任务指令。现在，GTIG 观察到的最新案例里，连指令都省了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1iaB16ScvlkKSgH3zuxECbAokAQHVFewKCbscnHFp7zicGwWGREK844tmvUL2JDDh3twiaPG4GYvbqOcmib9lD5JKNh5v6PBMErjUg/640?wx_fmt=jpeg&from=appmsg)

GTIG 点名的四个实战在用开源框架

速度已经有了直观的度量。GTIG 记录了一次云环境入侵：从攻破账户开始，到部署智能体、窃取数千条凭据，全程不到 6 小时。攻击者使用的工具没有任何特殊之处，一个 AI 编程聊天机器人，加一组 Markdown 写成的指令文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1hS1WicmIqPsZKS7iaCYSDOmelCRY5U0M5bdOBNd3pL6ghibR2BNCjXia6tVJnC0hwhME9aaTF5Lj5MbicQ4svsRjU0Adnp9UmSpFnk/640?wx_fmt=jpeg&from=appmsg)

GTIG 观察到的完整入侵案例：从失陷到窃取凭据不足 6 小时

报告还给出了一份时间表。谷歌把威胁者对大模型的使用划成七个阶段：从最早的聊天式提问，到把模型能力嵌进恶意软件，再到把自动化纳入攻击流程，直到当前实战所处的第五阶段——多个攻击环节由大模型驱动的工具完成，只剩极少人工参与。按这份时间表的预测，一到三个月内将出现基本无人在环的多智能体攻击，三到六个月内出现完全自主的智能体攻击。进攻的完全体，已经有了官方排期。

![](https://mmbiz.qpic.cn/mmbiz_jpg/j7ZnQr1RD1jAFoljicAibjZtBDZOibLhM22icS5ibVCyQLWONVooytOn6Eibia9zItVacicYUnKOFlzg4QQibVRxNs10ia8fJ2Qc91t3lCVahJ1B5qUTI/640?wx_fmt=jpeg&from=appmsg)

威胁者利用大模型的七个阶段，第六、七阶段为官方预测

谷歌威胁情报组首席分析师 John Hultquist 的判断很冷静。他说，攻击者并没有使用什么开创性的新方法，他们仍然在利用已知的、未修复的问题，只是速度和规模完全不同了。靠人力追赶机器的速度不现实，防御方必须同样拥抱智能体化，否则就会落后。

谷歌在发布报告的同一天推出了配套的防御产品 AI Threat Defense，把 Gemini 模型、Wiz 的上下文分析、CodeMender 的自动修补和 Mandiant 的专家响应组合在一起，宣称要在攻击者利用漏洞之前完成发现和修复。攻击侧和防御侧的军备，出现在了同一份报告里。

9 月的报告里，AI 攻击还需要人写一行任务目标；11 月的实战遥测里，这行指令也不需要了。留给企业的问题因此变得很具体：补丁装得有多快，凭据管得有多严，暴露面收得有多紧。在机器对机器的攻防里，这三件事是防御方仅剩的、属于人类的时间差。

---

参考来源：

https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gtig-ai-threat-tracker-q4-2026/

https://www.cyberinfos.in/google-gtig-exploit-agent-ai-report/

文中事实与引语均出自上述公开报告及报道，攻击目标与框架使用的归因判断为原报告机构观点，不代表本文立场。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zlD2iah6QpJjciciaI6Ylp5L7rn9Y2O6cTxzf9Suxyw0cwibRgVtpuBzNrqS1ibK3USX8IXHulcNen2rMApDXn352cg/0?wx_fmt=png)

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