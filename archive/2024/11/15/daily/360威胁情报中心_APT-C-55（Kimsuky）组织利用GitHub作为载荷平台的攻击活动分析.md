---
title: APT-C-55（Kimsuky）组织利用GitHub作为载荷平台的攻击活动分析
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247504218&idx=1&sn=47c3680b0c07f8e130630073914a3992&chksm=f9c1e253ceb66b45133aab01c77e2d084f8fab26acb1b923dc60b611085dbacce4f44f642926&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2024-11-15
fetch_date: 2025-10-06T19:21:53.347987
---

# APT-C-55（Kimsuky）组织利用GitHub作为载荷平台的攻击活动分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8ZMbmxpgE99XXeGFkZ2aKibrQMwq5Ixzotz9esxYh5hSc6mxCibX2icI8Q/0?wx_fmt=jpeg)

# APT-C-55（Kimsuky）组织利用GitHub作为载荷平台的攻击活动分析

高级威胁研究院

360威胁情报中心

**APT-C-55**

**Kimsuky**

APT-C-55（Kimsuky）组织，也被称为Mystery Baby、Baby Coin、Smoke Screen、BabyShark、Cobra Venom等多个别名，最早由Kaspersky在2013年公开披露。长期以来，该组织专注于对韩国的智囊团、政府外交部门、新闻媒体和教育学术机构等进行网络攻击。在过去几年中，Kimsuky的攻击范围已经扩大，目标包括美国、俄罗斯和欧洲等国家，其主要目的是进行情报窃取等。

在持续监测Kimsuky组织的威胁活动过程中，360高级威胁研究院通过对与Kimsuky相关的样本进行细致入微的关联分析，鉴别出一个具有高度关注价值的恶意文件。深入剖析该文件后，我们确认其中包含的代码与Kimsuky组织历史上使用的恶意宏代码存在显著的相似性。进一步的调查显示，Kimsuky组织采纳了一种新颖策略，即利用GitHub作为恶意载荷的分发平台，以此实现信息窃取等恶意行为。这一发现不仅凸显了Kimsuky组织在技术和战术上的动态演变与进步，同时也强调了他们对特定目标持续且精密的威胁态势，以及其在隐蔽性和复杂性方面的提升。

# **一、攻击活动分析**

##

## **1.攻击流程分析**

在日常的高级威胁追踪过程中，我们注意到Kimsuky组织利用LNK类型的文件实施攻击。特别地，我们发现了一个名为“멀티캠퍼스강연의뢰서\_ 김병로교수님.docx.lnk”的LNK文件。为进一步探究，我们对其进行了分析，并意外地发现了另一个具有相同名称的文件。值得注意的是，该文件的实际类型并非LNK，而是包含了一段混淆的脚本代码。通过360安全大脑的深入分析，我们发现这段代码与Kimsuky组织所使用的恶意宏代码高度相似，这一发现引起了我们的高度警觉。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8UMu3LXicAyV8ibmWCQqUTjxxRrBqdfdxvHEsNmBmNdE9GaEcFxPNI7WQ/640?wx_fmt=png&from=appmsg)

图1 混乱的代码(左)和恶意宏代码(右)对比

随后的分析揭示了Kimsuky组织利用GitHub平台来投递恶意载荷的攻击活动。我们推测，在这次攻击活动中，Kimsuky组织依然采用了恶意文档作为初始攻击手段，进而部署后续的恶意载荷以进行信息窃取。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8NM6blHpXlHIxtPR67qKEiaYlUiatuc3wiccvUW7VGcaYnCW4IicIexKia0A/640?wx_fmt=png&from=appmsg)

图2 攻击流程图

## **2.攻击组件分析**

对上述提到的混淆代码进行深入分析后，我们识别出其中嵌入的一个恶意地址（https://raw.githubusercontent[.]com/vertigose/risker/main/db.txt）。紧接着，我们对该GitHub账号进行了全面分析。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP82Tz7NPeXb1BcF7DVQGm4OrzovF7c9SBPrwQJLx7lsKxps6lZ0PTPibA/640?wx_fmt=png&from=appmsg)

图3 去混淆之后的恶意代码

我们发现该GitHub账号创建于2024年6月14日，并且其中托管了一个具有恶意性质的存储库。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8FicUtUmfia0gpu9Gm6y9UCiaF1ewmJYjMhBib336ve4BQmehwn40vbT8fw/640?wx_fmt=png&from=appmsg)

