---
title: 【工具推荐】Zack-AI-Scanner
url: https://mp.weixin.qq.com/s/jAHcooCT_oh49wWShWq44Q
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:58:30.830953
---

# 【工具推荐】Zack-AI-Scanner

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DRNXoxlicJJtXeW8ia6BdKuEghZ2AS4yAfia7PaMaVgebjPicxdmicGL85oIcDu1yt2nVBXpUaSRvXYJ5l1ibeaITTnQ9M2aI4zPI4ygmy6GmDCqg/0?wx_fmt=jpeg)

# 【工具推荐】Zack-AI-Scanner

原创

CatalyzeSec
CatalyzeSec

CatalyzeSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 工具介绍

    Zack-AI-Scanner 是一款基于大语言模型的自动化 Web 漏洞扫描工具，作为 Burp Suite 扩展运行。随着大模型技术的快速发展，AI 驱动的安全测试正在改变传统渗透测试的工作流——从手工构造 Payload、逐条分析响应，转向由模型自主理解请求语义、动态生成测试策略并验证结果。Zack-AI-Scanner 正是在这一思路下诞生的产物。 它通过集成 OpenAI、Claude、Gemini、通义千问、DeepSeek 等 16 家主流大模型服务商，将 AI 的语义理解能力嫁接到 Burp Suite 的代理流量上。用户只需在 Burp 中选择目标请求，插件即可自动分析 HTTP 特征，识别潜在漏洞类型，生成针对性的测试 Payload，并通过 AI 二次验证确保漏洞真实性。支持 17 种常见 Web 漏洞类型，内置 WAF 绕过策略，适合在攻防演练、SRC 挖掘与授权渗透测试中快速梳理 Web 攻击面。

# 安装使用

插件基于 Java 17 编译，使用前请确认 Burp Suite 自带 JRE 版本不低于 17。安装流程为标准的 Burp 扩展加载：

![](https://mmbiz.qpic.cn/mmbiz_png/DRNXoxlicJJtqxtTTqP5Gm0pf4oSJKHlSdWXicsFgSPJytpCn8icAfOJpoyszlpRjQZKsSaq8w6Zyfq1OqibWPrDMrh18xGibWmQPCPStbTSCqC4/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/DRNXoxlicJJtK0JPQ4CoNHZLtN6M3oBibVDZoy8oQ2fuiaEUaepB28EmmJlKHUYMQ6O8vW6khibRqFvmbS8JqN1ERW3neSrVXoKqa4GmZuxGQ80/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/DRNXoxlicJJvMXDN22tJndppNLBK9eTic2V9UIcRjXNyvStkGxjAn8azMhrgfdeVwibFLAXYnTsJZb6Hszz6icrbvsqGGVbwKe5JAqiaOryYskY8/640?wx_fmt=png)

功能及特点相较于传统的手工测试或规则型扫描器，本插件主打「AI 驱动 + 语义理解」路线，利用大语言模型替代固定的 PoC 模板，显著提升了对非常规注入点和业务逻辑漏洞的覆盖能力。

```
项目地址：https://github.com/ZackSecurity/Zack-AI-Scanner
```

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/EqMwaEZz0ykH1KHFqibib8xIJtOkJbKW7UIiapCYNUtnwa99blUPhUWE1X554Q7GCRtPLghVWT4WvT4D8OEMvtVHQ/0?wx_fmt=png)

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