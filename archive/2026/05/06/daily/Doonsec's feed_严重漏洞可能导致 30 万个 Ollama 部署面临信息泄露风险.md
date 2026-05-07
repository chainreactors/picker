---
title: 严重漏洞可能导致 30 万个 Ollama 部署面临信息泄露风险
url: https://mp.weixin.qq.com/s/mITg4jM2D8IwByt9nUM9eg
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:32:04.178819
---

# 严重漏洞可能导致 30 万个 Ollama 部署面临信息泄露风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7OJKsibibsC7PmcYfm6oslWmh0B1WcdiajDibTvkWvhD4kYRZJQyXKZ7icBL0JVq6xib7Fp77rwgAUYSyYWhpRZZBsBZobLZfzy25GIs/0?wx_fmt=jpeg)

# 严重漏洞可能导致 30 万个 Ollama 部署面临信息泄露风险

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**Cyera 警告称，大约有 30 万个 Ollama 部署容易受到远程可利用的未经身份验证的关键漏洞的攻击，导致敏感信息被窃取。**

Ollama 是一个开源解决方案，用于在本地机器上运行 LLM，并且作为自托管 AI 推理引擎，在组织中非常受欢迎。

Cyera 表示，Ollama 中存在堆越界读取问题，可利用此问题访问存储在堆上的敏感信息，包括提示、消息和环境变量，以及 API 密钥、令牌和密钥。

该漏洞被追踪为CVE-2026-7482（CVSS 评分为 9.3），并被命名为“流血的羊驼”，它影响 GGUF 模型加载器，该加载器接受攻击者提供的 GGUF 文件，其中包含声明的张量偏移量和大小大于文件长度。

在处理文件时，传感器会读取已分配的堆缓冲区之外的数据，访问可能包含敏感信息的内存。

Cyera表示：“攻击者随后利用Ollama内置的模型推送功能，将生成的文件（包含窃取的堆数据）泄露到攻击者控制的服务器。整个攻击过程仅需三次未经身份验证的API调用。”

这家网络安全公司解释说，Ollama 默认启动时无需身份验证，并且会监听所有网络接口，这意味着所有可从互联网访问的实例都容易受到攻击。

Cyera 警告说：“目前大约有 30 万台 Ollama 服务器暴露在公共互联网上，这种漏洞可以立即被广泛利用——无需任何凭证。”

根据 Ollama 的使用方式，成功利用 Bleeding Llama 可能会暴露员工交互、开发代码、路由工具输出以及包含 PII、PHI 和其他敏感信息的提示。

Cyera 表示，“任何 Ollama 可以通过网络访问，而前面又没有防火墙或身份验证代理的部署”都存在被利用的风险。

Ollama 0.17.1 版本已修复此漏洞。建议各组织尽快应用此修复程序，并限制对其部署的网络访问。部署身份验证代理和网络分段可以提高安全性。

组织还应审核正在运行的实例是否存在互联网暴露风险，并将任何可从互联网访问的实例以及通过该实例传输的环境变量和数据视为已受到损害。

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