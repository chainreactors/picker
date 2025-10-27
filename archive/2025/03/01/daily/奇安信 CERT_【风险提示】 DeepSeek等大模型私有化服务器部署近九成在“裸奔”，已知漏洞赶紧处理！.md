---
title: 【风险提示】 DeepSeek等大模型私有化服务器部署近九成在“裸奔”，已知漏洞赶紧处理！
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247503061&idx=1&sn=d35bc82adb76b97ee71ebd660128a85d&chksm=fe79e84dc90e615b14715455df9ec7a0e2bd9fe219cbe0c114bef033092b8ebd014e8e51a106&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2025-03-01
fetch_date: 2025-10-06T21:58:48.566714
---

# 【风险提示】 DeepSeek等大模型私有化服务器部署近九成在“裸奔”，已知漏洞赶紧处理！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4icpQdCHGl7xgk0DSnKbHSzmRd1s4gMVTviaU7mvbpsR2pPCGU2nwZaxeiaDiajicDoHkmpJjDNE55Nmhw/0?wx_fmt=jpeg)

# 【风险提示】 DeepSeek等大模型私有化服务器部署近九成在“裸奔”，已知漏洞赶紧处理！

奇安信 CERT

问题概述

近期，随着国产大模型 DeepSeek 的迅速流行，越来越多的企业和个人选择将其进行私有化部署。然而，根据奇安信资产测绘鹰图平台的监测数据，在 8971 个运行 Ollama 大模型框架的服务器中，有 6449 个活跃服务器，其中 88.9% 的服务器未采取有效的安全防护措施，处于“裸奔”状态。这种状态导致任何人都可以在未经授权的情况下访问这些服务，从而引发数据泄露、服务中断、算力盗用甚至模型文件被删除等严重风险。

相关组件和系统漏洞

**1.Ollama工具的安全漏洞**

Ollama 是一款用于私有化部署大模型的工具，支持 DeepSeek、Qwen、Llama、Mistral 等多种语言模型。

默认未设置身份验证和访问控制功能，导致服务 API 接口（如http://XX.XX.XX.XX:11434）可在未经授权的情况下被调用。

2024年11月，研究人员披露了 Ollama 框架中的六个安全漏洞，可能被利用执行拒绝服务攻击（DDoS）、模型污染和模型盗窃等恶意行为。

**2.大模型服务器的安全风险**

服务器未进行必要的安全配置，如未启用防火墙、未设置 IP 白名单、未对数据传输进行加密。

已出现通过自动化脚本扫描“裸奔”状态的 DeepSeek 服务器，并恶意占用大量计算资源，导致部分用户服务器崩溃的事件。

