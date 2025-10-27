---
title: 微软计划将网络安全厂商踢出Windows内核？
url: https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485966&idx=1&sn=d0dfab481b6da8d0f35fe3f51093d0f4&chksm=fb04c966cc734070e760d4156363d52cac17dd312f5482669927b566c19f49e680d14e54dc67&scene=58&subscene=0#rd
source: 天御攻防实验室
date: 2024-09-12
fetch_date: 2025-10-06T18:28:51.856457
---

# 微软计划将网络安全厂商踢出Windows内核？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBBXqibMicE416M9FlCV2kqfqLYGt6vTMLHMqpOIWibuB4osMziazZTxDPYibUG0byrvUlUoL04bwiaQE80A/0?wx_fmt=jpeg)

# 微软计划将网络安全厂商踢出Windows内核？

原创

天御

天御攻防实验室

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBBXqibMicE416M9FlCV2kqfqLcW8ic2reGBKygJBc1rj34lOuV6AQ7mrkBbwXG2nvTwJeD0SzE0dRnIQ/640?wx_fmt=png&from=appmsg)

2024年9月10日，在微软总部举行的Windows终端安全生态系统峰会的官方目标是，在CrowdStrike全球大规模宕机事件后制定"具体步骤"以提高安全性和恢复能力。

微软已召集CrowdStrike、选定的合作伙伴、政府代表和终端安全供应商（笔者注：前几天，在群里问了一下，国内好像没有EDR厂商参加？），就"提高恢复能力和保护共同客户的关键基础设施"进行讨论。

政府官员将到场以"确保最高级别的透明度"，微软承诺将制定"短期和长期行动与计划的下一步措施"。

活动将不对记者开放，会后将发布"更新"让我们知道达成了什么协议(或者可能是微软发布了什么命令)。

尽管我们不确定峰会上将讨论什么，但几乎可以肯定的是，围绕内核访问权限将会有所变化。

内核访问和蓝屏死机

几年前，苹果将开发者踢出了MacOS操作系统。时至今日，在CrowdStrike宕机导致850万台计算机遭遇蓝屏死机后，内核访问再次成为议程。

CrowdStrike的根本原因分析发现，宕机的原因归结为未能发现新部署的威胁检测配置与在内核模式下运行的代理之间的输入验证不匹配，这触发了越界读取。

在一份技术报告中，微软企业和操作系统安全副总裁David Weston也将宕机归咎于CrowdStrike的CSagent.sys驱动程序中的越界内存安全错误。

限制内核访问通过最小化攻击面和减少用户模式应用程序中漏洞的影响范围来增强安全性。但它也可能阻碍需要深度内核交互的合法安全解决方案(如EDR - 终端检测和响应工具)的性能和功能。

微软本身告诉《金融时报》，它"正在考虑几种选择，以使其系统更加稳定，并没有排除完全阻止访问Windows内核的可能性"。该报还指出，"竞争对手"(我们认为，如安全供应商)可能处于与Defender(微软自己的安全产品)竞争的"劣势"。

Red Canary的联合创始人兼首席安全官Keith McCammon表示，微软面临三个选择。

"它可以维持现状，引入或强制实施额外的安全措施，或者完全限制对内核的访问，"他说。"如果微软的计划是维持现状，那么它不太可能举办这次峰会，所以我们可以假设它计划宣布一项变革。"

McCammon指出，对内核接口或访问的任何更改都将对安全产品供应商产生连锁影响。供应商也将不得不改变他们的工作方式 - 特别是在试图使他们的产品在市场上脱颖而出时。

"目前，终端安全供应商的差异化部分基于他们对Windows平台的检测，包括他们使用内核驱动程序进行数据访问和威胁响应，"McCammon说。"根据微软选择的路径，这种类型的差异化可能成为过去。"

"虚拟警察国家"的冒险

如果深入内核不是你的工作，那么你可能会很高兴听到任何提供增强安全性的更新，特别是在广泛报道的全球宕机事件之后。

IT策略师Zenaciti的CEO和安全公司Anitian的创始人Andrew Plato告诉我们:"最终这将对消费者产生净收益。内核限制在核心操作系统内部创造了一种'虚拟警察国家'。"

"没有微软的明确批准(以加密签名证书的形式)，任何东西都无法运行。多年来，苹果一直限制iOS和MacOS的内核访问，这使得这些产品通常更加安全。"（笔者注：也更加不安全）

然而，任何试图将供应商锁定在内核之外的尝试都可能导致大规模的哀嚎和牙齿咬合，在最好的情况下强制软件重写，在最坏的情况下破坏长期建立的商业模式。

Plato补充说:"大多数反恶意软件产品，如CrowdStrike、Sentinel One或McAfee、360，都需要内核访问来执行安全监控功能。这意味着这些供应商需要与微软合作以获得访问权限。"

