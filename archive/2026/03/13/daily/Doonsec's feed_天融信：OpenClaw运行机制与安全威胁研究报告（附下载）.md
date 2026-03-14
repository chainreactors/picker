---
title: 天融信：OpenClaw运行机制与安全威胁研究报告（附下载）
url: https://mp.weixin.qq.com/s/bRaay6sS6WG0fDucX6rJ2g
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:05:46.173154
---

# 天融信：OpenClaw运行机制与安全威胁研究报告（附下载）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dSWSuPicfjTdAUxjosxhibbH4tenk5eGyHodFIn7x9hAJiagPCYDnMVuyqV1IAJB6b9tyR5P8ovQyO4okG7FZBMWVPiajupVEwd8PMrOPWEWM34/0?wx_fmt=jpeg)

# 天融信：OpenClaw运行机制与安全威胁研究报告（附下载）

天融信

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/nJmicCz2NYxNibMqIOfXMnZxbVBPBGKu3pficMjqFslyVdhUYhSozJ0egjyKoezIaK9qEyYy6ttzMv3T5Kiasiae7icg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

OpenClaw是2025年末开源、2026年初在GitHub上爆炸式走红的本地优先（Local‑First）AI智能体（Agent）与自动化平台，由开发者Peter Steinberger发起，短短数月即累计二十多万Star，成为GitHub史上增长最快的开源项目之一。它的核心理念是让大模型从“对话式顾问”变成“真正能在本地动手干活的数字员工”，通过深度控制操作系统、调用外部工具和在线服务，自动执行复杂任务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTccep9OxQ90OD607MrJGSRvVZ1IwRLlb3dwZicWct822zjDqT7JURYkojeLRjc2w9tdO8fVe6oicNZ3gNdndpltJHbicNte1iapP4M/640?wx_fmt=png&from=appmsg)

OpenClaw因图标是红色龙虾，被广泛昵称为“龙虾”或“小龙虾”，同时受到产业界和广大用户广泛关注并积极实践应用，引发关于“养龙虾是否安全”的广泛讨论。工业和信息化部网络安全威胁和漏洞信息共享平台（NVDB）已发布专门预警，提示OpenClaw在不安全部署方式下存在较高安全风险，容易引发网络攻击和信息泄露。

在此背景下，天融信正式发布《OpenClaw运行机制与安全威胁研究》报告，从体系结构与运行机理出发，系统梳理OpenClaw的工作流程、Skill机制与大模型交互特点，并对其已披露漏洞和系统性安全威胁进行分析，为后续防护与治理提供技术依据。

