---
title: 新开源网络安全平台CyberSentinel AI v3.0 正式亮相
url: https://mp.weixin.qq.com/s/5oxSt1UtaF7_zBM1_qNA_Q
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:02:32.998910
---

# 新开源网络安全平台CyberSentinel AI v3.0 正式亮相

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH1zibCyvHUt92ayQRkS2thxcYaHaexH80MRrsGHSWqNjIZFSibQwfbl0aia0Q5WicgwMEf0ib1CbHlQggUVibZQwpvvwFca3wiapUpIXg/0?wx_fmt=jpeg)

# 新开源网络安全平台CyberSentinel AI v3.0 正式亮相

原创

安全ker
安全ker

安全客

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 一款名为 **CyberSentinel AI v3.0** 的新开源网络安全平台正式亮相，成为自主安全工具领域的重要进展。该平台融合了 **33 款真实渗透测试与威胁情报工具**，并搭载与提供商无关的 AI 引擎，支持 Claude、GPT-4o、OpenRouter，以及通过 Ollama 实现的完全离线本地推理。

与仅能提出命令建议的传统 AI 安全助手不同，CyberSentinel AI 能够在隔离的 Kali Linux Docker 沙箱中**真正执行工具**——包括 Nmap、SQLMap、Nikto、Nuclei 和 OWASP ZAP——并由 AI 对结果进行实时分析。

该平台在 GitHub 上以 `3sk1nt4n/cybersentinel-ai` 发布，完全运行于本地基础设施，**无需任何云服务依赖**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/97Bx8JKrib1MEj924r6XWia9iajfGT1R23Awib5ibRx8fZT3O1qwgGppMu8kOf3SUwZGsEyfF1Q0prSdZOkwdSrUWic1GWEU9bYDamC3HC4zAZw4Q/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/qXNHvpelMgLhOc2MRIyZG5XnCvMtIONMyx5fXyTQbB2CW8dKicfLXGpM6Usg7Z6AOlKR2C23tNnNs5UBiaThZ7gY0PnXmKhkxUKUicGufCSaUE/640?from=appmsg)

架构：七大容器化服务

平台通过 Docker Compose 部署，共包含七个容器化服务：

* Next.js 前端

  （端口 3000）：提供流式聊天界面
* FastAPI 后端

  （端口 8000）：负责 AI 路由、意图分类与工具编排
* Kali 沙箱容器

  在完全隔离的环境中执行安全扫描，防止危险操作波及宿主系统
* Neo4j

  用于攻击面与 MITRE ATT&CK 技术知识图谱映射
* ChromaDB

  基于 MITRE、CIS 和 NIST 框架的 RAG（检索增强生成）引擎
* Elasticsearch + Kibana

  ELK Stack SIEM，预置安全事件数据，用于日志分析训练

该平台的**自主执行模型**允许 AI 自动分类用户意图、自主选择合适工具，并支持**最多同时并发运行五个工具**，最终综合输出统一分析报告——这是向实用安全自动化迈出的重要一步。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/97Bx8JKrib1MEj924r6XWia9iajfGT1R23Awib5ibRx8fZT3O1qwgGppMu8kOf3SUwZGsEyfF1Q0prSdZOkwdSrUWic1GWEU9bYDamC3HC4zAZw4Q/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/qXNHvpelMgLhOc2MRIyZG5XnCvMtIONMyx5fXyTQbB2CW8dKicfLXGpM6Usg7Z6AOlKR2C23tNnNs5UBiaThZ7gY0PnXmKhkxUKUicGufCSaUE/640?from=appmsg)

33 款安全工具，覆盖六大功能类别

