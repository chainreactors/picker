---
title: G.O.S.S.I.P 阅读推荐 2026-03-13 以（脆弱的）驱动之名
url: https://mp.weixin.qq.com/s/UEMUG2DC4TpdX8YZNlg2LA
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:04:53.373384
---

# G.O.S.S.I.P 阅读推荐 2026-03-13 以（脆弱的）驱动之名

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eQ0Wf6rqolVx5nblPdJ4QcjtXFaUXfzr50WVAWiba3ekj08JLiaK1zgqmicoSHfYwqYGR8uesia5kcgLohxndPbfJciaMSzOhkYS2GF4DOkqMOUE/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-03-13 以（脆弱的）驱动之名

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器中沉浸阅读

前几天（2026年3月2日）有个公众号发了个新闻，标题党得很，叫做《30天内挖掘100+内核漏洞：Windows驱动安全大危机？》，具体说的是什么呢？说的是有一个叫做Hexaplex AI的安全公司（这种命名风格最近非常多啊，挂着AI的名头），说他们构建了一个自主平台，从互联网各个角落抓取具有合法签名的Windows驱动程序，然后用AI去识别内存损坏漏洞，号称是对每个驱动的分析成本只有3美元，而结果是**从158个不同的驱动程序二进制文件中发现了521处潜在漏洞**，然后手动确认并向包括联想、富士通、IBM、英特尔、AMD、Silicom、英伟达和戴尔在内的供应商报告了15处漏洞。（不过只从富士通那边拿到了一个漏洞编号CVE-2025-65001）。

初读这篇文章，很多人肯定又是那个经典的先“哇塞”然后“x的，安全分析师又要完蛋了”的反应，不过我们如果把目光聚焦到几天之前召开的NDSS 2026会议上，那么在读完下面我们要介绍的这篇论文*Unveiling BYOVD Threats: Malware’s Use and Abuse of Kernel Drivers*之后，不知道你会作何感想？是不是让人想到了一种可能的商业模式：**让AI快速学习最新的学术论文的研究成果，然后在这个基础上编提出来一套更为“AI而宏大”的理论和结果，接下来就走入到融资的道路上**？算了，不能胡乱揣测，~~毕竟人家亚历山大王（Alexandr Wang）就是这种天才套路嘛~~，我们还是专注于介绍今天的内容吧！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolUtme7lIKIngoEy1fJo5uktCNziaXUR5fdbFLicM1d93netRDVh8he3EQkraeibq7yU3PwMiaP2PCDXMibLkiaJlSSiasn8NfJnEgu1I0/640?wx_fmt=png&from=appmsg)

前面其实已经把研究背景介绍得很清楚了：本文讨论的 Bring Your Own Vulnerable Driver (BYOVD) attacks 就是一种找到现有的合法驱动程序，在里面找到漏洞，然后拿这个有漏洞的驱动来当特洛伊木马（虽然这匹木马并不是自己想干坏事）的攻击方法。关于怎么实施具体的安全攻击，这里我们只能引用那段经典的废话——“*这种事情我见的多了，我只想说懂得都懂，不懂的我也不多说了，说了你也不明白，不如不说，细细品吧，你也别来问我怎么回事，这里面利益牵扯太大了，说了对你我都没有好处，你就当不知道就行了，其余的我只能说这里水很深，牵扯到很多东西，详细情况你们很难找到的，网上大部分都删干净了，所以我说懂得都懂，不懂也没办法*。” （或者你随便在网上搜索一下，例如 https://forum.butian.net/share/2832 这种文章也很多，哪有被删光的说法？）

打住打住，这部分大家还是去网上找教程或者看看论文的第二章去了解个大概吧，本文并不是教你搞黑产的，作者想要介绍的是对整个安全生态的调研：为了研究malware使用存在漏洞的驱动程序实施攻击的情况，作者首先开发了一套分析系统（如下图所示，是一个基于虚拟化的沙盒分析系统）来进行分析：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolWenaQYNwtgIdxTPPprowib4y0CHWT3TNUlR8EU2sUibvccaLW09oJUOm7mAkBGPeaOYnS3B1JVhLfiaT1XtIassloMiaxI0fxUHcM/640?wx_fmt=png&from=appmsg)

这套分析系统基于波兰安全研究人员开发的DRAKVUF Sandbox框架开发，DRAKVUF的好处是你甚至都不需要往guest OS里面写什么插桩代码，它直接就给你提供了Virtual Machine Introspection（VMI）功能，于是分析人员可以很轻松地记录driver loading and unloading routine执行、关键的内存管理API调用、IOCTL请求、kernel callback routine执行等关键事件，并把这些信息存储为特定的execution trace，供后续分析使用。

> https://github.com/CERT-Polska/drakvuf-sandbox

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolUvdI4EL3aDmLUumHUibdZYHUDjYS8X1cTibOenPRyBroibpKZwDDemyuKeI0aibGkUHG9lHIvhpqnu7uN63zicIdwtVYwUSr5Lan9Q/640?wx_fmt=png&from=appmsg)

为了区分什么是正常的驱动行为，什么是被攻击者利用然后干坏事的行为，作者列出了8条经验规则（论文的第IV.C章，这里不全部详述了），主要就是观察可疑的内存分配和关联的一些内核API的调用。而且，作者在论文的第IV.D章里面还介绍了一些可配置的execution trace记录方法，允许大家选择性地监控不同的行为。

