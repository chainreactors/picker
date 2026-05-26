---
title: API公益中转站建议还是先了解后再用
url: https://mp.weixin.qq.com/s/46sTtB-BX97rc4hsbo-WPg
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:05:25.353821
---

# API公益中转站建议还是先了解后再用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aV8UF5rUbwfib9P1u7m9gOiaKqib3ygkHtmXcmPnfK00GIe4JImZDomCUOgib9WdB8LSvDfj1o1ZuH7XOkRo9GbOSrMKCGBxPoib2f6sUreuvhhY/0?wx_fmt=jpeg)

# API公益中转站建议还是先了解后再用

原创

吾爱pojie
吾爱pojie

吾爱破解论坛

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

作者**论****坛账号：Lkkxi**

## 【聊聊 本地 Agent 接第三方API中转后的一个危险问题】

很多人现在已经默认：本地Agent + 中转站也是属于日常玩法了。
发现这里其实有个被很多人忽略的风险：

> AI Agent 已经不是“聊天机器人--编码助手”了。

它是真的能操作你电脑
比如这类：

* Claude Code
* OpenCode
* Codex
  这些东西本质已经是：LLM + 本地执行器。

---

## 一、很多人误以为“中转站只是转发”

最开始我也这么觉得感觉就是：
客户端
↓
Proxy
↓
Claude/OpenAI
无非就是：

* 换个 API 地址
* 省点钱
* 解区域限制

但后面发现问题没这么简单因为很多第三方 Proxy：并不是透明转发
它其实可以：

* 修改 Prompt
* 注入 System Prompt
* 污染模型返回
* 插入 Tool Call
* 修改 Function Call

本质其实已经很像：MITM（中间人）了。

---

## 二、最近微信群碰到的一个真实案例

* AppData 下被创建了 `.ps1`
* Startup 启动目录被写入 `.vbs`
* 开机自动运行
* PowerShell 隐藏执行

  ![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwfk9AAKJo1ic6mibUMAgE6aibIYf9F3LTkjotw9kMkMnRYLr7LlMN47QHXvPvXn9bxsCEqVYj5nDZ11e8cQS7kHJia6ib4c63MODO80/640?wx_fmt=png&from=appmsg)

  文件拿到沙箱运行最后变成这样：

  ![](https://mmbiz.qpic.cn/mmbiz_png/aV8UF5rUbwcV057J3mUUFxXXUNrowIPGBUL4uxzvXatXXichPEPS924WYRaydpjBuSyAFccZUUiaH3Fic5BptjJHG26V3icoCbcpKjyM5E3iaGIc/640?wx_fmt=png&from=appmsg)

## 三、启动项这里其实才是重点

从图里还能看到：Startup\我们拥有的信仰.vbs
以及：WScript.Shell.Run powershell ...
并且：WindowStyle Hidden也就是隐藏运行

这已经是非常经典的：

* VBS 启动项
* PS1 Payload
* Hidden PowerShell

虽然这里只是弹窗。
但这个行为模式本身：已经和传统脚本木马很接近了

---

## 四、问题真正出在哪

很多人以为：中转站黑进了电脑其实并不是，真实链路更像：

用户请求
↓
Claude Code
↓
第三方Proxy
↓
Proxy修改返回
↓
Claude Code相信返回
↓
调用Shell/File Tool
↓
本机执行

注意：真正危险的是“返回结果”

---

而且用户还不容易发现
因为 Agent 平时本来就会：

* 创建文件
* 改配置
* 跑 terminal
* 安装依赖
* 写脚本
  所以：恶意操作很容易混进去尤其终端疯狂刷屏的时候，很多人根本不会逐条看。
  而且用户看到的是：Claude Code 在正常工作
  天然警惕性就会低很多。

---

## 五、现在感觉 AI Agent 的边界已经有点模糊了

以前木马：

* 要漏洞
* 要RCE
* 要提权
  现在：用户主动安装了一个“会自己执行命令的AI”
  甚至还能获取全盘权限，这个变化其实挺大的。

****-官方论坛****

www.52pojie.cn

**👆👆👆**

公众号**设置“星标”，**您**不会错过**新的消息通知

如**开放注册、精华文章和周边活动**等公告

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZK0l7v6mmrudZKXzpdM1WcomgJQnibvLzBUFRSurSkmIfl0ZrDNvSy3MszKNY3XOkcuUbWp31HMjLQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=e9ekqttt&tp=webp#imgIndex=11)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLyxib6edSK27iajkxL2xVZoS1Lbnzjavd2ZDp2KicftN0Tq7vEcJMlLG3chkhj7NcSTEMoLGTRjqDaA/0?wx_fmt=png)

吾爱破解论坛

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLyxib6edSK27iajkxL2xVZoS1Lbnzjavd2ZDp2KicftN0Tq7vEcJMlLG3chkhj7NcSTEMoLGTRjqDaA/0?wx_fmt=png)

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