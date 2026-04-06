---
title: 谷歌正式发布 Gemma 4 ：最强开源本地大模型，支持多模态+离线运行，附部署教程！
url: https://mp.weixin.qq.com/s/7BCTsMg41w-6VGZZdtA6dQ
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:38:34.462642
---

# 谷歌正式发布 Gemma 4 ：最强开源本地大模型，支持多模态+离线运行，附部署教程！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVsGZnk2DnnAfKwft0j1rI6KDOtjia2kEG4ydebNcACKvxMRdF8OwaXsR0IytjVPgWGmPomRmDZTHsHOd4WqtgXfRariaF9qmKDLw/0?wx_fmt=jpeg)

# 谷歌正式发布 Gemma 4 ：最强开源本地大模型，支持多模态+离线运行，附部署教程！

灰帽安全

![]()

在小说阅读器中沉浸阅读

谷歌正式发布了迄今为止最智能的开源大模型 —— **Gemma 4**。这次发布可以说在AI圈引发了不小的轰动，因为它主打两个关键词：

本地运行

多模态能力

一经上线，评价普遍非常高，甚至被认为是当前最值得关注的开源模型之一。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVtd94fxIiaI1DpNMSoRqribicr3qicAnWTicWibQxwHm6aqZYDWbkO9SJRQGTeicazEECF55icAIOw3CZVDSQ0Z5p5Guwx97aFhibJgUGZY/640?wx_fmt=webp&from=appmsg)

一、Gemma 4 有哪些版本？

这次谷歌一共推出了 4个不同规模的模型版本，覆盖从手机到高端GPU的全场景使用。

轻量级（移动端 / IoT）

2B（20亿参数）

4B（40亿参数）

 特点：

更低延迟

强调多模态能力

可运行在手机甚至物联网设备上

![](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVvXz8t34L6tR0F6Sd4aDHTHTCmJM8ib78Cia0h2XsaibgVsFQgtPpZf3ricOTHULEIShQvMzg8PQ2Fj4hB3XtZWJIuqK1jicDpTfsGo/640?wx_fmt=webp&from=appmsg)

高性能（本地GPU）

26B（专家混合模型）

31B（稠密模型）

 特点：

支持复杂推理

可用于编程助手、Agent系统

完全支持离线运行

 二、性能到底有多强？

谷歌表示：

Gemma 4 在“单位参数智能水平”上达到了前所未有的高度。

在 Arena-Hard 排行榜中：

31B → 排名第3

26B → 排名第6

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVsK7nZJJ2eiciaHoicVl1JicL5hRmibPBHljMJO4qbyJUX7DwQBmgbiaR7ELic4uImctgj2RZIg8VVxb9lRMTkmR4k1xvvOnic91s3wMpk/640?wx_fmt=webp&from=appmsg)

甚至超过了一些规模大20倍的模型。

这意味着：

效率 > 参数量，真正实现“小模型干大事”

![](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVsQddQHMl1afEGhDAMOSL7Kiao1IZk40fl1fswicHmCoB2FplickABWKyt67QJyeWp0QWicxMZ0AU8Q5TtDuDnHyiatiaZg63Z6ibeGac/640?wx_fmt=webp&from=appmsg)

三、核心能力一览

Gemma 4 不只是一个文本模型，它已经是一个完整的 AI 系统能力集合：

多模态能力

图像识别（OCR）

视频理解

音频输入（小模型支持）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVuOfRnFNlKdfIz2vzOQlFDv7iaJmBF08cUerJoWS9grU1QpByFhHegicXtVfXKfRmBDdKOEE8TwFhPLPC1JqZicOibAT5u5Eex24yg/640?wx_fmt=webp&from=appmsg)

编程能力

离线代码生成

Web开发支持

自动生成 Docker 配置

 Agent能力

自动任务执行

工具调用

工作流自动化

 多语言支持

支持 140+ 语言

隐私 & 本地化

完全离线运行

数据不上传云端

更适合企业/个人隐私场景

可以轻松对接 OpenClaw 小龙虾进行使用

![](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVv42HL4ItY9NR0uOPem6xX6UstPDC8yjA4lsR15J55O5icYYibxsyRpgBEu0icOoGjibG8MBPypxk1eXIdXyTbqDsewaRJDmibicgdico/640?wx_fmt=webp&from=appmsg)

四、开源协议（重点）

Gemma 4 使用的是：

 Apache 2.0 协议

意味着：

 免费商用

 可修改

 可二次开发

 可私有部署

 这一点对开发者来说非常重要

五、本地部署配置要求

根据官方说明，不同版本对显存要求如下：

|  |  |
| --- | --- |
| 模型 | 显存要求 |
| 量化版（Q4） | 最低约 3GB |
| 26B | ~18GB |
| 31B | ~20GB |
| 31B BF16 满血版 | ~63GB |
| 举个例子： | RTX 4090（24GB）  可以运行 26B / 31B 量化版 |

