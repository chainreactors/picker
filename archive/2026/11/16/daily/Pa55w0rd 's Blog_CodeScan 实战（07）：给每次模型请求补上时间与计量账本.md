---
title: CodeScan 实战（07）：给每次模型请求补上时间与计量账本
url: https://www.pa55w0rd.online/codescan-07/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:36.827523
---

# CodeScan 实战（07）：给每次模型请求补上时间与计量账本

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
4. CodeScan 实战（07）：给每次模型请求补上时间与计量账本

# CodeScan 实战（07）：给每次模型请求补上时间与计量账本

[系列目录](/codescan-00/) · 第 07 篇

总览里只有累计 token，很难解释一次任务为什么跑了半小时。输入多，是重复带了源码，还是命中了缓存？停顿长，是模型生成慢，还是某次调用失败？两个任务同时运行时，时间有没有重叠？

这一轮先建立逐次调用账本，把“任务总共消耗多少”拆成“每次调用发生了什么”。

## 0x01 计量和原文录制分开

完整模型请求、响应会包含大量源码和任务信息。为了查看时间，不应该要求操作者先开启重型原文录制。

因此轻量 `llm_usage` 持续记录计量信息；需要排查协议细节时，再选择开启原文录制。总览读取轻量账本，按任务权限分页返回，接口不附带提示词、响应正文或密钥。

两条记录共用同一次调用的计时边界，避免原文页面和总览各算一套时间。

## 0x02 一条记录至少应该包含什么

| 字段 | 含义 |
| --- | --- |
| 任务与调用身份 | 这次调用属于哪个任务、哪类角色和模型配置 |
| `started_at` | 实际调用开始时间，保留时区 |
| `completed_at` | 调用结束、失败或取消的时间 |
| 总耗时 | 从调用边界测量的经过时间 |
| 输入与输出 token | 按 Provider 返回的可用用量记录 |
| 缓存读取与写入 | 分开保存，避免把缓存命中误读为新增生成 |
| 结果状态 | 成功、失败、中断及可定位的错误信息 |

失败调用也需要记录。若只保存成功请求，页面会把漫长重试“压缩”成一段没有解释的空白。

## 0x03 两种时钟各做一件事

开始和结束时间用于回答“什么时候发生”，使用系统墙钟；耗时用于回答“经过多久”，尽量使用单调时钟。

如果操作系统在调用期间校时，结束时间减开始时间可能与记录耗时有少量差异。保留实际观测值更有价值，不必为了让两列对齐而重写时间戳。

调用结束后再写计量记录，数据库保存耗时不计入模型调用耗时。相应地，这份账本是调用完成后可见的记录，不是正在生成过程中的逐 token 实时仪表盘。

## 0x04 “每次请求”在这里指什么

这里的单位是平台对 Provider 的一次 `Stream` 或 `Complete` 调用。流式调用在迭代消费开始时计时，非流式调用在调用入口计时。

SDK 内部可能执行建连重试。如果这些重试没有重新进入平台 Provider 边界，它们会包含在同一条记录里。这份表不能直接当成每个物理 HTTP 请求的访问日志。

同样，任务页面里的“轮次”和“调用次数”也不必一一对应：规划、工作、压缩和收尾可能分别发生模型调用。应先确认统计单位，再分析平均耗时或失败率。

[![一次Provider调用从实际调用边界计时，包含SDK内部重试与响应消费；轻量计量持续记录，原文录制可选，两者共用计时边界。](/assets/codescan/07-request-accounting-v1.webp)](/assets/codescan/07-request-accounting-v1.svg "一次计量记录，对应一次 Provider 调用")

图 07｜一次 Provider 调用的计时范围与两种记录方式。 [打开 SVG 原图](/assets/codescan/07-request-accounting-v1.svg)

## 0x05 旧记录保持未知

旧版本只存一个时间字段时，不能拿结束时间减耗时，倒推出一个看似精确的开始时间。耗时可能采用不同边界，历史进程也可能有暂停或时间校正。

迁移后，缺失的 `started_at`、`completed_at` 保留为空。前端显示“未知”或破折号，不补成当前时间，也不写成零。

这看起来不如一张填满的表整齐，却能让后续排查知道哪些是实际采集，哪些数据从来没有。

## 0x06 这一轮如何验收

验证覆盖流式、非流式、失败和取消，检查时间字段迁移、分页、任务读权限以及原文录制与轻量账本的一致性；前端完成类型检查和生产静态导出。记录中还核对了历史部署中的实际计时调用。

验收只说明该版本把这些调用记录下来了，没有测出模型吞吐上限，也没有得到一组可推广的 P50 或 P95。TTFT 和分段速率需要额外观测事件，不能只用总耗时估算全部阶段。

第 09 篇继续说明新增性能指标到底测到了哪一段，以及为什么“Prefill tok/s”必须标成客户端估算。

[上一篇：目标拆解恢复](/codescan-06/) · [下一篇：任务类型与长上下文](/codescan-08/)

<https://www.pa55w0rd.online/codescan-07/>

分享到
[留言](/codescan-07/#comments)

* [CodeScan-Artex](/tags/CodeScan-Artex/)
* [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/)
* [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-07/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（08）：拆开任务类型，收窄长上下文工作单元](/codescan-08/)
[**下一篇 →**

CodeScan 实战（06）：模型恢复了，目标拆解也要继续](/codescan-06/)

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
* [2023年08月](/a...