---
title: 俄罗斯官方MAX应用的监控风暴——秘密记录、VPN追踪与反规避实证
url: https://mp.weixin.qq.com/s/xyqJ2mm9R_x0b0HhpeZSgA
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:38:10.020549
---

# 俄罗斯官方MAX应用的监控风暴——秘密记录、VPN追踪与反规避实证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lQ1jXOMq3d3cb8pBsDvpIqaZNHm3mNiaMHNcLuXCPZf2MglLKhtsibYvM6ERbu6seVTlBzvUIibLG2OojoicXU7KRAv5mQPwuYnOiagPbzy12je4/0?wx_fmt=jpeg)

# 俄罗斯官方MAX应用的监控风暴——秘密记录、VPN追踪与反规避实证

原创

网空闲话
网空闲话

网空闲话plus

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

俄罗斯官方力推的即时通讯应用MAX，正因一系列严重的安全指控而陷入舆论风暴。综合独立研究人员的逆向工程、数字权利组织RKS Global的验证以及媒体交叉调查，这款由国家支持并强制预装的“超级应用”被证实内置了庞大的监控框架，不仅能够秘密记录用户活动，还构建了一套精密而强硬的反VPN机制。而MAX官方的全面否认，在众多技术实证面前显得苍白无力。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lQ1jXOMq3d0RkhyBR9bO6h7xMYQolcF9WVBqCvv3elQsaRarDx2l449aMZZRibGIOy26DNHKOZyFO6CVVP1Cic63gjcbMSQ7GC4oGbo1UJt7A/640?wx_fmt=webp&from=appmsg)

#### 从“可选项”到“唯一通道”：强制普及下的监控底座

MAX由俄罗斯科技巨头VK开发，2025年3月首次推出，并迅速与政府服务深度整合。决定性的一步发生在2025年9月，MAX被要求**强制预装在俄罗斯境内销售的每一部新智能手机和平板电脑上**。同时，其域名 `max.ru` 被列入俄罗斯技术反制措施系统的白名单，这意味着当其他通讯应用可能遭到封锁时，MAX成为唯一被保证始终可用的平台。这种强制的排他性地位，为大规模监控提供了海量的用户基础和无可回避的入口。

事实上，对其监控潜力的预警早已有之。早在去年，就有安全研究人员指出该应用具有“巨大的监控潜力”。近期，美国基础设施巨头Cloudflare曾将MAX标记为“间谍软件”，虽然该标签在24小时后被撤销，但来自技术社区的警惕可见一斑。

#### 监控代码拆解：从麦克风到设备指纹的全景透视

2026年5月，一名研究人员在俄罗斯安全论坛Habr上发布了完整的MAX APK逆向分析报告，将监控指控推向了最高潮。该报告揭示了至少15项严重安全问题，随后RKS Global对其拆解出的25项具体技术声明进行了静态代码验证，结论是：**14项完全证实，6项部分证实，5项因需动态测试无法在静态层面确证，“但没有一项是完全错误的”**。

在这些发现中，最核心的监控能力直接指向了本文的核心命题——秘密记录与VPN追踪。

**1、无声录音与音频监控**

分析代码显示，MAX集成的定制化WebRTC模块中，存在一个名为 `collect-debug-dump` 的服务器指令。一旦通话建立，服务器可静默下发一个JSON指令，要求以“调试转储”为名，从音频处理管道的6个点位录制原始PCM音频，其中包含**麦克风在降噪前的纯净输入**，最长录制时长可达惊人的2147483647秒。这些音频文件生成后，会通过后台任务管理器的 `SampleUploadWorker` 静默上传至 `apptracer.ru`，整个过程无任何告知与界面提示，形成实质上的无声监听。MAX官方在回应中坚称“不敢拥有监听通话的技术能力”，而研究人员则反诘：这功能并非外来的黑客脚本，而是就写在官方发布的APK代码当中。

此外，该应用早期版本还内置了完整的设备端关键词识别（KWS）与说话人识别引擎，能实时侦听音频流中的特定关键词，并将触发事件及其置信度上报。虽然这一词识别模块在后续版本26.16.0中被移除，但下载并加载ML模型的整套底层框架完整保留——只需服务器重新下发模型文件，该功能即可随时恢复。

**2、绕开VPN的隐形链：去匿名化与实时探测**

MAX对VPN的追踪并非简单的检测，而是一套组合拳。首先，在应用内，从聊天列表到通话界面等五个关键位置会弹出“请关闭VPN以使用MAX”的强制提示。其背后是一个可由服务器远程配置的三级阻断策略：最高一级下，用户只要开启VPN，就被完全禁止访问聊天与小程序，直至关闭VPN。小程序在VPN环境下会直接抛出 `WebAppHasVpnException` 异常。

