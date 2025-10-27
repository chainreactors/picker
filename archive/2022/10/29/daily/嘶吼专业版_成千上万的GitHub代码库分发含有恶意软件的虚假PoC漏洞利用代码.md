---
title: 成千上万的GitHub代码库分发含有恶意软件的虚假PoC漏洞利用代码
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247552901&idx=1&sn=6b508f55415007ada6193d9eaf7aa281&chksm=e915dfbfde6256a94aca316a2fe2d2ef07dacd7ab5e3b70f879889e99d897941e353af87c316&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-10-29
fetch_date: 2025-10-03T21:14:40.747047
---

# 成千上万的GitHub代码库分发含有恶意软件的虚假PoC漏洞利用代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KiciboMeXVQibgvsu7ArtVjBFdxHfQ5YsSfOCsD0xgwZ6r5RK4Lh9L8hwmUg/0?wx_fmt=jpeg)

# 成千上万的GitHub代码库分发含有恶意软件的虚假PoC漏洞利用代码

布加迪

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

莱顿高级计算机科学研究所的研究人员近日在GitHub上发现了成千上万个代码库提供针对多个漏洞的虚假概念证明（PoC）漏洞利用代码（exploit），其中一些含有恶意软件。

GitHub是全球最大的代码托管平台之一，众多研究人员使用它发布PoC漏洞利用代码，以帮助安全行业验证漏洞修复程序，或者确定漏洞的影响和范围。

据莱顿高级计算机科学研究所的研究人员撰写的技术文章显示，感染上恶意软件而不是获得PoC的可能性也许高达10.3%，这不包括已证实的虚假漏洞利用代码和恶作剧软件。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicib6DyQ1QV3hpRiaFgA0shvw6MogPOoia8YuloMMD6LblrLz5yCbFWLSibicQ/640?wx_fmt=png)数据收集和分析

研究人员使用以下三种机制分析了47300多个代码库，这些代码库发布了针对2017年至2021年期间披露的一个漏洞的漏洞利用代码：

IP地址分析：将PoC的发布者IP与公共黑名单、VT和AbuseIPDB进行比对。

二进制文件分析：对提供的可执行程序及其散列运行VirusTotal检查。

十六进制文件和Base64分析：在执行二进制文件和IP检查之前解码经过混淆处理的文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibDpY1Ocbrj2IDGZuicdkiaGZKPiaVHwS1GoEcZAqkSvKyicbEicbRuqPXVUg/640?wx_fmt=png)

图1. 数据分析方法（来源：Arxiv.org）

在提取的150734个独特IP中，有2864个IP与黑名单条目匹配，在Virus Total上的反病毒扫描中检测到1522个IP是恶意IP，其中1069个IP存在于AbuseeIPDB数据库中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibmR0IA7Jh1fjMLLzPmAFMKicesUWsicTYVtqW3BdRHmFONucsJHHpnyBw/640?wx_fmt=png)

图2. 各个黑名单上找到的IP地址（来源：Arxiv.org）

二进制文件分析检查了一组6160个可执行程序，显示总共2164个恶意样本驻留在1398个代码库中。

在测试的47313个代码库中，共有4893个代码库被认为是恶意的，其中大多数涉及来自2020年的漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibGOFh5ACA7HXictOK1rl8Kn9MoE8P4uGcMSFLicj9zwMBD0Sbrs3DN8CA/640?wx_fmt=png)

图3. 每年的恶意代码库（来源：Arxiv.org）

这份报告中包含的一小组代码库含有分发恶意软件的虚假PoC。然而，研究人员向BleepingComputer表明了至少另外60个代码库依然存在，目前正在被GitHub撤下的过程中。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicib6DyQ1QV3hpRiaFgA0shvw6MogPOoia8YuloMMD6LblrLz5yCbFWLSibicQ/640?wx_fmt=png)PoC中的恶意软件

通过进一步研究其中一些代码库，研究人员发现了大量不同的恶意软件和有害脚本，从远程访问木马到Cobalt Strike，不一而足。

一个值得关注的例子是CVE-2019-0708（通常名为“BlueKeep”）的PoC，它含有一个用base64模糊处理的Python脚本，该脚本可以从Pastebin获取VBScript。

