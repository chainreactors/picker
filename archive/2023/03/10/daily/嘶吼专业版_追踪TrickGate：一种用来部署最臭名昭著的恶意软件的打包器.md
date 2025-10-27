---
title: 追踪TrickGate：一种用来部署最臭名昭著的恶意软件的打包器
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247558465&idx=3&sn=35f638e96ec6cce9eb3695e1e57dc87c&chksm=e914357bde63bc6d03b0d4c282ee6215b680a8051fc99e2d7e03321831233f7f67b61669d117&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-03-10
fetch_date: 2025-10-04T09:09:34.523169
---

# 追踪TrickGate：一种用来部署最臭名昭著的恶意软件的打包器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2ZrUPoF9ibTlIw8DWOvL8P1ndEA6qfzlL63KdHnymiaAcOtrPNfCgEwyGAA/0?wx_fmt=jpeg)

# 追踪TrickGate：一种用来部署最臭名昭著的恶意软件的打包器

布加迪

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

TrickGate最初于2016年7月被发现，这种基于外壳代码（shellcode）的打包器（packer）作为一项服务来提供，用于隐藏恶意软件以免被端点检测和响应（EDR）以及杀毒软件发现。

在过去六年间，TrickGate 被用来部署最臭名昭著的恶意软件，比如Cerber、Trickbot、Maze、Emotet、REvil、Cobalt Strike、AZORult、Formbook和AgentTesla 等。

由于定期会改头换面，TrickGate多年来一直没有被人注意。这个特征导致研究界通过众多属性和名称来识别其身份。

虽然该打包器的包装程序会不断变化，但TrickGate外壳代码中的主要构建模块至今仍在使用中。

Check Point 的威胁模拟（Threat Emulation）解决方案成功检测并阻止了TrickGate打包器。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zrh7BMiaV3N1P4dS1vIbdbbia0Cm2vln7tdpJbOXNBe28WpeWuI5sDQwcg/640?wx_fmt=png)介绍

网络犯罪分子日益依赖打包器来执行恶意活动。该打包器在黑客论坛上又叫Crypter（加密器）和FUD，使杀毒软件更难检测到恶意代码。通过使用打包器，恶意分子可以更轻松地传播恶意软件，而影响更小。商业打包器即服务的主要特征之一是，它不关心攻击载荷是什么，这意味着它可以用来打包许多不同的恶意样本。该打包器的另一个重要特征是它能改头换面——该打包器的包装程序会定期改变，因此不被安全产品发现。

TrickGate是一种典型的功能强大且有弹性的打包器即服务，多年来没有被网络安全产品所发现，并以不同的方式不断改进自己。我们设法追查到了TrickGate的下落，尽管它会迅速改变外层的包装程序。

TrickGate堪称伪装高手，因不同的属性而被赋予了许多名称。名称包括TrickGate、Emotet的打包器、新的加载器、Loncom和基于NSIS的加密器等。我们联系了之前的研究成果，基本上确定这起活动似乎是作为一项服务来提供的。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zrh7BMiaV3N1P4dS1vIbdbbia0Cm2vln7tdpJbOXNBe28WpeWuI5sDQwcg/640?wx_fmt=png)TrickGate历年来的活动

我们首次观察到TrickGate是在2016年底。当时，它被用来传播Cerber勒索软件。从那时起，我们一直在观察TrickGate，发现它被用来传播所有类型的恶意软件工具，比如勒索软件、RAT、信息窃取器、银行木马和挖币软件。我们注意到，许多高级持续性威胁（APT）组织和威胁分子经常使用TrickGate来包装恶意代码，以免被安全产品检测出来。TrickGate参与了包装一些最臭名昭著的恶意软件家族的活动，比如Cerber、Trickbot、Maze、Emotet、REvil、CoinMiner、Cobalt  Strike、DarkVNC、BuerLoader、HawkEye、NetWire、AZORult、Formbook、Remcos、Lokibot和AgentTesla等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2ZrtsOfNHy0xNjq5MGfCjqohquxFPwYrZicLIr7lAzYiaWBGnUxqM6V7hnA/640?wx_fmt=png)

图1. TrickGate历年来的活动

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zrh7BMiaV3N1P4dS1vIbdbbia0Cm2vln7tdpJbOXNBe28WpeWuI5sDQwcg/640?wx_fmt=png)TrickGate的分布

在过去两年里，我们每周监测到40次到650次攻击。据我们的遥测数据显示，使用TrickGate的威胁分子主要攻击制造业，但也攻击教育设施、医疗保健、金融和商业企业。这些攻击遍布全球各地，越来越集中在中国台湾和土耳其。近两个月使用TrickGate的最盛行的恶意软件家族是Formbook，占跟踪分布总量的42%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zrw9zicU601lVSWOYXKhmVSZgtlr1DC7libHmvHH8iaafA3DH29KqNQpiaRA/640?wx_fmt=png)

