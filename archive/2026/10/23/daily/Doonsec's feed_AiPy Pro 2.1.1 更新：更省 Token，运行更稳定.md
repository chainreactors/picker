---
title: AiPy Pro 2.1.1 更新：更省 Token，运行更稳定
url: https://mp.weixin.qq.com/s/JjrbSVtcFFHfN1znsXrBSw
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:44:51.807021
---

# AiPy Pro 2.1.1 更新：更省 Token，运行更稳定

# AiPy Pro 2.1.1 更新：更省 Token，运行更稳定

知道创宇

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

10 月 22 日，AiPy Pro 2.1.1 完成更新。

这一版有两个重大更新：优化长上下文自动压缩机制，让长文档、多文件任务处理得更省；提升新发布模型的兼容性，让 DeepSeek-V4.1-Flash-1017、Qwen3.8-Flash 等模型运行得更稳。

这两项改动都落在 AiPy 最核心的执行链路上——一个决定你花多少钱，一个决定任务的成功执行率。

先说最实在的：同样的任务，尽可能少花 Token。

![设置 → 关于，版本号已更新为 2.1.1（aipyapp 0.5.0）](https://mmbiz.qpic.cn/sz_mmbiz_png/mVOy0n0uJdiaoYSaKS4TbsicNibhZDmY19ANoFK3uAdg13euzDumJpdmopHiaTYibpJUUj9KVC8Z6TSObibNebBJba04wEEkrZTY1ELvI1icUJjib6s/640?from=appmsg)

设置 → 关于，版本号已更新为 2.1.1（aipyapp 0.5.0）

## 一、长上下文压缩：同样的活，花更少的钱

长文档处理是 AiPy 的高频场景。几份立项书、会议纪要、采购合同一起交给它，让它交叉核对、建立事实清单——这类任务的共同点是上下文极长，且会随工具调用不断累积。

过去的压缩机制在达到阈值后触发，时机相对粗略，容易造成关键信息重复处理，Token 消耗自然上去了。2.1.1 重写了这套机制：压缩时机更精准、关键信息保留更完整、重复计算更少。

落到使用体验上，就是三件事：

**Token 消耗更低：**同样的任务，以更少的 Token 完成

**长任务更省：**减少上下文累积带来的额外开销

**前后文衔接更好：**压缩后仍保留关键结论与任务约束

我们用两组真实任务做了实测。

第一组：6 份项目资料，1 分钟完成交叉核对。把立项建议书、技术方案评审纪要、采购框架协议、季度经营分析报告一次性交给 AiPy，要求跨文件核对并输出事实清单。

![6 份项目资料一次性投入，要求跨文件交叉核对](https://mmbiz.qpic.cn/mmbiz_png/mVOy0n0uJdia698kr3mbLVQ4ejNKS6rwEsWYTGibiajEt54WzPPnaJsE4nbeS526XMiafPeO3ib4mOOq18Yh3wicP6z3GXkhg81mgGj47QPOhJAg8/640?from=appmsg)

6 份项目资料一次性投入，要求跨文件交叉核对

每条事项都附了文件名、章节和原文摘句，另附 16 条变更记录、18 条原文索引，可直接用于答辩或审计追溯。

更关键的是，它不只是汇总，还能识别口径差异。资料里出现了 4,800 万、4,320 万、4,650 万三个预算数字——核对后发现，4,800 万是立项申报额，4,320 万是剔除预备费口径，4,650 万才是投委会最终批复。简单检索很容易把它们当成矛盾，真正有价值的是把版本、时间和口径理清楚。

![事实清单交付：三类信息分开，每条可追溯到原文](https://mmbiz.qpic.cn/mmbiz_png/mVOy0n0uJdiavuEcnw1E6M5ibU5ZJVoeMStGSZLOKXyNuEy40DyEcw9ZlaDV2rAYric1ALrZQLmjTYMO9S2of8HPxGJX0ibKYClicG4LibkicjPs3M/640?from=appmsg)

事实清单交付：三类信息分开，每条可追溯到原文

第二组：4 种格式的数据，1 分 58 秒完成分析。销售订单 CSV、员工绩效 Excel、服务器日志 JSON、库存盘点 TXT 一起投入，要求先做数据体检、再合并统计、最后出报告。

![4 个不同格式的文件同时投入，一句话下发完整分析任务](https://mmbiz.qpic.cn/sz_mmbiz_png/mVOy0n0uJdgiaoPyNEibADI9lYLyxkXFspmPG1XJRaQib71mJjgv1jjkyQttsRAZU9ic1gtTibNqArygHbpDwKDyA5cG67gEsrdyia3sYmIUibj6O8/640?from=appmsg)

4 个不同格式的文件同时投入，一句话下发完整分析任务

300 条记录的「单价 × 数量」与销售额全部一致，日期格式全部合规。从多格式读取、质量检查、合并统计到报告输出，整个流程一次跑完。

![自动产出结构化分析报告，结论均可回溯到原始数据](https://mmbiz.qpic.cn/mmbiz_png/mVOy0n0uJdgY149uzicFq3z0KInJscbrcrFFOYB0S15UsxaOcZplsHLprttOuDqQEVxIMUctibcz1aGK0YhQiblbbgQrlhSibQpoV4iaUic9uUeM4/640?from=appmsg)

自动产出结构化分析报告，结论均可回溯到原始数据

一句话总结：该记住的信息尽量记住，该省下的开销尽可能省下。

省下的钱是看得见的。而省下的时间，取决于模型跑得稳不稳——这正是第二个更新要解决的问题。

## 二、新模型兼容：经多轮测试，稳定性大幅提升

DeepSeek-V4.1-Flash-1017、Qwen3.8-Flash 是近期发布的两款新模型，在 AiPy 执行过程中的任务成功率极高，DeepSeek-V4.1-Flash-1017 的成功率甚至达到了 94%！

工具调用格式、流式输出、上下文窗口处理，各家实现细节都不一样。一个参数解析异常，就可能让整条任务链在最后一步断掉。所以 AiPy 对新模型的适配，一直坚持先测后用。

在 2.1.1 版本中，AiPy 团队针对这两款模型完成了多轮适配测试，结果如下：

| 模型 | 评测任务 | 成功任务 | 成功率 |
| --- | --- | --- | --- |
| DeepSeek-V4.1-Flash-1017 | 63 项 | 59 项 | 93.7% |
| Qwen3.8-Flash | 63 项 | 51 项 | 81.0% |

其中，DeepSeek-V4.1-Flash-1017 在文档与数据处理、代码与工具开发、内容创作与设计三大维度实现 100% 通过；Qwen3.8-Flash 在网络信息检索、创意内容生成、多模态理解三个维度同样 100% 通过。

这 63 项任务全部来自真实办公、开发与生活场景，覆盖文档处理、联网调研、系统操控、代码开发、内容创作与多模态理解六大维度。测的不是“答得对不对”，而是“活儿能不能干完、文件能不能落地”。

经多轮测试，两款模型在兼容性与任务完成的稳定性上均得到大幅提升。落到日常使用，就是三件事：

**工具调用更稳定：**减少复杂任务中的参数解析异常

**任务成功率更高：**长链路任务不容易中途断掉

**执行效率更好：**减少兼容性问题导致的无效重试

![模型列表：deepseek-flash 已标注 v4.1，qwen3.8-flash 标注最新发布](https://mmbiz.qpic.cn/mmbiz_png/mVOy0n0uJdiaRynK6TiaKAhQVhob8XGEPmxjFiaaQmnYOJbTT1nL7BPJ1icIKPAAVK74TIQ5dy4wTPcteDKGEzrXMibnf8vwG2kev5WiapOEkoV30/640?from=appmsg)

模型列表：deepseek-flash 已标注 v4.1，qwen3.8-flash 标注最新发布

在模型列表中，deepseek-flash 已标注 v4.1，qwen3.8-flash 已标注「最新发布」，选中即可使用，无需额外配置。配合 Auto 模式的「动态优化 / 极限性价比」策略，AiPy 会按任务复杂度自动匹配模型——简单的活交给快模型，复杂的活交给强模型。

对用户来说，模型更新不该意味着重新折腾配置。新模型能顺畅接入、已有工作流能稳定运行，才是这次适配希望带来的体验。

## 三、如何升级

打开 AiPy Pro，进入「设置 → 关于」，点击「检查更新」即可，当前版本号 2.1.1（aipyapp 0.5.0）。也可以前往官网 aipyaipy.com 下载最新安装包，支持 Windows、macOS 及国产信创操作系统。

![官网已同步更新至 2.1.1](https://mmbiz.qpic.cn/mmbiz_png/mVOy0n0uJdjoSgE7f3m2NOSrS3J5iaWqaebcfUUsEVejVHia1x1gS3SOSCShC2XyrhGPkL2FfNuRePfKtarMWPU87ribDwyIsahHichWQrIKylI/640?from=appmsg)

官网已同步更新至 2.1.1

## 最后

一个让长上下文任务处理得更省，一个让新模型接入和执行更稳。更新说明只有两行，但这两行背后，是 AiPy 执行链路上最吃成本、也最容易出问题的两个环节。

真正的升级，往往不在界面上多一个按钮。

升级到最新版，找一份长文档、几张表格，或者一个之前觉得麻烦的任务，让 AiPy 试着帮你搞定吧。

还没有下载的朋友，可前往 AiPy 官网（aipyaipy.com）下载安装。

## 关于 AiPy

AiPy（爱派）是北京知道创宇信息技术股份有限公司推出的 AI 桌面智能体，发布于2025年4月，是全球较早推出的 AI 桌面助手之一。产品以「不止聊天，更能代劳」为理念，支持通过自然语言和语音下达任务，面向数据分析、办公自动化、数据采集、PPT 制作、量化研究及软件开发等场景提供智能体能力。

AiPy 支持 Windows、macOS 及国产信创操作系统，并采用免费开源模式，持续探索 AI 技术在个人办公、企业业务及开发者生态中的应用。

了解更多：https://www.aipyaipy.com/

![AiPy 产品展示](https://mmbiz.qpic.cn/mmbiz_jpg/mVOy0n0uJdiah6IpxICr8xG7l3FQWmsh4jqNMeF77L2Pwva1TKXhI8YHqRLOTGYFmF4zS0WS1ZJiax4jC0rmGmziaHWtXiabKNgQPhrKl2jn7g0/640?from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Oan15mBs7fOYe1ETMicrrK5eEreO2UU1sxFQL4Eebn6tthroecicEQrsbZ8qRzV2xMGpvCyU3lWjJwASBPD5QpBg/0?wx_fmt=png)

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