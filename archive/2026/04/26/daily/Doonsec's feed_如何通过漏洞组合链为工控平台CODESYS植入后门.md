---
title: 如何通过漏洞组合链为工控平台CODESYS植入后门
url: https://mp.weixin.qq.com/s/9N7PunFuq6yAsV40SKXloQ
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:01:52.549449
---

# 如何通过漏洞组合链为工控平台CODESYS植入后门

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDoG08mGcRjicBeOBdZXicBrk1yDX2RyZu0Anr6ljBF1LRztKgQj9WtSTt1icbMX2ickWZCcicsBd6dH629kKOwOGaOIZiadsHGPbgx9E/0?wx_fmt=jpeg)

# 如何通过漏洞组合链为工控平台CODESYS植入后门

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在现代工业生产中，可编程逻辑控制器（PLC）是控制生产线、发电站、水处理厂等关键基础设施的大脑。

CODESYS 是由德国 3S-Smart Software Solutions 公司开发的一款工业自动化软件平台。它提供了一个集成开发环境（IDE），允许工程师使用符合国际标准 IEC 61131-3 的编程语言（如梯形图、功能块图、结构化文本等）编写控制逻辑，然后将这些逻辑下载到 PLC 上执行。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoGsMvcl2pRyycibk3OpjQHtzN38JBG9108HdMtE3CJg4mxDalBIbwPUHNotiacELibiarpUQUoo5GIzbKXq84VDFgWRibTlCXJdEQI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrAm8tb2FMIeXn4ZW3KHIPl1oCEbynQKTKHKYRYm7cYwISJnZS0XMvGxqXgTmfXVzRibobpPhl0Uqus52jnn3wAticwqcHLD9FkY/640?wx_fmt=png&from=appmsg)

传统 PLC 是一个专用的硬件盒子，里面固化了控制程序。Soft PLC 则是一个纯软件程序，它可以运行在普通的电脑、树莓派甚至服务器上，实现和传统硬件 PLC 完全一样的控制功能。这大大降低了成本，提高了灵活性，但也带来了传统 IT 系统常见的安全问题。

**IEC 61131-3是全球通用的工业控制器编程语言标准，规定了梯形图、功能块图、结构化文本等 5 种编程语言。所有符合这个标准的 PLC，工程师都可以用相同的方法编程，不用重新学习不同厂商的专有语言。**

而 CODESYS 作为全球最广泛使用的 PLC 开发平台之一，被超过 500 家制造商的 1000 多种设备采用，运行在全球数百万台工业设备上。简单来说，CODESYS 就像是工业设备的操作系统和开发工具的结合体。从汽车制造流水线到核电站的控制系统，从智能电网到轨道交通，几乎所有现代工业领域都能看到 CODESYS 的身影。

近期，专门针对工业网络安全的Nozomi Networks发布了一项重要研究，揭示了攻击者如何通过组合多个漏洞，在 CODESYS 应用中植入持久化后门，从而完全控制工业控制系统。

（如何允许拥有有限权限的已认证攻击者完全控制运行 CODESYS Control 运行时的设备。）

这种攻击方式不仅隐蔽性强，而且危害巨大，可能导致生产中断、设备损坏甚至更严重的安全事故。

**本研究针对 CODESYS Control 运行时，特别是适用于树莓派 SL 版本的 CODESYS Control。该版本运行在低成本的 ARM 硬件上，提供完整的 CODESYS Control 功能集，使其成为安全分析的一个易于获取且具有代表性的目标。**

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpQUPPGugz4PPlRVQZh7OfdXCjwib62VOAx1JUV25sR72iavB2Nib4xb9UibcrzVqxpPJILyMyPK8ub6aV7CjACVsLsndtHOwfAuDk/640?wx_fmt=png&from=appmsg)

研究人员发现，攻击者可以通过以下步骤构建漏洞攻击链，而不是依靠单个漏洞攻击，为 CODESYS 应用植入后门：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpDKdAVduYnQxic6mDtcX60y3DY9arZTjbS6VRHTWiaQm2Z19FtFRwILuTG6HwsTeFEic1pdialA1tSk3iaJldC0dxibZQou81Sxq6pM/640?wx_fmt=png&from=appmsg)

### 第一步：获取初始访问权限

攻击的第一步通常是获取对目标 PLC 网络的初始访问权限。这可以通过多种方式实现：