图4 恶意的存储库示例

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8ypjeSMAoDYOKzFTIyOYCIhjgLM70qzJojR0gnoY4LoWN9jhgPFxDuA/640?&wx_fmt=png)

图5 账号建立时间示例

该存储库中包含了四个恶意载荷，其中db.txt是攻击者在成功利用初始载荷后所下发的第一个恶意代码。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8Vp0NdJCFfEgMbicrwVhLFz8msaHUS1B4d0xfiaylKxhUCXsra1HRCbJQ/640?wx_fmt=png&from=appmsg)

图6 恶意载荷示例

这些恶意代码的主要功能是调用getinfo、uploadResult以及downCommand函数，以从远程的GitHub地址下载info1.txt、up1.txt和down1.txt这三个文件，解密并执行它们。特别地，down1.txt的下载过程被设置为每30分钟循环进行一次。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8G6L3e9Zubsxwq55BvMKyj2VsibfSZ7T2qXYrrEJrTS67oiaFBqyicvyFg/640?wx_fmt=png&from=appmsg)

图7 db.txt中恶意代码示例

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8uGQO3wbqficffgibZTySHQBgX6pDft8rvyoH9YTnq2XmQYZUdH1iakadA/640?wx_fmt=png&from=appmsg)

图8 db.txt中实现主要功能的恶意代码示例

其中，DecodeString函数代码的作用主要是使用提供的密钥从安全字符串中恢复原始数据。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8Ca4TpPbOYzrd1Y8wV9BibXPQqBPuDbrd6MsXOWFouEwBkfPe6YKXIFQ/640?wx_fmt=png&from=appmsg)

图9 db.txt中实现解密功能的恶意代码示例

解密后的info1.txt主要负责收集用户最近访问的文件列表、系统的完整网络配置信息，以及当前系统的所有进程信息，并将这些信息保存到%appdata%\Ahnlab\avira.txt文件中。

据我们所知，AhnLab是一家知名的韩国网络安全企业，以其卓越的网络威胁情报能力和威胁检测与响应服务著称。另一方面，Avira Operations GmbH & Co. KG是一家德国跨国计算机安全软件公司，以其广受欢迎的Avira Free Security Suite防病毒软件而广为人知。攻击者利用此类信息，并以防病毒产品相关的文件路径进行伪装，这是一种常见的社会工程学技巧，旨在增加攻击活动的隐蔽性。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8Me3V3q72pwAX2wh9sDD5ickmUJWuubRibY4SYf9GesTXG8UUpp0FYKhQ/640?wx_fmt=png&from=appmsg)

图10 info1.txt解密后的代码示例

解密后的up1.txt主要负责将包含受害者系统信息的avira.txt文件上传到远程FTP服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8ewbXU4JGH7TY11GhTtsqX4lFP2GyF3VdtwOcxuJ2W3MuOusZQnfwMg/640?wx_fmt=png&from=appmsg)

图11 up1.txt解密后的代码示例

解密后的down1.txt则负责将一段powershell命令保存到%appdata%\utf8settings.ini文件内。这段命令的主要功能是从远程地址（https://raw.githubusercontent[.]com/vertigose/risker/main/db.txt）下载恶意载荷并执行。

之后，该脚本会在系统的Startup目录下创建一个名为settinqs.lnk的快捷方式，该快捷方式指向PowerShell可执行文件，并设置相应的参数，确保在系统启动时，PowerShell以隐藏窗口的方式执行保存在utf8settings.ini文件中的命令。

作为隐蔽性措施的一部分，该脚本还会清理掉PowerShell的历史记录文件ConsoleHost\_history.txt，这样做是为了进一步降低其恶意行为被检测到的风险。通过这样的手段，攻击者能够确保其恶意软件在受感染系统中持续运行，同时难以被用户或常规安全检查发现。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8FqCyU8AfIoO4ibIr06LpxpAJjySPPWlVzu2Fibv3BzBnZLfnMXQ3M9pA/640?wx_fmt=png&from=appmsg)

图12 down1.txt解密后的代码示例

# **二、基础设施分析**

