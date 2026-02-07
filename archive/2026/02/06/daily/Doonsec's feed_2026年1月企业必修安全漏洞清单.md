---
title: 2026年1月企业必修安全漏洞清单
url: https://mp.weixin.qq.com/s/0m3JdmA36CrB4bvCBMeMoA
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:04:08.220562
---

# 2026年1月企业必修安全漏洞清单

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VL7Qr6N3skhiaY7LeqWQCynS6nBXLm1mPlvg3KkQUtuyISkpWVqg8mE6LFUKxyDNgQftyzqK10ibvLKOWlicjtvl3xRWtxG2YS1hjuLq9agfgQ/0?wx_fmt=jpeg)

# 2026年1月企业必修安全漏洞清单

原创

腾讯云安全
腾讯云安全

云鼎实验室

![]()

在小说阅读器中沉浸阅读

所谓必修漏洞，就是运维人员必须修复、不可拖延、影响范围较广的漏洞，被黑客利用并发生入侵事件后，会造成十分严重的后果。

腾讯云安全参考“安全漏洞的危害及影响力、漏洞技术细节披露情况、该漏洞在安全技术社区的讨论热度”等因素，综合评估该漏洞在攻防实战场景的风险。当漏洞综合评估为风险严重、影响面较广、技术细节已披露，且被安全社区高度关注时，就将该漏洞列入必修安全漏洞候选清单。

腾讯云安全定期发布安全漏洞必修清单，以此指引企业安全运维人员修复漏洞，从而避免重大损失。 **以下是2026年1月份必修安全漏洞清单**：

**一、**RAGFlow 远程代码执行漏洞(CVE-2025-68700）

**二、**n8n 远程代码执行漏洞(CVE-2025-68668)

**三、**n8n 未授权文件访问漏洞(CVE-2026-21858)

**四、**ComfyUI Manager CRLF 注入远程代码执行漏洞(CVE-2026-22777)

**五、**Apache Struts2 XWork XML外部实体注入漏洞(CVE-2025-68493)

**六、Crawl4AI**远程代码执行漏洞( TVD-2026-3804)

**七、GNU InetUtils telnetd 远程身份认证绕过漏洞(CVE-2026-24061)**

**八、**SmarterMail 身份认证绕过漏洞(CVE-2026-23760)

九、SmarterMail ConnectToHub 远程代码执行漏洞(CVE-2026-24423）

十、OpenCode 远程代码执行漏洞(CVE-2026-22813)

**漏洞介绍及修复建议详见后文**

**一、****RAGFlow **远程代码执行漏洞****

![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3one41I6gqD2FtlJX2bnKQunF2Xm0FAciaaTgsV6iaq9Z7X2CYKVuvCAmYXr4w8RowkosXRR2fZZvumA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp)

**漏洞概述**

腾讯云安全近期监测到关于RAGFlow的风险公告，漏洞编号：TVD-2025-44186(CVE编号：CVE-2025-68700，CNNVD编号：CNNVD-202512-5500)。成功利用此漏洞的攻击者，最终可远程执行任意代码。

RAGFlow是一款开源的检索增强生成（RAG）引擎，旨在通过结合外部知识检索与生成式模型，提升大语言模型在问答、内容生成等场景下的准确性与知识覆盖度。该引擎广泛应用于智能客服、企业知识库、自动化文档处理等需要知识推理与自然语言交互的场景中。RAGFlow具备灵活的插件架构和前端可视化操作界面，支持多种数据源接入与自定义数据处理流程，方便开发者与业务人员构建定制化的智能应用。

据描述，该漏洞源于RAGFlow的前端Canvas CodeExec组件在处理未受信任的数据（如stdout输出）时，直接使用eval()函数进行解析，且未实施任何过滤或沙箱隔离措施，攻击者可通过构造恶意输入，利用eval()执行任意代码，从而在服务器上运行系统命令。

*注：未经身份验证的攻击者可结合 RAGFlow 身份认证绕过漏洞（CVE-2025-69286）绕过身份认证执行任意代码。*

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpctyZ81h7UIw8chftfeznx7jLATIbpichqGjibViaIfHNIFcLjcicCzrnoA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)漏洞状态：**

|  |  |
| --- | --- |
| **类别** | **状态** |
| 安全补丁 | 已公开 |
| 漏洞细节 | 已公开 |
| PoC | 已公开 |
| 在野利用 | 未发现 |

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpctyZ81h7UIw8chftfeznx7jLATIbpichqGjibViaIfHNIFcLjcicCzrnoA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)风险等级：**

