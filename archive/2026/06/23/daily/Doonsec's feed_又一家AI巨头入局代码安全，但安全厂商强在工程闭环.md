---
title: 又一家AI巨头入局代码安全，但安全厂商强在工程闭环
url: https://mp.weixin.qq.com/s/wLFgJn0ybrrtkMcfbkOJZg
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:03:09.999068
---

# 又一家AI巨头入局代码安全，但安全厂商强在工程闭环

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uX9TOlqibIRtZXYDDmQKAhQuibicuwnlQUJbDr2catRdSvyIDicIY3CRfTeym3hfQGIq7XDaP1XW4dia7d3gEfpQ3FRKpYdYicwo6gDTD0g7HmyqI/0?wx_fmt=jpeg)

# 又一家AI巨头入局代码安全，但安全厂商强在工程闭环

长亭安全观察

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![长亭安全观察首图.gif](https://mmbiz.qpic.cn/mmbiz_gif/uX9TOlqibIRu00tmyWzBKCtCLrurOn9iawm5BYhaziabB4dA72Ny9SkFu8UURMvHusR0DfRibtpHJKrBHCeG7JticDlxRZgeFGliahNR6WJTS5KEo/640?from=appmsg)

 6月22日，大模型厂商在网络安全上又有新的动作。

OpenAI发布了Daybreak网络安全计划,主打“**原生防御**（resilient by design）”理念：GPT-5.5 加 Codex Security 组成代理框架，接入企业代码库后，自动构建威胁模型、排查高危路径、验证补丁。

OpenAI该举措被视为对Anthropic Mythos漏洞挖掘能力的直接战略回应，显示出大模型巨头都开始将网络安全作为企业级服务的核心战场。此前Anthropic因安全风险将Mythos限制于“Glasswing”计划，才上线3天就被下架的Fable 5也是因为安全能力太强，无法有效管控被选择全球一刀切暂停访问。

时间推到半年前，当时行业还在争论 AI 漏洞挖掘的安全边界。现在头部大模型公司纷纷把代码安全推到前台。硅谷巨头的叙事逻辑基本差不多，用最强模型做漏洞挖掘和自动修复，做网络安全的底层操作系统。巨头的密集对垒，呈现出一个清晰的趋势：

***AI 正在重塑代码安全的底层逻辑**。*

代码安全不是新需求，SAST、SCA、渗透测试、代码审计，这些能力在安全行业存在了十几年。但当AI Coding 大规模普及以后，代码安全被推到了C位。

AI Coding让代码产出量快速上升，提交频率拉高，业务逻辑复杂度跟着水涨船高。安全问题的发生窗口被压缩，传统扫描的节奏跟不上生成速度。企业采购模型时，开始关注代码写完之后怎么审、怎么验、怎么修复，安全能力正在从附加项变成基础项。

Daybreak 把“原生防御”写进产品定义，对准的就是这个缺口。模型厂商从代码生成开始切入，把安全检测嵌进同一段链路，打破了传统代码安全的市场边界。

代码安全长期以来有一个焦点问题：**能报风险的工具很多，能交出可用结论的工具很少。**

研发团队接到的是一堆疑似风险的报告，得自己判断能不能触发、影响范围多大、修复后有没有回归问题。从发现到确认的过程，消耗的人力经常比修复本身更大。

OpenAI 援引的数据显示，大模型在语法正确率上超过 90%，但安全测试集通过率仅约 55%。这意味着接近一半的 AI 生成代码天然携带高风险漏洞。当 AI 编码工具将代码产出速度提升数倍，人工审计彻底成为瓶颈。

纯靠大模型推理做代码审计，有几个绕不过去的问题。结果不够稳定，误报率不好控制，确认成本下不来。企业部署时还要面对源码不出域、权限管控、多语言兼容、存量系统对接。这些是项目落地的基本线。

长亭科技的回应是**让 AI 同时做“矛”和“盾”**。码力的 AI 研发工程师负责需求拆解和代码编写，AI 安全工程师负责同步审计和修复建议，AI 降噪工程师负责结果治理。三个虚拟工程师角色形成闭环，在效率与安全之间找到动态平衡。MonkeyScan 则更聚焦独立开发者和开源使用者的场景，提供低门槛的代码安全复查，给 AI 生成的代码补一轮安全检查。

![2557C844-7B2F-457B-9F50-D44F99E361CA.png](https://mmbiz.qpic.cn/mmbiz_png/uX9TOlqibIRssTTrshsuc8UyN7gNWHErcdHwClzPibK8uxexcXv92ysWaoM1f12eR5nj5VxlM9gu3xJVH1QPugGQWcq8sOUP6T7jL6vGTk2JE/640?from=appmsg)

AI时代，随着大模型厂商的下场，代码安全的市场预期不断被抬高。AI巨头用旗舰模型打标杆、抢生态位，国内厂商用工程化能力解决落地问题。两者回答的是同一个命题：当 AI 让代码写得越来越快，安全必须从交付前的一道工序变成编码中的一个自然环节。

代码安全工具应该理解业务逻辑，应该给出可验证结论，应该自动校验补丁，应该留下审计证据。这是AI时代研发模式的切换，最终验证的是企业把每一次安全判断做成可验证、可修复、可追溯的工程闭环能力。

\*本文资讯内容编自网络公开报道

![长亭安全观察尾图.png](https://mmbiz.qpic.cn/mmbiz_png/uX9TOlqibIRsS8JgNsicayo7giciaYBwa66W7ugJBrFIeVCjqK4tbVVh9bsceLiccQ2YMODqWiazxe0zqYOexOib2CzqDoufUhibKiaseO4WkllNv6iaU/640?from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NCzpaOPov3N5yAlpsNymmdInF4KibIIE3jw5ia8hFSctjBqgeVBic5zBdVpe6rTWiaL9hEsh0eSibNPVlBWrSnNJpPg/0?wx_fmt=png)

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