---
title: 「推安早报」0730 | outlook C2、ESXi漏洞、红蓝工具
url: https://mp.weixin.qq.com/s?__biz=MzU0MDcyMTMxOQ==&mid=2247487691&idx=1&sn=383f62eea8e5e77b27c6b320d9af61c1&chksm=fb35b903cc423015b83726b63dc28c72861c94a6e47c925f76a5c55e5f26c1c11c1ef39b8f0f&scene=58&subscene=0#rd
source: 甲方安全建设
date: 2024-07-31
fetch_date: 2025-10-06T17:44:50.086294
---

# 「推安早报」0730 | outlook C2、ESXi漏洞、红蓝工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZnmMbSSOXzLLv374fC8mUZN4WHMCibtTWxZhCdcMv6X51zODCdZCicFVsa5WAB1AkG9SHmN8GfDESBA/0?wx_fmt=jpeg)

# 「推安早报」0730 | outlook C2、ESXi漏洞、红蓝工具

bggsec

甲方安全建设

# 2024-07-30 「红蓝热点」每天快人一步

> 1. 推送`「新、热、赞」`，帮部分人`阅读提效`
> 2. 学有`精读浅读深读`，艺有`会熟精绝化`，觉知此事`重躬行`。推送只在`浅读预览`
> 3. 机读为主，人工辅助，每日数万网站，10w推特速读
> 4. 推送可能`大众或小众`，不代表本人偏好或认可
> 5. 因渲染和外链原因，公众号`甲方安全建设`发送`日报`或日期,如`20240730`获取`图文评论版pdf`

### 目录

> 0x01 【2024-0729】C#自删除二进制代码实现
> 0x02 【2024-0729】Cnext项目中的CosmicSting漏洞利用分析
> 0x03 【2024-0730】勒索软件操作者利用ESXi虚拟机管理程序漏洞进行大规模加密
> 0x04 【2024-0730】规则探索者项目REx介绍
> 0x05 【2024-0730】利用注册表将Outlook变为C2代理
> 0x06 【2024-0730】Specula框架：在Outlook环境下利用VBScript进行恶意软件操作

### 0x01 C#自删除二进制代码实现

> 网页提供了一个C#语言编写的自删除二进制文件的示例代码，这对于恶意软件的开发特别有用，因为在正常情况下，Windows系统不允许运行中的二进制文件被删除。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnmMbSSOXzLLv374fC8mUZNB98RmO4V76oLAeLvncL14oDyBKY7Ol2PZDfXrZkNib70oicr5VHOCSUg/640?from=appmsg)

### 热评

### 关键信息点

* 自删除机制：网页提供的C#代码能够让运行中的程序自我删除，这在Windows系统中通常是不可能的。
* 恶意软件应用：这种技术对于恶意软件来说具有特殊的用途，因为它可以帮助恶意软件在执行完毕后自我清理，减少被检测到的可能性。
* 技术实现：代码通过调用Windows API，如`GetModuleFileName`、`CreateFileW`和`SetFileInformationByHandle`，实现了对二进制文件的默认数据流重命名和删除操作。
* 项目需求：作者在开发SharpCovertTube项目时，出于项目需求，将原本用C语言编写的Maldev Academy课程代码进行了端口，以适应C#环境。

🏷️: C#, 自删除, 恶意软件, Windows

### 0x02 Cnext项目中的CosmicSting漏洞利用分析

> 网页提供了一个名为 `cosmicsting-cnext-exploit.py` 的 GitHub 仓库中的 Python 文件，该文件是由 `ambionics/cnext-exploits` 项目的最新提交中的一个部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnmMbSSOXzLLv374fC8mUZNEMqjTQRmL7TP4SUQyCJM6DVoz92eAIJfGqH8iafAQM0KvciakrAA2TlQ/640?from=appmsg)

### 热评

* Magento 漏洞利用公开：CosmicSting 和 CNEXT 导致远程代码执行
* Magento 漏洞利用工具发布：CosmicSting 和 CNEXT

### 关键信息点

* 该 Python 脚本是针对 CosmicString CNEXT 的一个漏洞利用工具。
* 脚本的最新提交包含了 557 行有效的 Python 代码，用于实现漏洞利用的功能。
* 文件大小为 23.2 KB，这表明脚本可能包含了一些额外的功能或者是较为复杂的代码结构。
* 页面上的错误消息可能指向了 GitHub 上的某种操作限制，比如在特定时间内无法提交更改或者执行其他操作。 请注意，由于提供的内容非常有限，以上信息仅基于该片段，可能不能全面反映整个网页的内容。

🏷️: 漏洞利用, GitHub, 代码分析

### 0x03 勒索软件操作者利用ESXi虚拟机管理程序漏洞进行大规模加密

> 微软研究人员发现ESXi虚拟机管理程序中存在的一个漏洞，被多个勒索软件运营商用于获取对域连接的ESXi虚拟机管理程序的完全管理权限，可能导致虚拟机的文件系统加密、数据窃取或网络内部横向移动。

### 热评

