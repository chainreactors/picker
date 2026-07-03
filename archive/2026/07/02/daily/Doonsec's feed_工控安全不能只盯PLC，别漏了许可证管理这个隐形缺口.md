---
title: 工控安全不能只盯PLC，别漏了许可证管理这个隐形缺口
url: https://mp.weixin.qq.com/s/Pe7S2VgwQZO_fJGsRSbMlw
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:44:03.019775
---

# 工控安全不能只盯PLC，别漏了许可证管理这个隐形缺口

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDpZAKStDBgLB0Dt7WOy65YPRic3VQv2rfMngDTU66O2ueRclPD7AESyCKjXRgkeZM4gy1qlQAfiakM4oXqepPnIUicv1Drw9LyYgE/0?wx_fmt=jpeg)

# 工控安全不能只盯PLC，别漏了许可证管理这个隐形缺口

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在工业自动化场景里，PLC 编程软件、SCADA 监控系统这类核心工具向来是防护重点，但很少有人会留意负责管理软件授权的许可证服务。

最近卡巴斯基安全团队发布的技术分析显示，施耐德电气旗下的浮动许可证管理器存在编号为 CVE-2024-2658 的漏洞，普通本地用户仅靠构造一个配置文件，就有机会拿到系统最高权限，风险甚至能蔓延到整个工业网络。

由于这类设备在很多工业网络中购入即不更新系统，因此风险会一直存在。

CVE-2024-2658 发现于 2024 年，出现在 Schneider Electric Floating License Manager 也就是施耐德电气浮动许可证管理器中，这套软件负责全系列工业自动化产品的授权管理，覆盖从单台 PLC 编程工具到整厂中央控制室系统的各类场景。

浮动授权（Floating authorization）是一种基于服务器验证的软件授权机制，可通过返还和重新发放操作在不同计算机间转移使用权，同时确保激活总数不超过预设上限。 该机制分为局域网和广域网两种类型，支持硬件指纹绑定（CPU、主板、硬盘等）并通过授权管理平台追踪激活记录。

漏洞归类为 不受控搜索路径元素问题。简单来说就是程序调用外部配置文件时，使用了一段硬编码的文件路径，又没有对路径所属目录做严格的权限校验，给低权限用户留下了篡改配置、注入恶意代码的空间。

问题的核心来自软件集成的第三方组件 FlexNet Publisher。这是 Flexera Software 推出的商业授权管理库，大量行业软件都会内嵌它处理许可证逻辑。在 11.19.6.0 及更早的版本中，FlexNet Publisher 没有限制低权限用户修改替换 openssl.cnf 配置文件，最终演变成了完整的权限提升风险。

## 风险根源：一个本不存在的配置路径

要理解攻击的原理，得先理清这套许可证服务的运行机制。

施耐德电气 FLM 的核心是名为 lmadmin.exe 的 32 位后台程序，安装后会自动注册为 lmadminSchneider 系统服务，默认开机自启，运行在 NT AUTHORITY\LOCAL SERVICE 账号下。这个服务负责响应 PLC、HMI、SCADA 等各类设备的许可证请求，是整个授权体系的中枢。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrLQJ41d2lD36NkpGQ323sEVWLNbCicoNM9kQQNAribh8M3g24EyDaRjibanW4ib0AmdRK5u7Qz33ZyNqgL3Sd4uiabr9zcSiaicEFs3g/640?wx_fmt=png&from=appmsg)

服务运行时需要调用 OpenSSL 相关功能，而程序代码里硬编码了一个 openssl.cnf 配置文件的地址，路径中还包含 MS-DOS 8.3 格式的短文件名。整个路径指向 C 盘下一串 cygwin 相关的目录，而这里藏着两个致命的设计缺陷。

第一个缺陷是路径默认不存在。干净的默认安装流程根本不会创建这个目录，程序每次启动都会去一个空地址寻找配置文件。第二个缺陷是权限门槛极低，Windows 系统默认规则下，所有经过身份验证的普通用户，都有权在 C 盘根目录创建新文件夹，也能按照短文件名规则构造出完全匹配的目录结构。

这就相当于程序每次启动都会去一个原本不存在的地址找配置说明书，而任何能登录系统的普通用户，都可以手动搭出一模一样的路径，再放一份自己编写的假说明书进去。程序不会验证文件来源是否可信，只要路径对得上就会直接读取执行。

