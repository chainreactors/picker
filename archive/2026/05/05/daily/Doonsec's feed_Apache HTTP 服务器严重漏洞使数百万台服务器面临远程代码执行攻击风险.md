---
title: Apache HTTP 服务器严重漏洞使数百万台服务器面临远程代码执行攻击风险
url: https://mp.weixin.qq.com/s/mWmqm0m1f8zbaV8xk3vY8g
source: Doonsec's feed
date: 2026-05-05
fetch_date: 2026-05-06T05:07:47.529935
---

# Apache HTTP 服务器严重漏洞使数百万台服务器面临远程代码执行攻击风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PLj3kbibuuHryAhcwBGcYHMsxJ6Z4dwn19j8YulH88jgLv8Zkgp0B7WUFPrV6jH4Hp6544fTJTZ3dUUvY0ozrjxicSb1xuy9qrc/0?wx_fmt=jpeg)

# Apache HTTP 服务器严重漏洞使数百万台服务器面临远程代码执行攻击风险

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Apache 软件基金会发布了针对Apache HTTP 服务器的关键安全更新，修复了五个漏洞，其中包括一个危险的双重释放漏洞，该漏洞可能在 2026 年 5 月 4 日发布的 2.4.67 版本中启用远程代码执行 (RCE)。强烈建议所有运行 2.4.66 或更早版本的用户立即升级。

五个漏洞中最严重的是 CVE-2026-23918，评级为“高”，CVSS 基本得分为 8.8。

该缺陷是 Apache HTTP/2 协议实现中在“早期流重置”序列期间触发的双重释放内存损坏错误。

当程序尝试两次释放同一内存区域时，就会发生双重释放漏洞，这会破坏堆内存结构，并可能使攻击者能够重定向执行流程，从而打开远程代码执行的大门。

该漏洞仅影响 Apache HTTP 服务器版本 2.4.66，最早由 striga.ai 的 Bartlomiej Dmitruk 和 isec.pl 的 Stanislaw Strzalkowski 于 2025 年 12 月 10 日向 Apache 安全团队报告。

修复程序`r1930444`于第二天，即 2025 年 12 月 11 日，在修订版中提交，公开补丁于 2026 年 5 月 4 日在 2.4.67 版本中发布。

第二个缺陷 CVE-2026-24072 被评为中等，针对的`mod_rewrite`是`ap_expr`表达式评估的使用。

该漏洞允许本地`.htaccess`作者以用户的权限读取任意文件`httpd`，从而有效地将权限提升到超出其预期访问级别之外。

该错误影响 Apache HTTP Server 2.4.66 及更早版本，由研究员 y7syeu 于 2026 年 1 月 20 日报告。

## **已修复其他漏洞**

在 2.4.67 版本更新中，还修复了另外三个严重程度较低的缺陷：

* **CVE-2026-28780** — 一个基于堆的缓冲区溢出漏洞`mod_proxy_ajp`。`ajp_msg_check_header()`如果`mod_proxy_ajp`连接到恶意 AJP 服务器，该服务器可以发送精心构造的 AJP 消息，导致该模块向堆缓冲区末尾写入 4 个由攻击者控制的字节。该漏洞由四位研究人员在 2026 年 2 月至 3 月期间独立报告。
* **CVE-2026-29168** — 的 OCSP 响应处理程序中存在一个未限制资源分配的漏洞`mod_md`。攻击者可以利用此漏洞，通过过大的 OCSP 响应数据耗尽服务器资源。该漏洞影响 2.4.30 至 2.4.66 版本，由 Aisle Research 的 Pavel Kohout 于 2026 年 3 月 2 日报告。
* **CVE-2026-29169** — 一个空指针解引用漏洞`mod_dav_lock`，攻击者可利用恶意构造的请求使服务器崩溃。值得注意的是，该漏洞`mod_dav_lock`在内部并未被 Apache Subversion 或 Apache Subversion 内部使用`mod_dav`——`mod_dav_fs`其唯一已知的使用案例是`mod_dav_svn`Apache Subversion 1.2.0 之前的版本。作为缓解措施，无法立即升级的管理员可以简单地移除该漏洞`mod_dav_lock`。

| CVE | 严重程度 | 成分 | 影响 | 受影响版本 |
| --- | --- | --- | --- | --- |
| CVE-2026-23918 | 高（CVSS 8.8） | HTTP/2 | 双倍免费/RCE | 仅限 2.4.66 版本 |
| CVE-2026-24072 | 中 | mod\_rewrite（ap\_expr） | 权限提升 | ≤ 2.4.66 |
| CVE-2026-28780 | 低的 | mod\_proxy\_ajp | 堆缓冲区溢出 | ≤ 2.4.66 |
| CVE-2026-29168 | 低的 | mod\_md（OCSP） | 资源耗尽 | 2.4.30–2.4.66 |
| CVE-2026-29169 | 低的 | mod\_dav\_lock | 空指针解引用/拒绝服务 | ≤ 2.4.66 |

## 缓解措施

鉴于 Apache HTTP 服务器在全球范围内的庞大部署规模，CVE-2026-23918 带来的远程代码执行 (RCE) 风险对全球企业基础设施构成重大威胁。管理员应立即采取以下措施：

1. **升级到 Apache HTTP Server 2.4.67** — 是唯一能够彻底修复所有五个漏洞的版本。
2. 如果立即升级不可行，则暂时**禁用 HTTP/2以减少 CVE-2026-23918 的风险。**
3. **`mod_dav_lock`**如果该模块未处于活跃使用状态，**则将其移除，作为 CVE-2026-29169 的临时缓解措施。**
4. **在本地用户访问受到关注的环境中，审核`.htaccess`权限**以限制 CVE-2026-24072 的暴露。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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