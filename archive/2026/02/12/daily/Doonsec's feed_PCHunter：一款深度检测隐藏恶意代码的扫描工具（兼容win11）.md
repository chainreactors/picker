---
title: PCHunter：一款深度检测隐藏恶意代码的扫描工具（兼容win11）
url: https://mp.weixin.qq.com/s/NqtVvek9BD6NLXMIUcK-cw
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:15:25.611076
---

# PCHunter：一款深度检测隐藏恶意代码的扫描工具（兼容win11）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicJ33fLbW3Qeffqkeu0gjoneVwjibTic6QQXH5arAhmq3pPSGTREuu30oGMTcHCpZXDLCccEVPr4puRCQQiaPpjrY5gr89rfwHSicEE/0?wx_fmt=jpeg)

# PCHunter：一款深度检测隐藏恶意代码的扫描工具（兼容win11）

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[【已复现】最新版微信v4.1出现远程命令执行漏洞：one-click RCE on Linux WeChat](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486318&idx=1&sn=a39e4ceaadd2fcffea08ecdc48319fc9&scene=21#wechat_redirect)

·[xss\_scanner\_mix：一款自动化深度XSS漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486302&idx=1&sn=08544ff7835ce01fae582f677ad02a98&scene=21#wechat_redirect)

·[StegoScan：CTF自动化隐写识别和解密工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486301&idx=1&sn=704da2217fce796fe07611b66c3448d4&scene=21#wechat_redirect)

·[Metasploit Pro：可视化的metasploit渗透测试工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486276&idx=1&sn=44e00b0ee13437083417bd8c16f15f0c&scene=21#wechat_redirect)

·[Coda：实现Windows/Linux入侵痕迹抹除](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486251&idx=1&sn=c2c9dc8f482b43d9c5c0384d37eeb8a6&scene=21#wechat_redirect)

·[OSV-Scanner：一款专门于发现开源软件漏洞的扫描器](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486240&idx=1&sn=69241fc574c182a305e1c17747377ae6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKtxDxF1qZT7avszsjWKia7cjsOjDKHsLdoZHphAMwvasUxHAHpxwf2CUd3j0ct2bzuZRNJWLUxzz7LFhJu1aTaotIGyBoqXMMQ/640?wx_fmt=png&from=appmsg)

      PCHunter 是一款面向 Windows 平台的深度系统分析与恶意代码检测工具，通过内核态驱动注入与 Ring0 权限交互，实现对系统进程、线程、模块、驱动、注册表、文件系统及网络连接的全维度监控与篡改溯源，其核心能力依托 SSDT/SSDT Shadow 钩子检测、内核对象枚举、隐藏进程 / 线程扫描、Rootkit 特征匹配等底层技术，可精准识别并定位各类恶意软件、后门程序及内核级威胁，同时支持进程内存 dump、驱动强制卸载、关键注册表项修复等应急响应操作，是渗透测试、恶意代码分析及系统安全加固场景下的核心辅助工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

使用

1. 进程管理

核心能力：枚举并展示系统中所有进程（包括通过修改 EPROCESS 链表等方式隐藏的恶意进程），提供进程 PID、PPID、内存占用、模块加载、线程列表等详细信息。

关键操作：支持终止进程、强制卸载可疑 DLL、Dump 进程内存镜像、查看进程句柄表等，用于定位并处置恶意程序。

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIksuqcicg8eibz801VDxwJdIKNX1jCicwzQ63e2lacicvXmZIEp58U9pf0dliaPYrVuCdD6p37VPI2RndS6LWWFqJohsmz1CSH1A2Q/640?wx_fmt=png&from=appmsg)

2. 驱动模块

核心能力：枚举所有已加载的内核驱动，展示驱动名、基地址、大小、驱动对象、驱动路径、服务名及文件厂商等信息。

关键操作：可识别未签名或来源不明的可疑驱动，支持强制卸载驱动、恢复被篡改的内核钩子，是检测 Rootkit 的核心模块。

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKFJKeQaDLQzyFQt3mUIPgRfOD5yHiadJO75K2WhNxjyypUvNxFamic1oZ7h1KVZVEbYxACJlKtCRxaLCpiauYyyLWAZen9cfTJro/640?wx_fmt=png&from=appmsg)

3. 内核钩子检测

核心能力：扫描并对比 SSDT（系统服务描述表）、SSDT Shadow 及内核对象钩子的当前地址与原始地址，标记被恶意代码篡改的系统调用。

关键操作：提供 “恢复钩子” 功能，可一键还原被篡改的内核函数，阻断 Rootkit 对系统的控制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIyke4fsn48PbT08iay6TadjtponlUoFDKNqZdXTlEP5fLwlptZpEzR83aSmmwZp2kcqCl6ib0rAZgrIStEaJIttFwicblUSx3qVg/640?wx_fmt=png&from=appmsg)

4. 应用层钩子

核心能力：检测用户态应用程序中的 IAT/EAT 钩子、Inline Hook 等，定位恶意代码对应用程序的注入与篡改。

关键操作：可查看钩子详情、定位注入模块，用于分析恶意软件的行为模式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIiayO8Yt8LiavNbHGVoZSa2SGtHfqDXx1eCG6WQOylpUAzZYn7seDqE3PEzUmJ6asyjcicOZCZBicsoZp3UUQGnJrKE1l7qrg3toI/640?wx_fmt=png&from=appmsg)

5. 网络连接

核心能力：枚举所有 TCP/UDP 连接及监听端口，关联对应进程，展示本地 / 远程地址、端口及连接状态。

关键操作：支持终止可疑网络连接，阻断恶意程序的 C2 通信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJhEf1iaprNiaw7fjhcAGCM3QAqsmrekdNtGQIuwDtrNcibRDB1N6GEbhBCYaPUyrJoUFMbF037yHqSS8j3F1ENxEHUU1sK4Sqbsc/640?wx_fmt=png&from=appmsg)

