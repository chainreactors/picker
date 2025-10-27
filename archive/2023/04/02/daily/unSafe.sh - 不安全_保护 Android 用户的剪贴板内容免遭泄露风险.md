---
title: 保护 Android 用户的剪贴板内容免遭泄露风险
url: https://buaq.net/go-156443.html
source: unSafe.sh - 不安全
date: 2023-04-02
fetch_date: 2025-10-04T11:26:35.480781
---

# 保护 Android 用户的剪贴板内容免遭泄露风险

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

![](https://8aqnet.cdn.bcebos.com/8afa6956fc8de949baa56eb004403f02.jpg)

保护 Android 用户的剪贴板内容免遭泄露风险

导语：安全研究人员发现，中国时尚电子零售商 Shein 的 Android 应用程序存在缺陷，允许从不知情的用户那里获取剪贴板数据并将其传输到远程服务器，受影响的用户数量可能达到数百万。
*2023-4-1 12:0:0
Author: [www.4hou.com(查看原文)](/jump-156443.htm)
阅读量:35
收藏*

---

导语：安全研究人员发现，中国时尚电子零售商 Shein 的 Android 应用程序存在缺陷，允许从不知情的用户那里获取剪贴板数据并将其传输到远程服务器，受影响的用户数量可能达到数百万。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230331/1680247327141159.png "1678239149885491.png")

这种危险形式的恶意软件于 2017 年首次在 Windows 平台上传播，并于 2018 年夏季在阴暗的 Android 应用商店中被发现。2019 年 2 月，在官方 Android 应用商店 Google Play 上首次出现了一个恶意窃取剪切板的程序。

安全研究人员发现一类潜伏在 Google Play 商店中的 Clipper 恶意软件被杀毒软件检测为 Android/Clipper.C 恶意程序，该恶意软件模拟了一个名为MetaMask的合法服务。该恶意软件的主要目的是窃取受害者的凭证和私钥，以控制受害者的以太坊资金。但是，它也可以用属于攻击者的地址替换复制到剪贴板的比特币或以太坊钱包地址。

为了减轻此类隐私风险，谷歌近年来对 Android 进行了进一步改进，包括在应用程序访问剪贴板时显示 toast 消息，并禁止应用程序获取数据，除非它在前台主动运行。

**前言**

安全研究人员发现，中国时尚电子零售商 Shein 的 Android 应用程序存在缺陷，允许从不知情的用户那里获取剪贴板数据并将其传输到远程服务器，受影响的用户数量可能达到数百万，因为 Shein 的 Android 应用程序在 Google Play 商店中的下载量已超过 1 亿次。Shein 原名 ZZKKO，成立于 2008 年，是一家总部位于新加坡的中国在线快时尚零售商。该应用程序目前的版本为 9.0.0，在 Google Play 商店中的下载量已达到上亿次。该公司 2021 年收入超过 150 亿美元，预计 2022 年将超过 200 亿美元。

Microsoft 365 Defender 研究团队表示，他们在 2021 年 12 月 16 日发布的应用程序7.9.2 版本中发现了该问题。该问题已于 2022 年 5 月得到解决。

虽然微软研究人员并未发现应用程序开发人员有任何恶意，但他们认为收集剪贴板数据对用户正确使用该应用程序来说是不必要的。

**Android 剪贴板的安全风险**

Android剪贴板最有趣的特点是它的全局可访问性，也就是说，放在剪贴板上的所有内容都是公共的，设备上所有正在运行的应用程序都可以访问，无需任何权限要求或用户交互。Android甚至允许应用程序通过向系统注册一个回调监听器来监控剪贴板上的数据更改。在桌面环境中，这不是一个严重的安全问题，因为它的剪贴板是用户驱动的，一个窗口应该只在响应用户[1]的命令时将数据传输到剪贴板或从剪贴板传输数据。

相比之下，Android将每个应用程序视为拥有不同特权的不同用户。由于全局无保护访问，各种用户，即应用程序，都可以在Android剪贴板上任意操作，不受任何限制。更糟糕的是，移动设备的屏幕尺寸有限。首先，用户更有可能在移动设备上复制和粘贴数据，以节省打字工作量。此外，在将内容从剪贴板粘贴到应用程序后，用户可以看到的字符更少，从而减轻了攻击者隐藏攻击的工作量。攻击者针对Android剪贴板的另一个优势是在普通应用程序开发中缺乏安全考虑。

