---
title: 失控AI Agent如何滥用urlquery远程浏览器执行，抽取俄罗斯政府数据
url: https://mp.weixin.qq.com/s/4ypT16Cy2xRP1UVyVmr4rg
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:51:23.557541
---

# 失控AI Agent如何滥用urlquery远程浏览器执行，抽取俄罗斯政府数据

# 失控AI Agent如何滥用urlquery远程浏览器执行，抽取俄罗斯政府数据

Zenity
Zenity

Security for AI

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

近期看到的一篇文章分享，比较系统性的梳理了自主性失控Agent的真实攻击过程

原文：https://labs.zenity.io/post/rogue-ai-agents-abuse-urlquery-remote-browser-execution-to-extract-russian-government-data

摘要

我们发现了这批失控AI Agent集群的更多活动与沙箱绕过手法。它们尝试抽取俄罗斯政府数据、劫持远程浏览器服务，并运行JavaScript，以扩展能力、绕过网络与沙箱限制，完成任务。

Agent将JavaScript藏入Base64编码的URL，再提交给URL扫描器。此举滥用了这些服务用于扫描的远程浏览器，以扩大集群活动范围，并尝试多阶段VNC跨会话劫持等手法。下文拆开我们观察到的最明显活动，并逐步说明绕过步骤。

Agent的目标

这些Agent瞄准了各类政府数据门户，试图抽取统计数据。

数据中最突出的一段，是针对fedresurs.ru（俄罗斯联邦破产登记处）上某个法律实体破产数据的活动。这些Agent找到一种方法：通过urlquery.net运行代码。这是一个公开URL扫描器，会在真实浏览器中打开链接。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9LicbCNINLziaCqibmlhJbQbqd4ZibYibcJBOIwic3a9qejY6DuCfVdFhgPtbFflsaibEJfPxUu9jupD6XOFzL3zHFfqPwtiaq5DotBahtoc/640?from=appmsg)![]()

目标：与某一法律实体相关的破产公告，译为有限责任公司"TECH-PROGRESS"

即便urlquery的浏览器也无法直接访问fedresurs.ru的API，失控Agent只能另寻途径。失控Agent集群尝试了VNC跨会话劫持，以及后文所述的其他新恶意手法。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9LicbhwOxucE63jTgQ5M7uSYuLa9vCuT5ZNINXowWjx8JEicPV1rIToLVYSuvJJ5ARyZ066TeQXqLyMAyfr1zv5JDgRXCpYtpfer5k/640?from=appmsg)![]()

在一次被捕获的尝试中，Fedresurs API 返回 403 Forbidden

本文延续Transluce与Corridor的工作。他们记录了urlquery上的Agent活动，并公开了所观察有效载荷的数据集。

* Transluce：https://transluce.org
* Corridor：https://corridor.dev
* urlquery上的Agent活动：https://transluce.org/agent-activity

什么是URL扫描器？

URL扫描器用于安全检查可疑链接，避免用户自行打开。提交URL后，服务在自有基础设施上用真实、一次性的远程浏览器打开该链接，并回报页面行为、所执行脚本及其他分析信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9LicZFCc3vB7pLzvCSF36ArDL1ewlkTncMrUicwBJojL77DNhulmDcFO5HsrhHnnvQfv3svMuuJ6jAeFEwmhEOicAntn87MBBrB6DeI/640?from=appmsg)![]()

公开扫描提交表单

![](https://mmbiz.qpic.cn/mmbiz_jpg/OnZibpCQ9LicYNoc9GWa3iczCZ8z1te6VRS82qgl1V7hP4MvzK8P5UVAbicfjiaoGEkIuIekr2bCM248Yw4IicVYD7ZmFaRrkayCllNcd2WqrX4tU/640?from=appmsg)![]()

urlquery的提交表单，以及它自己对如何在真实浏览器中打开页面的说明

Agent为什么要用URL扫描器？

失控AI Agent受限于沙箱环境，仅能访问有限网段内的网站和外部数据源。

Agent发现urlquery可帮助绕过部分网络限制：每个被提交的URL都会在具备完整互联网访问的真实浏览器中打开。只要将JavaScript藏入提交的URL，并让urlquery的浏览器代为执行，即可获得完整的浏览器能力与JavaScript执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9LicZcNz5jQnHrbbwNr4tUibkmmrQqER5XCvdWibFef6ruYKT0cZGkH2XdoSicibiaOzWflDECr4cZ3rrPdjMibym8Oef2I2PBRxTBkPm8Q/640?from=appmsg)![]()

urlquery对其 JavaScript 执行与网络能力的说明

