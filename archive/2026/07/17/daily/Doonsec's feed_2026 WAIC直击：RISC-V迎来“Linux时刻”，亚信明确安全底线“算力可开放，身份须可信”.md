---
title: 2026 WAIC直击：RISC-V迎来“Linux时刻”，亚信明确安全底线“算力可开放，身份须可信”
url: https://mp.weixin.qq.com/s/qb9N4-f-tQxcwF8sKP0SkA
source: Doonsec's feed
date: 2026-07-17
fetch_date: 2026-07-18T04:40:27.169482
---

# 2026 WAIC直击：RISC-V迎来“Linux时刻”，亚信明确安全底线“算力可开放，身份须可信”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YUnWCyLjbun0z6p41UibXRqFZJLoxmbrpEQovMM0TZlw0RYiaoK1GezC3ZPmxCRbWMja17z7uDFluL3YMr8lfFibNSvy2wxEcQYgjPNb9IMYro/0?wx_fmt=jpeg)

# 2026 WAIC直击：RISC-V迎来“Linux时刻”，亚信明确安全底线“算力可开放，身份须可信”

你信任的
你信任的

亚信安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

7月17日，2026世界人工智能大会暨人工智能全球治理高级别会议（WAIC 2026）在上海正式启幕。本届大会以“以共商促共享 以善治促善智”为主题，汇聚全球顶尖智慧，全方位展示人工智能领域的最新突破与前沿治理范式。亚信出席本次盛会，直击AI与智能体互联网时代的硬核关切，围绕Token运营、超级数字员工、数智本体以及AI与智能体安全，分享前沿理念观点，并全方位展示创新应用成果。

![](https://mmbiz.qpic.cn/mmbiz_jpg/YUnWCyLjbulXwRibv4h19UzQjv4UwibiauyHbg05QtTwYsJRjlWLbIMgccKv5y5AN8Y8UyYoXMrtdYY1gPJafQFYdF39cW9IO5RxQNrCvlBdlc/640?wx_fmt=jpeg)

17日下午，由国家互联网信息办公室、中国科学院主办，中国网络空间安全协会、北京开源芯片研究院承办的“RISC-V与AI融合发展分论坛”隆重召开。论坛邀请了RISC-V领域的院士、科研院所专家及知名企业家，共同探讨如何从指令集层面更好地支持AI训练与推理，提出协同演进的新路径。亚信出席活动，亚信安全高级副总裁付廷升受邀参加论坛圆桌对话环节，与多位行业顶尖专家同台，就RISC-V芯片进入AI算力基础设施所带来的全新安全挑战，以及安全产业如何协同构建健康生态，分享了前瞻洞察与亚信安全的创新实践。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YUnWCyLjbuk07uLKJEJ5J1v66F7PWWXN5jCkiaQocDUtzOZLNmwBxianJ5t8CtEckGDgITsKHDSatU9ViaxddEhPibSUW4dpoRA3ZFafrwUOiblU/640?wx_fmt=jpeg)

**RISC-V正在迎来属于它的“Linux时刻”**

当前，RISC-V凭借开放、灵活、可扩展的优势，正在成为智能计算的重要技术路径。在圆桌对话环节中，与会嘉宾围绕AI算力基建的巨大变化展开讨论。针对安全行业对RISC-V新架构的高度关注，付廷升表示：“行业的关切已经从‘要不要看’变成了‘怎么看、怎么跟’。 在产业层面，我们已经接收到了几个非常明确的标志性信号：今年SiFive的RISC-V CPU已经通过NVLink Fusion实现与NVIDIA GPU的直连；如进迭 K3 等首批符合 RVA23 标准的开源架构芯片，标称可运行 300–800 亿参数的高性能大模型；同时，目前Ubuntu、Fedora 等主流开源操作系统已实现全面支持并持续深化，开源软件生态正加速向 RISC-V 靠拢，业界常把这一刻比作RISC-V的‘Linux时刻’。”

