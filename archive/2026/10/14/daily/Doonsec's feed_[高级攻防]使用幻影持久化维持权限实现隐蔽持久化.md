---
title: [高级攻防]使用幻影持久化维持权限实现隐蔽持久化
url: https://mp.weixin.qq.com/s/cfJldrmwmTfCQ1QwJDw8yQ
source: Doonsec's feed
date: 2026-10-14
fetch_date: 2026-10-15T06:42:36.369289
---

# [高级攻防]使用幻影持久化维持权限实现隐蔽持久化

# [高级攻防]使用幻影持久化维持权限实现隐蔽持久化

原创

陆安予
陆安予

白帽子安全笔记2.0

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 一、这是什么

之前我介绍了使用强制用户配置文件维持权限的技术[海莲花维持权限攻击手法复现](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485728&idx=1&sn=e89f46c30d188676cb1756b78b715611&scene=21#wechat_redirect)，实际上是利用合法机制进行隐蔽持久化。
为了举一反三此类技术，我还查找了其它方法，例如`LegacyHive`。甚至你可以观察到，目前普遍趋势例如前段时间知名的Defender各种破盾漏洞，全部都是利用合法机制。

最终，我寻找到了一种`极其好用`的维持权限方法，该技术由`美国幻影安全网络安全公司`的总裁`S1n1st3r`发现，其核心在于滥用 Windows 的应用重启机制，通过主动劫持关机流程，诱导内核在关机后期自动写入持久化条目，从而规避基于注册表写入监控的检测。因此取名为`幻影持久化`。

## 二、技术原理

### 1. Windows 应用重启机制

Windows 提供了一套名为 Application Restart and Recovery 的 API，用于在应用崩溃或系统更新导致重启后自动恢复应用状态。其核心 API 为：

```
1

HRESULT RegisterApplicationRestart(PCWSTR pwzCommandline, DWORD dwFlags);
```

调用此 API 注册后，Windows 会在系统关机/重启时记录该应用的信息，并在下次启动时自动重新启动它。（由系统进程 csrss.exe 在关机流程的最后阶段自动写入注册表）

```
1

HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce\Application Restart #<NUMBER>
```

这意味着操作者进程完全不触碰注册表，从而规避了大多数 EDR 的注册表监控。

### 2. 关机流程劫持

幻影持久化的精妙之处在于主动劫持关机流程。当系统发起关机时，隐藏窗口会收到 WM\_QUERYENDSESSION 消息。操作者在此消息处理中执行以下操作：：

1. 1. 调用 ShutdownBlockReasonCreate 声明“系统还在关机中”，暂时阻止关机。
2. 2. 调用 AbortSystemShutdown 取消当前关机流程。
3. 3. 启用 SE\_SHUTDOWN\_NAME 特权。
4. 4. 调用 ExitWindowsEx(EWX\_RESTARTAPPS | EWX\_FORCE, ...) 主动触发带 RESTARTAPPS 标志的重启。

## 三. 运行流程

进程启动调用 RegisterApplicationRestart 注册重启等待 60 秒以满足系统要求创建隐藏窗口并进入消息循环下载并执行远程 Shellcode系统发起关机隐藏窗口拦截 WM\_QUERYENDSESSION阻止关机流程启用 SE\_SHUTDOWN\_NAME 特权主动触发带 EWX\_RESTARTAPPS 标志的重启csrss.exe 在关机后期写入 RunOnce 条目系统重启explorer.exe 读取 RunOnce 条目自动启动该应用重新下载并执行 Shellcode结束开始关机劫持过程持久化写入过程重启恢复过程

此方法`opsec规避`极高，主要体现在：

1. 1. 持久化由Windows在关机最后阶段写入，不触碰注册表。
2. 2. 关机后期大多数 EDR 监控进程可能已离线，检测概率低。
3. 3. 利用合法系统API。
4. 4. 无需管理员权限

微弱缺点：

1. 1. 强制关机或系统崩溃时持久化无效。
2. 2. 仅适合PC，服务器很少重启，因此效果有限。

## 四. PoC代码

为了演示这一点，我录了一个视频（幻影持久化 + APC执行shellcodeloader），但安全起见，我无法提供完整代码。

[视频区域]

> 已在WIN11多个知名杀软中测试。

## 五、使用场景

1.在企业授权的攻防演习中，验证防守方的检测与响应能力
2.理解各类加载技术的实现机制与运行过程
3.在受控环境中测试安全设备的检出情况，用于优化检测策略

## 六、免责声明

本文涉及方案仅限合法授权的安全研究、渗透测试用途，使用者须确保符合《网络安全法》及相关法规。具体条款如下：

1.仅可用于已获得书面授权的目标系统测试；
2.遵守法律法规，不得用于侵犯他人隐私或数据窃取；

本人不承担因用户滥用本软件导致的任何后果。使用即视为同意并接受上述条款。

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqOq43RSf7lfRmsfht4j1OYpZFxV2yBmkPGsNJ4ROQHcUkhseQdibY4vbINt7aotxvSXjWxIEmph546T4Ql1zVcJWTgMNBkYib4ibo/0?wx_fmt=png)

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