---
title: 「深蓝洞察」2024年度最难以阻挡的攻防趋势
url: https://mp.weixin.qq.com/s?__biz=MzkyMjM5MTk3NQ==&mid=2247486905&idx=1&sn=435f1a02245e2b6b030f4a1d1863f40b&chksm=c1f44971f683c067fa6fae09578a2f36a6f6a415dd0d6eab3ed98da5d345432cd10ebc8688a8&scene=58&subscene=0#rd
source: DARKNAVY
date: 2025-02-15
fetch_date: 2025-10-06T20:39:34.198826
---

# 「深蓝洞察」2024年度最难以阻挡的攻防趋势

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6aFicjrXnvghHHlWia0koFlEthNQBDmGsdAHibCS7s90oeQB2bL99EQqqibYPnef07MNib4qNK3ZaUD1Alel65RhRfQ/0?wx_fmt=jpeg)

# 「深蓝洞察」2024年度最难以阻挡的攻防趋势

原创

深蓝洞察

DARKNAVY

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvghHHlWia0koFlEthNQBDmGsdrma2PHdAgrGyRGRjXwr4vCfqjljxnnianZNmP1wLJhtzdggBh4Kxmgw/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvgh2Q51ebIpwK8q31M942CdX8SdkA8XyOFfpaK8ahXPNEmvnAAlA3YeMDYACdPzRh36gc4zfzvCOHA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMjM5MTk3NQ==&mid=2247486888&idx=1&sn=d522612c695b4b968d31c40d17546643&scene=21#wechat_redirect)

**近**年来，漏洞攻防不断演进。从多年前仅需一个栈溢出就能攻破系统，到如今需要运用各种精妙的手法来突破系统的层层防御。“盾”与“矛”始终处于动态对抗：每当新的防御措施出现，新的攻击手段随之而来。防御机制的升级促使攻击者寻找新的突破口，而攻击方法的创新又推动着防御技术的进一步发展。

以下为本期****《深蓝洞察 | 2024 年度安全报告》****的**第七篇**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvghHHlWia0koFlEthNQBDmGsdcsibDrkkRapsOqCcVQAr37192UP4IgIeFqfr9QzGSxxxNCWvWpmEzAA/640?wx_fmt=png&from=appmsg)

**愈发坚韧的“盾”**

**每**个防御机制的提出都是对内存漏洞利用的精准打击。多年前，ASLR的引入显著提高了漏洞利用的难度和复杂性。时至今日，绕过ASLR仍然是大多数漏洞利用的首要步骤。到了2024年，针对内存破坏的防御机制更是层出不穷。

2023年推出的Google Pixel 8支持了被称为“内存问题终极武器”的Memory Tagging Extension（MTE）特性，其是ARM v8.5新增的一个硬件特性，MTE将指针与其内存利用tag进行匹配，以此来阻止内存的非法访问。同时，这也是MTE首次走入消费者群体。**2024年的1月，DARKNAVY的安全研究员发布了****[关于MTE对软件安全性影响的研究](https://mp.weixin.qq.com/s?__biz=MzkyMjM5MTk3NQ==&mid=2247484917&idx=1&sn=b2a1c2cbb13b8cd865d72bd7c4a26f1e&scene=21#wechat_redirect)**。研究表明，MTE有效缓解了堆内存漏洞（如UAF、堆越界读写等），在线性溢出场景下几乎完全消除了漏洞利用的可能性。作为UAF漏洞的长期受害者，Google也为Chrome提出了MiraclePtr机制，更是自信地宣称：受MiraclePtr保护的UAF不再视为安全漏洞。

Linux作为使用最广泛的操作系统之一，其内核近几年也引入了各种防御措施以阻止内存破坏的利用。为了缓解内核中的堆内存破坏问题，Linux Kernel中引入 "SLAB VIRTUAL"、"RANDOM\_KMALLOC\_CACHES"、"AUTOSLAB"等一系列防御机制。为了加强用户态程序的安全性，Linux Kernel 6.10新增系统调用mseal（memory seal），允许开发人员在程序运行时保护内存区域免受非法修改。

那么如此多的防御机制是否阻止了某些利用呢？

2024年11月，苹果披露了两个针对WebKit的在野利用，但这些利用仅限于Intel芯片的Mac设备。为什么2024年的漏洞只在较早的系统版本上被利用？这很可能与M系列芯片的先进防御机制有关，这些机制阻止了攻击者的利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvgh7UORFicKxvM5WVYBqDf1pmfcooibMT7F1B5ia1UA3ia5EyugdQlxuicBnccOLUK7fLDJoHI3475dhrWQ/640?wx_fmt=png&from=appmsg)

