---
title: 「推安早报」0718 | elf加密反向shell、红蓝工具推荐
url: https://mp.weixin.qq.com/s?__biz=MzU0MDcyMTMxOQ==&mid=2247487535&idx=1&sn=f1ff1579aa1f7cdfaef7c8c4fa906493&chksm=fb35b9e7cc4230f1dfa15329e0a35d451cd12171dd2a05a097880e618442d65a7c6e6714ae8a&scene=58&subscene=0#rd
source: 甲方安全建设
date: 2024-07-19
fetch_date: 2025-10-06T17:42:35.354305
---

# 「推安早报」0718 | elf加密反向shell、红蓝工具推荐

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZmf8HKsAOjMBqkaZeYOnBbg39PzU5LRIMgMJpbx44XEZCWJmXX1xsAId49Xm0gFaIHkdibX5Vu3dtQ/0?wx_fmt=jpeg)

# 「推安早报」0718 | elf加密反向shell、红蓝工具推荐

bggsec

甲方安全建设

# 2024-07-18 安全「信息差」每天快人一步

> 1. 推送「新、热、赞」，降噪增效
>
> 2. 查漏补缺，你可能错过了一些小东西

### 0x01 内存中执行未经管理的PE文件工具

> `No-Consolation` 是一款可以在内存中执行未经管理的 PE 文件（包括 EXE 和 DLL），并且能够检索输出结果而不需要分配控制台或创建新进程的工具。

### 关键信息点

* `No-Consolation` 工具的设计目的是在不创建新进程和控制台的情况下，高效地在内存中执行未经管理的 PE 文件，并且能够处理这些文件的输出。
* 该工具的内存管理功能，包括加载、保存和卸载 PE 文件，提高了操作的灵活性和安全性。
* 通过丰富的命令行选项，用户可以精确控制 PE 文件的加载方式、执行方式和内存管理行为，满足不同的使用场景。
* `No-Consolation` 的设计考虑到了对 DLL 的支持，包括链接到 PEB、执行特定导出函数以及处理依赖项。

🏷️: No-Consolation, PE文件执行, 内存管理, 工具, 编程

### 0x02 Bifrost 工具使用指南

> Bifrost 是一个针对 macOS 设备上 Heimdal krb5 APIs 的 Objective-C 项目，旨在通过原生 API 进行更好的安全测试，特别是针对 Kerberos 的测试，无需安装额外的框架或包。

### 关键信息点

* Bifrost 项目的设计目的是为了在 macOS 环境下进行 Kerberos 安全测试，它利用了 Heimdal krb5 APIs 提供的功能。
* Bifrost 提供了一系列命令行工具，使得安全研究人员能够更方便地操作和测试 Kerberos 认证流程。
* 通过 Bifrost，用户可以轻松地导出和导入 Kerberos 票证，以及执行高级操作，如 S4U 和 Kerberoasting。
* Bifrost 支持多种加密类型，确保了在不同安全要求的环境中的适用性。

🏷️: 网络安全, 工具使用

### 0x03 利用提示注入攻击生成式AI聊天机器人的方法

> NetSPI 研究人员通过 prompt injection 漏洞成功地对一个集成了大型语言模型（LLM）的聊天机器人进行了攻击，实现了远程代码执行（RCE），并强调了 AI 聊天机器人安全性的重要性。

### 关键信息点

* AI 聊天机器人的安全性至关重要，尤其是当它们能够接受和执行用户输入时。
* 聊天机器人的代码执行功能需要得到适当的限制和隔离，以防止恶意行为。
* 对于 AI 系统，应该实施强 authentication 和 access controls 以防止未授权的交互。
* AI 系统的输入应该进行验证和消毒，以防止 prompt injection 和其他攻击技术。

🏷️: AI安全, 聊天机器人, 提示注入, 语言模型, 系统漏洞

### 0x04 识别PsExec的关键方法

