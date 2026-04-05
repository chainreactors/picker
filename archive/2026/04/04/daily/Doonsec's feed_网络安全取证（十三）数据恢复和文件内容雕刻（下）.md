---
title: 网络安全取证（十三）数据恢复和文件内容雕刻（下）
url: https://mp.weixin.qq.com/s/UyZrV_qgfbZWjjCoowDjqA
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:37:45.790608
---

# 网络安全取证（十三）数据恢复和文件内容雕刻（下）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sNicKB84ZxoGG4xJVDkxC0cAb5Q0rNAQHVnH9WprFzicKLf0fTIHFibwTsRznuWPA7psP8bOUm18MWnicxhId5tEXA/0?wx_fmt=jpeg)

# 网络安全取证（十三）数据恢复和文件内容雕刻（下）

祺印说信安

![]()

在小说阅读器中沉浸阅读

以下文章来源于河南等级保护测评
，作者铸盾安全

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6K0EVc7j5pWsAJ9u6w7rYeIAhXFEQq1xNsbnxs8DMtkQ/0)

**河南等级保护测评**
.

等级保护，不只是等级测评！一起探讨更全面的等级保护制度！ 做对用户有真实价值的网络安全服务，等级保护测评、风险评估、网络安全培训、网络安全咨询、网络安全合规。 传播网络安全知识，分享网络安全政策，共建风清气正的网络安全氛围。

|  |
| --- |
| **关注公众号****回复“****河南等保1028****”获取“****网络取证电子书****”****了解更多取证****知识** |

---

