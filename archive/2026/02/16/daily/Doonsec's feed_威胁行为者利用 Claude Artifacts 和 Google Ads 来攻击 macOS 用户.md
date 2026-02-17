---
title: 威胁行为者利用 Claude Artifacts 和 Google Ads 来攻击 macOS 用户
url: https://mp.weixin.qq.com/s/HylmDA76a2G2Dwx3S7iNwQ
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:17:12.331991
---

# 威胁行为者利用 Claude Artifacts 和 Google Ads 来攻击 macOS 用户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7OR6Pib1AUibaZnujVRFptYgugaH09kQJA81x0Wx4J8mTMictibKFAJ0kibqNqO17ia2b3bicick1lyJUSh08BCJcygrxNd4oYZYYLIYR0/0?wx_fmt=jpeg)

# 威胁行为者利用 Claude Artifacts 和 Google Ads 来攻击 macOS 用户

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

一场精心策划的恶意软件活动，通过谷歌赞助的搜索结果和合法平台（包括Anthropic 的 Claude AI和 Medium）针对 macOS 用户。

该攻击活动已经通过两种不同的攻击变种，利用用户对现有在线服务的信任，影响了超过 15,000 名潜在受害者。

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PWsw2JiaibLpyd0ag0FfE65KbLuWFDOI5HWTGffgxYkZpltv38WhINLn2s29yPcph7Cmp2iaYR7m7nibtpaR2oxQNiaLGiaXm9cnmvU/640?wx_fmt=jpeg)

第一种攻击途径利用 Google Ads 来推广伪装成合法 macOS 安全指南的恶意 Claude AI 程序。

当用户搜索“在线 DNS 解析器”时，他们会遇到一个赞助链接，该链接会将他们引导至一个名为“macOS 安全命令执行”的 Claude 公共项目。

这篇虚假指南指示用户将一条经过 base64 编码的命令粘贴到终端应用程序中。该命令会解码并执行一个恶意 shell 脚本，该脚本会下载MacSync 信息窃取恶意软件。

一旦执行，该恶意软件就会使用硬编码的身份验证令牌和 API 密钥与其位于 a2abotnet[.]com/dynamic 的命令和控制服务器建立通信。

为了逃避检测，该恶意软件会伪造合法的 macOS 浏览器 User-Agent 字符串，使其网络流量看起来像是正常的网页浏览活动。

该有效载荷会获取一个 AppleScript 组件，该组件会执行实际的数据窃取操作，目标是敏感信息，例如钥匙串凭证、浏览器数据和加密货币钱包文件。

Moonlock Lab 的网络安全研究人员发现，被盗数据在通过 HTTP POST 请求泄露到 a2abotnet[.]com/gate 之前，会被压缩到 /tmp/osalogging.zip 中。

该恶意软件包含复杂的重试机制来处理大数据传输，包括分块上传（最多可尝试 8 次重试）和指数退避。数据传输成功后，该恶意软件会删除暂存文件以掩盖其踪迹。

第二种攻击变种的目标是通过 apple-mac-disk-space.medium[.]com 上发布的 Medium 文章，攻击搜索“macos cli disk space analyzer”的用户。

本文冒充苹果官方支持团队，并采用了与ClickFix 相同的社会工程学手法。然而，此变种使用了双层编码和不同的托管基础设施。

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PTp9OZuGnukFh05lWuLxkFNyfW6IY8y2nVCQj4vsbT67PqfKFQn4iczQ0WDg6UaDgicXONBicILE4714uojRjicvjsiaXVtpWN8cpk/640?wx_fmt=jpeg)

该恶意命令使用字符串连接技巧（cur””l 而不是 curl）来绕过简单的模式匹配检测系统和 YARA 规则。

这两种变种都体现了威胁行为者滥用合法平台和可信服务来传播恶意软件的日益增长的趋势。

利用谷歌广告传播恶意软件凸显了验证来源的重要性，即使这些来源出现在赞助搜索结果中也是如此。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7OH5ZCNW1txPbCjeE1k3s8LVzm5Ar8M9niceavne6agEK28pb77J941NUic7wlsW4TnN1BicEX0UfvJE9hYf7Cnnz6qxBicMjNvj4c/640?wx_fmt=jpeg)

用户在从任何在线来源复制和执行终端命令时都应格外谨慎，无论该平台看起来多么合法。

建议 macOS 用户避免执行来自未知来源的终端命令。对于声称来自 Apple 或其他可信供应商的支持文章，应核实其真实性。

组织应实施终端检测解决方案，该方案能够监控可疑的终端活动以及与未知命令和控制服务器的网络连接。

**IOCs**

| 指标类型 | 指标 | 描述 |
| --- | --- | --- |
| 领域 | a2abotnet[.]com | 命令与控制服务器 |
| 领域 | raxelpak[.]com | 有效载荷托管域 |
| 领域 | apple-mac-disk-space.medium[.]com | 伪造的苹果支持文章 |
| 文件路径 | /tmp/osalogging.zip | 用于存放被盗数据的暂存文件 |
| 恶意软件 | MacSync | 针对 macOS 的信息窃取程序 |

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