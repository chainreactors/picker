---
title: 今日（2026年5月2日）热点网络安全漏洞动态
url: https://mp.weixin.qq.com/s/wT5hFY9_7vIjWQHLPiMR-Q
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:24:54.500664
---

# 今日（2026年5月2日）热点网络安全漏洞动态

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555sAosjMTft6KjKhQbtjKW6BjSHnSpcYXByLem5VRAeAbUv4cxfae3sN617OHNnUGrDKkGibbaWE986KqRTczNKMm62dH3kNuqg8/0?wx_fmt=jpeg)

# 今日（2026年5月2日）热点网络安全漏洞动态

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**日期：**2026-05-02　　**威胁等级：****High****来源：**CISA KEV · securityonline.info · 官方公告

## 一、概要

2026年5月2日前后最新高热度漏洞：**Linux内核本地权限提升**（CVE-2026-31431，5月1日新进KEV）；**CoreDNS多高危漏洞**（K8s云原生核心组件）；**Wazuh集群同步漏洞**（CVE-2026-30893，横向移动+Root访问）；**ASUSTOR ADM根级RCE**（CVE-2026-6644，PoC已公开）；以及**Jenkins插件RCE/XSS漏洞**。以上漏洞涵盖内核、DevOps、云原生和NAS环境，建议立即评估修复。

## 二、高危漏洞详情

### CVE-2026-31431：Linux Kernel 本地权限提升（KEV新增）

**本地提权**5月1日新进KEV

**受影响产品：**Linux Kernel（多个发行版，algif\_aead模块受影响）。

**影响：**本地普通用户可通过确定性方式在任意可读文件的页缓存中写入受控4字节数据，实现**本地提权至root**，并支持容器逃逸，影响服务器、容器或虚拟化环境。

**热度原因：**2026年5月1日加入CISA KEV目录，有活跃利用证据；Linux内核广泛使用，提权漏洞易被用于持久化攻击；4月30日由Theori团队正式披露，技术细节详细，trivially exploitable。

**修复建议：**立即升级到包含修复的最新内核版本（参考kernel.org stable分支）；启用SELinux/AppArmor等访问控制；监控异常进程；无法升级时隔离受影响系统。

### CoreDNS 多高危漏洞（4月30日安全更新）

**DoS · DNS缓存投毒**K8s核心组件

**受影响产品：**CoreDNS（早期版本，广泛用于Kubernetes等云原生环境）。

**影响：**DoH/DoQ相关漏洞，可能导致**拒绝服务、DNS缓存投毒或信息泄露**，影响基础设施解析安全。

**热度原因：**4月30日发布安全警报并推送修复版本；CoreDNS是云原生核心组件，暴露面广，Kubernetes环境中几乎无处不在，易被针对性攻击。

**修复建议：**立即升级到**CoreDNS 1.14.3+**；限制DoH/DoQ暴露；加强DNS日志监控和访问控制。

### CVE-2026-30893：Wazuh 集群同步漏洞

**横向移动 · Root访问**4月30日警报

**受影响产品：**Wazuh（开源SIEM/XDR平台，受影响版本）。

**影响：**可通过集群同步机制实现**远程代码执行和节点接管**，横向移动并获取Root访问权限。

**热度原因：**4月30日警报发布；Wazuh用于企业安全监控，一旦攻破影响范围大，集群环境风险突出；安全监控平台自身被攻破可导致攻击者静默潜伏。

**修复建议：**升级Wazuh到修复版本；隔离集群节点、强化认证机制、使用最小权限；监控异常集群通信。

### CVE-2026-6644：ASUSTOR ADM Root 远程代码执行

**Root RCE**PoC已公开

**受影响产品：**ASUSTOR ADM（NAS管理系统）。

**影响：**未授权攻击者可**完全接管NAS设备**，获取Root级别远程代码执行权限，可导致数据泄露、勒索加密或进一步横向渗透。

**热度原因：**4月30日公开PoC和技术细节；NAS设备常暴露互联网，PoC公开加速在野利用；ASUSTOR在企业和家庭存储市场有广泛部署。

**修复建议：**立即升级ADM固件到最新修复版本；禁用不必要互联网暴露（建议VPN访问）；更改默认凭证；监控执行日志。

### Jenkins 插件高危远程代码执行与 XSS 漏洞

**RCE · XSS**CI/CD供应链

**受影响产品：**流行CI/CD Jenkins插件（具体插件见Jenkins官方安全公告）。

**影响：**远程代码执行（RCE）和跨站脚本（XSS），可导致服务器接管、凭证窃取或供应链攻击。

**热度原因：**4月30日安全公告；Jenkins是主流DevOps工具，插件生态庞大；CI/CD管道被攻破可导致大规模供应链攻击，热度持续。

**修复建议：**更新受影响插件到最新安全版本；限制插件权限、启用安全沙箱；定期审计构建环境；参考Jenkins官方安全公告确认受影响插件列表。

### 其他近期高关注漏洞补充

**SonicWall SonicOS 多漏洞**：影响多代防火墙，已发布修复，建议尽快 patching。

**NVIDIA NemoClaw 提示注入/SSRF漏洞**（v0.0.18修复）：AI相关框架高危，影响LLM调用安全。

## 三、总体修复提醒

* **最高优先：**

  Linux内核CVE-2026-31431（5月1日新进KEV，容器逃逸风险，云环境立即打补丁）和ASUSTOR ADM CVE-2026-6644（PoC已公开，NAS设备勿轻视）。
* **DevOps与云原生：**

  Wazuh（集群隔离）、CoreDNS（升级1.14.3+）和Jenkins插件（更新安全版本）同步处置。
* **通用防护：**

  启用自动更新和EDR监控；优先处理互联网暴露的关键资产；参考CISA KEV目录排序风险；定期扫描并管理供应链组件。

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