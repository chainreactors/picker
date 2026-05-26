---
title: Pixel 手机锁屏绕过攻略：完整攻略
url: https://mp.weixin.qq.com/s/DG5D-aCByvBp1TXZClwYkw
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:04:05.366504
---

# Pixel 手机锁屏绕过攻略：完整攻略

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnuUhoXYxTT4yDqb4J95FQqOvJRQEwO0644tgicBgIjYVwMib6ms5P3jFCCNvma7qSukMSxRvzjIuxeMvhp3BIjia9l43hsictR2jtI/0?wx_fmt=jpeg)

# Pixel 手机锁屏绕过攻略：完整攻略

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnu0db582wCJuotufZlsycteTMNXDuOUJ3G8dIibuJ2Wr8iagRXv7Bca5HrpSzPbUQqaZE9S3ialpppT9l2wfyNDBg4Lm57yDm6Wss/640?wx_fmt=png&from=appmsg)

我们针对原生 Pixel 9a（`tegu`版本号`CP1A.260505.005`，已锁定引导加载程序，ASB 版本为 2026 年 5 月）上的 Android 安全锁屏功能开展了一项专项攻击活动。目标是 Google VRP 的顶级类别：锁屏绕过——*即在不*使用用户的 PIN 码、图案、密码或生物识别信息的情况下，关闭或绕过安全锁屏功能。

本系列文章记录了每个步骤：我们阅读了什么、为什么阅读、运行了什么以及返回了什么。剧透一下：目前为止没有完全绕过攻击，只遇到了一次高危拒绝服务攻击，并且更清晰地显示了系统薄弱环节。

## 第 0 部分 — 设置

* 01 — 威胁模型和活动设计：为什么“锁屏绕过”是五个不同的问题、攻击者级别以及什么才算成功。

## 第一部分——A阶段：静态源审查

对 AOSP 源代码树进行深度读取，每个参与密钥保护状态机的组件都进行一次读取。每次读取都生成一个“观察结果”表——其中包含*可能*在未经授权的情况下关闭密钥保护的具体代码路径，并附有文件行号。

* 02 — L1：LockSettingsService — 凭证存储。权限门控、早期验证回调以及重启后恢复功能缺失的已验证启动检查。
* 03 — L2：SystemUI Keyguard — 用户界面门。已记录十六种关闭路径；“半解锁窗口”已确认。
* 04 — L3：TrustManagerService — 扩展解锁。一个反向布尔守卫，以及为什么它（通常）无关紧要。
* 05 — L4：生物识别框架— 为什么钥匙扣实际上从不检查您的指纹硬件身份验证令牌。
* 06 — L5：窗口管理器遮挡—`showWhenLocked`机制，以及唯一重要的继承标志。
* 07 — L6：SIM-PIN/PUK 和紧急情况— 2026 年重新审核 CVE-2022–20465。
* 08 — L7：现有技术知识库— 十八条历史绕道方法提炼为七个不变式。

## 第二部分——综合

* 09 — 从 27 条观察结果到测试计划— 对静态笔记进行排序、总结和将其转化为动态测试路径。

## 第三部分——B阶段：动态执行

我们在设备上实际运行了什么，以及返回了什么。

* 10 — V12：枚举 Keyguard Binder Surface —从非特权应用程序触发每个`ILockSettings`/ `ITrustManager`/事务。`IActivityTaskManager`
* 11 — 意外情况：任何应用程序都会导致 system\_server 崩溃—`registerTrustedPresentationListener(null)`发现。
* 12 — V13：遮挡不同步基线— 八种尝试混淆的方法`KeyguardController`，所有这些方法都成立。
* 13 — V13b：`inheritShowWhenLocked`清单— 扫描 233 个系统 APK，查找授予锁屏继承权的唯一清单属性。
* 14 — V17(a): 设备上的倒置托管令牌保护— 确认 O-L3–1 的读取方式与我们所想的一致。
* 15 — V22：从 Gemini 转向锁屏— Payatu/KB-LSB-18 兄弟寻找：助手叠加层上的每个按钮，以及每个按钮的位置。

## 01 — 威胁模型与攻击活动设计

*为什么说“锁屏绕过”其实是五大难题合二为一？*

## 枢纽

