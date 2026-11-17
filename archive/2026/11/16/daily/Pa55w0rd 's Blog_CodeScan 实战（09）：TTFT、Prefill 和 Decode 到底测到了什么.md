---
title: CodeScan 实战（09）：TTFT、Prefill 和 Decode 到底测到了什么
url: https://www.pa55w0rd.online/codescan-09/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:37.118970
---

# CodeScan 实战（09）：TTFT、Prefill 和 Decode 到底测到了什么

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
4. CodeScan 实战（09）：TTFT、Prefill 和 Decode 到底测到了什么

# CodeScan 实战（09）：TTFT、Prefill 和 Decode 到底测到了什么

[系列目录](/codescan-00/) · 第 09 篇

补上时间戳后，用户进一步要求查看 TTFT、Prefill tok/s、Decode tok/s 和总耗时。这些字段能帮助发现排队和生成瓶颈，但名字相同，不代表测量口径相同。

本项目能直接观测的是客户端收到事件的时间。服务端 GPU 何时开始计算、队列等待多久，需要模型服务另行提供数据。

## 0x01 首个事件不一定是首个输出

流式连接可能先收到角色声明、空 delta、用量、心跳或签名。把这些事件算作首 token，会得到一个很好看、却没有回答用户等待时间的数值。

`llmrec/performance.go` 只把以下内容当作有效输出：

* 非空正文片段。
* 非空推理片段。
* 非空工具调用名称。
* 非空工具参数 JSON 片段。

因此这里的 TTFT 更准确地说，是“到首个有效输出事件的时间”。一个事件可能包含多个 token，并不等于客户端看见了引擎生成的第一个 token。

## 0x02 当前计算公式

设请求开始为 `t0`，首个有效输出到达为 `t1`，调用结束为 `t2`：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` TTFT              = t1 - t0 Decode 区间        = t2 - t1 总耗时             = t2 - t0  Prefill tok/s 估算 = (输入 token - 缓存读取 token) / TTFT秒 Decode tok/s 估算  = (输出 token - 1) / Decode区间秒 ``` |

输入 token 在 SDK 中已归一化为包含缓存读取子集，因此估算预填充时减去缓存读取；缓存写入仍需要处理输入，不能一起减掉。

Decode 分子减去首个输出 token，但分母仍包含网络、缓冲、消费者延迟和流结束尾部。这个比值用于客户端侧比较，不等同于引擎内部逐 token 解码速度。

[![请求开始到首个有效输出为TTFT，之后到调用结束为Decode区间；Prefill和Decode速率按客户端可观测时间及完整用量估算。](/assets/codescan/09-client-timing-v1.webp)](/assets/codescan/09-client-timing-v1.svg "TTFT 与吞吐：客户端究竟观测到什么")

图 09｜客户端时序与计算口径，图中未绘制任何实测吞吐数据。 [打开 SVG 原图](/assets/codescan/09-client-timing-v1.svg)

## 0x03 为什么 Prefill 必须写“估算”

假设输入 10000 token，其中缓存读取 6000 token，TTFT 为 4 秒，那么按当前口径，Prefill 估算为：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` (10000 - 6000) / 4 = 1000 tok/s ``` |

但这 4 秒可能含有排队、网络传输和服务端调度。没有队列时长与引擎时序，无法从中分离纯预填充计算耗时。

两个任务争用单并发模型服务时，后到请求即使预填充很快，客户端也可能看到很长 TTFT。这应作为排队线索，不能直接归因于 GPU 算得慢。

若要定位服务端瓶颈，应把请求关联到模型服务日志、队列指标和 GPU 指标，再分析具体阶段。

## 0x04 哪些情况下不计算速率

只有一块输出一次性交付时，客户端无法观察生成节奏，不给 Decode 速率。输出 token 不足、区间为零或用量不合法时，同样保留未知。

调用失败或被截断，返回的 usage 可能只是一部分。这时如果已经看到首个有效输出，可以保留 TTFT，但不把不完整用量换算为吞吐。

非流式调用只能确定调用开始与结束，不能伪造中间的首输出时间。历史记录未采集的字段也保持空值，页面用破折号提示，不填 0 tok/s。

这些规则会让表里出现空白。空白表示测不到，不是系统确认了“性能为零”。

## 0x05 页面怎么帮助排查

请求明细同时显示时间、模型、角色、输入输出、缓存、TTFT、分段速率与总耗时；移动端允许表格横向滚动，不把所有列压缩成难以辨认的数字。

实际查看时，先看失败和超长请求，再看 TTFT 与输出区间的占比。若多数时间都在 TTFT，优先核对排队、长输入和连接；若输出区间很长，结合输出量和预算分析。

不能拿几条调用就宣布 P95，也不能跨模型、上下文长度和缓存状态直接比较一个 tok/s 数字。

## 0x06 验收与维护复盘

本轮针对空事件、工具输出、缓存、单块输出、失败用量等情况进行了后端回归，并检查前端类型、静态导出和 Mock 页面；390 像素宽度下核验过表格布局。

历史部署时还有一个运维教训：当次恢复 Docker 环境曾影响同机原实例。后续不能把“端口不同”写成“共享运行时完全隔离”，也不能为了更新本项目顺手重启整个 Docker Desktop。

性能表提供排查依据，不替代模型服务压测与生产容量评估。

[上一篇：任务类型与上下文](/codescan-08/) · [下一篇：完整审计模式](/codescan-10/)

<https://www.pa55w0rd.online/codescan-09/>

分享到
[留言](/codescan-09/#comments)

* [TTFT](/tags/TTFT/)
* [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/)
* [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-09/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（10）：从二选一，走到同一任务内的完整审计](/codescan-10/)
[**下一篇 →**

CodeScan 实战（08）：拆开任务类型，收窄长上下文工作单元](/codescan-08/)

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

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [CI-CD](/tags/CI-CD/) [ChatGPT](/tags/ChatGPT/) [CodeScan-Artex](/tags/CodeScan-Artex/) [DevSecOps](/tags/DevSecOps/) [Docker](/tags/Docker/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [Mantis](/tags/Mantis/) [PHPstudy](/tags/PHPstudy/) [Planner](/tags/Planner/) [SDL](/tags/SDL/) [SSE](/tags/SSE/) [STRIDE](/tags/STRIDE/) [TRS](/tags/TRS/) [TTFT](/tags/TTFT/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/) [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/) [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/) [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [反证](/tags/%E5%8F%8D%E8%AF%81/) [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/) [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/) [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/) [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/) [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/) [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/) [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/) [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/) [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8/) [漏洞管理](/tags/%E6%BC%8F%E6%B4%9E%E7%AE%A1%E7%90%86/) [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/) [移动安全](/tags/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/) [编程基础](/tags/%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/) [蜜罐](/tags/%E8%9C%9C%E7%BD%90/) [解决方法](/tags/%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/) [记录](/tags/%E8%AE%B0%E5%BD%95/) [证据链](/tags/%E8%AF%81%E6%8D%AE%E9%93%BE/) [资产扫描](/tags/%E8%B5%84%E4%BA%A7%E6%89%AB%E6%8F%8F/) [身份认证](/tags/%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81/) [迁移](/tags/%E8%BF%81%E7%A7%BB/) [运维安全](/tags/%E8%BF%90%E7%BB%B4%E5%AE%89%E5%85%A8/) [运行复盘](/tags/%E8%B...