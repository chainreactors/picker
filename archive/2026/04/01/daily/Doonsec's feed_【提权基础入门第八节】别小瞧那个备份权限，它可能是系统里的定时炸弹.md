---
title: 【提权基础入门第八节】别小瞧那个备份权限，它可能是系统里的定时炸弹
url: https://mp.weixin.qq.com/s/iUqxlx7Fb5bBk_HgHD_WQw
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:24:34.083979
---

# 【提权基础入门第八节】别小瞧那个备份权限，它可能是系统里的定时炸弹

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdpicSYDZwx36bFFGSwXu0iaDkozpL1eoZ3RDqiaHZmpSlJwU5ibnTDCctvcJiaq4p9Sw6umia3Nd8rlNTN147mHP0XYibVibW4PePHLA0/0?wx_fmt=jpeg)

# 【提权基础入门第八节】别小瞧那个备份权限，它可能是系统里的定时炸弹

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> SeBackupPrivilege，一个看似为备份而生的合法权限，在Windows权限管理不当的系统中，却能成为攻击者绕过所有访问控制、直达系统核心的秘密钥匙。本文带你深入理解这个权限的运作机制、检测方法以及它如何被用于权限提升攻击。

## 什么是 SeBackupPrivilege？

你在安全策略里可能见过这个选项："备份文件和目录"。在Windows内部，它对应的是`SeBackupPrivilege`。

微软设立它的初衷很单纯：为了让备份软件能正常干活。想象一下你公司的域控制器，里面有数不清的机密文件，每个文件上都有复杂的访问控制列表，规定谁能读谁能写。现在需要做一个全盘备份，难道要手动给备份服务账户授予每一个文件的读取权限吗？显然不现实。

所以，`SeBackupPrivilege`就成了一个"尚方宝剑"。拥有这个特权的用户或进程，可以无视任何文件或目录上的访问控制列表，直接读取内容。

> 问题就出在这里。这把"尚方宝剑"如果发错了人，或者落在了不该拿的人手里，后果不堪设想。攻击者完全可以用它来窃取系统里最敏感的数据。

这个漏洞的危险性常常被低估。许多人觉得，能给用户分配这种特权的高级管理员，自己本身就已经是"上帝"了，还怕什么？但他们忘了，特权可能在继承、在批量配置时被错误地授予，或者通过其他渠道被攻击者获取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfibMb3xjO9xjtwUNKzoZXblVbaklHLLsJm3pGJSbiby5xNZibHeAwZoauOiaC8AZLUW3vJbn1f9wW5dtHcfhI0MjWsAzyzQ9DVxaM/640?wx_fmt=png&from=appmsg)

这不是什么新奇的漏洞，但其影响持久而深远。它代表了对Windows安全模型基础——自主访问控制的一种合法旁路。

## 如何在实验室里复现？

想真正理解一个漏洞，最好的办法就是亲手把它搭出来再打一遍。

### 手动配置环境

第一步，你需要一个有管理员权限的PowerShell窗口。

创建一个测试用户，比如叫"ncv"，并设置密码：

net user ncv Passw0rd! /add

接着，把远程管理相关的服务开起来，方便后续操作。运行`Enable-PSRemoting -Force`，然后把这个新用户加到"远程管理用户"组里。

关键的一步来了：授予`SeBackupPrivilege`。这里需要一个叫Carbon的PowerShell模块来帮忙。安装并导入后，用两行命令完成授权和验证：

Grant-CPrivilege -Identity ncv -Privilege SeBackupPrivilege
Test-CPrivilege -Identity ncv -Privilege SeBackupPrivilege

看到返回True，就意味着这个普通用户已经拿到了那把"尚方宝剑"。

### 更快的脚本化部署

如果你不想一步步敲命令，作者还准备了一个现成的PowerShell脚本`SeBackupPrivilege.ps1`。

用管理员身份运行它，脚本会自动完成从创建用户到授予权限的全部流程。对快速搭建测试环境来说，这非常方便。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdMKicoKdrttUfUZbM0GTeoVnvIQUbm10NicXmmAr8aGHQJbNgdjZ0BmbWTiaLy3HR2beHqT1ZESK3G5bbD2wiaXU7TezWv2uHwib7g/640?wx_fmt=png&from=appmsg)

## 我怎么知道自己有没有这个权限？

攻击的第一步永远是信息收集。作为防守方，你也需要知道自己的系统里有没有这种配置问题。

### 手动检测

最简单直接的方法，打开命令提示符，输入：

whoami /priv