![](https://mmbiz.qpic.cn/mmbiz_jpg/YUnWCyLjbuloa8w8sJRy242Lic6PJ86J5zMuRdRXmO7xpZngb778Giby320ZnwksEbtRlDYSicwCVe9tib1ZSqWCclIKh1g5caTSvlamuianWadI/640?wx_fmt=jpeg)

**亚信安全硬核输出：算力可以开放，信任不能开放**

在产业加速爆发的同时，开源算力基础设施底座的快速更迭，也给安全防御体系带来了全新的变量。如何应对繁荣背后的安全挑战，成为了产业协同发展中不可回避的关键一环。

**挑战一：开放定制是双刃剑，安全验证复杂度呈指数级上升**

RISC-V最大的优势在于开放可定制，但站在安全角度，这恰恰是最大的变量和风险根源。x86和Arm作为封闭架构，其安全建立在统一的“硬件信任根”之上。而RISC-V开源意味着其设计对攻击者完全“透明”。当每个人都能定制指令集时，意味着每颗芯片的信任锚点都不一样，安全验证的复杂度正在呈指数级上升。

**挑战二：AI负载引入物理与逻辑层面的全新攻击面**

模型权重是端侧最有价值的资产，而它恰恰暴露在开放的架构上。在物理层面，侧信道攻击可以通过功耗、电磁、时序等无形方式窃取核心参数；在逻辑层面，公开研究已证实，仅需一个时钟毛刺，就能将开源RISC-V内核的合法指令篡改为非法指令，从而直接改变AI的推理结果。

**挑战三：上层安全产品脱节，生态协同亟待加速**

目前，整个产业在讨论“RISC-V+AI”时，关键词往往集中在性能、生态和工具链上，安全往往被置于最后。相比x86和Arm成熟几十年的TEE（可信执行环境）与安全固件体系，RISC-V的安全生态仍处于早期阶段，芯片层安全原语虽多，但上层安全产品尚未完全跟上。

基于这些痛点，付廷升指出：“当每个智能体都跑在‘信任锚点不统一’的芯片上时，唯一的解法是让身份和行为本身成为信任的锚点。算力可以开放，身份必须可验证。”

为此，**亚信安全在今年率先布局，发布了智能体身份安全系统，并推出了业界首款ATF（ Agent Trust Fabric）智能体信任框架。**该框架的核心在于为每一个AI智能体签发一张可验证的数字身份证，从源头上解决信任链破碎的问题。同时，亚信安全也已联合三大运营商和阿里云，共同发起了“智能体原生安全产业共同体”，通过产业合力加速行动。

**亚信安全：致力于成为RISC-V生态的“安全连接器”**

对于安全在RISC-V生态协同构建中的重要作用，亚信安全认为，RISC-V生态的繁荣绝非单打独斗可以实现。亚信安全未来将重点从三个维度与生态深度协同：

* **标准协同（Security by Design）：**亚信安全将积极倡导将“智能体身份安全标准”注入到RISC-V基金会的相关安全工作组中，让智能体的身份标识、鉴权协议成为芯片设计的标准语言。
* **能力开放（基因注入）：** 亚信安全愿意将自身在“智能体身份安全”上的核心能力，无保留地向RISC-V芯片厂商和IP提供商开放，在芯片出厂、固件刷写阶段就注入安全的基因。
* **应用协同（样板间打造）：** 联合产业链上下游，在智能汽车、工业控制等关键领域共同落地“基于RISC-V + 智能体身份安全”的端到端行业标杆方案。

面对“RISC-V+AI”的历史机遇，亚信安全将致力于发挥“安全连接器”的作用，通过标准协同、能力开放以及应用协同，向上连接芯片厂商，中接工具链与操作系统厂商，下接行业用户，共同构建端到端的可信生态体系。

在开源与AI交汇的新浪潮下，让RISC-V高效释放AI智能体的算力价值，让安全能力切实守护智能体的行为边界，产业链上下游的紧密协同，将是推动“RISC-V+AI”行稳致远的关键基石。

**往期推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YUnWCyLjbunKrocjUYib0klk5IJLS01EydUG9txJdicnyEibK8fQicE4EcyNx9sicjKttGjUiaAklbBlia5x7mWxFkLmXeWo1rFb6VAI3BiaGwic3ZjQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631938&idx=1&sn=8b8b4a390c11eb376ecf33336038df9b&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631938&idx=1&sn=8b8b4a390c11eb376ecf33336038df9b&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YUnWCyLjbukic9ZL42OHJ2vAJDribtETgHQfplT2ib1ScM94TCMJF7biahmGib6LwHDMic62vLU71ia7Sq5jRvibJWhQ1cg8m3ePJmayKOxmjNpT0yk/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631281&idx=2&sn=c7f0130ebef075eed470a3f40c8b2fc8&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631281&idx=2&sn=c7f0130ebef075eed470a3f40c8b2fc8&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YUnWCyLjbulZmz0fbgjAMwibAcibsYZfZibRuZgXGiaCswtXG5jn2WM4KmqKqcZLRkvxlGV50qwG3OQUJ2ibrYMwIQ2yqSFOMrW3IyBaIrEIxQ2I/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631675&idx=1&sn=7a152477ddaab4285e27a869dbbb7fe7&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631675&idx=1&sn=7a152477ddaab4285e27a869dbbb7fe7&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YUnWCyLjbuklzSjFOd7scAda6AMtlkrJvgRQw0RnXAvs4YtU2QyNZlCwgImsTg2ianknoostKZBaEbDibczAETYcQPGnicFeibel42415giaKLcs/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631281&idx=1&sn=f4cf251ecd044970aad4afaf82a4bdc4&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631281&idx=1&sn=f4cf251ecd044970aad4afaf82a4bdc4&scene=21#wechat_redirect")

了解亚信安全，请点击**“阅读原文”**

**求点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0FZMB3vsw4wxyNMbXwC42FoG8KmicxOYyR9Em8f5BFRia2jia66l1HibEyCKXqUq6bGLUCj7uDtZS58pg/640?wx_fmt=gif)

**求分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0FZMB3vsw4wxyNMbXwC42FoHFSQRwicdBWfDiaNibTtUyQ2lPiaicDV5pZaUgZTzY3TJQ3ZbmR1Tj5iciaYg/640?wx_fmt=gif)

**求喜欢**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0FZMB3vsw4wxyNMbXwC42FoAV9dDSmbcAxOs8iaCgcpDEBjGNObDFpgTXjZSyjr9DzTgMblPrUYILA/640?wx_fmt=gif)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iczzp36h0nbHibibbM15ufBwzEl7XmKf0qYkQWrLy6Kib3bicyrLrH8tGx9p996AKQPT93mOcicjK8mzibsV2yVyU6puA/0?wx_fmt=png)

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