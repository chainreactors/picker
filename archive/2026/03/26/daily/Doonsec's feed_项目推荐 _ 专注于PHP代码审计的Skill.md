---
title: 项目推荐 | 专注于PHP代码审计的Skill
url: https://mp.weixin.qq.com/s/qlfnc0gRUBXCHGozQcsF4Q
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:29:22.088543
---

# 项目推荐 | 专注于PHP代码审计的Skill

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVk0Gx7iblLLbfu0Hzlhsp6HpHDFETSYjpm8rJgEicdn2axGwl5HiaSLp9Yxkvc3a3CBlibHFDMF9lV6kIibowWbYgXwrEicm8Yop9LgU/0?wx_fmt=jpeg)

# 项目推荐 | 专注于PHP代码审计的Skill

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 564，阅读大约需 3 分钟

## 前言

项目地址：https://github.com/0xShe/PHP-Code-Audit-Skill

PHP-Code-Audit-Skill 是一套面向 PHP Web 的白盒代码安全审计 Skill 集合，覆盖「路由枚举 → 鉴权建模 → 数据流追踪 → 分类漏洞审计 → 证据一致性校验 → 报告汇总」全流程；在 Cursor 等环境中以 Agent 按 SKILL 文档执行 的方式落地。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlQmQia7qcOiaI9H4I0jzAXCCVSvhpRSoVibzyIDMmups4m5e2WYtsC25n4fmfxnIkf5KEdqcic8zEQdzgIJyRHZPAHrWTeibjZQ4J0/640?wx_fmt=png&from=appmsg)

## 能力

### 路由建模与追踪

* • `php-route-mapper`：提取**所有**路由与完整请求参数结构，并生成可用于测试的请求模板。
* • `php-route-tracer`：基于路由与参数输入，输出从 handler 到最终 sink 的 **数据流链、分支执行证据、可控性矩阵**（不做漏洞结论）。

### 漏洞审计

每类漏洞审计遵循证据契约：须逐项引用 `php-route-tracer` 的 `## 9) Sink Evidence Type Checklist` 中对应行的证据点 ID（无 trace 时的静态对齐方式见 `shared/EVIDENCE_POINT_IDS.md` 文首说明）。

* • SQL 注入：`php-sql-audit`
* • NoSQL 注入：`php-nosql-audit`
* • 命令注入：`php-cmd-audit`
* • SSRF：`php-ssrf-audit`
* • XSS：`php-xss-audit`
* • 任意文件读取/路径穿越（含 include/require 执行面边界）：`php-file-read-audit`
* • 文件上传：`php-file-upload-audit`
* • 任意文件写入（路径穿越到落点/写入链）：`php-file-write-audit`
* • 归档解压路径穿越（Zip Slip）：`php-archive-extract-audit`
* • XXE：`php-xxe-audit`
* • 反序列化/对象注入：`php-deser-audit`
* • 模板注入/SSTI：`php-tpl-audit`
* • LDAP 注入：`php-ldap-audit`
* • 表达式注入（非模板）：`php-expr-audit`
* • 认证/鉴权绕过/越权/IDOR：`php-auth-audit`
* • CSRF：`php-csrf-audit`
* • 开放重定向：`php-open-redirect-audit`
* • CRLF/响应分割：`php-crlf-audit`
* • 会话与 Cookie 安全：`php-session-cookie-audit`
* • 安全配置（危险开关/CORS/错误暴露/安全头）：`php-config-audit`
* • 加密与密钥安全：`php-crypto-audit`
* • 业务逻辑漏洞：`php-logic-audit`
* • 安全日志与监控：`php-logging-audit`

### 非 trace-gate 的增强能力

* • `php-filesystem-audit`：审计文件系统操作（权限/链接/删除/TOCTOU 等），用于提升链式利用可行性（不替代 FILE/UPLOAD/WRITE 等 sink 审计）。

### 链路聚合

* • `php-exploit-chain-audit`：把已产出的漏洞报告按前置条件串成跨漏洞利用链叙事，并输出「未能串联原因清单」。

### 供应链与框架检测

* • `php-vuln-scanner`：基于 `composer.json` / `composer.lock`（及可选规则集）做依赖版本与已知漏洞匹配；可与环境中的 `composer audit` 交叉比对（见该 SKILL 内说明）。
* • `php-*-audit`（框架专项）：Laravel / Symfony / Yii / ThinkPHP / WordPress / CodeIgniter 等典型配置与用法风险映射。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过