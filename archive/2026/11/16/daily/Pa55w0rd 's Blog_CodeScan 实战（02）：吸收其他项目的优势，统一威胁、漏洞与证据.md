---
title: CodeScan 实战（02）：吸收其他项目的优势，统一威胁、漏洞与证据
url: https://www.pa55w0rd.online/codescan-02/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:36.077203
---

# CodeScan 实战（02）：吸收其他项目的优势，统一威胁、漏洞与证据

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

约 1.2k 字
约 4 分钟读完

2026-11-17

1. [首页](/)
2. [开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)
3. [CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)
4. CodeScan 实战（02）：吸收其他项目的优势，统一威胁、漏洞与证据

# CodeScan 实战（02）：吸收其他项目的优势，统一威胁、漏洞与证据

[系列目录](/codescan-00/) · 第 02 篇

改造保留了 CodeScan-Artex 的 Go 后端、任务编排、双图和 PostgreSQL，把其他项目中有价值的机制落到已有执行路径里。

我首先关注的是材料能否在系统里流转：模型提到的威胁、接口、源码、漏洞和 PoC，怎样对应到同一个版本？

## 0x01 分别吸收了什么

| 来源 | 借鉴重点 | 主项目落点 |
| — | — | — | — |
| 威胁建模项目 | STRIDE、组件、数据流、信任边界和源码引用校验 | 模型契约、源码校验与威胁模型工作区 |
| VeriAudit | Source→Sink、传播关系、安全控制、PoC 和验证分工 | `audit.Case`、`audit.PoC` 与独立复核 |
| 知弈 AgentOS | 内容摘要、追加版本、前序哈希、归属校验和幂等 | 审计记录链、归档恢复与证据包校验 |

当次记录还保留了各仓库的许可核对结果，因此没有直接搬入大段实现或提示词。

## 0x02 用一份漏洞契约串起材料

`audit.Case` 保存一条候选漏洞的关键内容：

* 审计时的源码版本与文件摘要。
* Source、Sink、逐跳传播证据及安全控制。
* 攻击者能力、成立前提、影响和修复建议。
* PoC 环境、准备步骤、载荷、成功判据、阴性对照和清理。
* 威胁模型关联与保存时的模型快照。

这份结构要能被 Agent 提交、后端读取、页面展示和报告导出。只在提示词里要求“给出完整证据链”，无法保证后面的系统接得到这些材料。

## 0x03 源码证据由宿主重新读取

源码引用包含相对路径、精确行范围、原样片段和 SHA-256。保存时，服务端从本任务源码根目录重新读取并核对。

这样可以发现路径越界、文件变化、片段不匹配和引用缺失。重复代码片段也不能通过“随便找一个相似位置”来通过检查。

但引用匹配只回答“这段内容是否在这个版本中”。从公开入口是否可达、上游有没有鉴权、攻击者能否控制这个值，仍需要沿调用与数据流检查。

## 0x04 把几种状态分清楚

| 状态 | 含义 |
| --- | --- |
| `needs_validation` | 材料存在缺口，返回具体待补项 |
| `poc_generated` | 结构化材料和引用检查满足要求，PoC 已生成 |
| `oracle_matched` | 本地观测满足所配置的判据，阴性对照未命中 |
| `not_reproduced` | 本次运行没有观察到判据 |
| `blocked` | 运行失败、响应不完整或缺少条件 |

独立复核另有 `confirmed / refuted / inconclusive`。这两套状态分别表达材料及观测质量、漏洞判断，不能用一个布尔字段把它们合并。

## 0x05 PoC 分为材料和实际观测

Agent 继续保持静态分析边界。它生成复现步骤和载荷，操作员再在明确的本地环境运行。

新增的 HTTP 运行器只接受显式回环 IP，不跟随重定向，也不启动任意目标进程。请求参数、HTTP 解析后的响应头、原始正文和摘要都会保留。响应截断或解析失败时，应保持受阻状态。

