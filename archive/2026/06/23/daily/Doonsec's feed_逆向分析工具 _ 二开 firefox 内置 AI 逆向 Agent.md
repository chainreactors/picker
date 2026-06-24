---
title: 逆向分析工具 | 二开 firefox 内置 AI 逆向 Agent
url: https://mp.weixin.qq.com/s/FH6sa3WSMOtsev7Dnk_L3Q
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:01:43.148771
---

# 逆向分析工具 | 二开 firefox 内置 AI 逆向 Agent

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVkwgOR6rKJCFptBia6mnslf4DrlL4XHvgWkibQt9VatSBfAUZwmHjsYbZ2StkhtAtzewCJgYiaVgUequOMAqW9HKeicxZeoqvPZTrA/0?wx_fmt=jpeg)

# 逆向分析工具 | 二开 firefox 内置 AI 逆向 Agent

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 431，阅读大约需 3 分钟

## 前言

内置 AI 逆向 Agent 的 Firefox — 通用 JS/JSVMP/WASM/签名逆向工作站，SpiderMonkey 引擎层非侵入 trace，把加密参数从黑盒还原成不依赖浏览器的纯算法

项目地址：https://github.com/WhiteNightShadow/firefox-reverse

![fec6f5f81e9bc8056d2f8560d78bab3c.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkAFfHdSQdjPrsWUYyI4EaapotuOZiaib7AJmzWccfXIickpbk23cfSqeWFrr4KKwQ0LL6Krf10ljeNQkS4bAylbaXxpEnCQh0GWg/640?from=appmsg "null")

fec6f5f81e9bc8056d2f8560d78bab3c.png

## 使用

从release中下载适合自己的应用，解压后打开

打开 AI 侧边栏 启动浏览器 → 点右侧边栏的 Firefox‑Reverse 工具图标（机器人/逆向图标），打开 Agent 面板。
![04f12bb4dbd0ebe8c2ea470192ee5ebe.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVk1HqAeicpupKPJrVpaRnKL2zZlG935xNkxBbMvNWmS1H8iaRb0UPicsYcXTZebcHmuf04pZs3TMvjQbaRpkEtp1Aia7wT0SgSEbLc/640?from=appmsg "null")

04f12bb4dbd0ebe8c2ea470192ee5ebe.png

配置模型：

> 支持 DeepSeek、智谱 GLM、Kimi（Moonshot）、MiniMax、通义千问（Qwen）、Claude、OpenAI，或任何 OpenAI / Anthropic 协议兼容的自定义端点（填 baseUrl + token + 模型名即可）。

![cb1e672540d7b5675362d6afeb94e758.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmTNYibynW3PUY15jNicyCbeRqt6ibl78t4vIyXZ8CQPnhwm8yNScCrhx1HZicIia8P140XWEXGYAVQdToNj4Tqp9vts5htPScZet0M/640?from=appmsg "null")

cb1e672540d7b5675362d6afeb94e758.png

**两种模式**

* • 全自动 —— 给它目标接口/参数，它一条龙自己搞定（适合放着跑）；
* • AI辅助 —— 它先出方案、每做完一个阶段就停下、给你方向选项，你来拍板、逐步推进（适合边看边学、复杂目标）。

**示例**
把目标告诉它 按下面这个格式把任务说清楚（信息越具体，AI 越少走弯路）：

```
【站点URL】https://example.com/list          # 能看到目标请求的页面
【接口URL】GET https://example.com/api/v1/list?page=1   # 你最终想复现的请求
【目标参数】请求头里的 X-Sign（签名）。若还有其他动态参数（时间戳 / 设备指纹 / token 等）一并列出
【输出目标】① 黑盒可用版：用 Node.js 还原参数生成算法，脱离浏览器独立把接口请求成功
      ② 白盒纯算版：进一步把它还原成不依赖原始混淆代码的纯 JS 实现（可选）
```

然后看它自己抓包、定位、补环境、实打验证。产物（脚本、还原代码、笔记）都会落到你为这个会话指定的工作目录里。

项目地址：https://github.com/WhiteNightShadow/firefox-reverse

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