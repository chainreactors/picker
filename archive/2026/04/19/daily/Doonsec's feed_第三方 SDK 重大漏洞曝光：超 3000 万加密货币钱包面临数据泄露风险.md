---
title: 第三方 SDK 重大漏洞曝光：超 3000 万加密货币钱包面临数据泄露风险
url: https://mp.weixin.qq.com/s/SJh5wLY6FOZyqNHAqNNVIg
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:52:44.387649
---

# 第三方 SDK 重大漏洞曝光：超 3000 万加密货币钱包面临数据泄露风险

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/PO9bjOzlHYDS8FiaA9gtD7ibk4CqRicwdXKVwmmbk9lwJf3iboKFjT5ibd4pz1kkl4xRyJo0dAyDboRoA99FYzfnt5WxHb3DxB7u8nu2XXBJLlFY/0?wx_fmt=jpeg)

# 第三方 SDK 重大漏洞曝光：超 3000 万加密货币钱包面临数据泄露风险

bitbot
bitbot

Desync InfoSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

第三方 SDK 重大漏洞曝光：超 3000 万加密货币钱包面临数据泄露风险

微软安全研究团队在例行研究中发现，广泛使用的第三方 Android SDK —— **EngageSDK（EngageLab）**存在严重的 **Intent 重定向漏洞**。该漏洞允许同设备上的恶意应用绕过 Android 安全沙箱，未经授权访问私密数据。仅加密货币钱包类应用的安装量就超过 **3000 万次**，涉及的用户个人信息、登录凭据和金融数据均暴露在风险之下。

────────────────

目前所有使用受影响版本的应用均已从 Google Play 下架。EngageLab 已在 **v5.2.1** 版本中修复该漏洞。截至文章发布，尚无证据表明该漏洞已被野外利用。

**关键数据：**受影响安装量超 5000 万次（含非钱包应用） | 漏洞修复版本：EngageSDK v5.2.1（2025年11月3日发布） | 来源：Microsoft Defender Security Research

────────────────

一、Android Intent 重定向漏洞原理

图 1：Intent 重定向攻击流程可视化

Android 系统通过 **Intent** 机制实现应用间通信。当一个应用将自身的信任身份和权限"传递"给恶意 Intent 时，就会发生 Intent 重定向攻击。

攻击者利用受攻击应用的可信上下文，以该应用的权限执行恶意负载，可导致：

• 未授权访问受保护组件

• 敏感数据泄露

• Android 环境中的权限提升

**风险等级：严重** — Android 安全团队将此漏洞定性为严重级别。被标记为存在漏洞的应用将面临强制执行措施，包括从平台下架。

二、EngageLab SDK 漏洞深度剖析

EngageLab SDK 是开发者用来管理移动应用消息推送和通知的库。一旦被集成到项目中，它会在构建后的合并清单（merged manifest）中自动添加一个导出的 Activity —— **MTCommonActivity**。

图 2：易受攻击的 MTCommonActivity 被添加到合并清单中

**关键问题在于：**这个 Activity 在合并清单中声明为 exported=true，意味着设备上任何其他应用都可以向它发送 Intent。由于它是在构建过程中自动生成的，开发者在开发阶段往往难以察觉。

三、攻击链详解

当 Activity 接收 Intent 时，取决于其生命周期状态：

• 首次启动 → 调用 onCreate()

• 已处于活动状态 → 调用 onNewIntent()

两种回调都会触发 processIntent() 方法。

图 3：processIntent() 方法调用链

图 4：processIntent() 方法源码分析

该方法从传入 Intent 的 data 字段初始化 uri 变量，若非空则调用 processPlatformMessage()。

图 5：processPlatformMessage() 方法

processPlatformMessage() 会用传入的 URI 字符串创建 JSON 对象，检查其中的 **n\_intent\_uri** 字段。如果存在，将创建 NotificationMessage 对象并设置其 intentUri 字段。

图 6：intentUri 使用概览

**核心漏洞点：**方法调用 parseUri() 时使用了 **URI\_ALLOW\_UNSAFE** 标志（常量值 4），该标志可允许访问应用的 Content Provider。更严重的是，方法表面上构造了一个隐式 Intent（通过 setComponent(null)），但实际返回的是一个**显式 Intent**，可直接调用目标 Activity。

图 7：易受攻击的代码概览

四、利用方式与影响范围

利用过程如下：恶意应用创建一个 Intent 对象，在 extra 字段中嵌入精心构造的 URI。易受攻击的应用处理该 URI 后，会以**自身身份和权限**创建并发送 Intent。

由于 URI\_ALLOW\_UNSAFE 标志的存在，Intent URI 可包含以下权限标志：

• FLAG\_GRANT\_PERSISTABLE\_URI\_PERMISSION — 持久化 URI 权限

• FLAG\_GRANT\_READ\_URI\_PERMISSION — 读取权限

• FLAG\_GRANT\_WRITE\_URI\_PERMISSION — 写入权限

这三种标志组合后，恶意应用可获得对目标应用私密数据的**持久性读写访问权限**，直到目标应用显式撤销。即使 Content Provider 未声明为 exported，也可通过此途径访问。

图 8：获取对非导出 Content Provider 的读写权限

图 9：攻击 MTCommonActivity 的流程

**影响规模：**受影响的钱包类应用安装量超 3000 万次，加上其他使用同一 SDK 的非钱包应用，总暴露量超过 **5000 万次安装**。受影响应用已全部从 Google Play 移除。

五、漏洞披露时间线

|  |  |
| --- | --- |
| 时间 | 事件 |
| 2025 年 4 月 | 在 EngageLab SDK v4.5.4 中发现漏洞，向 EngageLab 报告 |
| 2025 年 5 月 | 将问题升级至 Android 安全团队处理通过 Google Play 分发的受影响应用 |
| 2025 年 11 月 3 日 | EngageLab 发布 v5.2.1，修复漏洞（将 Activity 设为 non-exported） |

六、安全建议

**对开发者：**

• 立即升级 EngageLab SDK 至 **v5.2.1** 或更高版本

• 集成第三方 SDK 后，务必审查**合并后的 Android 清单文件**（merged manifest）

• 特别关注是否存在意外导出的组件或新增权限

• 遵循 Android 开发者安全最佳实践，验证所有导出组件的访问控制

**对用户：**

• Android 已更新自动用户保护机制，针对此漏洞提供额外缓解措施

• 曾下载过受影响应用的用户已受到系统级保护

• 建议及时更新所有加密货币钱包类应用至最新版本

────────────────

**文章来源：**Microsoft Security Blog

**原文链接：**https://www.microsoft.com/en-us/security/blog/2026/04/09/intent-redirection-vulnerability-third-party-sdk-android/

**研究团队：**Microsoft Defender Security Research · Dimitrios Valsamaras 等

**发布日期：**2026 年 4 月 9 日

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

Desync InfoSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

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