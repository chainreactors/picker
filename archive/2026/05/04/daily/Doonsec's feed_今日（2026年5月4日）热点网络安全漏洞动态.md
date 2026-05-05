---
title: 今日（2026年5月4日）热点网络安全漏洞动态
url: https://mp.weixin.qq.com/s/iERwGEYTYSiryFCqSuqFQQ
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:58:11.879771
---

# 今日（2026年5月4日）热点网络安全漏洞动态

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555sNzvgpBTWUah3UIKOZ8pbkeBXeibs6ROK5RrqSic6mfc4lIVicAkDTMJ9gXWKDGy4sMhT5nTzLpoA5h55osBYHRkuJpEUTuRUJNU/0?wx_fmt=jpeg)

# 今日（2026年5月4日）热点网络安全漏洞动态

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**日期：**2026-05-04　　**威胁等级：****High****来源：**securityonline.info · NVD · Tenable

## 一、概要

2026年5月4日前后热度较高的漏洞：**Edimax路由器缓冲区溢出**（CVE-2026-7685/7684，PoC已公开）；**ProFTPD mod\_sql SQL注入**（完整PoC披露）；**ModSecurity v3 DoS漏洞**（CVE-2026-30923，一行脚本可崩溃WAF）；以及**Jenkins DDoS Botnet利用**（5月1-4日活跃，RCE植入僵尸网络）。近期热点转向边缘设备、FTP/WAF组件和DevOps工具，需立即处置。

## 二、高危漏洞详情

### CVE-2026-7685 & CVE-2026-7684：Edimax路由器缓冲区溢出（PoC已公开）

**CVSS High**5月3日披露 · PoC公开

**受影响产品：**Edimax BR-6208AC（<=1.02）、BR-6428nC（<=1.16）等型号路由器。

**影响：**远程攻击者通过WAN设置接口（`/goform/setWAN`）操纵`pptpDfGateway`等参数触发栈缓冲区溢出，可导致**拒绝服务（DoS）或潜在远程代码执行（RCE）**。

**热度原因：**5月3日最新披露，PoC已公开，厂商未及时响应；路由器设备基数大、固件更新慢，易被大规模扫描利用，成为边缘网络攻击新热点。

**修复建议：**立即升级到最新固件版本（检查厂商官网）；禁用远程WAN管理、将设备置于防火墙后、更改默认凭证；使用WAF或入侵检测阻挡异常WAN请求；无法升级的建议隔离或更换设备。

### ProFTPD mod\_sql SQL注入（完整PoC披露）

**CVSS Critical**5月3日PoC公开

**受影响产品：**ProFTPD with mod\_sql模块（特定配置下的版本）。

**影响：**允许攻击者通过SQL注入执行任意查询，可能导致认证绕过、数据泄露、权限提升甚至**远程代码执行**，在FTP服务器广泛部署的环境中风险极高。

**热度原因：**5月3日前后完整技术细节和PoC公开；FTP服务仍是常见攻击面，易引发连锁利用（数据窃取+横向移动）；企业文件传输基础设施中ProFTPD部署广泛。

**修复建议：**升级ProFTPD到最新安全版本并禁用/更新mod\_sql配置；使用参数化查询或严格输入验证；限制FTP暴露（使用SFTP替代）、启用日志监控和WAF规则；生产环境测试后立即重启服务。

### CVE-2026-30923：ModSecurity v3 DoS漏洞（一行脚本崩溃WAF）

**CVSS High**5月1-3日热议

**受影响产品：**ModSecurity v3（libmodsecurity3库）。

**影响：**攻击者发送特定请求即可触发DoS，使WAF崩溃或拒绝服务，**绕过防护导致后端应用直接暴露**，一行脚本即可攻击。

**热度原因：**5月1-3日报道，一行脚本即可攻击；WAF作为关键防护层被针对；安全社区讨论热烈；对依赖ModSecurity作为主要防护的企业影响大。

**修复建议：**升级到最新ModSecurity版本（应用官方补丁）；配置请求限流和异常检测规则；结合其他WAF/防护层（如Cloudflare/Nginx模块）；监控WAF日志中的崩溃信号。

### Jenkins DDoS Botnet利用（5月1-4日活跃）

**RCE + Botnet**5月1日起活跃

**受影响产品：**未打补丁的Jenkins实例（常见于CI/CD环境）。

**影响：**攻击者利用Jenkins漏洞实现**远程代码执行**，植入DDoS僵尸网络，主要针对游戏服务器等高带宽目标，已形成真实威胁。

**热度原因：**5月1日左右新Botnet活动报道；结合Jenkins的广泛使用和游戏行业攻击趋势；实时威胁高，已观察到真实攻击流量。

**修复建议：**升级Jenkins到最新版本，启用安全插件并禁用不必要脚本/代理；使用最小权限、ACL和网络隔离；监控异常构建/插件活动；部署Web应用防火墙阻挡已知Jenkins利用路径。

## 三、总体修复提醒

* **最高优先：**

  Jenkins（5月1日起活跃，Botnet植入，立即升级）和ProFTPD（完整PoC公开，FTP服务器立即修补）。
* **边缘设备：**

  Edimax路由器（PoC已公开，禁用WAN管理）和ModSecurity（升级最新版本，加固WAF）。
* **通用防护：**

  公网暴露服务严格限制；启用自动更新和定期漏洞扫描；使用零信任原则和WAF防护；持续关注CISA KEV、NVD和securityonline.info最新条目。

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