---
title: CodeScan 实战（06）：模型恢复了，目标拆解也要继续
url: https://www.pa55w0rd.online/codescan-06/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:36.646514
---

# CodeScan 实战（06）：模型恢复了，目标拆解也要继续

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
4. CodeScan 实战（06）：模型恢复了，目标拆解也要继续

# CodeScan 实战（06）：模型恢复了，目标拆解也要继续

[系列目录](/codescan-00/) · 第 06 篇

一次任务的前两轮都因模型服务连接失败结束。第三轮恢复后，Planner 开始读取源码、准备威胁建模。新的问题随之出现：最前面的目标拆解到底做过没有，是页面没显示，还是程序已经跳过去了？

这不能靠模型补一句“已经理解目标”来解释。任务调度需要知道，一个阶段是否真正产生了可恢复的结果。

## 0x01 原始要求和系统目标不能混在一起

创建任务时，用户可能提交很长的要求：接口枚举、权限复核、依赖审计、逐漏洞 PoC、报告归档。程序为了维持工作流，也会补充最低交付要求。

这两种内容应分别保留。系统预置了几个目标，不代表用户原始要求已经完成拆解；模型输出一段计划，也不代表这些计划已经成为任务可执行、可判定的目标。

因此先保存用户原文，再保存拆解状态与拆解结果。页面显示、后续调度和恢复逻辑都读取这个状态，不能通过“现在不是第零轮”推断前置阶段已经成功。

## 0x02 失败的阶段要留在待办里

这一轮改造的核心，是把目标拆解从一次临时调用，改成有持久化状态的步骤：

[![原始目标进入拆解，失败保留待办并退避，恢复后补做；有效目标与成功状态原子提交，再进入后续建模或审计。](/assets/codescan/06-goal-recovery-v1.webp)](/assets/codescan/06-goal-recovery-v1.svg "失败阶段留在待办中，恢复后先补做")

图 06｜目标拆解的持久化、退避重试与恢复示意。 [打开 SVG 原图](/assets/codescan/06-goal-recovery-v1.svg)

模型暂时不可用时，不写“拆解成功”。模型恢复后，调度先检查仍缺失的拆解，再推进后续阶段。

成功状态与目标写入需要保持一致。否则进程在两次写入之间退出，会出现“状态成功但没有目标”，或者“目标已经插入但下一次又重复插入”。

## 0x03 恢复时不能删掉已经有用的东西

恢复并不等于重建整个任务。可能已经有人工补充目标，也可能有意图与现有目标关联。一次自动重试不能把它们清空。

处理原则是：失败结果不作为正式目标集；成功结果去重并原子落库；保留人工目标和已有关系。已有事实、源码、漏洞材料也不因前置阶段补做而被删除。

这使“补齐遗漏阶段”和“推倒重跑”成为两件不同的操作。长期任务尤其需要前者，否则每次短暂故障都会变成一次昂贵的全量重跑。

## 0x04 重试要给模型服务恢复时间

连接被拒绝通常意味着目标地址上没有可接受连接的服务，或者路径中的转发不可用。它不是“已经审过一次源码但没找到漏洞”。

当时为拆解失败加入了退避：30 秒、1 分钟、2 分钟、4 分钟，之后最长 5 分钟。这个间隔属于该轮实现记录，部署时仍应核对当前配置。

用户暂停任务时不继续调用；服务未恢复时，也不应靠高频空转制造更多失败轮次。页面需要区分“等待重试”“用户暂停”和“已完成”，让操作者知道下一步是等待服务恢复，还是修改任务材料。

## 0x05 如何判断第三轮有没有补做

比起只看规划文字，更可靠的是一起看三类记录：

| 记录 | 要回答的问题 |
| --- | --- |
| 拆解状态 | 上次失败后，是否出现后续成功提交 |
| 持久化目标 | 用户要求是否落成真实目标，有没有重复或遗漏 |
| 调度与工具轨迹 | 后续阶段依据了哪些目标，实际调用了什么 |

只看到模型开始 `LS`、`Read`，最多能说明它开始探索，不能证明此前拆解已经完成。修复后的验证应包含“前几次失败、后一次成功”的受控序列，并检查数据库最终状态。

## 0x06 验收和仍然存在的限制

该轮进行了针对性的 Go、数据库与前端构建检查，验证重试、去重、旧目标保留及显示状态，并留下历史部署记录。

这些检查没有使远端模型服务自动获得高可用能力，也没有保证每次自然语言目标都能被拆成最佳粒度。它们解决的是：故障不会被当成完成，恢复后有明确补做入口，结果能被程序和用户共同核对。

下一步还需要把每一次实际模型调用的时间和消耗记下来，才能解释“卡在拆解”究竟是在排队、生成还是反复失败。

[上一篇：空参数排查](/codescan-05/) · [下一篇：逐次请求账本](/codescan-07/)

<https://www.pa55w0rd.online/codescan-06/>

分享到
[留言](/codescan-06/#comments)

* [CodeScan-Artex](/tags/CodeScan-Artex/)
* [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/)
* [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-06/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（07）：给每次模型请求补上时间与计量账本](/codescan-07/)
[**下一篇 →**

CodeScan 实战（05）：save\_threat\_model 为什么会收到空参数](/codescan-05/)

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
* [2021年09月](/archi...