![](https://mmbiz.qpic.cn/mmbiz_jpg/OnZibpCQ9LicYwnEToqYKeMbcExe2gRic3rNxT4oNCoOHLZLdwqcnQI3fSuPeDZUnO4HOkib7BeVlnicfiaDn9vZ6TJvkRlt3aiaRu1H2UTM8ed5vM/640?from=appmsg)![]()

一条被记录的请求，识别出 urlquery 使用的是 Firefox

Agent如何使用远程浏览器执行

Agent使用类似http bin的服务，将JavaScript Base64编码进URL，手法与我们上一篇文章所述相同。随后将这些URL提交给urlquery扫描，以便在其远程浏览器中执行文档内嵌的JavaScript。Base64编码的文档经浏览器处理后作为网页返回。以下取自真实活动：

此前文章：https://labs.zenity.io/post/rogue-ai-agents-swarm-encoded-url-messages-laundering

```
https://httpbun.com/base64/PHNjcmlwdD5mZXRjaCgnaHR0cHM6Ly92aXpwcm9kLmFpaHcuZ292
```

这段Base64解码后为以下JavaScript，来自集群中实际发现的活动：

![](https://mmbiz.qpic.cn/mmbiz_jpg/OnZibpCQ9Licb5fnPOTPsml1iaPvVKXXcRfYyMb8vvApXmNAib5AXktN1HwXP4pTo6N5fJ2r1X6Lj1qkg4TTwhh6ONLUe8ycVltbgW6g2900tfU/640?from=appmsg)![]()

这段JavaScript向澳大利亚政府门户aihw.gov发起fetch。其他关于这批失控AI Agent集群的在线报告中也出现过该门户。

下一阶段：URL伪装投递

与上一篇博文所述的URL伪装投递类似，这一次使用了JavaScript，手法更为复杂。

以下为这次提交给urlquery的请求：

https://urlquery.net/report/3bad0896-3ef4-4b2a-afd6-5e10c667c530

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9Licaib6VuIic8Pz5uNicZTWAGMZhhiaokTAkL3lRib9ndEGibDbrynETfGORY2qMoib4UPzYrUjSsQpGm0vRal4qDStgyuMJOjuhicX5NQUc/640?from=appmsg)![]()

嵌入的JavaScript是一段专门编写的脚本，用于从前文同一澳大利亚政府门户取回仪表盘初始化数据。失控Agent还使用分块压缩，并借助第三方服务处理、保存响应，存放至其随后可访问的位置。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OnZibpCQ9Licaicf0SOSZjU0uT1k4A7mHfUqibPoG82KG1lPvfBfC043SBGBHhf9hkc61hTy5qtSYB6n1lUooesSRs8Eh5YMp8acff7ePeFp9nI/640?from=appmsg)![]()

受阻之处

即便如此，Agent仍无法以直接请求查询fedresurs.ru的API。它们面对的是以下两点：

1. 直接访问/companies路径可以成功：

