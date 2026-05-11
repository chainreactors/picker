---
title: Hx0 鹰眼 v1.0.2 正式发布：AI任务上线，社区版开放拦截模式
url: https://mp.weixin.qq.com/s/sb-T0Wf5-z2ct6ur4VtoAQ
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:52:51.349327
---

# Hx0 鹰眼 v1.0.2 正式发布：AI任务上线，社区版开放拦截模式

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rkE16nqDZNVoP2l5CKwPobLA7sYKlaic9ZICiaQ76rC3a6nXbWX3UANQot35bD4kf5oib3wz11tPsHicOW4zEFXsFx62BoKabbNdP8LmPaiaeL0U/0?wx_fmt=jpeg)

# Hx0 鹰眼 v1.0.2 正式发布：AI任务上线，社区版开放拦截模式

原创

asaotomo
asaotomo

Hx0战队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Hx0 鹰眼 v1.0.2 正式发布。

这是一个面向 Web 安全测试、接口调试、CTF 靶场和授权验证场景的浏览器侧边栏工具。它希望把流量捕获、请求筛选、重放验证、微型 Fuzz、敏感信息识别和 AI 辅助分析，尽量整合在浏览器里完成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNUgch0T2t0nv74xIQIfxmMRJCYQunEAoc0tEN4sW3aerWrxrNKx8YUgeWGqdHRveVib7EKzN1MYSPzvVovjQQZYrqJsPbYTScws/640?wx_fmt=png&from=appmsg)

少切工具，少搬请求，把验证动作留在现场。

项目地址：https://github.com/asaotomo/Hx0-HawkEye

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNWgcYLuEbQZ3iaZn7JqAN5dVeECCIB3AjWXiblsPK8Wibq70C2q85wJLfMzxBMGaCGMicxUoYEbVRTV6O9qrOzM2ex6dXSGlWPAUhU/640?wx_fmt=png&from=appmsg)

# AI任务：智能渗透与 CTF 解题双模式

v1.0.2 的「AI任务」提供两类核心能力：智能渗透和 CTF 解题。

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNUUPrYJ2uQ62W1gjQzmN5OhzzIBFePeNibSQSNQiaich6weT9GCyHvqnzY2n7KY1HrFrS6jN5IlOfrFM18EibFVCJGhas7fUC5lGm0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNU7NsbibHBoQfO6IBJteH1HIfkUibcLsrzmdJSXIo5bc5vB7MjJ7fjgHV8Bmxh3e71DFeHToHtP1nzJc7Q6K161icnvUg4dKL8JlM/640?wx_fmt=png&from=appmsg)

「智能渗透」更适合真实授权测试场景。它会围绕当前站点、历史流量、接口参数、响应内容等信息，帮助你梳理攻击面、生成测试思路、定位可疑入口，并结合重放、Fuzz、响应分析推进验证。它关注的是风险发现、验证路径和证据沉淀，适合日常 Web 安全测试、接口审计和漏洞复测。

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNUMRWHjmibW7I30tib0Dm85qDdpKsYC3cric9RQzRpias2thZjt4JyUzrPNLyMoQq2sck1gajg3MY1RknGEqSoAqIpxjoD9fRIaGtU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNWhlX6Xiahicp05gknRylo1MIoWPSpYrt3ibkeuUKMzKzH1prkg3CK2ywlWBGe3ZgN8l8MaDhicnQSsV21EQhQSH1SjvQQ5u4pPIf8/640?wx_fmt=png&from=appmsg)

「CTF 解题」则更适合靶场和比赛场景。它会根据题目环境、页面线索、请求响应、报错信息和历史尝试，帮助你判断题型方向、拆解解题路径、生成 Payload 思路，并持续围绕 flag 获取目标进行分析。它关注的是快速识别考点、收敛思路和推进解题过程。

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNVvonS1HXt73ywXrJTjv5Fm6n1xGyUSUbJVtBudADm7St8f97SVu1iax5Qq9hpFYultnRsCibpKB3zNicR8picJxVtIB93TF8fgXPM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNXicQsGZg8zwWJfXb27yaJf3VgBJv1EPyMrmgX5fkG1v0RJwhXd9efac0ABAO4qnibqx1CGNUbQYo567XwRvq5PUG3NS92LO0tdw/640?wx_fmt=png&from=appmsg)

