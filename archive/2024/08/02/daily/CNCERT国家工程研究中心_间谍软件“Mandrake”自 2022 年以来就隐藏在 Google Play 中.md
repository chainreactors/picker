---
title: 间谍软件“Mandrake”自 2022 年以来就隐藏在 Google Play 中
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546142&idx=3&sn=7a9f6647406db0e2d5bc2a0cd0ba607b&chksm=fa9383dfcde40ac9d9a52d23066bce7492d5d7a44e60858ecc499dad1f5de4b2ba1360eb84da&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-02
fetch_date: 2025-10-06T18:03:58.959945
---

# 间谍软件“Mandrake”自 2022 年以来就隐藏在 Google Play 中

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176m2qTjVgj5dk8hichkDl1YR2W7FWWTS7qN1rPDqsD3hiawB9qKfYmkJzGrCUaG8FwGKTKQLpydtELicA/0?wx_fmt=jpeg)

# 间谍软件“Mandrake”自 2022 年以来就隐藏在 Google Play 中

网络安全应急技术国家工程中心

Bitdefender 于 2020 年首次记录了 Android 间谍软件“Mandrake”，研究人员强调了该恶意软件复杂的间谍功能，并指出它至少从 2016 年开始就在野外运行。

卡巴斯基最近报告称，具有更好的混淆和规避功能的 Mandrake 新变种已经通过 2022 年提交给 Google Play

这些应用程序至少持续可用一年，而最后一个应用程序 AirFS（在受欢迎程度和感染率方面较为突出）于 2024 年 3 月底被删除。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28VOlHIkbj1uFLMhwqZlKQ9Im0S4rvic4PfECgia2MbVicdDiaSPQdz6ymuvtaSJGAaEPcc9db88zbmfw/640?wx_fmt=png&from=appmsg&wxfrom=13)

Google Play 上的 AirFS

卡巴斯基确定了五款携带 Mandrake 的应用程序如下：

· AirFS – it9042 通过 Wi-Fi 共享文件（2022 年 4 月 28 日至 2024 年 3 月 15 日期间下载量为 30,305 次）

· Astro Explorer 来自 shevabad（2022 年 5 月 30 日至 2023 年 6 月 6 日期间下载量为 718 次）

· Amber 来自 kodaslda（2022 年 2 月 27 日至 2023 年 8 月 19 日期间下载量为 19 次）

· CryptoPulsing 来自 shevabad（2022 年 11 月 2 日至 2023 年 6 月 6 日期间下载量为 790 次）

· Brain Matrix 来自 kodaslda（2022 年 4 月 27 日至 2023 年 6 月 6 日期间下载量为 259 次）

该网络安全公司表示，大多数下载来自加拿大、德国、意大利、墨西哥、西班牙、秘鲁和英国。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28VOlHIkbj1uFLMhwqZlKQ9xpibb5bMXYcCQd4IHpVIn84JXg4OYhe2MLNxjRUvwwbHQ2gCokRmSVw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

四款应用将 Mandrake 恶意软件植入受害者设备

# **逃避侦查**

与将恶意逻辑放置在应用程序的 DEX 文件中的典型 Android 恶意软件不同，Mandrake 将其初始阶段隐藏在本机库“libopencv\_dnn.so”中，该库使用 OLLVM 进行大量混淆。

在恶意应用程序安装后，该库会导出函数以从其资产文件夹解密第二阶段加载器 DEX 并将其加载到内存中。

第二阶段请求绘制覆盖的权限并加载第二个本机库“libopencv\_java3.so”，该库解密证书以便与命令和控制（C2）服务器进行安全通信。

与 C2 建立通信后，该应用程序会发送设备配置文件，并在认为合适时接收核心 Mandrake 组件（第三阶段）。一旦激活核心组件，Mandrake 间谍软件就可以执行各种恶意活动，包括数据收集、屏幕录制和监控、命令执行、模拟用户滑动和点击、文件管理和应用程序安装。

值得注意的是，威胁者可以通过显示模仿 Google Play 的通知来提示用户安装更多恶意 APK，诱骗用户通过看似可信的过程安装不安全的文件。

卡巴斯基表示，该恶意软件还使用基于会话的安装方法来绕过 Android 13（及更高版本）对非官方来源 APK 安装的限制。

与其他 Android 恶意软件一样，Mandrake 可以要求用户授予在后台运行的权限，并在受害者的设备上隐藏植入程序应用程序的图标，从而秘密运行。

该恶意软件的最新版本还具有逃避攻击的功能，可在 Frida（一种在安全分析师中流行的动态检测工具包）中存在。

它还检查设备根状态，搜索与其相关的特定二进制文件，验证系统分区是否以只读方式安装，并检查设备上是否启用了开发设置和 ADB。

Mandrake 威胁仍然存在，尽管卡巴斯基认定为植入程序的五款应用已不再在 Google Play 上提供，但该恶意软件可能会通过新的、更难检测的应用卷土重来。

建议 Android 用户仅安装来自信誉良好的发行商的应用，在安装前查看用户评论，避免授予与应用功能无关的危险权限请求，并确保 Play Protect 始终处于活动状态。

Google 也分享了有关在 Google Play 上发现恶意应用的声明表示，Google Play Protect 会自动保护 Android 用户免受已知版本的恶意软件侵害，该功能在安装有 Google Play 服务的 Android 设备上默认启用。Google Play Protect 可以警告用户或阻止已知表现出恶意行为的应用程序，即使这些应用程序来自 Play 以外的来源。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/android-spyware-mandrake-hidden-in-apps-on-google-play-since-2022/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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