---
title: axios npm 供应链投毒攻击事件分析
url: https://mp.weixin.qq.com/s/NcNY65bmzLy3K9yfb6NzAQ
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:24:07.990281
---

# axios npm 供应链投毒攻击事件分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/APc6NwjLsxTicxQvZQb3bhjiaE9yjQd5oXe7LRAhjX6o8IwB3h79V7KCf73rTeicG0EDxPJr9zM3PsE9OrsLY0Aicx6vkY98wYh3faH3ILospAo/0?wx_fmt=jpeg)

# axios npm 供应链投毒攻击事件分析

深瞻情报实验室
深瞻情报实验室

深信服千里目安全技术中心

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxQsnWQicmn8KEJDsTbGLTIqAkGxXk3SybicoXM4mmpBM0WspBZGwhOASkicx2TuMg05BLBPSSZFfcLW18WxPC7LxO1apsnicToxByY/640?wx_fmt=gif&from=appmsg)

**事件概述**

**2026年3月31日，全球最广泛使用的 JavaScript HTTP 客户端库 axios（周下载量逾3亿次）遭遇严重供应链投毒攻击。攻击者通过劫持核心维护者 npm 账号，绕过官方 GitHub Actions CI/CD 发布流程，手动发布了两个恶意版本（axios@1.14.1 与 axios@0.30.4），同时覆盖 1.x 与 0.x 两大版本分支。恶意版本以幻影依赖（phantom dependency） plain-crypto-js@4.2.1 为载体，在用户执行 npm install 时通过 postinstall 钩子自动投放跨平台远程访问木马（RAT），目标覆盖 Windows / macOS / Linux 三大平台，并具备自清除反取证机制。恶意版本存活约 2–4 小时后被 npm 官方下架。**

**事件基础信息**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxRURcZaA3pE6CJicP617Gfh164f9QrHq9tXPRN5giaAwLoia0FhyqxCyOR7ibCZZzyrYZIchd1Jhr9Wuq1rxticbAicYMT52v6ulBsv8/640?wx_fmt=gif&from=appmsg)

**攻击时间线（UTC，精确到分钟）**

|  |  |
| --- | --- |
| **UTC 时间** | **事件** |
| 2026-03-30 05:57 | plain-crypto-js@4.2.0 发布（干净版本，用于预埋身份伪装） |
| 2026-03-30 23:59 | plain-crypto-js@4.2.1 发布（恶意版本，含 postinstall dropper） |
| 2026-03-31 00:21 | axios@1.14.1 通过被劫持账号 jasonsaayman 手动发布（恶意） |
| 2026-03-31 01:00 | axios@0.30.4 发布（恶意，间隔 39 分钟，覆盖 0.x 分支） |
| 2026-03-31 ~03:00 | 社区用户发现异常，GitHub Issue #10604 创建并传播 |
| 2026-03-31 03:01:59 | 协作者DigitalBrainJS 在 GitHub 置顶警告 Issue |
| 2026-03-31 03:15 | npm 官方下架 axios@1.14.1 与 axios@0.30.4 |
| 2026-03-31 03:25 | npm 对 plain-crypto-js 启动安全封禁（security hold） |
| 2026-03-31 04:26 | npm 发布安全占位版本 plain-crypto-js@0.0.1-security.0 |

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxQdpm6Lepp414zbHddcWmOibRKichicKa3Ekt33ombGv4KT05wlicj2qMOO3UicO0nfVGXnyVBpsO9xtXhnia2Xe9haDkBH3s0KlBibC4/640?wx_fmt=gif&from=appmsg)

**影响版本与受害范围**

**恶意版本（立即停止使用）**

|  |  |  |
| --- | --- | --- |
| **包名** | **恶意版本** | **SHA1（npm tarball）** |
| axios | 1.14.1 | 2553649f2322049666871cea80a5d0d6adc700ca |
| axios | 0.30.4 | d6f3f62fd3b9f5432f5782b62d8cfd5247d5ee71 |
| plain-crypto-js | 4.2.1 | 07d889e2dadce6f3910dcbc253317d28ca61c766 |

**安全版本（立即回退至此）**

· axios@1.14.0 — 1.x 分支最后安全版本

· axios@0.30.3 — 0.x 分支最后安全版本

**受害规模估算**

· axios 周下载量：> 3 亿次（npm 官方数据）

· 直接依赖 axios 的 npm 包：> 320 万个

· 恶意版本暴露窗口：约 2–4 小时（00:21 UTC – 03:15 UTC）

· 同时攻击 1.x 和 0.x，覆盖绝大多数使用中的版本线

· 受 CI/CD 自动拉取影响的流水线：无法精确估算，建议全面审查

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxTbbRicMGUHibiaXNP5utQ6v44T5E3oibHwlrqNq0icqSmFicnU6FZrMb4JB7He5qA25AMWY2kTbuGW4MaWkxvOb9icyX8vLO93RfZDes/640?wx_fmt=gif&from=appmsg)

