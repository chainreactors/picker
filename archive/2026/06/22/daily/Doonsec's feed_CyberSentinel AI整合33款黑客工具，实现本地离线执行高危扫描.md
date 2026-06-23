---
title: CyberSentinel AI整合33款黑客工具，实现本地离线执行高危扫描
url: https://mp.weixin.qq.com/s/Xa0TV8z97bt2NK1UrtnW8w
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:04:27.660091
---

# CyberSentinel AI整合33款黑客工具，实现本地离线执行高危扫描

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2tlZcwfpcDGKErp5JibgaVKyuSZicwh4ib2MEEqTUZ3wLyapFSwmBzgGAhQaB34t7kgguqNSJkWngCQq5cegCc0wgf5R7cAo7w3M/0?wx_fmt=jpeg)

# CyberSentinel AI整合33款黑客工具，实现本地离线执行高危扫描

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX2c9S6c5tzX9TG2K4Id4mBxEALVYI2rT6cbWpcrdDuEwGadb4FtR2ptuib5c9FHFTZwqWstywZmibVe4WWT4Q9viceqLj3sdIibq7w/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0Tz2o6B44t6rP97W2aYGGu7e9mNktYiaay9piaInfs5Z7pK2XUc3QF3sb3wbzRpA2nWmibeia8wISm7ZGpehHlaAVibCb4WFlibD2FA/640?wx_fmt=jpeg)

开源网络安全平台CyberSentinel AI v3.0近日发布，标志着自主安全工具领域的重大进展。该平台整合了33款实战渗透测试与威胁情报工具，并搭载供应商无关的AI引擎，支持Claude、GPT-4o、OpenRouter，以及通过Ollama实现的完全离线本地推理。

与传统仅提供命令建议的AI安全助手不同，CyberSentinel AI能在隔离的Kali Linux Docker沙箱中实际执行Nmap、SQLMap、Nikto、Nuclei和OWASP ZAP等工具，并利用AI实时分析扫描结果。该平台已在GitHub发布（仓库地址：3sk1nt4n/cybersentinel-ai），设计为完全在本地基础设施运行，无需依赖云服务。

![CyberSentinel AI平台](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2poQX15xGia2z4g7pmdQlmn3qXn4kGIZYElWFFZq96YCYMwHIMPx4Co7eg0DrLib1ZxVQJYDSXboH4brjoD2WdbgiczRZyMQKYaM/640?wx_fmt=png)

Part01

技术架构

平台通过Docker Compose部署，包含七个容器化服务：

* Next.js前端（端口3000）提供流式聊天界面
* FastAPI后端（端口8000）处理AI路由、意图分类和工具编排
* 安全扫描在沙盒化的Kali容器内执行，确保高危操作与主机系统完全隔离

AI层由三大数据基础设施支撑：

* Neo4j：用于攻击面和MITRE ATT&CK技术的知识图谱映射
* ChromaDB：基于MITRE、CIS和NIST框架的检索增强生成（RAG）引擎
* 集成Kibana的Elasticsearch：作为预置安全事件的ELK Stack SIEM，用于日志分析训练

Part02

工具集分类

平台将33款工具划分为六大功能类别：

* 实时扫描工具（11款）：Nmap、Nikto、Nuclei、SQLMap、Subfinder、OWASP ZAP、SSL/TLS分析、DNS侦察、WHOIS、HTTP头检测及Ping/路由追踪
* 威胁情报API（5个）：Shodan、VirusTotal、AbuseIPDB、AlienVault OTX及NVD/CISA KEV集成
* SIEM集成（3种）：ELK Stack、Splunk和Wazuh连接器
* AI检测模块（5项）：Zeek分析器、IOC提取器、日志分析器、威胁检测及钓鱼邮件分析
* 威胁狩猎（4类）：YARA规则、Sigma规则、Snort/Suricata规则及SIEM查询生成器
* 合规框架（5套）：MITRE ATT&CK、MITRE ATLAS、NIST/CIS、HIPAA/PCI-DSS及SOC 2/FedRAMP

Part03

核心特性

平台支持对话中无缝切换AI供应商，用户可在Anthropic Claude、OpenAI GPT-4o、OpenRouter（支持100+模型）及本地运行的Ollama（搭载qwen2.5:7b模型）之间自由切换，且不丢失对话上下文。所有API密钥均为可选，平台默认使用Ollama作为离线推理引擎。

威胁情报动态更新机制会自动从NVD、CISA KEV、EPSS、AlienVault OTX和Abuse.ch获取最新漏洞数据。安全防护方面设有输入/输出护栏，可阻断提示注入、SSRF攻击和系统提示泄露。

Part04

使用须知

所有扫描均在隔离容器内执行，项目明确警示用户：根据《计算机欺诈与滥用法案》（CFAA），未经授权的扫描属违法行为。推荐的安全测试目标包括scanme.nmap.org和testphp.vulnweb.com。

系统要求Docker Desktop环境及至少8GB内存。初始构建需下载约4-5GB的镜像和模型数据，后续启动时间约30秒。CyberSentinel AI v3.0实现了Agentic AI与实战安全工具的有力结合，为安全研究人员和红队提供了不依赖云服务的自主操作方案。

参考来源：

CyberSentinel AI with 33 Security Tools, Including Nmap, SQLMap, ZAP, and uses Claude, GPT

https://cybersecuritynews.com/cybersentinel-ai-with-33-security-tools/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2JXiaeRXDdhP1b1yIW5ia7iaiaQibSfw82mLRk8mamNA5ePnYGjYtSHhDAJAwe3CxuiavndLBnLABKf95QofDIicy0cI2BNicxnE6jooY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340512&idx=1&sn=88628c0f7cabd6cae377643824d2ffe9&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1WgT6uY8WS5x81Ek2AvNjbhqyOCGL1416DCVVAmCE9IyV54ffo9FPTZfZ5lXQcfW4qRo0FxPtjUdfXgyFv33ibOFU0V8Ct9qPs/640?wx_fmt=jpeg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1X4enJ3Jg430Lq35ib6TKMfwMWPxpHxMTQkuB9iaHj8Dj755KsjMFZvicpFQEoIcZc5MiblY9MAMfKjrACxXChC1QibqxBjRdYoSAM/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3X7WGI2rXPqAzCWXrGjRKsN5yjUV9BoibElELIHDAkotuemLyRebpuqevWQ5EkFXCsicicbVEnB6iaAgd8a7hBYX4m430XS37O4CQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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