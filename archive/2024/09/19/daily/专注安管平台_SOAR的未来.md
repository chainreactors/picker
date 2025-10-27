---
title: SOAR的未来
url: https://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484818&idx=1&sn=1966e121ac2e4f4dacda712854534d0c&chksm=fa002f26cd77a630d390f0d1c8e8456f22f6f19289dc79da7c0b70ef0489c0e8fc23022a95cf&scene=58&subscene=0#rd
source: 专注安管平台
date: 2024-09-19
fetch_date: 2025-10-06T18:26:27.365287
---

# SOAR的未来

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t7v7zyOTkMdGGBNqwIOIXXkLzRcrxicgT5iaCib3RhbA18mAqLCGubGW64ZrsuRXEnx0VoSibS4kJpiagUcRysJSbhA/0?wx_fmt=jpeg)

# SOAR的未来

原创

Benny Ye

专注安管平台

**Gartner一句“SOAR已过时”引发热议**

2024年7月底，Gartner发布了2024年度的安全运行（SecOps）技术与服务成熟度曲线（Hype Cycle）。报告中，Gartner正式表示SOAR“已经过时（obsolete）”，进而在业内引发热议。

*之前主打SOAR现在改打“安全自动化”的厂商Swimlane的CEO James Brear在X上表示：“任何有关SOAR已死的提法都是我听过的最愚蠢（dumbest）的事情——绝对愚蠢（absolutely asinine）”*

*IBM产品管理副总裁及SOAR产品Resilient（被IBM收购）的联合创始人Ted Julian在Linkedin上愤怒的表示：“鉴于Gartner正在取消SOAR，我要……取消Gartner”。Ted更是直言Gartner的分析和业务模式已经过时。*

而针对Ted在Linkedin上的发言，有人赞同有人反对。有人表示，这对于正在进行下一代SOAR（AI SOAR）创业的公司来说是一个打击【笔者：换个名字不就好了】。

*D3 Security的一位产品市场经理表示，尽管Gartner将SOAR归为过时产品，并且出现了一些不再使用SOAR缩写的新SOAR公司，但SOAR市场仍在增长，并估计每年有超过10亿美元的交易，这说明SOAR有市场。*

这类声音的核心意思是认为SOAR技术依然存在，虽然遇到很多问题，但依然有其市场空间，并且还在不断改善和演进。

还有不少公司也在官网博客上发表观点，赞同Gartner的观点，并为自己的产品打Call。

*号称下一代SOAR（超级自动化）的厂商Torq表示，“SecOps专业人员对过时的、传统的SOAR产品深感不安”，“基于GenAI的安全自动化是现代企业的发展方向”，然后表示自己的产品代表SOAR的未来。*

*标榜“安全自动副驾”Blink表示，“SOAR已经过时”，“网络安全的重点显然正在转向更先进的自动化工具，尤其是那些由GenAI驱动的工具”。*

*StrikeReady的首席客户官表示，“SOAR就不是一个产品类别”，“作为一个功能集合，它早就失败了”，然后就给自己的产品打Call。*

网络上，还有很多“XX已死，XX永生”的言论。

*Google云安全首席营销官及前Siemplify首席营销官Nimmy Reichenberg则表示赞同Gartner关于SOAR已经过时的提法，认为SOAR已经是大多数安全运营平台的一部分，不再值得作为独立产品类别了，就像以前的UEBA那样，并不是说不需要SOAR了，而是演变成了大平台的功能。*

*Exabeam首席战略官及前Gartner分析师Gorka Sadowski发表了一篇题为《SOAR已死，SOAR永生》的文章，提及了SOAR的起源、繁荣和当前遇到的困境，表示SOAR就跟UEBA一样，作为独立市场基本消失，更多融入到了其它市场（譬如SIEM）中。他写道：“是否还需要独立SOAR工具？有时需要，但更多组织可以利用他们技术栈中已有工具的SOAR功能，尤其是SIEM和CloudSec工具。”*