图2. 2022年10月至11月期间的TrickGate统计数据

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zrh7BMiaV3N1P4dS1vIbdbbia0Cm2vln7tdpJbOXNBe28WpeWuI5sDQwcg/640?wx_fmt=png)攻击流程

下面概述了涉及TrickGate的攻击中常见的攻击流程。

**初始访问**

打包器用户进行的初始访问可能会有很大差异。我们监测的打包样本主要通过带有恶意附件的网络钓鱼电子邮件来传播，但也通过恶意链接来传播。

**初始文件**

第一阶段主要以压缩可执行文件的形式出现，但我们监测后发现了导致相同外壳代码的许多文件类型和传播手段。我们在第一阶段观察到以下文件类型：

压缩文件：7Z、ACE、ARJ、BZ、BZ2、CAB、GZ、IMG、ISO、IZH、LHA、LZ、LZH、R00、RAR、TAR、TGZ、UU、 UUE、XZ、Z、ZIP、ZIPX、ZST。

可执行文件：BAT、CMD、COM、EXE、LNK、PIF、SCR。

文档：DOC、DOCX、PDF、XLL、XLS、XLSX、RTF。

**外壳代码加载器**

第二阶段是外壳代码加载器，它负责解密和运行外壳代码。

我们注意到三种不同类型的代码语言用于外壳代码加载器。NSIS脚本、AutoIT脚本和C都实现了类似的功能。

**外壳代码**

外壳代码是打包器的核心。它负责解密攻击载荷，并将载荷悄悄注入到新进程中。

**攻击载荷**

攻击载荷是实际的恶意代码，负责执行预期的恶意活动。攻击载荷因使用打包器的威胁分子而异。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2ZrAqdnNtUMGSsontXnd4pyNeynScPcAI47FQhQibibt8rV1ibqoibY6WqbicQ/640?wx_fmt=png)

图3. 攻击流程

我们在过去一年观察到的不同攻击流程的示例：

2022年2月24日

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zr8tWkl4lMOA8IyeloTSgFtZytibv3xK0tQTQEJicV85gG3jtZzR3LnYYg/640?wx_fmt=png)

图4. LNK攻击流程

RAR：3f5758da2f4469810958714faed747b2309142ae

LNK：bba7c7e6b4cb113b8f8652d67ce3592901b18a74

URL：jardinaix[.]fr/w.exe

EXE：63205c7b5c84296478f1ad7d335aa06b8b7da536

2022年3月10日

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2ZrYc7XQuFrWBqY4iaLUmhF3GXF7N17wpyr3jKHL4H7RtXZ9dk8Micgkzag/640?wx_fmt=png)

图5. PDF攻击流程

PDF：08a9cf364796b483327fb76335f166fe4bf7c581

XLSX：36b7140f0b5673d03c059a35c10e96e0ef3d429a

URL：192.227.196[.]211/t.wirr/XLD.exe

EXE：386e4686dd27b82e4cabca7a099fef08b000de81

2022年10月3日

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zrr9IWUJibJt5A05YA7DEbumzUMaJzuJzUCNibOkPBrLd3djEzejDGxbvA/640?wx_fmt=png)

图6. SFX攻击流程

7Z：fac7a9d4c7d74eea7ed87d2ac5fedad08cf1d50a

EXE：3437ea9b7592a4a05077028d54ef8ad194b45d2f

2022年11月15日

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zrp6tnalDE114hFBwI6Hj6VdONVQiaiaAhnKhfM78rMWHVm9a0RGPJab3A/640?wx_fmt=png)

图7. AutoIT攻击流程

R11：755ee43ae80421c80abfab5481d44615784e76da

EXE：666c5b23521c1491adeeee26716a1794b09080ec

**外壳代码加载器**

外壳代码加载器通常含有一个函数，负责解密外壳代码并将其加载到内存中。以下是基本步骤：

1. 读取经过加密的外壳代码。经过加密的外壳代码可以存储在光盘上的文件中、“.rdata”部分或存储成资源。

2. 为外壳代码分配内存，常通过调用VirtualAlloc来分配。

3. 解密外壳代码。

4. 触发外壳代码。正如我们在下面解释的那样，这可以通过使用直接调用或回调函数来完成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zr6RNeJIk0DD1ccQcrPIC8ib8Kr0n1Mzv7TC5EqIYAictS9ptCxic7Za5fw/640?wx_fmt=png)

图8. 外壳代码加载器——去混淆处理的AutoIT版本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zr3mwc7QOqKJQb3rvicjic4jYvsv8UwYianSmOkE9zHYOArhv2LHzAlI2Qg/640?wx_fmt=png)

图9. 外壳代码加载器C版本

