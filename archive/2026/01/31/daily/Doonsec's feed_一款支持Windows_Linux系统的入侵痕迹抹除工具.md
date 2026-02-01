---
title: 一款支持Windows/Linux系统的入侵痕迹抹除工具
url: https://mp.weixin.qq.com/s/xFdxn9xxqwzwvNhQy_Mm_g
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:24:42.175124
---

# 一款支持Windows/Linux系统的入侵痕迹抹除工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2kibtdoibz6UfMJ9qDNGyQZ7bGknJmr8Pqx7hHbjW2nWUicyjI0icav6eL9XJvWVjoRslCczFGUDHtJsg/0?wx_fmt=jpeg)

# 一款支持Windows/Linux系统的入侵痕迹抹除工具

星夜AI安全
星夜AI安全

星夜AI安全

![]()

在小说阅读器中沉浸阅读

📌各位可以将公众号设为星标⭐

📌这样就不会错过每期的推荐内容啦~

📌这对我真的很重要！

![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg "image")

📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。

📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。

📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。

# Coda

> 请勿利用文章内的相关技术从事**非法渗透测试** ，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除** 。

## 简介

Coda 是一款适用于 Windows 和 Linux 系统的入侵痕迹清除工具，能够帮助使用者快速抹除系统内的攻击痕迹。该工具采用 Golang 语言开发。

## 编译方法 (需要具备 GO 环境)

首先，克隆项目源码：

```
git clone https://github.com/Symph0nia/Coda.git
```

安装 GO 环境（以 Windows 为例，可通过以下链接下载安装程序，安装时选择合适的路径，其余选项保持默认即可）：

https://dl.google.com/go/go1.25.6.windows-amd64.msi[1]

然后，进入项目目录并执行编译命令：

```
cd Coda
go build ./main.go  # 默认会生成 main.exe 可执行文件，使用时需要根据实际的文件名来调用
```

编译成功后即可使用该工具。

## 使用方法 (默认编译生成的文件为 main.exe)

Coda 接受以下三个参数：

```
./coda -D # 删除所有日志信息
./coda -B # 删除大型日志信息，并将小型日志备份到 /TEMP 或 /tmp 目录下
./coda -R # 将备份的日志信息恢复到原始位置
```

## 原理

Coda 的基本功能是直接删除所有日志文件，以此达到干扰溯源分析的目的。

Coda 的高级用法是“备份后恢复”（Backup 2 Restore）模式。

渗透测试成功后，首先运行 `Coda -B` 命令，对当前的日志信息进行镜像备份。随后可以进行敏感操作，例如数据窃取或删除。

在渗透测试结束阶段，运行 `Coda -R` 命令，将之前备份的日志信息恢复到系统中。这样并非完全清除日志，而是创造了一段优雅的、无监控记录的空白时间窗口。

## 注意事项

⚠️ 警告

Coda 对系统文件造成的修改是不可逆的，请谨慎使用。

当前的日志分类规则是：大于 100MB 的日志文件被视为大型日志。

当前工具会清除的日志文件列表如下：

### Windows 系统：

| 日志文件路径 | 作用 |
| --- | --- |
| `C:\\Windows\\System32\\winevt\\Logs\\Security.evtx` | 记录安全相关事件，例如登录尝试、权限使用等。 |
| `C:\\Windows\\System32\\winevt\\Logs\\Application.evtx` | 记录应用程序相关事件，由应用程序生成的日志信息。 |
| `C:\\Windows\\System32\\winevt\\Logs\\System.evtx` | 记录系统级别事件，包括驱动程序加载、系统组件的启动和停止等。 |
| `C:\\Program Files\\Apache Group\\Apache2\\logs\\access.log` | 记录 Apache 服务器的访问日志，包含每个请求的详细信息。 |
| `C:\\Program Files\\Apache Group\\Apache2\\logs\\error.log` | 记录 Apache 服务器的错误日志，包含启动、运行时错误和异常。 |
| 详情请查阅项目 README.md 文件........ | .......... |

### Linux 系统：

| 日志文件路径 | 作用 |
| --- | --- |
| `/var/log/syslog` | 记录系统日志，包含内核消息、服务启动和停止、各类系统事件。 |
| `/var/log/messages` | 记录一般系统消息和非关键的系统错误信息。 |
| `/var/log/auth.log` | 记录认证相关的日志，包含登录尝试、sudo 使用等。 |
| `/var/log/lastlog` | 记录上次登录的信息。 |
| `/var/log/wtmp` | 记录登录和注销事件的永久性日志。 |
| `/var/log/btmp` | 记录失败的登录尝试。 |
| `/var/log/faillog` | 记录失败的用户登录信息。 |
| 详情请查阅项目 README.md 文件................ | .......... |

## 📖 项目地址

关注微信公众号后台回复“**20260131** ”，即可获取项目下载地址

关注微信公众号后台回复**入群** 即可加入星夜AI安全交流群

## 圈子介绍

现任职于某头部网络安全企业攻防研究部，核心红队成员。2021-2023年间累计参与40+场国家级、行业级攻防实战演练，精通漏洞挖掘、红蓝对抗策略制定、恶意代码分析、内网横向渗透及应急响应等技术领域。在多次大型演练中，主导突破多个高防护目标网络，曾获“最佳攻击手”“突出贡献个人”等荣誉。

已产出的安全工具及成果包括：

* 多款主流杀软通杀工具（兼容卡巴斯基、诺顿、瑞星、360等终端防护，无感知运行，突破多引擎联合检测）
* XXByPassBehinder v1.1 冰蝎免杀生成器（定制化冰蝎免杀工具，绕过主流终端防护与EDR动态检测，支持自定义载荷）
* 哥斯拉二开免杀定制版（二开优化，深度免杀，突破终端防护与EDR检测，适配多场景植入）
* NeoCS4.9终极版（高级免杀加载工具，强化载荷注入与进程劫持，适配多系统版本，无兼容问题）
* WinDump\_免杀版（浏览器凭证窃取工具，支持Chrome/Edge/Firefox等主流浏览器，一键提取敏感数据，免杀过防护）\_
* \_DumpBrowser\_V1\_免杀版（浏览器凭证窃取工具，专攻浏览器密码、Cookie、历史记录提取，免杀性能拉满）
* fscan二开版（二开优化内网扫描工具，增强指纹精度、弱口令爆破与结果标准化输出，适配复杂内网）
* RingQ加载器二开版（二开优化免杀加载器，支持Shellcode内存执行，绕过各类终端防护与EDR检测）
* 多款免杀Webshell集合（覆盖PHP/JSP/ASPX，过主流WAF与终端防护，适配不同Web场景）
* 免杀360专属加载器（支持Shellcode内存执行，针对性绕过360全系防护检测，无感知运行）

后续将不断更新到内部圈子中 欢迎加入圈子 ![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kTp5BpCMb901r34Qsxiar69niau36nIE6q7fMIIrylRMNSb6PiaetIQDU7cCBCDnFibeQTPWeArDO9tA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5 "image")![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kTp5BpCMb901r34Qsxiar69aBRExZP9U4yAnhfoP9wABkmc0DCYs7NTyicvYcBaqLxVxfAJoicMyWGQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6 "image")

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

星夜AI安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

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