| 类别 | 工具数量 | 主要工具 |
| --- | --- | --- |
| 实时扫描器 | 11 款 | Nmap、Nikto、Nuclei、SQLMap、Subfinder、OWASP ZAP、SSL/TLS 分析、DNS 侦察、WHOIS、HTTP 头部检测、Ping/Traceroute |
| 威胁情报 API | 5 款 | Shodan、VirusTotal、AbuseIPDB、AlienVault OTX、NVD/CISA KEV |
| SIEM 集成 | 3 款 | ELK Stack、Splunk、Wazuh |
| AI 检测 | 5 款 | Zeek 分析器、IOC 提取器、日志分析器、威胁检测、电子邮件钓鱼分析器 |
| 威胁狩猎 | 4 款 | YARA 规则、Sigma 规则、Snort/Suricata 规则、SIEM 查询生成器 |
| 合规框架 | 5 款 | MITRE ATT&CK、MITRE ATLAS、NIST/CIS、HIPAA/PCI-DSS、SOC 2/FedRAMP |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/97Bx8JKrib1MEj924r6XWia9iajfGT1R23Awib5ibRx8fZT3O1qwgGppMu8kOf3SUwZGsEyfF1Q0prSdZOkwdSrUWic1GWEU9bYDamC3HC4zAZw4Q/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/qXNHvpelMgLhOc2MRIyZG5XnCvMtIONMyx5fXyTQbB2CW8dKicfLXGpM6Usg7Z6AOlKR2C23tNnNs5UBiaThZ7gY0PnXmKhkxUKUicGufCSaUE/640?from=appmsg)

核心亮点

**会话中途切换 AI 提供商**是 CyberSentinel 的突出特性之一。用户可在 Anthropic Claude、OpenAI GPT-4o、OpenRouter（支持 100+ 模型）与本地运行的 Ollama（默认模型 `qwen2.5:7b`）之间随时切换，**且不会丢失任何对话上下文**。所有 API 密钥均为可选，平台可以 Ollama 作为默认推理引擎实现完全离线运行。

**实时威胁情报**动态拉取自 NVD、CISA KEV、EPSS、AlienVault OTX 和 Abuse.ch，无需手动更新即可保持漏洞上下文的持续更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/97Bx8JKrib1MEj924r6XWia9iajfGT1R23Awib5ibRx8fZT3O1qwgGppMu8kOf3SUwZGsEyfF1Q0prSdZOkwdSrUWic1GWEU9bYDamC3HC4zAZw4Q/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/qXNHvpelMgLhOc2MRIyZG5XnCvMtIONMyx5fXyTQbB2CW8dKicfLXGpM6Usg7Z6AOlKR2C23tNnNs5UBiaThZ7gY0PnXmKhkxUKUicGufCSaUE/640?from=appmsg)

安全防护机制

平台内置多重安全保障措施：

* 输入/输出过滤

  屏蔽提示词注入（Prompt Injection）、SSRF 攻击和系统提示词泄露
* 沙箱隔离

  所有扫描均在独立容器内执行
* 法律警告

  项目明确提示，未经授权的扫描行为属于违法行为

