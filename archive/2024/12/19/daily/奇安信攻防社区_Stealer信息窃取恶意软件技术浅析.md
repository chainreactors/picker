---
title: Stealer信息窃取恶意软件技术浅析
url: https://forum.butian.net/share/3941
source: 奇安信攻防社区
date: 2024-12-19
fetch_date: 2025-10-06T19:34:28.281325
---

# Stealer信息窃取恶意软件技术浅析

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### Stealer信息窃取恶意软件技术浅析

样本分析
该样本是一个信息窃取恶意软件，这类恶意软件因能够窃取关键数据（如系统详细信息、自动填充数据、信用卡信息、Cookies、浏览历史、用户名和密码以及加密货币钱包数据）而存在重大风险...

样本分析
====
该样本是一个信息窃取恶意软件，这类恶意软件因能够窃取关键数据（如系统详细信息、自动填充数据、信用卡信息、Cookies、浏览历史、用户名和密码以及加密货币钱包数据）而存在重大风险。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-b38b791955335ab2c2d572afb33a0598d74a28fb.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-4ef11ba98a47e6676ec1b039b5fce2c2e2d6a36b.png)
样本为 32 位文件，采用 Delphi 编程语言编写。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d7b603ab99b1a5e966bd4fd1f3a2538273d57e38.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-9f0576fb0273dbc31e79963ecd67d8811fbf71a3.png)
虽然在 DIE 工具中显示样本为 Delphi 编程语言开发，但进一步分析显示，其核心功能使用 PHP 编写，并通过 ExeOutput for PHP 软件封装。ExeOutput for PHP 可将 PHP 脚本编译为 Windows 可执行文件，这使得恶意软件能够伪装成合法的本地程序运行，同时具备动态加载能力。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d4fbb03c062b15c6e3059aca5247edd02289e067.png)
恶意软件被观察到会通过大量注册表操作来提取系统信息。通过分析确认，恶意软件通过注册表获取计算机名称、用户名、操作系统及其版本、Windows 语言以及 Windows 产品密钥等信息。不过，没有发现任何持久化操作的证据。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-195ebfedb9d65efad14b51b2ac4a5a6229b85c1f.png)
动态分析显示，Ailurophile Stealer 会在磁盘上的特定位置创建一个目录，用于临时存储从受害者系统窃取的数据。
涉及函数：
- `SetCurrentDirectory` 用于将当前工作目录更改为指定路径。
- `CheckFileAccessibility` 并不是一个标准的 Windows API 函数，但这个名字通常用于描述检查文件访问权限或文件是否存在的逻辑。
- `ProcessInputData` 自定义的函数，用于处理数据。
- `DeleteFileOrDirectory`删除文件或目录。
根据分析，存储数据的临时目录位于 `%HOME%\AppData\Local\Ailurophile`。该文件夹会在数据被上传到 C2 服务器后被删除，以避免用户察觉到恶意活动的存在。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ce07539e3f2702e4ce90699a1e3ae394dcbf3e2c.png)
在将被盗数据传输到远程 C2 服务器后，恶意软件会自动删除 `%HOME%\AppData\Local\Ailurophile` 文件夹及其内容，从而彻底清除作案痕迹。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e91181d8a76b914fb21fc60517eda88c9234cb90.png)
运行期间，恶意软件会搜索特定的窗口并尝试将其关闭。动态分析表明，它主要针对浏览器窗口执行此操作。例如，它通过以下命令强制关闭 Microsoft Edge：
```bash
cmd.exe /s /c "taskkill /IM msedge.exe /F"
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-9629611257e964bc5434fbf9375af849396b9ced.png)
恶意软件通过以下命令列出系统中正在运行的所有进程：
```bash
cmd.exe /s /c "tasklist"
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-50a2cfcaafb03e243d57f1085df17a7b1f08ef49.png)
恶意软件首先从磁盘中读取浏览器数据，然后执行以下 PowerShell 命令以解密用户浏览器中的加密数据：
```powershell
cmd.exe /s /c "powershell.exe -Command "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process; Add-Type -AssemblyName System.Security; $decryptedKey = [System.Security.Cryptography.ProtectedData]::Unprotect([byte[]]@(1,0,0,0,208,...), $null, [System.Security.Cryptography.DataProtectionScope]::CurrentUser); $decryptedKeyString = [System.BitConverter]::ToString($decryptedKey) -replace '-', ''; Write-Output $decryptedKeyString""
```
上述命令通过当前用户的身份验证生成解密密钥，用于提取浏览器数据。这种方式是许多窃取恶意软件的常见技术。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-495efabad6bf63eb0269a9a84dd9bdf6f684745b.png)
恶意软件会使用 Kernel32 API 的 `ConnectNamedPipe` 函数实现进程间通信。运行期间，伪装成合法程序的窃取者会创建一个子进程，并通过该子进程执行所有恶意活动。在分析中检测到使用了进程空洞技术（Process Hollowing），以规避杀毒软件的检测。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2030338037d22dcea38d3ee200e369c93f8fa453.png)
通过汇编代码分析，恶意软件调用了以下函数来检测调试器、虚拟机和沙箱环境：
- `RtlQueryPerformanceCounter`
- `QueryPerformanceCounter`
- `GetTickCount`
- `GetSystemTime`
- `IsDebuggerPresent`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-10a4b07c4592f40e5016a3536de61bbebec8afb3.png)
通过分析发现，样本中使用了多种异或（XOR）操作。其中一些用于解密数据库，另一些则用于代码混淆，以提高逆向工程难度并绕过杀毒软件的检测。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-50a7c66beaf8d55a70c2b55a0baff9dff6330237.png)
通过调用 `AdjustTokenPrivileges` 函数，恶意软件尝试提升自身权限。这种技术常用于权限提升攻击，以获取更高的系统访问权限，执行更具破坏性的操作。

* 发表于 2024-12-18 10:02:57
* 阅读 ( 3150 )
* 分类：[二进制](https://forum.butian.net/community/erjinzhi)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![友人Aaaaaaaaaa](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/36845)

[友人Aaaaaaaaaa](https://forum.butian.net/people/36845)

5 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![友人Aaaaaaaaaa](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---