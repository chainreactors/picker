---
title: 黑客利用思科 Firepower 设备的 n day漏洞获取未经授权的访问权限
url: https://mp.weixin.qq.com/s/WvmXybsgPtQa0Rz_eZ30fA
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:56:00.955877
---

# 黑客利用思科 Firepower 设备的 n day漏洞获取未经授权的访问权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7OczQCcuhm8gwEADm1UN4IctB08YqI36gcfhvf6gibDy5IQia7wpmkAHvwdS3m4LWAiaxMTibWSibH9OM6NBaEodCYJCoYdQib79kiadk/0?wx_fmt=jpeg)

# 黑客利用思科 Firepower 设备的 n day漏洞获取未经授权的访问权限

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

国家支持的威胁行为者正积极利用已知漏洞，通过链接部署高度定制的后门，攻击Cisco Firepower 设备。

Cisco Talos 最近发现，专注于间谍活动的威胁组织 UAT-4356 正在利用两个 n 天漏洞（编号分别为 CVE-2025-20333 和 CVE-2025-20362）渗透Firepower 可扩展操作系统 (FXOS)环境。

UAT-4356 此前策划了 ArcaneDoor 活动，该活动成功地以网络边界设备为目标，进行广泛的间谍活动。

在最近的这次攻击中，攻击者利用其初始访问权限安装“FIRESTARTER”，这是一种高级植入程序，可以对受感染的网络进行未经授权的远程控制。

FIRESTARTER 后门程序深入植入思科 ASA 和 FTD 设备的核心组件中。该恶意软件专门针对 LINA 进程，允许攻击者直接在设备内存中执行任意 shellcode。

## **恶意有效载荷执行**

为了建立控制点，UAT-4356 通过修改 Cisco 服务平台挂载列表来操纵设备的启动顺序。值得注意的是，这种持久化机制完全是瞬态的，仅在正常重启期间触发。

当设备处理标准终止信号时，FIRESTARTER 会将自身复制到备份日志文件中。它会更新挂载列表以确保重新执行。

恶意载荷重新启动后，会通过恢复原始挂载列表和删除临时文件来清除痕迹。

由于该恶意软件严重依赖运行级别状态，管理员可以通过执行硬重启（例如物理断开硬件与电源的连接）来彻底清除该植入程序。

在感染阶段，FIRESTARTER 会仔细扫描 LINA 进程的内存，查找与共享库框架关联的特定字节标记和可执行内存范围。

找到合适的环境后，恶意软件会将其辅助 shellcode 复制到内存中，并覆盖合法的内部数据结构。

此过程成功地将标准的WebVPN XML 处理函数替换为攻击者的恶意例程。然后，FIRESTARTER 会主动拦截传入的 WebVPN 请求。

如果传入的请求匹配特定的自定义前缀，恶意软件会立即执行附加的 shellcode。如果数据缺少所需的前缀，FIRESTARTER 会悄悄地将请求转发给原始处理程序，以避免引起怀疑。

分析人士指出，这种复杂的加载机制与 RayInitiator 的部署策略有大量的技术重叠之处。

## **检测与缓解**

安全团队应主动搜寻 FIRESTARTER 感染，正如Cisco Talos Intelligence 建议的那样，检查工件文件和异常进程，以防止进一步的间谍活动。

组织应采取以下步骤来保护其基础设施：

* 查找隐藏在磁盘上的恶意后台进程或临时核心日志文件。
* 对所有受影响的设备进行重新映像，以彻底清除系统架构中的 FIRESTARTER 感染。
* 终止受损进程，并在非锁定模式下运行的 FTD 软件上重新加载系统。
* 应用思科安全公告和 CISA 紧急指令 25-03中推荐的关键软件升级。
* 部署 Snort 规则 65340 和 46897 以检测漏洞利用，并部署规则 62949 以标记后门活动。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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