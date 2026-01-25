---
title: 2026年网络安全学习指南 核心方法与路径汇总
url: https://mp.weixin.qq.com/s/t6R2SZCuyK_vzb1zY7kyEg
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:52:51.923287
---

# 2026年网络安全学习指南 核心方法与路径汇总

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0sjvG0TycCoWmZe4sARhrSl2foNiblGibFW7ltFTdAopqMd5n8BEHqAXxdz83m6qfEWAE8g9EE2nPMTAG8bx0NOA/0?wx_fmt=jpeg)

# 2026年网络安全学习指南 核心方法与路径

原创

山河
山河

不止Security

![]()

在小说阅读器中沉浸阅读

网络安全已从单一技能演变为多领域协同的工程体系。2026年，不同岗位对能力的要求差异显著。本文结合行业实际需求，为学习者梳理八条清晰可行的路径，涵盖：渗透测试、SRC漏洞挖掘、红队攻防、代码审计、应急响应、红队免杀、JS逆向、App渗透，每条路径均包含学习内容、实践任务、重点知识与常见误区，帮助你少走弯路。

PART 01

通用基础阶段（所有方向必学）

无论选择哪个方向，以下基础必须扎实掌握：

操作系统

掌握 Linux 常用命令、文件权限、进程管理； 了解 Windows PowerShell 与注册表基础。 目标：能部署 Web 服务、查看日志、排查异常进程。

计算机网络

理解 TCP/IP 模型、HTTP/HTTPS 协议细节、DNS 解析流程、Cookie/Session 机制。 目标：能用 Wireshark 分析一次完整登录或 API 调用过程。

Web 基础

熟悉 HTML/CSS 结构、JavaScript 事件与 Ajax 请求、浏览器开发者工具使用。 目标：能从页面中提取接口地址、分析请求参数。

编程入门

掌握 Python 基础语法、requests 发送 HTTP 请求、正则表达式、文件读写。 目标：能编写脚本批量检测 URL 存活性或提取日志关键词。

数据库

掌握 SQL 基础（SELECT/INSERT/UPDATE）、JOIN 查询、MySQL 安装与管理。 目标：能手写联合查询语句，理解注入风险点。

建议在 VirtualBox 或 VMware 中搭建 Ubuntu + Kali + Windows 10 三系统实验环境。

PART 02

渗透测试方向

学习内容

外网漏洞利用

* SQL 注入（联合查询、盲注、报错注入）

* XSS（反射型、存储型、DOM 型）

* 文件上传绕过（MIME 类型、解析漏洞）

* 越权（水平/垂直权限绕过）

* SSRF（内网探测、gopher 协议利用）

工具链掌握

* Burp Suite（Proxy、Repeater、Intruder）

* Nmap（服务识别 + NSE 脚本扫描）

* Dirsearch / ffuf（目录爆破）

报告规范

* CVSS 3.1 风险评分方法

* 等保2.0 对安全测试的基本要求

* 漏洞复现步骤的标准化写法

实践任务

* 在 PortSwigger Web Security Academy 完成全部实验

* 本地复现 DVWA、WebGoat 所有漏洞并手写 PoC

* 对 WordPress 或 Drupal 进行完整渗透测试，绘制攻击面地图

* 在补天或教育 SRC 提交至少 3 个有效漏洞，并获得审核通过

重点知识

理解漏洞成因比利用方式更重要； 同一漏洞在不同业务上下文中风险等级可能完全不同。

常见误区

只会用自动化工具，不会手工验证； 忽略报告质量与修复建议； 在未授权目标上测试。

PART 03

SRC 漏洞挖掘方向

学习内容

资产测绘

* 使用 subfinder + httpx 扫描子域名

* 通过 crt.sh、certspotter 查找证书关联资产

* 利用 LinkFinder 从 JS 文件中提取敏感接口或密钥

* 检测 S3、OSS 等云存储桶是否公开

