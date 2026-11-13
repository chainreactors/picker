---
title: 工信部漏洞库：关于防范Node.js越界写入超危漏洞的风险提示
url: https://mp.weixin.qq.com/s/LpfRgo2RGZfpRbvJIS7Psw
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:03:30.558546
---

# 工信部漏洞库：关于防范Node.js越界写入超危漏洞的风险提示

# 工信部漏洞库：关于防范Node.js越界写入超危漏洞的风险提示

华盟信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

可被未经身份验证的攻击者利用，破坏进程内存，进而导致程序崩溃、进程内存信息泄露或远程代码执行。

近日，工业和信息化部网络安全威胁和漏洞信息共享平台（NVDB）监测发现，Node.js存在越界写入超危漏洞，危害严重。

Node.js是一个开源的JavaScript运行环境，广泛用于Web服务器构建及命令行工具编写。其内置的Brotli解码器存在越界写入漏洞，可被未经身份验证的攻击者利用，破坏进程内存，进而导致程序崩溃、进程内存信息泄露或远程代码执行。当前仍处于维护期内的受影响版本包括：22.x系列＜22.23.4、24.x系列＜24.22.1、26.x系列＜26.12.1。

目前，Node.js项目团队已修复上述漏洞并发布安全公告（URL链接：https://nodejs.org/zh-cn/blog/vulnerability/october-2026-security-releases）。建议相关单位和用户立即开展全面排查，及时升级至最新安全版本，消除网络安全隐患。

文章来源：网络安全威胁和漏洞信息共享平台

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kZ8oAGNeUuj6mOI5YlyeqpmfFDmlWrhDUPtdowLH0Fe1bbFYw5foqQqLA333icDSHCp2490tNgrcOArofX5wjWw/0?wx_fmt=png)

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