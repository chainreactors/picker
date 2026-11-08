---
title: 网络安全早报·11月06日
url: https://mp.weixin.qq.com/s/eD0uYCwNKXCU3VGsNm45KQ
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:12:25.541243
---

# 网络安全早报·11月06日

# 网络安全早报·11月06日

原创

安全早报
安全早报

Ncko

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026 年 11 月 6 日 · 共 8 条

01高危OpenSSH 密码认证绕过漏洞披露次日出现利用尝试

11 月 6 日，The Hacker News 报道称，针对 OpenSSH 漏洞 CVE-2026-123158 的登录尝试在披露后数小时出现。该漏洞代号 SSHole，影响在 musl C 库上运行、未启用 PAM 的 Linux 系统，Alpine Linux 默认 openssh-server 配置在受影响范围内。

攻击者向本应禁用密码的账户提交 257 至 1024 字节的超长密码，即可通过认证。安全厂商 Previdian 称，其蜜罐在披露后数小时内被登录并取得 root。漏洞来自 2016 年为修复用户名枚举问题（CVE-2016-6210）引入的补丁，CVSS 评分 8.1。

**受影响：**OpenSSH 10.6p2 之前版本，条件为 musl + 未启用 PAM + 开启密码登录；Alpine Linux 3.16 至 3.24 及 edge。

**官方处置：**OpenSSH 于 11 月 5 日发布 10.6p2；Alpine 已为 3.16 起各分支发布修复包，升级后需重启 sshd。OpenSSH 认为根因在 sshd 之外，已在代码中加入规避措施。

02Chainalysis 确认全平台用户凭据与令牌泄露，KYT 分批恢复

11 月 6 日，Chainalysis 更新安全事件说明。公司称 11 月 2 日发现恶意行为者获取了全部用户的姓名、用户名、密码哈希与有效令牌（live tokens），调查期间已将 Reactor 与 Data Solutions 下线。

11 月 6 日 3:30（美东时间）起，KYT 与 Address Screening 进入分阶段恢复。公司称目前没有证据显示调查数据被访问，或归因数据被篡改。

**受影响：**Chainalysis 平台全部用户；KYT、Reactor、Address Screening 等产品。

**官方处置：**分阶段恢复访问；要求用户提交可信 IP 加入白名单，恢复后所有用户须重置密码并轮换 API 密钥。

03Barracuda 邮件网关两漏洞可串联，免登录拿到 root

11 月 6 日，安全公司 watchTowr 公开 Barracuda Email Security Gateway 的攻击链。CVE-2026-116606 是授权绕过，未认证攻击者可恢复特制配置备份并修改设备全局设置。

CVE-2026-111560 是命令注入，可将命令以 root 权限执行，通常需要管理员账户。两者串联后，攻击者无需登录即可获得 root。Barracuda 于 11 月 2 日发布补丁。

**受影响：**Email Security Gateway（授权绕过）；命令注入另影响 5 款产品，但在这些产品上仍需管理员权限。

**官方处置：**Barracuda 已发布 BNSF-40425 与 BNSF-40430 修复包，需按设备固件版本选择对应更新。

04高危Windows 画图 RCE 修复仅通过 Microsoft Store 分发

11 月 6 日，The Hacker News 报道 Windows 画图（Paint）漏洞 CVE-2026-83844 的修复已进入 Microsoft Store。该漏洞为越界读取（CWE-125），CVSS 评分 8.1，微软评级 Important。

攻击者可通过网络向受影响服务发送特制数据包执行代码，无需认证与用户交互。修复版本为 11.2609.401.0，不随 Windows Update 下发。在多个国家检查中，Store 曾长期只提供未修复的 11.2605.81.0。

**受影响：**Windows 内置画图应用，版本低于 11.2609.401.0。

**官方处置：**微软在 Microsoft Store 发布 11.2609.401.0；微软称利用需深入了解目标系统，发布时未见在野利用或公开披露。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5LNgXJargeWo8pt8tvI1vc6MwNSDd6y2N2vAmVOJLu9fMyp4Q1gJ8jVsyicbnE9OreYKUOTIBMQwvdEVatz4V757hjCKJgw9S2LjibuYFaic4g/640?from=appmsg)

图：GBHackers 报道配图，2026-11-06

05Control Web Panel 的 cwpsrv 被植入后门 cwpdoor

11 月 6 日，奇安信 XLab 披露在 Control Web Panel（CWP）的 Web 服务器 cwpsrv 中发现后门，命名为 cwpdoor。被改造的 cwpsrv 会执行攻击者通过 Web 请求发送的命令，且这些请求不写入访问日志。

研究人员 6 月 29 日截获伪装成版本更新的安装脚本，脚本只处理 cwpsrv 1.15.10 与 1.24.0 两个版本。9 月 30 日，一份后门副本从巴西上传至 VirusTotal。XLab 称这表明已有真实受害者，但未给出感染服务器数量。

**受影响：**Control Web Panel 的 cwpsrv 1.15.10、1.24.0。安装后门需 root 权限，XLab 尚未确认攻击者获取 root 的途径。