高价值漏洞挖掘

* Swagger UI、Nacos、Druid 等中间件的未授权访问

* 密码重置绕过、积分兑换滥用、优惠券篡改等业务逻辑缺陷

* 短信轰炸、验证码爆破、批量信息查询等接口滥用问题

报告提交规范

* 明确判断是否属于 SRC 资产范围

* 提供完整且可复现的请求/响应包

* 避免提交 robots.txt、版本号等低价值信息泄露

实践任务

* 选定一家上市公司或高校，系统性找出 5 个以上非主站资产（如 test、dev、mail、api 子域）

* 在 edusrc 或补天平台找到一个有效的未授权接口或逻辑漏洞并成功提交

* 持续优化报告格式，争取获得多次有效奖励

重点知识

主站往往无洞，边缘系统才是突破口； 业务逻辑漏洞需结合用户旅程分析。

常见误区

只扫描主站，忽略测试环境、小程序、邮件系统； 提交大量低危漏洞被平台降权； 不看 SRC 范围说明。

PART 04

红队攻防方向

学习内容

外网打点

* 钓鱼邮件构造（HTML 伪装、短链接诱导）

* 免杀木马生成（Sliver、VShell、Donut）

* C2 通信混淆（HTTPS 伪装、DNS 隧道、ICMP 隐蔽通道）

内网渗透

* 深入理解 Active Directory 架构

* 掌握哈希传递（PTH）、票据传递（PTT）

* 黄金票据（Golden Ticket）、白银票据（Silver Ticket）伪造

* 使用 BloodHound 分析权限路径

权限维持与反溯源

* 计划任务、WMI、服务后门部署

* Windows 日志清理（Event Log、PowerShell History）

* 绕过 Sysmon 监控、ETW 补丁或 Hook

实践任务

* 在 Vulnhub 或本地靶机实现上线，并绕过 Windows Defender 基础检测

* 搭建 Windows 域环境，完成从普通域用户到域控的完整提权链

* 设计一次 72 小时权限维持演练，确保不被常规监控发现

重点知识

红队核心在内网横向，不在外网打点； Living-off-the-Land（利用系统自带工具）是降低特征的关键。

常见误区

过度依赖 Cobalt Strike； 只练打点不练内网； 忽视蓝队视角，无法预判防御动作。

PART 05

代码审计方向

学习内容

环境搭建

* PHPStorm + Xdebug 调试配置

* 部署 ThinkPHP、Laravel、DedeCMS 等项目

漏洞模式识别

* SQL 拼接 vs 参数化查询

* 动态文件包含（include( $ \_GET['page'])）

* 反序列化 POP 链构造

* 命令执行（system/exec/popen）

静态分析辅助

* Seay 源码审计系统

* CodeQL 基础规则编写

* Semgrep 快速扫描

多语言拓展

* Java：Spring Boot Actuator 未授权、Fastjson 反序列化

* Python：Flask SSTI、pickle 反序列化

* Node.js：原型污染、child\_process 命令注入

实践任务

* 单步调试 DedeCMS 登录流程，找到一处 SQL 注入并写出完整利用链

* 对 WordPress 插件进行批量扫描，人工验证高危结果

* 审计一个 Java 开源项目（如若依），发现未授权或 RCE 漏洞

重点知识

跟踪用户输入（ GET/GET/ \_POST/body）到危险函数（eval/system/unserialize）的完整数据流； 理解框架特性（如 Laravel 中间件、ThinkPHP 路由）是关键。

常见误区

只看函数名不看上下文； 依赖工具不人工验证； 审计大型项目无目标，效率低下。

PART 06

应急响应方向

学习内容

日志体系认知

* Windows Event Log（4688 进程创建、4624 登录事件）

* Linux auditd / syslog / bash\_history

* Web 服务器日志（Nginx/Apache 访问日志）

* 网络流量日志（NetFlow、PCAP）

威胁排查方法

