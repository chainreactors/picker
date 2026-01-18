---
title: Firefox 147发布时修复了16个允许任意代码执行的漏洞
url: https://mp.weixin.qq.com/s/rzd1vTKvrVuCpUprR1lwlQ
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:34:23.271717
---

# Firefox 147发布时修复了16个允许任意代码执行的漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo49E74BLfrEBM3Nko9RBqsZMtlj5khrxZYs99BJUdtbKlIpccYa2YesJN12RuBnoQl0uzfByzbIoA/0?wx_fmt=jpeg)

# Firefox 147发布时修复了16个允许任意代码执行的漏洞

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo49E74BLfrEBM3Nko9RBqsZiahDV6k6P3AW3Z8IY3JZ3XmjrFzSyqKSyMDmmvJSLd9OFS3qJJz4L3w/640?wx_fmt=jpeg&from=appmsg)

Firefox 147于2026年1月12日发布，修复了16个安全漏洞，其中包括6个高危漏洞，主要涉及沙箱逃逸和内存安全问题，建议所有用户立即更新以防止潜在的任意代码执行攻击。

## 一、漏洞概览与核心修复

### 1. 漏洞统计与严重性分布

| 严重程度 | 漏洞数量 | 主要类型 |
| --- | --- | --- |
| 高危 (High) | 6 | 沙箱逃逸、内存破坏、DOM绕过 |
| 中危 (Moderate) | 7 | 信息泄露、释放后重用（Use-after-free） |
| 低危 (Low) | 3 | 拒绝服务、界面欺骗 |

此次更新主要修复了六个高影响漏洞（CVE-2026-0877至CVE-2026-0882），这些漏洞可能被利用来实现沙箱逃逸，从而在用户的设备上执行任意代码。此外，还修复了包括CVE-2026-0891和CVE-2026-0892在内的多个内存安全漏洞4。

### 2. 关键高危漏洞技术细节

* **CVE-2026-0877**：DOM安全组件中的缓解措施绕过漏洞，允许攻击者绕过同源策略限制
* **CVE-2026-0878至CVE-2026-0880**：Graphics和CanvasWebGL组件中的边界条件和整数溢出漏洞，可导致沙箱逃逸
* **CVE-2026-0881**：消息系统组件中的沙箱逃逸漏洞，可能被用于进程间通信攻击
* **CVE-2026-0882**：IPC（进程间通信）组件中的释放后重用（Use-after-free）漏洞

特别值得注意的是，**CVE-2026-0891和CVE-2026-0892**是两个已被证实存在内存破坏问题的漏洞，Mozilla的fuzzing团队已观察到内存损坏的迹象，表明这些漏洞可能被利用。这些漏洞主要影响JavaScript引擎和图形渲染组件14。

## 二、受影响产品与修复范围

### 1. 受影响产品矩阵

| 产品 | 受影响版本 | 修复版本 |
| --- | --- | --- |
| Firefox | 146及更早版本 | 147 |
| Firefox ESR | 140.6及更早版本 | 140.7 |
| Thunderbird | 146及更早版本 | 147 |
| Thunderbird ESR | 140.6及更早版本 | 140.7 |

### 2. 漏洞发现来源

此次修复的漏洞主要通过以下渠道发现：

* **外部研究人员**：Oskar L.报告了3个高危沙箱逃逸漏洞
* **Mozilla fuzzing团队**：通过自动化测试发现了内存安全漏洞
* **社区报告**：Andrew McCreight、Randell Jesup等安全研究员提交了多个漏洞

## 三、技术背景与安全机制

Firefox采用多进程架构和沙箱机制来隔离不同组件，防止恶意代码访问系统资源。然而，此次修复的多个“沙箱逃逸”（Sandbox Escape）漏洞表明，攻击者可能通过精心构造的网页内容，利用这些漏洞突破沙箱的隔离限制，从而在用户的设备上执行任意代码。

沙箱逃逸通常涉及利用浏览器引擎中的内存破坏漏洞。例如，通过JavaScript触发内存错误，攻击者可能获得在内存中执行任意代码的能力，进而完全控制浏览器进程，甚至可能提升权限控制整个系统14。

## 四、更新建议与最佳实践

### 1. 立即更新方案

* **普通用户**：通过"帮助→关于Firefox"检查并安装更新，或访问

  官方下载页面
* **企业环境**：通过组策略部署更新，使用policies.json配置自动更新策略
* **Linux用户**：注意，Firefox 147 版本也修复了自2003年起报告的、与Linux系统文件目录相关的长期问题（Bug 259356），该问题存在已超过20年1820。

### 2. 临时缓解措施

* 禁用不必要的浏览器扩展，特别是那些需要高级权限的扩展
* 避免访问不可信网站，特别是包含复杂WebGL内容的站点
* 不要下载和运行来源不明的文件

### 3. 企业安全策略建议

* **实施应用控制**：使用如Windows Defender Application Control (WDAC)等工具，仅允许执行经过签名验证的代码，阻止未经授权的脚本和可执行文件。
* **启用强化跟踪保护**：在Firefox中启用“增强跟踪保护”(ETP)，该功能在“严格”模式下会默认阻止许多可能用于攻击的第三方内容19。
* **定期安全审计**：检查浏览器扩展和用户配置文件，确保没有异常活动

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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