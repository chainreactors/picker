---
title: 一日一技 | 用远程「投影」的方式，解决 Windows 微信双开需求
url: https://buaq.net/go-152065.html
source: unSafe.sh - 不安全
date: 2023-03-06
fetch_date: 2025-10-04T08:44:51.569715
---

# 一日一技 | 用远程「投影」的方式，解决 Windows 微信双开需求

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/046fa3c78f07c39eddba43d693cdc17f.jpg)

一日一技 | 用远程「投影」的方式，解决 Windows 微信双开需求

一日一技 | 用远程「投影」的方式，解决 Windows 微信双开需求 我有个人、工作两个微信账号，按照微信的说法，聊天记录仅保存在用户的电脑、手机等设备上，在不同电脑登录同一个微信账号后
*2023-3-5 18:54:11
Author: [sspai.com(查看原文)](/jump-152065.htm)
阅读量:30
收藏*

---

一日一技 | 用远程「投影」的方式，解决 Windows 微信双开需求

我有个人、工作两个微信账号，按照微信的说法，聊天记录仅保存在用户的电脑、手机等设备上，在不同电脑登录同一个微信账号后，每台设备上保存的聊天记录是无法同步的，用起来多少有点不方便。

此前网上流行的一般做法是通过 start 命令同时运行或搭配使用 UWP + Win32 客户端来实现微信「多开」，但这两种方法都会影响微信不久前引入的无需扫码自动登录功能，并且依然无法解决不同电脑上的聊天记录同步问题。

既然无法做到一台电脑同时登录两个微信，那不妨换个思路——**两台电脑分别登录工作号与个人号，然后将其中一台设备上的微信「投影」到另一台上来，不就实现了「双开」并且绕开了聊天记录同步和自动登录等问题吗**？

远程桌面系统大家应该多少都有听说过，微软远程桌面、向日葵、TeamViewer 等工具，所提供的基本都是具备完整桌面连接的远端操控体验。我们需要的则是 2009 年微软在 Windows Server 2008 R2 中推出的，能够提供近似本地程序使用体验、贴合「应用投影」需求的 RemoteApp。

