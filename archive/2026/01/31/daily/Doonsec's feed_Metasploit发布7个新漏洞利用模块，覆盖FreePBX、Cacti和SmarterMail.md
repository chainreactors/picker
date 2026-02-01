---
title: Metasploit发布7个新漏洞利用模块，覆盖FreePBX、Cacti和SmarterMail
url: https://mp.weixin.qq.com/s/S6IEtr56ruwCPpGQWpHPXw
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:25:02.001211
---

# Metasploit发布7个新漏洞利用模块，覆盖FreePBX、Cacti和SmarterMail

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibdIDHM7Kns9672aia7ZlDr12Pgiakrlhzq9zYeoJIkV8hQ3nl3wN7DMl6YCwCMVL3Hpdz4vgj5ArWQ/0?wx_fmt=jpeg)

# Metasploit发布7个新漏洞利用模块，覆盖FreePBX、Cacti和SmarterMail

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibdIDHM7Kns9672aia7ZlDr1e15xsKPAf9xM0wJBswXBPQN6ekHZckciaCKlMPjFmA8LlhtzMxZEW0A/640?wx_fmt=png&from=appmsg)

本周 Metasploit 框架的最新更新为渗透测试人员和红队成员带来重大增强，新增了七个针对常用企业软件的漏洞利用模块。本次更新的亮点包括三个针对 FreePBX 的复杂模块，以及针对 Cacti 和 SmarterMail 的关键远程代码执行（RCE）功能。

此次更新凸显了通过将认证绕过漏洞与次要漏洞串联实现完全系统入侵的持续风险。

**Part01**

## ****FreePBX漏洞串联攻击****

框架最重要的新增功能涉及三个针对 FreePBX 的不同模块。FreePBX 是控制 Asterisk（PBX）的开源图形界面。研究人员 Noah King 和 msutovsky-r7 开发了一种方法，通过串联多个漏洞将权限从未认证状态提升至远程代码执行。

攻击链始于（CVE-2025-66039），这是一个认证绕过漏洞，允许未授权攻击者绕过登录协议。一旦突破认证屏障，框架提供两条不同的 RCE 路径。

第一条利用路径利用了被标识为（CVE-2025-61675）的 SQL 注入漏洞。通过注入恶意 SQL 命令，攻击者可操纵数据库向 cron\_job 表插入新任务，从而有效安排任意代码的执行。

第二条路径则利用（CVE-2025-61678），这是固件上传功能中存在的不受限制文件上传漏洞。攻击者可借此直接向服务器上传 webshell，立即获得控制权。

该系列中的第三个辅助模块利用相同的 SQL 注入漏洞创建恶意管理员账户，展示了该漏洞利用链的多功能性。

**Part02**

## ****Cacti和SmarterMail的关键RCE漏洞****

除 VoIP 领域外，本次更新还涉及监控和通信平台的严重漏洞。新模块针对流行网络监控工具 Cacti，专门利用（CVE-2025-24367）。该漏洞影响 1.2.29 之前版本，允许通过图形模板机制进行未认证远程代码执行。鉴于 Cacti 在基础设施监控中的广泛使用，该模块成为网络管理员需优先测试的案例。

同时，框架新增了对 SmarterTools SmarterMail 中（CVE-2025-52691）的利用支持。这一未认证文件上传漏洞依赖于对 guid 变量的路径遍历操作。该模块显著特点是兼容不同操作系统：针对 Windows 目标时，漏洞利用会在 webroot 目录部署 webshell；针对 Linux 环境时，则通过创建 /etc/cron.d 定时任务实现持久化和执行。

**Part03**

## ****持久化工具与核心修复****

本次发布还通过新增持久化模块增强了攻击后能力。新的 Burp Suite 扩展持久化模块允许攻击者在专业版和社区版上安装恶意扩展，使其在用户启动应用时自动执行。此外，团队将 Windows 和 Linux 的 SSH 密钥持久化功能整合为统一模块以简化操作。

在维护方面，修复了若干关键错误。包括导致哈希数据与 John the Ripper 密码破解工具不兼容的格式问题，以及 SSH 登录扫描器中存在的逻辑错误（该错误曾将会话无法开启的成功登录误报为失败），现已修复以确保测试期间报告的准确性。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibdIDHM7Kns9672aia7ZlDr19d84ealfz5ZGFADfZ4BicXXhdMWA3AicpJ5hre5V8ttqbLouHPnN5O9w/640?wx_fmt=png&from=appmsg)

**参考来源：**

Metasploit Releases 7 New Exploit Modules covering FreePBX, Cacti and SmarterMail

https://cybersecuritynews.com/metasploit-exploit-modules/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvic9mib2trd1W0JGAJEHlF8tTYRNsg6a0FfibX0r25TSibsMNZQhtboVibXRZU0vs9tRR2kk7BHa4oFQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334591&idx=1&sn=7a53f598d945f86ed376200b93146133&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibnrQibOZyPeN5gojum7YiajavXr2P3enIq4nKL0Stc3jSz0aakk3cPwzllaKQuvWRJwmEdaUibF4fEA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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