**Sumo Logic的Field CTO Chase Clawson表示，SOAR功能已经迁移到各种安全产品之中。**

在Linkedin上也有不少类似的声音。其核心思想就是说，SOAR技术本身并未过时，SOAR还是很有价值的，否则为什么Gartner的这份Hype Cycle依然详细分析了SOAR技术，并明确给出了他的价值，以及用户应该如何选购SOAR的建议？Gartner想要表达的主要是独立SOAR市场已经过时了。

**对于SOAR已过时的论断，各位读者怎么看？欢迎参与小调研，或者留言交流。**

**在深入讨论SOAR是否已死之前，让我们先回顾一下SOAR的发展历程，当前面临的困境和市场格局，以及发展趋势。**

**SOAR的发展历程**

Gartner在[2015年发明了SOAR这个术语，并在2017年正式确立了现代SOAR的定义](http://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484584&idx=1&sn=ec647bae8b71e4f2a4d68603b8aade00&chksm=fa002e1ccd77a70ae712591a9b745f5dd4f82aee5fe7959fd63e6ef641e5d5d7952576cf5309&scene=21#wechat_redirect)。

目前，SOAR的最新定义是：

SOAR是一个将事件响应、编排和自动化以及威胁情报管理功能组合成的单一解决方案。SOAR 工具可用于许多安全运营任务，例如记录并实施流程，支持安全事件管理，向人类安全分析师和操作员提供基于机器的协助，以及更好地实现威胁情报实战化。

根据Gartner的定义，SOAR是包含安全编排与自动化（SOA， Security Orchestration and Automation）、安全事件响应平台（SIRP, Security Incident Response Platform）和威胁情报平台（TIP, Threat Intelligence Platform）的三合一解决方案，主要旨在解决安全运营（SecOps）的事件响应环节的自动化和闭环，捎带进行自动化的威胁情报管理与利用，后来又发展到可以自动化处理安全运营各个环节的任务。

在SOAR之前，安全运营人员先是借助自定义的脚本实现原始的自动化，后来又借助IT运营自动化工具，以及RPA等面向跨系统工作流程的通用自动化平台。而SOAR正是基于之前这些实践基础上专门面向安全运营的自动化技术。

在SOAR技术处于Gartner技术成熟曲线炒作高峰的那段时间，人们对SOAR的期待很高，给人感觉SOAR自动化能力“没有上限”。

**SOAR面临****的困境**

随着SOAR实践的深入，SOAR暴露的问题也越来越多。

首先，人们再次认识到安全运营作为一种人、技术和流程相结合的产物，不存在技术上的银弹。SOAR技术也一样，它严重依赖组织的安全运营流程和规程，需要投入资源进行剧本的设计与开发，并要持续投入。人们发现，对于中小型组织或者安全运营成熟度不高的组织而言，上SOAR的投入产出比可能不高。

其次，基于预置剧本的编排更适合那些机械式重复的、相对简单和固化的工作任务的自动化。对于一些复杂的、时常变化的工作过程，采用剧本编排则很容易陷入无止尽的开发、修改过程之中。而不幸的是，网络安全领域的攻防变化太快，响应过程分支情况太多。

再次，与各类第三方系统和工具的对接和集成也成为了制约SOAR发展的瓶颈。

**SOAR的演进**

为了应对上述挑战，SOAR厂商们也在尽力改善。当前，所谓的“下一代SOAR”的主要功能都反映在如何改善上述问题上。现在的“下一代SOAR”主要有两个发展方向。一个是向所谓“超自动化SOAR”方向发展（譬如Torq），旨在将安全编排自动化技术的应用领域向安全运营之外扩展，成为通用安全自动化工具。同时，充分采用低代码-无代码开发技术，降低剧本开发难度和成本。此外，预先开发好大量第三方应用接口，并内置大量剧本模板，再以应用市场和社区的形式进行发布，降低用户的使用门槛。另一个发展方向则是“AI SOAR”或“AI SOC助理”（譬如DropZone.AI），使用GenAI技术实现一个“网络AI助理”，用智能化改造基于剧本的编排自动化。

此外，SOAR厂商们也逐步总结了一套剧本设计开发的方法论，并不断将SOAR的价值聚焦到基于剧本的编排技术能够驾驭的应用场景上去。

****SOAR市场格局****

在SOAR技术不断演进的同时，SOAR市场格局也经历了巨变。

从安全运营的角度来看，正是由于自动化和响应如此重要，响应技术（包括自动化响应）已经不再是SOAR的专属。检测类产品纷纷布局响应，出现了各种DR（检测与响应）类产品，从NDR、EDR到后来的XDR，纷纷内置（简化的）SOAR能力。而作为SOC核心的SIEM产品也在朝TDIR方向前进，大力发展响应自动化技术，并成为SOAR厂商的最大买家群体。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMcclMcHAuIVBMek9aULhLiceySRJXsVpFOkD9O1RBQl5HaY3m9XiciccfsicoeOKYvuEiauYqicXibaAWd6Q/640?wx_fmt=png&from=appmsg)

