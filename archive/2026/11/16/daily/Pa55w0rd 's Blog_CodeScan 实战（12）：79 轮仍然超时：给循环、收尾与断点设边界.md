---
title: CodeScan 实战（12）：79 轮仍然超时：给循环、收尾与断点设边界
url: https://www.pa55w0rd.online/codescan-12/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:37.527142
---

# CodeScan 实战（12）：79 轮仍然超时：给循环、收尾与断点设边界

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
4. CodeScan 实战（12）：79 轮仍然超时：给循环、收尾与断点设边界

# CodeScan 实战（12）：79 轮仍然超时：给循环、收尾与断点设边界

[系列目录](/codescan-00/) · 第 12 篇

一次 Worker 运行结束时，页面给出如下信息：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` 终态：timeout 已执行：79 轮 运行耗时：26m44s 输入 token：6,663,707 输出 token：56,830 缓存读取：5,491,703 中断前最后一个工具：TodoWrite ``` |

这不是模型供应商宣布“审计完成”。`timeout` 来自宿主的单次运行预算：到达墙钟上限后中断探索，进入有限收尾，意图按耗尽处理。

## 0x01 时间用完，和工作完成是两回事

一次执行可以先有主要探索，再有正在退出的请求或工具，最后进入收尾。因此页面总耗时可能略大于配置的主预算。

“已写回事实”说明部分持久化操作已经成功，不代表所有工具都有结果，也不代表已形成最终报告。反过来，“无文字总结”也不等于数据库里什么都没保存。

恢复前应该先看 Worker 输出、事实和断点，确认上次到底留下了什么，而不是把整段原始目标原封不动再派一次。

## 0x02 高轮数里面有多少是在空转

这一轮排查发现，相关运行里 `save_finding_audit` 被调用 47 次，全部失败：46 次属于使用范围错误，另一次被中断。还出现同一份事实摘要反复保存的情况。

这类问题不是简单的“模型推理需要更久”。工具本来就不适合承接那份材料，重复调用只会消耗上下文与时间。

例如没有覆盖账本保存权限的 Worker，应该通过 `record_fact` 交接已检查范围、草稿路径和剩余项，由 Planner 合并。用漏洞保存工具承载任意 TODO 或覆盖清单，会持续被契约拒绝。

## 0x03 对重复错误设停止条件

Worker 增加了重复工具错误保护：相同工具、相同参数、相同错误累计达到 3 次，下一次模型请求前停止本轮，保留 `repeated_tool_error` 原因。

这里不能只看“工具失败三次”。修改参数后有意义地重试、随后成功，和原样循环需要区分。把所有失败一律累计，会过早终止正常排查。

同一意图、相同证据内容的事实保存也做幂等处理；不同意图或新增证据仍然保留，不能为了压缩数量把有价值的关联删掉。

## 0x04 收尾不该变成第二轮探索

原先默认收尾最多还有 10 轮，这一轮收紧到 4 轮。明确管理员正数配置继续尊重，不悄悄覆盖。

收尾阶段禁用 `TodoWrite` 以及 `Read`、`Grep`、`Glob`、`LS` 等继续探索的入口，让剩余预算用于保存已经知道的事实、证据和交接信息。

这不表示所有工具都被粗暴打断后立刻丢弃结果，而是给“继续找新东西”和“保存已经找到的东西”划清预算边界。

## 0x05 断点要让下一次知道怎么继续

有用的断点至少回答：

| 内容 | 用途 |
| --- | --- |
| 已用预算、轮数与耗时 | 判断是否需要缩小下一批范围 |
| 有限的 TODO 摘要 | 保存下一步，不复制整段对话 |
| 持久化写入计数 | 核对材料有没有真正落库 |
| 最后工具与错误 | 避免再次撞上同一契约问题 |
| 已保存事实和证据引用 | 让恢复基于实际材料继续 |