在列出的特权列表中，仔细寻找"SeBackupPrivilege"。看到了，就说明你的当前账户拥有这个危险的能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeOELNtRlA7Bl9V7sL6rP3OKK1veG0lUd4d6jG8TAUibvtmuiaLJlWaLvozeVWmH6iadQ4U2c5kuA281mHqJNUibT5tjnOYTGkYZk8/640?wx_fmt=png&from=appmsg)

### 使用工具扫描

对于规模大一点的系统，手动查就不现实了。这时可以用一些现成的工具，比如**SharpUp**。它是PowerSploit框架里一个很棒的工具，专门用来在Windows本地找提权路径。

运行下面的命令，让它帮你检查特权：

SharpUp.exe audit TokenPrivileges

工具会输出一份报告，清晰地告诉你，当前用户拥有哪些可能被滥用的特权，`SeBackupPrivilege`会赫然在列。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdnHhsdekQnoUSsZAHwAYO5lg1icibIITSF81lyWUd92nKBTXNBcGWsBxKTVL1mLzDRXwJO6rMNRF3rib5icdS79ekic2CQp85s93Og/640?wx_fmt=png&from=appmsg)

## 拿到了权限，然后呢？

现在，假设我们是一个攻击者，已经拿到了一个拥有`SeBackupPrivilege`的普通用户 shell。接下来就是把它变成管理员权限的时刻。

核心思路很清晰：既然我能读任何文件，那系统里最有价值的文件是什么？**SAM数据库和SYSTEM注册表配置单元**。这里面存放着所有本地用户的密码哈希。

1. 找个临时目录，比如`C:\temp`。
2. 利用特权，将SAM和SYSTEM的文件副本保存下来：

   reg save hklm\sam C:\temp\sam.hive
   reg save hklm\system C:\temp\system.hive

   这一步是关键。普通用户绝对无法访问这些核心系统文件，但`SeBackupPrivilege`让我们绕过了所有限制。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdUuEaRXxATLxTNTGDFbdjG4AIL2WdaKuCKPPgLq13RgZ6ib8HmHh14ibXMThoicV8aUHlE7uw5M6Ttb8I23a8n7UHFZpR2DzHO5I/640?wx_fmt=png&from=appmsg)

3. 把这两个`.hive`文件传到你的攻击机上，使用Impacket工具包里的`secretsdump`来提取哈希：

   impacket-secretsdump -sam sam.hive -system system.hive LOCAL

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibftc9G1QUkNxiccboQJO9EdS5QNuqfH6VFp89iaSicuCSN4RdJgamF8mnJ2BRicazAOFliap6QiadJGAiax4dB7jYjKE2MDLR7umDA0ib0/640?wx_fmt=png&from=appmsg)

屏幕上会滚出所有本地用户的NTLM哈希，其中就包括Administrator的。

4. 拿到Administrator的哈希后，攻击就完成了。直接用Pass-the-Hash技术登录，比如用evil-winrm：

   evil-winrm -i [目标IP] -u "Administrator" -H "[提取的NTLM哈希]"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdNwQz4Fbib6TdgsSsxTCROlFXTp5Etjr0ZtZ1oV3E71lafzZR6jX4sck8vkZq7Jjv7maR5XYPe1ibrjWsMvb00Ne91Q6PcWDcHs/640?wx_fmt=png&from=appmsg)

一个普通的、看起来人畜无害的用户，就这样摇身一变，成了系统的最高管理者。整个过程不需要破解任何密码，也不需要利用复杂的缓冲区溢出。

## 怎么防御？收紧你的权限发放

知道了攻击链条，防御就清晰了。核心原则就一条：**严格遵循最小权限原则**。

`SeBackupPrivilege`不应该被授予任何普通用户或日常使用的服务账户。它只应该分配给那些专门用于执行备份任务的、备受监控的服务账户。

检查和移除这个权限的步骤也很简单：

1. 按`Win+R`，输入`secpol.msc`打开本地安全策略。
2. 依次展开"本地策略" -> "用户权限分配"。
3. 在右侧找到"备份文件和目录"这项策略。
4. 双击打开，你会看到一个用户或组列表。仔细审查，将任何不必要的用户或组从中移除。

定期审计用户权限分配应该是安全运维的常规动作。像`SeBackupPrivilege`、`SeRestorePrivilege`、`SeDebugPrivilege`这类高风险特权，更是审计的重点。

说实话，Windows系统里像这样的"合法后门"还有好几个。每一个设计初衷都是为了方便管理，但每一个都可能成为攻击者眼中的突破口。安全从来不是简单地打上补丁，而是对系统每一项权限的清醒认识和严格控制。

---

**参考：**

* Microsoft官方文档：分配给新登录的特殊特权 (https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4672)

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