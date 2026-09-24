---
title: 一款整合型漏洞扫描工具
url: https://mp.weixin.qq.com/s/4349Ypkl0r5B-uAHSTkgxg
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:02:06.313833
---

# 一款整合型漏洞扫描工具

# 一款整合型漏洞扫描工具

点击关注 👉
点击关注 👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj56A4gqVnQoIMLe1kFaS4UxxosIQicUuF7Rric3J0mVsVr0yMfaBpicPdHJ87c9MK84ZSIqiaj2bpEQMptZ9fODEjvicaBdhrePOgQU4/640?wx_fmt=png&from=appmsg)

工具介绍

一款整合型漏洞扫描工具，将 Web DAST、代码 SAST 和 SCA 能力集成于统一界面中。

![](https://mmbiz.qpic.cn/mmbiz_png/AFjuWEpVxULLU7RtG80rTMWjjPGRaPB5roud6dhHn8314sibPSibErkWbtDCcwHPaNX7v8LvxYziaOYPCINNuYEBNP6YQrvMYerW94cWeHb9Eg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

## 功能特性

* **7 个内置扫描器** -- 安全头检查（含 CSP 值检查、Cookie 安全属性）、SSL/TLS（证书 + SAN 域名匹配）、敏感路径探测（~130 条）、信息泄露检测（内部 IP/Email 泄露）、端口扫描（61 端口 + Banner）、源码漏洞分析（10 类模式）、依赖 CVE 检查（10 种格式）
* **9 个外部工具集成** -- Nuclei（全模板类型）、Nmap（TCP+UDP 双扫描）、SQLMap（level=5/risk=3 + WAF 绕过）、Nikto（全部 13 类检查）、ffuf（路径×扩展名×递归）、Bandit、Semgrep（4 个规则集）、Trivy（漏洞+密钥+配置错误）、Grype
* **自定义 HTTP 选项** -- 请求头、Cookies、POST 数据、请求方法；支持粘贴浏览器 curl 命令自动填充
* **CLI 和 GUI 双界面** -- 终端命令行或图形窗口，随意选择
* **HTML + JSON 报告生成** -- 丰富的 HTML 报告和机器可读的 JSON 报告
* **漏洞自动去重** -- 多个扫描器发现的相同漏洞自动合并，减少报告噪声
* **调试日志输出** -- `--log-file` 参数将详细扫描日志写入文件，方便排查问题
* **Cyber 深邃/明亮主题** -- GUI 支持Cyber 深邃（GitHub Dark 风格）和明亮主题切换
* **一键安装外部工具** -- GUI 中不可用工具旁显示"安装"和"浏览"按钮；支持 .exe/.py/.pl/.jar/.ps1 脚本；自定义路径保存到 `~/.vulnscan/tool_paths.json`
* **跨平台支持** -- Windows / macOS / Linux
* **中英文双语** -- 自动检测系统语言或手动切换

## 图形界面 (GUI)

启动图形界面：

```
python main.py gui
# 或直接运行（无参数默认启动 GUI）
python main.py
```

GUI 提供以下功能：

* 目标 URL/路径输入
* 扫描器选择（可单独开关各扫描器）
* 实时扫描进度显示
* 漏洞结果表格，支持按严重级别筛选
* 一键生成 HTML/JSON 报告
* 扫描器状态概览
* 中英文语言切换

## 内置扫描器

| 扫描器 | 类型 | 目标 | 说明 |
| --- | --- | --- | --- |
| HeaderScanner | DAST | URL | HTTP 安全响应头检查 |
| SSLScanner | 基础设施 | URL | SSL/TLS 证书和协议检查 |
| DirectoryScanner | DAST | URL | 敏感路径和文件暴露检测 |
| InfoLeakScanner | DAST | URL | 服务器信息泄露检测 |
| PortScanner | 基础设施 | URL | TCP 端口扫描，含 Banner 抓取 |
| FileAnalyzer | SAST | 文件 | 源代码漏洞模式匹配 |
| DependencyScanner | SCA | 文件 | 依赖组件漏洞检查（通过 OSV API） |

## 外部工具扫描器

以下扫描器需要单独安装外部工具。

| 扫描器 | 类型 | 目标 | 说明 | 安装命令 |
| --- | --- | --- | --- | --- |
| Nuclei | DAST | URL | 基于模板的漏洞扫描器 | `go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` |
| Nmap | 基础设施 | URL | 网络端口和服务扫描器 | 从 https://nmap.org/download.html 下载 |
| SQLMap | DAST | URL | SQL 注入检测工具 | `pip install sqlmap` |
| Nikto | DAST | URL | Web 服务器漏洞扫描器 | `sudo apt install nikto` (Linux)、`brew install nikto` (macOS) |
| ffuf | DAST | URL | Web 模糊测试与路径发现 | 从 https://github.com/ffuf/ffuf/releases 下载 |
| Bandit | SAST | 文件 | Python 安全代码检查工具 | `pip install bandit` |
| Semgrep | SAST | 文件 | 多语言静态代码分析 | `pip install semgrep` |
| Trivy | SCA | 文件 | 文件系统漏洞扫描器 | 从 https://github.com/aquasecurity/trivy/releases 下载 |
| Grype | SCA | 文件 | 依赖组件漏洞扫描器 | `brew install grype` (macOS)、从 https://github.com/anchore/grype/releases 下载 |

使用 `python main.py status` 查看哪些外部工具已安装且可用。

## 项目地址

https://github.com/bbyybb/vulnscan/

内容转自菜鸟学信安，侵删

![](https://mmbiz.qpic.cn/mmbiz_png/INa3lxHH4I2aV3zCmfiaj4cXeQ2HQd6s53wJS36HYI65ib48fujDK8najfWiahicsljzsdT3dfVS8HHyxaviaSd8g2g/640?wxfrom=5&wx_lazy=1&wx_fmt=png&wx_co=1)

#马哥教育17周年双节盛典 进行中

网络安全课程限时优惠

活动时间到10月8日

想学习网安的师傅不要错过

扫码咨询课程

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj56GWlFpAuJBpDq9xgZp8de9R91BMgAgGaf5D4gwsyWl1FR9RN64BiaJqzxqDicCAgoKtwb9LPrZm4c15qTds6Ux29Cda2avFL0mY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2I159AwKj55cnlqsISH0ibpdAZiaQkWZI5QBjejPUH5DjLicyuvKBoe7icAE52TcCtV5siaDpD1r4UCmXbd6aSL3bhDM2dNB4BYLraHavyiaEtpeg/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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