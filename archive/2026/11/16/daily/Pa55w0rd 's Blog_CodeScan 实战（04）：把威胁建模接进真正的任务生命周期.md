---
title: CodeScan 实战（04）：把威胁建模接进真正的任务生命周期
url: https://www.pa55w0rd.online/codescan-04/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:36.375298
---

# CodeScan 实战（04）：把威胁建模接进真正的任务生命周期

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
4. CodeScan 实战（04）：把威胁建模接进真正的任务生命周期

# CodeScan 实战（04）：把威胁建模接进真正的任务生命周期

[系列目录](/codescan-00/) · 第 04 篇

当时提出的问题是：创建代码审计任务后，会不会自动做威胁建模？

只在任务目标里加一句“先建模”，不能回答谁来做、做完保存在哪里，以及什么时候允许后续审计启动。这一轮把建模变成了实际阶段。

## 0x01 建模从源码和系统目的开始

模型需要说明系统保护什么、如何部署、哪些主体能够进入、数据在哪些组件之间流动，以及哪些位置跨越信任边界。

我希望入口清单至少回答下面这些问题：

| 事项 | 需要保留的内容 |
| --- | --- |
| 路由真实性 | 方法、完整 URI 或操作符号、挂载位置及动态注册条件 |
| 身份与权限 | 认证链、角色、对象归属和租户授权 |
| 输入 | 攻击者能够控制哪些字段，经过了什么转换 |
| 数据流 | 组件间调用、存储、消息及第三方依赖 |
| 依据 | 当前源码片段、配置事实和无法确认的条件 |

HTTP 之外，RPC、WebSocket、消息、定时任务、CLI 和管理入口也需要按项目实际情况检查。

## 0x02 STRIDE 覆盖到具体元素

如果只写六段 STRIDE 介绍，很容易形成一份通用模板。更有用的方式是把威胁假设落到组件、数据流、信任边界和入口上。

每个假设需要对应资产、攻击者能力、安全控制和核验计划。源码已经能证明的事实与部署条件未知的部分，要分开记录。

只有被测系统实际使用 AI、Agent、MCP、工具或记忆时，才补充这些风险。审计平台自身使用大模型，不会让每个被测项目都自动具有相同的 AI 风险面。

## 0x03 程序阶段怎样接起来

这一轮的自动前置流程由宿主登记建模任务，Planner 分批读取源码、补模型并保存。基础模型未就绪时，后续审计派发会受到约束。

关键点是把“创建页面”和“开始执行”分开。查看一个尚未启动的任务，不应偷偷触发模型请求；用户启动后，阶段状态才按实际流程推进。

模型保存仍使用当前修订号、源码清单和内容摘要。草稿可以保存，但材料缺口必须可见。

[![创建任务与显式启动分开，启动后建模并复核真实入口权限，基础模型就绪后进入审计；源码或模型变化需要复核。](/assets/codescan/04-model-lifecycle-v1.webp)](/assets/codescan/04-model-lifecycle-v1.svg "建模前置：由启动推进的任务生命周期")

图 04｜建模前置流程及源码变化后的复核关系。 [打开 SVG 原图](/assets/codescan/04-model-lifecycle-v1.svg)

## 0x04 模型变化后怎样处理

威胁模型需要对应本次源码。代码、入口或控制条件变化时，旧假设应重新核对；不能继续拿旧摘要当作新版本的结论。

同样，保存成功只说明结构与引用检查通过，无法自动证明所有架构元素都已穷尽。对动态路由、运行时中间件和缺失依赖，应保留明确未知项。

## 0x05 后来为什么还要拆分任务类型

自动前置适合完整审计，却不适合所有场景。用户可能只想交付威胁模型，也可能已有可信模型，只需要审计指定接口。

所以这一轮是阶段治理的起点，后续第 08 篇引入独立类型，第 10 篇再提供同一任务内的完整审计。阅读历史记录时，需要留意对应版本，避免把早期的强制前置套用到后来的独立代码审计。

## 0x06 验收与剩余边界

本轮通过受控模型、数据库和源码检查路径验证阶段约束，并形成了本地部署记录。测试关注草稿保存、引用校验、源码变化后的失效、派发条件和目标交付。

它没有给真实业务仓库做一次完整的模型驱动安全验收，也没有证明威胁模型覆盖了所有未知部署行为。

源码入口：`db/audit_phase.go`、`agent/planner.go`、`server/engine.go`。

[上一篇：覆盖与收官门禁](/codescan-03/) · [下一篇：工具空参数](/codescan-05/)

<https://www.pa55w0rd.online/codescan-04/>

分享到
[留言](/codescan-04/#comments)

* [CodeScan-Artex](/tags/CodeScan-Artex/)
* [STRIDE](/tags/STRIDE/)
* [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-04/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（05）：save\_threat\_model 为什么会收到空参数](/codescan-05/)
[**下一篇 →**

CodeScan 实战（03）：补齐审计覆盖、反证和收官门禁](/codescan-03/)

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
* [2021年12月](/archives/2021/12/)2
* [2021年09月](/archives/2021/09/)1
* [2021年08月](/archives/2021/08/)5
* [2021年07月](/archives/2021/07/)1
* [2021年06月](/archives/2021/06/)1
* [2021年05月](/archives/2021/05/)...