![](https://mmbiz.qpic.cn/sz_mmbiz_png/97Bx8JKrib1MEj924r6XWia9iajfGT1R23Awib5ibRx8fZT3O1qwgGppMu8kOf3SUwZGsEyfF1Q0prSdZOkwdSrUWic1GWEU9bYDamC3HC4zAZw4Q/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/qXNHvpelMgLhOc2MRIyZG5XnCvMtIONMyx5fXyTQbB2CW8dKicfLXGpM6Usg7Z6AOlKR2C23tNnNs5UBiaThZ7gY0PnXmKhkxUKUicGufCSaUE/640?from=appmsg)

系统要求

* 必须安装

  Docker Desktop
* 最低内存

  8 GB RAM
* 首次构建

  约需下载 4–5 GB 镜像及模型数据
* 后续启动

  约 30 秒内完成

CyberSentinel AI v3.0 实现了**自主 AI 与真实安全工具的深度融合**，为安全研究人员和红队提供了一套完全自托管、无云依赖的替代性平台，是安全自动化领域值得关注的实践性进展。

信息来源：https://cybersecuritynews.com/cybersentinel-ai-with-33-security-tools/

![](https://mmbiz.qpic.cn/mmbiz_png/e8XlCTfPrcM4SD27bheY74gn8dPagfIOekOMj8iapjKdXVeHY08GT5wjvb73xa77ZwB1FseR8zphAc9pMg7icqx4t2AmAvLQiaibZR5IGmEWc18/640?from=appmsg)

END

推荐阅读

[Splunk AI Toolkit曝高危漏洞：CVSS 9.1，可远程执行任意系统命令](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790099&idx=1&sn=17ef8b65a5934d609189271357051b6a&scene=21#wechat_redirect)

2026-06-18

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH1vSD0t4nv5lKzY9COrk5YQMPPMmwRgtotcVYKreINgf6icVCjBgIyMfBtIiakuYJgctDEVmeiaRcmA3M8cLsOlDX4MZAibaas4hgk/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790099&idx=1&sn=17ef8b65a5934d609189271357051b6a&scene=21#wechat_redirect)

[Weaxor勒索软件又添Linux平台变种](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790094&idx=1&sn=e06d67c3804a4211060e273061b1f30e&scene=21#wechat_redirect)

2026-06-17

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH1xrxHHdxpkVH7hNLtqLiaD3tdmXlnKVxiclUoQHEFJmbbuKCCysuDWkJ7g1MLGAibne1LpK5Ie3oKuN1cccg6IkMAribIHiag7NiaWI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790094&idx=1&sn=e06d67c3804a4211060e273061b1f30e&scene=21#wechat_redirect)

[制药巨头诺和诺德遭遇安全事件：药企网络安全再敲警钟](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790068&idx=1&sn=ed7d53228ef279c16414c2c463c78e52&scene=21#wechat_redirect)

2026-06-15

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH1znda5ZjZxJLLmiaFjZVjxmcoHwkvJGLUkUYYice8IenehOuK74CjayXcPJicq9nng7CxOJ40H75gtBUywaQ7vYDhC2bM8EvOwVk/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790068&idx=1&sn=ed7d53228ef279c16414c2c463c78e52&scene=21#wechat_redirect)

[45.5万人中招！英国名校遭供应链攻击，你的校园账户还安全吗？](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790063&idx=1&sn=bab80c055559d24502094d21728ce1ed&scene=21#wechat_redirect)

2026-06-14

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH3yBnXubLjquibGnC0XWmS5ER0YrrSfTQZqograsCwbmcuA4Amdk1j67q7UaCIiaJz6GHQvVPB63sOtnlp5bibVk5tdCa473daictg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790063&idx=1&sn=bab80c055559d24502094d21728ce1ed&scene=21#wechat_redirect)

[360「Aiker World社区」× PMI中国「AI+项目管理社区」AI人才生态战略合作发布](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790056&idx=1&sn=49e37a8953e7e7f486e32fccb9e0fd4e&scene=21#wechat_redirect)

2026-06-13

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH1ctZDGhj4NX51Uq5HIwAhz7dINWP0yTAdZO12ad9UjuUxS6M6iag4nBTC3RTWMVqOhCMoUNpibHkYDIMM12E2S6CxPNmpY7U5VI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790056&idx=1&sn=49e37a8953e7e7f486e32fccb9e0fd4e&scene=21#wechat_redirect)

[Mythos可数小时内把漏洞变成武器：Anthropic还是未开放使用](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790051&idx=1&sn=52cfd439a009d5ae32e098a4bd6706b0&scene=21#wechat_redirect)

2026-06-11

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH387evkTonuKT4ayIlWkELLgibmqjcVav75RRowNlBibxc9wUElENAJXkMjs1iaDBwyRcrdZg6L4zbicR4HK7PRdAcDGcEzzS6H1BM/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790051&idx=1&sn=52cfd439a009d5ae32e098a4bd6706b0&scene=21#wechat_redirect)

[10万行空行就能骗过AI安检？顶尖安全团队实测：主流技能扫描器全部穿帮](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790046&idx=1&sn=465bf3f2a4a264db6daa33030ec607cc&scene=21#wechat_redirect)

2026-06-10

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH2UQVUt1icErMSowlwZ8FVHzRbGKkwHKRaLF5yGia1JbDEgvYX5W3V0ULxx82HBibzstPKvwzDyZyClro3nZMicvv7gfqvWWCYiaud4/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790046&idx=1&sn=465bf3f2a4a264db6daa33030ec607cc&scene=21#wechat_redirect)

[文科生AI黑客松：从「代码边缘」到「智能核心」的范式转移](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790040&idx=1&sn=aa96d7fb4234de856768fb68274ed6a3&scene=21#wechat_redirect)

2026-06-09

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH226P2LUCKkmmYYicjlXDhf21q24v6NS1kRURkibT2EeBPktGyFjpHCFP5EiacZM9E9rKj3piaZYQXjdehIP5nFPDRic7bSdS2btVQw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790040&idx=1&sn=aa96d7fb4234de856768fb68274ed6a3&scene=2...