> 本文介绍了如何识别并分析使用 PsExec 工具的活动，特别是在安全事件和恶意软件攻击中，强调了新的识别方法，如 USN 日志和 Prefetch 文件。

### 关键信息点

* PsExec 是一个强大的工具，但也常被威胁行为者用于恶意目的，如勒索软件部署。
* 通过系统事件 7045 和安全事件 4624 类型 3，可以追踪 PsExec 的执行和源系统。
* PsExec v2.30 及以后版本引入了 `.key` 文件的机制，这些文件的创建被记录在 USN 日志和 Prefetch 文件中，为分析师提供了新的识别手段。
* 尽管存在一些异常情况，USN 日志中可能不会记录 `.key` 文件的创建事件，但这些新的识别方法对于取证分析和追踪威胁行为者的活动至关重要。

🏷️: PsExec, 远程管理工具, 威胁行为者, 系统安全

### 0x05 如何绕过Golang的SSL验证

> 本文介绍了如何在使用 Golang 的 HTTPS 请求时绕过 SSL 证书验证，包括手动修改代码和使用 Python 脚本自动化修补预编译应用程序的方法。

### 关键信息点

* Golang 的 HTTPS 请求默认启用 SSL 验证，这可能会干扰安全测试和漏洞检查。
* 直接修改预编译应用程序的二进制文件是绕过 SSL 验证的一种方法，这对于没有源代码访问权限的情况尤其有用。
* 深入理解 `net/http` 库和 `verifyServerCertificate` 函数的工作原理是关键，它使得定位并修改相关的程序集指令成为可能。
* 逆向工程和程序集级别的修改需要对程序的内部结构有一定的了解，但不需要深入的低级编程技能。

🏷️: Golang, SSL验证, 网络安全, HTTPS请求

### 0x06 统领一切的反向Shell工具

> 本文介绍了一种新的反向shell工具oneshell，旨在解决现有工具存在的问题，如依赖不同的系统环境、连接不安全等，提供了一种跨平台、安全的反向shell解决方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZmf8HKsAOjMBqkaZeYOnBbgY2hpwISN3tRVDnSKZ9OHk81Q4YrO1RDc1Q6MkccD5iaprwzhwMYmS8A/640?wx_fmt=jpeg&quot)

### 关键信息点

* 跨平台兼容性：oneshell的设计目标是创建一个在大多数系统上都能工作的payload，减少攻击者在建立连接时需要尝试的payload数量。
* 连接安全性：使用Mutual TLS（MTLS）来确保数据传输的安全性，防止中间人攻击和数据泄露。
* 简化依赖：通过创建一个极小的ELF文件，避免了对系统中的curl、wget等工具的依赖，使得payload更加通用。
* 数据完整性：采用Treyfer算法实现CBC-MAC，以确保下载的二进制文件未被篡改。

🏷️: 反向shell, 网络安全, 跨平台, 安全解决方案

### 0x07 Chunk Loader：动态加载JavaScript文件的Chrome扩展

> Chunk Loader 是一款 Chrome 扩展程序，用于从指定的 URL 加载和导入 JavaScript 分块文件，对于需要基于主脚本动态加载多个 JavaScript 文件的开发者来说非常有用。

### 关键信息点

* Chunk Loader 提供了一种高效的方式来动态加载和导入 JavaScript 分块文件，这对于前端开发和调试非常重要。
* 该扩展程序支持自定义分块文件的基路径和文件扩展名，增加了灵活性。
* 安装和使用 Chunk Loader 的过程被详细记录在网页上，便于开发者遵循。
* 项目鼓励社区参与，通过开源贡献来改进和完善该工具。

🏷️: Chrome扩展, JavaScript, 开发者工具

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZlbmEWU7ZApsl3ia3YLicI4H3nwksKq8ZBqrghjtia9TYiblaxU2VXrUpDcAM57Ric0wX9pBg69IusWVyg/640?wx_fmt=jpeg)

快来和老司机们一起学习吧

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

甲方安全建设

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

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