|  |  |
| --- | --- |
| **评定方式** | **等级** |
| 威胁等级 | 高危 |
| 影响面 | 高 |
| 攻击者价值 | 高 |
| 利用难度 | 低 |
| 漏洞评分 | 8.8 |

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpyMmKHz3l49YYK3IFIpeUDAZH9ywjHBPia1R5aGb9LIdQb0yYtqAPqAw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

**影响版本**

RAGFlow< 0.23.0

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgppKsWWD2v5KKg5WV1ibGa2aQqoicqDfqzAAZtNibAV2jQAAnIkWwibkECkg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

**修复建议**

1. 官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，酌情升级至安全版本。

【备注】建议您在升级前做好数据备份工作，避免出现意外。

https://github.com/infiniflow/ragflow/releases

2. 临时缓解方案：

- 如无必要，避免将服务开放至公网

- 配置防火墙或网络规则，仅允许特定IP地址或IP段访问

**二、****n8n****远程代码执行漏洞**

![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3one41I6gqD2FtlJX2bnKQunF2Xm0FAciaaTgsV6iaq9Z7X2CYKVuvCAmYXr4w8RowkosXRR2fZZvumA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp)

**漏洞概述**

腾讯云安全近期监测到关于n8n的风险公告，漏洞编号：TVD-2025-43636(CVE编号：CVE-2025-68668，CNNVD编号：CNNVD-202512-4823)。成功利用此漏洞的攻击者，最终可远程执行任意代码。

n8n是一个开源的工作流自动化平台，它允许用户通过可视化界面或代码来创建、管理和执行各种自动化任务和工作流。该平台具有高度的灵活性和可扩展性，支持多种集成方式和节点类型，可用于数据处理、系统集成、自动化业务流程等多种场景。用户可以根据自身需求自定义工作流，实现不同系统之间的数据交互和任务自动化，提高工作效率和准确性，在企业级自动化流程中应用广泛。

据描述，该漏洞源于n8n中基于Pyodide实现的Python代码节点存在沙箱隔离缺陷。该节点旨在为工作流提供安全的Python代码执行环境，但其隔离机制（Pyodide）可能被经过身份验证的攻击者通过注入或构造特定的Python代码绕过，从而突破沙箱限制，直接访问并操作底层主机操作系统的资源。这使得拥有创建工作流权限的攻击者可以通过编辑或创建包含恶意代码的 Python 节点，以 n8n 进程的权限在服务器上执行任意系统命令。

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpctyZ81h7UIw8chftfeznx7jLATIbpichqGjibViaIfHNIFcLjcicCzrnoA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)漏洞状态：**

|  |  |
| --- | --- |
| **类别** | **状态** |
| 安全补丁 | 已公开 |
| 漏洞细节 | 已公开 |
| PoC | 已公开 |
| 在野利用 | 未发现 |

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpctyZ81h7UIw8chftfeznx7jLATIbpichqGjibViaIfHNIFcLjcicCzrnoA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)风险等级：**

|  |  |
| --- | --- |
| **评定方式** | **等级** |
| 威胁等级 | 高危 |
| 影响面 | 高 |
| 攻击者价值 | 高 |
| 利用难度 | 低 |
| 漏洞评分 | 9.9 |

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpyMmKHz3l49YYK3IFIpeUDAZH9ywjHBPia1R5aGb9LIdQb0yYtqAPqAw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

**影响版本**

1.0.0 <= n8n < 2.0.0

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgppKsWWD2v5KKg5WV1ibGa2aQqoicqDfqzAAZtNibAV2jQAAnIkWwibkECkg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

**修复建议**

1. 官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，酌情升级至安全版本。

【备注】建议您在升级前做好数据备份工作，避免出现意外。

https://github.com/n8n-io/n8n/releases

2. 由于n8n从1.111.0版本起，引入了基于任务运行器（task-runner）的原生Python 实现可选功能，提供了更安全的隔离模型。因此也可通过配置环境变量 N8N\_RUNNERS\_ENABLED和N8N\_NATIVE\_PYTHON\_RUNNER启用进行修复。并且此安全实现自2.0.0版本起已成为默认配置。

3. 临时缓解措施：

- 禁用代码节点：设置环境变量 NODES\_EXCLUDE: "[\"n8n-nodes-base.code\"]"，可参考以下链接：

https://docs.n8n.io/hosting/securing/blocking-nodes/

- 禁用 Python 支持：设置环境变量 N8N\_PYTHON\_ENABLED=false（该环境变量自 1.104.0 版本引入）。

