---
title: 新型“EDR杀手”工具现身网络攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492273&idx=1&sn=225390666f3289a71ea6b78f867d2e3e&chksm=e90dc89bde7a418d11f53ccf65de2cd69f259c6f862f2c379c876e7d7d6cdbd8772be3df95f6&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-08-16
fetch_date: 2025-10-06T18:05:28.114116
---

# 新型“EDR杀手”工具现身网络攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 新型“EDR杀手”工具现身网络攻击

BaizeSec

白泽安全实验室

**事件概述：**

Sophos安全研究人员揭露了一款名为EDRKillShifter的新型工具，该工具被用于攻击并终止端点防护软件。这一发现是在分析一起针对名为RansomHub的勒索软件攻击的失败尝试中被披露的。尽管勒索软件攻击未能成功，但事后分析揭示了这一新工具的存在。

自2022年起，随着用户越来越广泛地采用EDR工具保护端点，分析人员观察到，旨在禁用EDR系统的恶意软件在技术上越来越复杂。EDRKillShifter是此类恶意软件中的最新成员，它是一种“加载器”可执行文件，用于传递可能被滥用的合法驱动程序，也就是所谓的“自带易受攻击的驱动程序”(BYOVD)工具。

在5月的事件中，威胁行为者试图使用EDRKillShifter终止目标计算机上的Sophos保护，但该工具未能奏效。随后，他们试图在控制的机器上运行勒索软件可执行文件，但同样失败，因为端点代理的CryptoGuard功能被触发。

**EDRKillShifter工作原理：**

EDRKillShifter工具是一个“加载器”可执行文件，它是一种传递易受滥用的合法驱动程序的机制（也被称为“自带易受攻击的驱动程序”，或BYOVD工具）。根据攻击者的要求，它可以传递各种不同的驱动程序有效载荷。

执行过程包括三个步骤：攻击者必须使用包含密码字符串的命令行执行EDRKillShifter。当使用正确的密码运行时，可执行文件会解密一个名为BIN的嵌入资源，并在内存中执行它。

BIN代码解包并执行最终的有效载荷。这个最终有效载荷是用Go编程语言编写的，它会投放并利用各种不同的易受攻击的合法驱动程序，以获得足够的权限来取消挂钩EDR工具的保护。

**分析细节：**

初步分析显示，所有样本都共享相同的版本数据，原始文件名为Loader.exe，产品名为ARK-Game，暗示攻击者可能试图将最终有效载荷伪装成流行的电脑游戏ARK: Survival Evolved。所有样本都需要一个独特的64字符密码，如果密码错误或未提供，则不会执行。

执行时，EDRKillShifter将加密的BIN资源加载到内存中，并将其复制到一个名为Config.ini的新文件中，然后将该文件写入到二进制文件执行的同一文件系统位置。然后，它使用VirtualAlloc分配新的内存页，将加密内容写入新分配的页面，并删除config.ini文件，继续解密下一组有效载荷。

**执行失败：**

如果用户没有提供正确的密码，执行将失败。EDRKillShifter加载了一个名为BIN的加密资源到内存中，并将其复制到一个名为Config.ini的新文件中，并将该文件写入到二进制文件执行的同一文件系统位置。

**加载最终的EDR杀手到内存：**

第二阶段通过使用自修改代码技术来混淆。在运行时，第二层修改它自己的指令。由于实际执行的指令只有在执行期间才会显示，因此需要额外的工具或仿真来进行分析。

**最终有效载荷分析：**

我们分析的所有样本在内存中执行了不同的EDR杀手变体。它们都是用Go编写的，并且经过混淆处理（可能是通过使用名为gobfuscate的开源工具）。混淆器是旨在阻碍逆向工程的工具。

**缓解措施和建议：**

* 确保端点安全产品实现并启用了防篡改保护。
* 实施强化的Windows系统安全策略，确保用户帐户与管理员帐户之间有明确的权限分离。
* 保持系统更新，利用微软去年开始推动的更新撤销已知被滥用的已签名驱动程序的认证。

参考链接：

https://news.sophos.com/en-us/2024/08/14/edr-kill-shifter/

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