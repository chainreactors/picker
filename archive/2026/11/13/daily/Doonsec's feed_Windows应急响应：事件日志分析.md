---
title: Windows应急响应：事件日志分析
url: https://mp.weixin.qq.com/s/JlCgg70XanoWfZAxZXVcoQ
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:15:43.508088
---

# Windows应急响应：事件日志分析

# Windows应急响应：事件日志分析

原创

xersec
xersec

小二安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

如果入侵排查是检查主机当前状态，那么日志分析就是还原主机历史行为，比如攻击者是怎么进来的、执行了什么、什么时候建立持久化、有没有横向移动、是否删除日志等。

## 策略配置

默认配置下，Windows只会记录部分日志，并不全面，且日志存储大小上限20M，超过上限会覆盖旧日志，部分事件需要提前启用相应的审核策略才会产生。

### 审核策略

Win+R打开运行对话框，输入`gpedit.msc`打开本地组策略编辑器，按顺序依次打开“本地计算机策略”->"计算机配置"->“Windows设置”->“安全设置”->“本地策略”->“审核策略”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Uxm6fgkqwg832vG1Cib2clya7cHOT4ricqPuKRQwZBMBibg64H8vrNCXicH1fPmbCwngDFy6NJzfYbq9zOfFARl17xica0C7JpRto2vqquh31NpU/640?wx_fmt=png&from=appmsg)

每项策略都开启审核（包括成功和失败）。

### 日志存储

Win+R打开运行对话框，输入`eventvwr.msc`打开事件查看器，选择Windows日志，以安全日志为例，在属性中配置，可以增加日志最大大小，覆盖事件保持默认。

