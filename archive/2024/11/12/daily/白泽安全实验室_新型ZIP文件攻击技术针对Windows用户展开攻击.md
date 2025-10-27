---
title: 新型ZIP文件攻击技术针对Windows用户展开攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492407&idx=1&sn=46d269f120a792b4ef554869afc0c33e&chksm=e90dc91dde7a400b43625d99685bf291d7852b6ceb5716dace85d1bd1778b07f7385e86903e8&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-11-12
fetch_date: 2025-10-06T19:21:28.510890
---

# 新型ZIP文件攻击技术针对Windows用户展开攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 新型ZIP文件攻击技术针对Windows用户展开攻击

BaizeSec

白泽安全实验室

近日， Perception Point安全研究人员发现了一种新型的恶意软件攻击技术，该技术通过ZIP文件的串联来隐藏恶意攻击载荷，从而绕过常见的安全检测工具。这种攻击手段利用了不同ZIP阅读器和归档管理器处理串联ZIP文件的差异，使得特定工具的用户成为攻击目标。ZIP文件格式因其在压缩和捆绑多个文件方面的便捷性而被广泛使用。然而，其结构的灵活性也使其成为逃避恶意软件交付的有吸引力的载体。攻击者利用ZIP文件结构的灵活性，通过串联技术将多个ZIP归档附加到一个文件中，从而隐藏恶意内容。

**ZIP文件由几个关键部分组成：**

* **文件条目（File Entries）：**这些是ZIP内部压缩的文件或文件夹。每个条目包括文件名、大小和修改日期等元数据。
* **中央目录（Central Directory）：**作为整个归档的索引，位于ZIP文件的末尾。它列出了所有文件条目及其在归档中的偏移量，允许ZIP阅读器快速定位和提取文件，而无需顺序扫描整个ZIP文件。这种设计提高了性能，使得对归档的更改更加容易。
* **EOCD（End of Central Directory）：**这个记录标志着中央目录的结束，并包含重要的元数据，例如文件条目的总数和中央目录的起始位置。ZIP阅读器依赖这部分来确定中央目录的开始位置。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIMhNleEibzc8ic8icB6bXwwunbdrBsiaBOVLegL2n3879FpcZRR6UDzhp42vuvmVWObUgibEsOQj5QJAHw/640?wx_fmt=png&from=appmsg)图 1 ZIP文件结构

攻击者利用这些结构组件，通过串联技术来绕过安全检查。串联涉及将多个ZIP归档附加到一个文件中，尽管这个组合文件可能看起来像一个归档，但实际上它包含多个中央目录，每个目录指向不同的文件条目集合。这种处理串联ZIP文件的差异使得攻击者能够通过在某些ZIP阅读器无法或不访问的归档部分隐藏恶意有效载荷来绕过检测工具。

**攻击过程详细分析**

**1.创建文件：**攻击者首先创建两个文本文件，一个包含无害的内容，另一个包含恶意内容。

**2.压缩文件：**使用7zip工具，攻击者将这两个文件分别压缩成两个独立的ZIP文件，例如pt1.zip和pt2.zip。

**3.串联ZIP文件：**攻击者将这两个ZIP文件串联成一个文件，例如combined.zip。在这个过程中，第二个ZIP文件的中央目录将覆盖第一个，导致某些ZIP阅读器只能看到第二个归档中的内容。

**4.伪装文件：**攻击者将串联的ZIP文件的扩展名改为.rar，伪装成RAR文件，以增加其通过初步安全检测的可能性。

**5.发送恶意邮件：**攻击者通过电子邮件发送这个伪装的RAR文件，邮件内容伪装成正常文档，例如：来自运输公司的紧急文件，诱使收件人打开附件。

**6.利用ZIP阅读器差异：**不同的ZIP阅读器处理串联ZIP文件的方式不同。例如，7zip可能只显示第一个归档的内容，而WinRAR和Windows文件资源管理器可能显示第二个归档的内容，从而发现隐藏的恶意软件。

**7.执行恶意软件：**如果收件人使用WinRAR或Windows文件资源管理器打开附件，他们可能会无意中执行隐藏在第二个归档中的恶意软件，这是一种Trojan恶意软件，能够自动执行一系列恶意活动，如下载和执行额外的有效载荷。

通过这种精心设计的攻击，攻击者能够针对使用特定ZIP阅读器的用户，同时绕过依赖于文件扩展名进行初步评估的基本检测机制。在最近一次攻击中，研究人员发现攻击者通过电子邮件发送了一个伪装成合法运输文件的Trojan恶意软件。该恶意软件以串联ZIP文件的形式作为电子邮件附件，旨在绕过大多数标准ZIP阅读器的检测，同时针对Windows和WinRAR用户。安全研究人员随后联系了7zip开发人员，希望以解决串联ZIP文件的特定行为。但是开发人员回复确认这不是一个错误，而是有意为之的功能，这意味着这种行为不太可能改变，为攻击者继续利用这一漏洞留下了空间。

参考链接：

https://perception-point.io/blog/evasive-concatenated-zip-trojan-targets-windows-users/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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