"微软可能会效仿苹果的做法，实施加密签名系统，只有获得批准的驱动程序才能访问内核。此外，微软可能需要实施方法，让最终用户能够禁用此功能，就像苹果那样。"（笔者注：微软会不会把国内EDR踢出内核？）

BeyondTrust的首席安全顾问兼多本安全书籍作者Morey Haber指出，欧洲一个著名案例将不可避免地影响微软关于关闭内核访问的决定。

"2009年，欧盟在一起反竞争诉讼中裁定微软败诉，"Haber说。"所有微软Windows API、文件和开发工具包现在都同等地提供给竞争对手和开发者，就像微软内部使用的一样。"

"这项反竞争裁决也管辖内核访问，这就是为什么CrowdStrike和其他供应商能够成功开发出与微软本身一样好或更好的安全解决方案。如果微软确实限制内核访问，它必须遵守欧盟裁决的指导原则，或者准备重新面对诉讼。"

据报道，微软本身告诉《华尔街日报》，由于与欧盟的"谅解"，它"在法律上不能像苹果那样封锁其操作系统"，该谅解给予安全软件供应商与微软享有的相同级别的Windows访问权限。

如果微软限制或减少内核访问会发生什么?

如果限制对内核的访问，微软将需要开发新的接口来促进安全监控以及目前需要驱动程序的低级操作系统功能。像eBPF(扩展Berkeley数据包过滤器)这样的技术允许沙盒程序在特权上下文中运行，包括内核。然而，虽然eBPF在Linux上常用，但它还没有跳转到Windows上。

Pvotal Technologies的首席技术官Ashley Manraj预测，微软不会"仅仅寻求意见，而是积极引导Windows版eBPF的发展轨迹"。

Manraj说:"微软可能希望提出一个受限用户输入的采用计划，重新审视他们十多年来一直坚持但在欧洲监管机构决定后未能部署的立场。它可能会为eBPF程序建立或甚至强制执行特定的开发实践、测试协议和严格的安全措施。"

"为了简化这些标准的遵守，微软可能会引入新的开发工具、测试框架，甚至专门为eBPF安全应用程序量身定制的专门运行时环境。"

微软:独裁者还是合作者?

前FBI反恐和反情报特工、安全服务提供商Nexasure AI创始人和全球安全演讲者Eric O'Neill建议，微软可能"优先考虑损害控制而不是透明合作"。

他警告说:"这些会议的闭门性质限制了更广泛安全社区的不同观点。一种更开放和包容的方法来解决Windows安全缺陷可能会带来更有效的解决方案。微软欠其用户群和整个科技社区更多的透明度。"

"限制对内核的访问对操作系统的稳定性和安全性来说是一个很好的做法。然而，安全软件需要完全可见操作系统和应用程序正在执行的内容，而在微软当前的Windows环境中，唯一的方法就是内核访问。"

"微软有办法改变这一点，但我怀疑其庞大的市场份额、遗留系统以及对强制许多依赖Windows生存的应用程序(如鲸鱼上的吸盘鱼)修改代码的担忧阻止了微软做出必要的改变。"

参考资料：

https://www.thestack.technology/microsoft-endpoint-summit-kernel/

**推荐阅读**

**闲谈**

