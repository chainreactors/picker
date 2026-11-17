---
title: CodeScan 实战（08）：拆开任务类型，收窄长上下文工作单元
url: https://www.pa55w0rd.online/codescan-08/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:36.973500
---

# CodeScan 实战（08）：拆开任务类型，收窄长上下文工作单元

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

约 1.5k 字
约 5 分钟读完

2026-11-17

1. [首页](/)
2. [开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)
3. [CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)
4. CodeScan 实战（08）：拆开任务类型，收窄长上下文工作单元

# CodeScan 实战（08）：拆开任务类型，收窄长上下文工作单元

[系列目录](/codescan-00/) · 第 08 篇

同一个入口既承担威胁建模，又承担完整漏洞审计，很容易让用户和调度器对“完成”产生不同理解。有人只想得到系统边界和威胁清单，有人已有模型，只想沿接口追踪漏洞。

这一轮先拆出两种独立任务，再收窄每次调用的工作量。后续需要两者连续执行时，增加了第 10 篇的“完整审计”模式。

## 0x01 类型先决定交付物

| 类型 | 主要工作 | 完成时必须交付 |
| --- | --- | --- |
| `threat_modeling` | 理解系统、暴露面、权限与信任边界，形成威胁假设 | 模型、来源、未知项与核验计划 |
| `code_audit` | 沿可达入口追踪输入、安全控制和敏感操作 | 覆盖、漏洞材料、反证、PoC 和报告 |

独立建模由 Planner 直接推进，不为它启动漏洞审计 Worker，也不要求每条威胁都变成漏洞或 PoC。独立审计不再强制先提交一份完整模型，但保留证据与交付门禁。

旧任务保留 `legacy_audit` 的原有语义，不能迁移时把已经运行的任务重新解释成另一类工作。

创建页按类型带出目标，切换时分别保留草稿。否则用户在“建模”里补了范围，切到“审计”又被系统默认文案覆盖，会造成任务输入悄悄丢失。

## 0x02 大窗口为什么仍然会卡

模型支持 200K 上下文，只说明一次能容纳较长输入，不代表单轮输出越长越好，也不说明服务支持多少并发。

此前客户端输出预算达到 32768 token，某次生成持续约 17 分钟。若模型服务实际只处理一个请求，其他任务和连接测试就要等待。30 秒测试超时，可能是服务忙，也可能是网络故障，不能只凭超时判定模型不可用。

平台随后增加了端点活动信息：发现已有活动 HTTP 请求时，连接测试明确提示忙碌及“尚未测试”，不把排队混进一个真假难辨的健康结果。

## 0x03 给每轮输出设上限

当前 `agent/budget.go` 的 `ReplyBudget` 采用以下规则：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` 目标拆解：默认上限 4096 其他角色：默认上限 8192 配置更小的正数：尊重更小配置 已知上下文窗口：进一步限制为不超过窗口的四分之一 ``` |

这是客户端生成预算，不会修改远端服务的上下文长度或并发配置。它也不是“每轮必须写满”的目标。

更有用的变化是任务粒度：一次意图只推进一条入口调用链或一组相关文件。保存证据、版本、未解决项和下一步后再继续，避免把“全仓所有接口全部审计完”交给一个 Worker。

## 0x04 大材料留在持久层

长程运行的主要负担经常是重复搬运。完整模型、源码清单和覆盖账本每轮都回传，输入会越来越大，压缩时又可能丢掉细节。

这轮采用分页读取、任务目录文件提交和小回执；大窗口提前压缩，摘要本身也有限额。工具返回 `partial=true` 时继续读 `next_offset`，不能把第一页当作全量清单。

摘要只负责导航，不能用摘要覆盖原始完整材料。多个 Worker 产生的覆盖增量由 Planner 合并；没有覆盖保存权限的 Worker 用事实记录交接范围、路径和剩余项，不借用漏洞工具存任意账本。

[![完整源码和账本保留在持久层，每次读取当前批次，限制输出预算并保存证据和断点，再进入下一批，不用摘要覆盖完整材料。](/assets/codescan/08-bounded-context-v1.webp)](/assets/codescan/08-bounded-context-v1.svg "长程任务：每次只推进一个可验收批次")

