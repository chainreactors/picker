---
title: 一周4500万次攻击，全球wp2shell漏洞遭大规模利用
url: https://mp.weixin.qq.com/s/zh0szU9aOLkehqMBfvMBgg
source: Doonsec's feed
date: 2026-08-24
fetch_date: 2026-08-25T02:58:19.935929
---

# 一周4500万次攻击，全球wp2shell漏洞遭大规模利用

# 一周4500万次攻击，全球wp2shell漏洞遭大规模利用

e安在线
e安在线

e安在线

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9lficfxbMRL57Mbt28cBfGWoqEJk4icUBMRmEtfNFdibu0qiaSDofWibNxZW9d3libasHDibk3yVGDZ5cqSX9NSy43AwFLn43OiaKFAHQQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9m9V1GiacqeziaQIMria5sS6ic9ernA5n5TDXaBRoMYZkVPBFUBkT9651VOM3d6DGniceFs7FtiaPflmshMib2VPS0BKz6rDxhtYBDpuk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9mjjxDD2DTIaCF2h5ia4xYI8G8Z0z2yuPLrwJJPXauaDjPsricEQ9Uyez6qdN5FXsh5dKIaRNYz59mgesj3KicA8IZt5ySy0G2ItI/640?wx_fmt=png&from=appmsg)

**Wp2shell漏洞披露后首周即遭大规模利用，攻击者从近15万个独立网络来源发起超过4500万次攻击尝试，规模约为Drupalgeddon同期的20倍，显示漏洞武器化速度正在明显加快。**

**传统按天或按周推进的补丁流程已难以应对当前攻击节奏。安全团队需将响应窗口压缩至小时级，并结合WAF、网络分段、容器隔离和实时遥测，在补丁完成前降低暴露**

**风险。**

最新的wp2shell漏洞是WordPress历史上最大的安全事件之一。这一严重漏洞链结合了两个缺陷，使得未认证的攻击者能够利用存在漏洞的网站，最终远程执行恶意代码，甚至有可能完全控制这些网站。

在漏洞披露后的第一周内，攻击者从近15万个独立网络来源发起了超过4500万次漏洞利用尝试。随着攻击数量持续攀升，我们看到了漏洞披露转化为大规模利用的速度有多快。相比之下，这一规模大约是Drupalgeddon事件期间的20倍，充分展示了自动化攻击能力的大幅提升。

经历此次事件之后，我们不应只关注漏洞本身，更应关注防御者在漏洞披露与大规模利用之间所拥有的时间已经所剩无几。安全团队必须摒弃那种围绕数天或数周评估与修复周期构建的漏洞管理流程，这条时间线已经不再准确。他们现在需要为以小时计的响应窗口做好准备。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9lwiaxn5WicoVRkVyVlj5icOerHDxmAZnyp3iaG2Aqp4pPUevBOuu0sRBicFbabibERgZ1WP49JUm5fGbFgCLw6uLv0eJrKx4yNiaRtLg/640?wx_fmt=png&from=appmsg)

**大规模利用不再需要精确定位**

这次攻击揭示了现代攻击者的诸多行为特征。一个关键的迹象是，攻击者不再花时间在行动前仔细识别存在漏洞的环境。

在此次事件中，我们观察到自动化wp2shell扫描使用相同的WordPress特定URL模式攻击Drupal环境——这些网站从一开始就根本不可能受此特定漏洞影响。

这是一个颇有深意的细节，因为它表明这种扫描并非经过精心筛选，也不是由侦察驱动的。攻击者只是将扫描请求不加区分地倾泻向互联网上任何可访问的目标，URL模式本身就是唯一的“定位”手段。在这种攻击规模下，失败的请求对攻击者来说几乎不构成任何成本。这从根本上改变了漏洞利用的成本收益逻辑，从“先识别，再攻击”转变为“广泛攻击，再筛选有效目标”。

虽然漏洞利用自动化并非新鲜事物，但当今的AI（人工智能）和LLM（大语言模型）有可能进一步压缩这一过程的某些环节，例如帮助解读漏洞披露信息、改编PoC（概念验证）代码、生成载荷变体或排查脚本问题。安全负责人已经看到AI在合法安全工作中发挥着战斗力倍增器的作用，而同样的成本收益逻辑也适用于攻击者：重复性的技术任务正变得能够以更快速度和更大规模完成。

不过，AI并不是这次攻击规模如此巨大的唯一原因。安全团队应当基于“新漏洞被武器化的速度比以往任何时候都快”这一前提来开展工作，无论攻击者具体使用何种自动化工具。

各组织不应再想当然地认为，默默无闻、平台差异或攻击者缺乏兴趣能为自己争取到宝贵时间，因为此次事件恰恰证明了情况正好相反。

**缓解措施不等于漏洞修复**

打破漏洞利用链并不一定意味着底层漏洞已经消失。例如，基于容器的隔离和运行时控制可以阻断攻击链中的远程代码执行组件，即使某个漏洞正被大规模积极利用，也能显著降低潜在影响。然而，在应用程序级修复和更广泛的网络防护措施全面实施之前，未打补丁的应用程序可能仍然容易受到攻击链中其他组件（如SQL注入）的攻击。

基础设施防御措施，例如容器化、网络分段、WAF（Web应用防火墙）规则和边缘控制，可以提供关键保护，但它们应被视为为防御者争取时间的多层防线，而非打补丁的替代方案。任何单一防护措施都不应被指望承担全部防护责任。纵深防御的目的在于，当某一控制措施失效或只能阻断攻击的某个阶段时，还有另一道防线挡在攻击者与系统完全沦陷之间。

