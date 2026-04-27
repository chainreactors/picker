---
title: 73 个与 GlassWorm 关联的 Open VSX Sleeper 扩展程序激活了新的恶意软件活动
url: https://mp.weixin.qq.com/s/Ajaac7Tj4A1mH-fpvfDHWg
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:03:15.275055
---

# 73 个与 GlassWorm 关联的 Open VSX Sleeper 扩展程序激活了新的恶意软件活动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PUN8DHkZx6RTd8mwarO9sFauYAAfvk6R7zxoYlm7altYlFTeDaZ8XHia8cMoqRUppXBX7TIO7RXos5z1KJichCkNhTiajSSicesicY/0?wx_fmt=jpeg)

# 73 个与 GlassWorm 关联的 Open VSX Sleeper 扩展程序激活了新的恶意软件活动

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

针对 Open VSX 市场的GlassWorm供应链攻击已经升级，发现了 73 个新的“潜伏”扩展程序。

该集群于 2026 年 4 月被发现，标志着威胁行为者向软件开发人员分发恶意软件的方式发生了危险的转变。

继 2026 年 3 月发现的大规模浪潮之后，研究人员记录了72 个与 GlassWorm 行动相关的恶意 Open VSX 扩展。

早期变种利用扩展依赖项特性悄无声息地安装恶意加载器。然而，2026 年 4 月出现的新集群表明，攻击者正在改进其策略以规避安全扫描。

## **扩展策略**

潜伏扩展程序是指威胁行为者在将其武器化之前发布的虚假软件包。这些扩展程序最初看起来无害，目的是建立视觉信任、获取信誉并收集下载量。

攻击者利用新创建的 GitHub 帐户发布热门工具的克隆版本。

例如，攻击者创建了一个伪造的Visual Studio Code土耳其语语言包，该语言包与正版语言包极其相似。他们复制了地球图标和描述，只是简单地替换了发布者名称。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7OdFf0vnOqQaYtEc9byRGTnOXVAC3fO5McVreWqL4ISMXbvDeKicgLxfdw3vQTYDVFmeViamA8KE9csInFAKX4QzKicRrWarvhicQU/640?wx_fmt=png&from=appmsg)

一旦开发者安装了这些克隆工具，攻击者就会等待时机，然后推送包含恶意软件的软件更新。在73个新扩展程序中，至少有6个已被激活，用于传播恶意代码。

## **不断演变的递送机制**

在最新版本中，该扩展程序仅充当轻量级加载器，用于获取外部有效载荷。

恶意代码不再直接显示在扩展程序的源代码中，增加了逃避检测的可能性。

该活动主要采用两种执行方式：

* **原生二进制文件：**捆绑的 .node 文件隐藏在扩展代码中。一个简单的 JavaScript 文件运行该二进制文件，其中包含嵌入的 URL，用于下载恶意 .vsix 文件，这些文件会感染 VS Code 和 Cursor 等 IDE。
* **混淆的 JavaScript：**恶意逻辑经过高度混淆，不依赖于捆绑的二进制文件。代码在运行时自行解码，从 GitHub 发布版本中检索恶意 .vsix 有效载荷，并通过命令行路径进行安装。

**妥协的迹象**

安全团队应监控以下指标：

* **本地安装程序二进制文件（SHA256）：** 1b62b7c2ed7cc296ce821f977ef7b22bae59ef1dcdb9a34ae19467ee39bcf168。
* **已下载 VSIX 有效载荷 (SHA256)：** 97c275e3406ad6576529f41604ad138c5bdc4297d195bf61b049e14f6b30adfd。
* **恶意 GitHub 托管：** github[.]com/SquadMagistrate10/wnxtgkih。
* **已确认的恶意扩展：** outsidestormcommand、monochromator-theme、boulderzitunnel、vscode-buddies。

根据 Socket Research Team 的说法，开发者在从 Open VSX 市场安装扩展程序之前，必须验证发布者命名空间并仔细检查下载次数。

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