![boxcnJlXeEdsOtNb0IfgSaqPHTd](https://cdn.sspai.com/editor/u_/cg24mblb34t9fp5m6qa0?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

## 前期准备

### 设备要求

RemoteApp 需要一台运行 Windows 系统的电脑充当服务端，且系统版本为 Windows XP ~ 11 专业版、企业版、旗舰版，详细可参考微软[远程桌面服务](https://learn.microsoft.com/zh-cn/windows-server/remote/remote-desktop-services/clients/remote-desktop-supported-config)文档中有关兼容性的介绍。

客户端的设备可使用 Windows、macOS、Android、iOS 等能够连接远程桌面的设备，用于连接 RemoteApp。

### 网络环境

为了保证流畅使用，服务端的上行带宽建议 ≥10Mbps。因为微软的远程桌面没有服务器中转功能，直接将服务端的 `3389` 端口暴露的风险会比较高，为确保安全性，推荐使用代理隧道网络，或 Zerotier、TailScale 等工具部署虚拟局域网。此外你也可以为远程桌面服务配置 SSL 加密，降低非授权访问的可能性。

学校的内部局域网没有 IPv6 地址，无法通过公网直接连接到宿舍具备公网 IPv6 地址的电脑，因此我在这里选用的是 Zerotier 来搭建 Site-to-Site 虚拟局域网，详细方法可参考《[异地网络远程访问指北](https://sspai.com/prime/story/remote-lan-access-guide-03)》等文章，本文不过多介绍。

搭建成功后，我们可以通过 Ping 虚拟局域网的 IP 地址、尝试连接远程桌面来测试虚拟网络是否正常。

### 开启远程桌面服务

微软 RemoteApp 功能是基于 RDP 协议（Remote Desktop Protocol），我们需要打开服务端的远程桌面功能。进入「设置 > 系统 > 远程桌面」，开启远程桌面功能，随后点击「远程桌面用户」，设置允许登入远程桌面的用户。

![](https://cdn.sspai.com/2023/03/05/d89cbce6f9d27a4e7a220919c0899c7b.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

开启远程桌面

设置完成后，可以在同一局域网的设备上尝试能否连接远程桌面。还有一点需要留意，非 Server 系列的 Windows 个人版系统只能保留一个活跃连接，即连接了远程桌面后，已登录的账户会进入锁屏界面暂停使用。

## 部署 RemoteApp

### 下载与安装 RemoteApp Tool、Wix Toolset

![boxcnRV9aTKF5BjO8V3vbHZmQLb](https://cdn.sspai.com/editor/u_/cg24me5b34t9flbpehsg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

[RemoteApp Tool](https://github.com/kimmknight/remoteapptool/) 是一款可以在非 Windows Server 系统上创建与管理 RemoteApp 的工具。首先前往 GitHub 页面下载 RemoteApp Tool 的安装包并将它安装在服务端上。

如果需要为 RemoteApp 生成 MSI 安装包，还需要安装 [WiX Toolset](https://wixtoolset.org/docs/wix3/) 环境——MSI 安装包的优势在于在客户端安装后，客户端可以像本地程序一样，通过开始菜单、桌面的快捷方式来访问 RemoteApp。

### 导入程序、修改配置

![boxcnBTpcrj9TxZnMl9JaBlzzKh](https://cdn.sspai.com/editor/u_/cg24medb34t9e3l011lg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

RemoteApp Tool - 主界面

安装完成后打开 RemoteApp Tool，点击主界面左下角的 Add a new RemoteApp，以微信客户端为例，在弹出的文件框中选择 WeChat.exe 的路径 `C:\Program Files (x86)\Tencent\WeChat\WeChat.exe`，随后设置 RemoteApp 的名称、图标、文件关联，便完成了程序的添加。

### 生成 RDP 文件 / MSI 安装包

添加完成后，选中列表里的 WeChat，点击主界面右下角 Create Client Connection 生成 RDP 连接文件。配置项分为 6 项 —— Host（服务器地址）、Options（生成连接文件的类型）、Gateway（远程桌面连接网关）、File types（文件关联）、MSI options（生成 MSI 安装包的相关设置）、Signing（RDP 签名）。

![boxcnm9d4VVR7dmhsa7afWdCaJc](https://cdn.sspai.com/editor/u_/cg24melb34t9fp5m6qag?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

RemoteApp Tool - Host 配置

需要留意的配置项有 Host、Options 两项 —— Host（服务器地址）配置项中，需要输入服务端的 IP 地址，在 RemoteApp Tool（版本：v6.0.0.0）默认服务端的远程桌面端口为 `3389`，如果内网穿透或防火墙设置中开放的远程桌面端口不是 `3389`，需要修改随后生成的 RDP 连接文件内 `full address` 配置项。Options 配置项里可选择连接文件的生成类型，如 RDP 文件或 MSI 安装包。

![boxcnAnNBVyeLF0uQbMtaGjq6rc](https://cdn.sspai.com/editor/u_/cg24metb34t9fp5m6qb0?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

RemoteApp Tool - Options 配置

![boxcngVNKQqR4HmAC8biJeFSGcd](https://cdn.sspai.com/editor/u_/cg24mfdb34t9e3l011m0?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

RemoteApp Tool - MSI options 配置

完成设置后，点击主界面右下角 Create 便可生成 RemoteApp 的连接文件，将 RDP 文件或 MSI 安装包发送到客户端后，便可连接 RemoteApp。

## RemoteApp 的使用体验

![](https://cdn.sspai.com/2023/03/05/0f0646cb2e4f058d7543ac994028adf0.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

「微信双开」效果图

在 RemoteApp 的加持下，我们就可以在同一台电脑上同时登录并使用个人微信与工作微信，且两边都使用同样的 Win32 版本客户端了，这个版本在小程序、自动登录这两方面的使用体验相比 UWP 版更好；使用 RemoteApp 连接的微信回复消息、水群、摸鱼与本地客户端差别不大，除了文件外，文字、图片也都可以在客户端与服务端之间粘贴。

体验的过程中我也发现 RemoteApp 有着以下几个问题：如果使用了第三方输入法（我使用的是搜狗输入法），客户端上会同时显示两个输入法状态栏，无法通过 `Win + 空格` 快捷键切换，只能关闭或隐藏第三方输入法的状态栏。

![boxcnIsZidBXXt5OkCfV1Ffcm1f](https://cdn.sspai.com/editor/u_/cg24mgtb34t9ebmbibh0?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

阴影残留问题

其次，RemoteApp 的窗口有几率残留窗口阴影、或出现显示光标与实际位置偏移的情况，遇到光标位置偏移时可以先最小化 RemoteApp 再重新呼出，而窗口残影目前没有发现比较好的解决方法。

延迟方面，对于低带宽要求的微信来说使用比较流畅，体验过程中没有出现明显的卡顿，都市天际线、Adobe Photoshop 等涉及大面积内容变化的应用则对服务端与客户端的带宽要求较高。

总的来说，RemoteApp 实现了远程访问应用程序而无需将数据存储在同一台电脑中，网络良好的情况下有着不亚于本地程序的使用体验。连接 RemoteApp 的客户端不局限于 Windows 电脑，macOS、iOS、Android 或 Linux 等设备都可通过生成的 RDP 文件连接远端的 RemoteApp。如果你感兴趣的话值得一试，欢迎在本文评论区反馈讨论使用效果。

题图来自 [Pixabay](https://pixabay.com/illustrations/cartoon-wechat-communication-4802367/)

> 下载 [少数派 2.0 客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，解锁全新阅读体验 📰

> 实用、好用的 [正版软件](https://sspai.com/mall)，少数派为你呈现 🚀

© 本文著作权归作者所有，并授权少数派独家使用，未经少数派许可，不得转载使用。

[![XavierWang](https://cdn-static.sspai.com/ui/img-placeholder.png)](https://sspai.com/u/xavierwang/updates)

H! / 我的博客：https://xavier.wang / 公众号：鸟之言语

文章来源: https://sspai.com/post/78644
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)