考虑到移动用户经常使用剪贴板复制和粘贴敏感信息，如密码或支付信息，剪贴板内容可能成为网络攻击的诱人目标。利用剪贴板可以使攻击者收集目标信息并泄露有用数据。甚至存在攻击者出于恶意目的劫持和替换剪贴板内容的示例，例如在用户将复制的加密货币钱包地址粘贴到加密钱包应用程序或聊天消息之前修改它。此外，这些类型的攻击滥用合法的系统功能而不是利用漏洞，使得问题更难以缓解。

微软的安全团队发现旧版本的 SHEIN Android 应用程序会定期读取 Android 设备剪贴板的内容，如果存在特定模式，则会将剪贴板的内容发送到远程服务器。虽然我们并未具体了解该行为背后的任何恶意意图，但我们评估认为该行为对于用户在应用程序上执行任务而言并非必需。

SHEIN 的 Android 应用程序在 Google Play 商店发布，下载量超过 1 亿次。即使 SHEIN 的剪贴板行为不涉及恶意，这个案例也凸显了安装的应用程序可能带来的风险，包括那些非常受欢迎并从平台的官方应用程序商店获得的应用程序。我们向 Play 商店的运营商 Google 公司报告了我们的发现，推动他们的 Android 安全团队展开调查。2022 年 5 月，谷歌通知我们，我们确认 SHEIN 从应用程序中删除了该行为。我们要感谢 Google 的 Android 安全团队以及 SHEIN 团队为解决此问题所做的努力和协作。

在此博文中，我们详细介绍了我们如何识别 SHEIN 应用程序的剪贴板行为，以及 Android 用户如何保护自己免受基于剪贴板的攻击。我们还与更大的安全社区分享这项研究，以强调协作在提高所有人安全性方面的重要性。

**静态和动态分析**

以下分析详细说明了我们如何识别和验证 SHEIN 应用程序剪贴板行为的存在，我们分析的 SHEIN 应用程序的版本是 7.9.2 (SHA-256: ff07dc6e237acd19cb33e35c60cb2ae52c460aac76bc27116d8de76abec66c51 )。我们首先对应用程序进行了静态分析，以确定对行为负责的相关代码。然后，我们通过在检测环境中运行该应用程序来执行动态分析以观察代码，包括它如何读取剪贴板并将其内容发送到远程服务器。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230331/1680247328121411.png "1678239164199745.png")

图 1. 通过 SHEIN 应用程序导致剪贴板访问的调用链示例

**识别代码**

打开应用程序后，启动器活动com.shein.user\_service.welcome.WelcomeActivity扩展了com.zzkko.base.ui.BaseActivity类，该类在onResume回调中执行对iBaseActivityCallBack.h方法的调用，如下面第 11 行所示:

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230331/1680247328112748.png "1678239180210317.png")

图 2. com.zzkko.base.ui.BaseActivity 类在 onResume 回调 中执行对iBaseActivityCallBack.h方法的调用

com.zzkko.app.iBaseActivityCallBack是由com.zzkko.app.BaseActivityCallBack 实现的接口。上一次调用的方法h ，部分描述如下，在同一类中 执行对方法o 的调用，如第 16 行所示：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230331/1680247328184243.png "1678239191214627.png")

图 3. 方法h执行对同一类中方法o的调用

最后，在com.zzkko.app.BaseActivityCallBack.o方法中调用了com.zzkko.util.MarketClipboardPhaseLinker.f方法，如第 2 行所示：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230331/1680247329696008.png "1678239198173525.png")

图 4. com.zzkko.app.BaseActivityCallBack.o方法调用com.zzkko.util.MarketClipboardPhaseLinker.f方法

方法com.zzkko.app.BaseActivityCallBack.f 的实现逻辑如下图所示，检查字符序列“$”和“://”是否存在于剪贴板文本中，如第 6 行所示。如果两者都存在，则调用同一类中的方法k，并将剪贴板文本作为参数提供，如第8行所示:

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230331/1680247329103242.png "1678239273111739.png")

图 5. com.zzkko.app.BaseActivityCallBack.f方法检查剪贴板中的“$”和“://”，将剪贴板文本作为参数提供给方法k

方法com.zzkko.app.BaseActivityCallBack.k启动一个请求流，该请求流在BaseUrlConstant.APP\_URL + “ /marketing/tinyurl/phrase ”处向服务器执行 POST 请求，解析为https://api-service[.]shein[ .]com/marketing/tinyurl/phrase：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230331/1680247329133826.png "1678239263166536.png")

图 6. 方法com.zzkko.app.BaseActivityCallBack.k启动一个请求流，它向位于BaseUrlConstant.APP\_URL + “ /marketing/tinyurl/phrase ”的服务器执行 POST 请求

