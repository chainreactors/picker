---
title: 30 万个 Ollama 部署面临信息失窃风险
url: https://mp.weixin.qq.com/s/gAk8o_KbGMp-2uobjOhCjw
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:28:51.906183
---

# 30 万个 Ollama 部署面临信息失窃风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ricqMN2UMva4jDYicNPKzo5Y5uA08Y7VCAneqlicias6HkaSia7f3yfjTCRabGJoRBgo7DmIga2SDMDC8EX6b5htibycia7icDeF5k4vpyOaPuHpzGk/0?wx_fmt=jpeg)

# 30 万个 Ollama 部署面临信息失窃风险

HackerNews
HackerNews

安全威胁纵横

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

高危漏洞

**紧急修复指南**

RCE Patch

Cyera 警告称，**约 30 万个 Ollama 部署因一个可远程利用、无需身份验证的严重漏洞，易面临敏感信息失窃风险。**

推测e

Ollama 是一款用于在本地机器上运行大语言模型（LLMs）的开源解决方案，作为一种自托管的人工智能推理引擎，在各组织中广受欢迎。

Cyera 表示，Ollama 中的一个堆越界读取问题，可被利用来访问存储在堆中的敏感信息，包括提示词、消息以及环境变量，如 API 密钥、令牌和机密信息等。

该漏洞编号为 CVE-2026-7482（严重程度评分 CVSS 为 9.3），被称为 “流血骆驼”，影响 GGUF 模型加载器。攻击者可提供一个 GGUF 文件，其中声明的张量偏移量和大小超过文件长度。

在处理该文件时，传感器会读取超出已分配堆缓冲区的内容，从而访问可能包含敏感信息的内存。

Cyera 称：**“攻击者随后利用 Ollama 内置的模型推送功能，将包含窃取的堆数据的文件泄露到攻击者控制的服务器。整个攻击仅需三次无需身份验证的 API 调用。”**

这家网络安全公司解释说，Ollama 默认启动时无需身份验证，且会监听所有网络接口，这意味着所有可通过互联网访问的实例都易受攻击。

Cyera 警告：“目前约有 30 万个 Ollama 服务器暴露在公共互联网上，此漏洞可即刻被广泛利用，无需凭证。”

根据 Ollama 的使用方式，成功利用 “流血骆驼” 漏洞可能导致员工交互信息、开发代码、路由工具输出，以及包含个人身份信息（PII）、个人健康信息（PHI）和其他敏感信息的提示词被泄露。

据 Cyera 称，“任何未在前面设置防火墙或身份验证代理就可通过网络访问的 Ollama 部署” 都有被利用的风险。

Ollama 0.17.1 版本已修复该漏洞。建议各组织尽快应用修复程序，并限制对其部署的网络访问。部署身份验证代理和进行网络分段应能提高安全性。

各组织还应对正在运行的实例进行互联网暴露情况审计，并将任何可从互联网访问的实例，以及通过该实例的环境变量和数据，视为已遭泄露。

转载请注明出处@安全威胁纵横，封面来源于网络；

**消息来源：https://www.securityweek.com/critical-bug-could-expose-300000-ollama-deployments-to-information-theft/**

更多网络安全视频，请关注视频号“知道创宇404实验室”

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/AYVicr6OzRAEhiaraapUTicic4reqx4oC5ssbTLiauoq7YZl4nnCOPicsCDHZzINJibpc5ck9YEpe1cqgLJ7mbWM7TpZw/0?wx_fmt=png)

安全威胁纵横

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AYVicr6OzRAEhiaraapUTicic4reqx4oC5ssbTLiauoq7YZl4nnCOPicsCDHZzINJibpc5ck9YEpe1cqgLJ7mbWM7TpZw/0?wx_fmt=png)

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