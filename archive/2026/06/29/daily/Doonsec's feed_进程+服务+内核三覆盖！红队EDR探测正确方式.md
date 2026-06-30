---
title: 进程+服务+内核三覆盖！红队EDR探测正确方式
url: https://mp.weixin.qq.com/s/CF9it00uyo2c98dvoCd_XA
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:07:32.851508
---

# 进程+服务+内核三覆盖！红队EDR探测正确方式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lFfjZayicKlEzaN8WpibUCCoWm3fj88f5icGdjFP8Th2EjuUy2nEz4VZicXqzNFj8eewSEmDkRdmjPBZM5fQKcOia5eGakhvtjBqicjhOibmuUcfDE/0?wx_fmt=jpeg)

# 进程+服务+内核三覆盖！红队EDR探测正确方式

蚁景网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于潇湘信安
，作者3had0w

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6fpNgxJic72iaxuNHwNA0BooiblUaaQuiavCyr7GWWPulUHw/0)

**潇湘信安**
.

一个不会编程、挖SRC、代码审计的安全爱好者，主要分享一些安全经验、渗透思路、奇淫技巧与知识总结。

|
|  |

前言

做红队后渗透的朋友，大概率都踩过这个坑：

刚拿到一台主机的 Beacon，第一件事就是想确认上面有没有 EDR、装了什么杀软。结果随手甩了条 PowerShell 命令，下一秒会话就黑了 —— 等于主动跑到 EDR 脸上跳脸输出。

讽刺的是，我们用来检测 “系统有没有被监控” 的手段，恰恰是监控最严的行为。

最近在 GitHub 上挖到一个 Cobalt Strike 的 Aggressor 脚本，刚好把这个问题解决得很漂亮：它把 EDR 枚举做成了**分级噪音模式**，从完全零痕迹的进程内执行，到全量 WMI 枚举，一共 6 个档位。你当前环境能接受多大风险，就用对应的方式，不用上来就搞出大动静。

**覆盖全品类，三层特征匹配**

这款工具的特征库覆盖了进程、服务、内核驱动三个维度，主流终端安全产品基本都能识别到。从 CrowdStrike、SentinelOne、Defender for Endpoint 这类一线 EDR，到卡巴斯基、ESET、Malwarebytes 这类常规杀毒，再到 Sysmon、Splunk UF、Wazuh 这类遥测 / SIEM 探针，甚至 Zscaler、CyberArk 这类 ZTNA / 权限类组件，都在特征库里。

识别完成后会自动给当前环境评定威胁等级：

* HIGH：检测到活跃 EDR，具备内核回调、用户态 Hook、云分析、防篡改能力
* MODERATE：杀毒软件 + 遥测探针，日志会转发到 SOC
* LOW：仅基础杀毒，只有文件扫描和 AMSI 防护
* UNKNOWN：未检测到特征，也可能是无代理、纯内核级方案

输出也按产品类型做了颜色标注，扫一眼就能摸清当前终端的防护配置。

**6 档噪音，风险自己掌控**

这是整个项目最精髓的设计：它不用容易搞反的 “OPSEC 等级”，直接用星级标注噪音 ——★越少越安静，★越多动静越大，一眼就能看懂。

★ 最低噪：纯进程内执行，零痕迹

两档一星命令是这套工具的核心。edr\_check直接调用 Beacon 原生的进程列表接口，edr\_services\_bof通过内联 BOF 枚举服务和驱动。

全程没有子进程创建，没有 CLR 加载，不触发 AMSI，连 ETW 日志都不会产生，真正的 “扫完和没扫过一样”。

其中 BOF 还支持三种模式切换：默认同时查服务 + 驱动；加svc只查服务，快速定位厂商；加drv只查内核驱动，比如干掉 EDR 服务后，可以用它验证内核回调是不是还在。

![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNIDEyFp68sWBicagdB694SiaMP3AC9icW3vQ6SySckQwg8D0PkTG9suRUqrkibXOXlXEOMD0Plq5RAZxo8bwDwAvuCkqoMhYgw5uLs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNIMjb1NQkmNYFrgISMSk3iawFEKankmTZ6AlDhticDM8xpe18RknylzkaPtC0RFDMrY1uzwDNCaKE8ictbCknKQ8n4kX5tibfaWScE/640?wx_fmt=png&from=appmsg)

★★ 低噪：非托管PowerShell

edr\_services\_pick通过 bpowerpick 执行，不会弹出 powershell.exe 子进程，但会在 Beacon 进程内加载 CLR，会触发.NET 运行时的 ETW 和 AMSI 初始化。适合对 CLR 加载不敏感的环境。