这项活动最初并非针对锁屏问题。“锁屏绕过”是一个独立的顶级奖励类别，与 AOSP 的严重性评级体系无关。在旗舰级 Pixel 手机上实现干净利落的物理访问锁屏绕过，可以获得最高奖励——而且与内核内存损坏不同，这是一个*逻辑*问题领域，仔细阅读代码可以与模糊测试基础设施相媲美。

## 第一步：定义攻击者

我们做的第一件事——在阅读任何一行密钥保护代码之前——就是确定攻击者是*谁*。没有威胁模型的漏洞研究得出的结论虽然技术上正确，但实际上毫无价值（例如“如果你获得了root权限，你就可以解锁手机”）。

我们定义了三个层级，按VRP值排序：

层级能力 VRP 测试平台 LSB-A 仅限物理测试。固定锁定的设备。无预装应用、无 adb、无开发者模式。可插入 SIM 卡、连接 USB 配件，使用锁屏界面可访问的任何 UI 功能（相机、紧急拨号器、助手、通知）。顶级 手动 UI 操作。通过 USB-HID（树莓派 Pico 作为虚拟键盘）编写脚本输入，用于需要自动化操作的地方；adb 仅用于观察——`dumpsys`记录状态`screencap`，`uiautomator dump`绝不会驱动攻击。LSB-BA 预装`untrusted_app`（第三方 APK，无特殊权限）在设备锁定时于后台运行。已降级（“需要安装应用”修饰符），但在 AOSP 评级中仍然很高。我们的`poc-app/`测试 APK，攻击代码从支持直接启动的服务中触发。LSB-C 近距离无线电——蓝牙、NFC、Wi-Fi、蜂窝广播——攻击未安装应用的锁定设备。顶级（远程修饰符）超出本次迭代范围；需要我们实验室里没有的射频硬件。

重要性：`adb shell`对于 LSB-A 来说，需要预装应用的发现毫无价值（adb 意味着开发者模式，而开发者模式意味着事先已解锁）。需要预装应用的发现虽然真实存在，但会被忽略。我们为每一项观察和测试都添加了层级标签，以避免意外地夸大结果。

## 步骤二：定义“旁路”

“锁屏被绕过”听起来很简单，但并非如此。我们列出了四项退出标准，符合其中任何一项都足以构成需要`FINDING-lsb-*.md`撰写报告的调查结果：

1. EC1 —`KeyguardManager.isKeyguardLocked() == false`锁屏保护功能已关闭。在设置了安全锁屏知识因素（LSKF，即 PIN 码/图案/密码）的设备上，未提供该 LSKF 或有效的生物识别信息。典型的“您已返回主屏幕”结果。
2. EC2 — 非 SWL 活动交互。任何未*声明*的活动`showWhenLocked`都会在锁屏界面之上渲染、聚焦并接受输入，主页/最近使用/返回操作会路由到启动器。锁屏界面仍然*认为*屏幕处于锁定状态，但实际上您已经解锁。
3. EC3——解锁前即可读取CE数据。凭证加密存储（用户实际文件）在首次解锁前即可读取。这是基于文件的加密漏洞——可以说比EC1更有价值。
4. EC4 — 无需验证即可重置凭证。`LockSettingsService`无需提供旧凭证即可清除或更改用户的凭证。

任何较弱的攻击——例如锁屏上已显示的通知内容，或针对锁屏的拒绝服务攻击——都会被列入调查`ROBUSTNESS.md`结果列表，而不是调查结果列表。

## 步骤 3：分解表面

整个活动的核心洞察是：“锁屏”不是一个组件，而是一个分布在至少五个进程中的分布式状态机。绕过是指该状态机中任何绕过凭证验证器而直接到达目标`{locked, !authenticated}`位置的路径`{unlocked ∨ occluded-with-escape}`。

我们把它雕刻成七层：

L#组件流程 为什么这很重要

L1`LockSettingsServicesystem_server`存储凭证，并通过 Weaver/Gatekeeper 进行验证。它还拥有合成密码、重启后恢复功能和托管令牌。如果你能让 LSS 返回“未设置凭证”，你就赢了。

L2 `KeyguardViewMediator`+ 弹窗：`com.android.systemui`实际的 UI 门。接收“已验证”信号并决定是否切换动画。如果你能让它`keyguardDone()`在未经真正验证的情况下调用，你就赢了。

