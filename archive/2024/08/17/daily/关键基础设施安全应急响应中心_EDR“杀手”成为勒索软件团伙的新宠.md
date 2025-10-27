---
title: EDR“杀手”成为勒索软件团伙的新宠
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545390&idx=3&sn=b86feda1cd145b9a999b75fd7ec67a8e&chksm=c1e9be7ff69e37697e16be19eb78ceb4206e40ded968a9955ddc61c3becbc6252c4644441c78&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-08-17
fetch_date: 2025-10-06T18:06:20.456195
---

# EDR“杀手”成为勒索软件团伙的新宠

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogteoRCNR1McUWtMU4vbPRyibG7AsNPyI7KvIcp8Z5GPmIGetyMjnSibexXic4UVxOI6Cwn4EqnxYkPsw/0?wx_fmt=jpeg)

# EDR“杀手”成为勒索软件团伙的新宠

关键基础设施安全应急响应中心

RansomHub勒索软件团伙最近开始在攻击中使用一种新型恶意软件，名为“EDRKillShifter”，其设计目的是禁用终端检测与响应（EDR）安全软件，从而提高攻击成功率。这种恶意软件通过利用合法但易受攻击的驱动程序，实施“自带漏洞驱动程序”（BYOVD）的攻击技术，旨在绕过系统的安全防护措施。该恶意软件由Sophos的安全研究人员在2024年5月的一次勒索软件调查中发现。EDRKillShifter能够部署易受攻击的合法驱动程序，以提升权限，禁用安全解决方案，并接管目标系统。研究人员发现了两种不同版本的EDRKillShifter，均利用了在GitHub上公开的概念验证漏洞代码。其中一种版本利用了名为RentDrv2的易受攻击驱动程序，另一种则利用了ThreatFireMonitor驱动程序，这是一个已被弃用的系统监控软件的一部分。Sophos的研究显示，这种技术不仅被RansomHub使用，还被多个其他具有不同动机的威胁行为者，包括金融目的的勒索软件团伙和国家支持的黑客组织广泛采用。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icX1ZzT2mb9OFBibtmxlhvPx1IYKribzTWhhJ8lB2gh0mCJ0iak1W9vjZMyayD8qZFmvDxNqz1ic3XTmVA/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

EDRKillShifter的工作原理

EDRKillShifter 具是一个“加载器”可执行文件，这是一种合法驱动程序的交付机制，但容易受到滥用（也称为“自带易受攻击的驱动程序”或 BYOVD工具）。根据威胁行为者的要求，它可以交付各种不同的驱动程序有效载荷。

该加载程序的执行过程分为三个步骤。攻击者必须使用包含口令字符串的命令行执行 EDRKillShifter。当使用正确的口令运行时，可执行文件会解密名为BIN的嵌入资源并在内存中执行。

1、口令保护与初步加载：EDRKillShifter的执行需要提供一个64字符的唯一口令。如果口令错误，程序将无法运行。恶意软件伪装成游戏程序，通过伪装隐藏其真实意图。

2、内存加载与解密：正确口令提供后，恶意软件将加密的资源加载到内存，并使用VirtualAlloc分配新的内存页面进行解密。解密后的数据包括滥用的驱动程序和Go二进制文件。

3、自修改代码与最终载荷执行：在成功解密第二层有效载荷后，恶意软件通过自修改代码技术动态更改指令，并最终将有效载荷加载到内存中执行。这一步骤确保恶意活动的隐蔽性和复杂性。

值得注意的是，EDRKillShifter会创建一个新的驱动服务，并在启动后进入一个不断枚举运行进程的无限循环中，终止其硬编码列表中的目标进程。Sophos的研究人员怀疑，攻击者可能借用了部分概念验证代码，进行了修改，并将其移植到Go语言中，以增强恶意软件的灵活性和隐蔽性。

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icX1ZzT2mb9OFBibtmxlhvPx150qUwjzSLTeIpzkicJshGlOrnIOym3ibOd2IoicZIXjcXibZGuRbNPd2Sg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

最终有效载荷分析

研究人员对 EDRKillShifter 恶意软件的最终有效载荷进行了详细分析，发现所有样本均在内存中执行不同的变体，主要由 Go 语言编写并经过混淆处理。混淆技术通常用于阻碍逆向工程，保护知识产权，但在此案例中也用于掩盖恶意软件的真正意图和功能。关键发现包括：

混淆与隐藏：恶意软件使用混淆工具（如 gobfuscate）隐藏了关键数据，包括加密的字符串、Go版本信息以及包信息。这使得分析变得更加困难，但通过使用 Mandiant GoReSym工具，研究人员仍然能够提取出有价值的信息。

变体行为的一致性：所有分析的变体在 .data部分嵌入了一个易受攻击的驱动程序，行为一致。它们会将易受攻击的驱动程序放入 \AppData\Local\Temp 文件夹，创建服务、启动并加载驱动程序，然后进入一个无限循环，监控并终止硬编码目标列表中的进程。

利用易受攻击的驱动程序：研究发现两种主要变体分别利用了不同的易受攻击驱动程序：RentDrv2: 该驱动程序的概念验证代码可在 GitHub 上找到。该变体还支持额外的命令行参数（如“-list”）用于传递目标进程列表。ThreatFireMonitor: 属于已弃用的系统监控包的组件，其概念验证代码也可在 GitHub 上找到。该变体没有额外的命令行选项。

缓解措施及建议

研究人员认为，嵌入到加载程序中的最终有效载荷会因事件而异（并且可能因创建者而异）。如果我们尝试将 EDRKillShifter 映射到更大的威胁形势，加载程序和最终有效载荷也可能由不同的威胁行为者开发。

在暗网上销售加载器或混淆器是一项利润丰厚的业务。Sophos X-Ops怀疑加载器的唯一目的是部署最终的BYOVD有效载荷，并且它可能是在暗网上获得的。

种种迹象表明，旨在禁用受感染系统上的EDR系统的恶意软件的复杂程度有所提高。针对这种新型威胁，Sophos建议企业启用终端安全产品中的篡改保护功能，严格区分用户和管理员权限，防止攻击者加载漏洞驱动程序。此外，保持系统更新也至关重要，因为微软不断撤销已知被滥用驱动程序的签名，以减少此类攻击的风险。

2023年，Sophos还发现了另一个类似的EDR杀手恶意软件，名为AuKill，它在Medusa Locker和LockBit勒索软件攻击中利用了一个易受攻击的Process Explorer驱动程序。AuKill与一个名为Backstab的开源工具相似，后者也曾被LockBit团伙用于至少一次攻击。这些攻击事件表明，威胁行为者正不断改进和扩展他们的工具，以有效绕过现有的安全防护。

**参考资源：**

1.https://www.bleepingcomputer.com/news/security/ransomware-gang-deploys-new-malware-to-kill-security-software/

2.https://news.sophos.com/en-us/2024/08/14/edr-kill-shifter/

原文来源：网空闲话plus

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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