作者还在论文的第五章介绍了关于怎么去寻找有问题的驱动，并且如何构建相关的数据集给后面的实验使用的过程，这里面提到了两个资源，第一个是一个由安全分析人员提交的，已经包含了1805个（且数量不断在增长）被人工确认有漏洞的驱动的集合，第二个则是微软自己维护的Microsoft Vulnerable Driver Blocklist：

[1] Living off the land drivers https://www.loldrivers.io/
[2] Microsoft recommended driver block rules https://learn.
microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/microsoft-recommended-driver-block-rules

除了这些已知有漏洞的驱动，作者还对Windows全体驱动进行了筛选，只要符合下表的标准（存在**可疑的导入表**，即abusable imports），都选进来作为candidate进行分析：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolW4Sf3IwGSsABTlfSDiaUG02q4IFNPFOKBU3GuHNI1icOFYNSEVVqoPvhxXw4qJrfxgAyA8eicoCdzBcIVJE3zwyKh4qpbbl6ricBw/640?wx_fmt=png&from=appmsg)

作者总共收集了8779个可执行文件样本，涉及到加载773个（可能）有问题的驱动，然后进行了大规模的分析实验，实验里面很自然地分为了两部分：对已知恶意程序的分析和对未知恶意攻击的分析。针对已知恶意程序的分析看起来不是那么乐观：针对2995个样本的分析（已经确认它们和162个有漏洞的驱动相关联）表明，仅有10%左右的样本（304个）的动态执行看起来是有问题的（suspicious），而差不多一半的样本（1524个）就没真正执行任何的驱动加载行为，作者分析了半天，指出这就是传统的病毒分析里面的大问题——恶意行为如何触发，不过我们也感谢作者在这里没有提任何AI或者小龙虾，本来以为作者要靠万能的AI来让病毒分析变得更简单呢~

对于其中56.25%的产生了相关驱动加载行为的样本，作者表示，尽管没监控到什么可疑的行为（因为作者的sandbox只能监控一些事件，而不是进行指令级别的trace），但是经过查阅了相关文献，以及对部分驱动行为进行了人工分析，发现它们可能就变成了CTF pwn题目了——调用代码利用驱动漏洞直接去进行内存操作。作者表示，日后会开发指令级别的记录工具（召唤QEMU？）来增强分析。

但是你也别嘲笑人家作者的方法不够小龙虾，即使只是基于下表的特征筛选，作者针对潜在可能有问题的驱动进行分析，就发现了很多可疑的样本。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolVf7TOIOqt9QRrIYiatcDh0U2OhxicGLMa2j8v2Dv2v6kxc4BxianeFUnYtTSLGX2RQbUVWeytV6NsHnNZCm9wuPdpHbhhemiaRdbI/640?wx_fmt=png&from=appmsg)

作者实打实地列出来了存在问题的驱动（如下表），并且在case studies章节里面具体讨论了这些驱动里面包含的高危操作，不过作者也没有很浮夸，只是说他们把这些驱动发给了微软和相关的厂商，然后只收到了一个CVE编号（CVE-2024-26506，针对`probmon.sys`）。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolU6JW3ia4O30Gib87F7ic3fmD5EckQyX5W1Xzx3KVUwmD9nSHSO0gqaxJnOBEDibDUcfElZjv5CBrdGwH0UqZCTBd3MLuwdxQBLpmY/640?wx_fmt=png&from=appmsg)

---

顺便提一嘴，大家有没有想过哪些驱动程序是容易被利用的漏洞大户？一开始你以为是硬件厂商，但是仔细想想还有什么更恶心的驱动？对，就是那些游戏厂商的**反作弊检查**代码，在2022年就有这么个例子：

*安全公司趋势科技的研究人员报告，《原神》的反作弊驱动 mhyprot2.sys 被勒索软件利用杀死杀毒软件的进程和服务。mhyprot2.sys 作为设备驱动是与《原神》游戏分开安装的，卸载《原神》并不会卸载 mhyprot2.sys，早在 2020 年 9 月米哈游发布 《原神》时游戏社区就开始讨论具有间谍软件能力的 mhyprot2.sys。它很快被发现存在漏洞允许被利用杀死进程。开发者神楽坂早苗/kagurazakasanae 和 Kento Oki 分别发布了 PoC 演示了杀死进程的能力。Kento Oki 向米哈游报告了漏洞，但该公司没有承认也没有修复。勒索软件利用的 mhyprot2.sys 是 2020 年 8 月构建的，其签名至今仍然有效没有撤销。*

上面的例子当然不是孤例，论文中列举了CAPCOM这个游戏巨头开发的`capcom.sys`反作弊驱动作为又一个反面教材（不过这个是2017年的旧闻了），说`capcom.sys`里面甚至学习eBPF搞了一个允许用户态发送代码过来给它执行的接口……实际上，就连V社都已经不能忍了：从2024年开始，Valve就强制要求游戏开发商在游戏介绍页面必须**披露是否使用了内核级反作弊技术**。

总之，驱动程序里面的问题确实很多，但是究竟是去关注那些基于AI智能体的安全分析~~营销~~文章，还是来学习这种传统的安全分析思路，这留给我们的读者自己去思考了（写这段话的目的其实是SEO，最近发现好像公众号文章里面不带AI和小龙虾，阅读量就一路下滑……此处重复**OpenClaw一万遍**）

---

> 论文：https://www.ndss-symposium.org/wp-content/uploads/2026-s1491-paper.pdf
> Open Science：https://doi.org/10.5281/zenodo.15864111

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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