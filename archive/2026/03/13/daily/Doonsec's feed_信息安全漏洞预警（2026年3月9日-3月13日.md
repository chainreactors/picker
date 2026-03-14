---
title: 信息安全漏洞预警（2026年3月9日-3月13日
url: https://mp.weixin.qq.com/s/skH3iBOmLiWiUpsBGvkw8g
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:11:41.872927
---

# 信息安全漏洞预警（2026年3月9日-3月13日

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2xCpgJcagf8UvmiaeDp7Unibp3AAJOKvo9wSg1fRK2ncOIZvZGEsftibDqQ8ibYbcvUiaGPctbCuib09tJ14J5ZFOYDfYicD4VHfOWNrJvGMWZ1Ops/0?wx_fmt=jpeg)

# 信息安全漏洞预警（2026年3月9日-3月13日

松杨网络安全资料库

![]()

在小说阅读器中沉浸阅读

我司致力于持续观察与收集国内外最新的漏洞情报，重点关注CNVD、CNNVD等权威安全平台发布的漏洞公告，及时整理和收录相关漏洞信息，助力提升信息安全防护能力，保障客户系统的安全稳定运行。经过我们团队的分析和筛查，我们收录了以下安全漏洞信息。目前，相关官方机构已经发布了针对这些安全漏洞的补丁和修复方案。我们建议相关用户和组织及时关注并采取相应的安全措施，以确保信息系统的安全和稳定。收录的漏洞详细信息如下：

涉及漏洞数量：CVE漏洞：756个；CNVD漏洞：3个 ；其它漏洞：1个；

重点关注漏洞：

### 1.Nginx UI信息泄露漏洞(CVE-2026-27944)

| 漏洞名称 | Nginx UI信息泄露漏洞 |
| --- | --- |
| 漏洞编号 | CVE-2026-27944 |
| 影响等级 | 高危 |
| 漏洞披露时间 | 2026-03-9 |
| 影响版本 | Nginx UI < 2.3.3 |
| 漏洞说明 | 该漏洞源于/api/backup 端点无需身份验证即可访问，并在 X-Backup-Security 响应头中泄露了解密备份所需的加密密钥。攻击者能够下载服务器敏感数据（用户凭据、会话令牌、SSL 私钥、Nginx 配置）的完整系统备份并解密。 |
| 修复方式 | 厂商已提供漏洞修补方案，建议用户下载使用：https://github.com/0xJacky/nginx-ui/releases/ |
| 相关链接 | https://github.com/0xJacky/nginx-ui/security/advisories/GHSA-g9w5-qffc-6762 |

### 2.Apache Tomcat客户端证书验证缺陷漏洞

| 漏洞名称 | Apache Tomcat客户端证书验证缺陷漏洞 |
| --- | --- |
| 漏洞编号 | CNVD-2026-13409 |
| 影响等级 | 中危 |
| 漏洞披露时间 | 2026-03-11 |
| 影响版本 | Apache Tomcat 11.0.18、Apache Tomcat 10.1.52、Apache Tomcat 9.0.115 |
| 漏洞说明 | Apache Tomcat是美国阿帕奇（Apache）基金会的一款轻量级Web应用服务器，用于实现对Servlet和JavaServer Page（JSP）的支持。Apache Tomcat客户端证书存在验证缺陷漏洞，该漏洞是由于允许吊销证书/测试证书访问，如同时启用了基于客户端证书的认证机制，攻击者可利用该漏洞导致应用的授权机制绕过和EoP。 |
| 修复方式 | 目前没有详细解决方案提供，缓解措施为：停用APR + Tomcat Native / FFM；切换SSL Implementation至JSSEImplementation |
| 相关链接 | https://www.cnvd.org.cn/flaw/show/CNVD-2026-13409 |

### 3.OpenClaw代码问题漏洞

