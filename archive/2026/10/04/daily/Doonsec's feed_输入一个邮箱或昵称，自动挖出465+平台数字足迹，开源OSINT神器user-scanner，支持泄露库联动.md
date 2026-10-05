---
title: 输入一个邮箱或昵称，自动挖出465+平台数字足迹，开源OSINT神器user-scanner，支持泄露库联动
url: https://mp.weixin.qq.com/s/cpBneWqwXoXsYG0_7wOEhQ
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:56:48.031894
---

# 输入一个邮箱或昵称，自动挖出465+平台数字足迹，开源OSINT神器user-scanner，支持泄露库联动

# 输入一个邮箱或昵称，自动挖出465+平台数字足迹，开源OSINT神器user-scanner，支持泄露库联动

子午猫
子午猫

网络侦查研究院

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一、单点触发、465+平台并发探测

user-scanner 是 Python 编写的 MIT 开源 OSINT 工具（GitHub Star **4310**）。输入一个邮箱或昵称，可在数秒内并发探测 **175+** 邮箱注册检测站点与 **290+** 用户名平台（TikTok/Reddit/Steam/HackerOne/Codeforces 等），而非简单判“存在/不存在”，还会 DOM 解析提取头像、简介、UID、粉丝数、卖家认证等结构化元数据。

二、自动跨平台关联，形成递归情报链

核心能力 Cross-Scan：扫到 Twitter bio 写“Check my blog at jane.dev”会自动提取域名解析 WHOIS 或 GitHub 绑定邮箱，发现新邮箱即启动第二轮扫描，形成“邮箱至昵称至新邮箱至新平台”递归链。支持 --hudson 直连 Hudson Rock 恶意软件日志库，判断邮箱是否曾出现在被窃浏览器密码、Telegram 日志或勒索受害者快照中。

三、代理自适应、报告多格式、MCP 可接 AI

底层 httpx 加 curl\_cffi 双引擎模拟 Chrome/Firefox TLS 指纹绕过 Cloudflare/Imperva，支持 HTTP/SOCKS5 代理健康预检；扫描结果一键导出 PDF/JSON（可接 SIEM/SOAR）/CSV；内置 MCP 服务器可直接对接 Claude Desktop、Cursor 等本地 AI，让其读取 JSON 报告归纳目标技术栈。适合红队信息收集、离职审计、个人隐私自查三类用户。高频扫描须配代理池并 --delay 限速，部分平台需 --cookies 注入。

情报价值：本文介绍的开源情报采集范式，对网安/反诈侦查有双向意义：一是“输入单点→自动跨平台关联+泄露库联动”正是涉诈资金/身份溯源的刚需能力，可快速勾勒嫌疑人数字画像；二是工具开源、上手门槛低，也意味着黑灰产同样可用，审查时应将“社工库/OSINT 自动化”纳入攻击面评估；三是 --hudson 这类泄露库直连提示：浏览器窃密（Infostealer）已是身份泄露主渠道，反诈宣防须覆盖“被盗浏览器密码→被精准钓鱼”链路。

来源：openklc（KLC开源易选·2026-09-03 06:22 重庆）

![](https://mmbiz.qpic.cn/mmbiz_jpg/mQFl6fQOc0rQz9ZvWQRHEJ9OmGkfMibIicnPK4d1N1znEDVC2ib95N9P6CxdSo09ribgI1sEOQibia0QMG4nAEdFRibasHlME5rlHiaicgHBFMb1KXuE/640?from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/4kCmTUe2v2b9Dn5TZppcYVNqtewpGLM6TUkWg29ayK9yWAJbqViaE15Ltf8AprRumW3Lmw3ibHOAsMYMnhNqcfiaA/0?wx_fmt=png)

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