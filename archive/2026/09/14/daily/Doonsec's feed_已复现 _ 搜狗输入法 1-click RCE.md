---
title: 已复现 | 搜狗输入法 1-click RCE
url: https://mp.weixin.qq.com/s/m-alNYyQLozh3Nqc8uRrwA
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T06:56:46.485183
---

# 已复现 | 搜狗输入法 1-click RCE

# 已复现 | 搜狗输入法 1-click RCE

原创

微步情报局
微步情报局

微步在线研究响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

漏洞概况

搜狗输入法（搜狗拼音输入法）是北京搜狗科技有限公司开发的中文输入法（IME）软件，负责将用户输入的拼音、五笔、语音或手写内容转换为汉字候选，并把选中的文字送入微信、浏览器、Word 等应用。

近日，微步情报局监测到互联网披露了搜狗输入法远程代码执行漏洞（CVE-2026-51990）。微步情报局已成功复现该漏洞。经分析，Windows 版搜狗输入法存在由自定义协议处理缺陷触发的远程代码执行链，远程攻击者可构造恶意 sgbiz: 链接注入启动参数，迫使内置浏览器访问恶意网页，进而执行任意代码。（完整漏洞情报请查阅https://x.threatbook.com/v5/vul/XVE-2026-62927）

攻击者仅需诱导受害者点击一次恶意链接，即可执行任意代码；该攻击已被 UNC3569 用于投放 GRAYRABBIT 后门。建议受影响用户尽快修复。

漏洞处置优先级(VPT)

**综合处置优先级：**高风险

|  |  |  |
| --- | --- | --- |
| 基本信息 | 微步编号 | XVE-2026-62927 |
| CVE编号 | CVE-2026-51990 |
| 漏洞类型 | 远程代码执行 |
| 利用条件评估 | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 否 |
| 对被攻击系统的要求 | Windows 操作系统 |
| 利用漏洞的权限要求 | 无须用户权限 |
| 是否需要受害者配合 | 是 |
| 利用情报 | 是否有POC | 是 |
| 已知利用行为 | 是，已被 UNC3569 用于投放 GRAYRABBIT 后门 |

漏洞影响范围

|  |  |
| --- | --- |
| 产品名称 | 搜狗拼音输入法 |
| 受影响版本 | version<16.3.0.3498 |
| 有无修复补丁 | 有 |

漏洞复现

点击特殊构造的sgbiz: 链接，成功在搜狗内嵌chromium中触发v8nday漏洞，弹出计算器，实现任意代码执行。

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEOQjVx8icsyNxswWkQNwOp12cyBqFEdOda8w0pH5BKYXBam5oFAbfJgjiaShwEYhmLunjtusHh9W2B44SCyuib5Tj9EpSzhJeQENg/640?wx_fmt=png&from=appmsg)

修复方案

### 官方修复方案

官方已发布新版本，请访问链接下载：

https://shurufa.sogou.com/windows

微步产品支撑

微步漏洞情报于2026-09-14收录该漏洞。

微步下一代威胁情报平台NGTIP及X情报中心已于漏洞收录时向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。

当前OneSEC已支持CVE-2026-51990检测，可关注告警规则ID：1994

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEMibHdNrtXW6RsNF8IGdgoqgdAMibIfenPQ7iawx2Ler9haTXIa51jHz05x9ibxkC1wPhD4RpklXu3VnvcpQ3WMWRLmjDK0ZzQOTPY/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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