恢复沿用意图会话，但必须先读持久化断点。`exhausted` 不是 `completed`；如果阻塞没有修正，就不该用相同输入再跑一轮。

[![Worker达到宿主预算后停止探索，有限收尾并保存证据和断点，意图耗尽后读取断点再恢复；耗尽不是完成。](/assets/codescan/12-budget-checkpoint-v1.webp)](/assets/codescan/12-budget-checkpoint-v1.svg "运行预算耗尽后，先留下可恢复的交接")

图 12｜预算耗尽、有限收尾、断点与后续恢复之间的关系。 [打开 SVG 原图](/assets/codescan/12-budget-checkpoint-v1.svg)

## 0x06 累计输入不能简单当成独立源码体积

多轮调用会反复携带相同上下文，累计输入因此可能达到数百万 token。缓存读取较高，说明其中有可复用部分，但缓存命中仍可能伴随排队、网络和调度成本。

应结合第 07、09 篇的逐次记录，定位哪些调用又长又没有产生持久化进展。只提高 MaxDuration，可能只是让循环持续得更久。

本轮使用模拟 Provider、实际 SDK 和隔离 PostgreSQL 验证重复错误、事实去重及断点流程，没有进行同一真实业务 79 轮的前后成本对照。因此不报告一个未经实测的“节省 token 百分比”。

[上一篇：实时连接恢复](/codescan-11/) · [下一篇：Planner 实际进展](/codescan-13/)

<https://www.pa55w0rd.online/codescan-12/>

分享到
[留言](/codescan-12/#comments)

* [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/)
* [运行预算](/tags/%E8%BF%90%E8%A1%8C%E9%A2%84%E7%AE%97/)
* [长程任务](/tags/%E9%95%BF%E7%A8%8B%E4%BB%BB%E5%8A%A1/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-12/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（13）：模型说已经派发，程序必须看到实际动作](/codescan-13/)
[**下一篇 →**

CodeScan 实战（11）：一直重连，最后查到了端口之外的登录冲突](/codescan-11/)

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

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [CI-CD](/tags/CI-CD/) [ChatGPT](/tags/ChatGPT/) [CodeScan-Artex](/tags/CodeScan-Artex/) [DevSecOps](/tags/DevSecOps/) [Docker](/tags/Docker/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [Mantis](/tags/Mantis/) [PHPstudy](/tags/PHPstudy/) [Planner](/tags/Planner/) [SDL](/tags/SDL/) [SSE](/tags/SSE/) [STRIDE](/tags/STRIDE/) [TRS](/tags/TRS/) [TTFT](/tags/TTFT/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/) [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/) [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/) [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [反证](/tags/%E5%8F%8D%E8%AF%81/) [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/) [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/) [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/) [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/) [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/) [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/) [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/) [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/) [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8/) [漏洞管理](/tags/%E6%BC%8F%E6%B4%9E%E7%AE%A1%E7%90%86/) [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/) [移动安全](/tags/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/) [编程基础](/tags/%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/) [蜜罐](/tags/%E8%9C%9C%E7%BD%90/) [解决方法](/tags/%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/) [记录](/tags/%E8%AE%B0%E5%BD%95/) [证据链](/tags/%E8%AF%81%E6%8D%AE%E9%93%BE/) [资产扫描](/tags/%E8%B5%84%E4%BA%A7%E6%89%AB%E6%8F%8F/) [身份认证](/tags/%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81/) [迁移](/tags/%E8%BF%81%E7%A7%BB/) [运维安全](/tags/%E8%BF%90%E7%BB%B4%E5%AE%89%E5%85%A8/) [运行复盘](/tags/%E8%BF%90%E8%A1%8C%E5%A4%8D%E7%9B%98/) [运行预算](/tags/%E8%BF%90%E8%A1%8C%E9%A2%84%E7%AE%97/) [速查表](/tags/%E9%80%9F%E6%9F%A5%E8%A1%A8/) [长上下文](/tags/%E9%95%BF%E4%B8%8A%...