1. [中国网络安全行业出了什么问题？](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485457&idx=1&sn=d45cc35242cdc83e98b124531ea7c093&chksm=fb04cb79cc73426f21801f35912b626bf515dc2b9d85b3da578f8087d0a2960396ef1e6347bc&scene=21#wechat_redirect)
2. [国内威胁情报行业的五大“悲哀”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484999&idx=1&sn=485863f4e66a62f55aa69334c787e6f3&chksm=fb04c52fcc734c3919fc28c61a9b13488b89efe4c1ba5cb16f8f00f0c6e996c7f1df47984463&scene=21#wechat_redirect)
3. [安全产品的终局](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484846&idx=1&sn=35bab89f917f5043919e40893268d576&chksm=fb04c6c6cc734fd05c0423dc971a0578eb8b951ef1764be0a99e2bdd1c26b736d64cf61b6d77&scene=21#wechat_redirect)
4. [老板，安全不是成本部门！！！](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485908&idx=1&sn=b6cff013a1e9a9599bdde63ce56ecec0&chksm=fb04cabccc7343aac55b3c43020c855bade147461fece597f730bc0460e65c5610dd0f5d988b&scene=21#wechat_redirect)

**威胁情报**

1.[威胁情报 - 最危险的网络安全工作](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485331&idx=1&sn=0857185a1bc7ed04c2d1edc60cb93a34&chksm=fb04c4fbcc734dede0fd243984c30250ff7859f68a265b1a278ac72a5761ac0ccaf0038537ec&scene=21#wechat_redirect)
2.[威胁情报专栏 | 威胁情报这十年（前传）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484880&idx=1&sn=c2b5730f2a7011959096526ff775c8ac&chksm=fb04c6b8cc734fae9f6d2e0693cecd5fd594a01694d8e38bd95926cb88a0f627c3d5b2f36ea2&scene=21#wechat_redirect)
3.[网络威胁情报的未来](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485003&idx=1&sn=76253d23e51dde8dbf4d675b79ab43cf&chksm=fb04c523cc734c352490ca37f55f1c3a989d55807298cb308aa3c126e24816d6fda11a8766f1&scene=21#wechat_redirect)
4.[情报内生？| 利用威胁情报平台落地网空杀伤链的七种方法](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485042&idx=1&sn=afd1212b585f30bccdece8471fadd31d&chksm=fb04c51acc734c0c9fd0d1d388b7672defbe5ce17a10af58d3a5d336ba21fa21398b4ad860e2&scene=21#wechat_redirect)
5.[威胁情报专栏 | 特别策划 - 网空杀伤链](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484709&idx=1&sn=649a27516ca01baab49ce750e3502cc3&chksm=fb04c64dcc734f5becd252686228f6c3c2bd00bff52041e9dae6fde2008e1a43057989b9d16f&scene=21#wechat_redirect)
 **APT**

1. [XZ计划中的后门手法 - “NOBUS”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485524&idx=1&sn=aa2b7b0d57b250e5cc101e5dcbebbca6&chksm=fb04cb3ccc73422a9fe22937b801eceb205ceaf8bf3b76a92143d575d55e5fd2eef5adfacb36&scene=21#wechat_redirect)
2. [十个常见的归因偏见（上）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484868&idx=1&sn=3d65e81115c967b165fa16021a211967&chksm=fb04c6accc734fba7c760fd14caaaf9a2d7991acc2557ee340e772ccbb805b30f1a46c793e8a&scene=21#wechat_redirect)
3. [抓APT的一点故事](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485237&idx=1&sn=9152fcb5f5b1f884e6da97ba9b04f69a&chksm=fb04c45dcc734d4bd8fbede2ae93dc52feeaaa11e215a3240bca32f3d43444a2c909e01a2814&scene=21#wechat_redirect)
4. [揭秘三角行动（Operation Triangulation）一](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485278&idx=1&sn=9def52d0d9063e86acb16533be2a52e8&chksm=fb04c436cc734d20b8c67348f7db21fa10921ad3826b37c713e847b73972f50de82b6c1f1e6b&scene=21#wechat_redirect)
5. [闲话APT报告生产与消费](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485325&idx=1&sn=d0219cfe811afe5e8fc8729c603de2bc&chksm=fb04c4e5cc734df3a8ad433a992172c1a9a0f236fd69550c72eb499e1202d23b81f32b379259&scene=21#wechat_redirect)
6. [一名TAO黑客的网络安全之旅](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485451&idx=1&sn=5f794deaaccf45e7d81958eba82cd556&chksm=fb04cb63cc73427538546f24b1be7cd78375a9017498efb3fd2da46de5c38c0d4599c2e01100&scene=21#wechat_redirect)
7. [NSA TAO负责人警告私营部门不要搞“黑回去”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485250&idx=1&sn=a35def8b58f86f8a149e335f3df3a1c9&chksm=fb04c42acc734d3cdfd1e8f2ae852731c3569533ab8fa83bd0126b788ea20673a2f912cdf011&scene=21#wechat_redirect)
8. [我们为什么没有抓到高端APT领导者的荷兰AIVD](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485961&idx=1&sn=4853510858376f0e417b352dba02b5a3&chksm=fb04c961cc734077f68ebb17906c57cd19657ab24eb9d5a4a436d66ecbfd2dc370def58b5714&scene=21#wechat_redirect)
9. [抓NSA特种木马的方法](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485892&idx=1&sn=c04d398e85fd4ad28b7bbf714b1c9153&chksm=fb04caaccc7343ba99536892e2e3bb654867c4b5e64813a8ee69082e61de161c38ced94239c6&scene=21#wechat_redirect)

**入侵分析与红队攻防**

1. [入侵分析与痛苦金字塔](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485464&idx=1&sn=f05718bec99d4506a8fe1c49dc2bf337&chksm=fb04cb70cc734266a436d4225d4eb0486becaed5f0258748e6ff3de46a22caaa01b0da1b0e4f&scene=21#wechat_redirect)
2. [资深红队专家谈EDR的工作原理与规避](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485494&idx=1&sn=f45125e76dd412a291cfa3bccd5943c5&chksm=fb04cb5ecc734248332218f7df17be9a31d4b09777b8cd846b69821248a5e75b44baa6bfbfe4&scene=21#wechat_redi...