在对攻击者运营的FTP服务器进行调查时，我们发现了两个特定的文件夹：strongsi.sportsontheweb[.]net和sussthanks.sportsontheweb[.]net。其中，sussthanks.sportsontheweb[.]net文件夹中保存了与受害者系统交互的相关信息。基于我们的分析结果，我们推断攻击者可能使用这两个域名作为其攻击活动的一部分，并将收集到的信息存储在这两个对应的文件夹内。这表明攻击者可能通过这些域名进行恶意操作，并将受感染系统的数据汇总在FTP服务器上的指定位置。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8PutCgEMOvMTMMCzebyic30bw0iaHvGNTKZ2LjjcUUDiajzgGt2jw1FFXQ/640?wx_fmt=png&from=appmsg)

图13 FTP服务器上发现的文件夹示例

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8icYjKuYJNCczibmvl6C35H43O7KaXYEM0Gp8AW6AOd5gmUne9qHWHVXw/640?wx_fmt=png&from=appmsg)

图14 sussthanks.sportsontheweb[.]net文件夹内容示例

其中的php文件的代码主要用于记录访问者的相关信息。当访问方式为POST时，代码会以访问者的IP地址和当前日期为文件名创建一个新的文件，并将POST请求中的内容保存到这个文件中。

这种做法允许攻击者跟踪和分析受害者的活动，同时为后续的攻击活动提供有价值的数据。通过这种方式，攻击者可以轻松地将不同受害者的数据区分开来，并根据需要对这些数据进行整理和利用。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pp2ZVz57a8IjmDK25jAbvP8yjy0W3RuP6c6T6fsuj6Xzjx0Yxz4DAH0xGpd1UTffKxRAMSicB52Jdw/640?wx_fmt=png&from=appmsg)

图15  php代码示例

# **三、归属研判**

基于上文提及的混淆代码与Kimsuky组织过往使用的恶意宏代码之间的相似性，以及代码中明确提及的与韩国相关的信息（如“AhnLab”字符串），这些特征均与Kimsuky组织典型的攻击模式和地域目标相吻合。因此，我们有足够的理由将这次利用GitHub作为载荷分发平台的攻击活动归属于Kimsuky组织。

# **四、防范排查建议**

# 1. 定期扫描系统中的可疑文件，特别是那些位于非标准路径或具有异常行为的文件。

2. 使用文件签名验证工具来验证%appdata%\Ahnlab\avira.txt文件的来源和完整性，确保它没有被篡改或感染。

3. 部署网络监控工具，实时监控所有进出网络的流量，重点关注与未知GitHub存储库的通信。

4. 定期检查正在运行的进程列表，识别并调查任何未经授权或可疑的进程，特别是那些与PowerShell相关的进程。

5. 使用应用白名单策略，限制只能运行经过批准的软件，防止恶意软件执行。

6. 对员工进行安全意识培训，教育他们如何识别和处理钓鱼邮件、可疑链接和未知文档。

7. 建立和测试数据备份和恢复计划，确保在发生安全事件时能够快速恢复关键数据和服务。

#

**附录 IOC**

#

bdb4dedc5706a88233e4f9d96d97f04f

28EBE557693B889713AC191766C62643

1784304e486d48ee0710fd5037859209

5f00a81c906f72821b577873b13f79d4

ftp://4209698:XmdDv4T6enkizfU@genyo.getenjoyment.net/genyo[.]getenjoyment.net/

https://raw.githubusercontent.com/vertigose/risker/main/db[.]txt

https://raw.githubusercontent.com/vertigose/risker/main/info1[.]txt

https://raw.githubusercontent.com/vertigose/risker/main/down1[.]txt

https://raw.githubusercontent.com/vertigose/risker/main/ up1[.]txt

https://raw.githubusercontent.com/wanpaz/czech/main/db[.]txt

https://raw.githubusercontent.com/wanpaz/czech/main/info1[.]txt

https://raw.githubusercontent.com/wanpaz/czech/main/down1[.]txt

https://raw.githubusercontent.com/wanpaz/czech/main/up1[.]txt

**团队介绍**

TEAM INTRODUCTION

**360****高级威胁研究院**

360高级威胁研究院是360政企安全集团的核心能力支持部门，由360资深安全专家组成，专注于高级威胁的发现、防御、处置和研究，曾在全球范围内率先捕获双杀、双星、噩梦公式等多起业界知名的0day在野攻击，独家披露多个国家级APT组织的高级行动，赢得业内外的广泛认可，为360保障国家网络安全提供有力支撑。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

360威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

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