![](https://mmbiz.qpic.cn/mmbiz_png/Uxm6fgkqwgibu53LTRicNd0icE1Q5x4w8ScQdZzUKuE3UvfWa8icwib3rLgUQEqgibEWXWvmDRWT7cCe7xc1yzwhmpw33QXpN99wRE7Fq08AicwWWI/640?wx_fmt=png&from=appmsg)

### PowerShell日志

排查的时候，PowerShell日志也很重要，Windows默认是关闭的，需要手动启动。

Win+R打开运行对话框，输入`gpedit.msc`打开本地组策略编辑器，按顺序依次打开“本地计算机策略”->"计算机配置"->“管理模板”->“Windows组件”->“Windows PowerShell”

![](https://mmbiz.qpic.cn/mmbiz_png/Uxm6fgkqwgicUicm2p2Q4Rv2cunqT4FLbhTFdwgZ4qqLOROjO4TmusdjduaNR6fN43LaciaL0ibyBurYsicZ3gBtfDNLrtNhk3qYTyZ6bwMlsRBw/640?wx_fmt=png&from=appmsg)

启用“打开PowerShell脚本块日志记录”就够用了，根据需求启动“启用模块日志记录”。

## 日志类型

Windows事件日志种类非常多，并不用每一项都分析，在事件查看器中，事件日志分两类，Windows日志和应用程序和服务日志。

### Windows日志

Windows日志分五类：

| 日志类型 | 主要记录内容 |
| --- | --- |
| 应用程序日志 | 用户登录、登录失败、账户创建、权限变更、审核策略等 |
| 安全日志 | 系统启动、关机、服务启动、驱动加载、系统异常等 |
| Setup日志 | 应用程序运行错误、崩溃、异常事件等 |
| 系统日志 | 系统组件、更新和安装相关事件 |
| Forwarded Events日志 | 从其他计算机转发过来的事件日志 |

### 应用程序和服务日志

应用程序和服务日志包含Windows各个组件、功能模块产生的专用日志。

可以重点关注以下几类：

| 日志名称 | 主要用途 |
| --- | --- |
| PowerShell | PowerShell执行记录 |
| TaskScheduler | 计划任务执行记录 |
| TerminalServices | 远程桌面连接记录 |
| WMI-Activity | WMI操作记录 |
| 等等 | 等等 |

## 事件ID

对于应急响应来说，Windows日志中，可以重点关注安全日志和系统日志。

### 安全日志

| 事件ID | 含义 | 排查目的 |
| --- | --- | --- |
| 4624 | 登录成功 | 排查异常登录、远程登录 |
| 4625 | 登录失败 | 排查暴力破解、密码猜测 |
| 4648 | 使用显式凭据登录 | 排查异常凭据使用 |
| 4672 | 分配特殊权限 | 排查高权限账户登录 |
| 4688 | 创建新进程 | 排查可疑命令和程序执行 |
| 4720 | 创建用户账户 | 排查后门账户 |
| 4722 | 启用用户账户 | 排查异常账户启用 |
| 4724 | 尝试重置账户密码 | 排查异常密码重置 |
| 4726 | 删除用户账户 | 排查异常账户删除 |
| 4732 | 用户加入本地安全组 | 排查账户权限提升 |
| 4697 | 安装新服务 | 排查服务持久化 |
| 4698 | 创建计划任务 | 排查计划任务持久化 |
| 4702 | 更新计划任务 | 排查计划任务被篡改 |
| 4719 | 审核策略发生变更 | 排查安全审计配置被修改 |
| 1102 | 安全审核日志被清除 | 排查日志清理行为 |
| 等等 | 等等 | 等等 |

### 系统日志

| 事件ID | 含义 | 排查目的 |
| --- | --- | --- |
| 7045 | 安装新服务 | 排查恶意服务、服务持久化 |
| 7036 | 服务状态发生变化 | 排查异常服务启动、停止 |
| 7040 | 服务启动类型发生变化 | 排查服务启动方式被修改 |
| 1074 | 系统关机或重启 | 排查异常关机、重启行为 |
| 6005 | 事件日志服务启动 | 辅助判断系统启动时间 |
| 6006 | 事件日志服务停止 | 辅助判断正常关机时间 |
| 6008 | 上次关机异常 | 排查异常关机、意外重启 |
| 41 | 系统未正常关闭便重新启动 | 排查异常重启、系统崩溃 |
| 1001 | 系统错误报告 | 排查蓝屏、系统崩溃原因 |

### PowerShell

攻击者经常利用PowerShell执行命令、下载文件、执行脚本，甚至进行内存加载。如果系统开启了相应日志记录，可以通过PowerShell日志分析执行过哪些命令。

| 事件ID | 含义 |
| --- | --- |
| 4103 | PowerShell模块内容，可以看到调用了哪个模块的命令 |
| 4104 | PowerShell脚本块内容，可以看到实际执行的脚本 |

### TaskScheduler

入侵排查时，通过当前计划任务列表，只能看到目前存在的任务，无法完整还原历史任务变化。而TaskScheduler日志可以辅助分析任务的注册、更新、启动和执行情况。例如，攻击者创建计划任务实现开机启动，即使后来删除了任务，也可以尝试从历史日志中寻找相关记录。

### TerminalServices

日志位置：

```
应用程序和服务日志
  Microsoft
    Windows
      TerminalServices-LocalSessionManager
      TerminalServices-RemoteConnectionManager
```

| 事件ID | 含义 |
| --- | --- |
| 21 | 远程桌面用户身份验证成功 |
| 22 | 远程桌面会话登录成功 |
| 24 | 远程桌面Shell启动通知 |
| 25 | 远程桌面会话断开 |
| 1149 | 远程桌面会话重新连接 |

通过这些记录，可以辅助判断是否存在异常远程桌面访问，以及连接和断开时间。

## 日志筛选

正常情况下，日志会非常多，挨个分析不现实，排查起来也麻烦，这就会用到日志筛选功能来提高效率，日志筛选可以筛选时间范围、时间级别、事件ID等。

以安全日志为例，筛选指定时间内，用户登录成功和失败的日志。

![](https://mmbiz.qpic.cn/mmbiz_png/Uxm6fgkqwgibp9Ejbic86iaNIrFFqqeDiaRrFqgo0RiaAN07lmjA1LN2MxqePaynlh302icicS8vlAlF7o0H3D9UIkiapib8kZOaTbWNcBHWngDHMxYA/640?wx_fmt=png&from=appmsg)

还可以将筛选后的日志进行保存，在右侧操作列中的“将已筛选日志文件另存为”功能。保存后，还可以打开保存的日志，再次进行筛选。

比如筛选当前保存日志中，用户登录成功的日志。

![](https://mmbiz.qpic.cn/mmbiz_png/Uxm6fgkqwgiccBFB6aR2UT1ViabY5ianRiaLpIdf9YtmxwiavePUTF8ZKKPEfzoezlgG56oXmen2IJeODEYwbWruVAvfkQV0shWGng0mcxyzjOwI/640?wx_fmt=png&from=appmsg)

---

写到这里就结束了，感谢阅读。小二安全主要分享渗透测试、代码审计、红蓝对抗等内容，感兴趣欢迎关注。我们下篇见。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Uxm6fgkqwgibBFZlINmXkLEuAom5fg3G7p53zKbgbRgcgnAI3VFbDdsJ3tNNicTjz1WdedIZGL6twu4ncibx46J9E0tAegbg0wq65I9ysfExk8/0?wx_fmt=png)

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