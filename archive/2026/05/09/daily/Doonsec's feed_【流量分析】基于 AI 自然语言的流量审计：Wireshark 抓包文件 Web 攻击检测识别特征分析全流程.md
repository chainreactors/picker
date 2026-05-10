---
title: 【流量分析】基于 AI 自然语言的流量审计：Wireshark 抓包文件 Web 攻击检测识别特征分析全流程
url: https://mp.weixin.qq.com/s/JVN_uJLp4HUx17MBnksbPg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:35:58.796992
---

# 【流量分析】基于 AI 自然语言的流量审计：Wireshark 抓包文件 Web 攻击检测识别特征分析全流程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EZicQGyMXoOn4WiaC4HHLZFG77c36ibn39xw8GcZDDUwh6U65IIINibe3Q0hEsbyaNdibnDw3YL3S9ABST2ibzE6trd1lboblXVBXWIXWk1e9SaH8/0?wx_fmt=jpeg)

# 【流量分析】基于 AI 自然语言的流量审计：Wireshark 抓包文件 Web 攻击检测识别特征分析全流程

原创

渗透测试
渗透测试

渗透测试

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOmb7tlU2Ez7f559NjnW3Zv57CAg7H4LCeibw6HLsloI7fl87c3urcpiaqSbS40HNqJ45H4MD8gkHVK63Z8wn9febXmd5Rn8SdT1o/640?wx_fmt=other&wxfrom=13&wx_lazy=1&wx_co=1&randomid=d3ftoiiz&watermark=1&tp=wxpic#imgIndex=0)

**点击上方蓝字******关注【渗透测试】不迷路****

    1、实战演示：以Wireshark 抓包的 hacker2025.pcap 流量日志为例，演示用 AiScan‑N 审计 PCAP 流量文件，识别WEB 扫描 IP 数量、攻击途径等安全特征。

    2、工具配置：通过CC Switch统一配置并切换 Claude、Codex、Gemini CLI、OpenCode、OpenClaw 等 AI 工具，实现与 AiScan‑N 的对接调用，完成 MCP 管理面板配置与验证。

相关文章参考：