如上图所示，入围Gartner2024年SIEM魔力象限的所有SIEM厂商都有SOAR，要么自研，要么收购（主要方式），要么是SIEM产品中的一个模块，要么是SIEM产品套件中的一个子产品。

Gartner在[2023年的SOAR市场指南报告](http://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484685&idx=1&sn=2fe383d8335d300614f748ee7f91ceb7&chksm=fa002fb9cd77a6af55094c6484ef13c2e8faa85e5e5536d9c371eed9fd1933c8bee6526b9252&scene=21#wechat_redirect)中就指出，SOAR整合到各种TDIR类产品中的趋势已经十分明显。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMfzYw8Jc8c9ibKGCKQjBgQ5m0vRAQDpUXF0Pox3k0a1P7CPRyozv33hmewqowkcBx0LR92dxvVQq8Q/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**Gartner的观点解读**

对SOAR进行了全面审视之后，我们再回过头来研究Gartner的观点。

在2024年2月份的时候，笔者跟Gartner分析师Pete Shoard进行了一次Inquiry，当时就询问他对SOAR未来的看法，SOAR市场是否会消失。Shoard当时就委婉的表示，SOAR将更多的融入SIEM中，但独立SOAR还存在于某些缝隙（niche）市场。同时，Shoard表示Gartner对GenAI应用于安全（包括SOAR）持审慎态度。笔者理解，GenAI作为革新SOAR或者安全自动化的技术还有较长的路要走。

今年8月份，Dark Reading对Gartner的SOAR过时论点进行了专门的文章报道。文章引述了Gartner SecOps Hype Cycle报告中SOAR词条的主笔分析师Eric Ahlm的话。他表示，将SOAR标记为过时是因为该类产品的组件已经被其它产品和服务所取代。当前，自动化越来越成为一种众人期待的功能，SOC需要编排作为一项单独的功能，将分散的产品集成到单一的运营中心。同时，由于企业客户越来越倾向于简化运营，因而供应商纷纷将SOAR与他们的产品和服务进一步整合到一起。Ahlm进一步表示，Gartner真正要传递的信息，不是说SOAR这个概念过时或者自动化已经终结，而是有很多不同的方法可以增加自动化（以提升效率、扩大规模），而无需去购买独立的SOAR平台。

**总结一下，笔者认为Gartner的观点是：**

基于三方面原因——1）随着自动化技术越来越渗透到各类安全产品（尤其是SIEM）中，独立SOAR厂商和产品越来越少；2）SOAR自身面临各种落地障碍，需要将SOAR与其它产品能力相结合来化解其中的一些障碍；3）用户对于供应商和产品能力整合的呼声越来越高——Gartner呼吁用户更多考虑在SIEM等其它SOC核心产品平台中考虑使用SOAR功能，而不要使用独立SOAR。因此，Gartner将SOAR标记为过时，独立SOAR产品将不再是主流产品，独立SOAR市场将逐步萎缩，仅存在于某些缝隙市场，但SOAR技术将在其它产品和市场中继续发展演进。

顺便提一下，笔者在8月份的时候，针对SOAR的未来发展趋势也咨询了Forrester的分析师Allie Mellen。她表示，独立SOAR依然会存在，但它也会变成更广泛产品的一个能力，因为越来越多的客户在购买其它产品时都会需要这个自动化的能力。对于SOAR未来技术趋势，她认为除了GenAI之外，还要关注低代码-无代码能力，以及诸如案例管理、协作管理等安全运营功能。

**SOAR在中国的未来**

那么，中国SOAR市场未来走势如何？**笔者认为，其实在国内尤其更加需要独立SOAR产品。**因为当前国内大部分客户的SOC/SIEM平台都不具备SOAR能力。在用户彻底更换为下一代具有SOAR功能的SOC平台之前，还需要购买独立SOAR来弥补现有平台的这部分不足。而鉴于当前的中国经济不利局面，用户花费大量资金投资于下一代SOC替换以前大额投资的意愿不高，会倾向于采用“向存量投资要效益"和"查漏补缺"的方式来完善其SOC。因此，**在中国，独立SOAR的机会仍然很多**。

不论SOAR是否独立存在，还是被整合到SIEM或其它产品中，SOAR技术都必须继续演进。

在技术发展趋势方面，需要让SOAR更加易于实施和维护，要降低用户使用成本，譬如积极引入低代码-无代码开发技术降低用户设计开发剧本的难度，积极探索利用GenAI增强现有的SOAR能力。功能上，应该继续深化作战室功能，把SIRP平台做好。对于Gartner提及的TIP部分，[鉴于国内的实际情况](http://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484584&idx=1&sn=ec647bae8b71e4f2a4d68603b8aade00&chksm=fa002e1ccd77a70ae712591a9b745f5dd4f82aee5fe7959fd63e6ef641e5d5d7952576cf5309&scene=21#wechat_redirect)，建议由专门的TIP承接，在SOAR产品中更多考虑如何利用好威胁情报即可。此外，应内置尽可能多的剧本和APP，提升产品开箱即用的程度。最后，要优化剧本开发方法论，教育用户树立正确认知，聚焦投入产出比高的应用场景，避免造成“SOAR万能自动化”的假象。

最后，作为中国SOAR厂商，应该在继续发展独立SOAR的同时，将SOAR与SOC平台进行整合。

【参考】

[Gartner2023年SOAR市场指南报告评述](http://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484685&idx=1&sn=2fe383d8335d300614f748ee7f91ceb7&chksm=fa002fb9cd77a6af55094c6484ef13c2e8faa85e5e5536d9c371eed9fd1933c8bee6526b9252&scene=21#wechat_redirect)

[重新定义SOAR（2023年重编完整版）](http://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484584&idx=1&sn=ec647bae8b71e4f2a4d68603b8aade00&chksm=fa002e1ccd77a70ae712591a9b745f5dd4f82aee5fe7959fd63e6ef641e5d5d7952576cf5309&scene=21#wechat_redirect)

https://www.darkreading.com/cybersecurity-operations/soar-is-dead-long-live-soar

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMepicSn33np52HRygZK2DSdFuVV6ibZQQESNfWcyP8lrVECk9GEVloZQdj7FJbib6tvyt5nh36XxJeicA/0?wx_fmt=png)

专注安管平台

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMepicSn33np52HRygZK2DSdFuVV6ibZQQESNfWcyP8lrVECk9GEVloZQdj7FJbib6tvyt5nh36XxJeicA/0?wx_fmt=png)

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