![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNJzvUjFzMDDpLWwicobzHNn9EfogR5v2dGPSHwq3Mxv3bRU5BrZy0E6wKicib5eIQ0oyYNZsCz1rnNvkic1nMkChmHCDgzgibbhg0sQ/640?wx_fmt=png&from=appmsg)

★★★ 中噪：cmd.exe调用sc查询

edr\_services\_cmd通过 bshell 执行sc query，会创建 cmd.exe 子进程，触发进程创建日志（Sysmon EID 1 / Windows 4688）。但没有 CLR、没有 PowerShell 相关日志，适合 cmd 执行不敏感的环境。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNIJraFwia9cN4icoqVY4zmxadmnzkQzFc1hpic2zHWzaI8rgicZL8Z5OcgKp1edMmw0qtYMXNoQibg52efjt7wJZreqF0PRsk29UyCY/640?wx_fmt=png&from=appmsg)

★★★★ 高噪：完整PowerShell/WMI枚举

edr\_services和edr\_enum都会创建 powershell.exe 子进程，脚本块日志、模块日志、AMSI、全量 ETW 都会触发。优点是信息最全面，edr\_enum还会通过 WMI 读取 AV 产品信息，适合已经暴露、不需要藏行踪的场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNJPyu97JeHq4aicCVYSvIUr1Aoa9MOCTLgIor7x30KBFeaEkBiaDgrRLWvibGgcX3e2CtaHIV40AhQZ05M5allQOrPJSBoPfDK77E/640?wx_fmt=png&from=appmsg)

**实战推荐工作流**

作者也给出了标准的使用顺序，从低到高逐步升级，避免一上来就打草惊蛇：

1. 先跑`edr_check`，零成本，先从进程层面筛一遍明显的 EDR
2. 再上`edr_services_bof`，补全服务和内核驱动信息，同样零噪音
3. 能接受 CLR 加载的话，再用`edr_services_pick`补充信息
4. 环境宽松的话，再考虑 cmd 和 PowerShell 版本
5. 必须要全量信息时，最后再上`edr_enum`

`![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNJnl5FfGwOxibRhDO9IgbB8PFYqphod60CLJZsPyWrs8AwPV47fM1ynqNscyJ6VsBa16jRsuvKuBeNtxUzVicvGvx0ANIR56XZAE/640?wx_fmt=png&from=appmsg)`

最优组合就是`edr_check` + `edr_services_bof`：进程、服务、内核驱动三层全覆盖，全程噪音等级★，没有任何额外痕迹，性价比拉满。

**BOF 为什么这么安静？**

很多人关心 BOF 为什么能做到零痕迹，原理其实很清晰：

它直接调用 Windows 服务控制管理器（SCM）的原生 API，分两阶段枚举：第一阶段扫用户态服务，第二阶段扫内核驱动（包括文件系统微过滤驱动），全程共用一个句柄。

所有 API 调用都用了动态函数解析，没有静态导入表，不会留下 IAT 痕迹；全程在 Beacon 进程内执行，不创建子进程，自然也就不会触发进程创建、PowerShell 日志、AMSI 这类常见检测点。

**安装与使用**

安装分两步，非常简单：

1. 基础功能直接用：把`edr-enum.cna`导入 Cobalt Strike 的脚本管理器，除 BOF 外的所有命令就能直接用，不需要编译。
2. 编译 BOF（强烈推荐）：装个 mingw-w64，用项目里的 Makefile 执行 make 编译，把生成的`.o`文件和 cna 脚本放同目录就行。

在 Beacon 里输入`edr_help`还能调出完整的速查表，纯客户端执行，不会往目标机发任何流量。

**最后**

这款工具最难得的地方，是它没有追求 “一键全查” 的爽感，而是把检测权衡交给了操作者。

在红队作业里，很多时候不是查得越全越好，而是在不被发现的前提下，拿到足够决策的信息就够了。从静默探测到全量枚举，每一步的检测面都清清楚楚，操作者可以根据目标环境灵活选择 —— 这才是后渗透工具该有的样子。

项目地址：

https://github.com/VirtualAlllocEx/CS-EDR-Enumeration

之前《[自写的几个BOF，可过内存防护！](https://mp.weixin.qq.com/s?__biz=MzkyNTY3Nzc3Mg==&mid=2247491533&idx=1&sn=83b8f454e372d594cc7ac5d7e500003f&scene=21#wechat_redirect)》这篇文章中我写的是checkav\_bof主要是使用自己整理的进程数据通过进程方式进行识别，这里也可以把我们常见AV/EDR等安全防护产品的进程整理到他这个CNA脚本中用于识别，还是看个人使用习惯吧。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

学习网安实战技术，戳“阅读原文”

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

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