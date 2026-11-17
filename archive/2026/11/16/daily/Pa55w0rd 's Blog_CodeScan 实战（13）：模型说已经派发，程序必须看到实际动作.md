---
title: CodeScan 实战（13）：模型说已经派发，程序必须看到实际动作
url: https://www.pa55w0rd.online/codescan-13/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:37.682530
---

# CodeScan 实战（13）：模型说已经派发，程序必须看到实际动作

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

约 1.1k 字
约 3 分钟读完

2026-11-17

1. [首页](/)
2. [开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)
3. [CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)
4. CodeScan 实战（13）：模型说已经派发，程序必须看到实际动作

# CodeScan 实战（13）：模型说已经派发，程序必须看到实际动作

[系列目录](/codescan-00/) · 第 13 篇

真实运行里出现过这样的规划输出：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` No response requested No tool calls needed. 已按要求派出一条入口梳理意图。 ``` |

问题是，程序没有看到新意图。模型声称派发，不等于 `add_intent` 已调用并落库；“不需要工具”也不能证明尚未完成的目标已经推进。

## 0x01 先分清没有动作是否合理

并非每轮都应该新建意图。已经有 Worker 在运行时，Planner 可以等待；独立威胁建模也可能直接保存模型和事实，而不派发审计 Worker。

因此不能写成“每轮没有工具调用就失败”。真正需要识别的是：

> 本任务仍有未完成目标，没有待执行或运行中的意图，且这一轮没有产生实际持久化进展。

这是调度停滞问题，与模型是否写了长篇规划没有直接关系。

## 0x02 用数据库变化核对进展

这一轮围绕本任务读取开放目标、活动意图、最近意图、漏洞材料、事实和审计版本等状态，比较规划前后变化。

比较范围必须限定当前任务。两个任务并行时，另一个任务插入了事实，不能被拿来证明本任务有进展。

对真实执行状态的判断大致如下：

| 观察 | 解释 |
| --- | --- |
| 新意图落库 | 已产生可调度动作 |
| 新事实、模型或漏洞材料落库 | 可能产生直接推进，继续核对内容与阶段 |
| 已有 Worker 正在运行 | 可以等待，不强迫重复派发 |
| 只有“已经派发”的文字 | 没有执行回执，不能算派发成功 |
| 目标未完成、无活动、无新增 | 触发停滞纠偏 |

这些信号不等于最终质量评分，主要用于防止调度器把无动作当作成功。

## 0x03 一次纠偏之后仍没有进展怎么办

首次判定停滞后，宿主明确告知模型：尚有目标未完成，没有实际落地动作，需要核对状态并推进。

如果立即纠偏后仍然只有 `No tool calls needed.`，任务以 `planner_no_progress` 失败结束，并展示原因。原输出保留为排查材料，不作为成功回执。

这类失败是程序的保护性终止，表示运行无法自行推进，不表示项目无漏洞，也不表示此前证据被删除。修正模型链路、工具契约或任务范围后，可以基于保留材料重新启动。

无限纠偏会让一个静止的任务持续计费；直接标完成则会制造更严重的假成功。

[![存在开放目标时先检查活动意图和实际保存进展，均没有时纠偏一次，再无进展才按planner_no_progress保护性失败。](/assets/codescan/13-planner-progress-v1.webp)](/assets/codescan/13-planner-progress-v1.svg "Planner 的进展，要看持久化动作")

图 13｜Planner 停滞判断与一次纠偏，不将模型声明作为成功回执。 [打开 SVG 原图](/assets/codescan/13-planner-progress-v1.svg)

## 0x04 根因不能从一句输出反推

`No tool results provided.` 可能涉及对话格式、工具结果衔接、模型模板、代理转换或模型自身选择。只有显示这句话，不足以判定是哪一项。

当时的真实最小探针在独立数据库中成功调用了 `add_intent`，说明基本工具调用路径能工作。它没有复现全部长上下文和并发条件，所以也不能反过来证明完整业务链路正常。

尤其不能得出“模型完全不支持工具”这样的结论。需要关联原始报文、工具定义、上下文和服务端模板，才有可能进一步缩小原因。

## 0x05 让失败对操作员有用

任务页面至少应说清楚：还剩多少目标、有没有活动意图、最后实际落库的动作是什么、纠偏是否尝试过，以及停止原因。

如果只剩一句“模型失败”，操作员很难决定是重派、缩小范围，还是先修服务。若页面直接保留模型原话，也容易让人误以为“已派发”是程序确认。

本轮验证覆盖任务隔离、已有工作例外、纠偏后无进展、直接保存进展和真实最小工具探针；并未因此宣称完整业务长程运行已经稳定。

[上一篇：Worker 预算](/codescan-12/) · [下一篇：四任务运行复盘](/codescan-14/)

<https://www.pa55w0rd.online/codescan-13/>

分享到
[留言](/codescan-13/#comments)

* [Planner](/tags/Planner/)
* [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/)
* [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-13/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（14）：四个真实任务复盘：预算、失败保护与增量保存](/codescan-14/)
[**下一篇 →**

CodeScan 实战（12）：79 轮仍然超时：给循环、收尾与断点设边界](/codescan-12/)

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
* [2022年03月](/archives/2022/03/)5
* [2021年12月](/ar...