* ESXi 域加入漏洞：黑客可获得 VMware ESX 全权限
* AD域管理漏洞：ESX Admins组权限风险

### 关键信息点

* ESXi虚拟机管理程序的CVE-2024-37085漏洞为勒索软件运营商提供了对域连接的ESXi虚拟机管理程序获取完全管理权限的途径。
* 攻击者可以通过利用“ESX Admins”组来提升权限，即使该组在Active Directory中不存在。
* ESXi虚拟机管理程序因其在企业网络中的普及性，成为了勒索软件攻击的热门目标。
* 微软强调了安全更新的重要性，并提供了多种安全措施和工具来帮助企业保护他们的ESXi虚拟机管理程序。

🏷️: 勒索软件, ESXi, 漏洞, 虚拟机管理程序, 网络安全

### 0x04 规则探索者项目REx介绍

> REx项目是一个开源安全检测规则集合的探索和分析平台，旨在通过Elastic Stack的搜索和可视化功能，提供对检测生态系统的深入理解。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZnmMbSSOXzLLv374fC8mUZNtETMq7syicCzRStVibZj0QaLJCWDMzeF8nhDbGjo9UZGzobhujQ0tokQ/640?from=appmsg)

<<<左右滑动见更多 >>>

### 热评

### 关键信息点

* REx项目强调通过可视化和数据分析来提供对检测规则集合的深入理解，以及通过不同视角来观察规则开发、检测工程生态系统和威胁景观。
* DETR作为一个交互式和动态的报告，提供了对规则集的最新快shots、变化趋势和独特性的深入分析，以及对已知威胁的应对分析。
* REx项目鼓励用户通过多种搜索和可视化方式来分析数据，以便从不同的角度和需求出发，获得更多的洞察力和视角。
* 项目的目标不是进行供应商或覆盖范围的比较，而是提供一个用于分析规则和检测工程生态系统的平台，帮助用户创建高质量、高效能的规则。

🏷️: 规则探索, 安全检测, 数据分析, 可视化

### 0x05 利用注册表将Outlook变为C2代理

> TrustedSec 发布了 Specula 框架，这是一个利用 Outlook 注册表更改将电子邮件客户端转变为持续的 C2 通信通道的工具，即使在许多坚固防守的网络中，这种攻击手段仍然未被察觉。

### 热评

* 「编者注」:outlook page这个洞还挺经典的，ruler也支持, 也可以relay或者账密添加恶意page, 并且不在常规安全更新补丁里，得手动打指定的补丁. ps: 之前用这个测试过茄子🤣，离职后，过了几年他重装电脑，发现又中招了，驻留很持久, 除非删除恶意page.

### 关键信息点

* Outlook 的首页功能可以被恶意利用作为 C2 通信通道，即使在应该已经修复的环境中也能有效。
* Specula 框架提供了一个强大、模块化的工具集，用于利用 Outlook 的注册表更改进行持续的 C2 通信。
* 即使在安装了安全更新的环境中，Outlook 的注册表值可能仍然允许攻击者建立 C2 通道。
* 为了防御此类攻击，建议采取多种措施，包括使用新版本的 Outlook、移除 vbscript 引擎、配置 GPO 以及应用安全基线。

🏷️: Outlook, C2, 网络安全, 注册表

### 0x06 Specula框架：在Outlook环境下利用VBScript进行恶意软件操作

> Specula 是一个利用 Outlook 环境下的 VBScript 功能，通过设置自定义首页来实现互动式恶意软件（implant）操作的框架。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnmMbSSOXzLLv374fC8mUZNwWMLJ36amER7BcETsbN1iaec2DsOPde2aGNtDgV88ghbZt3vM8FiaYDA/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnmMbSSOXzLLv374fC8mUZNEPLQ8V4cznO5hCukibyrQw4SXdJJoiavlcSCy8FjQDWiaRKqYXiafmicbPg/640?from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZnmMbSSOXzLLv374fC8mUZNeMFZvOqrmYjFwpWiaIxYJhW8HTfbQaic5aM9tuXiam7tm4SKUlJowmF6A/640?from=appmsg)

<<<左右滑动见更多 >>>

### 热评

### 关键信息点

* Specula 框架的创新之处在于它提供了一种自然且易于扩展的方式来利用 Outlook 作为一个功能完整的恶意软件。
* 安全性和隐蔽性：推荐使用 DNS 记录和 SSL 证书来增强安全性和隐蔽性，减少被检测到的风险。
* 易用性：Specula 提供了详细的安装和配置指南，包括视频教程和注册表项的自动生成工具，以简化用户的操作。
* 配置灵活性：Specula 提供了多种配置选项，允许用户根据自己的需求定制服务器的行为和通信方式。

🏷️: 恶意软件, Outlook, VBScript, Python, Web服务器

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZmwZuG4Yf5KAoarDAr2Ip46vfEibIH57REKzBPUKgDubRickg6g44OtmibSJ6Gaibr8icCItHpX9WyoJJw/640?wx_fmt=jpeg)

快来和老司机们一起学习吧

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

甲方安全建设

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

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