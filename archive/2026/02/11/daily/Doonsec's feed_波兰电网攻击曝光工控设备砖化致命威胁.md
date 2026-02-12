---
title: 波兰电网攻击曝光工控设备砖化致命威胁
url: https://mp.weixin.qq.com/s/ZWuI60DOGWqiYsKysm6xdQ
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:16:55.270532
---

# 波兰电网攻击曝光工控设备砖化致命威胁

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpChzSAoAGN5YbZ6b6KfsdwdvJ7Sxn3NydNe1UBCfLN5FnEIzyYbj3VO1e1xRvbyMG6phGBPmwco3NqiaCzjBz9r9xiarcHtjw58/0?wx_fmt=jpeg)

# 波兰电网攻击曝光工控设备砖化致命威胁

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

2025年12月29日，波兰电网相关的多个目标遭遇了一系列协同网络攻击，受攻击目标包括至少30座风电场、光伏电站，以及一座为近50万用户供热的热电联产厂。可见：[俄罗斯针对波兰电网进行破坏性网络攻击行动](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451184983&idx=1&sn=51136528937f325c19482a10af3fead8&scene=21#wechat_redirect)

此次攻击虽未对电网造成即时影响，但攻击者获取的访问权限、实施的破坏性操作，加之攻击发生在低温暴雪的特殊时段，让这起事件极具警示性。

尤为值得关注的是，这起事件中出现了多年来一直预警的一种战术、技术与程序（TTP）：将关键工业运营技术（OT）设备变砖，以此作为攻击放大策略。

砖（英语：brick）是指因严重配置错误、固件损坏或硬件故障，导致修复前无法正常使用。

软变砖设备通常都会有一些生命迹象，这类设备通常无法成功引导，卡在商标处，或无限重启。

硬变砖的设备通常几乎没有生命迹象。这类设备无法充电，或无法显示商标，屏幕基本不亮。硬变砖的主要原因是安装并非为目标设备设计的固件，中断刷写流程或遵循错误的刷写步骤。

事实上，此次电网攻击的威胁行为者似乎利用了CVE-2024-8036漏洞的一个变种，该漏洞是midnightblue安全团队数年前在ABB设备中发现的。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoDWibllgmqVPKDsHgjxVm7T5h3Bz1XQw7BQp3TaxUbuHCcfQuP8rlptoRg1SaamtSh8lTVicTQ0SsxGiblV8937GAghuib6xOf1ib0/640?wx_fmt=png&from=appmsg)

https://www.midnightblue.nl/blog/have-you-tried-turning-it-off-and-on-again-part-1

目前，攻击者使用该战术的频次正在上升，但防御方对其重视程度仍显不足，本文将探讨攻击者对嵌入式设备实施变砖攻击的具体风险、技术细节及潜在影响。

本文将聚焦此次针对风电场和光伏电站的攻击中所使用的部分战术、技术与程序。这些分布式能源发电设施向电网供电，并通过电网连接点（GCP）变电站与区域配电系统运营商（DSO）进行通信。电网连接点变电站内的远程终端单元（RTU）作为核心的远动控制与监控网关，与配电系统运营商的远程监控与数据采集系统（SCADA）进行交互。通常，配电系统运营商的监控与数据采集系统会向远程终端单元轮询采集测量数据和状态信息，也可发送指令或设定值，用于指定电网参数、切断供电并调节发电功率。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDohTvDialvh14icfK6hiaGAoUsNNU6opH8GH3e9Nk20fjkST1aUE4zc4ib0MnWR9fUomKVJEkCl6KiaNUctDMKb4fia1Ns8x8whnCMh0/640?wx_fmt=jpeg&from=appmsg)

配电系统运营商的监控与数据采集系统与远程终端单元的通信，经报道是通过部署在飞塔一体化防火墙和VPN集中器后的蜂窝或有线路由器链路，基于DNP3.0或IEC-101协议实现。

另有报道显示，波兰的配电系统运营商通常要求监控与数据采集系统和电网连接点之间通过串行链路通信，因此变电站内也配备了IP转RS232/485的串行转换器。

目前从公开报道中，尚无法明确该通信架构的具体实现方式（毕竟远程终端单元和监控与数据采集系统之间并非实际的点对点串行电缆连接），但综合信息可推测，远程终端单元要么通过串行链路连接至内置串转IP转换器的路由器，要么通过以太网连接，且通信过程中会经过IP-串行-IP的二次转换。