除了核心服务和配置文件，还有两个组件共同放大了风险。

一个是 FlexNet Publisher 授权库本身，它负责解析 openssl.cnf 里的 [engine] 字段，只要字段中定义了 dynamic\_path 参数，就会不加校验地加载对应路径的 DLL 文件。另一个是内嵌在 lmadmin.exe 进程中的 web 管理门户，分为无需认证的仪表盘页面和需要密码的管理后台，因为门户和服务共享同一块进程内存，一旦服务被注入恶意代码，攻击者可以直接截获管理后台的账号密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDq98YMPX1pKyYyZeJyIicNlDEloxXPKia6MmTl38GsoqkZzHPKgfSj9mGEFmpysP6hsfCHRw530jHCp8YWgXbbXiahAnic8iaewYuRo/640?wx_fmt=png&from=appmsg)

## 完整攻击链：从普通用户到系统最高权限

整个利用过程不需要复杂的零日工具，只要攻击者能以普通用户身份登录安装了 FLM 的机器，就能一步步完成权限突破。

第一步是构造恶意配置。攻击者按照程序硬编码的路径逐层创建目录，最后放入一份篡改过的 openssl.cnf，在配置的引擎段指定 dynamic\_path 参数，指向一个提前准备好的恶意 DLL，文件可以放在 C:\Users\Public 这类所有用户都有写入权限的公共目录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrTdvd6VOL0D5IkGPFIw9t7W2M4Vp5mBEBKLgkyzvvoYVbMctxlMJ5xUKW6ibGy2gdESTUrp55nWAInEHU6pAZl4p0p5lt8XuXM/640?wx_fmt=png&from=appmsg)

第二步是等待服务重启。要让新配置生效需要重启 lmadminSchneider 服务，普通用户默认没有重启服务的权限，但只要主机正常重启，服务就会自动重新加载配置。对于运维场景的服务器来说，补丁更新、例行维护重启都是常见操作，攻击者只需要等待时机。

服务重启后，FlexNet Publisher 初始化 OpenSSL 时会读取攻击者放置的配置文件，找到 dynamic\_path 参数后直接把恶意 DLL 加载进 lmadmin.exe 的进程空间。这时候恶意代码就会继承服务的运行身份，以 NT AUTHORITY\LOCAL SERVICE 账号的权限执行操作。

到这一步还远没有结束。LOCAL SERVICE 账号本身权限受限，但默认配置下这个服务进程拥有 SeImpersonatePrivilege 模拟特权。这个权限允许进程在认证完成后模拟客户端的安全上下文执行操作，攻击者可以通过 RPC、COM 或者命名管道等交互场景，配合 Potato 系列成熟的权限提升工具，进一步把权限提升到 NT AUTHORITY\SYSTEM，也就是 Windows 系统的最高权限等级。

拿到 SYSTEM 权限之后，攻击者可以完全控制主机上的所有配置文件、敏感数据和本地凭证。结合窃取到的许可证管理后台密码，攻击者还能根据网络拓扑向其他工程师工作站横向移动。哪怕不做横向渗透，仅仅关停许可证服务，也会直接导致工业设计和运维软件失效，打断正常的生产维护流程。

解决方案：把施耐德电气 FLM 升级到 3.0.0.0 及以上版本，对应修复 FlexNet Publisher 组件的路径校验逻辑，从代码层面彻底堵住漏洞。

CVE-2024-2658 是非常典型的第三方组件安全案例。许可证管理模块在整个工业软件体系里存在感很低，往往不会成为防护重点，但因为底层依赖的组件缺少路径校验，再结合 Windows 系统的默认权限配置，最终串联成了完整的本地权限提升链路。

工业安全的风险往往藏在容易被忽略的角落，从授权组件到底层运行库再到系统默认配置，任何一个环节的小问题，都可能变成攻破整个生产网络的入口。

往期：

[AI 凭空编出的假域名，正在成为软件供应链的新陷阱](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451187510&idx=1&sn=63d375c93053e54d31662d366ec203dc&scene=21#wechat_redirect)

[当大模型学会逆向拆解EDR，终端安全的天平正在倾斜](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451187497&idx=1&sn=205c20d4d465d4c690f4e2743346a157&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

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