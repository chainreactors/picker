---
title: CodeScan 实战（03）：补齐审计覆盖、反证和收官门禁
url: https://www.pa55w0rd.online/codescan-03/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:36.212180
---

# CodeScan 实战（03）：补齐审计覆盖、反证和收官门禁

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
4. CodeScan 实战（03）：补齐审计覆盖、反证和收官门禁

# CodeScan 实战（03）：补齐审计覆盖、反证和收官门禁

[系列目录](/codescan-00/) · 第 03 篇

漏洞列表能展示已经发现的问题，却没有说明未出现的部分发生了什么：是审过没有发现，还是根本没有检查？

这一轮我把重点放到覆盖账本和收官条件上。规划者可以继续派发任务，但最后一句“目标已完成”需要有可检查的依据。

## 0x01 外部方法怎么用

当次定向研究了 Cloudflare security-audit-skill、Trail of Bits skills、Anthropic security review、Shannon、Vulnhuntr 和 CyberGym。

它们带来的共同启发是：先理解上下文与约束，明确检查范围，主动寻找反证，并把运行观测和模型判断分开。

我没有把它们的默认规则整体照搬。例如，按文本模式忽略某些资源耗尽问题，可能会漏掉当前系统真正关心的风险。迁移方法前，先看目标项目的业务边界。

## 0x02 先给覆盖建立分母

`audit/coverage.go` 在宿主侧枚举上传源码，生成包含相对路径、长度、类型和摘要的清单。

隐藏配置、CI 文件和实际的构建产物同样可能影响安全。是否排除，需要给出范围依据；不能仅看见 `dist`、`test` 或 `vendor` 目录名就跳过。

文件状态区分：

| 状态 | 用途 |
| --- | --- |
| `pending` | 尚未获得足够检查记录 |
| `reviewed` | 有已完成的语义检查及核验引用支持 |
| `excluded` | 明确排除，并保留原因 |

遗漏的文件仍保持待审。排除项单列，也不会被加进“已审文件数”。

## 0x03 文件覆盖还不够

一个授权函数可能影响读取、删除、恢复和后台补偿等多条路径。读完文件，只能说明拿到了内容；需要检查的安全不变式还没有自动完成。

因此，账本进一步记录：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 真实入口 × 信任边界 × 子系统 × 攻击类别 × 生命周期 ``` |

例如，“租户对象读取”这一项，要说明入口如何确定、身份从哪里来、对象归属在哪里检查、跨文件查询是否保留租户条件，以及哪些未知事实会改变结论。

一项检查可以保持 `planned`、`blocked` 或 `not_applicable`。这些状态都有用途，尤其是在依赖源码或部署条件缺失时。

[![完整源码清单的待审、已核验和排除状态，与入口、边界、子系统、攻击类别、生命周期五维语义覆盖共同进入收官检查。](/assets/codescan/03-coverage-gate-v1.webp)](/assets/codescan/03-coverage-gate-v1.svg "覆盖的分母与收官门禁")

图 03｜文件覆盖与语义覆盖相互补充，由当前材料接受收官检查。 [打开 SVG 原图](/assets/codescan/03-coverage-gate-v1.svg)

## 0x04 证据链要解释每一跳

这轮给 `audit_case.reasoning` 加入逐跳传播说明。相邻两个引用之间，需要解释调用、赋值、参数或权限上下文如何延续。

接着检查可能推翻判断的因素：

* 路由之外是否还有统一鉴权或网关约束？
* 参数转换是否改变了攻击者可控范围？
* ORM、序列化器、拦截器或依赖代码里是否有关键保护？
* 当前假设的角色、资源或租户条件是否真实？

反证没有找到，不代表已经证明不存在。缺少上游源码时，应把问题留在未知项里，并给出下一步核验计划。

同根因变体检查也要记录实际范围和逐项结果，避免把几个相似关键词当成全仓审计。

## 0x05 收官由当前材料决定

最后一个目标准备完成时，程序核对源码清单、模型绑定、覆盖单元、漏洞材料和报告版本。

Agent 可以用 `get_audit_gate` 查看缺口。材料仍允许保存和导出，但未清除的必需缺口会阻止“全部完成”的判定。

`ready_for_review` 表示材料达到交付复核条件。漏洞是否成立、PoC 是否实际执行，以及生产入口是否可达，仍需要对应证据。

## 0x06 给 PoC 一个更具体的判据

普通正文标记有时会被接口原样反射。这轮增加 JSON Pointer 判据，例如：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` {   "oracle": {     "kind": "json_value",     "pointer": "/owner/id",     "equals": "fixture-victim"   } } ``` |

只有指定位置的值满足条件才算命中。解析失败、重复键、截断，以及阴性对照同样命中，都不能升级为有效观测。

即便命中了字段值，还要解释主体和资源关系。判据负责描述观测，漏洞语义由独立复核判断。

## 0x07 这一轮怎么验收

回归关注清单变化、并发版本比较、任务归属、报告过期、归档恢复和最后目标门禁。它们验证工程约束，没有测量真实仓库的检出率或误报率。

源码入口：`audit/coverage.go`、`audit/delivery.go`、`agent/audit_coverage.go`。

[上一篇：三个项目的集成](/codescan-02/) · [下一篇：建模生命周期](/codescan-04/)

<https://www.pa55w0rd.online/codescan-03/>

分享到
[留言](/codescan-03/#comments)

* [CodeScan-Artex](/tags/CodeScan-Artex/)
* [反证](/tags/%E5%8F%8D%E8%AF%81/)
* [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-03/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（04）：把威胁建模接进真正的任务生命周期](/codescan-04/)
[**下一篇 →**

CodeScan 实战（02）：吸收其他项目的优势，统一威胁、漏洞与证据](/codescan-02/)

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

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [CI-CD](/tags/CI-CD/) [ChatGPT](/tags/ChatGPT/) [CodeScan-Artex](/tags/CodeScan-Artex/) [DevSecOps](/tags/DevSecOps/) [Docker](/tags/Docker/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [Mantis](/tags/Mantis/) [PHPstudy](/tags/PHPstudy/) [Planner](/tags/Planner/) [SDL](/tags/SDL/) [SSE](/tags/SSE/) [STRIDE](/tags/STRIDE/) [TRS](/tags/TRS/) [TTFT](/tags/TTFT/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/) [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/) [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/) [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [反证](/tags/%E5%8F%8D%E8%AF%81/) [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/) [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/) [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/) [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/) [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/) [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/) [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/) [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/) [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8/) [漏洞管理](/tags/%E6%BC%8F%E6%B4%9E%E7%AE%A1%E7%90%86/) [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/) [移动安全](/tags/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/) [编程基础](/tags/%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/) [蜜罐](/tags/%E8%9C%9C%E7%BD%90/) [解决方法](/tags/%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/) [记录](/tags/%E8%AE%B0%E5%BD%95/) [证据链](/tags/%E8%AF%81%E6%8D%AE%E9%93%BE/) [资产扫描](/tags/%E8%B5%84%E4%BA%A7%E6%89%AB%E6%8F%8F/) [身份认证](/tags/%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81/) [迁移](/tags/%E8%BF%81%E7%A7%BB/) [运维安全](/tags/%E8%BF%90%E7%BB%B4%E5%AE%89%E5...