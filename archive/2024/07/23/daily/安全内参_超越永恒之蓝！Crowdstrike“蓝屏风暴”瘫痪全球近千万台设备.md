---
title: 超越永恒之蓝！Crowdstrike“蓝屏风暴”瘫痪全球近千万台设备
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512223&idx=2&sn=a3c5025519cb8984da0306d836cb3ea5&chksm=ebfaf7bfdc8d7ea9a3ef9e3b8feed5a4b8195e526fad1dc7c199c275f5a6838829256ff9a427&scene=58&subscene=0#rd
source: 安全内参
date: 2024-07-23
fetch_date: 2025-10-06T17:43:33.414525
---

# 超越永恒之蓝！Crowdstrike“蓝屏风暴”瘫痪全球近千万台设备

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tAS8ibAianMCbV19h9Iz70n3vxleB2NAYyg2vX8GutdttdWQO8K4J9ibKGPDf9bNV52EJSDLGr9oFTg/0?wx_fmt=jpeg)

# 超越永恒之蓝！Crowdstrike“蓝屏风暴”瘫痪全球近千万台设备

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvammqIfLf9G4icrSDWUFoqNWqCsFuWSvIlXOHzx3HrJr3H2B2r0hsEcLJckicKsKSDxexzkGr17xW3Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

根据微软周末最新发布的公告，受CrowdStrike软件更新错误影响，全球约850万台Windows设备在上周五经历了大规模的IT中断。该事件的规模和损失仍在持续增长，从微软公布的数据来看其影响已经超过了“心脏滴血”、“想哭病毒”等历史上最严重的网络安全事件。

**简化恢复工作，微软发布“急救U盘”**

由于之前的系统恢复工作需要人工操作效率很低（重启电脑15次，或进入安全模式删除相关配置文件），微软紧急发布了一款USB急救工具，帮助IT管理员加快修复受CrowdStrike Falcon代理问题影响的Windows客户端和服务器。

制作该工具的系统要求是：Windows 64位客户端，并至少拥有8GB的可用空间，用于创建可启动的USB驱动器，同时还需拥有Windows客户端的管理员权限。（相关链接在文末）

尽管受影响的Windows设备不到总量的1%，微软表示，已动员数百名工程师和专家，直接与客户合作以恢复系统和服务。

**事件溯源，EDR安全再成焦点**

业界对此次全球范围的大规模系统崩溃有着诸多猜测，但微软在公告中指出，事故的根源在于2024年7月19日04:09 UTC推送到Windows系统的Crowdstrike传感器配置更新，该更新触发了逻辑错误，使全球范围内的关键计算机系统出现蓝屏故障。

微软的说法与此前Crowdstrike的解释基本一致。在周六的更新中，CrowdStrike提供了技术警报，详细说明了问题原因及企业可采取的解决步骤。

虽然业界对Crowdstrike以如此草率的方式匆忙发布更新表示不解，且事件深层原因仍在调查中，但是有一件事值得注意，在Crowdstrike推出安全更新的前一天，黑客组织FIN7在暗网公开销售能够绕过大多数EDR的黑客工具，号称EDR杀手（代号AvNeutralizer）。该工具利用了Windows内置的TTD显示器驱动（ProcLaunchMon.sys）和Windows进程浏览驱动（procexp）。该工具被广泛用于2023年4月份以后的勒索软件攻击。

安全产品（尤其是EDR/XDR工具）为了跨IT系统执行实时监控和威胁检测，需要尽可能高的权限，访问非常敏感的信息，而且启动时不能被轻易删除。然而，权力越大，责任越大，这些安全工具中的严重漏洞可被黑客利用绕过检测甚至武器化成“超级恶意软件“，用来部署勒索软件、窃取机密信息，而且难以被发觉和删除。近年来主流EDR产品频频曝出严重漏洞，威胁着数以亿计的设备。

攻击者一旦能够利用安全软件的漏洞（或者安全厂商“手滑”），就可将其变成杀伤力极大的攻击武器。因此，企业在部署EDR/XDR等安全解决方案时，需要提高警惕，加强安全管理，并定期进行安全评估和漏洞修复。

**史上最大规模网络安全事件**

Crowdstrike大规模系统崩溃事件已经导致全球数十个国家近千万台计算机瘫痪，造成数十亿美元的直接或间接经济损失，对全球社会和经济的长期影响难以估量。

