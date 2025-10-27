---
title: 「推安早报」0720 | Bitlocker、Responder捕获、 自适应DLL劫持等
url: https://mp.weixin.qq.com/s?__biz=MzU0MDcyMTMxOQ==&mid=2247487565&idx=1&sn=5dede3202afe5235a887e85139d6a3b8&chksm=fb35b985cc42309332cad90bf9a7487a396e5ab61e79389e4f141fc1551b815c2f9e298d7b32&scene=58&subscene=0#rd
source: 甲方安全建设
date: 2024-07-21
fetch_date: 2025-10-06T17:41:28.366710
---

# 「推安早报」0720 | Bitlocker、Responder捕获、 自适应DLL劫持等

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZn2Du7Y5V92JTr3kZxnw3OoEgmYBUlfGuyodTUkYS2Ve4rI819tTTr8jTsz3bhJdoW85Pqq7kzpjQ/0?wx_fmt=jpeg)

# 「推安早报」0720 | Bitlocker、Responder捕获、 自适应DLL劫持等

bggsec

甲方安全建设

# 2024-07-20 安全「信息差」每天快人一步

> 1. 推送「新、热、赞」，降噪增效
> 2. 查漏补缺，你可能错过了一些小东西
> 3. 机读为主，人工辅助，每日数万网站，10w推特速读
> 4. 推送可能大众或小众，不代表本人偏好或认可
> 4. 因渲染和外链原因，公众号`甲方安全建设`发送`日报`或日期,如`20240720`获取完整pdf

### 0x01 提取NTDS文件中BitLocker密码的脚本

> 该网页提供了一个PowerShell脚本，用于从Windows的NTDS.dit文件中提取BitLocker密码恢复相关的记录。

### 关键信息点

* 脚本的目的 是为了帮助管理员或者安全分析师在需要时能够从NTDS.dit文件中提取BitLocker的密码恢复信息。
* 脚本的操作 包括验证NTDS文件的完整性，加载必要的程序集，附加和打开数据库，获取和检查数据表列，遍历记录以提取相关数据，以及最终的清理工作（关闭数据库连接）。
* 脚本的输出 是一个包含BitLocker密码恢复信息的数组，可以通过命令行输出或者图形界面展示。
* 脚本的版本 是20210828.01，表明它是在2021年8月28日发布的，并且在初始版本后进行了优化，移除了冗余的程序集。

🏷️: PowerShell, BitLocker, 数据安全

### 0x02 Respotter：网络Responder实例检测工具

> Respotter 是一个用于检测网络中活跃的 Responder 实例的应用程序，它通过监听 LLMNR、mDNS 和 NBNS 协议的请求来发现可能存在的 Responder 实例，并支持将警报通过 Webhook 发送到 Slack、Teams 或 Discord，也可以将事件发送到 Syslog 服务器。

### 关键信息点

* Respotter 利用 Responder 的特性检测网络中的潜在威胁：通过监听特定协议的请求，Respotter 能够发现网络中的 Responder 实例，这对于网络安全是一个重要的检测手段。
* 集成了多种警报机制：Respotter 支持将警报发送到 Slack、Teams、Discord 或 Syslog 服务器，这有助于及时通知团队成员或将事件整合到安全监控系统中。
* 考虑到通知的平衡：为了避免通知滥发，Respotter 对警报进行了速率限制，确保通知的有效性和重要性。
* 安全运营的考量：Respotter 不会进行响应毒化，这是出于对操作安全（opsec）的考虑，避免对网络中的其他客户端造成干扰或问题。

🏷️: 网络检测, Responder, 警报系统, Webhook

### 0x03 使用组策略在安全模式下自动修复CrowdStrike导致的蓝屏问题

> 网页提供了一个PowerShell脚本解决方案，用于在Windows系统中自动删除导致蓝屏（BSOD）的CrowdStrike驱动程序文件，并在修复后取消Safe Mode启动。

### 关键信息点

* 自动化解决方案：提供的PowerShell脚本实现了自动化删除问题驱动程序文件的功能，减少了手动操作的复杂性和时间消耗。
* 安全模式操作：脚本包括了在Safe Mode下操作的逻辑，确保在系统无法正常启动时也能执行修复。
* 错误处理：脚本中包含了异常处理，能够捕获删除文件过程中可能出现的错误并输出相应的信息。
* 系统恢复：脚本在完成修复后，会自动移除Safe Mode启动选项，确保系统在下次启动时恢复到正常模式。

🏷️: PowerShell, CrowdStrike, 蓝屏, 安全模式, 组策略

### 0x04 自适应DLL劫持攻击技术HADESS解析

> 网页主要介绍了DLL劫持攻击技术，包括其原理、技术变体、防御策略以及相关工具的使用。

### 关键信息点

* DLL劫持利用了Windows应用程序加载DLL的顺序，通过将恶意DLL放置在搜索路径的前面，可以实现对应用程序的控制。
* 已知DLL列表和安全搜索顺序是Windows防止DLL劫持的两种防御机制。
* 导出表克隆和动态IAT修补是DLL劫持的两种高级技术，它们可以在不影响应用程序原有功能的情况下，将函数调用重定向到恶意代码。
* 反射性DLL加载是一种在内存中加载和执行DLL的技术，它可以绕过文件系统检测，使得恶意DLL更难被发现。

🏷️: DLL劫持, Windows安全, 恶意软件, 攻击技术

### 0x05 Electron JS ASAR 完整性绕过

> 本网页主要介绍了如何绕过Electron JS应用程序中的ASAR文件完整性检查。

### 关键信息点

* Electron JS框架的ASAR文件完整性检查机制是为了防止应用程序代码被篡改。
* 通过计算ASAR文件头部信息的SHA256哈希值，可以获取与主执行文件中存储的哈希值相匹配的正确哈希值。
* 即使在没有错误日志的情况下，也可以通过应用程序崩溃时显示的错误信息来获取新的ASAR文件哈希值。
* 开发者可以通过修改ASAR文件，并在主执行文件中更新相应的哈希值来绕过完整性检查。

🏷️: Electron JS, ASAR, 完整性, 应用程序, 代码安全

### 0x06 Dock图标插件或可用于提权

> 网页主要介绍了macOS中Dock tile插件的安全风险，这些插件可能被用于提升权限，导致特权升级和虚拟机逃逸的漏洞，并最终得到了Apple在macOS Sonoma 14.4版本中的修复。

### 关键信息点

* Dock tile插件的设计允许应用在未运行时自定义Dock图标，但这也带来了安全风险。
* 如果Dock tile插件存在于所有用户可访问的目录，它们就可能被用于实现标准到管理员用户的权限升级。
* 在虚拟机环境中，如果共享文件夹被启用，Dock tile插件可以被用来实现虚拟机逃逸。
* Apple在macOS Sonoma 14.4版本中修复了这个漏洞，通过检查应用程序的数据容器来确保插件的安全加载。

🏷️: macOS, 插件, 权限提升

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZn2Du7Y5V92JTr3kZxnw3OolNew6IjUtXCMq4LCWjPUM2CRx21x3fVr68mdgL4CcIHBTmM9njiczQw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZlbmEWU7ZApsl3ia3YLicI4H3nwksKq8ZBqrghjtia9TYiblaxU2VXrUpDcAM57Ric0wX9pBg69IusWVyg/640?wx_fmt=jpeg)

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