* 异常进程分析（ps / tasklist / Process Explorer）

* 启动项检查（注册表 Run、crontab、systemd）

* 网络连接排查（netstat / ss / lsof）

* 文件时间线分析（mtime/atime/ctime）

工具链与自动化

* Wazuh / ELK 搭建简易 SIEM

* YARA 规则编写识别恶意样本

* 自动化响应脚本（隔离 IP、禁用账户）

体系化响应

* 编写应急响应报告（时间线、影响范围、根因、改进建议）

* MITRE ATT&CK 框架映射攻击行为

实践任务

* 在虚拟机中模拟 Webshell 上传与执行，完整记录各层日志

* 使用 Velociraptor 或 Sysmon 采集主机数据，定位后门并提取 IOC

* 复盘 Lazarus 等公开 APT 事件，输出蓝队应对方案

重点知识

从海量日志中重建攻击时间线； 将行为映射到 MITRE ATT&CK 提升分析效率。

常见误区

只看杀毒软件报警，忽略无文件攻击； 删除恶意文件就结束，不查横向路径； 报告只有结论，无证据链。

PART 07

红队免杀方向

学习内容

Windows 底层基础

* PE 文件结构（节表、导入表、重定位）

* 进程/线程/内存管理机制

* DLL 加载与 API 调用约定

免杀原理与绕过

* 静态特征混淆（字符串加密、控制流扁平化）

* 动态行为规避（延迟执行、间接调用、API 哈希）

* AMSI/Sysmon/ETW 绕过基础

自研加载器开发

* Shellcode 注入（CreateRemoteThread、APC、Process Hollowing）

* 无文件执行（PowerShell → .NET → Native）

* HTTPS C2 通信封装（自签证书、SNI 伪装）

进阶对抗技术

* ETW 日志清理（内核 Patch 或用户层 Hook）

* NTDLL 直接系统调用（Syscall）

* Living-off-the-Land（certutil、regsvr32、msbuild）

实践任务

* 用 C 编写一个动态加载 DLL 并调用导出函数的程序

* 修改 Cobalt Strike Beacon 或 Sliver Payload，绕过 Windows Defender 静态检测

* 用 Go 或 C++ 编写一个支持 HTTPS 的简易 C2 客户端

* 在启用了 CrowdStrike 或 SentinelOne 的环境中实现稳定上线

重点知识

EDR 主要监控行为（如可疑进程注入），而非文件哈希； 间接调用与延迟执行可有效规避检测。

常见误区

盲目使用开源免杀模板而不理解原理； 只测试 Defender，忽略商业 EDR； 忽视 C2 流量特征被 DPI 识别。

PART 08

JS 逆向方向

学习内容

基础调试技巧

* Chrome DevTools 断点、调用栈、作用域分析

* 控制台 Hook 函数（XMLHttpRequest、fetch、crypto）

* 绕过 debugger 反调试（never pause、覆盖 Function 构造器）

加密算法识别

* AES/RSA/Base64/MD5 特征识别

* 扣取加密函数并本地调用（补全 window/document）

* 使用 Node.js 复现加密逻辑

进阶对抗技术

* Webpack 打包代码还原（source map 或 AST 重构）

* AST 去混淆（删除花指令、还原控制流）

* Puppeteer + Playwright 自动化绕过滑块/验证码

小程序专项

* 微信开发者工具反编译

* wxapkg 解包（wxappUnpacker）

* 请求头伪造（xweb\_xhr、referer）

实践任务

* 对某电商或社交网站登录接口进行参数还原，提取 token 生成逻辑

* 扣出某微信小程序 sign 算法，在本地生成有效签名并通过接口验证

* 对某视频站 H5 页面实现无感播放，绕过 token 时效与设备绑定

* 提取某金融小程序的交易接口，模拟调用并分析风控策略

重点知识

快速定位加密入口（如 sign = encrypt(data)）； 在 Node.js 中补全浏览器环境对象是关键。