西方主流媒体纷纷用“混乱”和“灾难”等词语形容该事件，并指出该事件的影响目前仍在持续，有可能成为历史上最严重的IT安全事件。

事件爆发后，Crowdstrike首席执行官George Kurtz在X平台连续发贴引发众怒，Kurtz首先用外交辞令轻描淡写地将该事件定义为一次“内容更新异常”，在随后的发帖中，Kurtz虽然被迫做出道歉，但矢口否认该事件是“网络安全事件”（Cyber Incident），并声称“客户受到了全面的安全保护”（下图），再次引来业界人士的口诛笔伐。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvammqIfLf9G4icrSDWUFoqNWOr657kY6ksNsIX2mZic4icf0DtyvxE5K7icJ7O899b79PV9rjSVlrv4og/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

事实上，Crowdstrike导致的全球性系统崩溃对其广大客户，乃至全球社会经济和人员财产的杀伤力和爆炸半径远超“想哭病毒”、SolarWinds供应链攻击、NotPetya、“心脏滴血”漏洞等著名网络安全事件，是历史上最严重的网络安全事件，堪称核弹级别。

虽然微软强调发生系统崩溃的设备占比很低，但微软对该事件的损失和影响预期并不乐观。“尽管受影响的系统比例很小，但考虑到许多企业选择在运行重要服务的设备上安装CrowdStrike，因此其广泛的经济和社会影响难以估量。”微软表示。

**网络安全威胁论的破灭**

在网络安全领域，美国及其盟国近年来不遗余力地宣扬“中国威胁论”，将中国、伊朗、俄罗斯等国家视为“敌对国家”，捏造散布中国黑客组织攻击国外关键基础设施、操纵舆论并从事大规模间谍活动的不实言论。此次Crowdstrike的一个轻微疏忽就对西方IT基础设施造成灾难性后果，这一事实再次凸显是谁才是全球最大的网络威胁制造者和实施者。

对于此次微软全球蓝屏事件，安全专家Patrick Jones在X发帖一针见血地指出：

*不知道谁会为此承担责任？中国？俄罗斯？伊朗？朝鲜？还是以上所有？但是，谁真正控制着世界上大部分的计算机和 IT？究竟是谁有能力进行如此大规模的黑客攻击？谁是永远不允许谈论或指责的对象？谁从未被追究责任，却似乎总是身处此类事件的中心？谁想统治世界，并相信自己被选中？谁从未接受调查，却一直在进行调查？谁控制着媒体，为你提供故事叙述？好好欣赏吧。*

**除了“微软蓝屏****”，还有多少核弹级的风险值得关注**

在这个高度依赖科技的时代，除了“微软蓝屏”这样“浅显”的威胁外，还有许多潜在的核弹级风险需要我们密切关注和防范。无论是操作系统、处理器、智能手机（硬件）后门、开源供应链攻击、海底光缆安全，还是量子解密威胁、太空网络安全、公有云安全问题，以及AI大模型数据泄露和隐私侵犯，都是悬在数字化社会上空的利剑。各国在追求技术进步和经济繁荣的同时需要不断提升技术安全性和风险管理能力，才能避免灾难性的网络安全事件不断爆发或重演。

**CrowdStrike和相关技术供应商提供的修复资源汇总如下：**

个人主机的恢复步骤：

https://www.crowdstrike.com/blog/statement-on-falcon-content-update-for-windows-hosts/

帮助解决CrowdStrike问题的恢复工具（微软）：

https://techcommunity.microsoft.com/t5/intune-customer-success/new-recovery-tool-to-help-with-crowdstrike-issue-impacting/ba-p/4196959

公共云或类似环境（包括虚拟）的恢复步骤：

https://www.crowdstrike.com/blog/statement-on-falcon-content-update-for-windows-hosts/#cloud

AWS特定文档：

https://repost.aws/en/knowledge-center/ec2-instance-crowdstrike-agent

Azure环境中微软针对CrowdStrike Falcon代理的指导：

https://techcommunity.microsoft.com/t5/azure-compute-blog/recovery-options-for-azure-virtual-machines-vm-affected-by/ba-p/4196798

通过Citrix进行Bitlocker恢复：

https://docs.citrix.com/en-us/citrix-endpoint-management/device-management/windows/windows-desktop-laptop#bitlocker-recovery-key

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：GoUpSec

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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