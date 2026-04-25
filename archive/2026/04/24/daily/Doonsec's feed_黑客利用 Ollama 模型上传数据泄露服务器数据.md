---
title: 黑客利用 Ollama 模型上传数据泄露服务器数据
url: https://mp.weixin.qq.com/s/WVd1vPdLT4ZLBSmFtQCoZQ
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:32:07.995567
---

# 黑客利用 Ollama 模型上传数据泄露服务器数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7MmFuOeD1QhRWJYGwxw4iaicSyibKdq7X5Ppu2SsNscGY7ADPibVKoeOULDF4JgQpSPAoic2W4bNAI0obl9MSWcTdPakfG2iapLGfluY/0?wx_fmt=jpeg)

# 黑客利用 Ollama 模型上传数据泄露服务器数据

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

网络安全研究人员发现 Ollama 存在一个严重的、未修复的漏洞，Ollama 是一个流行的开源平台，用于在本地运行大型语言模型。

该漏洞编号为 CVE-2026-5757，存在于 Ollama 的模型量化引擎中。一旦被利用，未经身份验证的攻击者只需上传一个恶意构造的 AI 模型文件，即可窃取敏感的服务器数据。

## **漏洞利用原理**

为了提高性能和效率，Ollama 使用了量化技术，这降低了 AI 模型的数值精度。

然而，研究人员发现该引擎在处理GPT 生成的统一格式 (GGUF) 文件时存在越界内存漏洞。

当攻击者上传一个专门设计的 GGUF 文件并触发量化过程时，他们可以强制服务器读取超出其安全内存限制的数据。

这种危险的犯罪行为是由以下三个因素共同作用造成的：

* 引擎盲目信任用户提供的文件元数据，而不检查它是否与提供的数据大小实际匹配。
* 该软件使用 Go 语言中的不安全内存操作来创建数据切片，该切片会延伸到应用程序堆的深处。
* 系统意外地将泄漏的内存写入了一个新的模型层，使得攻击者能够通过 Ollama 的注册表 API 将窃取的数据推送到外部服务器。

由于此漏洞允许未经授权的攻击者访问服务器的核心堆，因此对于托管这些模型的组织而言，后果可能是毁灭性的。攻击者可以悄无声息地读取并提取在正常运行期间临时存储在系统内存中的高度敏感数据。

这种不必要的泄露可能很快导致 API 密钥、私人用户数据或专有知识产权被盗。

此外，恶意行为者可以利用这种未经授权的访问来更广泛地控制服务器，破坏底层网络，并在不触发标准安全警报的情况下建立隐蔽的持久性。

该漏洞最初是由安全研究员 Jeremy Brown 发现的，他使用人工智能辅助漏洞研究方法发现了该漏洞。

截至 2026 年 4 月下旬，CERT 协调中心仍无法联系到供应商，这意味着目前没有官方补丁可用。

使用 Ollama 的组织和开发人员必须立即采取人工措施，以保护其 AI 部署免受潜在攻击。

为降低被利用的风险，管理员应实施以下安全措施：

* 立即限制或关闭所有公开服务器上的模型上传功能。
* 将所有 Ollama 部署限制在本地、隔离或高度可信的网络环境中。
* 仅接受、下载和运行来自经过验证和高度可信来源的人工智能模型。
* 实施严格的网络验证控制，以防止未经授权的外部连接和数据泄露。

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