平台导入执行记录时还会核验签名、Case/PoC 摘要和当前证据版本。签名表达的是持有密钥的操作员提交了这份记录；目标的构建来源和漏洞语义仍要另外证明。

## 0x06 版本链和报告如何联动

模型、漏洞契约和执行记录采用追加版本，保留前序摘要。写入带当前读取的 `expected_revision`，并发冲突时重新读取，避免后保存的草稿覆盖别人已经补好的内容。

还有一个容易混淆的字段：`evidence_version` 表示报告所依据的整体证据版本，审计材料链的 `revision` 表示对应记录链的修订。两者用途不同。

材料变化后，旧报告应显示待更新。归档恢复和 ZIP 导出也要保留这些版本关系，使复核者知道报告依据的是哪一批材料。

[![威胁建模、Source到Sink审计与版本溯源机制汇入audit.Case，再由源码核验、观测复核和报告归档组成证据闭环。](/assets/codescan/02-evidence-contract-v1.webp)](/assets/codescan/02-evidence-contract-v1.svg "不同方法，汇入同一份漏洞材料")

图 02｜方法、材料契约与交付之间的关系示意。 [打开 SVG 原图](/assets/codescan/02-evidence-contract-v1.svg)

## 0x07 这一轮留下的基础

这一轮把“能够写出分析”推进到“材料可以保存、展示、复核、导出”。接下来还需要解决覆盖范围：即使每条漏洞材料都完整，也无法据此回答整个仓库审到了哪里。

源码入口：`audit/model.go`、`audit/source.go`、`db/audit.go`、`agent/audit_tools.go`。

[上一篇：本地部署](/codescan-01/) · [下一篇：覆盖与收官门禁](/codescan-03/)

<https://www.pa55w0rd.online/codescan-02/>

分享到
[留言](/codescan-02/#comments)

* [CodeScan-Artex](/tags/CodeScan-Artex/)
* [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/)
* [证据链](/tags/%E8%AF%81%E6%8D%AE%E9%93%BE/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-02/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（03）：补齐审计覆盖、反证和收官门禁](/codescan-03/)
[**下一篇 →**

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

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [CI-CD](/tags/CI-CD/) [ChatGPT](/tags/ChatGPT/) [CodeScan-Artex](/tags/CodeScan-Artex/) [DevSecOps](/tags/DevSecOps/) [Docker](/tags/Docker/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [Mantis](/tags/Mantis/) [PHPstudy](/tags/PHPstudy/) [Planner](/tags/Planner/) [SDL](/tags/SDL/) [SSE](/tags/SSE/) [STRIDE](/tags/STRIDE/) [TRS](/tags/TRS/) [TTFT](/tags/TTFT/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/) [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/) [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/) [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [反证](/tags/%E5%8F%8D%E8%AF%81/) [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/) [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/) [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/) [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/) [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/) [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/) [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/) [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/) [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8/) [漏洞管理](/tags/%E6%BC%8F%E6%B4%9E%E7%AE%A1%E7%90%86/) [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/) [移动安全](/tags/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/) [编程基础](/tags/%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/) [蜜罐](/tags/%E8%9C%9C%E7%BD%90/) [解决方法](/tags/%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/) [记录](/tags/%E8%AE%B0%E5%BD%95/) [证据链](/tags/%E8%AF%81%E6%8D%AE%E9%93%BE/) [资产扫描](/tags/%E8%B5%84%E4%BA%A7%E6%89%AB%E6%8F%8F/) [身份认证](/tags/%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81/) [迁移](/tags/%E8%BF%81%E7%A7%BB/) [运维安全](/tags/%E8%BF%90%E7%BB%B4%E5%AE%89%E5%85%A8/) [运行复盘](/tags/%E8%BF%90%E8%A1%8C%E5%A4%8D%E7%9B%98/) [运行预算](/tags/%E8%BF%90...