**[网络安全取证（一）定义和概念模型](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247487519&idx=1&sn=f3c847b218893d20f1f13f39c4fa4ec2&chksm=ce4636e8f931bffe889da4a5cd7cc68a3fca12f3a03c0646fc99436ba9bcbf69557124507a57&scene=21#wechat_redirect)**

**[网络安全取证（二）定义和概念模型之定义](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247487520&idx=1&sn=39e88d17d7b49791f4bc14309005c831&chksm=ce4636d7f931bfc1ba78e6fb95077b65881c46d23f234f8a3b5e0c04bb13d0f877bb4f166671&scene=21#wechat_redirect)**

**[网络安全取证（三）定义和概念模型之概念模型](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247487521&idx=1&sn=625c3034515ac5bf67c279a816c33bf4&chksm=ce4636d6f931bfc0cbb845d6e7ca7b812d940bea80250c1ec35658d393049b60254468aff8bf&scene=21#wechat_redirect)**

**[网络安全取证（四）定义和概念模型之概念模型](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247487525&idx=1&sn=fdca8d37bf1cd1d770906c2ce78a1a8a&chksm=ce4636d2f931bfc4f000fff4f3abe1c25e759e78c7f95f58b469688c0fa59e78051e1d0343ec&scene=21#wechat_redirect)**

**[网络安全取证（五）定义和概念模型之概念模型](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247487534&idx=1&sn=80ae33b71f6cad15dc6cbd597b2fe860&chksm=ce4636d9f931bfcf3491f9c5b8e454ece0e5c25f5855eabe25e6bf7d51ea6c2ade83773a55cc&scene=21#wechat_redirect)**

**[网络安全取证（六）定义和概念模型之取证流程](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247487535&idx=1&sn=b604839196d7a187774c1b0094aee3de&chksm=ce4636d8f931bfceaf2a922ce9890acaffde998697a30f7c18a7ffcc111f56affb87a3187f18&scene=21#wechat_redirect)**

**[网络安全取证（七）操作系统分析](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247487572&idx=1&sn=49be9fb89c3562a08ed399195a2ef131&chksm=ce4636a3f931bfb51f2e3ea5e80f382dce6f754393cef4d3febdb2d8652909978233ef564257&scene=21#wechat_redirect)**

**[网络安全取证（八）操作系统分析之存储取证](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247487574&idx=1&sn=3aec51871092c00d69112bd42335431f&chksm=ce4636a1f931bfb7233619ece6fd22318840760986b664f8a58ff9862820317d2809db4789eb&scene=21#wechat_redirect)**

**[网络安全取证（九）操作系统分析之文件系统分析](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247487576&idx=1&sn=a3f8f3f916b31e50268e697ef86e642f&chksm=ce4636aff931bfb90949fa1efea2634a27419ccb85592c8c13d38d1bd74205ac0bc51c5b2970&scene=21#wechat_redirect)**

**[网络安全取证（十）操作系统分析之存储取证](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247487577&idx=1&sn=8b681bb9ebea01ed90e123e5e9fb5dd0&chksm=ce4636aef931bfb88d73cfaf13eb88ff1c5be517d9a05cfc5d0aa1d7eb4ff05daac318fa2bae&scene=21#wechat_redirect)**

**[网络安全取证（十一）操作系统分析之块设备分析](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247487860&idx=2&sn=99ab4987ee3ab1cc1999e6f537b5ba76&chksm=ce463783f931be95772cb6bcfbac8ef0a23041ed0d049c89c9ef0dc3233bd3c9718f98ac54a6&scene=21#wechat_redirect)**

**[网络安全取证（十二）数据恢复和文件内容雕刻](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247487901&idx=1&sn=b2794ace0e62b29100334e24271073c1&chksm=ce46376af931be7cfdf8fe2c6afcdc72edf82c7393ddc41040dc6170960e3fb660aa5233a9cf&scene=21#wechat_redirect)**

##

**《网络安全知识体系》**

**网络安全取证（十三）**

**数据恢复和文件内容雕刻**

---

简介

数字取证科学或数字取证是应用科学工具和方法来识别，收集和分析数字（数据）工件，以支持法律诉讼。从技术角度来看，正是识别和重建相关事件序列的过程导致了目标IT的当前可观察状态。系统或（数字）伪影。随着信息技术的快速采用，数字证据的重要性与日新月异，导致数据以指数级的速度不断积累。同时，网络连接和IT系统的复杂性迅速增长，导致可能需要调查的更复杂的行为。

该知识区的主要目的是提供数字取证技术和功能的技术概述，并将其置于网络安全领域其他相关领域的更广泛视角。关于数字取证的法律方面的讨论仅限于一般原则和最佳实践，因为这些原则的应用的具体情况往往因司法管辖区而异。例如，知识区讨论了不同类型证据的可用性，但没有通过获取这些证据必须遵循的法律程序进行工作。法律&法规CyBOK知识领域讨论了与管辖权和获取，处理和提供数字证据的法律程序相关的具体问题。

![](https://mmbiz.qpic.cn/mmbiz_png/sNicKB84ZxoEBOJshicLq6qLbBiaw0mJMet6uK0vp7Lm1bvWPzc0MzjkhZ62WlBGUM2bSGhPicvR27XlOUEgRg4Rgg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

# 内容

# **2  操作系统分析**

**2.5 数据恢复和文件内容雕刻**

数据恢复工具的早期主要内容之一是“取消删除”功能，可以逆转用户删除数据的影响。最常见的情况是用户删除文件并需要撤消操作。在HDD上，这种逆转在删除后立即很容易实现-文件内容占用的存储只是被释放（标记为可用），但不会发生数据的实际破坏（清理）。

一个更困难的情况是已经使用了一段时间的HDD，并且 已经被 子格式化（例如，有人试图销毁证据）。通常使用的快速格式化命令具有覆盖与空文件系统相对应的一组数据结构的效果（完整格式会清理介质的内容，但可能需要数小时才能完成，因此使用频率较低）。因此，在查询这些结构后，正常的文件系统接口将报告没有文件。现实情况是，此时只有文件系统元数据被部分覆盖，并且表示文件内容的所有数据块仍然完整地存在于介质上。

与大多数其他类型的计算不同，取证计算对所有可恢复（部分）工件非常感兴趣，包括（有时特别是）已释放的工件。除非用户已采取特殊措施来安全擦除硬盘，否则在任何给定时间，介质都包含表面上已删除的可恢复应用程序项目（文件）。恢复文物的过程通常通过雕刻来完成。

![](https://mmbiz.qpic.cn/mmbiz_png/sNicKB84ZxoGG4xJVDkxC0cAb5Q0rNAQHWnmib6o9CH44Qibd0HFribhazM06bVtKYFr0bFygIoTncFIKbps5yKwUQ/640?wx_fmt=png)

文件雕刻是最古老和最常用的技术，其基本形式基于两个简单的观察：a）大多数文件格式具有特定的开始和结束标签（又名页眉和页脚）;b）文件系统强烈倾向于顺序布局以最大化吞吐量。

总之，这些产生了一个基本的恢复算法：1）顺序扫描捕获，直到找到已知的头；例如，JPEG图像总是以（十六进制）FF D8 FF报头开始；2）顺序扫描，直到找到对应的页脚；FF D9用于JPEG；3)复制中间的数据作为恢复的工件。图2说明了在文件雕刻过程中遇到的一些最常见的情况：

1. 无碎片是最典型的情况，因为现代文件系统需要额外的努力来确保顺序布局以获得最佳性能。

2. 嵌套内容通常是删除的结果；在本例中，在文件的初始顺序背靠背布局之后，文件B前面和后面的内容被删除并替换为A。在某些情况下，文件格式允许嵌套；例如，JPEG通常具有图像的缩略图版本，该版本也是JPEG格式。这种情况可以通过多次传递来解决——一旦B被切掉（并且其块从进一步考虑中移除），A的内容就变得连续，因此后续传递将很容易地提取它。

3. 双碎片文件被分割成两个相邻的部分，其中另一个内容位于两者之间，这也决定了重建的难度；如果中间的内容很容易与文件的内容（例如，压缩图像中间的文本片段）区分开来，那么问题就相对容易。否则，这是模棱两可的，很难识别匹配的部分。

4. 交错内容是嵌套的一个更复杂的版本，当使用较大的文件来填补由于删除较小的文件而产生的空白时，会发生这种情况。

这种简单的雕刻方法通常会产生大量可用的艺术品；然而，真实数据可能包含许多非典型模式，这可能导致大量重复和/或假阳性结果。一个主要原因是文件格式的设计没有考虑到雕刻，很少有健壮的内部元数据将组成部分连接在一起。有些甚至没有指定的页眉和/或页脚，这可能会导致大量误报，可能会产生比源数据大得多的结果。

松弛空间恢复。RAM和持久存储几乎总是以所选最小分配单元的倍数进行分配。因此，在分配空间的末尾，存在应用程序未使用但也不可用于其他用途的存储容量（空闲空间）。例如，如果最小分配是4KiB，并且一个文件需要14KiB，那么文件系统将分配四个4KiB块。应用程序将完全使用前三个块，但仅使用最后一个块的2KiB。这就有可能存储通过标准文件系统接口无法访问的数据，并且可以提供一种隐藏数据的简单方法。

一旦意识到在空闲空间中存储隐藏数据的潜力，就可以相对容易地识别和检查它，这是大多数调查中的标准步骤。

即将到来的挑战随着固态驱动器的容量不断增长，硬盘在操作数据存储中的比例越来越高，文件刻录的效用将随着时间的推移而降低。原因在于SSD块需要写入两次才能重用（第一次写入重置块的状态，从而启用其重用）。为了提高性能，将TRIM和UNMAP命令分别添加到ATA和SCSI命令集中；它们为文件系统提供了一种机制，以向存储设备指示哪些块需要被垃圾收集并准备好重用。

King&Vidas[31]通过实验证明，文件雕刻只能在现代固态硬盘（SSD）上的一组狭小环境下工作。具体来说，他们表明，对于一个支持TRIM的操作系统，如Windows 7和更高版本，其测试中的数据恢复率几乎普遍为零。相反，使用预TRIM操作系统（Windows XP）可以在相同的实验条件下实现近乎完美的恢复率。

|  |
| --- |
| [渗透测试过程中所需工具](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&amp;mid=2247487886&amp;idx=1&amp;sn=8ea236c4e70d8f3ac3aa273354a302e9&amp;chksm=ce463779f931be6fd06ad78ef70ba22aca024236b6a7e20ab570f490e8fe8189ef38e9a963e6&scene=21#wechat_redirect) |
| [渗透测试：信息安全测试和评估技术指南NIST   SP 800-115](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&amp;mid=2247487885&amp;idx=1&amp;sn=80c3eea6f9ce858e9ecdc1b6042cbf6f&amp;chksm=ce46377af931be6cc023b2b4f63949169062129236452b5901b125db8bca82ae214ff03033f5&scene=21#wechat_redirect) |
| [苹果发布iOS   16.1 和 iPadOS 16](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&amp;mid=2247487884&amp;idx=1&amp;sn=74a01a8a9d7ff3f0b06fac8672790b56&amp;chksm=ce46377bf931be6d461014fabdaa5103e622f68979f00f197ee39c23fba7f677da0ac5ddf4cd&scene=21#wechat_redirect) |
| [法国对人脸识别公司Clearview   AI处以罚款](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&amp;mid=2247487879&amp;idx=2&amp;sn=667d6a8457eacfff0a4f817a00fe240f&amp;chksm=ce463770f931be66c93ee73f7dbb06701f7ad5a3e4b381b6eb7d93fdb75bcc70ccdecf7556a6&scene=21#wechat_redirect) |
| [Offensive Security渗透测试报告模板](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&amp;mid=2247487879&amp;idx=1&amp;sn=b4f7122633612dadedbdd15e05cac461&amp;chksm=ce463770f931be666d7723f868ee42c6808e9c3f894cf254effdcc3434d7575b587b010d2d7f&scene=21#wechat_redirect) |
| [法国对人脸识别公司Clearview   AI处以罚款](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&amp;mid=2247487870&amp;idx=2&amp;sn=3314943e10cf9342279c39b6dab07790&amp;chksm=ce463789f931be9f025ec89e67e156bbd27b48b76233cc14fb7c795c981a2a5beaa82e7e3fa7&scene=21#wechat_redirect) |
| [密码报告：蜜罐数据显示针对 RDP、SSH 的 Bot 攻击趋势](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&amp;mid=2247487870&amp;idx=1&amp;sn=6553f3beaccdeeadd4580f769d50744d&amp;chksm=ce463789f931be9f87b9c98a1fca0b47643ddf937c395fb4e1efeaf9b27672f9e2d69adf8719&scene=21#wechat_redirect) |
| [网络安全取证（十一）操作系统分析之块设备分析](http://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==...