- 启用安全沙箱：配置环境变量 N8N\_RUNNERS\_ENABLED和N8N\_NATIVE\_PYTHON\_RUNNER，以使用基于任务运行器的 Python 沙箱，可参考以下链接：

https://docs.n8n.io/hosting/configuration/task-runners/

**三、****n8n **未授权文件访问漏洞****

![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3one41I6gqD2FtlJX2bnKQunF2Xm0FAciaaTgsV6iaq9Z7X2CYKVuvCAmYXr4w8RowkosXRR2fZZvumA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp)

**漏洞概述**

腾讯云安全近期监测到关于n8n的风险公告，漏洞编号：TVD-2026-3136(CVE编号：CVE-2026-21858，CNNVD编号：CNNVD-202601-1364)。成功利用此漏洞的攻击者，可访问服务器上的敏感文件，造成敏感信息泄露。

据描述，由于n8n的Webhook和文件处理逻辑中存在Content-Type混淆缺陷，当系统处理 Webhook请求时，错误的 Content-Type 标头处理会导致内部请求解析状态被覆盖。攻击者通过向公开的 Webhook 端点发送经过特制的 HTTP 请求，从而覆盖内部状态、访问包括身份验证密钥在内的敏感文件，并且可能通过伪造管理员会话，最终在主机上实现任意代码执行，从而完全控制自动化实例、窃取凭证和密钥，并横向渗透到连接的内部系统、API 和云服务中。

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpctyZ81h7UIw8chftfeznx7jLATIbpichqGjibViaIfHNIFcLjcicCzrnoA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)漏洞状态：**

|  |  |
| --- | --- |
| **类别** | **状态** |
| 安全补丁 | 已公开 |
| 漏洞细节 | 已公开 |
| PoC | 已公开 |
| 在野利用 | 未发现 |

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpctyZ81h7UIw8chftfeznx7jLATIbpichqGjibViaIfHNIFcLjcicCzrnoA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)风险等级：**

|  |  |
| --- | --- |
| **评定方式** | **等级** |
| 威胁等级 | 高危 |
| 影响面 | 高 |
| 攻击者价值 | 高 |
| 利用难度 | 低 |
| 漏洞评分 | 9.0 |

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpyMmKHz3l49YYK3IFIpeUDAZH9ywjHBPia1R5aGb9LIdQb0yYtqAPqAw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

**影响版本**

1.65.0 <= n8n < 1.121.0

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgppKsWWD2v5KKg5WV1ibGa2aQqoicqDfqzAAZtNibAV2jQAAnIkWwibkECkg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

****修复建议****

1. 官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，酌情升级至安全版本。

【备注】建议您在升级前做好数据备份工作，避免出现意外。

https://github.com/n8n-io/n8n/releases

2. 临时缓解方案：

- 限制或禁用公开访问的 webhook 和表单端点的访问

**四、****ComfyUI Manager CRLF****注入远程代码执行漏洞**

![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3one41I6gqD2FtlJX2bnKQunF2Xm0FAciaaTgsV6iaq9Z7X2CYKVuvCAmYXr4w8RowkosXRR2fZZvumA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp)

**漏洞概述**

腾讯云安全近期监测到关于ComfyUI-Manager的风险公告，漏洞编号：TVD-2026-3230(CVE编号：CVE-2026-22777，CNNVD编号：CNNVD-202601-1731)。成功利用此漏洞的攻击者，最终可远程执行任意代码。

ComfyUI-Manager是专为增强ComfyUI易用性而设计的扩展工具，旨在为ComfyUI用户提供更便捷的操作体验和功能管理能力。ComfyUI通常用于AI图像生成与处理领域，而ComfyUI-Manager作为其官方或社区推荐的扩展组件，提供了配置管理、插件集成、用户界面优化等功能，广泛被AI艺术创作者、开发者及研究人员所使用。该组件通过简化配置流程和增强交互体验，帮助用户更高效地使用ComfyUI平台，是AI图像生成生态中的重要辅助工具。

据描述，该漏洞源于ComfyUI Manager暴露了可通过Web API修改配置的接口，且在处理用户输入时，未能对回车换行符等特殊字符进行有效过滤，导致存在CRLF注入漏洞，攻击者可向该接口发送特制请求，在配置值中注入换行符，从而更改配置文件。攻击者可进一步利用 ComfyUI Manager 的 Git URL 安装功能，诱使应用从攻击者控制的仓库安装恶意自定义节点，最终在服务器上执行任意代码。

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0mI3Hn04TDicQGeRhYXPRSgpctyZ81h7UIw8chftfeznx7jLATIbpichqGjibViaIfHNIFcLjcicCzrnoA/640?wx...