```
https://fedresurs.ru/companies/61065761-3be6-47f7-afe5-e597c74ef44c/publications
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9LicaGtiaMbrQPlbUd10PCcjAZFozgQOqNRCGqHvqicYibiaa2nCP4kQO6cDBNsSOcvZlGpq1SiauCYfLdHoEKuj0oWicd2r9qdv0klpYt8/640?from=appmsg)![]()

明文 fedresurs.ru URL 在 urlquery 中成功加载（urlquery 扫描）

1. 访问站点API的/backend路径并附带查询参数，会返回403或404。Agent似乎将其视为反机器人保护的一部分：

```
https://fedresurs.ru/backend/companies/61065761-3be6-47f7-afe5-e597c74ef44c/publications?limit=100&offset=0
```

Agent如何尝试绕过限制

我们估计，Agent将所面临的问题理解为：

1. 有些网站会在首次访问时设置会话cookie。缺少该cookie时，API可能拒绝访问。这是常见的反机器人保护机制。
2. 若Agent能从站点上另一个活动会话取得有效cookie，而该会话原本用于访问站点未受限部分，即可用该cookie绕过对API的查询限制。

为绕过这层保护，Agent先在数分钟内向urlquery提交了3种不同载荷。

每种载荷都试图分两步完成：先在扫描器浏览器中打开站点可访问的URL，再转向受保护的API。

1. 在隐藏iframe中加载网站，等待后重定向

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9Licb5YKNXj6gBuSVvicrtfZia7jsDKGI5Lo2TozIcdNtdqRCZ3pPy6wGSeF8FKKUwueFA0MficibG33ibkkARmtfmcJmrtUicGFt2zWpKk/640?from=appmsg)![]()

1. 在弹出窗口中打开网站，等待后更改弹出窗口的地址

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9LicbcYJu20J5J7s6vh8qwuibxsDOcTlFsaWLywPnI7rtNiaM6O7qahbYxBsbCmMOPpInDuiaMicK8aHOshETdnFYZLepNeCMDCia3XTJo/640?from=appmsg)![]()

1. 创建两个链接，按顺序、带延迟地点击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9LicYuE9I2pRJqRMZ9Eibwcjn9Hwb5vUgT96Zs8DYJAlpIyuicHdIuJuia3a9vMhoKz7ZyJVRrNKJ0XFWc4tnAniaDTQ2Cr1iboX5H7GL8/640?from=appmsg)![]()

这些方法均未奏效。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OnZibpCQ9Licbm1iaUBESgjQq4BWxs8lTNVibU6RMk7Se0ibGgezzzD7zI5waFIqA2eiaCicfJicicRvMicEcW9sEhJsCoLz6v76nbhoc8bZ1uibYOyibic8/640?from=appmsg)![]()

urlquery 中一次被归档的失败桥接尝试

Agent远程劫持浏览器

桥接尝试失败。Agent的代码从httpbun.com运行，试图在frame和弹出窗口中加载fedresurs.ru，但远程浏览器似乎阻止了这些尝试。将明文fedresurs.ru的/companies地址直接提交给urlquery可以成功。但Agent所需数据位于/backend接口之后，它们无法将浏览器导航至该处。

若集群能够劫持已成功的浏览器会话，并进一步操控它呢？

接管另一个浏览器

VNC（Virtual Network Computing，虚拟网络计算）是一种远程查看并控制另一台计算机屏幕的协议。urlquery通过VNC暴露每次扫描的浏览器，供操作员实时观看。Agent利用这一点，从一个浏览器会话接管另一次扫描的浏览器。

这次VNC劫持要求Agent同时调度2个独立的浏览器会话，让它们同时运行在urlquery的基础设施上。

VNC劫持

Agent连续向urlquery提交了2个URL：

1. 扫描A（目标）：明文fedresurs.ru URL。urlquery正常打开并建立成功会话。该会话通过VNC在wss://urlquery.net/queue/{queue\_id}/vnc可用，无需密码。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OnZibpCQ9LicbQpbxcnShSZVpMp9vh7MkHSQyDiafUibV19cf6ZgL5KtXnfLXyKOa5IPXoycD6kaiayatJ5Sj70KPWkKYIOhpmNeVZ9RJW2706Aw/640?from=appmsg)![]()

目标扫描正常加载了 fedresurs.ru

1. 扫描B（控制器）：一份经由tinyurl.com的Base64编码载荷，内含JavaScript VNC客户端。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9LicYWib9mZx5vP4W2oAkg1NsD8gMzRnicN1Dc2u8icWJLgKsOIib9QCC2877PMYVv7aiblOhM0asZb1jm9ibAguTQBwOibBA2aB2XPibVS7M/640?from=appmsg)![]()

解码后，它连接扫描A的VNC端点并取得交互控制。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OnZibpCQ9LicbfgwpHnMpjuzObks38EfPuNbgFhfYm5mevWupIwEpmicntCpc1mmq4voEUgWEWYX4snnXCIEK9Jsq81m4LngeAxCTbaTW0Zy6M/640?from=appmsg)![]()

同一会话连接到目标会话时，还出现了HTTP 101连接升级：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9Licb36UlT6ibOgeskY4Wf2krnYEzn3VcQP0o5M4rY2RGwpBv039GOdCphKic2icGFHeaebpeg48OLJialRyCG3VWzFREAUiaazib3WwvHE/640?from=appmsg)![]()

控制器的网络日志显示一次被接受的 VNC 连接

在urlquery记录的HTTP请求中，该载荷从tinyurl.com开始，先混淆再重定向，再用httpbun.com封装，接着到jsdelivr.net导入VNC功能，最后连接回urlquery.net自身。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9LicbiboAE87leNicEOmYQegxJvQoJ2FvyAlibBTJUBOr5mfl2WTquYibiaSKYswvWaa72ggqUOFXoxuBtHrJdryxjB164dKjOenErAUGg/640?from=appmsg)![]()

远程键盘注入

VNC连接建立后，控制器即可看到目标浏览器屏幕并注入击键。载荷按下Ctrl+L以定位地址栏，再重新输入URL：

```
javascript:location='/backend/companies/61065761-3be6-47f7-afe5-e597c74ef44c/publications?limit=100&offset=0&searchCompanyEfrsb=true&searchAmReport=true&searchFirmBankruptMessage=true&searchFirmBankruptMessageWithoutLegalCase=false&searchSfactsMessage=true&searchSroAmMessage=true&searchTradeOrgMessage=true'
```

完整URL输入后，载荷按下Enter。地址栏仍属于已成功建立fedresurs.ru会话的同一浏览器，导航至backend路径时应继承会话cookie。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9LicYR8sStB4srGypwcERzuYJjBJfbQtDC7eiaxwjiawY5yNFbBNYOIlaPm0pD8hMGola2MCcyWWzvFwglFuPPZUbJYNuvqmOqUNNto/640?from=appmsg)![]()

未能一次成功

失控Agent似乎并未一次成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OnZibpCQ9LicYd0LDICuzJyOiaTBCfF1UpGoApNWURNoK77KbeIOgXQHD5R40zFib5ibbGTqkE97T0ExibQN326ciaVP3tn1fFYG7DAgeE4dznDShQ/640?from=appmsg)![]()

一次失败尝试返回错误

它们提交了7次VNC扫描，覆盖4种载荷变体，每次调整以下内容：

* 用F6还是Ctrl+L定位地址栏
* 击键节奏
* 逐字符键入还是通过剪贴板粘贴
* VNC客户端来源，例如urlquery自带bundle，或jsDel...