---
title: CodeScan 实战（14）：四个真实任务复盘：预算、失败保护与增量保存
url: https://www.pa55w0rd.online/codescan-14/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:37.833182
---

# CodeScan 实战（14）：四个真实任务复盘：预算、失败保护与增量保存

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

约 1.4k 字
约 4 分钟读完

2026-11-17

1. [首页](/)
2. [开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)
3. [CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)
4. CodeScan 实战（14）：四个真实任务复盘：预算、失败保护与增量保存

# CodeScan 实战（14）：四个真实任务复盘：预算、失败保护与增量保存

[系列目录](/codescan-00/) · 第 14 篇

单独修一个错误后，很难知道系统整体是否更可靠。这一轮把两个被审系统各自的两个任务放在一起复盘，分别核对轮次、工具轨迹、覆盖账本、漏洞材料和最终状态。本文将目标匿名为系统 A、系统 B。

最醒目的发现是：某一轮 Planner 持续约 20 小时，调用 `Write` 4164 次，对未开放的 `Bash` 产生 1143 次错误。问题已经超出“模型偶尔回答不好”的范围。

## 0x01 四个任务暴露的是不同故障

| 观察 | 问题 |
| --- | --- |
| 规划轮次长时间不退出 | Planner 自身缺少有效墙钟与默认轮数边界 |
| 不断尝试 Bash 或写生成脚本 | 把静态写文件与实际执行能力混淆 |
| 覆盖从大量已分类条目退回 pending | 局部更新采用整份替换，旧材料丢失 |
| 本地报告已写，平台仍提示过期 | 文件输出与证据版本绑定不是同一件事 |
| 每次调用重试失败，下一心跳继续 | 缺少任务级连续模型故障保护 |

这些现象可能同时出现。不能把所有失败都归咎模型，也不能因为已有漏洞条目，就把尚未覆盖的源码和未知条件标成完成。

## 0x02 给 Planner 自己设预算

此前 Worker 已有运行限制，但 Planner 的 `max_turns=0` 缺少默认边界，管理配置中的 `run_seconds` 也未真正约束其主探索。

这轮将 Planner 主探索上限设为 5 分钟，更小配置与任务剩余时限优先；未设轮数时默认 24 轮，默认收尾 2 轮，管理员显式正数轮数继续尊重。请求退出尾部与收尾仍可能让最终耗时略超主探索预算。

错误止损也区别于 Worker：Planner 同一工具的同类错误累计 3 次，或单轮工具错误合计达到 8 次时停止本轮。即使更换 Bash 参数，未知工具仍是同类问题，不能通过改几个字符绕过保护。

## 0x03 调用重试之外，还要有任务级保护

当时最小模型探针返回 `503 backend_unavailable`。这能确认所选后端没有接受该次请求，不能靠重试保存漏洞或读取源码解决。

连续 3 轮规划因模型或 API 故障结束后，任务以 `planner_model_unavailable` 停止，并明确可恢复。连续计数依据持久化结果，进程重启不重新赠送一轮无限重试；正常结果会打断连续失败。

用户暂停、工具契约错误不混算为供应商故障。任务停止时保留已有材料与可恢复工作，服务恢复后由操作员决定继续，避免修复部署顺手把所有旧任务重新启动。

## 0x04 局部更新不再要求重传整份账本

数千文件的覆盖账本，只改一条记录也要求模型重写全量，既昂贵又容易遗漏。旧接口对未提供文件补 pending，整份替换还会抹掉原语义单元和证据。

新增 `ledger_patch` 和文件方式的增量提交，按文件路径、证据 ID、语义维度合并，未修改内容保留。宿主掌握完整源码分母，遗漏文件仍如实保持待审，不要求模型手写数千个占位条目。

漏洞材料对应增加 `case_patch`：嵌套对象递归合并，未提供字段保留；数组只有显式提供才整组替换。操作员和模型都需要理解这一点，提交一个元素的数组，不等于自动追加。