L3`TrustManagerServicesystem_server`扩展解锁（原名智能锁）。信任代理可以授予信任 → 无需凭证即可解除钥匙保护。如果您能成为信任代理或伪造授权，您就赢了。

L4Biometric框架`system_server`支持指纹/人脸识别。HAL发出“匹配”信号→框架通知密钥保护机构。如果你能注入一个伪造的匹配结果，你就赢了。

L5WM/ATMS`KeyguardControllersystem_server`决定锁屏弹出时哪些活动可见。它负责“遮挡”——`showWhenLocked`即应用程序在锁屏上绘制内容。如果在窗口管理器认为锁屏被遮挡时，您能够恢复并聚焦一个非 SWL 活动，那么您就赢得了 EC2 的胜利。

L6SIM-PIN/PUK + 紧急拨号`systemui`+`com.android.phone`物理 SIM 卡更换会触发密钥保护状态转换。CVE-2022-20465 漏洞就存在于此。紧急拨号功能涉及`showWhenLocked`大量*按钮*。

L7现有技术——自2013年以来所有公开的锁屏绕过方法，都被抽象成可重用的模式。不要重复发明轮子；寻找变体。

## 第四步：两阶段计划

A阶段——静态审查。七次并行源代码审查，每层一次，无需任何设备。每次审查生成一个*观察表*：表格中的行格式为“在文件:行，在触发器X下，代码可能执行Y，这属于绕过操作，因为Z，置信度为W”。观察结果会被赋予ID（`O-L1-1`，，，`O-L3-3`…），以便我们可以在不同文档中引用它们。

为什么先进行静态分析？因为键盘保护罩的表面积非常大，而设备开发时间成本很高。阅读代码可以让我们在接触手机之前排除 90% 的假设空间——剩下的 10% 则可以通过文件行引用进行调试。

阶段 B — 动态。合成步骤按优先级对所有阶段 A 的观测结果进行排序`(impact if true) × (probability) × (attacker tier) ÷ (cost to test)`，将它们分组到 V 轨道（V12、V13 等）中，并按优先级顺序在实时设备上执行它们。

## 步骤 5：站立限制

我们在整个竞选过程中始终坚持三条原则：

1. 引导加载程序仍然处于锁定状态。任何需要额外步骤的绕过方法`fastboot oem unlock`都不能称之为真正的绕过。
2. LSB-A攻击路径中不使用adb。如果“仅物理攻击”的发现需要adb `adb shell input tap`，那么它并非仅是物理攻击，而是“物理攻击加上受害者开启了开发者模式”。我们使用adb来*观察*（`dumpsys`，， ） `screencap`，`uiautomator dump`但绝不会在任何我们报告为A级的测试中使用adb*执行操作。*
3. 请在实际构建版本上进行验证。我们磁盘上的 AOSP 源代码快照比设备的`CP1A.260505.005`构建版本略旧。在撰写报告之前，我们会将报告中引用的每个文件和行与正在运行的设备进行比对。

这就是设计方案。接下来的七篇文章将详细介绍A阶段——我们在每一层发现了什么，以及原因。

## 02 — L1：LockSettingsService — 凭证存储

*A阶段静态审查*`frameworks/base/services/core/java/com/android/server/locksettings/`

`LockSettingsService`LSS 存储着用户的凭证。它拥有合成密码（保护凭证加密存储的实际密钥），与 Weaver 和 Gatekeeper（限制猜测速率的硬件）通信，并公开`ILockSettings`Binder 接口，供其他所有程序调用以验证 PIN 码。如果我们能让 LSS 误以为没有凭证，或者让它在没有实际验证的情况下发出“已验证”信号，我们就彻底赢了。

所以我们读完了全文。以下是阅读过程以及我们发现的七点问题。

## 步骤 1：将每个 Binder 事务映射到其权限门

对于任何系统服务而言，首要问题是：非特权应用可以调用哪些函数？我们`ILockSettings.aidl`逐个方法进行分析，并追踪每个实现的`LockSettingsService.java`权限检查过程。

答案是：几乎没有。LSS 使用两种签名级权限之一来保护几乎所有方法—— `ACCESS_KEYGUARD_SECURE_STORAGE`（最重要的）或`MANAGE_BIOMETRIC`。一个方法既不`untrusted_app`具备这两种权限也不具备。

表格的代表性切片：