![](https://mmbiz.qpic.cn/mmbiz_png/dSWSuPicfjTd2QGYvlHRxWh5r6wmdCahBsw7xibyrWA7gSSjySaRthO3kIJkhYazuVzaYl32EJ12n5lqyS7k2SeicIbYu36OcDNmIFP5wIKibE8/640?wx_fmt=png&from=appmsg)

**关注“天融信”**

**私信回复“OpenClaw研究报告”**

**即可获取完整报告**

**OpenClaw的运行流程**

整体来看，OpenClaw以“本地常驻、模块化扩展、闭环执行”为核心特征，从消息接入、决策规划、工具执行到记忆沉淀形成完整链路。各模块分工明确、协同运转，使其区别于传统对话式AI，成为能够长期运行、自主完成复杂任务的通用Agent基础设施。

![](https://mmbiz.qpic.cn/mmbiz_png/dSWSuPicfjTcoOib4PgfAF4xMdicPAZictDzfKT1hAaZwyNcVjsOhYJDa5wTZyBTOKB3QvnIyvQMLfA7DqibVbUGT1CS3UaJeNyMVY8aYia8Uee6s/640?wx_fmt=png&from=appmsg)

**Skill机制与社区生态：**OpenClaw将Skills视为扩展Agent能力的核心机制，与其说Skill是一个简单的“提示词模板”，不如说它是“带结构化元数据、能驱动工具和脚本的任务模块”。

**默认“完全掌控电脑”的权限模型：**OpenClaw的一大特点是“真正能动手干活”，这在技术上意味着，如果按照常见教程全开工具而不做隔离或限制，就能几乎实现完整系统访问——可以读写文件系统、执行终端命令、控制浏览器、访问邮件和日历、调用SSH或云端API等。

**本地模型与云端模型支持：**OpenClaw的模型编排层支持接入多种云端大模型（如OpenAI GPT系列、Anthropic Claude、Google Gemini等）以及本地部署的开源模型（如通过Ollama或本地推理服务运行的Llama系列），用户可以在配置中选择首选模型和备选模型，并为不同任务设置不同的模型策略。

**OpenClaw面临的主要安全威胁**

依托架构特性与生态现状，OpenClaw面临多层级、多维度的安全风险，覆盖技能供应链、部署配置、框架漏洞、模型交互等关键环节。这些风险相互叠加，构成了当前智能体落地中最典型的安全挑战。

供应链安全：OpenClaw的能力高度依赖外部Skill与远程MCP工具，这使其天然暴露在供应链攻击面上。如果Skill或MCP工具被植入恶意代码或恶意提示词，Agent在毫无察觉的情况下就可能执行攻击者预置的行为。

OpenClaw自身安全配置与运维风险：除供应链问题外，OpenClaw自身的配置习惯和不安全部署方式也是当前攻击的重灾区。从下载不明来源的安装脚本，到将管理端口直接暴露在公网，加上Agent的特权运行、明文凭证存储等等，这些风险为攻击者敞开了大门。此外，由于Agent与大模型交互的黑盒特性，用户难以察觉到数据如何被调用和泄露。

大量已被披露的框架漏洞：在2026年初集中暴露出一组高危漏洞，其中以CVE‑2026‑25253、CVE‑2026‑24763和CVE-2026-25593为代表，叠加不安全默认配置，构成了极具破坏力的攻击链。

OpenClaw与大模型交互相关的安全威胁：由于OpenClaw的“决策大脑”依赖大语言模型，其安全性也不可避免地受到LLM相关攻击面的影响，包括：提示词注入、记忆投毒、模型幻觉与越权执行等。

**OpenClaw安全上岗指南**

OpenClaw既是AI Agent生态繁荣的典型代表，也是当前智能体安全风险的集中样本。其以本地优先、自托管、多渠道集成和Skill插件生态为特征，让普通用户和开发者第一次可以较低门槛地拥有“真正能动手”的个人智能体，这也是其在全球范围内迅速走红的原因之一。然而，正是这种深度系统权限与高度可扩展性，使其在多个维度上都呈现出前所未有的攻击面。

近日，针对“龙虾”典型应用场景下的安全风险，工业和信息化部网络安全威胁和漏洞信息共享平台（NVDB）组织智能体提供商、漏洞收集平台运营单位、网络安全企业等，研究提出[“六要六不要”建议](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650986319&idx=2&sn=b872b32d10d13fe3f62edc8963cbffa6&scene=21#wechat_redirect)。面对全新安全挑战，天融信从平台加固到使用规范，从模型与数据防护到常态化风险体检，提供五层安全能力，层层递进、环环相扣，全面覆盖OpenClaw全场景风险，帮助企业的“小龙虾”安全上岗。

[![](https://mmbiz.qpic.cn/mmbiz_png/dSWSuPicfjTeAqicxN8FkCEBsM0mN7ian7UK8AePG6rqambopZkrynBgUScbs9JqIqfoVFDQqKv3Wh62GkfTcc6pSVXyjGp42Se4OSsLxwKfZA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650986224&idx=1&sn=f7397f2d3bab30a0aa03ba8fcd81180e&scene=21#wechat_redirect)

点击图片查看更多详情

![](https://mmbiz.qpic.cn/mmbiz_png/dSWSuPicfjTdTbukDlPVZiaZ7tibB68BzYmRqZnJMfMicppI4xMxYJIJtAdErh43lvDToIv9plib5AkD3LWGRwgkqQIHHvIHFbVicZ8v2pSrqILec/640?wx_fmt=png&from=appmsg)

在可预见的未来，随着Skill数量和部署规模的继续增长，OpenClaw及类似智能体平台将长期处在“能力跃升与安全焦虑并存”的状态。只有通过规范化的权限管理、严格的技能生态治理、持续的漏洞修复与安全审计，以及对大模型交互风险的系统性防范，才能在充分释放OpenClaw生产力潜能的同时，将由此带来的安全风险控制在可接受范围内。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTeVnypcdSnT2QK9LLRKj4b6wkZqfzicqFYCR5PtHzemibovjHsOSiaAIiaJkWvdxrLm0QRhyPof2hIHI7vdXrMqmlKdStb1S0DhIPQ/640?wx_fmt=png&from=appmsg)

**关注“天融信”**

**私信回复“OpenClaw研究报告”**

**即可获取完整报告**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTdwt2DlajkpRsYsDrYUtoqazyU8GAcP8lyGafSuEEicMHkmUBmgvszIib6YJzI9Djn9ibIHqTlor3wm9kgW8ibXibhz7ce7B3stFlmI/640?wx_fmt=png&from=appmsg)

**相关阅读**

[天融信智算云一键部署OpenClaw🦞安全养龙虾，算力不浪费！](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650986181&idx=1&sn=5edc20f8824d831f28820a752fc97c9d&scene=21#wechat_redirect)

[天融信超融合老用户专属OpenClaw部署方案上线，安全也给安排上！](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650986268&idx=1&sn=d2277e1fdb704dd63dfb5be45f3d5394&scene=21#wechat_redirect)

[天融信：做好五层防护让OpenClaw安全上岗🦞](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650986224&idx=1&sn=f7397f2d3bab30a0aa03ba8fcd81180e&scene=21#wechat_redirect)

[天融信：做好OpenClaw安全管理，让智能的龙虾守规矩~](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650986319&idx=1&sn=75f38314ea4b8adbe25f2d78b923d2c8&scene=21#wechat_redirect)

[OpenClaw漏洞曝光！当AI接管电脑后，是全能助手还是AI刺客？](https://mp.weixin.qq.com/s?__biz=MzkwNDcyNjUyNw==&mid=2247504337&idx=1&sn=4e094a6d9d4caefdbf1d4464d6603614&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nJmicCz2NYxN9YQvlMUUUuxLy2MybDcqLMbtmd2zZKbaroFribHoicEsfL6VZemsk63eVJmas12sUZjDBJyBzuOhA/640?wx_fmt=jpeg&from=appmsg#imgIndex=9)

![](https://mmbiz.qpic.cn/mmbiz_png/nJmicCz2NYxNYPLEV3Hy3SHR9EP0KdgRM2j33GjevlMGgMaxAzSKVh3l3PxFoCQBE6IuZkyql2SwLgSULYKiaOUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=10)

[![](https://mmbiz.qpic.cn/mmbiz_png/dSWSuPicfjTfQCiaLt4wibdoOlRhkvNr2c2PVqY5d5B4dVicNloiaV2Ihu0UzMsEgNA40ZiaWkySQlZG6f7TT37icwGwa6H3eSWZibrmaSXjptQVpzk/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650982021&idx=1&sn=278db1de839bcce8fd566366f786a6bb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTcxQvp3J94yHniaILRSytich4h0u3TLddokUGhicl9vfknTGO5snwyRtQ8bc5OQBYUyGliadNKTduTFVsN4XGopeK4iaLw0AHmr0Eqc/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650986181&idx=1&sn=5edc20f8824d831f28820a752fc97c9d&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTeSSp6TTFv3KTyk5OIEd6OlVwUDiaLsiacMK7zPHcyNiacibEEXOfxwe1Vic53u3zzQPTRUyBwQ1gR0BBicsKsTBFrFyiaPxSUSlt1LBg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650986224&idx=1&sn=f7397f2d3bab30a0aa03ba8fcd81180e&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/nJmicCz2NYxPiazyASKVba57ReFHFEqicHGum3FRLQza0a8624LIibogluysp3HQgcztqd1HUchOdIDwak46dKT1IQ/0?wx_fmt=png)

天融信

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/nJmicCz2NYxPiazyASKVba57ReFHFEqicHGum3FRLQza0a8624LIibogluysp3HQgcztqd1HUchOdIDwak46dKT1IQ/0?wx_fmt=png)

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