简单来说：

智能渗透：面向真实授权测试，重点是发现风险、验证漏洞、整理证据。

CTF 解题：面向靶场比赛环境，重点是识别题型、构造思路、拿到 flag。

这两种模式都不是普通聊天，而是基于当前浏览器现场和流量上下文，帮助你把分析过程变得更连续、更高效。

该能力属于专业版功能，适合更深入的验证、分析与高频工作流。

# 社区版开放拦截模式

为了感谢社区用户的支持，从 v1.0.2 开始，社区版用户也可以使用拦截模式。

你可以在浏览器侧边栏中直接观察请求进入拦截队列，并进行基础处理：

* 查看拦截请求
* 选择目标请求
* 一键放行
* 一键丢弃
* 清空拦截记录

这让普通用户也能完成更完整的请求观察和调试流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNXrVriauKpYmrYzsPGkCwbODrJLibMpo00aUMMm9CzjZibynfbdDtEe9WbaTHdqqic9uFUYMr46rcfkkUGmF8A9oOYA3RmIzomEJKQ/640?wx_fmt=png&from=appmsg)

专业版则继续提供更适合高频测试的高级批量操作与深度联动能力。

# 更顺手的重放与 Fuzz 工作流

Hx0 鹰眼 v1.0.2 继续强化浏览器内验证体验。

在重放场景中，你可以更方便地调整常用请求上下文，例如：

* Referer
* User-Agent
* Origin
* X-Forwarded-For

在微型 Fuzz 场景中，你可以围绕目标参数快速投递 Payload，并结合状态码、响应长度、响应时间、敏感信息命中情况进行判断。

它不是为了替代大型扫描器，而是为了让你在发现一个可疑点时，可以马上验证、马上观察、马上推进。

# Chrome / Firefox 双端支持

Hx0 鹰眼 v1.0.2 同时提供 Chrome （包括可适配基于Chromium的浏览器：Microsoft Edge / 360 极速 / QQ / 搜狗浏览器等）与 Firefox 版本。

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNV5jeKxPx6C4s9iaEXmuGbTFTzQleibrYbiaknnXIBGe417pnZbZapeLKc6GVv4OomOAxZUcjvqDibibkrB5AaD7mH1PjRwK3vgo43Q/640?wx_fmt=png&from=appmsg)

无论你习惯使用哪一个浏览器，都可以获得一致的核心体验：

* 流量捕获
* 请求筛选
* 请求重放
* 拦截模式
* 微型 Fuzz
* 敏感信息识别
* AI任务

# 专业版能力扩展

# 适合哪些人使用

Hx0 鹰眼适合这些场景：

* Web 安全测试
* 接口调试
* CTF 与靶场练习
* 授权渗透测试
* 响应内容分析
* 快速 Payload 验证
* 浏览器现场问题定位

如果你希望有一个轻量、直接、贴近浏览器现场的安全工作台，v1.0.2 值得升级体验。

# 写在最后

Hx0 鹰眼会继续围绕一个目标迭代：

让浏览器里的安全验证更快、更集中、更顺手。

感谢每一位使用、反馈和支持 Hx0 鹰眼的朋友。

v1.0.2 已经准备好，欢迎升级体验。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNXsMShYbGicZb0q8iaodJfnYSEK2wj3ZQAAgxEvSLf4fMORkCxQp9pZ2YRoNJ0auoaOnnia3ywvv454ZCpDgOsH8Y2LlIIQTXicnqA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OC2Q345raO6FzicO8iasjtiavo2jy3hVzbIr7nVhQthvcpzut0ogYTqUOvZQj0ncoVCJoQ2HicXlmrYoJHDXW9uYjQ/0?wx_fmt=png)

Hx0战队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OC2Q345raO6FzicO8iasjtiavo2jy3hVzbIr7nVhQthvcpzut0ogYTqUOvZQj0ncoVCJoQ2HicXlmrYoJHDXW9uYjQ/0?wx_fmt=png)

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