该脚本其实是Houdini RAT，这个基于JavaScript的旧木马支持通过Windows CMD远程执行命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibZjvia0EtL1SoDlp0eGWFVfOO3f4ssC7Aib0nCoHtWzZ3bZNLciclXDjhQ/640?wx_fmt=png)

图4. 模糊处理的脚本和去模糊处理的Houdini

在另一种情况下，研究人员发现了一个虚假的PoC，这其实是信息窃取工具，收集系统信息、IP地址和用户代理。

这是另一名研究人员之前进行的一个安全实验，所以研究人员用自动化工具发现它，以确认他们的方法是有效的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kiciba7MtQFewsZBic1WgWdeVibdRCHYrBr6nd0jjJPY5IkcNVFTULGTwvBXg/640?wx_fmt=png)

图5. 虚假PoC泄密示例（来源：Arxiv.org）

其中一名研究人员El Yadmani Soufian还是Darktrac的安全研究人员，他好心地为BleepingComputer提供了技术报告中未包含的其他示例，如下所示:

含有用base64编码的二进制代码的PowerShell PoC在Virus Total中被标记为是恶意的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibgN6Z1iaYzSrguqmQAmibvUzg8ibjcBxgJc81S8vW1KXrDn4c3Z8bR90iag/640?wx_fmt=png)

图6. 虚假PowerShell PoC

Python PoC含有一行代码，用于解码用base64编码的攻击载荷，该攻击载荷在Virus Total上被标记为是恶意的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibPaI4YnXsmaS0QtBNUXv8D7WpIwJXSWevcQVlTJCGSib412WcV2yrxzQ/640?wx_fmt=png)

图7. 恶意的一行代码攻击载荷冒充PoC

虚假的BlueKeep漏洞利用代码含有一个可执行程序，该程序被大多数反病毒引擎标记为是恶意的，并被识别为是Cobalt Strike。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibyMdR71DglpT98z7qoUIHTdzZwnjibg3maMxZjNGN0Z7ux6whPLr47xw/640?wx_fmt=png)

图8. Cobalt Strike通过虚假PoC来投放

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicib9kYhSc1XsAFV5Jw9edtyvy46OiazMqx7zAXT4CXMeoo1fQicgMwic7mxg/640?wx_fmt=png)

图9. 无害但虚假的PoC

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9Kicib6DyQ1QV3hpRiaFgA0shvw6MogPOoia8YuloMMD6LblrLz5yCbFWLSibicQ/640?wx_fmt=png)如何保持安全？

盲目信任GitHub上来源未经验证的代码库是个坏主意，因为内容没有经过审核，所以用户在使用之前需要审核它。

建议软件测试人员仔细检查他们下载的PoC，并在执行它们之前运行尽可能多的检查。

Soufian认为，所有测试人员都应该遵循以下三个步骤：

1. 仔细阅读将要在贵公司的网络或客户的网络上运行的代码。

2. 如果代码太过模糊，需要大量的时间来手动分析，不妨将它放在沙盒环境（比如隔离的虚拟机）中，检查网络中的任何可疑流量。

3. 使用像VirusTotal这样的开源情报工具来分析二进制文件。

研究人员已经向GitHub报告了他们发现的所有恶意代码库，但需要一段时间才能审查和删除所有恶意代码库，因此仍有许多恶意代码库对公众开放。

正如Soufian所解释，他们的研究目的不仅仅是作为GitHub上的一次性清理行动，而是以此为契机，开发一种自动解决方案，可以用来标记上传代码中的恶意指令。

这是该团队研究的第一个版本，他们正在努力改进其探测工具。目前，这款检测工具遗漏了迷惑性较强的代码。

参考及来源：https://www.bleepingcomputer.com/news/security/thousands-of-github-repositories-deliver-fake-poc-exploits-with-malware/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibhuaKy6A3WHLicJOfiaaRPH2vemibJNmia9zCAkqwmpoxOQibk7qZTibpbqDw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icBzpZvEeWqs0ZuRQrm9KicibTnS3BkPFicuiafxVd2ud5NdtMbNibicjqaPwuH2YQkRtveM7qKELdVqwpw/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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