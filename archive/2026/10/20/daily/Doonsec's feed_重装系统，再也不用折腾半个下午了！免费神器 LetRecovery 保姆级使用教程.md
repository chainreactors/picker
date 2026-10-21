---
title: 重装系统，再也不用折腾半个下午了！免费神器 LetRecovery 保姆级使用教程
url: https://mp.weixin.qq.com/s/m0TS9ww8Qq4cqTwWcr32kA
source: Doonsec's feed
date: 2026-10-20
fetch_date: 2026-10-21T06:48:28.969677
---

# 重装系统，再也不用折腾半个下午了！免费神器 LetRecovery 保姆级使用教程

# 重装系统，再也不用折腾半个下午了！免费神器 LetRecovery 保姆级使用教程

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

教程预计阅读 5 分钟 · 共 1855 字

重装系统，再也不用折腾半个下午了！免费神器 LetRecovery 保姆级使用教程

系统重装 · 保姆级

#LetRecovery#开源#WinPE#免费

READING PATH

阅读路线

5 个章节

01

核心亮点速览

-

02

详细使用过程

-

03

其他常用功能快速上手

-

04

注意事项

-

05

下载与反馈

重装系统这件事，对很多电脑用户来说简直是"烫手山芋"。

刻录启动U盘、进BIOS改启动项、进PE、挂载镜像、解压镜像、找驱动、处理分区、遇到BitLocker还得先解锁……一整套流程下来，轻轻松松半个下午就没了。家里人电脑出问题，帮忙重装更是费时费力。

今天安利一款真正能大幅简化这个过程的工具——LetRecovery。

一款免费、源代码公开的 Windows 系统重装工具（GitHub 已收获 2.1k+ Stars），采用`PolyForm Noncommercial 1.0.0`许可，个人非商业使用完全免费。支持桌面端直接操作，也能自动切换到`WinPE`完成部署，真正实现"一键重装当前系统盘"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfxic1He6D43L4keCoAAbiaicTcm9WQupjsZ9CuChWkwWqibbfF4fJpnG47Rd2xOVZ9a6v9EK2g1QDBGmEH1ANDfBpmjaicuIdpQ2xBE/640?wx_fmt=png&from=appmsg)

CHAPTER 01

**01****核心亮点速览**HIGHLIGHTS

4 IN 1

四大核心亮点

1

多格式镜像全支持

WIM、ESD、SWM、GHO、ISO 统统通吃（包括 Windows XP/2003 的 i386 文本模式安装），自动挂载解析，多分卷/多版本一键选择

2

桌面端 + WinPE 双端协作

在正常 Windows 里就能操作。重装当前系统盘时，自动写引导、重启进内置 WinPE 完成后续部署，无需提前做启动U盘、无需手动改BIOS

3

BitLocker 加密盘直接处理

遇到 BitLocker 加密的系统盘，自动解锁/解密后再安装，省去手动关闭加密的麻烦

4

丰富工具箱

系统备份（完整/增量）、密码重置（在线/离线）、无损扩大C盘、驱动导入/导出、一键分区、分区对拷、镜像校验、引导修复等常用维护功能一应俱全

另外还支持在线下载系统镜像和常用软件（Aria2 多线程加速）、无人值守安装、`UEFI/Legacy`自动识别、WiFi 配置迁移等实用功能。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfw1NGRJhJuqygib5kytZf3v4sUN4SkIBibiaZrkN3xcg2R8s5rkI1pVULkxGcvOcdr3xYrgo2bASlQzAeibpPThNQQga3Vgw8ql83k/640?wx_fmt=png&from=appmsg)

CHAPTER 02

**02****详细使用过程**TUTORIAL

以重装当前系统为例。安装会格式化目标分区，请提前备份重要数据到其他盘或移动硬盘！

**系统要求**：Windows 7–11 64位（桌面端），至少 4GB 可用内存，管理员权限。推荐从官方渠道下载最新版，避免第三方修改版本。

5 STEPS

五步完成系统重装

1

步骤一 下载软件

前往 GitHub Releases 下载最新版 ZIP，解压即可

2

步骤二 以管理员身份运行

右键 LetRecovery.exe → 以管理员身份运行

3

步骤三 选择镜像

本地镜像或在线下载，自动解析版本列表

4

步骤四 选择目标分区

选C盘，按需勾选高级选项

5

步骤五 开始安装

点击开始安装，重启后 WinPE 自动完成部署

01

下载软件

