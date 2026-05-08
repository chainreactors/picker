---
title: 今日（2026年5月7日）热点网络安全漏洞动态
url: https://mp.weixin.qq.com/s/36DjOg0tEEkCLj29fysyFg
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:55:00.120742
---

# 今日（2026年5月7日）热点网络安全漏洞动态

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555sIVKeXjy3q8zPxxptFp4whHZYdF09VPoKX11qWPH35mo8tACPicWnWIskLBGGTWAy8NRtibRxicshNxEDPCQlXa32KRthnM2YctQ/0?wx_fmt=jpeg)

# 今日（2026年5月7日）热点网络安全漏洞动态

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**日期：**2026-05-07　　**威胁等级：****High****来源：**securityonline.info · NVD · thehackernews · Apache

## 一、概要

2026年5月6-7日最新高热度漏洞：**Apache HTTP Server HTTP/2 双重释放**（CVE-2026-23918，CVSS 8.8，全球数百万站点受影响）；**Nix/Lix NAR解析器栈溢出**（CVE-2026-44028，可获取root权限）；**OPNsense防火墙多漏洞**（Root RCE+认证锁绕过，PoC已发布）；**vm2沙箱逃逸**（CVSS 9.8，影响570万用户）；以及**Apache Thrift多语言Critical漏洞**。共同特点：利用门槛低、影响核心基础设施组件，PoC快速传播，建议优先扫描处置。

## 二、高危漏洞详情

### CVE-2026-23918：Apache HTTP Server HTTP/2 双重释放

**CVSS 8.8 High**HTTP/2 Double-Freethehackernews · 热度极高

**受影响产品：**Apache HTTP Server（httpd）2.4.66 版本（启用 mod\_http2 模块，默认多线程 MPM 配置）。

**影响：**HTTP/2 协议处理中的 double-free 内存漏洞。通过发送 HTTP/2 HEADERS 帧后立即跟 RST\_STREAM（非零错误码），可在相同 stream 上触发双重释放，导致 **DoS（轻松崩溃 worker 进程）**和潜在**远程代码执行（RCE）**（尤其在 Debian 系系统或官方 Docker 镜像使用 APR mmap 分配器时）。

**热度原因：**Apache 是全球最广泛使用的 Web 服务器之一，影响数百万站点；披露后（约5月4-5日）PoC/细节快速传播，DoS 利用门槛极低，RCE 在常见部署中可行；securityonline.info 等平台重点报道，在野利用风险高，引发运维和安全社区紧急关注。

**修复建议：**立即升级到 Apache HTTP Server **2.4.67+**；临时可禁用 HTTP/2（ModHttp2Off）或切换到 prefork MPM；限制互联网暴露或使用 WAF 过滤异常 HTTP/2 帧；监控 worker 进程崩溃和异常内存行为；厂商推荐所有用户尽快更新。

### CVE-2026-44028：Nix / Lix NAR Parser Stack Overflow（5月6日高热度）

**CVSS ~7.5 High**5月6日突出报道

**受影响产品：**Nix（2.24.4 至 2.34.6 版本）和 Lix（2.93.0 至 2.95.1 版本），包括 NixOS 等基于 Nix 的系统。

**影响：**本地攻击者（可连接 Nix daemon 的用户，默认允许所有用户）通过恶意 NAR 档案触发 unbounded recursion，导致 stack-to-heap overflow，可能实现**任意代码执行**，获得 Nix daemon root 权限（多用户安装下为 root）。

**热度原因：**Nix 在 DevOps、CI/CD 和云原生环境中广泛使用，root 权限提升对服务器/构建环境威胁极大；5月6日被 securityonline.info 等平台突出报道。

**修复建议：**立即升级到 Nix 2.34.7+（或对应旧分支修复版）/ Lix 2.95.2+；限制 daemon 访问（allowed-users 配置）；监控 daemon 连接和异常进程；临时可禁用非必要 NAR 处理。

### OPNsense Firewall 多漏洞（Root RCE + Auth Lockout Bypass，PoC已发布）

**CVSS Critical**PoC已公开

**受影响产品：**OPNsense 防火墙（FreeBSD 基础，近期未修补版本受影响）。

**影响：**Root 级别远程代码执行（RCE）结合认证锁绕过，允许攻击者**完全接管防火墙设备**，控制网络流量、注入后门等。

**热度原因：**公开 PoC 发布后热度迅速上升；OPNsense 在中小企业和边缘部署中使用广泛；PoC 使利用门槛降低，易引发连锁攻击。

**修复建议：**升级到最新 OPNsense 稳定版本；限制管理界面互联网暴露（使用 VPN 或 IP 白名单）；启用 WAF/入侵检测；立即应用厂商安全更新。

### vm2 Sandbox Escape 多CVE（CVSS 9.8，影响570万用户）

**CVSS 9.8 Critical**570万+用户

**受影响产品：**Node.js vm2 库（早期受影响版本，如 <=3.10.x 等，具体依多 CVE 变体）。

**影响：**沙箱逃逸导致**远程代码执行（RCE）**，攻击者可突破隔离执行主机任意代码，影响使用 vm2 执行不受信 JS 的应用（如 AI/插件系统、在线代码执行平台）。

**热度原因：**vm2 被广泛用于 Node.js 沙箱场景，用户量大（570万+）；多高危变体+公开细节，易被供应链攻击利用，5月6日在 securityonline.info 被突出。

**修复建议：**升级 vm2 到最新安全版本（>=3.11.0 或对应修复）；审查依赖并更新所有使用 vm2 的应用；避免在生产环境中运行不受信代码；监控 Node.js 进程异常行为。

### Apache Thrift 多语言 Critical Flaws（5月6日报道）

**CVSS Critical**供应链风险

**受影响产品：**Apache Thrift（0.23.0 之前版本），跨语言 RPC 框架（Rust、Java、Node.js 等实现）。

**影响：**多漏洞包括证书主机名验证不当、内存分配过度、路径遍历等，可能导致**信息泄露、DoS、RCE 或中间人攻击**。

**修复建议：**立即升级到 Apache Thrift 0.23.0+；审查证书验证和输入处理逻辑；限制 Thrift 服务暴露范围；启用严格网络分段和监控；更新所有依赖 Thrift 的服务。

## 三、总体修复提醒

* **最高优先：**

  Apache httpd CVE-2026-23918（全球最广泛Web服务器，立即升级 2.4.67+）和 vm2（CVSS 9.8，570万用户，立即升级）。
* **DevOps环境：**

  Nix/Lix（升级2.34.7+/2.95.2+，限制daemon访问）。
* **企业网络：**

  OPNsense（PoC已公开，立即升级 + VPN/IP白名单）。
* **通用防护：**

  优先扫描 Apache/Nix/OPNsense/Node.js 相关资产；遵循"尽快修补"原则；结合零信任和最小暴露原则。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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