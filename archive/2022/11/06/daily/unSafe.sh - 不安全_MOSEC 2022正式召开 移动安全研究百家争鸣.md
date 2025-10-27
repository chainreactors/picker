---
title: MOSEC 2022正式召开 移动安全研究百家争鸣
url: https://buaq.net/go-134325.html
source: unSafe.sh - 不安全
date: 2022-11-06
fetch_date: 2025-10-03T21:49:27.323892
---

# MOSEC 2022正式召开 移动安全研究百家争鸣

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/e85061c24729070742355e587acdeaba.jpg)

MOSEC 2022正式召开 移动安全研究百家争鸣

“从系统内核到底层芯片你关注的移动安全问题这届MOSEC上都有奇安信集团总裁吴云坤在致辞中表示，MOSEC从2015创立以来，一直坚持聚焦移动安全、专注于前沿技术，吸引聚集二进制漏洞攻防领域的顶级专家
*2022-11-5 17:59:36
Author: [mp.weixin.qq.com(查看原文)](/jump-134325.htm)
阅读量:35
收藏*

---

“

**从系统内核到底层芯片**

**你关注的移动安全问题这届MOSEC上都有**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FSXtTeMhKQsVPFRMrxJfJ9wfoRWUPH6gmb9HRfHjLNxmaW7Zb4hzUeaD0wpjq2trASsOqjxnYh4Q/640?wx_fmt=png)

奇安信集团总裁吴云坤在致辞中表示，MOSEC从2015创立以来，一直坚持聚焦移动安全、专注于前沿技术，吸引聚集二进制漏洞攻防领域的顶级专家还有他们的顶级成果和智慧，为移动安全领域的技术发展做出了贡献。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FSXtTeMhKQsVPFRMrxJfJ98O4vUmxeKka2XB5MxF7ssxIZcyISErLzeFQMVDarVXicdbwGDxwe2Lw/640?wx_fmt=png)

“三人行必有我师。”POCSEC CEO JinWook在致辞中说，作为最棒的移动安全盛会，MOSEC举办八年来，吸引了大量优秀的安全从业人员发表了许多优秀的成果，希望所有参会者都能从中有所收获。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FSXtTeMhKQsVPFRMrxJfJ9FIBbg5autdHeAW83gDS0PDYe1vdfnOLVc5o4CBeJZiaRSWhNryicK4IA/640?wx_fmt=png)

1

**模糊测试框架——探测无处不在的攻击面**

作为苹果手机无线网络的重要模块之一，Apple 80211 Wi-Fi子系统的攻击面分布在操作系统的各个角落——从用户态守护进程到操作系统网络协议栈，再到各类内核扩展程序，这使得攻击者能够从四面八方对其发动攻击。“能否将模糊测试系统整合起来并协同工作极为重要，而这促使我设计了一套全新的模糊测试框架。”杭州薮猫科技联合创始人、CEO王宇说，搭建远程内核调试环境能帮助快速的定位和分析漏洞成因。这套框架可以帮助研究员系统的对攻击面进行安全测试，从而发现其中的漏洞等安全风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FSXtTeMhKQsVPFRMrxJfJ9nPq89wIGxcJLIJTaYrroibdjYeN2owsEPxsf1RLBoeQP172JAwHMaxw/640?wx_fmt=png)

值得注意的是，作为这套框架的重要成果，王宇现场分享了他挖掘的超过十个零日漏洞，充分展示了这套框架的实际应用价值。

2

**白帽子的终极梦想——漏洞的批量挖掘**

“漏洞研究者的一个终极梦想是，输入目标手机的型号版本，就可以自动挖掘获取它的0day漏洞。”獬豸安全实验室负责人、高级总监Flanker将所有白帽子的终极梦想一语道破。为了实现这个目标，Flanker分享了他的研究成果Java程序分析引擎，包括指针分析、跨过程污点分析等多个模块。使用该系统，Flanker挖掘到了数十个主流厂商系统中的高危漏洞。“虽然目前还存在着这样那样的限制，但技术的进步仍然能让我们不断逼近我们的终极梦想。”Flanker说到。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FSXtTeMhKQsVPFRMrxJfJ9NGAZib05KKOjhOsicjMVPdRB3x5HibVUy0YwT5YZgl6Ghq0ARueZ4o8Hw/640?wx_fmt=png)

3

**安全进阶——内核奥秘的探究**

作为iOS操作系统的内核，XNU历来都受到开发人员和安全研究员的关注。而Mach IPC作为XNU中Mach子系统最核心的模块之一，iOS上进程间以及进程与内核间绝大多数通信都经由Mach IPC完成。

“在对Mach IPC研究的过程中，我们发现了一些漏洞。”昆仑实验室安全研究员Brightiup介绍说，锁是XNU对象管理中很重要的一点，时机和位置不对都容易引入安全问题，及时关注新增加的代码对研究者也十分重要。Brightiup表示，在去年MOSEC期间发表的port类型混淆漏洞的基础上进一步研究，又发现了多个通过条件竞争触发的类型混淆漏洞。随后，Brightiup通过引入更多的相关对象和功能（turnstile,knote,workloop等），逐步增加了审计的范围后，又发现了不少UAF类的漏洞，包括在最新的iOS 16.1中被修复的一个漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FSXtTeMhKQsVPFRMrxJfJ97qqcIIjSpW3RhOMSbY9KV7AdObjF87UZb0CoIoVIlvdbDrCLVicvQvA/640?wx_fmt=png)