由于应用程序的所有活动（用户界面）都扩展了com.zzkko.base.ui.BaseActivity，因此只要用户启动新活动，例如通过启动或恢复应用程序或在其中执行某些操作，就会触发上述调用链应用程序。

**验证代码的剪贴板行为**

为了验证我们的静态分析结果，我们对该应用程序进行了动态分析，该应用程序是我们从 Google Play 商店安装到运行 Android 9 的三星设备上的。

我们使用Frida拦截对android.content.ClipboardManager.getText和com.zzkko.util.MarketClipboardPhaseLinker.f方法的调用，以分析应用程序的剪贴板行为。我们还使用 Frida 绕过应用程序的内置证书，使我们能够使用Burp Proxy分析网络流量。

我们将设备剪贴板的内容设置为https://mybank[.]com/token=secretToken&transaction=100$并打开应用程序。

打开应用程序后，记录了以下调用：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230331/1680247330160405.png "1678239296172944.png")

图 7. 显示应用剪贴板过滤的通话记录

在上面的图 7 中，我们观察到以下内容：

第 28 行：调用函数com.zzkko.util.MarketClipboardPhaseLinker.f

第 29-49 行：堆栈跟踪函数com.zzkko.util.MarketClipboardPhaseLinker.F

第 53、55 行：调用ClipboardManager的hasPrimaryClip和getPrimaryClip方法

最后，执行对api-service[.]shein[.]com 的POST 请求。随后，我们在 Burp Proxy 中捕获了以下请求，显示了剪贴板内容到远程服务器的传输：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230331/1680247331829214.png "1678239308325346.png")

图 8. 将剪贴板内容传输到远程服务器

**安卓剪贴板保护**

如涉及 SHEIN 的此案例所示，Android 应用程序可以调用android.text.ClipboardManager API 来读取或写入设备剪贴板，而无需请求用户批准或需要任何特定的 Android 权限。虽然调用ClipboardManager API 可以让应用程序简化用户的流程，例如快速选择要复制的文本，但应用程序通常不需要这样做，因为复制和粘贴通常由设备输入法编辑器（键盘）执行，它是一个单独的应用程序。

为了解决我们的研究发现和手头更广泛的问题，谷歌已经认识到与剪贴板访问相关的风险，并对Android平台进行了以下改进以保护用户：

在 Android 10 及更高版本上，应用程序无法访问剪贴板，除非它当前具有焦点（正在设备显示屏上主动运行）或被设置为默认输入法编辑器（键盘）。此限制可防止后台应用程序访问剪贴板，但不会阻止此处描述的行为，因为 SHEIN 应用程序在前台运行。

在 Android 12 及更高版本上，当应用程序首次调用 ClipboardManager 以从另一个应用程序访问剪贴板数据时，会显示一条 toast 消息通知用户。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230331/1680247331144488.png "1678239318193867.png")

图 9. 访问设备剪贴板时屏幕底部显示的 Toast 消息示例

Android 13会在一段时间后清除剪贴板的内容，以提供额外程度的保护。

用户可以通过注意剪贴板访问消息来保护自己。如果消息意外显示，他们应该假设剪贴板上的任何数据都可能受到损害，并且他们应该考虑删除任何进行可疑剪贴板访问的应用程序。

**负责任的披露和行业合作提高了所有人的安全**

虽然我们不知道 SHEIN 是否有任何恶意，但即使是应用程序中看似良性的行为也可能被恶意利用。针对剪贴板的威胁可能会使任何复制和粘贴的信息面临被攻击者窃取或修改的风险，例如密码、财务详细信息、个人数据、加密货币钱包地址和其他敏感信息。

我们建议用户进一步遵循以下安全准则来防范此类风险和类似风险：

始终保持设备和已安装的应用程序是更新后的最新状态

切勿安装来自不受信任来源的应用程序

考虑删除具有意外行为的应用程序，例如剪贴板访问 toast 通知，并将该行为报告给供应商或应用程序商店运营商

在发现 SHEIN Android 应用程序剪贴板行为后，我们与 Google 的 Android 安全团队合作，确保从应用程序中删除此行为。我们感谢 Google 和 SHEIN 团队为解决该问题所做的努力和协作。

本文翻译自：https://www.microsoft.com/en-us/security/blog/2023/03/06/protecting-android-clipboard-content-from-unintended-exposure/如若转载，请注明原文地址

文章来源: https://www.4hou.com/posts/6Vgn
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)