**信源交叉验证结论**

|  |  |  |  |
| --- | --- | --- | --- |
| **级别** | **信源** | **URL** | **核心贡献** |
| 一级 | GitHub 官方 Issue #10604 | github.com/axios/axios/issues/10604 | 维护者声明、第一手时间戳 |
| 二级 | StepSecurity 分析报告 | stepsecurity.io/blog/axios-compromised-... | 完整技术分析、IoC、平台行为 |
| 二级 | Aikido Security | aikido.dev | 攻击手法独立确认 |
| 二级 | Socket.dev | socket.dev | 依赖注入方式分析 |
| 二级 | ITNews.com.au | itnews.com.au | 攻击范围与影响确认 |

验证结论：5 个独立信源对攻击时间、恶意版本号、C2 基础设施、三平台行为描述完全一致，信息可信度：高。

**技术分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxTK6WBdHda8Jg56wzltJKZaK6L0W67deEcicDXuFTa3GEESx1GXftj31WnFh6hsUmgp6yrb2XPFxPbotCUENia8IbiaXicWaHImWYs/640?wx_fmt=gif&from=appmsg)

**CVE / GHSA 编号**

截至报告发布时（2026-03-31），官方尚未分配独立 CVE 或 GHSA 编号。事件发生不足 24 小时，预计由 GitHub Security Advisory 或 MITRE 后续分配。

注：2026年2月存在独立漏洞 CVE-2026-25639 / GHSA-43fc-jf86-j433（axios mergeConfig DoS，影响 ≤1.13.4 / ≤0.30.2，已在 1.13.5/0.30.3 修复），与本次供应链攻击事件无关，请勿混淆。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxRGAgDT8LbdrtZbJEnsaJnSIdBeQ9cr9hclzrJV6tGkAd9Libay4ebyM3msPvq2WJNyE8CMibm8q12lCCjYXjxbFYNXkUS6xicqTE/640?wx_fmt=gif&from=appmsg)

**CVSS v3.1 评分**

|  |  |  |
| --- | --- | --- |
| **向量维度** | **取值** | **说明** |
| 攻击向量(AV) | N – 网络 | 通过npm install 远程触发，无需物理访问 |
| 攻击复杂度(AC) | L – 低 | 常规安装行为即触发，无需特殊条件 |
| 权限要求(PR) | N – 无 | 任何执行npm install 的用户均受影响 |
| 用户交互(UI) | N – 无 | postinstall 自动执行，无需用户确认 |
| 影响范围(S) | U – 不变 | 影响限于安装该包的系统 |
| 机密性影响(C) | H – 高 | RAT 可窃取系统所有凭据与文件 |
| 完整性影响(I) | H – 高 | RAT 可完全控制受感染系统 |
| 可用性影响(A) | H – 高 | RAT 可破坏系统可用性 |

**综合评分：9.8 (Critical)向量**：CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxSzmd5e9NibIVDSwM7KXia7M2uhm42Oj2WSfttRzLkmIeB6qBShFQnsaStchstb40FOqgHOt5QvhTaVu4cUguEnSMvuuwlO4eNoY/640?wx_fmt=gif&from=appmsg)

**官方维护者声明**

**来源：GitHub Issue #10604（2026-03-31 03:01:59 UTC），协作者 DigitalBrainJS：**

"The compromised account (jasonsaayman) has higher git permissions than

other team members. Whatever I fix, he will fix it after me.

We need npm to revoke his tokens immediately."

· 被劫持账号：jasonsaayman（axios 核心维护者）

· 劫持后账号关联邮箱被修改为：ifstap@proton.me

· 攻击者另创建账号：nrwise（nrwise@proton.me）协助操作

· 协作者因权限不足无法独立修复，依赖 npm 官方撤销 token

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxTPwAPuhhYImoLEfpGfZs4eaPyiasCkGXOhPGDpxlwqJnylhqLUMXtHKnviaZvgDOzp80abibgE0U3OSvib7NxqzOJKXAyMx7nt4H4/640?wx_fmt=gif&from=appmsg)

**npm 官方处置声明**

· 2026-03-31 03:15 UTC：npm 下架 axios@1.14.1 与 axios@0.30.4

· 2026-03-31 03:25 UTC：对 plain-crypto-js 启动 security hold

· 2026-03-31 04:26 UTC：发布占位版本 plain-crypto-js@0.0.1-security.0，阻止重新上传

· npm 已撤销被劫持账号的发布 token，GitHub 仓库访问权限修复中

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxTxxwGh5IXgnkoVNqwibSNnr5GPweJ5ibBgeV8PgRtA7SrcPaloqXa20IcibLPrL2MYZ2ZcQdLrOOdLl3DEAGkZC9AdKQMsKm6uzg/640?wx_fmt=gif&from=appmsg)