这种架构看似繁琐，但将串行接口仅部署在安全边界处，能有效减少暴露的攻击面。毕竟，若攻击者能够跨安全边界访问设备的IP协议栈，就有机会利用更多的解析漏洞，或调用协议中更多的潜在功能。

远程终端单元还会与变电站内的各类设备通信，其中包括负责故障检测、隔离以及断路器跳闸控制的保护继电器。

此次攻击导致电网连接点与配电系统运营商之间的通信中断，但该通信中断并不会使分布式能源发电设施停止向电网供电，这一情况可能引发电网功率失衡。如需了解该事件的更多背景信息，推荐阅读波兰计算机应急响应小组发布的详细技术报告、ESET针对此次攻击中所用擦除程序的分析文章，以及鲁本·圣塔马尔塔撰写的关于该事件潜在网络物理影响场景的深度分析系列文章。

波兰电网攻击中使用的破坏性战术、技术与程序

攻击过程中，攻击者按IP地址升序扫描探测各变电站内的各类工业运营技术设备，试图使其丧失正常功能或至少处于无响应状态，部分设备甚至被彻底变砖，只能通过物理方式更换。

日立Relion 650智能电子设备

Relion系列智能电子设备（IED）为变电站提供保护和控制功能，例如控制断路器、开关设备并检测故障状态。波兰计算机应急响应小组的报告中提及两起案例：攻击者使用默认凭证登录智能电子设备的FTP服务，删除设备关键文件，导致设备无法正常重启。

该攻击方式与利用CVE-2024-8036漏洞实施的软变砖攻击高度相似，而这一攻击方法是安全团队在为某配电系统运营商客户开展红队渗透测试时，在ABB设备中发现的。2020年，日立收购了ABB电网事业部80%以上的股份，同时获得了Relion 650和670系列智能电子设备的相关资产，而Relion 611、615、620和630等其他系列仍归ABB所有。从架构上看，这些设备的技术栈高度相似。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoDWibllgmqVPKDsHgjxVm7T5h3Bz1XQw7BQp3TaxUbuHCcfQuP8rlptoRg1SaamtSh8lTVicTQ0SsxGiblV8937GAghuib6xOf1ib0/640?wx_fmt=png&from=appmsg)

该漏洞的根源是异常条件处理不当（CWE-755）：

当FTP操作删除了关键配置文件，却未替换为可用的新配置文件时，就会触发漏洞。此类畸形的配置更新会让智能电子设备进入异常工作模式，丧失保护和控制功能，既无法进行远程通信，也无法通过设备自身的本地人机界面（LHMI）重置。

2016年，针对乌克兰电网的Industroyer攻击中，攻击者也曾尝试以类似方式破坏智能电子设备，只是破坏力相对较弱。当时，攻击者利用CVE-2015-5374拒绝服务（DoS）漏洞攻击西门子SIPROTEC 4系列智能电子设备，通过发送合法的协议指令（该操作难度极低，目前已有对应的Metasploit攻击模块），将设备置于固件更新模式并保持该状态，导致设备的保护和控制功能失效，且无法远程恢复，只能通过重启设备解决。值得注意的是，该漏洞在被利用时已存在一年半之久（与本次攻击中的CVE-2024-8036漏洞情况相似），且在攻击发生前半年，就已在俄罗斯某会议举办的夺旗（CTF）竞赛中被使用过。

日立RTU560远程终端单元

此次受攻击的分布式能源发电设施中，多数使用的是运行着过时固件的日立RTU560控制器。攻击者利用默认凭证登录该设备暴露的Web界面，随后上传恶意固件镜像，对设备实施硬变砖攻击。尽管RTU560设备从13.2.1版本固件开始新增了“安全更新”功能，但该功能默认未启用，且在13.7.7版本之前存在可被绕过的CVE-2024-2617漏洞。由于此次受攻击的所有远程终端单元均未启用该功能，攻击者可随意上传恶意固件。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqI0I3xwHz7RnKibruTlYOpOicRPw6ScsWr5KdjpjOuicu3oozcTNkBkW2WJz6XeRqmiaBW8CSxDr11xpaib24WjbGux3kGOuscKIrg/640?wx_fmt=png&from=appmsg)
攻击者在恶意固件的程序入口点插入了240字节的0xFF数据。从波兰计算机应急响应小组报告中提及的固件文件名（WBLRX）可判断，该恶意固件对应的是RTU560的核心模块——560CMR01通信单元的固件。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpibIDUh3pNs85gpjYmO0qZgFiaXsNPZXdHA68iarNRVOTpt2GJKibpvWcNtiaHC5gicaH4RF1dMiaTmAic13n5E0AjZV83Ria88pjfTP8Y/640?wx_fmt=png&from=appmsg)

