---
title: 【提权基础入门第十一节】UAC绕过：Windows那道总被找到后门的“安全锁”
url: https://mp.weixin.qq.com/s/jCQlAujEwurDdXAF1JGelA
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:32:57.035864
---

# 【提权基础入门第十一节】UAC绕过：Windows那道总被找到后门的“安全锁”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfvZBVxIudUOSzgab6L3BTBdGZ3EDO2Xmic7ZWjAztjoSOSkJgcRauOgekr125WMyU04lR76FkxQbRdVkw2bWjB6m4Tn5PAnhKM/0?wx_fmt=jpeg)

# 【提权基础入门第十一节】UAC绕过：Windows那道总被找到后门的“安全锁”

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 用户账户控制（UAC）是Windows的一道重要防线，设计初衷是防止恶意软件静默提权。但攻击者总有办法绕过它。本文从一个具体例子出发，剖析UAC的原理、绕过手法以及你能做些什么来加固它。

## UAC到底是什么？

2007年，Windows Vista最让人“印象深刻”的新功能——UAC，伴随着铺天盖地的弹窗来了。它的任务很简单：当有程序想干点需要管理员权限的“大事”，比如装软件、改系统设置，就得先问问你同不同意。

你可以把它想象成一栋大楼的安保系统。楼里不同区域有不同门禁等级。

* **低权限区（Low）**

  ：访客通道，比如浏览器从网上下载东西，就限制在这里活动。
* **中权限区（Medium）**

  ：大部分员工办公区，普通用户和标准管理员启动的程序默认就在这儿。
* **高权限区（High）**

  ：机房和总裁办公室，需要真正意义上的管理员权限才能进。
* **系统区（System）**

  ：大楼核心动力系统，服务和内核的地盘。

UAC就是那个站在中权限区和高权限区之间的保安。默认配置是：只要是微软自家的程序（保安脸熟），打个招呼就能进；要是别的公司的程序（生面孔），就得停下来认真盘问（弹窗）。

> UAC的设计哲学是“最小特权原则”，但它不是铜墙铁壁。它更像一个需要人工确认的检查站，如果检查站的规则本身有漏洞，或者保安（用户）习惯性点“是”，防线就形同虚设。

## 为什么UAC会被绕过？漏洞出在哪里

所谓UAC绕过，说白了就是一个中权限的程序，用某种方法骗过了系统，让自己或它的“孩子”程序直接以高权限运行，全程静默，没有弹窗。

绕过手法五花八门，但核心思路往往就几种：利用微软白名单程序、滥用自动提升机制、或者钻注册表和环境变量的空子。

今天说一个经典的例子：利用`fodhelper.exe`。这是Windows自带的一个用于管理可选功能的程序（比如添加语言包），关键点在于它是微软签名的、受信任的，并且有自动提升权限的逻辑。攻击者发现，它启动时会去读取当前用户上下文下的某个特定注册表键值来寻找要执行的命令。

这个机制就出问题了。

### 攻击链拆解：一次完整的绕过演示

1. **布设陷阱**

   ：攻击者（已有一个普通用户权限的shell）在`HKCU\Software\Classes\ms-settings\shell\open\command`路径下，创建一个注册表项，并把默认值设为一个恶意命令。因为是在当前用户（HKCU）下操作，不需要管理员权限。
2. **触发提权**

   ：然后，攻击者执行`fodhelper.exe`。系统看到这是个受信任的微软程序，允许它自动提升权限。
3. **执行恶意代码**

   ：提权后的`fodhelper.exe`忠实地按照设计去读取那个注册表路径，结果执行了攻击者预设的恶意命令。由于`fodhelper.exe`是以高权限运行的，它启动的恶意进程自然也继承了高权限。

整个过程，用户看不到任何UAC弹窗。安全边界悄无声息地被突破了。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TiberTiboKvM5w9zDAh8oJxpqtfeQD8RibltVnmPfh9ehYFlLe2GPwHVUQsPuUoiaR5iaq4ubOSCH8XkLqXoTiazBQVgbBicp1TT1RcljA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibfo6rqVeyaLk7781L0IZcQ36lVezk6I4GnGbYQ59E4VtUYfsNgBcNNyxs5m3TQVeQh3anxTwadwE5pGzPtyIC7BfDKypRTCEYI/640?wx_fmt=png&from=appmsg)