在较新版本的TrickGate中，外壳代码加载器滥用“回调函数”机制。加载器利用许多原生API调用，这些调用将内存地址作为回调函数的参数。加载器传递的不是回调函数，而是新分配的内存（内有外壳代码）的地址。当Windows到达注册事件点时，DriverCallback 执行外壳代码。这种技术通过让Windows操作系统在未知时间运行外壳代码来中断我们所监测的行为流。在上面的外壳代码加载器中，您可以在上面底部一行标有“EnumTimeFormatsA”和“EnumSystemCodePagesW”的配图中看到这两个示例。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zrh7BMiaV3N1P4dS1vIbdbbia0Cm2vln7tdpJbOXNBe28WpeWuI5sDQwcg/640?wx_fmt=png)外壳代码相似性和TrickGate暂停

当我们发现不相关的恶意软件家族在代码上存在相似性时，威胁分子通常更有可能从共享资源复制或共享某些片段的代码。我们在很长一段时间内注意到一种独特的注入技术，它结合使用直接内核系统调用的方法，但我们没有意识到其重要性，以为它可能是共享代码的片段。    我们在攻击活动中看到了偶尔的“暂停”，这使我们怀疑这种独特的注入技术可能完全由一个威胁团伙控制，毕竟几个不同的团伙同时偃旗息鼓的可能性很小。最近一次暂停长达3个多月（从2022年6月13日到2022年9月26日），这让我们有机会证实自己的猜疑，并深入研究外壳代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zric3ykRlvt67WovXxGJvyWMRAZxztPibsrz5KzDpZNeTqD63YmMnfzUlQ/640?wx_fmt=png)

图10. 过去两年的TrickGate

为了验证猜疑，我们开始分析不同时间段的样本。

我们通过将新样本与旧样本进行比较来开始分析。针对这一测试，我们使用2022-12\_Remcos:a1f73365b88872de170e69ed2150c6df7adcdc9c与2017-10\_CoinMiner：1a455baf4ce680d74af964ea6f5253bbeeacb3de作了比较。

我们分析行为后知道了外壳代码存在相似性，于是运行样本，直到外壳代码在内存中被解密，然后我们将外壳代码转储到磁盘上。接下来，我们使用归谷歌所有的Zynamics BinDiff工具，以检查两个外壳代码的相似性。结果显示，测试的外壳代码存在50%的相似性。没料到在很长一段时间内（超过五年）对于相当大的外壳代码（~5kb）而言存在50%的相似性。这自然让人怀疑这可能是由人维护的外壳代码，但我们需要进一步的证据表明在较短的时间内存在相似性，看看它是否逐渐变化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2ZrJCGlTKQTlwmT8gKXDz3F4f2LBGup2a89ppu4KmUOLudAibFsDnPuBSw/640?wx_fmt=png)

图11. 从2022-12\_Remcos：a1f73365b88872de170e69ed2150c6df7adcdc9c和  2017-10\_CoinMiner：1a455baf4ce680d74af964ea6f5253bbeeacb3de提取的外壳代码的BinDiff结果比较

为了进一步分析，我们抽取了过去六年的随机样本。针对每个样本，我们转储了外壳代码，并检查一段时间内结果的相似性。正如你在下图中所看到，结果表明逐渐出现的变化很小。在左侧，我们看到从2016年到2020年的样本显示存在大约90%的相似性。在右侧，我们看到分叉版本本身存在很高的相似性，但左侧原始版本的相似性较低。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2ZrCKQyXRCGsEcStWicNLTz0BLPoiaGMl0ughUibfXXy6JXWSJ21tlrt33icA/640?wx_fmt=png)

图12. 提取的外壳代码的Bindiff结果

然后我们深入研究外壳代码之间的差异，看看以下方面带来的影响：

不同的编译器

混淆

规避模块

持久性模块（在下次登录时运行载荷）

函数顺序

局部变量和结构

我们随后得到了打包器的核心功能。编写者不断维护外壳代码，但使用下一节中描述的“构建模块”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zr5Rr2UuFyEYwWWIMl1863ttxyiazTkSjJrQFpFZibFRykwibe3ospv2pbg/640?wx_fmt=png)

图13. 控制流程图—关于主注入函数。比较2016-07\_  Cerber：24aa45280c7821e0c9e404f6ce846f1ce00b9823与 2022-12\_Remcos：a1f73365b88872de170e69ed2150c6df7adcdc9c的差异

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2ZrexGokh6XF9ibiapRmJ15YvNBz6je7CuClagOrjcGCRlgZnPWnmm34c4w/640?wx_fmt=png)

图14.比较NtWriteVirtualMemory 2022-12\_Remcos:  a1f73365b88872de170e69ed2150c6df7adcdc9c与2016-07\_Cerber:  24aa45280c7821e0c9e404f6ce846f1ce00b9823的NtWriteVirtualMemory内核直接调用差异

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icpxOT5jcZXr2DVuzrxg2Zrh7BMiaV3N1P4dS1vIbdbbia0Cm2vln7tdpJbOXNBe28WpeWuI5sDQwcg/640?wx_fmt=png)TrickGate外壳代码的构建模块

如上所述，外壳代码一直在不断更新，但自2016年以来主要功能出现在了所有样本上。外壳代码的构建模块概述如下：

API哈希解析。

加载到内存...