CAS、归属、源码绑定、引用检查继续执行。整份替换如果撤销已有分类或移除材料，需要说明 `replace_reason`，不能静默把旧证据清掉。

## 0x05 写了报告文件，为什么门禁仍不通过

因为平台需要的是“这份报告对应当前哪一版证据”。本地写 `final-report.md`，或者推进审计记录 revision，并不会自动更新漏洞报告的 `report_evidence_version`。

证据新增、PoC 变化或独立复核更新后，报告需要重新生成并绑定当前证据版本。修复后的缺口提示应把实际证据版本和报告版本写清楚，让模型知道要更新哪份交付物。

同理，文件总数归零待审，也不代表语义覆盖已经闭合。接口、权限、边界和生命周期仍需自己的证据。

[![规划时间轮数预算、工具错误止损、连续模型故障保护及增量保存分别约束四类问题，报告必须对应当前证据版本。](/assets/codescan/14-runtime-safeguards-v1.webp)](/assets/codescan/14-runtime-safeguards-v1.svg "四类运行问题，对应四组保护")

图 14｜运行保护、增量材料与报告版本各自解决不同问题。 [打开 SVG 原图](/assets/codescan/14-runtime-safeguards-v1.svg)

## 0x06 本轮验收没有替真实长程复测背书

针对性回归记录为 102 项通过、0 失败；Windows 未执行的两项符号链接检查在 Linux 补测。测试使用真实 SDK、隔离数据库与模拟 Provider，覆盖预算、错误保护、补丁合并和报告检查。

真实模型探针仍返回 503，因此没有进行修复后四个真实任务的完整长程对照。已有数据库备份也只做了格式和摘要检查，没有完成全量恢复演练。

[上一篇：Planner 无实际动作](/codescan-13/) · [下一篇：Mantis 借鉴](/codescan-15/)

<https://www.pa55w0rd.online/codescan-14/>

分享到
[留言](/codescan-14/#comments)

* [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/)
* [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/)
* [运行复盘](/tags/%E8%BF%90%E8%A1%8C%E5%A4%8D%E7%9B%98/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-14/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（15）：借鉴 Mantis：版本化批次、累计预算和导航](/codescan-15/)
[**下一篇 →**

CodeScan 实战（13）：模型说已经派发，程序必须看到实际动作](/codescan-13/)

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

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [CI-CD](/tags/CI-CD/) [ChatGPT](/tags/ChatGPT/) [CodeScan-Artex](/tags/CodeScan-Artex/) [DevSecOps](/tags/DevSecOps/) [Docker](/tags/Docker/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [Mantis](/tags/Mantis/) [PHPstudy](/tags/PHPstudy/) [Planner](/tags/Planner/) [SDL](/tags/SDL/) [SSE](/tags/SSE/) [STRIDE](/tags/STRIDE/) [TRS](/tags/TRS/) [TTFT](/tags/TTFT/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/) [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/) [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/) [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [反证](/tags/%E5%8F%8D%E8%AF%81/) [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/) [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/) [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/) [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/) [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/) [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/) [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/) [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/) [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8/) [漏洞管理](/tags/%E6%BC%8F%E6%B4%9E%E7%AE%A1%E7%90%86/) [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/) [移动安全](/tags/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/) [编程基础](/tags/%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/) [蜜罐](/tags/%E8%9C%9C%E7%BD%90/) [解决方法](/tags/%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/) [记录](/tags/%E8%AE%B0%E5%BD%95/) [证据链](/tags/%E8%AF%81%E6%8D%AE%E9%93%BE/) [资产扫描](/tags/%E8%B5%84%E4%BA%A7%E6%89%AB%E6%8F%8F/) [身份认证](/tags/%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81/) [迁移](/tags/%E8%BF%81%E7%A7%BB/) [运维安全](/tags/%E8%BF%90%E7%BB%B4%E5%AE%89%E5%85%A8/) [运行复盘...