* 利用其他系统的漏洞渗透进入企业网络
* 通过钓鱼邮件攻击工程师的工作站
* 直接攻击暴露在互联网上的 PLC 设备

值得注意的是，许多工业设备仍然直接连接到互联网，并且使用默认密码或弱密码。根据美国国土安全部下属的网络安全和基础设施安全局（CISA）的报告，伊朗相关的网络攻击者近期就利用了这一点，通过合法的工程软件直接访问并控制了美国多个关键基础设施中的 PLC 设备。

### 第二步：绕过身份验证机制

一旦进入网络，攻击者需要绕过 PLC 的身份验证机制才能进行后续操作。CODESYS 系统通常要求用户提供用户名和密码才能连接到 PLC 并进行配置或程序下载。

然而，研究人员发现了多个可以绕过身份验证的漏洞。例如，在某些 Wago PLC 设备中，低权限用户可以通过 Web 界面的访问控制漏洞（CVE-2024-41969）禁用 CODESYS 客户端的身份验证要求。这样一来，任何用户都可以无需密码直接连接到 PLC。

此外，攻击者还可以利用重放攻击漏洞（如 CVE-2019-9013）窃取合法用户的凭据，然后使用这些凭据进行身份验证。

### 第三步：利用启动程序替换漏洞植入后门

这是整个攻击链中最关键的一步。Nozomi Networks 在 2026 年 3 月 24 日披露了一个高危漏洞 CVE-2025-41660，该漏洞存在于 CODESYS Control 运行时系统中，CVSS 评分为 8.8 分（高危）。

该漏洞的原理是：CODESYS 运行时系统在处理启动应用程序（Boot Application）的上传与校验时存在逻辑缺陷。具有低权限的远程攻击者可以利用 CODESYS 通信协议中的文件传输或应用下载服务，非法替换存储在设备上的启动应用程序文件。

由于系统在加载该程序时未能进行充分的完整性验证或强制性的代码签名校验，恶意程序将在系统启动或重新加载时被执行。这意味着攻击者可以将一个包含后门功能的恶意应用程序替换掉原来的合法启动程序，从而在 PLC 中建立持久化的控制通道。

| CVE ID | CWE（通用缺陷枚举） | CVSS v3.1 基础评分 | 风险等级 | CVSS v3.1 向量 |
| --- | --- | --- | --- | --- |
| CVE-2025-41658 | 不正确的默认权限 | 5.5 | 中危 | 本地低权限用户可读取敏感文件 |
| CVE-2025-41659 | 关键资源的权限分配不正确 | 8.3 | 高危 | 远程低权限用户可读取和修改加密密钥 |
| CVE-2025-41660 | 域间资源传输不正确 | 8.8 | 高危 | 远程低权限用户可通过备份功能覆盖任意文件 |

### 第四步：隐藏痕迹并维持长期控制

成功植入后门后，攻击者会采取一系列措施来隐藏自己的踪迹并维持长期控制：

* 修改系统日志，删除与攻击相关的记录
* 配置后门程序在系统启动时自动运行
* 建立加密的通信通道，避免被网络监控系统发现
* 定期更新后门程序，防止被安全软件检测到

##

## 下面为详细如何理解攻击链路

##

CODESYS 开发系统允许使用 IEC 61131-3 语言（如梯形图）对设备进行编程。

将一个简单的程序上传到设备可以展示该部署过程在实践中是如何工作的。

在这种情况下，梯形图应用程序被编译成一个名为`ApplicationName.app`的文件，该文件与校验和文件`ApplicationName.crc`一起传输到`/var/opt/codesys/PlcLogic/`目录。后者包含主应用程序的 CRC 校验和。

对于名为 Application 的应用程序，设备上生成的文件如下，其中`.app`文件包含可执行机器代码：

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqgULaldZu7RSMzrKXMqzBEIxOg9oyBiaIH15FME5lTRzO1VQHXyC4uA7oSw5CHibRvKVKNnGMGicUhPCY0jM2IkZGiagfT9FUjKIE/640?wx_fmt=png&from=appmsg)

CODESYS 开发系统将 IEC 61131-3 代码直接编译为机器代码，然后由之前分析的codesyscontrol进程在运行时加载和执行。不会生成新进程；codesyscontrol加载代码并在其自己的进程中执行它。