| 漏洞名称 | OpenClaw代码问题漏洞 |
| --- | --- |
| 漏洞编号 | CNVD-2026-13294 |
| 影响等级 | 高危 |
| 漏洞披露时间 | 2026-03-11 |
| 影响版本 | OpenClaw OpenClaw <2026.2.14 |
| 漏洞说明 | OpenClaw是OpenClaw开源的一个智能人工助理。OpenClaw存在代码问题漏洞，该漏洞源于Gateway工具接受工具提供的gatewayUrl时限制不足，攻击者可利用该漏洞导致OpenClaw主机尝试向用户指定的目标发起出站WebSocket连接，可用于有限的网络可达性探测。 |
| 修复方式 | 厂商已发布了漏洞修复程序，请及时关注更新：https://github.com/openclaw/openclaw/releases |
| 相关链接 | https://www.cnvd.org.cn/flaw/show/CNVD-2026-13294 |

### 4.OpenClaw操作系统命令注入漏洞（CNVD-2026-13291）

| 漏洞名称 | OpenClaw操作系统命令注入漏洞 |
| --- | --- |
| 漏洞编号 | CNVD-2026-13291 |
| 影响等级 | 高危 |
| 漏洞披露时间 | 2026-03-11 |
| 影响版本 | OpenClaw OpenClaw <2026.1.29 |
| 漏洞说明 | OpenClaw是openclaw开源的一个智能人工助理。OpenClaw存在操作系统命令注入漏洞，该漏洞源于Docker沙箱执行机制中构造shell命令时对PATH环境变量处理不安全，攻击者可利用该漏洞会影响容器上下文中的命令执行。 |
| 修复方式 | 目前厂商已经发布了升级补丁以修复这个安全问题，请到厂商的主页下载：https://github.com/openclaw/openclaw/commit/771f23d36b95ec2204cc9a0054045f5d8439ea75 |
| 相关链接 | https://www.cnvd.org.cn/flaw/show/CNVD-2026-13291 |

### 5.OpenClaw < 2026.2.2 身份验证绕过漏洞(CVE-2026-28472)

| 漏洞名称 | OpenClaw < 2026.2.2 身份验证绕过漏洞(CVE-2026-28472) |
| --- | --- |
| 漏洞编号 | CVE-2026-28472 |
| 影响等级 | 高危 |
| 漏洞披露时间 | 2026-03-06 |
| 影响版本 | 2026.2.1 版本之前 |
| 漏洞说明 | OpenClaw 是一个开源的个人AI 助手平台，支持通过多种消息渠道与AI 交互。 在其 2026.2.1 版本之前，存在一个逻辑漏洞：若请求中存在 `auth.token` 参数，则跳过设备标识（Device Identity）检查。然而，系统在跳过检查前并未对该令牌的有效性进行验证。攻击者可以通过在 WebSocket 握手请求中包含任意未经验证的 `auth.token` 来绕过身份验证和设备配对流程，从而与Agent环境直接交互，可能导致服务器失陷。 |
| 修复方式 | 1、升级至最新版本。2、利用安全组设置其仅对可信地址开放。 |
| 相关链接 | https://github.com/openclaw/openclaw/commit/fe81b1d7125a014b8280da461f34efbf5f761575 https://github.com/openclaw/openclaw/security/advisories/GHSA-rv39-79c4-7459 https://www.vulncheck.com/advisories/openclaw-device-identity-check-bypass-in... |

### 6.关于用友GRP-U8Cloud产品jmreport组件模块存漏洞的安全通告

| 漏洞名称 | 关于用友GRP-U8Cloud产品jmreport组件模块存漏洞的安全通告 |
| --- | --- |
| 漏洞编号 |  |
| 影响等级 | 高危 |
| 漏洞披露时间 | 2026-03-13 |
| 影响版本 | 影响版本包含用友GRP-U8Cloud行政G，教育G，乡财G，信创普及版 |
| 漏洞说明 | 已下线废弃的jmreport组件模块存安全漏洞，对产品造成潜在风险隐患。 |
| 修复方式 | 对相关功能下线处理，移除相关漏洞程序，避免潜在风险隐患，尽快更新安全补丁完成修复。 |
| 相关链接 | https://security.yonyou.com/#/noticeInfo?id=769 |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

松杨网络安全资料库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

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