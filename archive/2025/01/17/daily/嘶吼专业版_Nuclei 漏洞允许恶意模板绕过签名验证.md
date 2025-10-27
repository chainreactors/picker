---
title: Nuclei 漏洞允许恶意模板绕过签名验证
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580839&idx=1&sn=9bbf94cef195dc62ef4e9c2767e40736&chksm=e9146c9dde63e58b38dc1102ff184f3f04def7647e879875cf84eea98fd90bd0fb589e54a1ae&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-01-17
fetch_date: 2025-10-06T20:11:36.218392
---

# Nuclei 漏洞允许恶意模板绕过签名验证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29Sgp8iaMCnhMqNv8BTEu3YENFicYfUyUvIygeoQ4IXmvRPk8rROBpN54UFx7NOvNYoQRhjlFdeRSiaQ/0?wx_fmt=jpeg)

# Nuclei 漏洞允许恶意模板绕过签名验证

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

最新发现开源漏洞扫描器 Nuclei 中现已修复的漏洞可能允许攻击者绕过签名验证，同时将恶意代码潜入在本地系统上执行的模板中。

Nuclei 是 ProjectDiscovery 创建的一款流行的开源漏洞扫描程序，可扫描网站是否存在漏洞和其他弱点。该项目使用基于模板的扫描系统，该系统包含 10,000 多个 YAML 模板，可扫描网站是否存在已知漏洞、错误配置、暴露的配置文件、Webshell 和后门。

YAML 模板还包括一个代码协议，可用于在扩展模板功能的设备上本地执行命令或脚本。每个模板都使用摘要哈希进行“签名”，Nuclei 使用摘要哈希来验证模板是否未被修改以包含恶意代码。该摘要哈希以以下形式添加到模板的底部：

# digest:

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29Sgp8iaMCnhMqNv8BTEu3YEjya9CrZ6WdOZwESQkCiad2MR3kX7N2bJPwCzuHheSYOaruaTwsTB6vQ/640?wx_fmt=png&from=appmsg)漏洞绕过 Nuclei 签名验证

Wiz 研究人员发现了一个名为 CVE-2024-43405 的新 Nuclei 漏洞，即使模板被修改为包含恶意代码，该漏洞也会绕过 Nuclei 的签名验证。

该问题是由基于 Go 正则表达式的签名验证以及 YAML 解析器在验证签名时处理换行符的方式引起的。当验证签名时，Go 的验证逻辑将 \r 视为同一行的一部分。

但是，YAML 解析器将其解释为换行符。这种不匹配允许攻击者注入绕过验证但在 YAML 解析器处理时仍会执行的恶意内容。另一个问题是 Nuclei 如何处理多个 #digest: 签名行，因为该过程仅检查模板中第一次出现的 #digest:，而忽略模板中稍后发现的任何其他内容。

可以通过在包含恶意“代码”部分的初始有效摘要之后添加额外的恶意“#digest:”有效负载来利用此漏洞，然后在使用模板时注入并执行该有效负载。

Wiz 研究员解释说：“有了关于不匹配换行符解释的见解，我们制作了一个模板，利用 Go 的正则表达式实现和 YAML 解析器之间的差异。通过使用 \r 作为换行符，可以在模板中包含第二个 # 摘要：行，该行可以逃避签名验证过程，但由 YAML 解释器解析并执行。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29Sgp8iaMCnhMqNv8BTEu3YEoUDMVoxrhiaTEFFMdER6PF3FMwk4sic0rJX1A7U0JQreMRibvhNYJ2Lwg/640?wx_fmt=png&from=appmsg)

不同解析器如何解析 Nuclei 模板的示例

Wiz 于 2024 年 8 月 14 日向 ProjectDiscovery 披露了该漏洞，并于 9 月 4 日在 Nuclei v3.3.2 中对其进行了修复。如果使用的是旧版本的 Nuclei，安全研究人员强烈建议用户更新最新版本。此外，Goldenberg 还建议在虚拟机或隔离环境中使用 Nuclei，以防止恶意模板的潜在利用。

参考及来源：https://www.bleepingcomputer.com/news/security/nuclei-flaw-lets-malicious-templates-bypass-signature-verification/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29Sgp8iaMCnhMqNv8BTEu3YEByZv6dvZn9uYntTnnByzSh05ticBicnHNj4s7FWN4rtdfQJ7qcrK0fRA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29Sgp8iaMCnhMqNv8BTEu3YEgdyCQWibVr37Sab1hE5Z1ibjsOBNErRwpy4fJJTlPPN9xT4DCHJIy58Q/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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