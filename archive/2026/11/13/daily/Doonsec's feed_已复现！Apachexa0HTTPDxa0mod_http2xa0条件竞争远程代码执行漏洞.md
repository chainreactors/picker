---
title: 已复现！Apachexa0HTTPDxa0mod_http2xa0条件竞争远程代码执行漏洞
url: https://mp.weixin.qq.com/s/MNLLUui1lNS1gyOeFAWJ6g
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:13:44.203199
---

# 已复现！Apachexa0HTTPDxa0mod_http2xa0条件竞争远程代码执行漏洞

# 已复现！Apache HTTPD mod\_http2 条件竞争远程代码执行漏洞

微步情报局
微步情报局

微步在线研究响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

漏洞概况

Apache HTTP Server 是 Apache 软件基金会开发的开源 Web 服务器，是全球部署最广泛的 HTTP 服务端之一。

近日，Apache HTTP Server官方发布通告，修复了Apache HTTP Server mod\_http2 assign\_headers() 竞争条件漏洞（CVE-2026-119618）。微步情报局已成功复现该漏洞。经分析，Apache HTTP Server mod\_http2 的 assign\_headers() 函数存在并发同步缺陷，多个线程并发访问共享资源时缺少适当同步，特定 HTTP/2 请求序列可触发竞态条件造成内存破坏，满足特定利用条件时，可造成远程代码执行。

（完整漏洞情报请查阅https://x.threatbook.com/v5/vul/XVE-2026-96011）

攻击者成功利用此漏洞可在受影响服务器上执行任意代码，亦可导致子进程崩溃、业务中断。建议受影响用户尽快修复。

漏洞处置优先级(VPT)

**综合处置优先级：**中风险

|  |  |  |
| --- | --- | --- |
| 基本信息 | 微步编号 | XVE-2026-96011 |
| CVE编号 | CVE-2026-119618 |
| 漏洞类型 | 远程代码执行（条件竞争） |
| 利用条件评估 | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 否 |
| 对被攻击系统的要求 | 需加载 mod\_http2 模块且 Protocols 配置包含 h2/h2c（仅提供 HTTP/1.1 的服务器不受影响） |
| 利用漏洞的权限要求 | 无须用户权限 |
| 是否需要受害者配合 | 否 |
| 利用情报 | 是否有POC | 是 |
| 已知利用行为 | 暂无 |

漏洞影响范围

|  |  |
| --- | --- |
| 产品名称 | Apache HTTP Server |
| 受影响版本 | 2.4.55<=version<=2.4.70 |
| 有无修复补丁 | 有 |

漏洞复现

目标为已运行的 Apache HTTP Server 2.4.70 且启用了 HTTP/2，发送特制的 HTTP/2 请求，竞态触发后 prefork 子进程在 apr\_allocator\_free 处 SIGSEGV

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdENyAicoerh1w86hhDyNicHrOBIOKlw5OpSctl0uVOr5mlzSm7AF3y3UrYPIrLM6gpgH7uajDLu4ic7KWreXHGZyYykgP5qIqiaDCNI/640?wx_fmt=png&from=appmsg)

修复方案

### 官方修复方案

官方已发布修复方案，请访问链接下载：
https://httpd.apache.org/download.cgi

### 临时缓解措施

1、在反向代理、负载均衡或 WAF 上对不可信来源禁用 HTTP/2（移除 h2/h2c，仅保留 http/1.1），或对短时间大量创建 HTTP/2 流、请求头数量接近上限的客户端限速/阻断

 2、禁用 HTTP/2 协议：在 Apache 配置中将协议限制为仅使用 HTTP/1.1，避免触发 `mod\_http2` / `mod\_h2` 漏洞路径。

 3、以低权限账户运行 httpd 子进程，限制 Web 根目录、配置文件和日志目录的写权限。

微步产品支撑

微步漏洞情报于2026-11-11收录该漏洞。

微步下一代威胁情报平台NGTIP及X情报中心已于漏洞收录时向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

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