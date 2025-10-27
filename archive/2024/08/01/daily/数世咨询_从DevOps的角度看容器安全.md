---
title: 从DevOps的角度看容器安全
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514417&idx=1&sn=9e4b48c80bf12117c645e7853d56de76&chksm=c144cb8cf633429a4e486a5d82c55583e3e27901417a8e26f05b81d0d0d75925cf63ddc8c458&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-08-01
fetch_date: 2025-10-06T18:05:11.414559
---

# 从DevOps的角度看容器安全

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqrmvZt9she1QtruLtrSaD5RMCibldq4ceoj0pAkiaOQIqSlYUHmCibPcCaaQbJXVdLgAmibEmNyXrgGmg/0?wx_fmt=jpeg)

# 从DevOps的角度看容器安全

陈发明

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqrmvZt9she1QtruLtrSaD5Rf5SlbiaZsqic8Nwun5ZQuAcMiaeqUMLxpYHKXMxfr5ggZv4KyqM97DDTw/640?wx_fmt=jpeg&from=appmsg)

容器化彻底改变了应用程序的开发、部署和管理，这是有充分理由的。它使开发者能够轻松地将应用程序及其依赖项封装进一个便于部署的包中，这样他们就可以更专注于自己最擅长的事情：**编写代码**。

容器化被广泛认为是提高生产力和简化流程的首选方法，越来越多的组织通过容器化来优化软件开发和交付实践。根据 Forrester 的数据，**71% 的 DevOps 团队利用容器和微服务来交付应用程序。**因此，对于容器安全性的探讨显得尤为重要，重点关注DevOps如何为整个软件工程及交付流程提供一个稳健的框架。

**采用全面DevOps方法的组织能够有效避免容器化的潜在风险，并保障其在面对日益增加的网络安全威胁时的系统和数据的安全性。**

**01**

**DevOps和容器安全的相互作用**

开发和运营流程的融合，通常称为DevOps，强调协作和自动化是软件开发生命周期的关键组成部分。

**拥有持续交付和高软件质量的组织能够更快地将新的解决方案和功能推向市场。**然而，最大的困境是避免在速度和安全性之间进行权衡。2023年，Sysdig报告指出，生产环境中运行的容器映像中，有87%存在严重或高危漏洞。考虑到这一点，填补这些漏洞的需求变得尤为迫切。

**02**

**了解容器风险**

正如所有类型的部署一样，**容器也无法避免被利用的风险。**尽管容器化在很大程度上提升了安全性，但它同时也带来了新的安全隐患。这些隐患主要包括：

• **运行时威胁**：正在运行的容器不仅能暴露容器自身缺陷，也能暴露宿主机操作系统的缺陷。

• **配置错误**：配置错误可能会授予对容器和容器编排平台数据的未经授权的访问权限。

• **镜像漏洞**：容器中运行的软件可能存在安全漏洞，使攻击者能够首先访问容器，然后再入侵至宿主机。

**03**

**主动安全**

尽管容器安全工具在镜像扫描、密钥管理、运行时防护及合规检查方面发挥着重要作用，帮助实现安全性与便利性的平衡，但还有一种更为积极的安全策略——DevSecOps。这是**一种以安全为核心的进化扩展版本的DevOps**，可以通过早期识别和修复漏洞以及减少配置失误，来加强软件开发流程中的安全防护。

DevSecOps 和 DevOps 的最终目标是使用相同的原则和方法增强容器的安全性：

• **安全左移**：从项目一开始就将安全性作为开发过程的一部分来考虑。这种方法能够帮助在早期阶段识别并解决潜在的安全问题，从而减少后期投入生产时遇到的安全问题数量。这样做的结果是，最终交付的产品具有更高的安全性和更低的缺陷率。

• **自动化**：自动执行软件漏洞检查、监控正在运行的容器以及强制执行与项目和行业相关的安全实践可以有效地减轻开发人员的工作负担，同时降低潜在的安全风险。

• **加强协作**：通过打破不同组织单位之间的信息孤岛，可以增强软件开发过程的整体安全性，并培养一种责任共担的文化。

**04**

**强化容器化应用程序的策略**

