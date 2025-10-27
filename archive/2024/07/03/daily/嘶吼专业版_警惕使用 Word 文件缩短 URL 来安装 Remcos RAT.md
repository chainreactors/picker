---
title: 警惕使用 Word 文件缩短 URL 来安装 Remcos RAT
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247576024&idx=1&sn=59c27341f58b2c43cbecec4b4e475434&chksm=e91479e2de63f0f46a7e015d58f83fe799c9edb2cd96556c0620a8920409e73163960fb4058b&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-07-03
fetch_date: 2025-10-06T17:44:16.421496
---

# 警惕使用 Word 文件缩短 URL 来安装 Remcos RAT

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29vGv1DictBOrqFmJKjCrFrqkE2AX2tL84zuWmqK9x27zQNFkZvlnniaCF9oWOLyoIJazYvYz6h1VRA/0?wx_fmt=jpeg)

# 警惕使用 Word 文件缩短 URL 来安装 Remcos RAT

山卡拉

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29vGv1DictBOrqFmJKjCrFrqdN3y2Kg5of5KhHHPlQ7TRhgMtIHjN0yAm7Qv7dUhxMnKiaajN1jI72Q/640?wx_fmt=jpeg&from=appmsg)

近期，安全研究人员发现了一种分发 Remcos 远程访问木马 (RAT) 的新方法。这种恶意软件可以让攻击者完全控制受感染的系统，并通过包含缩短URL 的恶意 Word 文档进行传播。

这些URL会导致下载Remcos RAT，该木马可用于数据窃取、间谍活动以及其他恶意活动。理解感染链条并识别此类攻击的迹象对于减少这些威胁至关重要。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29vGv1DictBOrqFmJKjCrFrqu14GzFlIYgUw4vR1Rd40UqozraDdqnAnjDRlcefpTsuf3ehneXu3aA/640?wx_fmt=png&from=appmsg)感染链分析

这种攻击通常始于一封包含.docx附件的电子邮件，旨在欺骗接收者。在检查该文件时，发现其中包含一个缩短的URL，显示出恶意意图。该URL会重定向至下载以RTF格式存在的Equation Editor恶意软件的变种。

通过利用Equation Editor的漏洞（CVE-2017-11882），这种恶意软件试图下载一个由一长串连接的变量和字符串组成的VB脚本，可能经过编码或混淆处理。

这些字符串形成一个编码的有效负载，可以稍后在脚本中解码或执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29vGv1DictBOrqFmJKjCrFrq94a5GhFdqZJE4ZVw2zO9SdsFBosl2h51ZKoH5cS3hcBkLsiat4KRnkw/640?wx_fmt=png&from=appmsg)

该VB脚本解混淆后变成PowerShell代码，尝试通过隐写术图像和反向Base64编码的字符串下载恶意二进制文件。

尽管进行了一次命令与控制（C2）的调用，但也存在TCP重新连接，表明C2可能不可用。

被动DNS分析确认了C2域名，但它们目前处于停用状态。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29vGv1DictBOrqFmJKjCrFrqu14GzFlIYgUw4vR1Rd40UqozraDdqnAnjDRlcefpTsuf3ehneXu3aA/640?wx_fmt=png&from=appmsg)攻击细节

该文档（SHA1：f1d760423da2245150a931371af474dda519b6c9）包含两个关键文件：settings.xml.rels 和 document.xml.rels，位于 word/\_rels/。

Settings.xml.rels 文件显示了一个缩短的 URL，负责下载感染的下一阶段：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29vGv1DictBOrqFmJKjCrFrqibjNlR2gOwnzr0VhjdUCTjA9y5jjn5Cc4g6J0WhJxHoVHEdScrR18tw/640?wx_fmt=jpeg&from=appmsg)

在沙盒环境中运行该.docx文件发现它包含CVE-2017-0199漏洞。利用此漏洞后，该文档将尝试连接到远程服务器以下载恶意文件。

攻击者使用URL缩短服务来掩盖恶意URL，使受害者难以识别风险，并帮助绕过可能会标记可疑URL的安全过滤器。

PDF 文件看似无害，显示某公司与银行之间的交易。但真正的威胁在于通过缩短的URL 下载的 RTF 文件（SHA1：539deaf1e61fb54fb998c54ca5791d2d4b83b58c）。

该文件利用公式编辑器漏洞下载 VB 脚本（SHA1：9740c008e7e7eef31644ebddf99452a014fc87b4）。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29vGv1DictBOrqFmJKjCrFrqu14GzFlIYgUw4vR1Rd40UqozraDdqnAnjDRlcefpTsuf3ehneXu3aA/640?wx_fmt=png&from=appmsg)混淆和有效载荷投递

VB 脚本是一串连接变量和字符串的长字符串，可能是编码或混淆的数据。

重要变量“remercear”由反复连接各种字符串文字构成，表明它包含编码信息或命令。

去混淆后，PowerShell 代码尝试从两个不同的 URL 下载恶意二进制文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29vGv1DictBOrqFmJKjCrFrqbVtlfgXrJGmWRqfxoPGjxxciciaUwria1fFXiaVTm0vgOficaeia3vO9KqZQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29vGv1DictBOrqFmJKjCrFrqaX6Zh7ibicJFHbj68qEib7IHn8XJNpibby5QRoC8La3Mn67w7kELcPpbGg/640?wx_fmt=png&from=appmsg)

第一个 URL 使用隐写术将恶意软件隐藏在图像中：隐写图像

该图像包含一个长的Base64编码字符串，其中前六个字节解码为'MZ'，表明存在一个Windows可执行文件。

第二个 URL 与 IP 地址通信以检索包含反向 Base64 编码字符串的 TXT 文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29vGv1DictBOrqFmJKjCrFrqUfEl44OXlLZVicGGuEbW5QkK1SxeQKpXGsdMiapgS0aVmyedub13HrTQ/640?wx_fmt=png&from=appmsg)

这增加了一层混淆，从而逃避了简单的检测机制。

使用 Cyber Chef 等工具，对字符串进行反转，并对 Base64 进行解码以显示恶意负载（SHA1：83505673169efb06ab3b99d525ce51b126bd2009）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29vGv1DictBOrqFmJKjCrFrqN4ZiaS5QyZp9L6uiaVOpCjXs7Iibzn3NLfibOwFr3xfyM3GA1Hmr730HOA/640?wx_fmt=png&from=appmsg)

监控这些进程发现与潜在 C2 服务器（IP：94[.]156[.]66[.]67:2409）的连接目前已关闭，导致 TCP 重新连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29vGv1DictBOrqFmJKjCrFrqSQsNRSeSzcuhv4chu1fzEAMlKL2xXUh6fEO3qPOrqzVTvyVWADE4nA/640?wx_fmt=png&from=appmsg)

在Word文档中使用缩短URL来分发Remcos RAT突显了网络犯罪分子不断进化的策略。

通过理解感染链条并识别此类攻击的迹象，个人或企业组织可以更好地保护其免受这些威胁。所以，请始终谨慎处理未经请求的带附件的电子邮件，并避免点击来自未知来源的缩短URL。

参考及来源：https://gbhackers.com/beware-of-shorten-urls/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29vGv1DictBOrqFmJKjCrFrqref6yVwF4t0UC66wqWibUPibB79nbKIDiaXugAuaUuhUwY6dGM8Whahgg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29vGv1DictBOrqFmJKjCrFrq6MLZNnb5GoKt01MyNoEyshQ0SP3zu3YZJ9xoYF3zmRfVhofcZ8zgHw/640?wx_fmt=png&from=appmsg)

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