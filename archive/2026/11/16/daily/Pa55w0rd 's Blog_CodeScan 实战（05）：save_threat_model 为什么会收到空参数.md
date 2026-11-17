---
title: CodeScan 实战（05）：save_threat_model 为什么会收到空参数
url: https://www.pa55w0rd.online/codescan-05/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:36.509743
---

# CodeScan 实战（05）：save_threat_model 为什么会收到空参数

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
4. CodeScan 实战（05）：save\_threat\_model 为什么会收到空参数

# CodeScan 实战（05）：save\_threat\_model 为什么会收到空参数

[系列目录](/codescan-00/) · 第 05 篇

有一类错误很容易误判成“模型不会调用工具”：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` save_threat_model {} Error: invalid tool input: input: missing required property "expected_revision" ``` |

这个回执能确认的是：工具校验层收到的参数没有必填版本号。仅凭它，还不能确定参数在哪一层丢失，也不能确定所有类似错误具有同一个根因。

## 0x01 一次保存经过了哪些环节

保存威胁模型并不是把一段模型文字直接写入数据库。实际链路至少包含：

[![从工具定义、模型响应、流式组装到输入校验、业务核验和事务保存；空对象缺少expected_revision时在输入校验层拒绝。](/assets/codescan/05-tool-input-chain-v1.webp)](/assets/codescan/05-tool-input-chain-v1.svg "空参数报错：先定位失败发生在哪一层")

图 05｜工具参数经过的处理链路，以及空对象被拒绝的位置。 [打开 SVG 原图](/assets/codescan/05-tool-input-chain-v1.svg)

报错发生在哪一层，决定了该查哪里。缺少 `expected_revision` 属于输入契约错误；证据引用不存在，属于业务校验错误；`connect: connection refused` 则是在连接模型服务时就失败。这三类故障不应该都显示成一个笼统的“模型错误”。

## 0x02 为什么不能删掉 expected\_revision

这个字段负责并发版本比较。假设 Planner 读到模型版本 7，操作员随后补了一条信任边界，数据库已到版本 8。Planner 再提交基于版本 7 的整份模型，直接覆盖会把人工修改抹掉。

正确行为是拒绝旧版本提交，重新读取上下文后再合并。把必填字段去掉，或者由宿主一律补成当前版本，会掩盖冲突，让一次看似成功的保存变成数据丢失。

调用前应先读取 `get_audit_context`，使用其实际版本。支持文件提交的版本，可以在任务目录写好完整模型，再提交以下结构的参数：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` {   "expected_revision": <刚读取的真实版本号>,   "model_path": "<任务目录内的模型 JSON 相对路径>" } ``` |

这里是参数结构说明，尖括号需要替换。具体字段仍以当前部署实例暴露的工具 schema 为准，不能把旧版本样例直接当成接口规范。

## 0x03 修了什么

当时排查发现，大参数保存还会受到流式参数组装和回执体积的影响。围绕这条链路做了几件事：

| 位置 | 改造 |
| --- | --- |
| 参数接收 | 累积参数分片，处理文本、用量事件与参数事件交错 |
| 解码失败 | 保留参数长度、摘要和截断诊断，拒绝执行保存 |
| 工具定义 | 保留 required、数组结构和版本比较约束 |
| 大模型提交 | 支持任务目录内的 `model_path`，限制路径边界与 4 MiB 大小 |
| 业务校验 | 把缺失引用、非法状态定位到具体字段 |
| 工具返回 | 返回版本、摘要及有限缺口，避免整份模型再次灌回上下文 |

小回执解决的是下一轮上下文膨胀，文件提交解决的是超长参数传输。两者都不能替代模型结构和证据校验。

当次历史快照统计过 43 次保存调用，其中 27 次是空对象。这是排查时点的统计，不是永久累计值，也不能据此把每一次空对象都归因于截断。

## 0x04 后续复查没有支持“已经彻底解决”

复查时，仍观察到字面两字节 `{}` 到达工具层，并在执行保存前被 schema 拦下。说明早期补丁覆盖了可复现的组装问题，但没有消灭所有空参数来源。

要继续定位，需要关联同一请求的工具定义、原始请求、原始响应、分片事件和最终解码参数。当时缺少能够一一对应的完整原始报文，因此不能断言是模型直接生成了空对象、协议转换丢了内容，还是后续累积过程出错。

并发运行两个任务也只提供了排查线索，不能单凭时间相关性认定“并发把参数串了”。

## 0x05 这一轮留下的工程规则

保存失败必须保留失败，不伪造成功回执；版本冲突必须重读，不静默覆盖；日志可以帮助定位参数状态，但不应默认复制整份源码、模型正文或凭据。

本轮验收覆盖了针对性的 Go 测试、工具 schema、流式分片和大模型保存路径。它证明这些受控输入按预期处理，没有证明所有供应商、模型模板和代理转换路径都正常。

工具注册与参数解码实现，以及后续空参数排查记录。遇到同类错误，先保存请求关联标识和发生层次，再决定重试或修复哪一段链路。

[上一篇：任务生命周期](/codescan-04/) · [下一篇：目标拆解恢复](/codescan-06/)

<https://www.pa55w0rd.online/codescan-05/>

分享到
[留言](/codescan-05/#comments)

* [CodeScan-Artex](/tags/CodeScan-Artex/)
* [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/)
* [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-05/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（06）：模型恢复了，目标拆解也要继续](/codescan-06/)
[**下一篇 →**

CodeScan 实战（04）：把威胁建模接进真正的任务生命周期](/codescan-04/)

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

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [CI-CD](/tags/CI-CD/) [ChatGPT](/tags/ChatGPT/) [CodeScan-Artex](/tags/CodeScan-Artex/) [DevSecOps](/tags/DevSecOps/) [Docker](/tags/Docker/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [Mantis](/tags/Mantis/) [PHPstudy](/tags/PHPstudy/) [Planner](/tags/Planner/) [SDL](/tags/SDL/) [SSE](/tags/SSE/) [STRIDE](/tags/STRIDE/) [TRS](/tags/TRS/) [TTFT](/tags/TTFT/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/) [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/) [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/) [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [反证](/tags/%E5%8F%8D%E8%AF%81/) [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/) [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/) [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/) [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/) [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/) [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/) [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/) [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/) [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8/) [漏洞管理](/tags/%E6%BC%8F%E6%B4%9E%E7%AE%A1%E7%90%86/) [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/) [移动安全](/tags/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/) [编程基础](/tags/%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/) [蜜罐](/tags/%E8%9C%9C%E7%BD%90/) [解决方法](/tags/%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/) [记录](/tags/%E8%AE%B0%E5%BD%95/) [证据链](/tags/%E8%AF%81%E6%8D%AE%E9%93%BE/) [资产扫描](/tags/%E8%B5%84%E4%BA%A7%E6%89%AB%E6%8F%8F/) [身份认证](/tags/%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81/) [迁移](/tags/%E8%BF%81%E7%A7%BB/) [运维安全](/tags/%E8%BF%90%E7%BB%B4%E5%AE%89%E5%85%A8/) [运行复盘](/tags/%E8%BF%90%E8%A1%8C%E5%A4%8D%E7%9B%98/) [运行预算](/tags/%E8%BF%90%E8%A1%8C...