---
title: SQL 到 SSH：Grafana 中存在严重 CVSS 9.1 级远程代码执行漏洞，可将监控变成远程劫持
url: https://mp.weixin.qq.com/s/06Wx8xZAZJSBfcrdg2ZktA
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:34:39.052065
---

# SQL 到 SSH：Grafana 中存在严重 CVSS 9.1 级远程代码执行漏洞，可将监控变成远程劫持

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/y1BJgHFkOkqBwaPpwOsIJr9B3iadako6B643LTMxWPdvWMmmfYWibXbUo9I5CU3oyvEbrjISKBhPHaUlmBZWa3XzwkzB6XvYkgdzRdtogxPYw/0?wx_fmt=jpeg)

# SQL 到 SSH：Grafana 中存在严重 CVSS 9.1 级远程代码执行漏洞，可将监控变成远程劫持

sec随谈
sec随谈

sec随谈

![]()

在小说阅读器中沉浸阅读

Grafana 团队发布紧急安全公告，披露了两个重大**漏洞**，攻击者可利用这些漏洞劫持服务器或导致实例崩溃。此次发布的 Grafana 12.4.2版本，以及针对12.3、12.2、12.1和11.6版本的补丁，修复了一个严重的远程代码执行 (RCE) 漏洞和一个高危拒绝服务 (DoS) 漏洞。

建议安全团队“尽快安装新发布的版本”，以保护其监控基础设施。

最严重的威胁，编号为CVE-2026-27876 (CVSS 9.1)，存在于 Grafana 的 SQL 表达式功能中。该工具旨在帮助用户使用熟悉的 SQL 语法转换查询数据，但其处理文件写入的方式存在**缺陷**，使其成为一个危险的入口点。

根据该公告：

> “然而，这种语法也允许向文件系统写入任意文件，从而可以将多个攻击向量串联起来，实现远程代码执行。”

攻击原理：

* 要求：攻击者只需要查看者权限或更高权限即可执行数据源查询。
* 漏洞利用：通过启用 sqlExpressions 功能开关，攻击者可以覆盖 Sqlyze 驱动程序或创建恶意 AWS 数据源配置文件。
* 结果：成功利用该漏洞可以建立与 Grafana 主机的完整 SSH 连接。

第二个漏洞CVE-2026-27880（CVSS 7.5）针对 Grafana 的 OpenFeature 端点。这些端点目前不需要身份验证，更重要的是，它们接受“无限制的用户输入”。

由于此输入直接读取到内存中，未经身份验证的攻击者可以通过发送大量请求耗尽所有可用系统内存，从而使服务器崩溃。此**漏洞**影响 v12.1.0 及更高版本。

对所有管理员的首要建议是完全升级到最新的补丁版本。但是，对于无法立即更新的用户，我们提供以下几种替代方案：

| **漏洞** | **缓解方案** |
| --- | --- |
| **CVE-2026-27876**（远程代码执行） | • 关闭`sqlExpressions`功能开关。  • 将 Sqlyze 更新到 v1.5.0 或禁用它。  • 禁用所有已安装的 AWS 数据源。 |
| **CVE-2026-27880**（拒绝服务攻击） | • 在具有自动重启功能的高可用性环境中部署 Grafana 。  • 使用反向代理（如 Nginx 或 Cloudflare）来限制输入有效负载的大小。 |

管理员应注意，虽然这些变通方法可以降低风险，“但它们可能会对 Grafana 用户造成干扰，并且不能完全修复漏洞”。

参考链接:

https://grafana.com/blog/grafana-security-release-critical-and-high-severity-security-fixes-for-cve-2026-27876-and-cve-2026-27880/

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaYUeYwA2bziakiaSIiab3gicgEN5oibyibqGbjykE3b4sDfuWj0RZXsWhP7mg3YaIjklIlBbHxma0EZ5WicksaTehmL4g/0?wx_fmt=png)

sec随谈

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