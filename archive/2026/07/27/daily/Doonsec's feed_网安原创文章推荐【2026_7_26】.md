---
title: 网安原创文章推荐【2026/7/26】
url: https://mp.weixin.qq.com/s/SNQXp8X7kOJjbqqpsJ7qGA
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:56:06.428024
---

# 网安原创文章推荐【2026/7/26】

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CZMNsicRfJAAicdIicZ1gtry77IoKq0FmPMyge9payc468ichW3tt3ube6tM5Tb2ibqBqNcdVDftL4lqicVJXHzo8pIPxZRrBYibuKOibElVs9bJqGc/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/7/26】

AJay13
AJay13

洞见网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 2026-07-26 微信公众号精选安全技术文章总览

> 洞见网安 2026-07-26

---

### 0x1 [安全 DNS 部署指南](https://mp.weixin.qq.com/s?__biz=MzYzOTE5MDU0OA==&mid=2247484671&idx=1&sn=a16ddb02950fb638f51ae4e8ddf62080&scene=21#wechat_redirect "安全 DNS 部署指南")

> 哪吒网络安全 2026-07-26 22:31:25

![](https://mmbiz.qpic.cn/mmbiz_jpg/ia7TorzX5Pa3Q0urLDsvox4HkXxYwk0TCCcyK5sFZIcyPVk64nUPictF5IXvTVKxMYE1SBgEvUuvHvoms0xffQxVcTNLLWICA9icJ1jHxW46Ds/640?wx_fmt=jpeg)

本文为 NIST SP 800-81r3 的中文精译，旨在指导企业在零信任与纵深防御框架下，将 DNS 从纯运营组件升级为基础安全控制层。文章面向网络安全决策者和一线网络/安全运营团队，系统讲解了保护性 DNS、权威服务、递归/转发服务、存根解析器四大主题，并附有 DNS 协议教程与术语表。文章强调 DNS 在网络连接中的核心地位，以及其在安全策略中的重要性。建议普遍部署保护性 DNS，对内外部 DNS 流量加密，部署 DNSSEC 保护数据完整性，部署专用 DNS 服务器以缩减攻击面，并遵循技术指引确保 DNS 部署与协议的安全性和弹性。文章还详细分析了权威服务和递归/转发服务的威胁与防护措施，以及存根解析器的安全考量。

网络安全

零信任架构

纵深防御

DNSSEC

加密 DNS

权威服务

递归服务

存根解析器

---

### 0x2 [openHiTLS 在 Windows 下使用 MinGW-w64 编译全过程](https://mp.weixin.qq.com/s?__biz=MzU1Mjk3MDY1OA==&mid=2247526088&idx=1&sn=c1d5c5b245b11a85a63db3429b066342&scene=21#wechat_redirect "openHiTLS 在 Windows 下使用 MinGW-w64 编译全过程")

> 利刃信安 2026-07-26 22:00:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZaibroIiatwe3lPUejKuEPQuIbyIBNGbibibpAPE4dwSY3f8GFeOFRyz9Kice04Lpxq4GuYliaiaib13N7fAVoWQ13C81ooz1CwOR0kXgnYOM3YbTj4/640?wx_fmt=jpeg)

本文详细介绍了在 Windows 下使用 MinGW-w64 编译 openHiTLS 0.3.4 的全过程。由于 openHiTLS 是为 Linux/macOS 设计的密码学库，在 Windows 环境下编译面临系统级差异，如时间函数、动态库加载、网络编程、IO 控制和终端控制等方面的不兼容。为了解决这些问题，文章提出创建 MinGW 兼容层的核心策略，在 build/mingw\_compat/ 目录下创建同名头文件，利用 CMake 的搜索优先级拦截对缺失 POSIX 头文件的引用。同时，使用 Windows API 封装 POSIX 动态库接口，提供兼容的实现，如将 dlopen 映射到 LoadLibraryA。对于无法映射的功能，如终端控制，提供桩函数确保编译链接通过。此外，移除所有汇编源文件，使用 openHiTLS 自带的纯 C 备选实现，并利用 MinGW 已有的 vsnprintf\_s 实现缺失的 snprintf\_s。最终产出的 hitls.exe 是纯 Windows 原生 PE 可执行文件，运行时仅依赖 Windows 系统 DLL，支持国密和国际算法的全部功能。整个过程涉及修改 CMake 构建配置、源码文件和头文件，最终成功在 Windows 下编译 openHiTLS。

