---
title: 逆向 skills 路由包 reverse-skill
url: https://mp.weixin.qq.com/s/toAe-NOapGGw2s6nasywUw
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:57:00.897363
---

# 逆向 skills 路由包 reverse-skill

# 逆向 skills 路由包 reverse-skill

zhaoxuya520
zhaoxuya520

无影安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明：本篇文章仅用于技术交流，请勿利用文章内的相关技术从事非法测试，由于传播、利用本公众号无影安全实验室所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号无影安全实验室及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！所有工具安全性自测！！！**VX：smile62157**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把"**无影安全实验室**"设为星标，这样更新文章也能第一时间推送！

![](https://mmbiz.qpic.cn/mmbiz_gif/3GHDOauYyUGbiaHXGx1ib5UxkKzSNtpMzY5tbbGdibG7icBSxlH783x1YTF0icAv8MWrmanB4u5qjyKfmYo1dDf7YbA/640?&wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

安全工具

## 0x01 前言

AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base
逆向/渗透/安全技能路由包 — AI 自动路由 · 按需自举工具链 · 自动进化经验库

![79c44a34ed688b96d6989d760372dcd4.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkgSnvibDykMhJUHwOAM8V9icoMRhIywK9YqBhiaAw3K03pfUVzzicqrC9bpIjRMoLvozgsHW7jsYEqiadm1KAXLeYicia15j0bADDlsw/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "null")

## 0x02 支持场景

| 场景 | 入口 |
| --- | --- |
| APK / Android 逆向 | `skills/apk-reverse/` |
| iOS / 移动端 | `skills/mobile-reverse/` |
| 二进制逆向 (exe/dll/so/elf) | `skills/ida-reverse/` / `skills/radare2/` |
| .NET / C# | `skills/dotnet-reverse/` |
| 前端 JS 签名 / 加密参数 | `skills/js-reverse/` |
| DSL VM / 风控自定义 VM | `skills/reverse-engineering/dsl-vm-reverse/` |
| HTTP 抓包 / 请求重放 | anything-analyzer、Reqable MCP + `js-reverse/` |
| 恶意软件 / YARA | `skills/malware-analysis/` |
| 渗透测试 / 漏洞扫描 | `skills/pentest-tools/` |
| 攻击链 / 红队编排 | `skills/attack-chain/` |
| Case 证据审查 / 报告交接 | `skills/case-review/` |
| CTF 竞赛 | `CTF-Sandbox-Orchestrator/` （42 个子技能） |
| 固件 / IoT | `skills/firmware-pentest/` |
| 补丁差分 / N-day | `skills/patch-diff-exploit/` |
| Pwn / 漏洞利用 | `skills/pwn-chain/` |
| EDR 绕过 | `skills/edr-bypass-re/` |
| API / GraphQL | `skills/api-security/` |
| 供应链 / SBOM | `skills/supply-chain-security/` |
| LLM / AI 安全 | `skills/llm-security/` |
| OLLVM 脱密 | `skills/reverse-engineering/references/ollvm-deobfuscation.md` |
| 图表 / 报告 | `skills/diagram-generator/` / `skills/docs-generator/` |

## 0x03 工具使用

支持的操作系统：

* • Windows：完整主路径，使用 PowerShell 脚本、winget 和 Windows 路径。
* • Kali Linux：专门优化，使用 Kali 原生安全工具及 apt。
* • Ubuntu／Debian，以及 Mint、Pop!\_OS 等：通用 Linux 路径。
* • macOS：通用支持，主要使用 Homebrew。

**教学文档**
https://reverse.apivix.com/docs/#top

### Windows 安装

```
git clone https://github.com/zhaoxuya520/reverse-skill.git
cd reverse-skill
```

交给 AI 安装

```
请完整阅读 README_AI.md，并严格按照其中第 0 节自动完成当前环境的初始化与检查。
正常步骤请直接自动执行；只有需要我的授权、凭据、商业许可证，或会改变外部状态时再询问我。
完成后汇报已识别的平台、规则链、工具索引状态，然后继续处理我接下来给出的授权任务。
我不需要手动复制执行教学页里展示的流程命令。
```

![794f5d5a350e162069624a734e733a2a.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmY76ictKsjKZAd92yvjcfKUm9ibticibPKfy4xNyQD1ewkHHM9c5mGJG0knjVz3WvLZ6ocGCc68ibvDiaMzzqU81hgMKGmia2wfcELaI/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1 "null")

794f5d5a350e162069624a734e733a2a.png

使用

```
静态分析 xxxx.apk
```

![8eeef3c0d9d1acadc0d6c13755cd2c75.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmhK2XJgX1rBu002rpX9ibvWiaz6dNB7zjmfb4k6yszCrAjC6tfNrRDgibq2x9IcQoFQO52e0lbp5bGLhMiaUD2SNF3kicRoMSqgb6c/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2 "null")

## 0x04 工具使用

**可能存在的问题**

### 封号

![d90ff559f7e07106a343f9ba3aee36ee.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnW090bleSQdXdibcW9sJJ5Tv1zcx9gVdr4Ih2kllL54lnWg8m1Fc3nCib5MCrD2kDL5rELSibIIOfTclsmy5f5fSxzCsgFQUBO0Y/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3 "null")

### 检查项目的 skills

项目中的 skills，也是从 GitHub 上收集来的，其中可能存在问题，建议使用前检测 skills 是否存在敏感和危险操作，仅使用必要的 skills，分必要的都删除

## 0x05 工具下载

**点****击关注****下方名片****进入公众号**

**回复关键字【260923****】获取****下载链接**

最后推荐一下内部小密圈，干货满满，物超所值，**内部圈子每增加100人，价格将上涨20元，越早进越优惠！！！**

**![图片](https://mmbiz.qpic.cn/mmbiz_jpg/awCdqJkJFET8apEknf7bc6ZR8CyWIBqmV3L88k03ibsUgLfyzvyvuOjkZUfWm9YsK0phQ3owbjBgbhibnWBicgsXw/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&randomid=ebo9tcn3&tp=webp)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFESkGMPLLYOibsOdiaYUbUGH2ibd832G0h4stN7iacicE62hCJGle1IuVQbgGDx5v5GXjwUuE23xJNJjgTg/0?wx_fmt=png)

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