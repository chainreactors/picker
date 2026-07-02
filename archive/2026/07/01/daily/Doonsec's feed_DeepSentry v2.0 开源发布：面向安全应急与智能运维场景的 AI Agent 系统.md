---
title: DeepSentry v2.0 开源发布：面向安全应急与智能运维场景的 AI Agent 系统
url: https://mp.weixin.qq.com/s/hs7NoZ_GUmtbo_LhumLdyw
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:52:10.542629
---

# DeepSentry v2.0 开源发布：面向安全应急与智能运维场景的 AI Agent 系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PUTQGRQ4GO9wAFTr2ibKicQHoYic5SbHFIZZtwIHLP6bB90lDH2cFu7FheCu7MjIa0EictO7qibTuUyxiaI9K1bWbI1hCfgmiaxCk8l9oszibyIqnT8/0?wx_fmt=jpeg)

# DeepSentry v2.0 开源发布：面向安全应急与智能运维场景的 AI Agent 系统

原创

asaotomo
asaotomo

Hx0极客圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 当安全运维不再需要手动敲命令，会发生什么？

过去几年，安全工程师的日常工作几乎是固定循环：

* 登录服务器
* 查日志（auth.log / syslog）
* 看进程 / 网络连接
* 跑各种排查命令
* 人工分析异常
* 最后整理报告

问题从来不是“不会做”，而是：

> 太多重复工作，太多系统切换，太多信息需要人工拼接

于是我们开始思考一个问题：

> 能不能让安全分析变成一句话？

# 🛡️ DeepSentry v2.0 Ultimate｜深海哨兵

DeepSentry 是一款由Hx0战队开发的面向安全工程师的：

> 🤖 AI Security Agent（一款 AI 驱动的安全应急与智能运维 Agent）

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO9ibxaibwm4aLNjOxkS6vnjcZWbDOGiaxUvVdbFm0lT1nOq0r0icpNVSfDgOGjsmXic6urLoaGN8Kq4BZ7mT4guiavvCTJDWTrEbPQcs/640?wx_fmt=png&from=appmsg)

它不是聊天工具，也不是脚本集合，而是一个可以直接“执行安全工作的 AI 系统”。

# 🧠 它的使用方式非常简单

你只需要说一句话：

> “分析当前服务器是否存在异常登录与可疑进程，并输出风险报告”

DeepSentry 会自动完成：

* 系统信息采集
* 登录日志分析
* 进程与端口扫描
* 网络连接分析
* 攻击行为识别
* 风险评估
* 自动生成审计报告

# ⚙️ DeepSentry 是怎么工作的？

它不是“问答模型”，而是一个执行型安全 Agent Runtime：

> 自然语言 → 任务拆解 → 工具调用 → 多目标执行 → 证据分析 → 报告生成

# 🧩 一个完整流程如下：

用户输入任务

↓

AI 自动拆解子任务

↓

调用 59+ 内置安全工具

↓

执行本地 / SSH / Fleet 多目标分析

↓

聚合证据链

↓

生成 Markdown 审计报告

# 🚀 真实案例：SSH 爆破攻击自动识别

在一次实际测试中，我们让 DeepSentry 对服务器执行：

> “帮我统计今天爆破服务器ssh服务的IP和次数”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO95icYnOg5oE90KGcWCDlHJ9uibrbYKAxrXIWDlBbJjR09tekuaGUH2XLz8FIDOfBlQqWKQJkAFTav8OWBjtQ412ggcBjMPQp63M/640?wx_fmt=png&from=appmsg)

# 📊 它自动发现了什么？

DeepSentry 自动解析/var/log/auth.log，并输出关键结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO87OC25lIHm9jj08pEicggKJNV69Ya3HCNWibPxAY8tmW3pm7l9SfD96ibrFxhUIfFNMS42jQQ1ibZbkfiaBuMSeyOibH22aa0HtR78E/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GOib8FZXvzmI2D5PoTmvDsBatyVNeS3ssVSxZVIbrCbyHq5S6Tnlewsnk298DN5sicO8snWET6UleTIR1KynjIVnu5a5xfHevV8Yo/640?wx_fmt=png&from=appmsg)

🔥 Top 攻击 IP（自动统计）

101.201.31.157 → 11,774 次失败登录

92.118.39.59 → 905 次

45.198.224.154 → 886 次

80.94.92.27 → 652 次

2.57.122.137 → 652 次

# 📈 整体攻击态势：

独立攻击源 IP：

83 个

总爆破次数：

约 18,000+ 次

攻击行为：持续高频 SSH 爆破

# ⚠️ 自动生成安全结论

DeepSentry 不仅识别数据，还会直接输出建议：

* 建议封禁高频攻击 IP（iptables / ufw）
* 启用 fail2ban 自动封禁机制
* 禁止 root 远程登录
* 强化 SSH 密钥认证
* 调整 SSH 端口降低暴露面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO8Aanj4MWgricEyd6OCbuV2gSGqADMsKqVeiayvEEVYOnr2icAlZuGlOFViaMhicypO7LpJtT1IFhBdWq8GvQOv5IhLYicXpyQVT8k6A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOibRolXxvllMxsJnowLkZjRrS6rh7kibTCwWXafuYkRLNiacpza8eQTibe31qwNFNooOiah1tzibs8JWkGwLh11ADypUvI9r7RJdTOJg/640?wx_fmt=png&from=appmsg)