[AiScan-N 不止于此！一款基于人工智能驱动的Ai自动化网络安全（运维）工具【CLI Agent】](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247486777&idx=1&sn=d8f140a775224b8d14e050804500f98f&scene=21#wechat_redirect)

[【Ai渗透神器】AiScan‑N Ai自动渗透测试 | 助力CTF网络安全大赛，开启智能防护新篇章](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247486744&idx=1&sn=8a247f091498ada202e8b5ad987f3f14&scene=21#wechat_redirect)

[本地离线大模型DeepSeek‑R‑14B&Qwen3+ AiScan‑N助力CTF网络安全大赛|内网快速扫描，无需访问互联网！](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247486742&idx=1&sn=18de251b3bb1792abff297d4a38d6eb8&scene=21#wechat_redirect)

[【神兵利器】Ai全自动化渗透测试工具 | AiScan-N带你开启智能安全的新时代！](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247486594&idx=1&sn=ad542da6bc27d132bce6006e3b61805a&scene=21#wechat_redirect)

[用Ai做自动化渗透测试对CTF题目进行解密|CTF网络安全大赛](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247486619&idx=1&sn=21e0ee188906bad707c3fc6bc15d2785&scene=21#wechat_redirect)

[本地部署网络安全相关的大模型及安装使用方法+ AiScan‑N助力CTF网络安全大赛|内网快速扫描，无需访问互联网！](https://mp.weixin.qq.com/s?__biz=Mzg2ODY3NDYxNA==&mid=2247486965&idx=1&sn=e0ef8d7decc3583167b9b5e59edc0299&scene=21#wechat_redirect)

## 环境准备及工具

```
操作系统：Microsoft Windows 11 家庭中文版, 版本 10.0.26100CPU：13th Gen Intel(R) Core(TM) i7-13700HXClaudeCC SwitchAiScan-N  项目地址：https://github.com/SecNN/AiScan-N hacker2025.pcap 日志文件DeepSeek 官方大模型
```

本地离线AI大模型是直接部署在你的电脑上，配置低的电脑使用本地大模型分析日志性能可能欠佳，建议使用云模型。

## 1️⃣ 日志分析实战演示：Wireshark抓包的日志文件PCAP 扫描攻击特征分析

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOmxWmggy5ibg9Bq94iaw0v2hoCgL5ELEHUxDQIa0xFWKs4TC0Yl7boPFeKNf71ZIY686icz4Qm2aAHcM3Kme9NJ3NxBJ0Enqhrb2A/640?wx_fmt=png&from=appmsg)

```
帮我分析/home/aaa/AiScan-N2.0/hacker/hacker2025.pcap 文件，审计该流量文件，分析有多少个IP存在WEB扫描的特征。&&帮我分析/home/aaa/AiScan-N2.0/hacker/hacker2025.pcap 文件，审计该流量文件，分析有多少攻击途径，我需要详细的结果。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOmP6gzrbDib2siaNPCYOTEmJcSB3luq16IHMqByibLJy4ZIuaFcryFWU24ZpyHyXicibkKnoW7EdUK227L0nCLkoiaZGjxISUicyc8uLA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOn5sOJYUsgbCpyLnSnzuweXAkw4HQCLMoQJqPAhZIwyTSRk92UCSHzxYHckx6owM5VoJV0UUFBjTLAZmUnhm17P0yBBG0zOeTI/640?wx_fmt=png&from=appmsg)

流量文件的深度分析，**共发现 32 个IP地址存在明显的WEB扫描特征**。这些IP地址均向目标服务器（主要针对8080端口）发送了大量带有扫描特征的HTTP请求，包括对敏感路径的探测和使用扫描工具特有的User-Agent。

### 分析概要

1. **分析方法**：

* **可疑路径**

  ：请求路径包含 `.git`、`.env`、`admin`、`phpinfo.php`、`backup` 等常见漏洞扫描目标。
* **扫描工具User-Agent**

  ：请求头中包含 `nikto`、`sqlmap`、`dirb`、`gobuster`、`acunetix` 等已知扫描工具标识。

* 使用 `dpkt` 库解析pcap文件，提取所有HTTP请求（GET/POST/HEAD等）。
* 通过以下特征识别WEB扫描行为：
* 统计每个源IP的请求总数、可疑请求数、扫描工具User-Agent出现次数，并综合判断是否为扫描行为。

2. **关键发现**：

* 共识别出 **32 个源IP** 发起了HTTP请求。
* 所有32个IP的请求均触发了至少一项扫描特征（可疑路径或扫描工具User-Agent），因此全部被判定为存在WEB扫描行为。
* 大多数IP的请求量极大（最高达2455次请求），且可疑请求比例高（平均约30%-40%的请求为可疑路径）。

### 存在WEB扫描特征的IP列表

| 序号 | IP地址 | 总请求数 | 可疑请求数 | 扫描UA次数 |
| --- | --- | --- | --- | --- |
| 1 | 192.168.37.1 | 4 | 1 | 0 |
| 2 | 192.168.37.4 | 10 | 0 | 4 |
| 3 | 192.168.37.10 | 127 | 113 | 1 |
| 4 | 192.168.37.34 | 2455 | 827 | 534 |
| 5 | 192.168.37.35 | 2409 | 812 | 537 |
| 6 | 192.168.37.36 | 2377 | 808 | 502 |
| 7 | 192.168.37.37 | 2386 | 809 | 497 |
| 8 | 192.168.37.38 | 2389 | 810 | 507 |
| 9 | 192.168.37.39 | 2370 | 804 | 500 |
| 10 | 192.168.37.40 | 2392 | 811 | 466 |
| 11 | 192.168.37.41 | 2313 | 782 | 469 |
| 12 | 192.168.37.42 | 2355 | 794 | 495 |
| 13 | 192.168.37.43 | 1902 | 624 | 395 |
| 14 | 192.168.37.44 | 1957 | 636 | 427 |
| 15 | 192.168.37.100 | 1807 | 606 | 380 |
| 16 | 192.168.37.101 | 1714 | 568 | 313 |
| 17 | 192.168.37.102 | 2196 | 721 | 448 |
| 18 | 192.168.37.103 | 2055 | 671 | 437 |
| 19 | 192.168.37.104 | 1785 | 593 | 360 |
| 20 | 192.168.37.105 | 1736 | 573 | 381 |
| 21 | 192.168.37.106 | 1559 | 518 | 350 |
| 22 | 192.168.37.107 | 1263 | 474 | 294 |
| 23 | 192.168.37.108 | 1166 | 433 | 248 |
| 24 | 192.168.37.109 | 1593 | 518 | 321 |
| 25 | 192.168.37.110 | 1682 | 540 | 355 |
| 26 | 192.168.37.111 | 1822 | 613 | 415 |
| 27 | 192.168.37.112 | 2195 | 739 | 480 |
| 28 | 192.168.37.113 | 2249 | 760 | 476 |
| 29 | 192.168.37.114 | 2089 | 675 | 471 |
| 30 | 192.168.37.115 | 2219 | 755 | 454 |
| 31 | 192.168.37.116 | 2217 | 754 | 475 |
| 32 | 192.168.37.117 | 1819 | 611 | 417 |

### 结论

该流量文件记录了**一次规模化的WEB扫描活动**，涉及 **32 个不同的源IP**，这些IP均向目标服务器（端口8080）发起了带有明显扫描特征的HTTP请求。

2️⃣在Claude/ Codex / Gemini CLI / OpenCode / OpenClaw 等工具在配置AiScan-N

        CC Switch 是一款用于统一管理多个 AI 编程工具（如 Claude/ Codex / Gemini CLI / OpenCode / OpenClaw 等）配置和切换模型的工具，以下是其常见使用方式：

安装

    从 GitHub 发布页面（https://github.com/farion1231/cc-switch/releases） 下载对应操作系统的安装包（Windows 为 .msi，macOS 为 .dmg 或通过 Homebrew 安装，Linux 为 .deb、.rpm 或 .appimage）。

启动 CC Switch 应用程序

1. 已安装 Claude / Codex / Gemini CLI / OpenCode / OpenClaw（至少一种）。

2、添加供应商（API 配置）打开 CC-Switch，顶部选择对应工具分组：Claude / Codex / Gemini。

3、点右上角 +（Add Provider）。

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOlGQpvcK3iav7CGVM9aQeXD5KejC3ic7N72cxQ4Vh6C70U4haiaWfYseibYnBbVeGTokcZtm8M7OmqrQpjL0XJMLSlZvKOCU612fOY/640?wx_fmt=png&from=appmsg)

根据页面提示填写大模型相关信息。

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOlmibrsJb4cpUIY9EfsJ224dEwShPk8JtPWW9SMPwicye1iar8wGicBH0AYsMyJeB9QQlVOZVfiaIKTFwlqCibtfarRsKgfMwp9Fowes/640?wx_fmt=png&from=appmsg)

配置完成点击启用，重启终端 / 客户端

完全退出 Claude Code

重新运行：claude

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOnCibic9wWRzEhvrtJqzBzqVxXiaeSlNafXdDtugPJHjutf0qCnCZGWm7icSEf6SzicbpvsejqxytLcORh7D8WCQWdgcfxicXib0m7vQU/640?wx_fmt=png&from=appmsg)

发送测试消息，正常回复即证明大模型配置生效。

进入 MCP 管理面板

1. 打开 CC‑Switch

2. 顶部点 MCP 标签页（右上角）

```
一次配置可同步到 Claude/ Codex / Gemini CLI / OpenCode / OpenClaw
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOnVlqdmd2UbvZOe1PWarCZicHKLsMB7bX18jIic3icas0wEfP1sSmCmAoZSHKoWhhzDX7zNMLNtRicDqMPzJSHpTTg4uRKAyLEBiajU/640?wx_fmt=png&from=appmsg)

添加MCP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOkqj9pc8LPNSWibDQA6RDurD5cExv0arxK9LPJg3AnNItIRg8MeKjmYfibciaoKM9HkIO1sWYSXq6icSe2Hg5rvqCxYxSPNu18gqbM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOlEK48iaZsbk26MYXvQxOD4o3EIRX6Z0C1fCsRicBnBjPWvTOYcOla0WXtCVTEdaaYg3ePelj3bp4AHdsHibTMddPUiap5TuGp3Gjs/640?wx_fmt=png&from=appmsg)

保存

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOnQbq2rXZNNC6iap9vdull5ErRKLqszickQulZQ4jypRj0rEBBgHN4blLwPgr2rjs2nOayK9iaqKmStNgGn1jWic3clibGtXttagO9o/640?wx_fmt=png&from=appmsg)

验证是否生效

1、完全退出：Claude / Codex / Gemini CLI / OpenCode / OpenClaw

2、重新启动：Claude

输入

```
/mcp
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOkqjkY9QRfq7fTFTpLVePD9sUISzfzAOj4nMbPKZYarI27dibKwljtXc9hicC2wNgccATl9rxrPX0CqMG2EXsR9NTuicjhYldOvPU/640?wx_fmt=png&from=appmsg)

出现AiScan-N

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EZicQGyMXoOkmhYZLGWq2MwfIzjbg38JnsUqcTs4HEztZiaecy7xcKf5m03DsTKlIygghWPpKnvnJRH9wR0oZLTnbGelMeYEWaIF7rnfTTulg/640?wx_fmt=png&from=appmsg)

查看工具

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOmSkKalYrPnu67myc3wpvjADj9H3mMgGPyKMichGmVibzo2Jd4u53ic2HIqrNYHcKCJZOJAU0VTS8WJKmKKhO9yVjqQbcVw89Nvnw/640?wx_fmt=png&from=appmsg)

出现以下内容说明Claude与AiScan-N连接成功

![](https://mmbiz.qpic.cn/mmbiz_png/EZicQGyMXoOkHiauJlb0jNMl24l4ueTvXcXBtqib3ANr41APAhlAMNuqcFpuy1oqbbZTR7T6H2bWTxPRaiaJSlWRrVZ6pO7CeF3MwXibkklQo41M/640?wx_fmt=png&from=appmsg)

Claude中调用

```
参考提示词： https://secnn.com/admin.php/login/index.html  这是一个thinkp...