---
title: CodeScan 实战（10）：从二选一，走到同一任务内的完整审计
url: https://www.pa55w0rd.online/codescan-10/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:37.257426
---

# CodeScan 实战（10）：从二选一，走到同一任务内的完整审计

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
4. CodeScan 实战（10）：从二选一，走到同一任务内的完整审计

# CodeScan 实战（10）：从二选一，走到同一任务内的完整审计

[系列目录](/codescan-00/) · 第 10 篇

两种独立任务解决了范围不清的问题，接着又出现一个自然需求：“我想两者都做，选哪一个？”

答案是增加明确的完整审计模式。同一个任务先建立和复核模型，再开展漏洞审计，所有阶段沿用同一套源码身份、目标、覆盖与证据。

## 0x01 三种模式各自有边界

| 模式 | 适用需求 | 流程 |
| --- | --- | --- |
| 独立威胁建模 | 架构评审、审计前准备 | 建模、查漏、模型交付 |
| 独立代码审计 | 已有范围，希望直接分析代码 | 入口复核、漏洞审计、证据交付 |
| 完整审计 `full_audit` | 在同一任务中完成两者 | 建模 → 入口权限复核 → 审计 → 收官 |

前端新建任务默认推荐完整审计，明确发送 `full_audit`。为了兼容旧调用方，原始 HTTP 请求不传 `task_mode` 时仍保留 `code_audit` 默认值。界面默认和接口兼容默认需要分别说明。

旧任务的类型、目标、源码和证据不在迁移中重写；用户也不必为一次更新重新上传全部材料。

## 0x02 先后顺序要靠程序控制

只把“请先建模”写进提示词，无法保证执行顺序。完整审计需要宿主检查：源码是否上传，当前模型是否基础就绪，模型依据的源码是否仍与任务一致。

模型尚未就绪或源码发生变化时，相关审计意图不能被提前领取。模型就绪后，任务仍保留审计工具和开放的审计目标，不把“模型已保存”当作整个任务完成。

这同样要求界面显示当前阶段和待补项。用户应能看出卡在入口完整性、权限未知，还是正在分析具体漏洞，而不是只看到一个总进度圈。

[![独立建模交付模型，独立审计不强制先建立完整模型，完整审计先建模和入口权限复核再审计，并统一检查证据与报告。](/assets/codescan/10-task-modes-v1.webp)](/assets/codescan/10-task-modes-v1.svg "三种任务类型，三套完成条件")

图 10｜三种模式的工作路径和交付范围，不把建模完成当作完整审计完成。 [打开 SVG 原图](/assets/codescan/10-task-modes-v1.svg)

## 0x03 可复用的完整任务目标

下面这份目标不绑定 Java，可以按项目范围删减：

> 1. 理解系统目的、技术栈、部署形态与保护资产。基于源码建立组件、调用与数据流、信任边界、安全控制，以及 STRIDE 威胁假设和核验计划。区分源码事实、假设、未知条件和范围排除；只有系统实际使用 AI、Agent、工具或记忆时才补充对应风险。
> 2. 梳理全部暴露面和触发点，包括 HTTP、RPC、GraphQL、WebSocket、消息事件、定时任务、CLI、库调用、管理及调试入口。逐项记录完整方法与 URI 或操作符号、处理函数、输入、认证链、角色、对象和租户授权，以及网关、配置、动态注册条件和源码证据。
> 3. 沿路由挂载、前缀拼接、中间件、代理重写和调用链交叉复核清单。分别确认入口真实存在、部署条件满足、权限实际生效；无法确认的保留未知及验证计划。基础模型就绪后，按入口、边界、子系统与生命周期拆分审计批次。
> 4. 逐项追踪攻击者可控输入、转换与校验、安全控制和敏感操作，核对可达性、利用前提及反证，检查同根因变体。每个候选漏洞提交原样源码、逐跳证据、影响、修复和可复现 PoC，说明环境依赖、准备步骤、专属成功判据、阴性对照与清理。
> 5. 汇总威胁处置、接口、文件和语义覆盖及剩余缺口。分别标明假设、静态确认、PoC 已生成、实际执行观察和独立复核。报告必须对应当前源码、模型及证据版本，不能用零发现或关键词零命中证明安全。
>
> 依赖审计：依据锁文件、构建清单、缓存和运行版本检查第三方框架、鉴权、解析、序列化及插件代码。按技术栈使用 Maven、Gradle、npm、pnpm、yarn、Python、Go、NuGet、Composer、Cargo 等依赖来源；必要且工具可用时读取源码、符号或反编译产物，保留来源和版本。缺少依赖、运行环境或工具时明确阻塞，不臆测实现，不把拟定 PoC 写成复现成功。

