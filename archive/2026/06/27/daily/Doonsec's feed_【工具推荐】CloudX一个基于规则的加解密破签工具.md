---
title: 【工具推荐】CloudX一个基于规则的加解密破签工具
url: https://mp.weixin.qq.com/s/eGJ5SBAoq3YoyPhzPKYoLQ
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:09:54.823469
---

# 【工具推荐】CloudX一个基于规则的加解密破签工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DRNXoxlicJJvtpyuiaJjE47nh981FCyEoIjaRPZKPeHjXapP38ODK6ZBQD96arFBUYlDueXCDicDciaJEfQXUXzeMtt9MdBCyk4HlhF9XQ4wJOc/0?wx_fmt=jpeg)

# 【工具推荐】CloudX一个基于规则的加解密破签工具

原创

CatalyzeSec
CatalyzeSec

CatalyzeSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 工具介绍

CloudX 是一款面向 Burp Suite 的加解密与签名破解插件，基于 Montoya API 开发。核心思路是将渗透测试中遇到的加密请求、签名校验、防重放机制等场景抽象为可配置的处理规则，由插件在流量经过 Burp 时自动完成解密展示与重加密转发。

工具全部行为由规则驱动。规则配置以解密视角编写，例如 AES(URL(requestBody)) 表示请求体先经 URL 解码再经 AES 解密。规则支持多层嵌套组合，可覆盖 Base64 → AES → RSA 等逐层套娃场景，也支持通过表达式控制签名计算中哪些参数参与、哪些不参与。

# 安装使用

项目地址https://github.com/cloud-jie/CloudX

需使用支持 Montoya API 的新版 Burp Suite，不支持基于遗留 Extender API 的旧版本。在 Burp 的 Extensions 面板中加载编译后的 jar 包，加载成功后 Extender 标签页会出现 CloudX 的配置界面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DRNXoxlicJJs4RWibVItSqlFA77LicxrmkJgIReuxoibJLRb3Apu85ps20KunWx5NMfiaAq9BaohKopt2WJ0OQSWSwjjrIwk4kleG5WltAMueaqk/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/EqMwaEZz0ykH1KHFqibib8xIJtOkJbKW7UIiapCYNUtnwa99blUPhUWE1X554Q7GCRtPLghVWT4WvT4D8OEMvtVHQ/0?wx_fmt=png)

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