# 🧠 关键点

它不是帮你“看日志”，而是：

> 自动完成一次完整的安全事件分析

# 🧰 DeepSentry v2.0 做了什么升级？

# 🧠 1. 从工具 → AI安全执行系统

不再只是执行命令，而是：

* 自动规划执行路径
* 多轮修正任务策略
* 失败自动恢复
* 多步骤推理执行

# 🌐 2. 从单机 → 多目标 Fleet 系统

支持：

* 本地系统
* SSH 远程服务器
* Telnet 老设备
* FTP 取证节点
* 多机批量巡检（Fleet）

# 🧰 3. 内置 59+ Go 原生安全工具

覆盖：

* 系统审计
* 日志分析
* 网络流量分析
* 进程与文件分析
* Web / DB 探测
* 取证与扫描工具

👉 很多能力不依赖目标机环境

# 📊 4. 自动生成审计级报告

每一次任务都会输出：

* 执行步骤链路
* 命令与结果记录
* 风险判断过程
* Markdown审计报告

👉 可直接用于汇报 / 安全审计 / 留痕

# ⚡ 5. 支持 WebShell / 非交互环境

适用于：

* WebShell（蚁剑 / 哥斯拉 / 冰蝎）
* CI/CD环境
* 无TTY终端
* 应急远程执行

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOib75xnpKONp6y4EBvHaYQ8sWeUicWIdJSvy00rwv51W0C0gCED0uQDeZlDAVpLEVQnoDaYQ9vfMe6SKm2FTtqTKgR7IB8E4h8CM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO8ibMUL193rCWc84OysEDHZJbPXg0icC6yQEInPQfZibibkcbtbSkMt6G2P3iczlqMTEvCvwEKMCZxDBzyno3Wr6PttwbhdfvAiaPMQ4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO8rQibMsCFiafQY3zRjQkhATT15EicZ2pgjgX45q76V2jNg7kzZdeO0K3YbhZ8LQDia4YhT8WWZLpRiczyz5n8uib1VqnRdRLQgBDI9o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO9hqdTWTicvKwqrohr0ojmPLf0NDygHOLia8zRXTksc8REbHheibkakeY8s76x9zuLcygUvvM7pBWTKgwEOMXw4Kh3g1LTs9ysBW0/640?wx_fmt=png&from=appmsg)

# 🔁 6. 支持任务记忆 / 恢复 / 定时执行

支持：

* checkpoint 恢复
* 长任务续跑
* 多轮追问分析
* 定时巡检任务

# ⚔️ DeepSentry vs OpenClaw / Claude Code / Codex

很多人会把它们放在一起比较，但本质完全不同：

# 🧩 OpenClaw

> 通用 Agent 框架

特点：

* 高度可扩展
* 需要自行设计系统逻辑
* 更像“搭积木”

👉 强在灵活，弱在落地

# ⚔️ Claude Code / Codex

> 代码世界 Agent

擅长：

* 写代码
* 改代码
* 跑测试

但问题是：

❌ 不理解真实系统环境（服务器 / 网络 / 日志 / 多机）

# 🛡️ DeepSentry

> System-centric Security Agent（系统即战场）

直接操作：

* SSH服务器
* Fleet多机集群
* WebShell环境
* 网络与流量
* 日志与进程

# 🧠 核心区别一句话总结

|  |  |
| --- | --- |
| **类型** | **本质** |
| OpenClaw | Agent 框架 |
| Claude Code / Codex | 代码助手 |
| DeepSentry | 安全执行系统（Security Runtime） |

# 🧭 为什么要做 DeepSentry？

因为我们看到一个真实问题：

> 安全工程师的瓶颈，从来不是能力，而是效率。

AI 最适合做的是：

* 信息收集
* 日志分析
* 跨系统整合
* 重复排查
* 报告生成

# 🛡️DeepSentry 2.0版本已正式开源

👉 GitHub地址：

https://github.com/asaotomo/DeepSentry

# 🚀 我们希望它成为什么？

DeepSentry 想做的不是工具，而是：

> 下一代安全工作方式的起点

从：

* 人工命令
* 脚本拼接
* 手工分析

走向：

* 自然语言驱动的安全执行系统

# ⭐ 如果你是安全工程师 / 运维 / 红队 / 研究人员

欢迎：

⭐ Star 支持项目

🧠 提 Issue 反馈真实场景

🔧 贡献 Skill / Tool

🚀 一起构建 AI 安全 Agent 生态

# 👏欢迎对深哨感兴趣的小伙伴加入Hx0战队交流群一起交流学习

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUTQGRQ4GO9maHOgGZ2hGBux3jaek75XmJIcIXgykIlMVvGIpmpmbLjhmNyluHVfo8bRgxCsVXibVrs1G8J656RH0sbutxgWWgoNJSrgOIko/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

修改于

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a9DWk35VKuRRhBNEibyEN6qTwMaXdGj1T3BxtacXTgWCia3DICcv8DFhQE6sXWnknbkyOBlHcqrgyauzQKac95Kw/0?wx_fmt=png)

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