这份模板约束了交付内容，不意味着一次任务就能自动访问所有依赖缓存、启动所有运行环境。权限和工具仍以当前平台实际能力为准。

## 0x04 依赖审计不等于只看版本号

例如鉴权由第三方中间件完成，仅阅读业务控制器无法判断拒绝逻辑是否生效。需要确认实际加载版本、配置、调用路径和默认行为。

有源码先看源码；只有二进制时再评估符号或反编译。Java 本地 Maven 仓库只是其中一种来源，不能把 `.m2` 当作所有语言的固定步骤。

反编译结果还需要标记产物身份和局限，不能把看似相同的网上版本当作部署实例的真实代码。

## 0x05 这一轮验证到了哪里

验收覆盖类型迁移、源码上传、模型就绪前后的意图流转，以及建模完成后审计目标继续保留。受控测试使用隔离 PostgreSQL 和本地模拟 Provider。

前端检查了三种模式、默认选择、切换保留草稿和窄屏布局。这些是工程行为验证，没有据此声称已对真实业务完成完整审计。

[上一篇：性能指标](/codescan-09/) · [下一篇：实时连接与登录冲突](/codescan-11/)

<https://www.pa55w0rd.online/codescan-10/>

分享到
[留言](/codescan-10/#comments)

* [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/)
* [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/)
* [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-10/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（11）：一直重连，最后查到了端口之外的登录冲突](/codescan-11/)
[**下一篇 →**

CodeScan 实战（09）：TTFT、Prefill 和 Decode 到底测到了什么](/codescan-09/)

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

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [CI-CD](/tags/CI-CD/) [ChatGPT](/tags/ChatGPT/) [CodeScan-Artex](/tags/CodeScan-Artex/) [DevSecOps](/tags/DevSecOps/) [Docker](/tags/Docker/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [Mantis](/tags/Mantis/) [PHPstudy](/tags/PHPstudy/) [Planner](/tags/Planner/) [SDL](/tags/SDL/) [SSE](/tags/SSE/) [STRIDE](/tags/STRIDE/) [TRS](/tags/TRS/) [TTFT](/tags/TTFT/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/) [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/) [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/) [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [反证](/tags/%E5%8F%8D%E8%AF%81/) [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/) [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/) [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/) [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/) [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/) [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/) [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/) [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/) [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8/) [漏洞管理](/tags/%E6%BC%8F%E6%B4%9E%E7%AE%A1%E7%90%86/) [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/) [移动安全](/tags/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/) [编程基础](/tags/%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/) [蜜罐](/tags/%E8%9C%9C%E7%BD%90/) [解决方法](/tags/%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/) [记录](/tags/%E8%AE%B0%E5%BD%95/) [证据链](/tags/%E8%AF%81%E6%8D%AE%E9%93%BE/) [资产扫描](/tags/%E8%B5%84%E4%BA%A7%E6%89%AB%E6%8F%8F/) [身份认证](/tags/%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81/) [迁移](/tags/%E8%BF%81%E7%A7%BB/) [运维安全](/tags/%E8%BF%90%E7%BB%B4%E5%AE%89%E5%...