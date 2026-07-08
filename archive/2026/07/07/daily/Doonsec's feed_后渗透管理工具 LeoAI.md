---
title: 后渗透管理工具 LeoAI
url: https://mp.weixin.qq.com/s/OKCFIH1pqYixUgFi8g5dqQ
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:01:29.890600
---

# 后渗透管理工具 LeoAI

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVnvhicYdq3Cc3ibuGAMxb0Cdrxqdq1OqCtE0iafMlkGZAiciaXV8xRhXMEPCveXJOEqvRRoh8AeCelNcQlMBp0c4mNN725lMWiaAPyPE/0?wx_fmt=jpeg)

# 后渗透管理工具 LeoAI

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 354，阅读大约需 2 分钟

## 前言

LeoAI 是一款专为红队操作人员设计的后渗透管理工具，深度集成大语言模型（LLM）Agent 能力，实现智能化、自动化的后渗透操作流程。相比传统 WebShell 管理工具，LeoAI 提供 AI 辅助决策、多协议通信、流量伪装、团队协作等企业级能力，内置 Web 管理界面，开箱即用。

项目地址：https://github.com/cha0upup/LeoAI

![e956ace4f5ce3c666e287f39b85a5517.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkuvH4d4JsI0wUmXqVGYvibNT6colDwh60Uk8iaticb4naSl69IhOSwjYWnKKic5BGZuibzzllicEVHiaMnB6rCFWhhBFePoa0BIZPPbo/640?from=appmsg "null")

e956ace4f5ce3c666e287f39b85a5517.png

页面
![1c5c808c561bcd02ca55f40348429431.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkgvXw6QxXCvW12cfyEm9qriaOibekaGm6Pd5icNqaB2c87PTlvDz1RFjK00RVx3V2qTGibyuUhwpn0bBGLQEBwTs0no241Vcn8f1I/640?from=appmsg "null")

1c5c808c561bcd02ca55f40348429431.png

## 环境要求

| 项目 | 要求 |
| --- | --- |
| **Java 版本** | 17 或更高（JDK/JRE 均可） |
| **操作系统** | Linux、macOS、Windows |
| **内存** | 建议 4 GB 以上 |
| **磁盘** | 至少 500 MB 可用空间 |
| **浏览器** | Chrome、Firefox、Edge 等现代浏览器 |

> 无需单独安装数据库：内置 SQLite，首次启动自动初始化。
> 无需额外部署前端：Web 界面已打包至 JAR 文件中。

## jar 包启动

![20f3a5b4297a57a3e2a8563570778de0.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkyXymvYRGtiaFxIT3987bOMAR1C2uibbzTt5lTiaj0QdZ7ODAoZkWQ7RiattK0t2DqdeXKw1P7icRL0yu05dh8e2ia7icQajlibPdwKAc/640?from=appmsg "null")

20f3a5b4297a57a3e2a8563570778de0.png

```
set path=C:\Program Files\Java\jdk-21\bin;%path%
java -jar --add-opens java.base/java.lang=ALL-UNNAMED LeoAi-<version>.jar
```

> --add-opens java.base/java.lang=ALL-UNNAMED 参数不可省略，用于开放 Java 模块系统内部访问权限。

初次启动后
![75aefdbc44fb67fe40a7c613a6403ed3.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmHJnVPk14VoM5OaB3ONXQsHfe8IkIK6pEzBrZTdOQm1ElKYsgPoayJ5h7rIZicQAI04NghDPl3hGVaemvD6577FhMeVF9YwCCg/640?from=appmsg "null")

75aefdbc44fb67fe40a7c613a6403ed3.png

访问

```
http://localhost:8082
```

初始账号密码：admin / 54ikun，首次登录后请立即修改密码。

> 这密码……

![bc6b65cf60cb787e3074ef9ab01b6d60.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlCufOcIltgOoMlz0O633NmGLHdngubdd1JH3gkjmDqrpaVj1yLTnOibOnTic7rUf796XrzJjv0rf5SdG6ymia0n49rW36WJsLG0s/640?from=appmsg "null")

bc6b65cf60cb787e3074ef9ab01b6d60.png

## 支持的 AI 模型

兼容任何遵循 OpenAI API 格式的服务：

| 提供商 | Base URL 示例 |
| --- | --- |
| OpenAI | `https://api.openai.com/v1` |
| 通义千问（阿里） | `https://dashscope.aliyuncs.com/compatible-mode/v1` |
| DeepSeek | `https://api.deepseek.com` |
| Ollama（本地） | `http://localhost:11434/v1` |
| 其他兼容接口 | 根据文档填写对应地址 |

## 总结

项目地址：https://github.com/cha0upup/LeoAI

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