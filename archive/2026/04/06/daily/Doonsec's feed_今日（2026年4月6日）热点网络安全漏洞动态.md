---
title: 今日（2026年4月6日）热点网络安全漏洞动态
url: https://mp.weixin.qq.com/s/u6ILXE87wjp1d1Kbj0Oo8Q
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:28:06.584488
---

# 今日（2026年4月6日）热点网络安全漏洞动态

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555uvuYgxsfDUaHSPpicmciboXafzT3LSc8ATg6Je4w2nct9wB9oe0fCibVicgkOC5vLsT4QCWZaRjzxCIjzZrQQ9TFxD2PpmlfiageFY/0?wx_fmt=jpeg)

# 今日（2026年4月6日）热点网络安全漏洞动态

奇安信 CERT

![]()

在小说阅读器中沉浸阅读

# 2026年4月6日网络安全漏洞动态

> **发布日期**: 2026-04-06 | **威胁等级**: 🔴 高危

---

## 1. 概要

**今天（2026年4月6日）网络安全领域的主要新高热度漏洞总结如下。这些漏洞多为企业级产品的高危问题（CVSS 9.8或Critical），部分已处于主动利用状态，热度高是因为影响广泛的IT基础设施、官方紧急通报推动关注度，以及潜在的大规模企业/政府系统风险。**

---

## 2. 高危漏洞详情

### 🔥 FortiClient EMS CVE-2026-35616（Critical，不当访问控制漏洞）

**受影响产品**

FortiClient EMS 7.4.5 至 7.4.6 版本。

**影响**

未认证远程攻击者可完全接管服务器。

**热度原因**

CSA今日紧急警报，已在野外主动利用，Fortinet企业部署广泛。

**修复建议**

立即升级：更新至FortiClient EMS 7.4.7 或更高版本（推荐最新稳定版）。

官方补丁：登录Fortinet Support Portal下载对应热补丁（Hotfix），或通过FortiManager/FortiCloud自动推送。

临时缓解措施（打补丁前）：

1. 限制EMS管理界面仅内网访问（关闭公网暴露）。

2. 启用强认证并监控异常API请求。

3. 备份EMS数据库后隔离测试环境再升级。

**验证**

升级后运行FortiClient EMS自带完整性检查工具，确认版本号正确。厂商预计补丁已同步推送。

---

### 🔥 Cisco IMC CVE-2026-20093（CVSS 9.8，认证绕过漏洞）

**受影响产品**

Cisco Integrated Management Controller（IMC）多个企业硬件版本（5000 Series、Catalyst 8300、UCS C-Series/M5/M6/E-Series等）。

**影响**

未认证远程攻击者可直接劫持管理员密码并完全控制服务器。

**热度原因**

CSA今日警报，Cisco核心管理组件部署量巨大，无需认证特性极易被利用。

**修复建议**

立即升级：按照Cisco官方咨询更新至修复版本（具体见Cisco PSIRT公告，例如IMC 4.3(2.240)或更高，视硬件型号而定）。

官方补丁：通过Cisco Software Central或IMC Web界面在线升级；支持Smart Licensing的用户可一键推送。

临时缓解措施（打补丁前）：

1. 禁用IMC公网访问，仅允许可信IP通过ACL访问。

2. 启用多因素认证（MFA）并修改所有管理员密码。

3. 监控IMC日志中异常HTTP请求（尤其是密码修改API）。

**验证**

升级后在IMC界面检查“Firmware Version”并运行Cisco推荐的“Show Tech-Support”命令确认无漏洞残留。

---

### 🔥 Cisco SSM On-Prem CVE-2026-20160（CVSS 9.8，命令执行漏洞）

**受影响产品**

Cisco Smart Software Manager On-Prem（SSM On-Prem）9-202601 之前版本。

**影响**

未认证远程攻击者可root权限执行任意命令，完全控制系统。

**热度原因**

与IMC同属CSA今日警报，root级执行破坏力极强，企业许可管理系统广泛使用。

**修复建议**

立即升级：更新至SSM On-Prem 9-202601 或更高修复版本。

官方补丁：登录Cisco SSM On-Prem管理界面或通过Cisco Software Center下载并应用补丁包（支持离线安装）。

临时缓解措施（打补丁前）：

1. 关闭或限制SSM On-Prem暴露的内部服务端口（尤其是API端点）。

2. 在防火墙层面阻断非信任源IP对SSM的访问。

3. 启用详细审计日志并设置警报，监控root级命令执行。

**验证**

升级完成后运行Cisco提供的“ssm-health-check”工具，确保漏洞已完全修复。

---

### ⚠️ 其他今日新披露但热度相对较低的：

### CVE-2026-5609（Tenda i12 路由器栈缓冲区溢出，CVSS 8.8）

**修复建议**

立即固件升级至最新版本（Tenda官网下载i12最新固件），重启路由器后验证固件版本。临时缓解：关闭远程管理功能，改为仅LAN访问；家庭用户建议更换为更安全的路由器品牌。

---

## 1. 总体修复提醒

**优先级：上述Cisco与Fortinet漏洞均为CSA今日官方警报，必须在24-48小时内完成修复，否则面临真实在野攻击风险。**

**自动化建议：**使用漏洞扫描工具（Nessus、Qualys或厂商自带工具）批量检测受影响资产；企业环境推荐通过FortiManager/Cisco DNA Center集中推送补丁。

最佳实践：打完补丁后立即更换受影响系统的所有凭证，并监控48小时日志。

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