**归属 / Attribution 置信度**

|  |  |  |
| --- | --- | --- |
| **维度** | **观察** | **置信度** |
| 攻击者账号 | nrwise 账号使用 Proton Mail（匿名邮箱） | 高 |
| C2 基础设施 | sfrclak.com 域名无业务背景，HTTP 明文通信 | 高 |
| TTP 特征 | 与2021 ua-parser-js 事件手法高度相似（账号劫持+postinstall） | 中 |
| 动机 | 全平台RAT 植入，以情报窃取/凭据盗取为主要目的 | 中 |
| 归属组织 | 暂无充分证据归属至特定APT 组织 | 低 |

攻击者归因：有待进一步溯源。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxSYtvd5JRk6pTmlhetiae6TYnY5kUaicDOfYYNgPOqLGfOOP1RKIcJn8ibqicv54SrQQSBcO4cBiaHheOQwZvVhicpVdXKHhrnrtRM7k/640?wx_fmt=gif&from=appmsg)

**账号劫持机制分析**

攻击者获取 npm 发布权限的完整链条：

· 步骤 1：获取 jasonsaayman 的 npm 账号凭据（疑为钓鱼或凭据填充攻击）

· 步骤 2：修改账号关联邮箱，阻断真实维护者的密码重置通道

· 步骤 3：通过 npm CLI 直接执行 npm publish，绕过 GitHub Actions CI/CD

· 关键点：官方 CI/CD 流程要求对应 GitHub tag，手动 npm publish 无此约束

· 时机选择：UTC 00:21，对应北美东部时间前一日 20:21，维护者下班时段，延迟响应

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxThgh11T8S9tmP3MXl2pmLianpfUeKYbdqH1aeSPBVxdryj9y4bBF5BGnjS4vF5opURNyDiclvmDbKxrJm8YSFE3psnh6sMDica64/640?wx_fmt=gif&from=appmsg)

**恶意依赖注入方式（Phantom Dependency Injection）**

攻击手法核心：幻影依赖注入（Phantom Dependency Injection）

· plain-crypto-js@4.2.1 被添加至 axios 的 package.json dependencies 字段

· 该包在 axios 源代码的任何位置均无 import / require 引用

· 其存在的唯一目的：触发 npm 的自动 postinstall 执行机制

· plain-crypto-js/package.json 中声明："scripts": {"postinstall": "node setup.js"}

· 用户执行 npm install axios@1.14.1 → npm 拉取 plain-crypto-js@4.2.1 → 自动执行 setup.js

攻击者预先发布 plain-crypto-js@4.2.0（干净版本）以建立包的历史合法性，降低安全扫描器的告警概率。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxTnt8thxdBptNsL6IcX6yqbHW7icfuiccps5kCv8fZ9kY3oHbBRbic2YDj07CydqO173av9MmWib97Hf3ak7wHFibzCd94tFfHKngfI/640?wx_fmt=gif&from=appmsg)

**Dropper 静态分析（plain-crypto-js/setup.js）**

**混淆技术**

* 字符串混淆：XOR 密钥加密 + Base64 双重编码，有效规避静态字符串检测

* 函数名混淆：使用随机无意义变量名，代码可读性极低

* 动态解码：关键字符串（C2 URL、文件路径）在运行时解码，不以明文出现

**执行流程（还原后逻辑）**

|  |
| --- |
| 1. 解码混淆字符串  →  XOR decode → Base64 decode → 获得 C2 URL 等参数  2. 检测平台        →  process.platform: darwin / win32 / linux  3. 分支执行        →  根据平台选择对应 payload 投放逻辑  4. 请求 C2        →  HTTP POST http://sfrclak.com:8000/6202033                       body: { platform: "product0/1/2" }  5. 下载二阶段 RAT  →  写入平台特定路径并赋权执行  6. 自我清除        →  替换 package.json 为干净存根，删除 setup.js |

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxQpynDZE6ibdNmhZUw3JyWKC5WuyxQvY76TRopqL6u7z3SKdvYffnzz3ZUTEo09he8pswyvrmoY4ibuZic9iaZEwEL3MZ6Mkh8icZus/640?wx_fmt=gif&from=appmsg)

**三平台 Payload 行为详析**

|  |  |  |  |
| --- | --- | --- | --- |
| **维度** | **macOS (product0)** | **Windows (product1)** | **Linux (product2)** |
| RAT 落地路径 | /Library/Caches/ com.apple.act.mond | %PROGRAMDATA%\wt.exe %TEMP%\6202033.vbs %TEMP%\6202033.ps1 | /tmp/ld.py |
| 执行...