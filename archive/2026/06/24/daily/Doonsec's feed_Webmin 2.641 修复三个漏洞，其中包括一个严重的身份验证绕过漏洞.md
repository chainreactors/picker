---
title: Webmin 2.641 修复三个漏洞，其中包括一个严重的身份验证绕过漏洞
url: https://mp.weixin.qq.com/s/NL2Oa8h__B4pquR5ppN9NQ
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:05:52.074521
---

# Webmin 2.641 修复三个漏洞，其中包括一个严重的身份验证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/y1BJgHFkOkok1IRLicibaR83rlBUulnZUAibiarDlAnRzON5dONYzQFxz2ecrQJoat8nJS4b71jibsnXesqg71sPTly4M6icckrrP4aTMeRwMeGMw/0?wx_fmt=jpeg)

# Webmin 2.641 修复三个漏洞，其中包括一个严重的身份验证绕过漏洞

sec随谈
sec随谈

sec随谈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**简要概述**

Webmin 发布了 2.641 版本，修复了三个安全漏洞。其中最严重的一个允许未经身份验证的攻击者冒充任意用户。另外两个漏洞可绕过多因素认证（MFA）并暴露配置文件。目前尚未发现公开的漏洞利用案例。

---

**为何值得关注**

Webmin 是运行在类 Unix 服务器上的基于 Web 的管理面板，每年估计安装量达 100 万次。因此，一个漏洞就可能让攻击者控制大量系统。该工具管理着用户、服务、DNS 服务器和数据库，一旦被攻破，整个技术栈都将面临风险。此外，管理面板处于服务器信任体系的核心位置，进一步提升了威胁等级。

---

**攻击方式**

**CVE-2026-56020（CVSS 9.2）**

Webmin 的 HTTP 服务器 miniserv.pl 会信任伪造的 HTTP 头部。因此，远程攻击者可以伪造证书 DN，无需凭据即可以任意已配置用户的身份进行身份验证。这是本次最严重的漏洞。

**CVE-2026-56022（CVSS 6.9）**

通过构造 `User-Agent: webmin` 头部，可使 Webmin 在没有会话 Cookie 的情况下接受基本认证，从而绕过额外的 MFA 检查。

**CVE-2026-56021（CVSS 6.9）**

由于正则表达式存在绕过缺陷，未经身份验证的用户可读取模块目录中任意以 `.conf` 结尾的文件，进而获取配置信息和敏感凭据。

---

**受影响版本**

上述三个漏洞均影响 2.641 版本之前的所有 Webmin 发行版，且在默认配置下即可触发，并非仅限于特殊配置场景。详细信息可参阅官方安全公告。

---

**补丁与缓解措施**

请立即升级至 Webmin 2.641，该版本已修复上述全部三个漏洞，可从官方发布页面获取。目前没有可替代补丁的独立缓解方案，请尽快完成升级。在升级之前，建议限制对 Webmin 端口的网络访问，同时监控日志中异常的 User-Agent 字符串及意外的证书登录行为。

参考链接：

https://webmin.com/security/#webmin-prior-to-2641

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaYUeYwA2bziakiaSIiab3gicgEN5oibyibqGbjykE3b4sDfuWj0RZXsWhP7mg3YaIjklIlBbHxma0EZ5WicksaTehmL4g/0?wx_fmt=png)

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