六、如何本地安装（Ollama方式）

推荐使用：Ollama

```
https://www.ollama.com/
```

第一步：下载 Ollama

```
https://www.ollama.com/download/windows
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVsicRJZ83vuhXxVoWJM92goaJFqznTvHoIeXrbtrTYvibrgdXOOTqGQtORiaicVzibHa3flJ19IOTqa5ib37icX3Lq0IaEBGiaq7eMsXJw/640?wx_fmt=webp&from=appmsg)

进入官网下载安装（支持）：

Windows

Mac

Linux

第二步：下载 Gemma 4 模型

```
【HuggingFace】、【Ollama】或 下载满血版【模型打包下载】
```

安装  Ollama 后在CMD终端下执行：

```
ollama run gemma4
```

或者选择适合你显卡的版本（非常重要）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVuEbM33ORq1Jj7QobqfJDEmyV9BkFDkshzqViauRpFpjLyRRVvfINRdP0roFngON3vLHx0Et2QNAS04fgibEXnKI8KnWicYpHS6sc/640?wx_fmt=webp&from=appmsg)

第三步：对接OpenClaw

在Powershell下以管理员身份运行：

```
powershell -c "irm https://openclaw.ai/install.ps1 | iex"
```

安装最新版的小龙虾

安装后在执行命令：

```
ollama launch openclaw
```

即可启动！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVupcK68O0KYPk75V4k3VAgo5zZQErVraS6rnTBXGa9bkbib211B3ApfGC7vmdxVicYicxzOg8cDrOBPws9435bzKBZbn329HVN5nE/640?wx_fmt=webp&from=appmsg)

第四步：对接Claude Code

1、Windows CMD:

```
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

2、macOS, Linux, WSL:

```
curl -fsSL https://claude.ai/install.sh | bash
```

安装后再执行

```
ollama launch claude
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVslyicoSF11icXJUklcbt8KuiaCicjCmwGwPdlnDAxpM23zdQkMjtNpQTb9YtficxMgQudZmBqm9eoCsgEN8HrMtxZic36KPf9IZ1VQs/640?wx_fmt=webp&from=appmsg)

七、实测效果展示

根据实际测试，Gemma 4 表现非常亮眼：

1. 逻辑推理能力

输入问题：

为什么端口映射后外网无法访问？

模型可以：

自动分析网络结构

找出逻辑矛盾

给出排查步骤

 推理能力非常稳定

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVv4juH2j5fbzia4IytGlSBibxJgJmRLF2DtRDWnM4UgribI7wCANpbUK1dm6sKQZu5NWSTKoz9VtcNTbImeNTbju7EGUvf4Yo2P24/640?wx_fmt=webp&from=appmsg)

2. 图像 + 编程能力

上传一张架构图，它可以：

自动识别系统结构

生成完整 Docker 部署方案

 真正做到：看图写代码

3. AI生成游戏

仅通过一张截图

 自动生成一个可运行的小游戏

测试结果：

游戏可运行

有完整逻辑

体验流畅

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVv89xZ3uP48ET7NicUSjlq0fTkz86EkFep84uEwr0vzL0ZGdGS45YdgSptialsD7IzxSHhCmj8hJPnvK4g2PG9iaEhhItVXGyzOiaY/640?wx_fmt=webp&from=appmsg)

4. Agent自动化能力

结合工具后可以实现：

自动抓取新闻

自动翻译

自动生成博客（Markdown）

 已接近自动内容生产系统

八、使用建议（非常重要）

根据你的显卡来选模型：

8GB 显存  选择小模型

12GB  中等量化版

24GB  推荐 26B 或 31B

 不要盲目上最大模型，否则会：

 卡顿严重

 推理速度慢

九、总结

这次 Gemma 4 的发布，可以说是：

开源AI的一次重大突破

它带来的核心变化是：

更强推理

真正多模态

完全本地运行

原生支持Agent

 一句话总结

如果你想要一个能本地运行、性能强、还能做自动化工作的AI模型，Gemma 4 是目前最值得尝试的选择之一。

![](https://mmbiz.qpic.cn/mmbiz_png/1bQDlhHMib4AoxN1uN9D9c1ibdnPviaOD2v7hKY8FBZBx4c0UcuOhGfEI5OibJwQtvSLxHsDWbTib5pSeic0hSOicJwYw/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1bQDlhHMib4Du5uDacz69OWbdwAUlNfCrXUOicJH7wDmzV9CsHbsXjZ5lEDQcHMK6M33ZM0aApjXjcsBNjRqYx1g/0?wx_fmt=png)

灰帽安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1bQDlhHMib4Du5uDacz69OWbdwAUlNfCrXUOicJH7wDmzV9CsHbsXjZ5lEDQcHMK6M33ZM0aApjXjcsBNjRqYx1g/0?wx_fmt=png)

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