|  |  |  |
| --- | --- | --- |
| ****漏洞名称**** | ****风险等级**** | ****漏洞概述**** |
| Ollama 未授权访问风险 | 中风险 | Ollama 默认未设置身份验证和访问控制功能，其服务 API 接口（如http://XX.XX.XX.XX:11434）可在未授权情况下被调用，攻击者可远程访问该接口，窃取知识库、投喂虚假信息或滥用模型推理资源。 |
| Ollama 模型管理接口风险 | 中风险 | 攻击者可通过未授权访问 Ollama 的模型管理接口，读取、下载或删除私有模型文件。 |
| Ollama 模型推理接口风险 | 中风险 | 攻击者可利用未授权访问的模型推理接口，执行任意 Prompt 指令，滥用模型推理资源。 |
| Ollama 系统配置接口风险 | 中风险 | 攻击者可能通过未授权访问篡改 Ollama 服务参数，影响系统配置。 |
| Ollama 远程代码执行漏洞(CVE-2024-37032) | 高危（CVSS评分9.1） | 在 Ollama 0.1.34 之前的版本中存在远程代码执行漏洞，攻击者无需身份验证即可通过接口操控服务器，实现任意代码执行。 |
| Ollama 路径遍历漏洞(CVE-2024-45436) | 高危（CVSS评分9.1） | 在 Ollama 0.1.47 之前的版本中，extractFromZipFile函数在处理ZIP文件解压时，未能正确限制文件路径，导致攻击者可以通过特制的ZIP文件将文件解压到父目录之外。 |
| Ollama 信息泄露漏洞(CVE-2024-39722) | 高危（CVSS评分7.5） | 在 Ollama 0.1.46 之前的版本中发现了一个漏洞。它通过 api/push 路由中的路径遍历，攻击者可以通过发送包含不存在的文件路径参数的恶意请求，利用该漏洞确定服务器上文件的存在性。 |
| Ollama 信息泄露漏洞(CVE-2024-39719) | 高危（CVSS评分7.5） | Ollama 0.3.14 及之前版本存在信息泄露漏洞，该漏洞源于/api/create端点对路径参数处理不当。攻击者可以通过发送包含不存在的文件路径参数的恶意请求，利用该漏洞确定服务器上文件的存在性，从而可能泄露敏感信息。 |
| Ollama DNS 重绑定漏洞(CVE-2024-28224) | 高危（CVSS评分8.8） | Ollama 在 0.1.29 版本之前存在一个 DNS 重绑定漏洞，可能允许远程访问完整 API，从而让未经授权的用户与大型语言模型聊天、删除模型或导致拒绝服务（资源耗尽）。 |
| Ollama 拒绝服务漏洞(CVE-2024-39721) | 高危（CVSS评分7.5） | Ollama 在 0.1.34 版本之前存在一个拒绝服务漏洞，该漏洞存在于Ollama的/api/create端点中，CreateModelHandler函数未对用户控制的req.Path参数进行适当验证。攻击者可以通过向该端点发送包含特殊文件路径（如/dev/random）的POST请求，使程序进入无限循环，耗尽系统资源，最终导致拒绝服务。 |
| Ollama 拒绝服务漏洞(CVE-2024-39720) | 高危（CVSS评分8.2） | 在 Ollama 0.1.46 之前的版本中发现了一个漏洞。攻击者可以利用两个 HTTP 请求上传一个仅包含以 GGUF 自定义魔术头开始的 4 个字节的畸形 GGUF 文件。通过利用一个包含指向攻击者控制的 blob 文件的 FROM 语句的自定义 Modelfile，攻击者可以通过 CreateModel 路由使应用程序崩溃，导致段错误。 |

风险提示

多家政企单位发出风险提示，指出使用 Ollama 工具部署 DeepSeek 等大模型时，存在以下安全隐患：

1.未经授权的访问和调用。

2.数据泄露和服务中断。

3.模型文件被删除，导致系统不可用。

4.算力被非法占用，用于加密货币挖矿或 DDoS 攻击。

防范建议

**1.配置访问控制**

若 Ollama 仅对本地提供服务，建议设置环境变量 Environment="OLLAMA\_HOST=127.0.0.1"，限制为仅本地访问。

若需要对外提供服务，可通过修改 config.yaml 或 settings.json 配置文件限定可调用 Ollama 服务的 IP 地址，或在防火墙等设备上部署 IP 白名单。

**2.加强身份认证**

立即修改 Ollama 配置，增加身份认证机制。

**3.数据加密**

对所有传输的数据进行加密，避免敏感信息泄露。

**4.部署安全产品**

使用专业安全工具（如奇安信大模型卫士）防范越狱攻击、提示词注入等风险。

**5.定期检查与维护**

定期检查服务器的安全状态，关闭不必要的端口，限制计算资源的使用，并加强监控。

**6.升级安全防护手段**

针对大模型特有的安全风险，如提示注入攻击、信息内容安全风险、数据隐私泄漏等，升级安全防护手段。

奇安信ALPHA威胁分析平台已支持漏洞情报订阅服务：

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BY9IJ0MPzeiashvK2XLpdl3XtTtCD91h0jS26fqvuWpEMXgmXa85qLkoA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp "漏洞订阅上线.png")

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tG2LbK7WG3tezJEzJsicLSWCGsIggLbcfk4LB5WK7pdSwMksxPOAoHuibjQpBlEId4nyIIw52n2J8N8MowYZcjA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BYBVaibvBq1vXprZIc191LXKibdiaApA16q3UgmibQDv4yW09qT88J3jRUfA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp "CERT LOGO.png")

**奇安信 CERT**

**致力于**第一时间为企业级用户提供**权威**漏洞情报和**有效**解决方案。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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