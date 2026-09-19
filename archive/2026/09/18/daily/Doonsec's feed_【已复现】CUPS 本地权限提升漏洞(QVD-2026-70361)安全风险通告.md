---
title: 【已复现】CUPS 本地权限提升漏洞(QVD-2026-70361)安全风险通告
url: https://mp.weixin.qq.com/s/HnPHtleUt3p-k0Ri6bO0_A
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:57:08.307558
---

# 【已复现】CUPS 本地权限提升漏洞(QVD-2026-70361)安全风险通告

# 【已复现】CUPS 本地权限提升漏洞(QVD-2026-70361)安全风险通告

原创

奇安信 CERT
奇安信 CERT

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | CUPS 本地权限提升漏洞 | | |
| **漏洞编号** | QVD-2026-70361 | | |
| ****公开时间**** | 2026-09-17 | ****影响量级**** | 十万级 |
| **奇安信评级** | **高危** | **CVSS 3.1分数** | **7.8** |
| **威胁类型** | 权限提升 | **利用可能性** | ****高**** |
| **POC状态** | **已公开** | **在野利用状态** | 未发现 |
| **EXP状态** | **已公开** | **技术细节状态** | **已公开** |
| **危害描述：**攻击者可完全绕过身份认证边界，将 lpadmin 组权限提升为 root，获取交互式 root shell，进而完全控制主机、读取/篡改任意数据、安装持久化后门或横向移动。PoC 会自动恢复被修改的 CUPS 配置并清理队列与本地工件，隐蔽性较强。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

CUPS 是 OpenPrinting 维护的开源打印系统，是 Linux/Unix 平台事实上的打印服务标准，组件包括调度进程 cupsd、过滤器/后端框架以及 Web 管理界面；cups-filters 提供 serial、parallel 等后端。除桌面打印场景外，CUPS 还广泛部署于多用户主机、共享开发机、CI Runner 与打印服务器，常以 root 权限运行 cupsd 并提供本地打印管理接口。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到CUPS 本地权限提升漏洞(QVD-2026-70361)，该漏洞源于利用链将多个配置与权限边界缺陷串联：具备 lpadmin 组成员的本地攻击者首先利用以 root 权限运行的 serial 后端改写 /etc/cups/cups-files.conf，再通过畸形 IPP 订阅请求使 cupsd 崩溃并由 systemd 自动重启，从而以攻击者控制的 ServerBin 目录重启服务，最终由 cupsd 以 root 身份执行被替换的 cups-exec，获得交互式 root shell。目前该漏洞PoC和技术细节已公开。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**>****>****>****>**

**利用条件**

1. 本地账号且属于 lpadmin 组；目标使用 systemd；

2. 本地 CUPS 服务活跃；

3. 存在以 root 运行的特权 serial 后端。

**02**

**影响范围**

**>****>****>****>**

**影响版本**

Ubuntu 26.04 LTS（cups 2.4.16-1ubuntu1.3、cups-filters 2.0.1-0ubuntu4.1）；PoC 自述支持 AMD64/ARM64。其他满足“systemd + 本地 CUPS 服务 + 特权 serial 后端 + 标准 Ubuntu CUPS 路径”条件的 Ubuntu/Debian 发行版可能同样受影响。

**03**

**复现情况**

目前，奇安信CERT已成功复现CUPS 本地权限提升漏洞(QVD-2026-70361)，截图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RwAbCjh555vZ1T2DTia2DL6O2Q1YAkXxxOknAibuT4D54BfskTWy3L3TeMPPgeItGnxq7HnbKLCrp2SPZEZcRfwGuNnGM5MichmsB1mx9yQHKA/640?wx_fmt=png&from=appmsg)

**04**

**受影响资产情况**

奇安信鹰图资产测绘平台数据显示，CUPS 本地权限提升漏洞(QVD-2026-70361)关联的国内风险资产总数为30511个，关联IP总数为28139个。国内风险资产分布情况如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RwAbCjh555stZECNlx1gPWCpYiby3VdHJJMvWEurH1Vly4hIa7M49frG3y7Zls9IECEJIic2icntKfdhEo1Jt2bUnpWDUO63MXJEDYMMtDBzQc/640?wx_fmt=png&from=appmsg)

CUPS 本地权限提升漏洞(QVD-2026-70361)关联的全球风险资产总数为183759个，关联IP总数为179797个。全球风险资产分布情况如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RwAbCjh555s1KQibo3zZuGQgdKxY9F9AApUjTmcVrofXfMwjdvXMBNhZcF5WSo3seZuj9Et8YlTwKnVqiavuqUkBfiaReOmoMZ3XEvkhotYpqs/640?wx_fmt=png&from=appmsg)

**05**

**处置建议**

**>****>****>****>**

**安全更新**

截至 2026 年 9 月 18 日，上游 OpenPrinting 与各发行版尚未发布针对该利用链的安全公告、CVE 编号或补丁。建议持续关注以下渠道，并在补丁发布后第一时间更新：

https://github.com/OpenPrinting/cups/security/advisories

https://github.com/OpenPrinting/cups-filters/security/advisories

临时缓解措施：

1. 收紧 lpadmin 权限：审计并清理 lpadmin 组成员，仅保留可信管理员；getent group lpadmin。

2. 处置特权 serial 后端：不需要串口打印的主机可卸载 cups-filters 对应的 serial 后端或移除后端文件；仅在必要时保留，并配合 AppArmor 等强制访问控制限制 cupsd 对 /etc/cups、/etc/cups/interfaces 的写入。

3. 审计打印队列：使用 lpstat -v/检查 printers.conf，排查设备 URI 指向 serial:/ 且路径不是真实串口设备（如指向 /etc/cups/...）的队列，发现后立即删除。

**06**

**参考资料**

[1]https://github.com/v12-security/pocs/tree/main/cups/cups2root

**07**

**时间线**

2026年09月18日，奇安信 CERT发布安全风险通告。

**08**

**漏洞情报服务**

「奇安信漏洞情报平台」重磅上线，诚邀您来体验：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555tBKsRia72Pcf1aYd3Rk1ob68jleJ2tfrs5v07her5iaM5bFQj6PdxZqjZPVbgUG3ylv8YQEpVPhEQzbkiaoZU0PZjjFxibeTIZibNM/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tG2LbK7WG3tezJEzJsicLSWCGsIggLbcfk4LB5WK7pdSwMksxPOAoHuibjQpBlEId4nyIIw52n2J8N8MowYZcjA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=3)

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BYBVaibvBq1vXprZIc191LXKibdiaApA16q3UgmibQDv4yW09qT88J3jRUfA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=4 "CERT LOGO.png")

**奇安信 CERT**

**致力于**第一时间为企业级用户提供**权威**漏洞情报和**有效**解决方案。

点击↓**阅读原文**，到**ALPHA威胁分析平台**订阅更多漏洞信息。

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