WebKit 漏洞披露

从软件到硬件，从用户态到内核态，在防御机制的层层铁壁下，内存漏洞已难以突出重围。种种迹象表明，内存漏洞似乎正走向终结。

**未来之“矛”**

**漏**洞不会消失，安全问题依然存在，那么在内存漏洞式微的时代，一个"powerful"的漏洞及其利用又是什么样呢？

2024年6月，Meta Red Team披露了漏洞CVE-2024-31317，该漏洞允许攻击者以任意应用身份执行任意代码，并可在Android 9及更高版本上实现利用，实现Android通杀。

值得一提的是，CVE-2024-31317并不是一个内存破坏漏洞，而是发生在Zygote的命令注入漏洞。Zygote是Android系统上的核心组件之一，它会孵化出Android中Java世界的所有进程，system\_server也不例外。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvgh7UORFicKxvM5WVYBqDf1pml9clvVYAhWAKluw7HyxqSzaIXqaTCdBDnYdt9dYgiaBZibMgmcD2eia4Q/640?wx_fmt=png&from=appmsg)

Zygote 功能展示

(https://dawnslab.jd.com/the\_return\_of\_mystique/)

实际上，Zygote是通过command socket从system\_server中接收指令，并根据指令孵化出子进程。然而，Zygote只是盲目地去解析从system\_server接收到的buffer，而不做额外的二次校验。因此，如果能够通过某种方式操纵system\_server在command socket中写入攻击者可控的内容，就可以实现命令注入！

研究人员分析发现，`denylistexemptions` 就提供这种能力。在该机制中，当`hidden_api_blacklist_exemptions` 被修改后，新写入的值会在解析后直接写入到Zygote command socket中。因此，只要控制该值即可实现命令注入。

下图展示了该漏洞的利用效果之一，启动一个可调试注入的settings进程：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6aFicjrXnvgh2Q51ebIpwK8q31M942CdXAkUDvyz69fPQia5cPad1PDZLjDMibusA1yibsq8cEMO0C0nKAGIOdqvzg/640?wx_fmt=jpeg)

CVE-2024-31317 的利用效果之一：启动一个可调试注入的settings进程