图 08｜大材料持久保存、分页读取与小批次推进的关系。 [打开 SVG 原图](/assets/codescan/08-bounded-context-v1.svg)

## 0x05 按类型写目标，比一份超长通用提示更清楚

独立建模可以使用这样的目标：

> 基于当前源码和部署材料，确认系统目的、保护资产、组件、真实入口、认证授权、数据流与信任边界。为关键威胁建立来源、前提、安全控制及核验计划，明确事实、假设、未知和范围排除。只有目标实际包含 AI、Agent、工具或记忆时才加入对应风险。本任务交付威胁模型，不把尚未验证的威胁写成漏洞结论。

独立审计可以使用这样的目标：

> 交叉复核入口与权限清单，沿攻击者可控输入到敏感操作追踪转换、校验和安全控制，核对可达性、利用前提、反证和同根因变体。依据实际依赖版本检查第三方实现。每个候选漏洞保留源码、逐跳证据、影响、修复与可复现 PoC，区分静态结论、已生成材料和实际执行结果，汇总覆盖缺口与剩余阻塞。

“先建模再审计”的完整目标见第 10 篇。模板应让任务产生可核对的交付物，而不是靠“深入、全面、不要遗漏”几个形容词增加保证。

## 0x06 威胁建模页面也要控制读取成本

页面改为待补项置顶，并按系统信息、入口权限、数据流与边界、STRIDE、威胁控制、未知范围、源码证据等区域组织。搜索、状态筛选、证据跳转和每类 50 条展示，帮助人逐项复核。

完整下载仍然保留。分页只影响当前阅读和渲染，不删模型，也不改变总数。

该轮完成针对性后端、数据库、前端类型与构建检查，并用 Mock 数据核验布局。Mock 页面通过，不等于真实业务任务已经跑完，更不等于长上下文成本降低了某个确定百分比。

[上一篇：逐次请求账本](/codescan-07/) · [下一篇：性能指标的测量边界](/codescan-09/)

<https://www.pa55w0rd.online/codescan-08/>

分享到
[留言](/codescan-08/#comments)

* [CodeScan-Artex](/tags/CodeScan-Artex/)
* [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/)
* [长上下文](/tags/%E9%95%BF%E4%B8%8A%E4%B8%8B%E6%96%87/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-08/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（09）：TTFT、Prefill 和 Decode 到底测到了什么](/codescan-09/)
[**下一篇 →**

CodeScan 实战（07）：给每次模型请求补上时间与计量账本](/codescan-07/)

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

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [CI-CD](/tags/CI-CD/) [ChatGPT](/tags/ChatGPT/) [CodeScan-Artex](/tags/CodeScan-Artex/) [DevSecOps](/tags/DevSecOps/) [Docker](/tags/Docker/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [Mantis](/tags/Mantis/) [PHPstudy](/tags/PHPstudy/) [Planner](/tags/Planner/) [SDL](/tags/SDL/) [SSE](/tags/SSE/) [STRIDE](/tags/STRIDE/) [TRS](/tags/TRS/) [TTFT](/tags/TTFT/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/) [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/) [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/) [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [反证](/tags/%E5%8F%8D%E8%AF%81/) [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/) [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/) [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/) [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/) [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/) [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/) [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/) [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/) [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8/) [漏洞管理](/tags/%E6%BC%8F%E6%B4%9E%E7%AE%A1%E7%90%86/) [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/) [移动安全](/tags/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/) [编程基础](/tags/%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/) [蜜罐](/tags/%E8%9C%9C%E7%BD%90/) [解决方法](/tags/%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/) [记录](/tags/%E8%AE%B0%E5%BD%95/) [证据链](/tags/%E8%AF%81%E6%8D%AE%E9%93%BE/) [资产扫描](/tags/%E8%B5%84%E4%BA%A7%E6%89%AB%E6%8F%8F/) [身份认证](/tags/%E8%BA%AB%E4%BB%BD...