这一差距之所以重要，是因为在如此重大的漏洞披露之后，补丁的采用从来都不是一蹴而就的，也不是均衡推进的。在初始修复发布数周后，我们看到的情况仍然参差不齐。一些组织在几天内就完成了修补，而另一些至今仍暴露在风险之中。

正是这种长尾效应，让补偿性控制措施充分体现了其价值，因为它们正是介于缓慢的补丁周期与正在发生的入侵之间的一道防线。

漏洞披露与大规模利用之间的时间窗口正在不断缩短，因此各组织实际上可能无法立即修补所有受影响的应用程序。这正是架构如此重要的原因——良好的架构应当限制攻击者在披露与修复之间的空窗期内能够造成的损害。

就防御而言，目标并不是削弱打补丁的重要性，而是要防止一次遗漏或延迟的补丁立即演变成大规模入侵和全面攻击。

**漏洞管理需要跟上攻击者的速度**

在传统的漏洞优先级排序中，我们通常会看到严重性评分、资产关键性和计划性补丁窗口。虽然这些因素仍然重要，但漏洞已被积极利用这一事实应当从根本上改变考量方式。

对于面向互联网的关键漏洞，防御者应迅速判断：

* 漏洞利用是否已经达到不容忽视的规模。
* 现有控制措施是阻断了整个利用路径，还是只阻断了其中一个环节。
* 哪些系统仍然暴露在外，哪些补丁需要绕过常规维护周期紧急部署。
* 除了组织自身环境之外，托管服务商、云、CDN（内容分发网络）或安全提供商的遥测数据还能揭示哪些信息。

有效的响应还取决于将安全运营团队实时观察到的信息与环境中所设计的整体安全态势关联起来。遥测数据告诉防御者正在发生什么；架构则决定这些活动实际上能造成多大的损害。

对于单个网站所有者来说，他们可能只会看到少量可疑请求，而运营着广泛基础设施的托管平台则可以将这些相同请求识别为一场协调一致的全球性攻击活动的一部分。就我们而言，这种可见性让我们得以部署蜜罐环境，捕获真实的漏洞利用样本，并研究攻击者在入侵后究竟试图实现什么目标。这种模式在单一网站的视角下几乎不可见，但从整体来看却一目了然。

在防范攻击企图造成大范围破坏时，这种合作关系极为重要。

关键还在于让这种响应具有可重复性。安全团队应在下一次重大漏洞披露之前就制定好紧急漏洞响应流程，包括谁有权批准紧急补丁、哪些补偿性控制措施可以立即部署、以及哪些证据会触发升级响应。重大漏洞披露之时绝不是开始定义这些角色和流程的时机。

**漏洞小时级响应**

4500万次针对wp2shell漏洞的利用尝试，只是对未来局势的一次预览——随着技术越来越智能，攻击者的速度也越来越快。

但需要明确的是，未来并非每一个CMS（内容管理系统）漏洞都会产生数千万次的利用尝试。真正的要点在于，我们应当假定攻击者拥有所需的自动化和基础设施，几乎可以立即在数量庞大的系统中测试新披露的弱点。速度固然重要，但仅靠速度永远不够。

为了做好应对下一个重大漏洞的充分准备，安全团队应将快速修补与能够遏制漏洞利用的架构、可快速部署的基础设施级控制措施以及遥测技术相结合，从而及时识别漏洞何时已从理论风险演变为实际的攻击活动。

漏洞披露曾经为防御者赢得先机。而如今，它也越来越多地成为攻击者的发令枪。那些以这种方式看待漏洞披露的组织，将在下一个wp2shell出现时依然屹立不倒。

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9k0pmxmiaQBMEnhdGPARGqXKRu5AmUr4rQ8XaGU3dNjRlYgGxJ9IBsPkf8hTFmoo1ZSb2BLiaDIJ3ngU2UCpC61Y7ibajWcBBp7icM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9kua6NCic0S7Jdn6g7zvhyjNTLodkT3AEW1fsMCSCrBgQD05qc5YbWiaEbzsbTbZ3OliaicP5CicOcShaAOex0Z4xqyTK5AnV6xbrRk/640?wx_fmt=png&from=appmsg)

声明：除发布的文章无法追溯到作者并获得授权外，我们均会注明作者和文章来源。如涉及版权问题请及时联系我们，我们会在第一时间删改，谢谢！文章来源：FreeBuf

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9mbAlHVPjL9CVyvINgjnPSyB05UAXwoRs77ye6aMHuPicpKrqDDCYpBPahCV5CHibMLJHZKe5bUQjJvBXwmKd0iavIiaMLtHB35RRg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9kjdas46oR1ibaQNN5Z1LZrGxicOvLu8GF6xDy7TWOrTScDYUS2cy7A9s4IKh2bepo0OFYLnMB7KzOibNEvzLRMZSg0tNGspDBFH8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9kF4nt7W7O8O3Oib0dQVGVLIwwJDJ9Y2G3yicqNoASL1E4giatIQCaROpYNibNywMUSe7OFGY1wXJa95NYzYZiatDy2ZOd0dbTCc358/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1Y08O57sHWiaro9eC87veL2BfoUwAjnOfbTbGQwSaaunoz9m7KFdFkib1pMyMoNY4tVtskNSHickKmn7Nza8WGTeA/0?wx_fmt=png)

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