这手法巧妙在哪儿？它没有去攻击UAC验证逻辑本身，而是利用了系统对一个合法、可信程序的信任链。这种“借壳上市”的思路，是很多UAC绕过漏洞的共性。

## 防守视角：如何减轻UAC绕过风险

指望微软堵上所有漏洞是不现实的，新变种总会冒出来。我们能做的是改变游戏规则，增加攻击者的难度和成本。

最有效的一招：**把默认的“征询同意”改成“提示输入凭据”**。

* **默认（征询同意）**

  ：弹窗问你“允许此应用对你的设备进行更改吗？”，点是就完事。
* **改为（提示凭据）**

  ：弹窗要求你**重新输入管理员账号密码**。

这一个小小的改动，能防住绝大部分UAC绕过攻击。因为很多绕过手法（包括上面那个）依赖的是程序自动提升或用户下意识点“允许”。现在必须输密码，就算恶意程序启动了提权流程，也会卡在密码输入框这里。

设置方法：

打开组策略编辑器（运行`gpedit.msc`）或本地安全策略（`secpol.msc`）
定位到：计算机配置 -> Windows 设置 -> 安全设置 -> 本地策略 -> 安全选项
找到策略：“用户帐户控制: 管理员批准模式中管理员的提升权限提示的行为”
将其值从“不提示，直接提升”或“征询同意”改为“提示输入凭据”

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcOibaFemW2uvfMSS72D7evCZs1UDI4RAJjiaOJlkiciaJP9MHPMm61qPd3HHSF7Uf5dIvbQflVxFMYOP3O296qyagh8MVbCm82b4k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeBHZwWZvVxwxqpsIjofNbicUyXU9hJVKtREics5ssNiaXkiaK4ayuaPEEmiaKT3LFKOdFBxwfxug2MpVyx9lwW0Ruh2bPeOemqry1k/640?wx_fmt=png&from=appmsg)

当然，这会给日常管理带来一点麻烦，每次都要输密码。但在安全要求高的服务器或终端上，这个代价完全值得。

其他加固建议：

* **别用管理员账号做日常事**

  ：给每个用户标准账户，需要时再用管理员账户提权。这是UAC设计时预设的最佳实践。
* **保持系统更新**

  ：微软会修复已知的UAC绕过漏洞，尤其是那些被公开的。
* **启用受控文件夹访问**

  （Windows Defender防病毒中）：可以阻止未经授权的程序修改受保护文件夹，增加攻击链难度。

## 检查你的系统：UAC开没开？

检查UAC状态很简单，一条命令就行：

reg query HKEY\_LOCAL\_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\ /v EnableLUA

如果返回的`EnableLUA`值是`0x1`，说明UAC是启用的。如果是`0x0`，那UAC就被关了——这等于直接拆掉了那道安全门。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibetj6nqwpMc8vDh49WH0Uvmc0j0ibN0cMwzibmfRe7WPb2KL9x4WAXF6eOrPXnXPFXfwh5mQXcDsib7YKWUuGDPlYjyNbf3yXaaM4/640?wx_fmt=png&from=appmsg)

也可以用自动化工具如SharpUp来全面审计：

SharpUp.exe audit

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibctMib5Ss2Zs7KSXcQBmIRwicKqnFWo4ZYNcz4m292M1CvvW545558pDLdvvNNpaV2Qg5NrronXUMqHTYT1qeeAaIgAT2YgeSzaM/640?wx_fmt=png&from=appmsg)

## 最后聊聊

UAC从诞生起就伴随着争议，有人说它烦人，有人说它没用。说实话，它确实不是万能的。作为一种主要依赖用户判断的机制，它天生就容易被社会工程学攻击和逻辑漏洞绕过。

但它绝非无用。对于大量自动化传播的恶意软件，UAC弹窗是一道有效的减速带。它把静默安装变成了需要用户交互，这本身就淘汰了许多低级的攻击脚本。

安全从来不是一劳永逸。UAC绕过是攻防对抗的常态。关键在于，我们不能因为这道防线有漏洞就完全不用它。把它调整到更严格的模式（比如要求输入凭据），结合其他安全措施，依然能让攻击者的日子难过很多。

那句话怎么说的？锁防君子也防不了专业小偷，但好锁能让小偷多花十倍工夫，他可能就去找那家没锁门的了。UAC，就是Windows系统上那把你可以、也应该调紧一点的锁。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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