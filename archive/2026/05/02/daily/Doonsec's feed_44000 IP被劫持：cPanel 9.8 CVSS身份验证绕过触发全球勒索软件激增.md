---
title: 44000 IP被劫持：cPanel 9.8 CVSS身份验证绕过触发全球勒索软件激增
url: https://mp.weixin.qq.com/s/kVyya5ryI-pI3Ff6qxANOA
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:23:51.097608
---

# 44000 IP被劫持：cPanel 9.8 CVSS身份验证绕过触发全球勒索软件激增

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/y1BJgHFkOkrSIibI3X95UMZC0JGcOVCn139e7sjNKgdvUaQ9lKKqDoNYhib1SCicn8oBYf2zc27rtEdlwFzL74omBfWkRoaDyFJuSXI0jq26gg/0?wx_fmt=jpeg)

# 44000 IP被劫持：cPanel 9.8 CVSS身份验证绕过触发全球勒索软件激增

sec随谈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

网络安全和基础设施安全局（CISA）发行；颁布；发出紧急警告，加上危急警告脆弱性在WebPros cPanel&WHM到其已知被利用的漏洞（KEV）目录。瑕疵，指定CVE-2026-41940CVSS的严重性评分为9.8，并允许攻击者绕过关键函数的身份验证。

活跃开采的证据越来越多。Shadowserver基金会报告的攻击大规模激增，指出至少44,000个与cPanel实例相关的IP地址可能被泄露，截至4月底，已被看到扫描蜜罐。

大约有150万个cPanel实例无保护的到互联网，活跃感染人数正在急剧上升。数据来自Censys揭示2026年5月1日发生的戏剧性转变：

\* 5月1日的高峰：新的恶意分类主机在一天之内增加了大约19,000台。
\* cPanel的角色：超过15000个新的恶意主机是cPanel系统，占全球恶意活动每日激增的近80％。
该漏洞源于登录和会话加载过程中的回车换行符（CRLF）注入缺陷允许攻击者在不验证密码的情况下登录系统，有效地授予他们对网站后端、webmail和数据库的管理员访问权限。

成功开采的后果是严重的。一旦攻击者获得访问权限，他们就可以控制托管帐户中的一切，从敏感文件到电子邮件数据库。最近的观察表明，脆弱性被用于两个主要目的：

1.勒索软件活动：Censys的分析师发现，大约7000台服务器上的文件被重新命名为“. Sorry”后缀--这是Sorry勒索软件（隐藏-撕裂变体）的标志。
2.僵尸网络扩张：未经证实的报告显示，该漏洞正被用于部署名为“nuclear.x86”的Mirai僵尸网络的变种。攻击者可以访问cPanel，可以控制托管帐户中的所有内容，从网站、数据到电子邮件。他们可以利用这些权限植入后门或web shell，将用户重定向到恶意位置，或窃取敏感文件。
WebPros已经发布了一个紧急更新来解决这个漏洞。由于漏洞的严重性，建议管理员不要等待标准的自动循环。

如何保护服务器：

\* 运行Force Update：管理员应该手动执行命令/scripts/upcp-Force。这迫使cPanel更新过程运行，即使系统认为它已经在最新版本上。
\* 验证版本：确保您的安装运行的是补丁版本之一，如11.136.0.5、11.132.0.29或11.126.0.54。
\* 不支持的版本：运行不支持的cPanel版本的服务器没有资格进行安全更新，必须立即升级到支持的版本。
联邦民事行政部门（FCEB）机构已被中钢协勒令在2026年5月3日前纠正这一缺陷。鉴于僵尸网络和勒索软件浪潮的移动速度，鼓励私营部门管理员遵循同样严格的截止日期。

预览时标签不可点

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