更隐蔽的去匿名化来自一个经过XOR字符串加密混淆的隐藏SDK，其内部命名空间为 `ru.trace_flow.dps`（数字探测系统）。该模块在每次应用从后台恢复时，会绕过Android系统API，通过反射直接枚举 `tun`、`tap` 等虚拟接口，同时向 `ifconfig.me`、Yandex等**六个外部公网IP检查服务**发起查询，以获取用户的真实公网IP。随后，它把用户ID、设备ID、真实IP、VPN使用标志及SIM卡运营商信息打包，以POST方式发送至一个从未在隐私政策中披露的第三方域名 `trace-flow.ru`。这使得即使用户使用了VPN，MAX也能轻松定位其真实网络身份。RKS Global将“六个IP检查器”列为需动态测试的项目，但其完整逻辑链路已在静态代码中清晰可见。

与之配合的还有一项“主机可达性检查”功能。服务器可动态下发域名列表，让客户端在后台探测Google、Telegram、WhatsApp等服务的连接情况。探测结果连同用户的真实外部IP、运营商信息、VPN开启状态一并打包成JSON，发送至 `OneLog` 分析系统。官方解释此举是为“保障通话质量”，但无法说明为何将IP与VPN状态等高度敏感的组合信息发往分析通道。

**3、无法擦除的永恒指纹**

为实现持久化追踪，MAX利用了一项严重违规的技术：它从设备处理器的可信执行环境中提取Widevine DRM的唯一标识符，进行SHA-256哈希后作为设备ID使用。这个标识符**即使卸载应用、更换Google账号，乃至恢复出厂设置都无法清除**，意味着用户设备将被永久标记。该做法直接违反了Google Play的开发者政策，可能导致应用被下架，但也彻底暴露了MAX超越普通分析、意图对用户实施终生追踪的设计目标。

#### 监控的泛化：一场全国性的反VPN行动

MAX的监控功能并非孤立存在。RKS Global早在2026年4月就发布报告指出，在俄罗斯政府要求互联网服务商于4月15日前具备检测和限制VPN用户能力这一指令推动下，到4月16日，该国最受欢迎的**30款安卓应用全部开始扫描设备上的VPN连接**，其中20款会主动限制功能，MAX、VK系和Yandex系服务均在其中。这表明对VPN的探测与封锁已上升为受政策驱动的系统性工程，MAX是这套体系中最核心、渗透最深的一环。

#### 虚伪的否认与清晰的应对

面对铁证，MAX的公关团队先是将研究人员的分析斥为“虚假”，后又通过公司声明强调“不会监控用户，不会收集个人数据，也不敢拥有监听通话的技术能力”。然而，研究人员逐一拆解了这些反驳，并质问为何要使用违反Google政策的Widevine指纹，暗指其辩解如同“由神经网络生成的表面文章”。

对于不得不使用MAX的用户，RKS Global给出了极低信任度的安全建议：**将MAX视为完全透明的国营电话线路**，默认没有端到端加密，任何敏感言论都不应在其上说出。尽量在备用设备或沙盒化的安卓工作配置文件中使用，授予最小权限，避免通过俄罗斯官方应用商店RuStore安装（其版本存在更大攻击面），并清醒地认识到：普通的VPN在此应用中无法提供你所期望的隐私保护，它反而是触发更深度追踪和功能封锁的信号。

MAX的事件，展示的正是一个通讯工具如何被全面改造为国家监控网络中的一个末梢传感器，它提醒着所有人：当基础设施由不信任的力量控制时，隐私的防线可能比想象中更加脆弱。

参考文献

[1] Castro, C. *Russian researcher claims state-backed MAX app secretly records users and monitors VPNs* [EB/OL]. TechRadar, 2026-05-21. https://www.techradar.com/vpn/vpn-privacy-security/russian-researcher-claims-state-backed-max-app-secretly-records-users-and-monitors-vpns.

[2] Castro, C. *Major Russian Android apps know who's using a VPN, digital rights group warns* [EB/OL]. TechRadar, 2026-04-24. https://www.techradar.com/vpn/vpn-privacy-security/major-russian-android-apps-know-whos-using-a-vpn-digital-rights-group-warns.

[3] owenewans. *5 вещей, которые вы бы не хотели знать о мессенджере MAX: тайная запись звука с микрофона в звонках и много чего еще* [EB/OL]. Habr, 2026-05-18. https://habr.com/ru/articles/1036222/.

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

网空闲话plus

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

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