编译安全

跨平台兼容

系统安全

密码学库

安全函数

Windows安全

---

### 0x3 [SiYuan 未授权接管MCP可至RCE | CVE-2026-66012 研究及复现](https://mp.weixin.qq.com/s?__biz=MzE5ODMzOTgwMg==&mid=2247484773&idx=1&sn=35f2b2015523f516379ff80d2ea9ff3f&scene=21#wechat_redirect "SiYuan 未授权接管MCP可至RCE | CVE-2026-66012 研究及复现")

> 404号浪漫 2026-07-26 19:58:08

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eefCd8vibaic1pYYVib9HPquic3aehCSp2ayaLOFsIoB0UkEqu26jPsQTibicx8v4VibsghTibSQUiao8SVcFlNDSI4Qzt24hTQ2LrlZw0glggggR7CY/640?wx_fmt=jpeg)

思源笔记(v3.7.1)在开启匿名发布模式时，其内嵌的MCP服务端存在未授权访问缺陷。攻击者可无凭据访问MCP的file.write工具，向目标工作区的data/plugins/目录植入恶意Node.js代码。当受害者使用思源桌面客户端加载或同步该工作区时，由于Electron渲染进程配置了nodeIntegration: true且contextIsolation: false，桌面端将直接触发系统级命令执行。此漏洞链构成“服务端投毒、客户端爆发”的水坑攻击，最终导致运维或团队成员客户端被远程控制。攻击者通过零交互水坑攻击链路，可在服务器端静默埋伏恶意payload，待客户端启动加载时接管其本地系统权限。漏洞利用条件包括配置项publish.enable=true和publish.auth.enable=false，以及攻击者可访问发布端口（默认0.0.0.0:6808）。修复建议包括升级至最新版本v3.7.2及以上，启用发布服务Basic认证，防火墙限制访问，关闭发布服务，设置锁屏密码，以及审计和删除非本人安装的插件。

未授权访问

远程代码执行 (RCE)

服务端投毒

客户端爆发

水坑攻击

JWT 验证缺陷

配置错误

权限提升

凭证窃取

Electron 安全漏洞

---

### 0x4 [紧急安全预警｜GitLab 默认配置可遭远程代码执行：Oj 解析器漏洞链曝光（多版本受影响）](https://mp.weixin.qq.com/s?__biz=Mzk2OTAzNjI0OQ==&mid=2247486478&idx=1&sn=2602226ff441acda59164aa7047758ba&scene=21#wechat_redirect "紧急安全预警｜GitLab 默认配置可遭远程代码执行：Oj 解析器漏洞链曝光（多版本受影响）")

> 杂杂咱谈 2026-07-26 17:54:38

