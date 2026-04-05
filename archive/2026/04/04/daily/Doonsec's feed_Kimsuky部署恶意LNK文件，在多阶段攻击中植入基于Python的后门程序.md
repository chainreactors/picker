---
title: Kimsuky部署恶意LNK文件，在多阶段攻击中植入基于Python的后门程序
url: https://mp.weixin.qq.com/s/blpOMhYb7X4gwj8FGcBeQA
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:34:22.841165
---

# Kimsuky部署恶意LNK文件，在多阶段攻击中植入基于Python的后门程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7MwnFB7txrsNKvsM11pIkqS2ypE4nhcSrQHzcS2lsn1PVzYyNXibib7PG82yhU8P5DP2vRdRoKBazzkMZMlvKbgReGEqJibazMk7I/0?wx_fmt=jpeg)

# Kimsuky部署恶意LNK文件，在多阶段攻击中植入基于Python的后门程序

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

一个名为 Kimsuky 的朝鲜威胁组织被发现正在进行网络攻击活动，该活动使用恶意 Windows 快捷方式文件（称为 LNK 文件）在受害者系统上悄悄安装基于 Python 的后门。

该攻击在多个阶段保持隐蔽，使得安全工具在最终有效载荷到达目标机器之前更难检测到它。

Kimsuky 多年来一直活跃，以针对韩国及其他国家的政府机构、研究机构和个人而闻名。

在最近的这次攻击中，该组织改变了其传播恶意软件的方式，与之前的攻击有所不同。

虽然总体目标仍然相同——在受害者的机器上运行Python 后门——但该组织在攻击链的中间增加了更多步骤。

这些步骤使检测更加困难，并让攻击者对感染的展开方式拥有更大的控制权。

ASEC 的研究人员发现了这种转变，并指出 Kimsuky 组织对其恶意 LNK 文件的执行方式进行了明显的结构性改变。

过去，攻击流程是从 LNK 文件到 PowerShell，再直接到 BAT 文件。在最新版本中，中间阶段会依次经过 XML 文件、VBS 文件、PS1 文件，最后到达 BAT 文件，之后才会执行有效载荷。

这条扩展链在每个步骤之间增加了层级，使恶意软件有更大的空间来逃避检测。

本次攻击活动中的 LNK 文件伪装成日常文档，文件名诸如 *“简历（朴成敏）.hwp.lnk”* 和 *“建立数据备份和恢复程序指南（参考）.lnk”*。

这些文件名经过精心设计，看起来非常逼真，以便用户在不怀疑的情况下点击它们。一旦打开，LNK 文件会触发一个隐藏的 PowerShell 脚本，该脚本会在指定位置创建一个 `C:\windirr` 具有隐藏和系统属性的隐蔽文件夹，使其无法在常规文件浏览视图中显示。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7Pdtp4sibt5vblPWcKLIBZibJsaST6zyeVvsKs5p7p9GE5BcdzXH1icTSfej1eXtOh7osQU3iabPmpOcyhD0wiaDtOdaXiauN1u0DXsg/640?wx_fmt=jpeg)

LNK 执行后向受害者显示的诱饵 HWP 文档，旨在掩盖在后台运行的恶意活动。

这次攻击的影响十分严重。一旦后门完全安装，攻击者就能获得对受感染机器的远程控制权限。

攻击者可以运行shell 命令、浏览目录、上传和下载文件、删除文件以及执行其他程序。这种级别的访问权限使攻击者能够在受害者不察觉的情况下，悄无声息地监控并窃取系统中的敏感数据。

## **多阶段感染机制**

感染过程分为几个相互关联的阶段，每个阶段都旨在悄无声息地过渡到下一个阶段，而不会引起安全警报。

打开 LNK 文件后，PowerShell 脚本会创建隐藏文件夹并放置三个文件：一个 XML 任务计划程序文件（`sch_ha.db`）、一个 VBS 脚本（`11.vbs`）和一个 PowerShell 脚本（`pp.ps1`）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PpPwMtR9O58cftYoLqsXVfcuYeVxnsycyI1RIVBBtIoljgibyTve8vW6UvsFI2ZXaE2n7Lp7VTKU81icmNq9vpzuVGJ8XibxaGqU/640?wx_fmt=jpeg)

*名为GoogleUpdateTaskMachineCGI\_\_{56C6A980-91A1-4DB2-9812-5158E7E97388}*的任务  已在受害系统上注册，以每 17 分钟保持持续执行。

XML 文件注册了一个名为 `<task scheduler\_name>` 的任务调度程序 `GoogleUpdateTaskMachineCGI`，设置为每 17 分钟运行一次。这使得恶意软件即使在重启后也能保持活动状态。当 VBS 文件运行时，它会启动 `<task scheduler\_name>`  `pp.ps1`，该程序会收集系统详细信息，包括用户名、正在运行的进程、操作系统版本、公网 IP 地址和杀毒软件信息。窃取的数据随后通过 Dropbox 发送给攻击者。Dropbox 是一种合法的云服务，此处使用 Dropbox 是为了将其融入正常的网络流量中，从而避免被检测到。

该 PowerShell 脚本负责收集受害者系统信息并将其上传到攻击者的 Dropbox 帐户。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7NKVicUPERFySwDncH1WlBsVypZdbTOxPbpgkcewhLZKVxSc6f84tOoJ1o20wTeBenxWJVr7gJ1FWBQF8w4To4jiab4HXIVkJU6U/640?wx_fmt=jpeg)

该 `pp.ps1` 脚本还会从攻击者的 Dropbox 帐户下载一个 BAT 文件（`hh.bat`），并执行它。该 BAT 文件从远程服务器拉取两个 ZIP 片段，将它们合并，并将最终有效载荷提取到 `C:\winii`。

该归档文件包含一个名为 的 Python 后门 `beauty.py`，注册为一个名为 的任务 `GoogleExtension` ，并通过 XML 调度程序启动。

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7MISox1n8urk3rQUTRPQYXfETK0FvutG7WibkSL8Kd8qEZhLWunV37n2kglZLibBJAtkKU5Klmeibeibc2AyR6muIJvWnia8iaLaaSZY/640?wx_fmt=jpeg)

负责下载、合并 ZIP 片段并将最终的 Python 后门部署到受感染系统的批处理脚本。

后门连接到 C2 服务器 `45.95.186[.]232` 端口 `8080`，发送 *“HAPPY”* 数据包以确认感染，并等待命令。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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