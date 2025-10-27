---
title: 安全人士可以从CrowdStrike事件中汲取的五点教训
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546041&idx=3&sn=a07bf08719900497d8bbb04d4aa205c3&chksm=fa938278cde40b6e298bd1da2843864cb735d28f18988dbf7cc6a0825b07a5bc609e055377ea&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-26
fetch_date: 2025-10-06T17:43:29.744729
---

# 安全人士可以从CrowdStrike事件中汲取的五点教训

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kFDuibR06fBNEhLLebAn7IBLDRN3ibqKp4Rg78gL5LV0StSFrT9JxIAHfCicxv65bOT3owrD2S2fvpA/0?wx_fmt=jpeg)

# 安全人士可以从CrowdStrike事件中汲取的五点教训

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kFDuibR06fBNEhLLebAn7IBCRCkFq1jTqHPcAeia0m7TK0jwmhjIvXbHqpDKlFzvO8GW3Lq3A03Dag/640?wx_fmt=png&from=appmsg)

CrowdStrike错误更新导致全球范围Windows蓝屏事件已经发酵数日，该事件被业内人士看作是“历史上最大规模系统崩溃事件”，震惊了整个世界。

这次事件并非是某个国家级黑客组织或大师级黑客的杰作，而是CrowdStrike更新文件的一个错误，导致包括机场、银行、政府甚至紧急服务在内的大量关键基础设施系统因蓝屏死机而瘫痪。

以下是安全专业人士从这次事件中可以汲取的五点重要教训。

**1、无需幸灾乐祸，警惕害群之马**

Crowdstrike大规模系统崩溃事件是过去几天最热门的聊天话题之一，IT和安全专业人士们热衷转发表情包嘲讽该公司犯下的愚蠢错误，但请记住，下一个出现在热搜的可能就是你供职的公司。

随着平台化和云化的深入，网络安全市场的市场集中度不断提高，任何一次失误都可能引发全球性的连锁反应。公有云的几次重大停机事故已经引发了全球性的“下云运动”，网络安全行业需要反思如何缓解过度集中化的风险，避免单个企业的失误对整个行业造成毁灭性的打击。

**2、网络攻击还是意外？**

CrowdStrike的官方声明否认该事件是“网络安全事件”或者“网络攻击”。但是网络安全的一个关键原则是可用性，从手段和结果来看，对于CIO和CISO来说，这次事件显然与一次大规模的网络攻击没有什么区别（无需支付赎金，但恢复工作仍然极为痛苦）。

“一遭被蛇咬十年怕井绳”，此次事件后，相信大量CIO都会对EDR终端代理感到紧张。网络安全行业的其他企业可能会是该事件的最大受害者，网络安全企业与客户之间的基本信任已经被击碎。现在，CISO们需要为服务器和终端上运行的每个安全解决方案重新辩护。接下来的几周和几个月里，CISO们和安全供应商之间将会有很多艰难的对话。

**3、立即对威胁模型进行评估**

过去几天经常会看到这样的肤浅言论：“我们用的是Macbook，所以躲过了一劫”或“我们不用CrowdStrike，谢天谢地！”“我们是中资企业，所以不受影响，哈哈哈。”要知道，今天出事的是网络安全巨头CrowdStrike，明天可能就是其他更拉垮的草台班子。

现代IT环境是由各种软件代理和厂商产品混合而成，单点故障几乎不可避免。评估这种情况时，我们需要扪心自问：如果我的所有Windows服务器和终端都瘫痪了会怎样？我们能转向基于云的服务吗？我们有其他可用的终端代理吗？可以肯定的是，网络犯罪分子已经看到了这次停机事件造成惊人损失，并在思考如何从中获利（最常见的操作是冒充修复工具或漏洞补丁的网络钓鱼攻击）。

**4、检查你的补丁管理流程**

永远不要在周末前或周末期间打补丁。在打补丁时，分阶段进行，而不是批量更新。可以想象，全球数百万IT支持人员会无法理解CrowdStrike这种头部企业居然会忽视这些最基本的流程。

即使微软和Crowdstrike发布了修复程序和指南，但手动修复方式对于管理成千上万台服务器/终端的IT团队来说依然是一场噩梦。再加上大多数使用CrowdStrike的公司已经加密了他们的服务器（例如Bitlocker），这让恢复工作的痛苦指数进一步上升。更不用说，基于云的服务器不能简单地进入安全模式进行修复；你必须分离存储，修复它，然后重新连接。这将是对公司灾难恢复流程的巨大考验。幸运的是，已经有许多可用的自动化脚本发布，大大提高恢复流程的效率。

如果你所在的（网络安全）公司经常发布补丁，现在是重新评估补丁管理实践的好时机！永远不要在周末打补丁，如果必须这样做，请采用分阶段的灰度更新方法，确保能随时回滚到安全状态。

**5、重新审视你的软件供应链**

软件供应链是网络安全最大的盲点之一，业界对开源代码或网络安全企业自身的产品安全往往重视不足。事实上，没有任何软件是100%从头开始制作的，大多是各种软件代码库和依赖关系的混合体。即使你无法剔除这些依赖关系，至少可以深入了解你所拥有的代码资产及其风险状况。

要知道，与监控并掌管全球数亿设备的EDR/XDR软件市场相比，Crowdstrike事件只是冰山一角。此外，开源供应链攻击和AI大模型数据泄漏的规模和损失可能会超出你的想象，任何企业，无论是软件供应链的上游还是下游企业，都需要为此类风险做好预案和防御措施。

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