前往 GitHub Releases 页面下载最新版 ZIP 压缩包，解压到任意位置（绿色免安装）。也可访问官网 letrecovery.net 获取。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfxpTdjG1b9DKjt2kBvZ0EL0Or0icN9axFCic9HBiaUrAEgemcAzdHBzVpb5F4TaHZ72bibQjRgf9KGMZ9fjmKACOEU2RR2tZOAEZRQ/640?wx_fmt=png&from=appmsg)

02

以管理员身份运行

右键点击 `LetRecovery.exe` → 选择"以管理员身份运行"。首次运行可能提示防火墙拦截，请允许。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfxl1Kibr8mVYibuLibFu7yI8HjYVOhQmZEuiaMf1fjFIEA6icu69249ov12b1RpUia3KCs4hfydyfKG2GuS2UpClcM8I8yFHAd24qtDA/640?wx_fmt=png&from=appmsg)

03

选择镜像

进入"系统安装"：本地镜像点击选择 WIM/ESD/GHO/ISO 文件，程序自动挂载解析版本列表；在线下载可直接搜索官方镜像，Aria2 多线程加速。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfwCIVNh6AwLsnxnof0j8GnNZyrtu7joC0SQcf24KTADNH6f0k75LdlpIcH8eVqT2NOOu4fVteDLtbevrfKfynKcPNJHNHKPpibw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfw8VIZbE0y9qZXTwckWrk4ozbWExTbHl8nwpfHQSurwaXMZUhPSzdgFjoOBU9VclOCN1kYibOiboQFv5dUTxBibzGhKVGBwaKHamc/640?wx_fmt=png&from=appmsg)

04

选择目标分区

选择要安装系统的目标分区（通常是C盘）。高级选项可勾选：格式化分区、引导修复、驱动导入、移除预装UWP、OOBE绕过联网、WiFi配置迁移等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfyvzqn3YKDyViajiaaOiaVCykXaYicl1Zic8JJ8B8O1CDTus8Wum4w4JPLsRGXicJxPwvt9BlQZ2pqiatWOZVYEtEoCq0ovGXnDs6wsIw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfxWyoELdX0iaxBpTXlibVQcSRHpqhWFFS4l5zw7aaIe3iaKbxWX8qFJmgvNQgKwOUkAvJNNhFxs9d6ibLf5dhEpiceb055Kyf3v6cyo/640?wx_fmt=png&from=appmsg)

05

开始安装

确认后点击"开始安装"，程序暂存文件、写入引导、提示重启。重启后自动进入内置 WinPE 完成格式化、镜像部署、引导修复，全程无需人工干预。

小白模式

新手推荐开启「小白模式」

#简化#三步

在关于页面勾选「小白模式」，把流程简化为：选系统 → 选版本 → 确认。

实测完整安装 Windows 11 大约 15–20 分钟（视电脑性能和镜像大小而定），比传统U盘方式省去大量中间步骤。

CHAPTER 03

**03****其他常用功能快速上手**TOOLBOX

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfwCI6Z91nfPbhRiaLzCPwO3fcSvLISxEs0qor0syZuMs1XE4jzggPr0yjLDgQ142OUuQzvs0qCuNTDTZmibNZZx3BwT9ct5jFEH0/640?wx_fmt=png&from=appmsg)

CHAPTER 04

**04****注意事项**CAUTION

警告

使用前务必注意

#非商业#高权限#确认目标

- 仅限个人非商业使用，禁止商业用途 - 高权限工具，操作磁盘分区前务必确认目标，避免误操作 - 旧系统（如XP）能否正常启动取决于硬件和驱动支持

- 建议在虚拟机或测试机上先熟悉流程 - 请务必使用完整解压包运行，不要只拷贝单个 exe

CHAPTER 05

**05****下载与反馈**DOWNLOAD

GET STARTED

准备好告别折腾半天的重装体验了吗？

立即去 GitHub 下载 LetRecovery

地址

LetRecovery 下载方式

#GitHub#官网

GitHub 项目地址：`https://github.com/NORMAL-EX/LetRecovery`

最新 Release：`https://github.com/NORMAL-EX/LetRecovery/releases`

官网：`https://letrecovery.net`

觉得好用的话，欢迎去`GitHub =`点个 **Star** 支持原作者和维护团队！有问题可在 Issues 反馈。

以后帮自己或家人重装系统，再也不用花半天时间折腾了。

真正把"重装系统"从复杂工程变成几步点击的事。赶紧试试吧！

你平时重装系统用什么方式？

U盘PE、一键重装、还是找别人帮忙？评论区聊聊，转发给经常被叫去修电脑的朋友吧～

· 点赞 ·

喜欢就点个赞吧

· 转发 ·

分享给更多朋友

· 推荐 ·

推荐给身边的人

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

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