常见误区

试图完全还原混淆代码，其实只需扣出关键函数； 忽略反调试机制导致调试失败； 在未授权网站大规模爬取触发风控。

PART 09

App 渗透方向

学习内容

Android 基础

* APK 反编译（JADX 查 Java、Apktool 查资源）

* 抓包对抗（证书绑定绕过、SSL Pinning bypass）

* Frida Hook 基础（Java.perform、Interceptor）

协议解密

* 识别 native 层加密（libxxx.so 中的加密函数）

* Frida 主动调用 Java/Native 函数（rpc.exports）

* Xposed/Frida 脱壳（DexDump、FART）

iOS 专项

* macOS 环境配置（Xcode、frida）

* iOS 抓包（SSL Kill Switch、Charles 证书）

* frida-ios-dump 砸壳、objection 动态分析

客户端安全测试

* 组件暴露（Activity/Service/BroadcastReceiver）

* 敏感信息泄露（SharedPreferences、日志、剪贴板）

* Root/越狱检测绕过、本地存储加密分析

实践任务

* 对某新闻或社交类 App 实现 HTTPS 抓包，并修改返回数据验证漏洞

* 还原某社交 App 的消息加密协议，实现明文收发

* 对某银行或电商 iOS App 实现接口拦截，提取交易参数

* 完成一次完整 App 安全评估报告，涵盖组件、数据存储、通信、防护机制

重点知识

多数 App 采用 OkHttp + 自定义 TrustManager 实现证书绑定； SO 层加密需结合 IDA 静态分析与 Frida 动态调用。

常见误区

以为抓包成功就结束，忽略二次加密或签名； 在非 root 设备强行分析效率极低； 逆向商业 App 用于黑产，法律风险极高。

PART 10

通用建议

不要跳过基础：Linux、网络、Python 是所有方向的基石。 动手优先：每个知识点必须在虚拟机或靶场中验证。 合法第一：仅在授权平台（SRC、HTB、自购 App）练习，严禁未授权测试。 持续输出：写博客、做笔记、复盘案例，是能力沉淀的关键。 关注防御视角：即使是红队方向，也需理解蓝队如何检测，才能真正绕过。

PART 11

推荐资源汇总

靶场

PortSwigger Web Security Academy、Hack The Box、Vulnhub、LetsDefend、AppSecurityLab

工具

* 攻防：Burp Suite、Nmap、BloodHound、Sliver

* 逆向：JADX、Frida、Objection、IDA Free、Ghidra

* 防御：Wazuh、Velociraptor、YARA、ELK Stack、Sysmon

书籍

《Web安全深度剖析》《内网安全攻防》《加密与解密》《Android 软件安全权威指南》《The Practice of Network Security Monitoring》

社区

看雪论坛、FreeBuf、先知社区、GitHub Security Topics、MITRE ATT&CK 官网

2026年，网络安全的机会属于有方向、有耐心、有动手能力的人。 选择一条路，扎进去，练出来。 你会比想象中走得更远。

网络安全从业者如何走得更远？

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/0sjvG0TycCoWmZe4sARhrSl2foNiblGibF8E6TIFNZQa38B97vKfjU2ibAosvvic0KGQnuZIUtPmasgDTkQA2z28LA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU3OTYxNDY1NA==&mid=2247485982&idx=1&sn=bb3c13d3974dd5eb47941b120f454a13&scene=21#wechat_redirect)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0sjvG0TycCrkwqc9NOyXnxJdd3Sx952ibuNc9JbaRIwgribBX5MRFHecGVwgntRMicphmT55OA24qTJdzwXhegujQ/0?wx_fmt=png)

不止Security

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0sjvG0TycCrkwqc9NOyXnxJdd3Sx952ibuNc9JbaRIwgribBX5MRFHecGVwgntRMicphmT55OA24qTJdzwXhegujQ/0?wx_fmt=png)

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