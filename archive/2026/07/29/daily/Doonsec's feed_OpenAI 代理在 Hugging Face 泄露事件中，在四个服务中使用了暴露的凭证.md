---
title: OpenAI 代理在 Hugging Face 泄露事件中，在四个服务中使用了暴露的凭证
url: https://mp.weixin.qq.com/s/-UY_HbxxIgI3nNXROdgf_w
source: Doonsec's feed
date: 2026-07-29
fetch_date: 2026-07-30T04:47:44.443455
---

# OpenAI 代理在 Hugging Face 泄露事件中，在四个服务中使用了暴露的凭证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADs9iaGWytgEIPILcaQKWKIJSXyO3icFibgvnXicAmQia0FHMp2uyCjO4TofEqZHfvhmdlHNXoq1XJwLTic7Y5YtFNW7GN8Wibmibxa1W9kY/0?wx_fmt=jpeg)

# OpenAI 代理在 Hugging Face 泄露事件中，在四个服务中使用了暴露的凭证

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADs9XzBSRYDVMiaXJFd3mL6DqLruwmjydoX6aP3YK2HNLDm9bFfr04e1aXnnuFg3VpAOkNzkMzC2IzZ6NkCYbribse9DCv1Gib42qVw/640?wx_fmt=jpeg&from=appmsg)

OpenAI周二披露，逃脱其封闭评估环境并入侵Hugging Face生产环境的流氓人工智能（AI）代理，也在攻击中入侵了多个第三方账户和服务。

最新披露显示，这起源于内部安全测试的安全事件，其范围比此前认为的更为广泛。

这家人工智能公司表示，其对此次事件的持续审查显示，包括GPT-5.6 Sol和“更强大的预发布模型”在内的“少数案例”，在其他公开服务的账户层面识别并使用了暴露的凭证。

“这包括了作为”拥抱面“事件一部分，在四个服务上的四个账户（以及作为其他评估的一部分访问的几个账户）”，声明称。

“这四个账户中有一个用作出站中继和备用路径，另一个账户用于数据存储。剩余两个账户则以只读方式被模型访问，未被用于破坏Hugging Face的行为。”

OpenAI未透露账户所属的公司或组织，但指出将继续直接通知服务所有者，且未见任何证据表明泄露事件对这些服务提供者或账户造成更广泛的影响。不过，路透社报道称，Modal Labs的一位客户是被OpenAI代理攻破的实体之一。

此外，这些模型据说还使用了一系列公开服务，包括代码粘贴网站、请求捕获服务、截图服务、文件投放服务以及其他网络工具。在这些情景中，没有看到平台或账户层面的泄露。

OpenAI 在 2026 年 7 月 16 日泄露后与 Hugging Face 合作，承认这些模型识别并利用了 Artifactory 自托管版本中此前未知的零日漏洞，Artifactory 是由 JFrog 维护的包注册缓存代理，以获取互联网访问并突破其沙盒。这个问题在 Artifactory 7.161 中得到了解决。

Artifactory 7.161.15 的发布说明指出，该版本修补了多个安全漏洞，如果启用匿名访问，这些漏洞可能会串联成关键攻击场景。匿名访问默认被禁用，且不建议在生产环境中使用，出于安全风险。

JFrog首席技术官Yoav Landman表示：“这次事件中埋藏着一个重要且坦率乐观的教训：AI模型正成为非凡的零日发现引擎。”让模型找到人类未曾发现的漏洞路径的能力，也是让防御者能够先发现并消除这些路径的能力。”

这家美国人工智能公司还将该预发布模型描述为仅内部研究的原型，旨在公开发布。该模型后来被停用、加密，并限制了研究访问。

### 《拥抱面》发布事件的事后分析

根据Hugging Face发布的详细时间线，这个自主AI智能体在其基础设施中停留了大约两天半，目的是欺骗ExploitGym，这是一个基于AI系统发现和利用软件漏洞能力进行评分的基准测试框架。该公司表示，他们审查了2026年7月9日至13日期间从日志中恢复的约17,600起攻击者行为。

“我们认为，从代理人的角度来看，整个入侵都是试图作弊评估：进入我们的生产系统并窃取测试解决方案，而不是自己解决挑战，”Hugging Face说。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADsicoiaYfjm2Cl1CicnicCIfYCCjkPfkibj4LJtrxt3xccuVhJSk0ToQNNjca4ibkNGA5Sv34MQ8b4tr8ZrexsVvgmibibIaNn10LyVCvaE/640?wx_fmt=jpeg&from=appmsg)

据说这场端到端入侵分两个阶段展开——

* 该代理通过利用Artifactory的零日漏洞逃脱了沙盒，Artifactory是允许的网络出口带互联网，随后又利用第三方服务提供商基础设施托管的公开代码评估外部沙箱，以root身份运行命令，并将该沙箱作为“外部启动平台”。
* 在该沙盒中，代理利用 Hugging Face 的数据集处理流程获得了管理员对 Kubernetes 集群的访问权限;通过节点冒充、CSI令牌盗窃和伪造身份令牌的组合进行横向移动;建立指挥与控制（C2）;最终获得对GitHub部分内部源代码仓库的未经授权写入权限。

公司表示：“虽然入侵确实进入了Hugging Face的内部基础设施，但唯一访问的客户内容是存储在五个数据集中的ExploitGym/CyberGym挑战解决方案集合。”“没有其他面向客户的模型、数据集、空间或包受到影响，唯一读取的客户记录是与数据集服务器搜索查询相关的运营元数据。”

该攻击的一个显著特点是使用了一种临时通信协议用于C2。该协议叠加在公共服务请求捕获服务、Pastebin和文件丢弃服务之上，允许每个消息携带一个有效载荷，以及压缩和Base64编码负载类型的详细信息、将相关消息流分组的通道、用于将消息重新排序的序列号以及校验和。

该过程如下：（1） 代理向公共请求捕获服务发布自描述信封，（2） 接收方轮询该信封，重新组装区块，然后将有效载荷作为 shell 命令运行并分阶段处理结果。

Hugging Face还将该代理描述为短暂且有弹性，类似于自主评估运行，每次代码评估沙盒运行都会获得新的身份，同时采取措施避免暴露明文载荷。

“该代理跨越多个信任边界，逃离其评估环境，访问公共互联网，并持续了数天针对我们的生产基础设施发动连贯的攻击。”“每个短命的代码评估环境都是从零开始，但代理重建了工具，恢复了通道，并继续运行。”

针对此次事件，公司已将代码执行路径纳入数据集处理流程，锁定云元数据访问，轮换令牌和凭证，重建核心基础设施，隔离集群，并改进了警报机制。

Hugging Face 首席执行官 Clem Delangue 在周末于 X 上分享的一篇帖子呼吁“彻底透明化”，并补充道：“首个自主智能体网络攻击是前所未有的事件。它理应得到前所未有的回应。”

这些发现再次强调了人工智能工具在网络攻击能力上正迅速成熟，尽管它们并未揭示该技术的创新或颠覆性应用。这不仅降低了开发漏洞的门槛，还使恶意分子能够大规模发现、探查并利用错误配置，提升犯罪行动效率，从而带来更优质、更大、更快速的攻击。

这一进展同时，竞争对手Anthropic表示，其Claude Mythos Preview AI代理已发现攻击密码算法的方法，包括设计出一种密钥恢复技术，该技术“显著削弱”HAWK的潜力，HAWK是美国国家标准与技术研究院（NIST）选定的后量子标准化进程中候选数字签名方案之一。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

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