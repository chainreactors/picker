---
title: 微软蓝屏事件“致死率”高达3%
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546121&idx=3&sn=e9754e18b01b98f222868451be49df77&chksm=fa9383c8cde40ade8af8036c82c9062c2a5462cdeb53e8c73ec983eb88e710ec0f14e0321c20&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-01
fetch_date: 2025-10-06T18:06:00.481815
---

# 微软蓝屏事件“致死率”高达3%

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nOibnP9AsqErf6zoibLYbeJkKjatP5v1Z8uiclqXT1MmE3aR5oVVLr3OJnQ4NibTx1IrOSDbt5SpibhuQ/0?wx_fmt=jpeg)

# 微软蓝屏事件“致死率”高达3%

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176nOibnP9AsqErf6zoibLYbeJkvNw7OIUKmV95re41XEAGK5HicVFScfBhGvqW13dzkWnHlFYYZgyl3oA/640?wx_fmt=png&from=appmsg)

近日，CrowdStrike最新报告显示约3%的设备错过“抢救时机”，至今未能从此前的CrowdStrike软件更新引发的全球性系统崩溃事件中恢复。

尽管大部分受影响的系统已经恢复正常运行，但CrowdStrike大规模系统崩溃事件给全球经济和网络安全行业带来的损失和深远影响远超业界预期。此次事件不仅导致了全球范围内的业务中断，还对企业的运营和经济造成了深远影响。本文将从以下五个方面详细评估这次事件的影响及其后续发展。

**3%的系统设备至今回天乏术，损失高达54亿美元**

在此次由CrowdStrike软件更新引发的全球性系统崩溃事件中，微软统计显示约有850万台Windows设备受到影响。虽然CrowdStrike首席执行官George Kurtz表示，97%的受影响设备已经恢复正常，但仍有约25万台系统设备（约3%）至今未能恢复。从事件响应周期和成本来看，这些设备可能已经错过了最佳“抢救时机”，失去了恢复的可能或价值。专家指出，由于系统的崩溃，这些设备可能需要进行完全重置或更换，导致企业额外的时间和金钱投入。

此次蓝屏事件对全球经济和各行业造成了巨大的显性和隐性损失。根据Parametrix Insurance的估计，此次事件给财富500强公司带来的损失约为54亿美元。这一损失不仅包括因系统崩溃导致的直接经济损失，还包括航班取消、紧急响应系统瘫痪等引发的连锁反应。例如，达美航空由于机组调度系统瘫痪，不得不取消数千航班，造成大量乘客滞留和航空运营混乱。银行、医疗机构和其他关键基础设施也受到了严重影响，进一步放大了此次事件的负面影响。

**最危险的黑客：CrowdStrike**

Crowdstrike首席执行官在X上矢口否认CrowdStrike更新导致全球大规模系统崩溃是安全事件，结果遭到大批安全专业人士在跟帖中群起围攻，称该事件比任何网络攻击都更可怕。

此次事件暴露了网络安全公司自身也是一种安全威胁。在微软蓝屏事件之前，美国政府刚刚封杀了卡巴斯基，“罪名”是对美国国家安全构成威胁，但颇具讽刺意味的是，Crowdstrike导致的微软蓝屏事件，其杀伤力和爆炸半径远超任何一次网络攻击，同时也表明美国政府认为卡巴斯基对国家安全构成威胁，绝非危言耸听。

CrowdStrike作为全球知名的网络安全公司，其产品在众多企业和政府机构中得到广泛应用。然而，正是这种高度的市场集中，使得任何一次失误都可能引发全球性的连锁反应。这再次提醒我们，网络安全市场的健康发展需要多元化的竞争格局，以避免单一企业的失误对整个行业造成毁灭性打击。

**微软可能改变内核访问政策**

当安全软件在内核模式而非用户模式下运行时，可以完全访问系统的硬件和软件，使其加强大和灵活，但这也意味着像CrowdStrike的错误更新可能会导致更多问题。

CrowdStrike的Falcon传感器软件由于运行在内核模式下，对系统硬件和软件具有完全访问权限，这使得其更新问题带来的影响尤为严重。相比之下，macOS最近版本已经弃用第三方内核扩展，避免了类似问题。微软过去曾尝试限制第三方安全公司访问Windows内核，但遭遇了欧盟委员会的强烈反对。微软在增强系统安全性方面面临两难困境：一方面需要加强安全措施，另一方面又需避免引发反垄断审查。

Cable指出，VBS enclave和Azure Attestation就是可以保证Windows安全而无需内核级访问的产品示例，而大多数基于Windows的安全产品（包括CrowdStrike的Falcon传感器）现在都（应该）这样做。

微软副总裁约翰·凯布尔(John Cable)在一篇博文中表示，微软已经“聘请了超过5000名支持工程师，每周7天、每天24小时不间断工作”，以帮助清理CrowdStrike更新所造成的混乱，并暗示Windows的更改可能会有所帮助，前提是不违反监管机构的规定。

**CISO对网络安全巨头失去信任**

此次事件不仅暴露了系统的技术漏洞，也引发了首席信息安全官（CISO）对网络安全供应商的信任危机。许多CISO表示，此次事件后，他们对现有单一网络安全解决方案/平台的可靠性产生了严重怀疑。这种信任危机可能促使企业重新评估其网络安全策略，并更加谨慎地选择合作伙伴。事件发生后，一些CISO甚至公开表示，他们将考虑减少对单一供应商的依赖，转而采用多重防御策略，分散采购安全工具，以降低未来类似事件对企业运营的影响。

**CrowdStrike的救赎——一张“假”打车券**

CrowdStrike在事件响应和恢复过程中犯下了诸多错误。首席执行官George Kurtz一开始否认这是网络安全事件，试图用外交辞令淡化事件，引发了公众的不满。

雪上加霜的是，CrowdStrike在事件回顾报告中虽然提出了很多切实的测试流程整改计划，但矢口否认自己有任何“不负责任的行为”，在业界瞩目的内部事件调查报告中，CrowdStrike居然将责任归咎于“意外/失误”而非“错误/缺陷”，这种低劣的诡辩，导致CrowdStrike的“品设”彻底塌方。

CrowdStrike令人吃惊的不仅仅是“无出其左”的公关能力，营销部门的表现同样“炸裂”。事件发生后，CrowdStrike向部分损失惨重的客户和合作伙伴提供的补偿居然是价值10美元的UberEats促销码，而且，据一位CrowdStrike销售代表透露，该优惠码一度被Uber判定为欺诈行为而无法使用。

最终，CrowdStrike的一系列技术和非技术性的应对措施，不仅未能有效缓解事件带来的负面影响，反而进一步损害了自身和整个网络安全行业的声誉。

**参考链接：**

https://www.linkedin.com/posts/georgekurtz\_falcon-content-update-remediation-and-guidance-activity-7222323091652108289-19Xv

原文来源：GoUpSec

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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