![](https://mmbiz.qpic.cn/mmbiz_jpg/xoBWaEOhvREMuyA3PJr9de2UmMBcj1PtibPicJgz8qj4f7sZiabtaV7Byxdicej2KFe4NXEHNzT9o5hE0FEmmFLHwgwNDiae7jOeAfFk2TsEiaibwo/640?wx_fmt=jpeg)

本文报道了一起针对GitLab的高危漏洞利用链。该漏洞利用了GitLab默认配置下的Oj原生JSON解析库中的两个内存安全漏洞，通过组合这两个漏洞，攻击者可以在GitLab上实现远程代码执行。攻击者无需利用SSRF或管理员权限，仅需普通项目成员权限即可完成攻击。漏洞源于Oj解析器，研究人员发现攻击者可以通过提交恶意.ipynb文件并查看Diff来触发漏洞。该漏洞可能导致攻击者以GitLabgit系统用户身份执行任意命令，获取源码、Rails密钥、服务凭据以及内部网络资源。GitLab已发布修复版本，建议用户尽快升级至最新版本，并更新Oj组件至3.17.3或更高版本，同时加强对Notebook Diff功能、用户权限及异常日志的监控。

远程代码执行（RCE）

GitLab漏洞

内存安全漏洞

代码解析库漏洞

漏洞利用链

权限要求低

安全预警

版本影响

安全修复

---

### 0x5 [一条规则检测 Cobalt Strike 流量](https://mp.weixin.qq.com/s?__biz=MzAwMjQ2NTQ4Mg==&mid=2247509965&idx=1&sn=4f049e7494bcb1d3e8eeb1834f3122b3&scene=21#wechat_redirect "一条规则检测 Cobalt Strike 流量")

> Khan安全团队 2026-07-26 15:10:58

![](https://mmbiz.qpic.cn/mmbiz_jpg/J7CSmJcRR8lQyf2zE1h6VoDYkT8w6Pnq4ctPINarJIyQyTUM9Xx4C7ibgh3d5awIN3dFTYIFjCGQH5InT8BsunNfKPib5Bc8zx1KPmAcpkyoY/640?wx_fmt=jpeg)

本文介绍了一种通过分析Web Proxy日志来检测Cobalt Strike（CS）Beacon流量的方法。该方法的核心思想是寻找内网主机访问那些低信誉、低流量、低普及率的域名/IP，并且这些访问只涉及少量固定URI的异常HTTP通信。通过设置一系列条件，如URI数量不超过2、访问主机不超过4、连接次数达到300次以上等，可以识别出可能隐藏的Cobalt Strike C2通信。文章中给出了一个实战案例，展示了如何通过日志中的具体信息来识别Cobalt Strike的特征，包括内部主机地址、目标域名、URI、连接次数和HTTP方法等。

入侵检测

恶意软件检测

网络监控

异常流量分析

Cobalt Strike

---

### 0x6 [RokRAT恶意软件隐藏在伪造的PDF文件](https://mp.weixin.qq.com/s?__biz=MzYzOTMyNTUzNw==&mid=2247485540&idx=1&sn=e5798d09497743e1b9746ee3e7140f92&scene=21#wechat_redirect "RokRAT恶意软件隐藏在伪造的PDF文件")

> 威胁情报Z分析 2026-07-26 15:07:03

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0LGiaGIrzXukYAdc3DFNslbKVXDWD1uSAVjiawYafGkER0bzfFd0YluVrNrVgJvDAMHib2J4M2hA6tWHgiaY64zQsorGTIvSJvMwJkT3ZEvHHSU/640?wx_fmt=jpeg)

Genians 安全中心揭露了一起名为“胶囊保险库行动”的 RokRAT 恶意软件攻击活动，该活动涉及通过伪装成PDF的文件进行鱼叉式网络钓鱼。攻击者利用与朝鲜有关联的APT37组织，通过发送伪装成学术活动通知的邮件，诱骗受害者点击链接至Dropbox的ISO镜像文件。文件内部隐藏了一个PIF可执行文件，当受害者打开时，会显示真实的PDF文件，同时在后台运行RokRAT恶意软件。RokRAT恶意软件能够进行主机指纹识别，并与云服务通信以进行命令和控制操作。该攻击被关联到APT37组织，攻击目标为研究、政策和学术领域的人员。

恶意软件攻击

鱼叉式网络钓鱼

APT攻击

文档伪装

云服务利用

内存执行

命令和控制（C2）

数据窃取

受害者指纹识别

云账户关联

---

### 0x7 [CVE-2026-63030 / CVE-2026-60137 漏洞分析：从路由混淆到 SQL 注入](https://mp.weixin.qq.com/s?__biz=Mzk5MDc5MDY2OA==&mid=2247483936&idx=1&sn=5d91fdec1851512a1f1b3e0f33e41711&scene=21#wechat_redirect "CVE-2026-63030 / CVE-2026-60137 漏洞分析：从路由混淆到 SQL 注入")

> 剑指安全 2026-07-26 13:46:45

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LZBR0aDZ77ick2InhHp6IRv20Enn3gibZIx1xicwMMS4AxicHpw2qvcEqTQfYkT9FHj8TpNL3142QN4z5KVc403IzXXicTwib6L3SUXlqmxO0IGxE/640?wx_fmt=jpeg)

