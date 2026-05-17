---
title: 黑客利用 OrBit Rootkit 从 Linux 系统中窃取 SSH 和 sudo 凭据
url: https://mp.weixin.qq.com/s/GdhhQwftXQQh9YjWWDX1cQ
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:47:06.918818
---

# 黑客利用 OrBit Rootkit 从 Linux 系统中窃取 SSH 和 sudo 凭据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PaFY6wibdwyIN6rC4ibUCclonBK1icuqJvk1xMVFjtBhFTZrWg0SiaU7G3eqmdRicFIOGjdH2RKNUkcxrfCcich4U2vbRp4Q0nNpVGErPiaRXFbXJU/0?wx_fmt=jpeg)

# 黑客利用 OrBit Rootkit 从 Linux 系统中窃取 SSH 和 sudo 凭据

会杀毒的单反狗
会杀毒的单反狗

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**导****读**

一个名为 OrBit 的rootkit多年来一直默默针对 Linux 系统，窃取登录凭据并在受感染的设备中深度隐藏，而不会触发大多数安全工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PaFY6wibdwyKdWoCnvo1unvMFOBKbqqD9Ab1eEbaeNibNm8micyYOzAsbL23wwcQc7PM4JBur80hzbWD0qcyvkPxAy59KVzeoDUYTejT0Wg3sU/640?wx_fmt=jpeg&from=appmsg)

最新研究表明，曾经被认为是定制的威胁实际上是公开可用的 rootkit 的修改版本，并通过多个黑客组织在全球范围内传播。

OrBit 的工作原理是将自身嵌入到 Linux 系统的核心中，接入四十多个基本系统功能，从而使其几乎完全不可见。

一旦进入机器内部，它就会监听通过 SSH 和 sudo 进行的登录尝试，捕获用户名和密码，并将它们保存在一个标准系统扫描无法检测到的隐藏目录中。

攻击者随后通过秘密的 SSH 后门重新连接到被入侵的系统，而无需通过互联网发送命令。

Intezer 的研究人员在一份报告中表示，他们发现 OrBit 根本不是原创代码。它实际上是基于一个名为 Medusa 的公开 rootkit 构建的，该 rootkit 于 2022 年 12 月发布在 GitHub 上。

黑客的操作工作不是编写新代码，而是配置现有源文件、轮换密码和更改安装路径以保持隐蔽。

### OrBit Rootkit

Intezer 的分析追踪了 2022 年至 2026 年初的十几个样本。

该团队对每个样本进行了静态和差异分析，发现了两条不同的构建路径：一条是功能齐全的版本，称为 Lineage A，它包含了完整的攻击工具包；另一条是精简版，称为 Lineage B，它舍弃了一些功能，以减少资源占用。

Lineage B 似乎在 2024 年后就停止出现，这表明运营商可能已经重新整合到主版本中。

OrBit 以共享库文件的形式部署在目标 Linux 机器上。它通过修改动态链接器配置来实现持久化，使恶意库自动加载到系统上运行的每个进程中。

从这个位置，它可以拦截文件读取、目录列表和网络连接数据，使自己对管理员和安全工具都不可见。

该恶意软件将捕获的凭据和配置数据存储在名为 /lib/libseconf/ 的隐藏目录中，由于 rootkit 自身的钩子，标准工具无法看到该目录。

最显著的功能提升出现在 2025 年，当时最新版本添加了一个名为 pam\_sm\_authenticate 的钩子，这是一个服务器端身份验证功能。

早期版本只能被动地收集用户输入的凭据，而这个新版本还可以伪造身份验证结果，这意味着攻击者可以随意批准或拒绝在被入侵的系统上的登录尝试。

同年，出现了一种新的两阶段交付链：感染器嵌入投放器，然后投放器提取并安装 rootkit，同时创建一个 cron 作业从外部域获取更新的有效载荷。

### 多个黑客组织正在利用这个后门

至少有三个不同的黑客组织一直在使用 OrBit。

Mandiant 追踪到的网络间谍组织 UNC3886使用了相同的代码库，但具有特定的 0xAA 加密密钥、不同的凭据和与 Intezer 的 2024 Lineage A 样本完全匹配的安装路径。

CrowdStrike 在其 2026 年全球威胁报告中指出，以 Embargo 勒索软件而闻名的网络犯罪组织 BLOCKADE SPIDER 使用 OrBit 悄悄维持对 VMware 虚拟化环境的访问权限。

2025 年观察到的第三次攻击活动使用了与 RHOMBUS（一个于 2020 年首次报道的基于 Linux 的僵尸网络）相关的投放器架构相同的投放器架构，这两个投放器共享同一个 C2 域，解析到俄罗斯的基础设施。

建议防御者监控意外目录中出现的 sshpass.txt、.logpam 和 .ports 等文件名，因为无论哪个操作员编译了 rootkit，这些都是 Medusa 构建管道的固定产物。

YARA 规则使用可变键解码 XOR 字符串表，并匹配已知的明文条目，可以捕获此系列的任何版本，即使是使用新凭据和重命名安装路径的构建版本。

技术报告：

《OrBit重现：追踪一个开源 Linux rootkit 四年来的分支和部署历程》

https://intezer.com/blog/orbit-returns/

新闻链接：

https://cybersecuritynews.com/hackers-use-orbit-rootkit-to-harvest-ssh/

**![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg)**

扫码关注

军哥网络安全读报

**讲述普通人能听懂的安全故事**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

爱拍照的老李

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

![作者头像](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

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