来自奇点实验室的两位安全研究员刘深荣、刘鹏举则将目光放在了微内核上。与Linux、Unix等传统宏内核不同的是，微内核尽可能简化了自身的功能，主要负责不同模块之间请求的传递。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FSXtTeMhKQsVPFRMrxJfJ9zpZw8Rt5tyoibBPzaaCBAbyub5V5f1Fsb8576Y2HkLuCHic2Rq5c0EVg/640?wx_fmt=png)

刘深荣、刘鹏举详细介绍了一款嵌入式的微内核操作系统几大特性，包括基于NameSpace实现的组件隔离机制，用户态文件系统，微内核中的虚拟内存管理实现，以及应用沙箱的设计。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FSXtTeMhKQsVPFRMrxJfJ9R9EtID0yFe7be6mOvMSu0GsWQFvibicecTIyxpgibEJhe9GfbWynQwR3Q/640?wx_fmt=png)

当然作为安全研究员，刘深荣、刘鹏举更关心的还是安全性。据介绍，为了更方便的对其内核进行模糊测试，刘深荣、刘鹏举选取了Syzkaller引擎对其进行了适配，通过对其增加了覆盖率反馈相关的实现以及Syscall支持，可以使其较好的支持Syzkaller进行模糊测试，并发现多个内核安全漏洞，并且讲解了漏洞的利用技巧。

4

**芯片级漏洞——亿万手机的达摩克利斯之剑**

作为全球最大的无晶圆厂半导体供应商之一，联发科在移动终端、智能家居应用、无线连接技术及物联网产品等市场位居领先地位，同时是目前全球智能手机芯片市场占有率最高的厂商，旗下MTK芯片被亿万手机和IoT设备使用。

盘古实验室安全研究员张雪雯的议题便与MTK芯片相关。据她介绍，在芯片固件里，安全启动信任链是保证设备安全性至关重要的一个环节，一旦安全启动被攻破，后续的安全防护都将失去意义。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FSXtTeMhKQsVPFRMrxJfJ9gE2gcEUuo6vVNWCGr2prYEG8XPA9Q4FwoxlNDNV4icWEGXOdJeWDerw/640?wx_fmt=png)

值得注意的是，如果漏洞位于BootRom（写死在芯片）中，鉴于该区域的只读属性，这就意味着它不像软件漏洞一样可以能通过软件更新手段进行修复，进而永久存在于芯片中，可以说是悬在亿万手机和物联网设备头上的达摩克利斯之剑。2019年9月末，苹果手机A系列芯片中被曝出存在BootRom的漏洞。

张雪雯通过若干漏洞实例，详解了BootRom漏洞成因、利用方式以及如何通过攻击BootRom来击溃 MTK 的安全启动链，从而达到控制整个手机操作系统的目的。

5

**车载娱乐——黑客也狂欢**

除了手机以外，各类物联网设备也颇受极客们的青睐，电动汽车便是其中之一。近些年，电动车已然成为全球最具发展潜力的行业之一，并且受到互联网造车概念的影响，大批新兴的电动车制造商纷纷入市，与传统车企展开了同台竞技。

其中作为车企之间竞争的焦点之一，车载娱乐系统已经成为提升消费者驾车体验的重要环节，几乎每个厂家都争先恐后地为自己旗下电车配备自动驾驶、OTA、语音助手、导航、在线音乐电影等功能。

与此同时，车载娱乐系统的安全性却参差不齐。今年上半年，大众和奥迪几款车型的车载信息娱乐系统被曝存在多个漏洞，攻击者可以通过车载娱乐系统打开或关闭麦克风，监听司机正在进行的谈话、访问车主个人隐私信息以及车辆定位信息等。

据盘古实验室的安全研究员闻观行介绍，2021年入手的第一辆电动汽车，激发了他对于车载娱乐系统的兴趣。在近一年的时间里，闻观行找到了一条完整的漏洞利用链条来取得车载娱乐系统的完全控制权限。此外，闻观行还分享了获取权限后可以做到的一些功能演示，包括如何控制门窗、开启调试、跟子系统通信等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FSXtTeMhKQsVPFRMrxJfJ9N5kvtkCRsOC6yVP8yYyjZ3b0Gq47oUO0Npv0ynoVJA36TfhdBNlIgA/640?wx_fmt=png)

同时,作为历届MOSEC的重头戏，BaiJiuCon每年都吸引到众多嘉宾的积极参与。安全就酒，越喝越有，与会嘉宾只要喝一杯白酒，就有机会获得一定时间的演讲机会。

MOSEC移动安全技术峰会自2015年在国内首次举办以来,立足于高质量的安全技术,致力于分享移动安全领域前沿性的技术议题及发展趋势。因高质量的安全技术分享,每年大会都赢得与会者及业内一致好评,目前已经成长为国内安全技术峰会的重要风向标,吸引全球最顶尖的网络安全专家和白帽子黑客前来参会。

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/1UG7KPNHN8FxuBNT7e2ZEfQZgBuH2GkFjvK4tzErD5Q56kwaEL0N099icLfx1ZvVvqzcRG3oMtIXqUz5T9HYKicA/640?wx_fmt=gif)

戳“阅读原文”一起来充电吧！

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MjM5NTc2MDYxMw==&mid=2458482754&idx=2&sn=7b6d2758b9bb81f13ebc2a51d9c2340a&chksm=b18e48c886f9c1de2b5d078f995799418e0228912095133a284c7d41655a63f36a888530a3c7#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)