560CMR01模块基于德州仪器AM3352（ARM Cortex-A8）微处理器打造，运行VxWorks操作系统，分为两个版本：R0001版本配备标准网络安全功能，R0002版本搭载专用加密芯片。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqICNNIqxqyCcnLFnO9bDAdiav1d9ibHwF8RgMe1YaRCjKwzFv5ibAcYp2sohcqShmZQC1vnPl87sQiahNQ2GLgc8bIQWZRHg6Ngfs/640?wx_fmt=png&from=appmsg)

在ARM32处理器中，0xFFFFFFFF的32位指令字会被解析为触发软件中断（SWI），且对应的SWI编号为0xFFFFFF，条件标志位为0xF，这一标志位表示该指令永不执行。该条件本质上使这条指令成为未定义指令，会触发未定义指令异常；在多数情况下，处理器会进入未定义模式，并执行向量表中定义的未定义指令处理程序。而在本次攻击中，这一异常最终导致设备重启，进而陷入无限重启循环，彻底丧失功能。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqUH8tCk9s7nZ8d78nQ62sb6qwra94Pvk1ao9xn6UNzvcQzgI2pc9zZahdRNKOtGfd4a0ZPcoFn4khuFqxHlG0WYmSJu3HibEj0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpadSKnk6ibMXe2rygSXrQYHicAoVvJxoMkMicnd6fB3S3pqicficrdhTplGtIHWrk3nq3cT3ic7za2c9ghaJicKeszDDHR0z1E048Hk8/640?wx_fmt=png&from=appmsg)

Mikronika RTUs 远程终端单元

在使用Mikronika RTUs 远程终端单元的分布式能源发电设施中，攻击者通过SSH协议，使用默认的root账户凭证攻陷设备，随后擦除设备的文件系统。波兰计算机应急响应小组的报告未明确此次受攻击的米克罗尼卡设备具体型号，但该品牌的多数设备均基于德州仪器OMAP片上系统打造，其ARM核心运行Linux系统，这也让攻击者开发攻击载荷的过程变得相对简单。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoj91xnx7pLIRyU44RuVLwcWGRHLWbIuIibaxHfiaicw06ZlOGapT26l7h2icHWubTHceJMMTmfhFbicV1r7HuBXgE7jQ1DAib6UGnzU/640?wx_fmt=png&from=appmsg)

Moxa NPort 6000 系列串口服务器

此次攻击中，作为协议转换器的摩莎NPort 6000系列串口服务器也成为目标，但攻击者并未将其变砖。他们利用Web界面的默认凭证攻陷设备后，将其恢复出厂设置，同时修改登录密码和IP地址为不可访问的地址，以此拖延设备的恢复运营时间。

这一行为颇为耐人寻味：2015年针对乌克兰电网的BlackEnergy攻击中，攻击者曾将摩莎另一系列的串转网转换器变砖，同样是为了拖延恢复进程。

事实上，摩莎的串口转换器在工业运营技术安全领域早已因存在大量严重且易被利用的漏洞而声名狼藉，例如摩莎NPort 5000系列存在多处认证相关漏洞和固件未签名问题，其中部分漏洞也影响了NPort 6000系列。摩莎NPort 6000系列的固件更新可通过串行控制台、Web界面或摩莎设备搜索工具（DSU）实现，后两种方式虽需要用户名和密码，但默认凭证的存在让这一防护形同虚设。杰森·拉森在S4x20大会的《14小时与一张电网》演讲中，就演示了向摩莎5610串口转换器推送恶意固件，从而植入自定义恶意软件的过程。该设备同样未实现安全启动和固件签名，相比编写并加载恶意植入程序，将设备变砖的操作更为简单。

波兰计算机应急响应小组的报告未明确此次受攻击的NPort 6000系列具体型号，尽管该系列最新推出的第二代产品（6000-G2）据称已实现安全启动和固件签名功能，但受攻击的设施大概率并未部署该版本设备。

摩莎的第二代设备加固指南中明确说明，设备无默认凭证；而初代设备的加固指南则指出，仅从2.0版本固件开始，设备才取消默认凭证。这一细节也印证了，受攻击设施使用的是运行过时固件的初代设备，攻击者本可轻易将其变砖。