6. 注册表管理

核心能力：深度遍历并监控注册表关键项（如自启动项、服务配置、内核配置），标记被篡改的键值。

关键操作：支持删除恶意自启动项、修复被篡改的系统配置，用于清除恶意程序的持久化机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIfEf7bLvkT7MPR5HHfTmCy8RW8glkQpIIQfaqw0UaUl345tbI7ItATTLAYjKqjLib6iasCiaxoxia2xFmxtLoWnxewU7fbV0hVJ9M/640?wx_fmt=png&from=appmsg)

7. 文件系统

核心能力：枚举并监控文件系统，支持查看文件属性、权限、哈希值，定位被隐藏或篡改的恶意文件。

关键操作：提供强制删除、粉碎文件等功能，用于清除顽固恶意程序。

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLjkzO1ZeO6B29ibS7jQnswtrmRUI28vkiaTmag17PGhAd8C8aoqygvEZtdnQ3OKXpJI6Wnetm3lFUkzc8YicYngZ61ThRtzeMNwY/640?wx_fmt=png&from=appmsg)

8. 启动信息

核心能力：扫描系统启动项、服务、计划任务等，定位恶意程序的持久化入口。

关键操作：禁用或删除可疑启动项，防止恶意程序随系统自启。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKYicyRaMQF73YxZzyicTXia1iaflicpmN9QPg3dndcPyBPAic3m00kBibdYSZ4FZSmafUhGSd5jbDNwmgOyUVquN8icSUpgNvmbrrV1Gw/640?wx_fmt=png&from=appmsg)

9. 系统杂项

核心能力：提供系统信息、硬件信息、环境变量、服务列表等辅助信息，辅助全面评估系统安全状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKs6zdHayprTF16cIQuwibOVpUiaGEHswpmNIuVZFAa4xst2ZppqU1nNKYCVOStQEb7ibXtiazCNT6ltzkskvxzdvZ1WN6IypTkZEM/640?wx_fmt=png&from=appmsg)

10. 电脑体检

核心能力：一键扫描系统中存在的安全风险，如可疑进程、未签名驱动、恶意启动项等，并生成体检报告。

关键操作：根据报告提供处置建议，用于快速完成系统安全基线检查。

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJMGqgswBPHeiaM71s7K0ZgVhtovN2QnDWEicMibWVuBib24gU0YBpwl6FYXySDCiaEPtPkE5KqZhkBhOtSDnu9RNDY1XUPTpxY6pvc/640?wx_fmt=png&from=appmsg)

注意：PCHunter 的内核级操作存在导致系统崩溃的风险，建议在隔离的测试环境中使用，操作前需充分评估影响，并确保仅在授权范围内开展安全测试与应急响应。

通过网盘分享的文件：PCHunter\_V1.6.7z

链接:

https://pan.baidu.com/s/15N2BXHpMJd6QAFnRpnFFsw?pwd=7uni

提取码: 7uni

--来自百度网盘超级会员v3的分享

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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