这一观察结果具有重要的安全意义：在运行codesyscontrol运行时的机器上部署 IEC 61131-3 代码意味着以 root 权限在设备上执行代码。 这对于管理员来说是预期的行为。CODESYS 运行时甚至允许从 IEC 61131-3 代码调用的原始 C 模块在设备上执行。

CODESYS 运行时支持四个（默认）权限级别：

* 管理员
* 开发者
* 服务
* 监视

每个级别对系统中的各种对象具有不同的访问权限。对于每个对象，一个级别可以拥有（在适用时）：

* 添加 / 删除
* 修改
* 查看
* 执行

管理员可以自定义每个访问权限，但存在默认值。

下图显示了文件系统对象的默认权限。这些是`/var/opt/codesys`文件夹的根文件系统权限，每个子文件夹和文件默认继承这些权限，尽管每个都可以单独自定义。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDod7QDcxfQIBHE4DF3B3Jsskja0gC7bmW7MCUbXbWU0R3vCGlgors7WTOmO9A4qbfrn6rkpGPqE0p8JDbR3cFwJmECaHibCDboI/640?wx_fmt=png&from=appmsg)

从 CODESYS 开发系统备份应用程序，如下图所示，生成的备份是一个扩展名为`.tbf`的文件。该文件只是一个 zip 归档文件，包含一个元数据文件以及`Application.app`和`Application.crc`文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpgsdiccN7BBeAPsQC1wI46toYvrDUMzmibSanTgxgkroY4ialGJic4RYCSBLgcRZiaVia78VO3sSCPqTfJs0lKWYK8kZwBO6bL5OqQY/640?wx_fmt=png&from=appmsg)

由于备份只是一个 zip 归档文件，攻击路径应该很清楚。请注意，.crc文件包含一个简单的 CRC32 校验和，没有加密签名，因此在修改后重新计算它非常容易。 如果使用了加密或签名等可选加密保护措施，CVE-2025-41659 仍然可以为攻击者提供绕过这些保护措施所需的材料访问权限。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoJEeu68tMOUO1Bf0mR3swH5q6ABEbUPnJl3rQ8cN7SUVyq0s8mPl4Uln4tiaJ4mwOfrzMSEhiaHiatgJ00h3pTmnuByfAok0THvI/640?wx_fmt=png&from=appmsg)

服务用户可以按以下方式利用备份和恢复工作流：

1. 从设备下载备份
2. 解压缩并检查应用程序二进制文件
3. 注入生成反弹 root shell 的 shellcode
4. 重新计算`.crc`文件以匹配修改后的应用程序
5. 在设备上恢复被篡改的备份

对于该poc，将 shellcode 放在应用程序的入口点，覆盖了第一条指令。

真正的攻击者可以选择一个不那么显眼的注入点，例如hook一个很少执行的分支，这样应用程序的主要功能保持不变，并且篡改更难被发现。

攻击者无法做的一件事是重启应用程序，而这是植入后门的代码运行所必需的。

因此，攻击者必须等待有人重启应用程序（或重启系统），后门才会触发。

完成这些步骤并等待重启后，shellcode 执行，攻击者获得一个 root 反弹 shell：

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDq3d1GJqga51SrblLYjw99zPsicYNgSSyFbibibDvia1pNGy0TOrqNEOkElbrIGdP4NUvplFsNzvMaWwkqwfzYWIIBbLXBVjX5Z6gg/640?wx_fmt=png&from=appmsg)

此时，权限升级完成：攻击者可以篡改 CODESYS 运行时的本地状态并为自己授予管理员权限。

 值得注意的是，可选的加密保护措施不一定能阻止这种攻击。如攻击场景中所述，CVE-2025-41659 可以让攻击者访问解密和重新加密应用程序所需的材料，并在强制执行签名的情况下，引入受信任的签名材料并在恢复前重新签名修改后的代码。

此攻击链中利用的所有漏洞都已由 CODESYS 修补。

作为这些修复的一部分，CODESYS 默认将代码签名设为强制性要求，然后才能部署或执行 PLC 代码。因此，仍然需要能够创建和恢复备份的服务用户，再也无法在不被发现的情况下篡改应用程序代码。

相关报告:

https://www.nozominetworks.com/blog/backdooring-codesys-applications-via-vulnerability-chaining

往期:

[英国政府发布全球首款显示接口安全设备SilentGlass](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186523&idx=1&sn=439c40fe91a71cdd1368a19b1ef8d6d2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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