---
title: Claude Code使用
url: https://mp.weixin.qq.com/s/GfLayOyjyueqaIsXoIJkzg
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:07:54.616690
---

# Claude Code使用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/smrEGbtBXaVyDTHBvhv1nibCvOfaT1owu1CqqmiadQ7qRosMcXCNR77gITlMK0NsNplFW2HI5JQOge91oKuYVIbhOzxiaQdBALfymNEfEw6P3I/0?wx_fmt=jpeg)

# Claude Code使用

原创

信安路漫漫
信安路漫漫

信安路漫漫

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 前言

上一篇文章简要介绍了Claude Code的一些概念，本篇文章来简要介绍一下Claude Code的使用。

# 切换模型

claude默认使用的是sonnet模型，为了使用方便，可能需要切换到国内的模型，下面是切换的方法

1）下载cc switch

https://github.com/farion1231/cc-switch/releases/tag/v3.12.2

下载以后并安装，打开配置页面，如下添加千问模型，其它的模型可以自己查找请求地址

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/smrEGbtBXaXwkKAhBwlSYrEiaZ8UpGUlNdocquckQBokxTCM0Yw6Vcpe4GythdUWn2ibicicsXwbpibmYDRDwr7JJmiatbSn75dT0LODTMXQHJmIk/640?wx_fmt=png&from=appmsg)

2）编辑以后，从新打开claude，输入/model选择千问模型

![0](https://mmbiz.qpic.cn/mmbiz_png/smrEGbtBXaVJ2QDxexdTlryO3LuldHicyiabtuibdDoNFV5dWChMEP1HUoic6UgkQ7ZZT1L10ETicfZv4PrSUnsjmVOGTPQruDKnuqicu02ia2GTqc/640?wx_fmt=png&from=appmsg)

#

# ⌨️ 常用命令速查

Claude Code 的命令主要分为两类：在终端直接运行的 CLI 命令 和在交互式会话中使用的 斜杠命令 (/)。

终端 CLI 命令

这些命令用于启动、配置或执行一次性任务。

|  |  |  |
| --- | --- | --- |
| 命令 | 功能说明 | 示例 |
| claude | 在当前目录启动交互式会话 | claude |
| claude "任务描述" | 执行一次性任务后自动退出 | claude "帮我修复登录页面的bug" |
| claude -p "问题" | 单次查询并直接输出结果 | claude -p "解释一下这个函数的作用" |
| claude -c | 继续上一次中断的会话 | claude -c |

交互式斜杠命令 (/)

在 claude 启动的交互会话中，输入 / 可以触发各种内置指令，极大提升效率。

|  |  |  |
| --- | --- | --- |
| 命令 | 功能说明 | 使用场景 |
| /init | 项目初始化。自动生成   CLAUDE.md   文件，让 AI 记住项目结构、技术栈和编码规范。 | 开始一个新项目时首先执行。 |
| /clear | 清空对话。完全清除当前会话历史，开始全新对话。 | 切换到一个完全不相关的任务时。 |
| /compact | 压缩上下文。将冗长的对话历史总结成精炼的摘要，节省 Token。 | 长时间对话后，感觉 AI 响应变慢或上下文快满时。 |
| /model | 切换模型。在 Sonnet、Opus、Haiku 等不同模型间切换。 | 需要更强推理能力或更快响应速度时。 |
| /plan | 任务规划。将复杂模糊的需求拆解为清晰的、可执行的步骤。 | 开发新功能或进行大规模重构前。 |
| /review | 代码审查。对指定文件或目录的代码进行专业审查。 | 完成一个功能模块后，请求 AI 进行代码质量检查。 |
| /cost | 查看消耗。显示当前会话的 Token 使用量和费用统计。 | 需要监控 API 调用成本时。 |
| /doctor | 健康诊断。检查开发环境和 Claude Code 自身的运行状况。 | 遇到奇怪问题时，用于排查环境配置。 |

![0](https://mmbiz.qpic.cn/mmbiz_png/smrEGbtBXaUmSkmczRDTaZurStdFxxhiabHYicM1IHnhV9K0Fng5a7Fx96h1bQ7ZxtByJh7teXSSmPJwv8IQDMEdTGa395DTgQEJRiaIC2WWWs/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/smrEGbtBXaVyjcp5bAMyvCzZRxJ8BAkiahwozic6R2yUFvWbdzrQfcZhjKQ00Fw64gdk2SyjSNMfCGOPnBpZ18SbrESIl7HZKNX6kf9wk0Rfk/640?wx_fmt=png&from=appmsg)

# skill安装

手动安装（最稳妥的备选）

如果命令行完全无法使用，你可以像安装浏览器插件一样手动复制文件。

操作步骤：

1）下载 Skill：去 GitHub 找到你想要的 Skill 页面（例如 anthropics/skills），下载整个仓库的 ZIP 包并解压。

2）找到目标文件夹：

全局安装（推荐）：进入 C:\Users\你的用户名\.claude\skills (Windows) 或 ~/.claude/skills (Mac/Linux)。如果没有 skills 文件夹，请手动新建一个。

项目安装：进入你当前项目的 .claude/skills 目录。

3）复制文件：将下载好的 Skill 文件夹（例如 frontend-design 文件夹）直接拖入上面的目录中。

4）重启：重启 Claude Code 即可生效。

例如，在https://skillhub.tencent.com/skills/baidu-search下下载baidu-search的安装包，然后放到下面的目录中

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/smrEGbtBXaVXfibEQ87TuPxB1QkBuuDVQJibq9ckySwF2DuWbicUqNEqIupJKibml8N6MfUiaF18bl3dmTibZr85UIRA7WrDGCusCF1UcjxpOibdXQ/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/smrEGbtBXaXpDpLF2bv6vBibNeS7Etibvj6mlmibcHHk86iaeWhPdiaTVh2aVoyuSVOiasY8jInOiaTCic0icic4c7SvuW1IgibVYwg8yawwUIgY94b1bE/640?wx_fmt=png&from=appmsg)

重启claude即可看到这个skill

![0](https://mmbiz.qpic.cn/mmbiz_png/smrEGbtBXaXicXLK40xMCYxnZsljUNwGJkgichsANFlWCgNjyFOqfgSAZkfRDd9ribUvF8jIoeWakfibicRUJibjyDQqTJDJMFwu16B1ILlsfvzK4/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Rzo6rPw2nBzeSE9F8n8h6enwOQRic7J3SE7afEypJIw6rfTP291hkrrVzeuGMOlj17RGwbv8wJibtdQnmamtGNmQ/0?wx_fmt=png)

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