---
title: 基于URL的钓鱼邮件在发送成功率上完胜附件的钓鱼邮件
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247535465&idx=1&sn=5d9635f7cf3c17e464419895a50367ea&chksm=c1e9c738f69e4e2e4a89420c32f8324cfdc4b5da326cad38b92008d2b3cb724afa179bf66e23&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-03-18
fetch_date: 2025-10-04T09:58:41.025018
---

# 基于URL的钓鱼邮件在发送成功率上完胜附件的钓鱼邮件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguuYuQvON9tciaicG93HB1frm4ZVsDicqIkJ85DzO9QYnswdo1Na9nLPHAHDA8erhsSW2RlODnLT8B6A/0?wx_fmt=jpeg)

# 基于URL的钓鱼邮件在发送成功率上完胜附件的钓鱼邮件

关键基础设施安全应急响应中心

几十年来，传统钓鱼邮件的头几步一直没有发生变化：邮件含有恶意URL或附件。然而近年来，URL嵌入在网络钓鱼邮件中作为吸引目标受害者的初始手段，其到达目标受害者的速度远高于同样目的的附件。我们去年的数据显示，URL在2022年相比附件继续占主导地位，这有几个原因：可滥用的可信域名、互联网上提供网络钓鱼基础设施的免费服务以及重定向的规避效果。

# **与CredPhish相关的基于URL的网络钓鱼占有很高的比例**

URL继续占主导地位的这种趋势出现在到达企业组织的钓鱼邮件中，许多企业组织都受到知名的安全电子邮件网关（SEG）的保护。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icyzWnEQwbbH4R2OuT6cA3SvoLibMTC0o572EWupASxgqNFkDM0ETFABqOricNro2sH5ibZZXJnzt8Aw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图1. 2021年和2022年，到达收件箱的基于URL的钓鱼邮件和基于附件的钓鱼邮件各自的份额。

基于URL的钓鱼邮件比基于附件的邮件更容易逃脱SEG的检测，这可能有诸多原因。如果可信域名被滥用，URL可能具有固有的信任级别。SEG在识别恶意文件方面可能比识别URL来得更好。相当高比例的良性营销邮件含有来自来历不明的URL，因此很难与来自未知来源的恶意URL区分开来。除了SEG外，威胁分子有更充分的理由使用URL，因为在当今的工作环境中，用户可能更习惯点击未知链接，而不是点击未知附件。图1中的两张图表显示，在2021年至2022年，基于URL的钓鱼邮件所占的份额没有显著变化，但继续比使用附件高出四倍。使用附件所占的份额增加了大约3%。

传统的钓鱼邮件通常以窃取凭据或投递恶意软件为目标。附加的文件和嵌入的URL都可以用于实现这些目标中的任何一个。图2显示，尽管投递恶意软件的电子邮件比凭据网络钓鱼邮件更多地使用附件作为引诱受害者的方法，但两者都主要由嵌入式URL发起。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icyzWnEQwbbH4R2OuT6cA3SKh1375q180Dia7KyZU5dTts6ibL3IgFOd1uDxjYsPvUtrQJssHF4WiaAA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图2. 比较2022年用于凭据网络钓鱼和恶意软件投递的恶意链接和恶意附件。

一般来说，我们预计会看到更高比例的URL出现在凭据网络钓鱼中。这主要是由于大多数凭据网络钓鱼的变体已经要求使用URL。网络钓鱼即服务及其他预构建的网络钓鱼工具常常倾向于使用URL。然而使用附件仍然很常见，HTML和PDF等文件类型是凭据网络钓鱼邮件附件中最常见的类型。

如前所述，使用附件投递恶意软件比我们在凭据网络钓鱼活动中看到的更突出。这可能是由于大多数恶意软件投递已经要求使用文件作为最终载荷，这意味着威胁分子已经有点熟悉文件的使用。下面这种情况也很常见：威胁分子企图投递恶意软件，将恶意文件包含在受密码保护的ZIP压缩包中，以阻挠SEG分析。这增加了我们看到到达最终用户的钓鱼邮件的数量。此外，QakBot和Emotet等一些更高级的大肆传播的恶意软件家族已知在邮件中使用附件，但它们也的确使用嵌入式URL。

# **钓鱼URL及其规避策略**

钓鱼URL是目前最流行的吸引受害者的方法，用在到达收件箱的钓鱼邮件中。威胁分子采用的钓鱼策略以绕过电子邮件安全基础设施而出名，助长了这种情形。到达最终用户的钓鱼URL常常在嵌入式URL中使用以下策略之一（不过也存在其他策略）：

• 可信域名——云服务等可信服务常常被威胁分子滥用以托管恶意内容。这意味着他们的钓鱼网站将托管在被最终用户和SEG等安全基础设施视为可信的域名上。滥用这些服务的钓鱼邮件常常能成功地到达预定目标，因为这些域名无法被完全屏蔽。

• 公开可用的服务——威胁分子经常寻求免费或廉价的服务，以便在网络钓鱼活动中滥用这些服务。这常常甚至会导致他们的URL也有可信域名。任何免费或廉价的托管平台都面临被威胁分子滥用的风险。

• 多次重定向——这是一种常见的策略，嵌入在钓鱼邮件中的URL不是钓鱼攻击的第一阶段。通过使用多次重定向并创建有待分析的恶意URL链，威胁分子常常可以从初始URL重定向到最终页面，最终页面被直接用于下载恶意软件或窃取凭据，而SEG来不及分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icyzWnEQwbbH4R2OuT6cA3SQ0IcVia0cm69tiaaMhuDibaa1ojluoBZd7hErPA5yxC7gcqrKjl5iczVYw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图3. 使用恶意链接的钓鱼邮件示例。

# **恶意附件经配置后以到达收件箱**

为了有效地利用网络钓鱼邮件中的恶意附件，可以采用许多潜在的策略。恶意附件有各种用途，包括直接获取凭据、加入已压缩的其他恶意文件、重定向到钓鱼URL、充当恶意软件的第一阶段下载器，以及其他许多用途。此外，所使用的附件类型通常取决于所投递的威胁。我们在含有恶意附件的网络钓鱼邮件中看到的一些最常见的策略如下：

• 受密码保护的文件——威胁分子通常使用受密码保护的文件（比如ZIP压缩包）来绕过安全机制，到达预定目标。Emotet因使用这种策略而臭名昭著，经常传播大量带有恶意Office文件的邮件，这些文件被压缩到受密码保护的ZIP压缩包中。密码常常放在预定目标容易找到的地方，比如邮件正文。

• 不熟悉的附件——威胁分子经常寻找安全研究人员可能不知道、有机会绕过SEG的的新型附件。由于这种威胁简单、明显，大多数SEG会轻松捕获和阻止直接附加的恶意可执行文件。然而威胁分子已意识到了这一点，最近我们看到QakBot威胁团伙发送直接附加的.ONE文件，这似乎有效地逃避了SEG的检查。

• 编码过的文件——文件编码是一种使恶意附件难以分析的常见方法。HTML文件是威胁分子进行编码的一种非常流行的文件类型，但编码是众多文件类型中很常见的一种策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icyzWnEQwbbH4R2OuT6cA3S7ceqe0iasCicCib46m9gJUe29hUZMXPCMQsq8gFgFyReZMMzA8Q7ib2CPw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图4. 使用恶意附件的钓鱼邮件示例。

**参考及来源：**

https://cofense.com/blog/urls-4x-more-likely-than-phishing-attachments-to-reach-users/

原文来源：嘶吼专业版

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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