(https://dawnslab.jd.com/the\_return\_of\_mystique/)

可以看到该漏洞并不涉及内存破坏，依然影响了众多的安卓系统，这种漏洞本质是程序逻辑层面出现了问题，其影响力不亚于甚至超过传统的内存漏洞。随着内存漏洞利用门槛的持续攀升，非内存破坏类漏洞逐渐成为攻击者实现目标的“捷径”：

* 2024年2月，著名的“XZ Utils backdoor”事件曝光，一位别有用心的开发者在社区潜伏多年，最终成为核心维护者后在项目中植入了隐蔽后门。
* 2024年4月，全球知名防火墙软件PAN-OS被发现存在命令注入漏洞CVE-2024-3400，攻击者可对运行该系统的设备进行未授权RCE，并获取系统root权限。
* 2024年6月，DEVCORE披露了漏洞CVE-2024-4577，揭示Windows环境下运行的PHP-CGI存在参数注入漏洞。
* 2024年11月，watchTowr Labs披露了"FortiJump"漏洞，指出网络管理平台FortiManager存在命令注入漏洞。
* 2024年12月，DEVCORE的Orange Tsai在Black Hat EU 2024揭示了Windows ANSI API中潜藏的安全隐患。众多软件未能正确处理Windows的"Best-fit"特性，导致路径/文件名、命令行和环境变量的注入问题，并且几乎影响到全球所有Windows系统版本。

大胆猜测，内存漏洞难以利用后，未来之“矛”或许就隐藏在各种逻辑漏洞、供应链攻击之下。

**深蓝洞察**

当内存安全防御构建起层层壁垒，攻击者的“矛”已悄然转向更隐蔽的战场。“没有绝对安全的系统”，内存安全逐渐成为基础设施的“及格线”，安全防御面临更深层的体系化挑战：如何构建覆盖软件供应链的信任验证机制？如何实现业务逻辑的自动化安全建模？这些问题将是下一代安全对抗的重点。

安全对抗从未终结，只是在不断升级的维度中重塑对抗格局。安全研究者需要以更立体的视角审视安全边界——当内存漏洞走向黄昏时，逻辑漏洞的迷雾正在黎明中显现。

***参  考：***

[1] https://en.wikipedia.org/wiki/Address\_space\_layout\_randomization

[2] https://source.android.com/docs/security/test/memory-safety/arm-mte

[3] https://www.darknavy.org/blog/strengthening\_the\_shield\_mte\_in\_memory\_allocators/

[4] https://blog.trailofbits.com/2024/10/25/a-deep-dive-into-linuxs-new-mseal-syscall/

[5] https://lore.kernel.org/lkml/20230915105933.495735-15-matteorizzo@google.com/

[6] https://chromium.googlesource.com/chromium/src/+/ddc017f9569973a731a574be4199d8400616f5a5/base/memory/raw\_ptr.md

[7] https://webkitgtk.org/security/WSA-2024-0007.html

[8] https://support.apple.com/en-us/121752

[9] https://en.wikipedia.org/wiki/XZ\_Utils\_backdoor

[10] https://security.paloaltonetworks.com/CVE-2024-3400

[11] https://rtx.meta.security/exploitation/2024/06/03/Android-Zygote-injection.html

[12] https://devco.re/blog/2024/06/06/security-alert-cve-2024-4577-php-cgi-argument-injection-vulnerability-en/

[13] https://labs.watchtowr.com/hop-skip-fortijump-fortijumphigher-cve-2024-23113-cve-2024-47575/

[14] https://worst.fit/

[15] https://blog.flanker017.me/the-new-mystique-bug-cve-2024-31317/

明日，请继续关注《深蓝洞察 | 2024 年度安全报告》**第八篇**。

[![](https://mmbiz.qpic.cn/sz_mmbiz_gif/6aFicjrXnvgjjC2N7cDk3tsibSvNMXgndSRcnppHYug30bxTuDeN0qibDaRK8iaNmILicJXTrFhk9l1AnNAzJyFiauJA/640?wx_fmt=gif&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk0NzQ5MDYyNw==&mid=2247486978&idx=1&sn=858cee48fafc087c8fe6fd5829ac30f5&scene=21#wechat_redirect)

DARKNAVY 推出**《深蓝洞察专业版》**

独家深度研判-漏洞利用关键路径与安全防御深层逻辑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvggJOTO1cSAE3iaG1OqQ5GSwVa56VMseKhYamaKAaIoPuxE5icNOryKLuspT93O8XDTK1pnPPXs4URoA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvgiarjKdjUPPeBl73LPAQDzoiciaW1JM78eyiacmXTdzGq4ibClwvqib1CyrMlPaJajdnLn2Db1FwmbtIQtA/0?wx_fmt=png)

DARKNAVY

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvgiarjKdjUPPeBl73LPAQDzoiciaW1JM78eyiacmXTdzGq4ibClwvqib1CyrMlPaJajdnLn2Db1FwmbtIQtA/0?wx_fmt=png)

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