06恶意浏览器扩展可借 Claude Dispatch 在用户电脑执行命令

11 月 6 日，Forever Security 公布名为 ThisBash 的利用方式。具备 claude.ai 页面脚本执行权限的扩展，可向 Claude Desktop 的 Dispatch 功能发送指令，由后者在电脑上执行命令。

Dispatch 接受普通 claude.ai 登录会话，网页端未显示入口。PoC 用 Manifest V3 扩展在 200×200 非焦点弹窗中打开 Dispatch 页面，并每 1 秒点击一次"Allow"。Forever Security 于 5 月 14 日报告，Anthropic 确认问题有效。

**受影响：**启用 Dispatch 的 Claude Desktop，与已登录 claude.ai 的浏览器扩展；跨设备登录时，浏览器与桌面可在不同电脑。

**官方处置：**Anthropic 表示将下线 Dispatch，目标时间为 2026 年 10 月底；帮助页面显示新用户已不可用，现有用户仍可使用。

07高危在野利用WordPress Core 竞争条件 RCE 遭 24 万次利用尝试

11 月 6 日，Wordfence 数据披露针对 WordPress Core 漏洞 CVE-2026-119977 的利用尝试超过 24 万次。攻击自 10 月 28 日开始，与 WordPress 发布安全更新同日；10 月 30 日单日拦截请求超过 7.4 万次。

漏洞为升级过程中的竞争条件。完整升级时，安装文件被解压到 /wp-content/upgrade/ 下的可预测目录，未认证攻击者可在升级完成前访问临时安装程序，进而创建管理员账户并上传 PHP 代码。CVSS 评分 8.1。

**受影响：**4.7 至 7.1.3 的未修补分支。

**官方处置：**WordPress 于 10 月 28 日发布 7.1.4，并回补各分支至 6.6.11、6.7.11、6.8.12、6.9.11、7.0.8；Wordfence 建议升级前阻断 /wp-content/upgrade/ 下的 PHP 文件访问。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5LNgXJargeU3hekSHvoU6YOG1fwibVHQDNUMvQO6VMSsl3ibicVTaoiaUttibB0eeYKVlpanVg2z01sQtzSxqtQicekWbl9EMKSCGloNhZcuo9hJI/640?from=appmsg)

图：Cyber Security News 报道配图，2026-11-06

08Storm-2603 借 SharePoint ToolShell 植入无文件后门，用 Cloudflare Tunnel 维持访问

11 月 6 日，卡巴斯基发布针对 Storm-2603 的入侵分析。微软将该组织与中国关联，并将其与 Warlock 勒索软件联系。攻击者利用本地 SharePoint 的 ToolShell 漏洞链（CVE-2025-53770、CVE-2025-53771），在 IIS 工作进程 w3wp.exe 中加载仅驻留内存的 webshell。

主模块 G.cs 注册自定义 VirtualPathProvider 并挂钩 GetCacheKey()，仅在特定 User-Agent 出现时激活。权限提升使用 EfsPotato 式命名管道模拟获取 SYSTEM。随后通过 Velociraptor、Zoho Assist、VS Code CLI 与 Cloudflare Tunnel 建立多条隧道，使访问不再依赖 webshell。

**受影响：**未修补 ToolShell 漏洞的本地部署 SharePoint Server。

**官方处置：**微软建议安装 SharePoint 安全更新、启用 AMSI Full Mode、轮换 ASP.NET machine keys、执行 iisreset，并部署 Defender for Endpoint。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5LNgXJargeUG2IwLBw5J7cRxA66ic6ibI4fFh53ibyKIicvgSb85O49JEJBCnj3ykiaUibgeNRjI5LXuQSqqh9DZhbRD0a7eYUNfAj5OR8icS0hicTQ/640?from=appmsg)

图：卡巴斯基事件时间线，2026-11-06

信息来源

The Hacker News　https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html

Chainalysis　https://www.chainalysis.com/blog/security-incident-october-30/

OpenSSH　https://www.openssh.org/releasenotes.html

Alpine Linux　https://www.alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/

The Hacker News　https://thehackernews.com/2026/11/experts-demonstrate-barracuda-email.html

Microsoft　https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-83844

The Hacker News　https://thehackernews.com/2026/11/hackers-hide-linux-backdoor-in-control.html

The Hacker News　https://thehackernews.com/2026/11/malicious-browser-extensions-could-use.html

Cyber Security News　https://cybersecuritynews.com/240000-wordpress-exploit-attempts/

WordPress　https://wordpress.org/news/2026/10/wordpress-7-1-4/

Kaspersky　https://securelist.com/storm-2603-fileless-toolshell-attack/121467/

FreeBuf　https://www.freebuf.com/articles/system/511040.html

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GtFR6uY3nh6MJdyIdsWXrDem00Mia2eSiae1MMcoX2HUKRsPnx0EenFmcMdQwn0qAz5TJfRlOYVF4zsSibLicTlPtA/0?wx_fmt=png)

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