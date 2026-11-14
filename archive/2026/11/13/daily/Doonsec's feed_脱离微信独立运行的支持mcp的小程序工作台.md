---
title: 脱离微信独立运行的支持mcp的小程序工作台
url: https://mp.weixin.qq.com/s/f-QKij3cGs_A-pgI6UZMZg
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:18:56.151066
---

# 脱离微信独立运行的支持mcp的小程序工作台

# 脱离微信独立运行的支持mcp的小程序工作台

原创

Huo
Huo

荧惑安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 脱离微信独立实现的支持mcp的小程序工作台

> 完全脱离微信、扫码登录、小程序搜索、独立启动、运行时调试、代码还原，收在一个工具里。

## 声明

本工具仅面向**本人所有或已获明确授权**的目标，以及个人学习与研究。使用前请确认目标归属与授权范围，并遵守相关法律法规与平台条款。因违规使用产生的一切后果由使用者自行承担，开发者不承担任何责任。

## 它解决什么问题

做小程序方向的测试，流程往往被切得很碎：找入口用一个工具，调试换一个窗口，想拿代码又得另想办法。

小程序工作台把这些步骤连起来。从扫码登录到看到代码，中间不需要换程序。

![](https://mmbiz.qpic.cn/mmbiz_png/t1ibwWAEoQpzQk0QATlNZd30YAn078hGVMr8JqNohldleiaCS5GziaVAa6FFEpGxAkkPchkdYsJPAOiclW5douly777hYqIrRLQrduibGHYdEX7A/640?wx_fmt=png&from=appmsg)

## 能做什么

* **扫码登录**：微信扫码，账号留在本地，过期会提醒。
* **检索**：在线搜索与本地索引两条路，没有网络也能查。
* **独立启动**：自带运行环境，打开就能跑，不需要额外配环境。
* **运行时调试**：页面状态、控制台输出、请求记录、异常信息都能看；想验证点什么，直接求值。
* **代码还原**：加密的包可以在本地还原成工程目录，长任务后台跑，进度实时可见。
* **agent 接入**：全部能力都开放成 MCP 接口，agent 可以直接操作整套流程，人只看结果。

![](https://mmbiz.qpic.cn/mmbiz_png/t1ibwWAEoQpzjarbGUURko872TQSxDWqsZIuYxIk3MnbEa3UA9fqaAtlk3BkOo7QQNheYZdgG5wjFXuwCIznc63QFBQTbmq1YIyMiakP0icDDI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/t1ibwWAEoQpxEYicyeO1mcKvgsfRQAXAfyjbhjMzkaxQKLvnH9GibGGFoG8AlcEuSSSc7EvxrvLrttm89dfvySSoicHMhwgOFlQOw8NHhn0ibyd0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/t1ibwWAEoQpwNrrCtXJXIfz8ESpRhibTIAXibEvP1cjujPic8NBqJTbRWISvvbtCmQ4H6NJUJ5iaJwTxozYExrMab7bOmGsStElNyn9ywC0kZyRg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/t1ibwWAEoQpwsbD0icjxz8kt1R164VHahDlRu5HovrVHrGleuicvpt0GPJlzraqIDicichnh82mqP55VcgTH7Fmib2ribgFviaTfhBmqictvictibv5ptI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/t1ibwWAEoQpzic01qm2AO6CYgl5dbaAmwraPuMte4cYT18RKaYOnw3eMBgSBqdaUfrUBfMAzsnnhgC9D6qTHmKOYS9cbCib2nh9CEpTxYRibl5I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/t1ibwWAEoQpxtLoaqynr8p1ULXoGNg14VecTIS7GWN7VmvA6QtcErmeSk4FSLkborSSl8jF964VJ0ECefwXWvFZr3QHWicyGpC4iaP8uVIgluM/640?wx_fmt=png&from=appmsg)

适合谁

* 做小程序、小游戏安全研究的人
* 需要复现问题、观察运行时行为的开发
* 想把小程序调试接进 agent 工作流的人
* 单纯想看看手里的小程序在干什么的人

## 说明

工具在持续迭代，版本 `1.0.0`。

部分小程序的 worker、插件与媒体能力以实际兼容情况为准；还原出来的是运行时产物，不等同官方工程。

## 交流

提问题、功能建议等，欢迎在公众号留言。

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/u0lDOJgUr2tYhibueKpabiaV2mGm8q4IMcoe0Cn9zAlIYicJMiazNJCTUbHzDHEKLicVF9rxHo6obSRAJpXofocc7nQ/0?wx_fmt=png)

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