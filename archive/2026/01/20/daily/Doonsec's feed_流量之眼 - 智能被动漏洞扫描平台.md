---
title: 流量之眼 - 智能被动漏洞扫描平台
url: https://mp.weixin.qq.com/s/tPk20E0aI9aQeeWIdS1hHw
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:31:24.031292
---

# 流量之眼 - 智能被动漏洞扫描平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/awCdqJkJFETRlqAibUQvyAdcUNUe4ibGnt6h2d6Ky95BlSWHYAFh1LfiaYwb8bqhgiaM149Q7m1ffLTuAIzibxT6HIQ/0?wx_fmt=jpeg)

# 流量之眼 - 智能被动漏洞扫描平台

YingxueSec
YingxueSec

无影安全实验室

![]()

在小说阅读器中沉浸阅读

免责声明：本篇文章仅用于技术交流，请勿利用文章内的相关技术从事非法测试，由于传播、利用本公众号无影安全实验室所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号无影安全实验室及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！所有工具安全性自测！！！**VX：smile62157**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把"**无影安全实验室**"设为星标，这样更新文章也能第一时间推送！

![](https://mmbiz.qpic.cn/mmbiz_gif/3GHDOauYyUGbiaHXGx1ib5UxkKzSNtpMzY5tbbGdibG7icBSxlH783x1YTF0icAv8MWrmanB4u5qjyKfmYo1dDf7YbA/640?&wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

安全工具

## 0x01 工具介绍

**FlowEye（流量之眼）** 是一款专为安全测试人员打造的 Web 化被动漏洞扫描平台。通过与 Burp Suite 无缝集成，FlowEye 能够实时接收并分析 HTTP 流量，自动进行多维度漏洞检测，帮助安全研究人员高效发现 Web 应用安全风险。

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFETRlqAibUQvyAdcUNUe4ibGntHoXIsbX635HsElO9Tchc4vfarMfiaPWUtWeic2VpRoveNswaiaHfXG4Aw/640?wx_fmt=png&from=appmsg)

为什么选择 FlowEye？

| 特性 | 描述 |
| --- | --- |
| 🎯 **精准识别** | 内置 1000+ 指纹规则，自动识别目标技术栈 |
| 🧠 **智能调度** | 根据指纹结果智能选择扫描引擎，避免无效扫描 |
| ⚡ **高效扫描** | 多引擎并行，支持 Shiro/Struts2/SQL注入/XSS 等漏洞检测 |
| 🖥️ **现代界面** | React + TailwindCSS 构建的精美 Web UI |
| 📦 **开箱即用** | 单文件可执行，无需复杂配置 |
| 🇨🇳 **中文界面** | Burp 插件完整中文汉化 |

## 0x02 工具功能

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFETRlqAibUQvyAdcUNUe4ibGnt5E4BL1whcfJUwQqhooW9ZaClWHkWZyBBuDSE0WCdv3zLR56iaUZAZ8Q/640?wx_fmt=png&from=appmsg)

### 核心功能

* ✅ **零配置启动** - 无需任何配置文件，开箱即用
* ✅ **完全嵌入** - 前端 UI + 字典 + 规则全部内置到二进制
* ✅ **智能指纹识别** - 自动识别 Spring/Shiro/Struts2 等框架（1000+ 规则）
* ✅ **多引擎扫描** - SQLi/XSS/RCE/目录扫描/反序列化等
* ✅ **实时监控** - WebSocket 实时推送扫描结果
* ✅ **漏洞去重** - 智能过滤重复漏洞
* ✅ **Webhook 告警** - 支持飞书/钉钉/企业微信/Slack

### 扫描引擎

| 引擎 | 功能 | 规则数 |
| --- | --- | --- |
| **fingerprint** | 指纹识别 | 1000+ |
| **dirscan** | 敏感路径扫描 | 内置字典 |
| **shiro** | Apache Shiro 反序列化 | 100+ keys |
| **spring** | Spring 框架漏洞 | CVE-2018-1273, CVE-2022-22965 |
| **struts2** | Struts2 RCE | 多个 CVE |
| **sqli-fuzz** | SQL 注入检测 | 100+ payloads |
| **xss-fuzz** | XSS 跨站脚本 | 80+ payloads |
| **lfi-fuzz** | 本地文件包含 | 50+ payloads |
| **nuclei** | Nuclei 模板引擎 | 可扩展 |

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFETRlqAibUQvyAdcUNUe4ibGntog0WwJvp9GXyrWXOhIc8V7G84ZnBNyXhm0DMhXqCdB6nGYqnrkt1qQ/640?wx_fmt=png&from=appmsg)

## 0x03 工具下载

**点****击关注****下方名片****进入公众号**

**回复关键字【260120****】获取****下载链接**

最后推荐一下内部小密圈，干货满满，物超所值，**内部圈子每增加100人，价格将上涨20元，越早进越优惠！！！**

**![图片](https://mmbiz.qpic.cn/mmbiz_jpg/awCdqJkJFET8apEknf7bc6ZR8CyWIBqmV3L88k03ibsUgLfyzvyvuOjkZUfWm9YsK0phQ3owbjBgbhibnWBicgsXw/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&randomid=ebo9tcn3&tp=webp)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFESkGMPLLYOibsOdiaYUbUGH2ibd832G0h4stN7iacicE62hCJGle1IuVQbgGDx5v5GXjwUuE23xJNJjgTg/0?wx_fmt=png)

无影安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFESkGMPLLYOibsOdiaYUbUGH2ibd832G0h4stN7iacicE62hCJGle1IuVQbgGDx5v5GXjwUuE23xJNJjgTg/0?wx_fmt=png)

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