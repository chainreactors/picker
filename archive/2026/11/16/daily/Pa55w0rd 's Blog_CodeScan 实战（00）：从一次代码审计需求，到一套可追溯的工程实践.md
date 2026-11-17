---
title: CodeScan 实战（00）：从一次代码审计需求，到一套可追溯的工程实践
url: https://www.pa55w0rd.online/codescan-00/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:35.772487
---

# CodeScan 实战（00）：从一次代码审计需求，到一套可追溯的工程实践

# [Pa55w0rd 's Blog](/)

## [代码审计、威胁建模与企业安全实践](/)

[首页](/)
[归档](/archives)
[威胁情报](/threat-broadcast)
[关于我](/about)
[留言](/comments)
[公益404](/404.html)

2026-11-16

[开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)►[CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)

约 759 字
约 2 分钟读完

2026-11-17

1. [首页](/)
2. [开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)
3. [CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)
4. CodeScan 实战（00）：从一次代码审计需求，到一套可追溯的工程实践

# CodeScan 实战（00）：从一次代码审计需求，到一套可追溯的工程实践

最初的需求很直接：从GitHub上发现[CodeScan-Artex](https://github.com/Ernket/CodeScan-Artex)，以及自己收集、改写的其他代码审计Skills、威胁建模Skills、代码审计智能体等等，希望以 CodeScan-Artex 为主，把其余项目中有用的威胁建模、漏洞分析、PoC 和证据管理机制接进来。

真正开始运行后，问题很快从“怎么让模型多找漏洞”，变成了另一组更具体的问题：任务是否真的被拆解？接口和权限有没有源码依据？模型说已经派发，数据库里为什么没有意图？一轮结束时，哪些事实实际保存了？

这个系列按改造过程逐篇记录。它既包含部署步骤，也保留那些没有完成、不能确认和需要继续验证的部分。

[![CodeScan实战系列封面：源码、建模分析与可追溯证据档案的概念插画。](/assets/codescan/00-series-cover-v1.webp)](/assets/codescan/00-series-cover-v1.webp "CodeScan 实战系列封面")

系列封面为概念插画，用于表达源码、建模与证据之间的联系。 [打开封面大图](/assets/codescan/00-series-cover-v1.webp)

## 0x01 系列范围

文章标题里的序号表示阅读顺序。

系列记录的主线是：

[![完整审计从源码范围、建模和入口复核，经过分批审计、证据与PoC、独立复核，形成报告与归档。](/assets/codescan/00-audit-overview-v1.webp)](/assets/codescan/00-audit-overview-v1.svg "从源码到交付：完整审计主线")

图 00｜完整审计主线示意；独立任务采用各自的交付条件。 [打开 SVG 原图](/assets/codescan/00-audit-overview-v1.svg)

其中，“独立威胁建模”“独立代码审计”“完整审计”是三个不同工作流。

## 0x02 全系列目录

| 篇目 | 要解决的问题 |
| --- | --- |
| [01｜本地部署](/codescan-01/) | Compose 如何与原 Artex 共存，更新时怎样保住状态 |
| [02｜项目集成](/codescan-02/) | 如何把其他项目优势统一成主项目里的材料契约 |
| [03｜审计方法与覆盖](/codescan-03/) | 怎样知道审了什么，还有哪些没审 |
| [04｜建模生命周期](/codescan-04/) | 创建任务后，谁来建模，何时允许进入审计 |
| [05｜工具空参数](/codescan-05/) | `save_threat_model({})` 到底在哪一层失败 |
| [06｜目标拆解恢复](/codescan-06/) | 前两轮模型失败后，拆解会不会被跳过 |
| [07｜逐次请求时间](/codescan-07/) | 怎样把耗时、用量和具体请求对起来 |
| [08｜任务类型与长上下文](/codescan-08/) | 如何缩小一轮工作的范围，并改善模型页面 |
| [09｜模型性能指标](/codescan-09/) | TTFT、Prefill、Decode 的采集边界是什么 |
| [10｜完整审计模式](/codescan-10/) | 同一个任务里如何先建模、再审计 |
| [11｜SSE 重连](/codescan-11/) | 两个端口同时登录，为什么实时列表仍然失败 |
| [12｜超时、循环与断点](/codescan-12/) | 79 轮之后，程序应该如何停止并交接 |
| [13｜Planner 实际进展](/codescan-13/) | 怎样识别“说已经做了”，却没有执行动作 |
| [14｜四任务复盘](/codescan-14/) | 怎样限制长时间空转，并避免保存时丢材料 |
| [15｜借鉴 Mantis](/codescan-15/) | 如何接入版本化批次、累计预算和代码导航 |
| [16｜资源清理](/codescan-16/) | 如何清理测试产物，同时保留状态和证据 |
| [17｜SDL 路线图](/codescan-17/) | 怎样通过旁路 Hook 接入研发流程 |

每篇都可以单独阅读；遇到术语和状态不清楚时，建议先看第 02、03 篇。

**下一篇：[用 Docker Compose 部署，与原 Artex 共存](/codescan-01/)。**

<https://www.pa55w0rd.online/codescan-00/>

分享到
[留言](/codescan-00/#comments)

* [CodeScan-Artex](/tags/CodeScan-Artex/)
* [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/)
* [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-00/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（01）：用 Docker Compose 部署，与原 Artex 共存](/codescan-01/)

## 留言

欢迎补充、纠错或交流；发表评论需使用 GitHub 账号登录。

正在加载留言…

请启用 JavaScript 以查看留言。

### 近期文章

* [CodeScan 实战（00）：从一次代码审计需求，到一套可追溯的工程实践](/codescan-00/)
* [CodeScan 实战（01）：用 Docker Compose 部署，与原 Artex 共存](/codescan-01/)
* [CodeScan 实战（02）：吸收其他项目的优势，统一威胁、漏洞与证据](/codescan-02/)
* [CodeScan 实战（03）：补齐审计覆盖、反证和收官门禁](/codescan-03/)
* [CodeScan 实战（04）：把威胁建模接进真正的任务生命周期](/codescan-04/)

### 分类

* [note](/categories/note/)46
* [web安全](/categories/web%E5%AE%89%E5%85%A8/)14
* [安全建设](/categories/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/)31
* [应急响应](/categories/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)4
* [开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)25
  + [CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)18
* [移动安全](/categories/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/)3

### 标签云

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [CI-CD](/tags/CI-CD/) [ChatGPT](/tags/ChatGPT/) [CodeScan-Artex](/tags/CodeScan-Artex/) [DevSecOps](/tags/DevSecOps/) [Docker](/tags/Docker/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [Mantis](/tags/Mantis/) [PHPstudy](/tags/PHPstudy/) [Planner](/tags/Planner/) [SDL](/tags/SDL/) [SSE](/tags/SSE/) [STRIDE](/tags/STRIDE/) [TRS](/tags/TRS/) [TTFT](/tags/TTFT/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/) [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/) [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/) [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [反证](/tags/%E5%8F%8D%E8%AF%81/) [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/) [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/) [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/) [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/) [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/) [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/) [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/) [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/) [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8/) [漏洞管理](/tags/%E6%BC%8F%E6%B4%9E%E7%AE%A1%E7%90%86/) [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/) [移动安全](/tags/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/) [编程基础](/tags/%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/) [蜜罐](/tags/%E8%9C%9C%E7%BD%90/) [解决方法](/tags/%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/) [记录](/tags/%E8%AE%B0%E5%BD%95/) [证据链](/tags/%E8%AF%81%E6%8D%AE%E9%93%BE/) [资产扫描](/tags/%E8%B5%84%E4%BA%A7%E6%89%AB%E6%8F%8F/) [身份认证](/tags/%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81/) [迁移](/tags/%E8%BF%81%E7%A7%BB/) [运维安全](/tags/%E8%BF%90%E7%BB%B4%E5%AE%89%E5%85%A8/) [运行复盘](/tags/%E8%BF%90%E8%A1%8C%E5%A4%8D%E7%9B%98/) [运行预算](/tags/%E8%BF%90%E8%A1%8C%E9%A2%84%E7%AE%97/) [速查表](/tags/%E9%80%9F%E6%9F%A5%E8%A1%A8/) [长上下文](/tags/%E9%95%BF%E4%B8%8A%E4%B8%8B%E6%96%87/) [长程任务](/tags/%E9%95%BF%E7%A8%8B%E4%BB%BB%E5%8A%A1/) [零信任](/tags/%E9%9B%B6%E4%BF%A1%E4%BB%BB/)

### 归档

* [2026年11月](/archives/2026/11/)18
* [2023年08月](/archives/2023/08/)2
* ...