本文深入分析了WordPress 6.9.4版本中两个关键漏洞（CVE-2026-63030和CVE-2026-60137）的原理及利用方法。文章首先介绍了WordPress REST API的路由注册机制、请求执行流程以及关键组件的作用。接着，重点分析了/batch/v1接口的缺陷，即数组错位漏洞，该漏洞允许通过嵌套请求的方式，将一个请求的错误处理流程导向另一个正常的处理流程，从而实现未授权访问。文章进一步阐述了如何利用/batch/v1接口结合WP\_Query中的SQL注入漏洞，通过路由混淆和参数绕过技术，最终实现未授权SQL注入。最后，文章总结了漏洞链的全景图，并提出了相应的修复方案，包括修复数组错位漏洞和WP\_Query中的SQL注入漏洞。本文对于理解WordPress REST API的安全机制及漏洞利用具有重要意义。

WordPress

REST API

SQL注入

漏洞分析

漏洞利用

代码审计

批处理漏洞

权限绕过

---

### 0x8 [【已复现】NGINX 远程代码执行漏洞，RCE代码已公开(CVE-2026-42533)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM3NTU5MA==&mid=2247497748&idx=1&sn=7477c847391674a26d6264e5f9473792&scene=21#wechat_redirect "【已复现】NGINX 远程代码执行漏洞，RCE代码已公开(CVE-2026-42533)")

> 360漏洞研究院 2026-07-26 11:36:49

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dZ7ia5iaWFzz8DgX0J74OibIiaWpZoQkk0t0IFqdPicnsY30beMroRSv9yHNMrGib4CKFhd4QvY6Gr7BTjvC0dyCFsIMKnELwKRQvkBLnicbkOUA0Y/640?wx_fmt=jpeg)

本文报道了NGINX出现的高危堆缓冲区溢出漏洞（CVE-2026-42533），该漏洞CVSS评分为8.1，允许未经身份验证的远程攻击者通过发送特制的HTTP请求来触发NGINX worker进程的堆缓冲区溢出。该漏洞一旦被利用，可能导致远程代码执行，攻击者可以以NGINX服务的权限执行任意系统命令。360漏洞挖掘智能体已成功复现此漏洞。受影响的NGINX版本包括Open Source的1.30.0至1.30.3，以及NGINX Plus的R33至R36。建议用户升级至1.31.x系列或更高版本以修复此漏洞。文章详细介绍了漏洞的概述、技术原理、影响范围、复现步骤以及修复建议，并提供了相关的产品和时间线信息。

远程代码执行（RCE）

堆缓冲区溢出

NGINX 漏洞

安全漏洞

HTTP 请求攻击

CVSS评分

漏洞复现

安全修复

漏洞利用

网络安全预警

---

### 0x9 [通过两个 Ruby 内存损坏漏洞实现 GitLab RCE【PoC 已发布】](https://mp.weixin.qq.com/s?__biz=MjM5Mzc4MzUzMQ==&mid=2650265822&idx=1&sn=7315a76d2f380137f698bd2980874b94&scene=21#wechat_redirect "通过两个 Ruby 内存损坏漏洞实现 GitLab RCE【PoC 已发布】")

> 骨哥说事 2026-07-26 10:46:45

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZiaLfYNlAGNyiaWB4DJP8JJv1eIspcOtYITTI0Cb81C1P2ZVZzRdMb6HAkNk8s6WiaHhCznWC8W1pNE0BTFHwIcLq3j7mjNUCSsf0/640?wx_fmt=jpeg)

本文详细分析了一个由 Open Defense Initiative 的 depthfirst 系统发现的高性能 JSON 解析器 Oj 中的两个内存安全问题，这些漏洞被成功利用在 GitLab 中实现了远程代码执行。Oj 是一个主要使用原生 C 语言实现的 Ruby JSON 解析器，被广泛用于包括 GitLab 在内的许多 Ruby 应用程序。depthfirst 系统在 Oj 的源代码中发现了 18 个潜在漏洞，其中 7 个是内存安全问题。本文重点介绍了两个漏洞：一个越界写入和一个堆指针泄露。这两个漏洞在 Oj 中存在近五年，并被用于影响 GitLab CE 和 EE 的多个版本，包括 15.2.0 至 18.10.7、18.11.0 至 18.11.4 以及 19.0.0 至 19.0.1。GitLab 在收到报告后迅速发布了补丁。文章还讨论了攻击者如何利用这些漏洞构建攻击链，以及如何通过控制解析器状态和泄露堆指针来最终实现远程代码执行。此外，文章还提到了 Oj 中其他已发现的漏洞，以及 GitLab 和 Oj 作者对漏洞的修复时间线。
...