---
title: RustFS 控制台中的存储型 XSS 漏洞使 S3 管理员凭据面临风险
url: https://mp.weixin.qq.com/s/vUyr5vL2luaPJPOIxc8cPw
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:22:25.744949
---

# RustFS 控制台中的存储型 XSS 漏洞使 S3 管理员凭据面临风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7Orh8Tg2OGJPeBP4M7IDmy28nCGJxwD5Cmet4bVibXdWzr7q6xXCDwyYt0MOjianuiac31cyv5dK3EdNGibWL4CAvfU6LGvcyrp4ks/0?wx_fmt=jpeg)

# RustFS 控制台中的存储型 XSS 漏洞使 S3 管理员凭据面临风险

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

RustFS 控制台中发现了一个严重的安全漏洞，使管理员面临账户被盗用的高度风险。

该存储型跨站脚本 (XSS) 漏洞被追踪为 CVE-2026-27822，其CVSS v3 评分为 10.0，属于严重漏洞，影响 Rust 软件包 1.0.0-alpha.82 之前的版本。

该漏洞允许攻击者在管理控制台的上下文中执行任意 JavaScript 代码，从而可能导致系统完全被攻陷。

该漏洞源于两个主要问题：文件预览期间对响应内容类型的验证不当，以及 S3 对象交付和管理控制台之间缺乏源分离。

RustFS 通常将管理控制台和S3 API 托管在同一源（IP 和端口）上。这种设置会造成同源漏洞。

| 技术指标 | 漏洞详情 |
| --- | --- |
| **CVE ID** | CVE-2026-27822 |
| **GitHub 安全公告** | GHSA-v9fg-3cr2-277j |
| **漏洞类型** | 存储型跨站脚本攻击（XSS） |
| **已打补丁版本** | 1.0.0-alpha.83 |
| **严重程度评分** | 关键（/10） |

当预览文件时，应用程序会 `<iframe>` 根据文件扩展名渲染内容。但是，它未能严格验证实际提供的内容类型。

## **攻击机制**

RustFS 控制台将高度敏感的 S3 凭据（包括 AccessKey、SecretKey 和 SessionToken）不安全地存储在浏览器中 `localStorage`。

由于 `<iframe>` 预览窗口与控制台本身位于同一源，因此在该窗口内执行的任何脚本都可以不受限制地访问父窗口的数据。

根据 RustFS 的说法，攻击者可以通过上传恶意文件来利用这一点，例如，上传一个包含 JavaScript 的 HTML 文件，但将其命名为带有 `.pdf` 扩展名的文件。

至关重要的是，攻击者必须将文件的 `Content-Type` 元数据设置为 `text/html`。当管理员尝试预览这个看似无害的 PDF 文件时，浏览器会将内容解释为 HTML 并执行嵌入的 JavaScript。

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7OwZQAIedKenurSbP0ficakQOQVswDWSbAoWwvNtqiaTU2ibniaKEhICVvaZlgvDWCzwHjP1neJTp7Ymjb0V0r24yBPib5oYkGLVqPM/640?wx_fmt=jpeg)

概念验证 (PoC) 证明了这种攻击的简单性。

1. 攻击者创建类似这样的有效载荷 `<script>alert('XSS Success!\nLocalStorage Data: ' + JSON.stringify(window.parent.localStorage));</script>`。
2. 他们将此文件上传到目标存储桶，确保文件名是 `xss.pdf` ，属性是 `--attr "Content-Type=text/html"`。
3. 当管理员登录 RustFS 控制台并点击“预览”时 `xss.pdf`，JavaScript 会执行，立即窃取 `localStorage` 包含管理员凭据的数据。

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