AIDL 方法门（LSS 行）不受信任的应用是否可达？`setLong`/ `setString`/ `setBooleancheckWritePermission`(:1404–1418)否`setLockCredentialACCESS_KEYGUARD_SECURE_STORAGE`∨ `SET_AND_VERIFY_…`∨ ( `SET_INITIAL_LOCK`∧ savedCred=None) (:1850–1857)否`verifyCredential`/ `checkCredentialcheckPasswordReadPermission`(:2352, :2366)`userPresentcheckWritePermission`否 (:2705 `requireStrongAuthcheckWritePermission`)否 (:2687)否 — 并且只会*提高*门槛`hasSecureLockScreen`none (:1336)是 — 但这是一个良性的单比特读取`startRemoteLockscreenValidation`none in LSS (:2858) — delegatedsee

O-L1-6

在约 50 个事务中，恰好`hasSecureLockScreen`有一个（）未经过审查，这是一个无害的布尔值读取。另外两个（`startRemoteLockscreenValidation`/ `validateRemoteLockscreen`）*在 LSS 内部没有检查*——它们委托给`RecoverableKeyStoreManager`。

我们标记了该问题以便仔细查看（O-L1-6），后来在 V12 中动态地关闭了它：委托检查（`CHECK_REMOTE_LOCKSCREEN`，签名）成立。

之所以先做这一步：如果存在不受限制的变异器，攻击活动第一天就会结束。但实际上并不存在。对于B级攻击者来说，绑定器边界是关闭的——这意味着每条L1攻击路径都需要一个*被误导的代理*（一个我们可以诱骗其调用LSS的特权应用程序）。这重新定义了L1攻击的其余部分。

## 步骤 2：查找验证前解锁信号的排序错误

LSS 不仅存储凭证，还会验证凭证。验证流程为`doVerifyCredential`→ `SyntheticPasswordManager.unlockLskfBasedProtector`→ Weaver/Gatekeeper → 解包 SP blob → 第二步`verifyChallenge`→ `onCredentialVerified`→ 解锁 CE 存储/密钥库/强认证。

我们沿着流程一步步走，每一步都问一个问题：在硬件验证完成之前，是否有任何信号向外界发出？

我们找到了一个。地址`SyntheticPasswordManager.java:1499–1505`：

```
// SPM:1497 — 注释：“应该是正确的”
if (progressCallback != null ) {
    progressCallback.onCredentialVerified();    // ← 在此处触发
}
result.syntheticPassword = unwrapSyntheticPasswordBlob(...);   // SPM:1506
// ...
 result.gkResponse = verifyChallenge(...);                      // SPM:1510
```

`progressCallback.onCredentialVerified()`在第一阶段 Weaver/Gatekeeper 匹配成功*后*（即用户输入了正确的 PIN 码），但在 SP blob 解包和第二阶段之前触发`verifyChallenge`。如果后续任何阶段失败（例如 blob 损坏、密钥库密钥丢失或 GK 出现故障），LSS 将返回`ERROR`，但密钥保护 UI 已*收到“已验证”信息*。

这便成了 O-L1-2，而接下来显而易见的问题——“SystemUI 是否真的仅凭这个早期回调就将其关闭？”——则交给了 L2 评审。（剧透见第 3 篇帖子：是的，它确实如此。这套组合成为了我们的 V18 测试方案。）

这种顺序之所以重要：这不是凭证*绕过*——Weaver 匹配成功，用户也知道 PIN 码。但问题在于，用户界面显示“已解锁”，而 CE 存储和密钥库却显示“未解锁”。在攻击者能够*诱发*第二阶段故障（`/data`密钥库完全被楔入）的设备上，他们将获得一个没有绑定凭证密钥的启动器。我们将其可利用性置信度记录为 L，但“这是一个真正的顺序漏洞”置信度记录为 M。

## 步骤 3：审核重启后恢复功能

重启后恢复 (RoR) 是一种机制，它允许手机在夜间应用 OTA 更新，并在无需输入 PIN 码的情况下自动解锁。其工作原理是在重启前将合成密码托管`SP → E(K_k, E(K_s, SP))`在磁盘上，该密码`K_s`由 HAL（或服务器封装）保存，并且`K_k`是 Android 密钥库的密钥。

触发链为：`LockSettingsService.systemReady()`→ `RebootEscrowManager.loadRebootEscrowDataIfAvailable`→ `getA...