尽管在DevOps环境中实现容器安全有许多步骤，但有一些普遍认可的最佳实践，**所有开发人员都应该将它们纳入到自己的开发生命周期中。**

首要的实践是最大限度地保护容器运行时。类似 AppArmor 和 SELinux 这样的子系统（通常也被称为安全模块）是 Linux 内核的一部分，它们可以用来限制容器化应用程序在运行时的权限，从而有效地防止特权过高执行的情况发生，减少漏洞利用风险。

大多数软件开发并非从零开始，而是利用各种现有的代码和库。所有这些都可能成为攻击的向量。使用经过验证的软件和容器镜像进行开发可以降低最终产品中恶意代码或漏洞的风险。然而，即使是官方软件也可能存在安全漏洞，因此定期进行漏洞扫描可以帮助在部署前发现并解决问题。

实现最小特权原则并不局限于用户账户与管理员账户之间的划分，它同样适用于环境中的实际进程和软件。这一点与用户账户类似，最小特权原则意味着在可能的情况下，确保容器以非root用户的身份运行。这样可以在攻击者获得立足点后，最大限度地减少其对容器造成的损害。

在部署完成后主动监视和响应安全威胁同样非常重要。信息系统不是存在于真空中的，因此确保它们正常运行并保持健康对于整个环境的性能至关重要。这可以通过收集和分析容器日志和指标的各种监视和日志记录工具来实现，从而更轻松地实施响应计划并在环境中出现问题时快速解决这些问题。

**05**

**DevOps 是迈向安全容器生态系统的垫脚石**

安全作为一个总体概念是一系列不断变化的复杂挑战，虽然容器化确实有助于从根本上解决一些问题，但它也引入了许多新的攻击向量。

安全性必须被集成到软件开发的初始阶段，而这一过程正是由DevOps来推动的。通过使用自动化工具，组织可以大幅减少在部署和管理容器过程中遇到的风险。但至关重要的是，开发人员要在整个软件工程生命周期内承担安全责任。

**容器安全不是一个“即插即用”的功能，而是一个持续的过程，涉及在持续开发和集成中采用左移策略，监控并定期更新现有资源，以及迅速响应新检测到的威胁。**DevOps的最佳实践可以加强组织容器环境的安全性，无论是在本地还是在云端。

\* 本文为**陈发明**编译，原文地址：https://www.tripwire.com/state-of-security/look-container-security-through-lens-devops
图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#数字安全交流群来了！快来加入我们的粉丝群吧！

🎁 **多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

😄 嘻嘻，我们群里见！

更多推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpMYmic4xkqp3ky3wcian32ndo3MuLV2dqL6RgqTfITGP0SsmRzibUBftDFg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514213&idx=1&sn=fa2d0412dbbce05ec48a9df909b7cfd3&chksm=c144cad8f63343ce0f383fc9d885c2c7ddcb3f3871270abea4c274775307858d350f60db3b54&token=340500352&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrXJOcAym9Txd8SXyYpsl5tMKKKZOkjKCyFF73OcERMobc16eBGprcrFxpXPqf7uBeueamyuxTI9w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514336&idx=1&sn=e69b1126e86ab2c59c8ca8e315637031&chksm=c144ca5df633434b94b06186e74fa9475521d0ffe272ebfd78f9123b1017b1e2fe548a47a1a6&token=85424237&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpM6fVpib3ficMmxPXTULy4YxbmwckZnudDYBnPvV3icV1ibdoMWpSS7QzE9g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514264&idx=1&sn=34960d59e3146dcce9f986129c3593c2&chksm=c144ca25f633433381c6bb3bc13fe3e8f2c15984de2aa8f072497dc07648f85c713aa1347ba1&token=340500352&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp7W2bvNhnMbFqgLhjCicpyyqrSRhdKhMyqf2mNZqwqY5Acaicx7J3grHGNcfZZdPymz8YeHW7EVkeg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514185&idx=1&sn=8015c07a68a5e2b6074efd2c77f20085&chksm=c144caf4f63343e2c9b835748de4471cc7783155e35dd65cb8fcc818f946e8f770ddc30c09ba&token=1439057957&lang=zh_CN&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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