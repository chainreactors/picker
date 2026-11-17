---
title: CodeScan 实战（15）：借鉴 Mantis：版本化批次、累计预算和导航
url: https://www.pa55w0rd.online/codescan-15/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:37.969906
---

# CodeScan 实战（15）：借鉴 Mantis：版本化批次、累计预算和导航

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

约 1.3k 字
约 4 分钟读完

2026-11-17

1. [首页](/)
2. [开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)
3. [CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)
4. CodeScan 实战（15）：借鉴 Mantis：版本化批次、累计预算和导航

# CodeScan 实战（15）：借鉴 Mantis：版本化批次、累计预算和导航

[系列目录](/codescan-00/) · 第 15 篇

Google Mantis 有参考价值，但直接搬进另一套智能体框架，并不能自动修复本项目的长程任务问题。这一轮选择借鉴机制：工作批次绑定、累计预算、源码导航和分层评测，继续使用现有 Go 架构。

研究基于固定提交 `b51f9ced3590d0a640134374772f7eb8e06e976f`。本文记录的是该轮候选状态，不代表 Mantis 当前最新版本，也不代表本轮改造已经部署。

## 0x01 一个批次到底审的是哪份代码

之前保存了断点，但如果源码、模型、意图或工具配置变化，直接复用旧会话可能把两个上下文混在一起。

新增宿主批次记录，将源码清单、威胁模型材料、意图和配置摘要绑定，并记录尝试次数、状态和写回计数。绑定一致才能续跑；绑定变化则隔离旧对话和断点，旧证据保留。

执行结束还要检查源码与配置是否改变，不能只在启动时检查一次。批次 `finished` 只说明这次执行结束，不自动代表对应接口、文件或语义已经审完。

这部分借鉴了 Mantis 的[预算与批次设计](https://github.com/google/mantis/blob/b51f9ced3590d0a640134374772f7eb8e06e976f/reference/core/budget.py)，实现没有引入其 ADK 或 Python 工作流。

## 0x02 预算不能重启一次就重新计算

单轮限制可以防空转，但任务反复重启仍可能持续消耗。于是增加可选的任务级请求数和 token 总额度，规划、审计、对话与压缩共用持久化账本。

并发调用先在 PostgreSQL 中原子预占，再进入 Provider。旧任务默认保持原策略；需要启用时，在暂停且没有在途调用的状态下显式设置，并进行版本比较。

这里有几个需要说明的口径：

* 外层重新调用会增加请求数；SDK 内部重试仍包含在一次 Provider 调用中。
* token 预占依据请求字节量与最大输出预算估计，不是精确 tokenizer。
* 完整用量返回后，按输入与输出结算，不把输入中的缓存读取再重复相加。
* 用量缺失时保守保留预占，不把失败请求当作零成本退款。

因此它是任务准入和止损机制，不是账单系统，也不能承诺预估值永远等于实际 token。预算耗尽使用独立原因，不伪装成模型服务错误。

## 0x03 导航工具先承认自己的能力范围

`navigate_source` 每次最多 32 个文件、单文件 2 MiB、每页最多 100 项，只读，不执行目标、不安装依赖。

Go 使用原生 AST 定位函数声明、边界和语法调用位置；其他支持的语言先返回文本候选，明确提示注释、字符串、动态调用和未解析关系造成的误差。

这不是已经完成的跨语言语义调用图。借鉴[结构索引](https://github.com/google/mantis/blob/b51f9ced3590d0a640134374772f7eb8e06e976f/reference/core/structural_index.py)的价值，在于让模型更快定位、让工具说明缺口，而不是给所有文本命中贴上“可达调用链”的标签。

## 0x04 先建立能失败的效果基线

新增六个缩小样例，组成三组正负对照：Python 文件路径、Go SQL、TypeScript 跨文件租户授权。答案放在上传源码之外，审计执行与评分分开。

独立复核者依据结果标为 `vulnerable`、`safe` 或 `unknown`。这里的 safe 仅表示指定不变式被保护，不代表整个样例或项目没有其他风险。

评分器统计精确率、召回率、负例误报率、未知比例，以及有效发现的 token 和耗时。未审正例不能当成正确发现；未知负例不能当成正确排除。没有阳性预测时精确率为未知，不写成 100%。

公开样例只是回归起点，不能用计分器自检代替真实模型效果评测，也不能排除答案泄漏和训练污染。Mantis 的[分层评测说明](https://github.com/google/mantis/blob/b51f9ced3590d0a640134374772f7eb8e06e976f/reference/evals/README.md)提供了区分工程检查与端到端效果的参考。

[![Mantis借鉴形成版本化批次、累计预算、有限源码导航和六个正负样例评测，候选构建、部署与实际效果分别验收。](/assets/codescan/15-mantis-mechanisms-v1.webp)](/assets/codescan/15-mantis-mechanisms-v1.svg "借鉴 Mantis：四项候选机制")

图 15｜四项候选机制及各自验证边界，图示不代表已部署。 [打开 SVG 原图](/assets/codescan/15-mantis-mechanisms-v1.svg)

## 0x05 哪些内容没有直接照搬

[补丁技能](https://github.com/google/mantis/blob/b51f9ced3590d0a640134374772f7eb8e06e976f/skills/mantis-patch/SKILL.md)中的独立复现、阴性对照和再攻击值得继续做，但写在技能里的要求，不自动成为宿主能验证的硬约束。

当时固定版本的 [GitHub Action 文档](https://github.com/google/mantis/blob/b51f9ced3590d0a640134374772f7eb8e06e976f/reference/docs/github-action.md)也保留真实项目端到端验证限制，因此本项目没有据此新增自动合并阻断、自动修复或生产利用流程。

## 0x06 候选版验收与未完成项

该轮完成七个 Go 包编译、两项导航测试、七项 Python 计分器测试、前端类型检查、33 页静态导出和 Linux 候选构建。旧静态资源摘要和新页面引用也做了核对。

最终 PostgreSQL 并发预算、部分用量处理和归档恢复集成回归尚未补齐；没有进行真实模型效果评测、浏览器交互或漏洞复现。

[上一篇：四任务复盘](/codescan-14/) · [下一篇：中间产物清理](/codescan-16/)

<https://www.pa55w0rd.online/codescan-15/>

分享到
[留言](/codescan-15/#comments)

* [Mantis](/tags/Mantis/)
* [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/)
* [运行预算](/tags/%E8%BF%90%E8%A1%8C%E9%A2%84%E7%AE%97/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-15/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（16）：清理 5 GB 中间产物，保住运行状态和证据](/codescan-16/)
[**下一篇 →**

CodeScan 实战（14）：四个真实任务复盘：预算、失败保护与增量保存](/codescan-14/)

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

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [CI-CD](/tags/CI-CD/) [ChatGPT](/tags/ChatGPT/) [CodeScan-Artex](/tags/CodeScan-Artex/) [DevSecOps](/tags/DevSecOps/) [Docker](/tags/Docker/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [Mantis](/tags/Mantis/) [PHPstudy](/tags/PHPstudy/) [Planner](/tags/Planner/) [SDL](/tags/SDL/) [SSE](/tags/SSE/) [STRIDE](/tags/STRIDE/) [TRS](/tags/TRS/) [TTFT](/tags/TTFT/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/) [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/) [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/) [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [反证](/tags/%E5%8F%8D%E8%AF%81/) [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/) [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/) [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/) [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/) [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/) [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/) [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/) [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/) [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8/) [漏洞管理](/tags/%E6%BC%8F%E6%B4%9E%E7%AE%A1%E7%90%86/) [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/) [移动安全](/tags/%E7%A7%BB%...