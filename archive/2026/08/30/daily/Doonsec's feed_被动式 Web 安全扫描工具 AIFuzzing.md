---
title: 被动式 Web 安全扫描工具 AIFuzzing
url: https://mp.weixin.qq.com/s/XrwkwwGu0flYevTqN7EtPQ
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:50:25.900419
---

# 被动式 Web 安全扫描工具 AIFuzzing

# 被动式 Web 安全扫描工具 AIFuzzing

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 字数 273，阅读大约需 2 分钟

## 前言

AIFuzzing 是一款基于代理的被动式 Web 安全扫描工具，专注于检测未授权访问和越权漏洞。通过拦截和分析应用程序流量，自动发现潜在的安全问题，并提供智能化的结果分析和管理功能。

项目地址：https://github.com/darkfiv/AIFuzzing

![5cbc5c6391d6773ff45a1679b5d085bc.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVl7OwvQ0mticA0xUm2z9Bfq6uhbwJdyuo5DlJs6pHMNnTicSP3b6Gt5Y4W8SmIRmkO5m0ZFALcoTz80vQvDHia8byR0bKTW4tRhc8/640?from=appmsg "null")

5cbc5c6391d6773ff45a1679b5d085bc.png

## 快速使用

### 1. 启动服务

```
# Windows
AIFuzzing.exe

# macOS/Linux
./AIFuzzing
```

### 2. 配置代理

* • 设置浏览器代理：`127.0.0.1:9080`
* • 安装 HTTPS 证书（首次使用）

### 3. 开始扫描

* • 正常使用目标应用
* • 访问 `http://127.0.0.1:8222` 查看结果

## 配置大模型

配置文件

```
{
  "proxy": {
    "port": 9080,
    "streamLargeBodies": 102400
  },
  "unauthorizedScan": {
    "enabled": true,
    "removeHeaders": ["Authorization", "Cookie", "Token"],
    "similarityThreshold": 0.5,
    "excludePatterns": ["/static/", "/login", "/logout"]
  },
  "privilegeEscalationScan": {
    "enabled": true,
    "similarityThreshold": 0.6,
    "paramPatterns": ["id=\\d+", "userId=\\d+"]
  },
  "AI": "deepseek",
  "apiKeys": {
    "deepseek": "sk-xxx",
    "gpt": "sk-xxx",
    "glm": "sk-xxx"
  }
}
```

### 主要配置项

| 配置项 | 说明 | 默认值 |
| --- | --- | --- |
| `proxy.port` | 代理服务器端口 | 9080 |
| `unauthorizedScan.enabled` | 是否启用未授权扫描 | true |
| `unauthorizedScan.similarityThreshold` | 响应相似度阈值 | 0.5 |
| `privilegeEscalationScan.enabled` | 是否启用越权扫描 | true |
| `AI` | 默认 AI 模型 | deepseek |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png&wxfrom=13)

声明：文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！

如有侵权烦请告知，我会立即删除并致歉。谢谢！

文章有疑问的，可以公众号发消息问我，或者留言。我每天都会看的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png&wxfrom=13)

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