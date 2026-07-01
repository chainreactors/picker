---
title: 能探测 MCP、LLM 的AgentScan
url: https://mp.weixin.qq.com/s/JfSMeaUsnrJu5RJXiGeOmw
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:20:56.971108
---

# 能探测 MCP、LLM 的AgentScan

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVm76aAgO5pfbAxoZ6D0ZpSHLiaRaqwHGlnIa5AlKEjKCSavfuz4IPoRSQTLvg3zTdFibfsueM2xaIoplv60tuonfK9heUzjzTeSQ/0?wx_fmt=jpeg)

# 能探测 MCP、LLM 的AgentScan

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 354，阅读大约需 2 分钟

## 前言

传统端口扫描器只告诉你"这里有个 HTTP 服务"。AgentScan 继续往下走一层：判断这个服务是不是 MCP、是不是 A2A Agent、是不是开放的 LLM 接口，并输出可用工具、Agent 能力、模型列表和认证状态。

项目地址：https://github.com/7anX/AgentScan

## 能力

| 协议 | 识别内容 |
| --- | --- |
| MCP Server | Streamable HTTP、HTTP+SSE legacy、工具/资源/提示词列表、认证状态、蜜罐信号 |
| A2A Agent | Agent Card、skills、interfaces、无认证 JSON-RPC 可达性、私网地址泄露 |
| LLM 开放接口 | Ollama、vLLM、SGLang、TGI、llama.cpp、Xinference、LiteLLM、FastChat、LocalAI、LM Studio、LMDeploy |

## 使用

```
# 扫域名或 IP
./agentscan scan example.com

# 扫内网段
./agentscan scan 192.168.1.0/24

# 跳过端口扫描，直接验证已知 host:port
./agentscan scan -f targets.txt --skip-port-scan
```

![](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnZiagv84iay90ET5SQ938ABTjhEd8jKy6D0p1wc8C1OL1icAGFYFPPgZh92zD23yAzB7gicxRyQiaeTeA0JBE0U5aDNibGsnh2UH0zA/640?wx_fmt=png&from=appmsg)

### 组合用法

```
# masscan 发现端口，AgentScan 做 AI 协议识别
masscan 10.0.0.0/8 -p 80,443,8000,8080,11434 --rate 100000 -oL open_ports.txt
awk '/open/ {print $4 ":" $3}' open_ports.txt > targets.txt
agentscan scan -f targets.txt --skip-port-scan

# 测绘平台结果二次验证
agentscan scan -f fofa_export.txt --skip-port-scan --mcp-threads 200
```

### 命令

```
agentscan scan   # MCP + A2A + LLM 全协议扫描（最常用）
agentscan mcp    # 只扫 MCP
agentscan a2a    # 只扫 A2A Agent Card
agentscan llm    # 只扫 LLM 开放接口
```

常用参数：

```
-f, --file FILE          从文件读取目标（每行一个）
-T, --threads N          TCP 扫描并发，默认 500
--timeout MS             TCP 超时，默认 2000ms
--skip-port-scan         输入视为已开放的 host:port
--proxy URL              socks5/socks4/https/http 代理
-o, --output FILE        写 JSON；A2A/LLM 自动写 _a2a.json / _llm.json
-v, --verbose            显示探测详情
```

## 总结

项目地址：https://github.com/7anX/AgentScan

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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