摩莎NPort 6000系列加固指南相关内容：
为保障安全，设备默认启用账户和密码保护，需输入正确的账户和密码解锁设备，方可进入网关的Web控制台。
默认账户和密码均为小写，分别是admin和moxa。成功登录后，设备会弹出提示框，提醒用户修改密码以提升安全性。
「192.168.127.254提示：为提升安全性，请修改密码。」
从2.0版本固件开始，设备不再预设默认用户名和密码，首次登录前需自行创建，以增强设备安全性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrXx2iava6gFMj9BQIJXaAibaR9VibN3zUv62p2cYaVN4ibjvJQYtInKqPRt3xPC7tEdm6aKLZPa81hstOnu2Xh3XRAxdU1VXzb0Rw/640?wx_fmt=png&from=appmsg)

设备变砖为何值得高度警惕？

为何这一战术、技术与程序会引发如此高的关注？它难道不只是十多年来层出不穷的擦除程序和勒索软件的又一变种吗？完善的备份策略和应急响应计划，难道不足以规避最坏的结果吗？

简单来说：

变砖的设备无法远程恢复，在很多情况下，即便物理接触设备的本地接口，也无法完成恢复。这与被擦除的服务器有本质区别——服务器若配备惠普iLO、戴尔iDRAC等可远程访问的带外（OOB）管理接口，在理想情况下，管理员可直接通过该接口重新部署系统并恢复备份。

而嵌入式工业运营技术设备并不具备此类功能。若设备的固件被擦除，或文件系统损坏至无法正常启动的程度，部分设备可通过早期引导加载程序，借助本地串行控制台恢复出厂固件或备份固件，但这一操作需要工作人员到现场逐一操作每台受影响的设备。更有甚者，部分设备根本无此恢复功能；或攻击者在上传恶意固件时，同时篡改了引导加载程序，让这一恢复途径也彻底失效。在这种情况下，唯一的解决办法就是拆除并物理更换所有变砖的设备。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpOSZ093myDfT6FuARkNcvo0F9B2SibvJciarW0THQicEC6o4laWG3ycQQ3vJpCyV1XNMeA2ZGictBmPocRZYu3miaIUuENPKCScKqU/640?wx_fmt=png&from=appmsg)

在工业运营技术场景中，这一最坏情况造成的影响会更为严重。尽管物理更换数百台企业级交换机和服务器的过程既耗时又耗费成本，但操作本身相对简单，且厂商和商业仓库通常有足够的库存应对突发的需求高峰。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpDrfnG2Ke7xbO3f4L0yQylBPiccfFa2VQgj94VHI2pVjRzGQh4iaHqVacUlcYl0AE6CtOibCzMpT78FQYY0g0RhRr18oJmCZL8Jc/640?wx_fmt=png&from=appmsg)

例如，在NotPetya擦除程序攻击事件后，马士基仅用10天就完成了数万台新电脑和服务器的部署，重建了IT基础设施；而在臭名昭著的Shamoon擦除程序攻击中，全球范围内的企业曾紧急采购了数万台硬盘，用于替换被擦除的设备。尤其乌克兰的企业，在频繁遭遇此类“传统”企业级擦除程序攻击后，已形成了较强的抗风险能力。

但嵌入式工业运营技术设备的情况截然不同。资产所有者、系统集成商和经销商通常不会储备数百台备用的远程终端单元、智能电子设备、可编程逻辑控制器或串口转换器，厂商也不会保留大量库存。从DigiKey、RS Group等线上分销商及小型供应商的库存情况来看，这类设备的现货数量最多仅有几十台，少则不足十台。若一次性需要数百台，大部分设备都需要预订，甚至可能需要厂商按需生产。即便一切顺利，设备的交付周期也会超过一个月。美国国会收到的《战略变压器储备报告》中，也曾提及电网面临的变压器供应短缺问题，与此次情况类似。

此外，工业关键基础设施场景中，设备的更换、调试和现场验收测试（SAT）所需的时间，远超过企业环境中部署新服务器的时间。在这数周甚至数月的时间里，受影响的设施基本无法正常运营。尽管在远程站点安排工作人员现场手动操作，可在一定时间内弥补远程终端单元或串口转换器失效带来的影响（但如果同时受影响的站点过多，该方式也会迅速失效），但智能电子设备和可编程逻辑控制器是设施运营和安全防护的核心，失去它们的支撑，设施根本无法运行。这意味着，将工业运营技术设备变砖，能让攻击者将网络物理攻击的影响时长从数小时延长至数周。

技术细节解析

硬变砖与软变砖的区别

首先需要明确的是，设备变砖与常规的拒绝服务攻击并非同一概念，后者也常被用于放大网络物理攻击的影响，例如本次波兰攻击中针对摩莎NPort系列设备的操作，以及前文提及的Ind...