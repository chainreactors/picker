---
title: 云中的横向移动风险以及如何防止它们-第1部分：网络层（VPC）
url: https://mp.weixin.qq.com/s?__biz=MzI2NDQ5NTQzOQ==&mid=2247496980&idx=1&sn=f7d55e56545dbb612fd17300ebedbfa8&chksm=eaa97d34dddef4224d2b3524cb7e002ff5c765636b3a0682b26dde36a32f87eb88f56cad2b1e&scene=58&subscene=0#rd
source: 火线Zone
date: 2022-10-20
fetch_date: 2025-10-03T20:23:40.537262
---

# 云中的横向移动风险以及如何防止它们-第1部分：网络层（VPC）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0Z0LqMyVGaQt8HuVQwP5Kk0RMdTjUHiaXf35bYkGrOibtpU8xvdjZgvUs3hXN6JIybtiahuqNSOciarCicUg8MDzhjQ/0?wx_fmt=jpeg)

# 云中的横向移动风险以及如何防止它们-第1部分：网络层（VPC）

M1n0s

火线Zone

**本文为翻译文章，原文地址：****https://www.wiz.io/blog/lateral-movement-risks-in-the-cloud-and-how-to-prevent-them-part-1-the-network-layer**

在云中横向移动系列的第一篇博文中，我们将介绍横向移动，因为它与云的网络层虚拟私有云 (VPC) 有关。我们将讨论攻击者的策略、技术和程序
(TTP)，并概述安全从业者和云构建者的最佳实践，以帮助保护他们的云环境并降低 VPC 中和 VPC 之间横向移动的风险。这一点尤其重要，因为
58% 的云环境至少有一个公开暴露的工作负载，其中存储有明文的长期云密钥。

**云横向移动简介**

横向移动是攻击者用来扩展其网络访问以在环境中移动并实现其目标（例如泄露敏感数据、征用工作负载）的一种策略。

多年来，横向移动一直用于基于网络协议和服务（如 Active Directory、SMB 和 NTLM）的本地网络。从通过网络共享传播的Stuxnet蠕虫，到像 APT1 和 APT29 这样的高级威胁组执行传递哈希和传递票证，横向移动已经参与了许多重大攻击。

在云环境中，当攻击者获得初始访问权限并破坏工作负载时，他们可以滥用 IAM 权限或使用众所周知的本地横向移动技术在虚拟私有云 (VPC) 中从一个工作负载“跳跃”到另一个工作负载。他们的目标是获得高价值的资产，这些资产可以提供额外的横向移动和访问其他云资源和身份（例如具有敏感数据或管理员身份的皇冠资源），无论是在同一 VPC 内部还是外部。

**背景：本地与云**

在深入探讨云网络层中不同的横向移动技术之前，让我们先回顾一下本地环境和云环境之间的一些重要区别：

#### **身份和访问管理 (IAM)**

尽管许多横向移动技术适用于本地网络和云网络，但 IAM 是云中的一个重要差异化因素：IAM
管理访问控制并授权身份对特定资源执行某些操作。入侵其中一个身份的攻击者可能能够冒充它，根据其有效权限执行操作，并通过云提供商 API
命令横向移动到帐户中的不同云资源。

#### **部署和配置**

与需要广泛的网络知识、硬件限制和缓慢的采购流程的本地不同，在云中部署和配置 VPC 和网络资源（例如 Internet 网关、负载均衡器、ACL）非常简单直接。然而，这样的执行速度增加了可利用的网络错误配置和资源泄露的风险。

#### **可见性和风险管理**

云的复杂架构使得跟踪和保护数以千计的资源变得具有挑战性，更不用说它们之间的映射连接、评估有效权限以及分析和优先考虑对组织的关键威胁。为了解决这个问题，所有主要的
CSP 都支持专用
API，以提供对云环境中部署资源的可见性。尽管对云管理员有用，但恶意行为者可能会滥用此类功能来确定在受感染帐户中运行的具有皇冠宝石潜力的资源类型。

#

**网络横向移动策略、技术和程序**

云中的对手利用多种技术和功能进行横向移动攻击。其中包括远程服务、蠕虫、有效账户、VPC 对等互连、IaaS/PaaS 数据库、漏洞和错误配置。

**通过远程服务访问主机**——VPC 中的恶意行为者可以使用存储在受感染虚拟机中的明文私钥或凭证横向移动到接受远程连接（如 SSH 和 RDP）的机器。一旦进入 VPC ，他们还可以扫描可利用的易受攻击的远程服务。

**植物**蠕虫——攻击者经常使用蠕虫感染工作负载，然后扫描 VPC 中存在可利用漏洞和安全错误配置的其他工作负载。例如，具有不受限制的安全组规则和弱身份验证方法的 Linux 机器很容易成为目标，因为蠕虫可以扫描它并通过暴力破解本地用户的密码。DreamBus僵尸网络 就是一个很好的例子。

**冒充有效账户**——攻击者可以滥用现有账户的明文云密钥，并通过正确的权限冒充 IAM 身份，通过 IAM 层破坏其他云资源。这可以通过云提供商 API 命令在原始 VPC（例如 S3 存储桶）之外发生。受损的管理员身份 - 或可以升级到此类权限的身份 - 可能导致完整的帐户接管。

      ![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQt8HuVQwP5Kk0RMdTjUHiaXFr6qjucqDYQEM9VHtaySrwJ6owTG7ZgOHnMNxJn8pW5vLr9vnUl9vA/640?wx_fmt=png)

           *具有明文云密钥的公开 VM，与有权访问无服务器功能、存储帐户和 KMS 密钥的 IAM 用户关联（图 1）*

**通过 VPC**对等互连——与站点到站点 VPN 一样，VPC 对等互连支持两个隔离环境之间的通信。所有主要 CSP（AWS、Azure、GCP）都支持它。如果攻击者进入的 VPC 与另一个授予其不受限制的网络访问权限的 VPC 对等，则攻击者可以“逃离”第一个网络，在第二个网络中横向移动到其他工作负载，并可能危及跨订阅甚至租户的资源。

          ![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQt8HuVQwP5Kk0RMdTjUHiaXRQhUvaHxyBa3S7LiaiaPLr4w9H1ibHeVSN2wzz1UdIO51LpsAibV9egwwg/640?wx_fmt=png)

           *使用 VPC 对等连接的两个 VPC 可能允许攻击者横向移动并获得跨 VPC 访问（图 2）*

**发现 IaaS/PaaS 数据库——**明文私钥和凭证可以授予攻击者访问位于受感染 VPC 中的 IaaS 或 PaaS 数据库（例如 RDS 实例）的权限，而不管它们是否公开。这些类型的数据库可能是皇冠上的宝石，并且包含高度敏感的数据，例如凭据或客户 PII。

**利用漏洞和错误配置——**在寻找对横向移动至关重要的宝贵资产时，攻击者通常会寻找位于受感染 VPC 中的“唾手可得的果实”。理想的目标是具有漏洞和安全错误配置的可利用工作负载，例如具有关键 RCE 漏洞且没有严格安全组规则的网络可访问的内部虚拟机。

**大多数云环境容易受到横向移动的影响**

Wiz Research 调查了拥有至少一条横向移动路径的云环境的数量，这些路径涉及在具有明文私有 SSH 密钥或明文长期云密钥（例如 AWS 访问密钥）的 VPC 中公开暴露的工作负载。

> 我们的研究结果表明，大约 58% 的云环境至少有一个公开暴露的工作负载，其中存储有明文长期云密钥，而大约 35% 的云环境至少有一个公开暴露的工作负载，其中存储有明文私有 SSH 密钥。

在任何一种情况下，这种妥协都可以让攻击者在相关环境中提升他们的权限或连接到 VPC 中的其他工作负载。

可以看出，这些数字反映了许多组织的云环境中对横向移动攻击缺乏足够的防御。

**推荐的最佳做法**

以下是任何组织都应在其云环境中实施以降低横向移动攻击风险的 5 个关键网络最佳实践：

1.**实施严格的防火墙（安全组和 ACL）**

安全组充当 VPC 中进出虚拟机实例的入站/出站流量的防火墙，而 ACL 则充当子网级别的防火墙。所有安全组和 ACL  的最佳策略是将“最小特权”原则应用于所有规则：限制对特定 IP  地址的访问可减少工作负载受损时的攻击面。例如，严格配置的安全组可以通过阻止网络连接来防止攻击者横向移动到在特定端口上具有 RCE 漏洞的未暴露  VM。

          ![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQt8HuVQwP5Kk0RMdTjUHiaXhO1lficgUlue1G4tmzFibHKsJp1H7sTqWMORlAWT695UAIzkU7C0z1RQ/640?wx_fmt=png)

           *具有严格安全组规则的易受攻击的内部虚拟机，可阻止攻击者横向移动并对其进行破坏（图 3）*

2.**删除明文云和私钥**

明文长期云密钥不应存储在您的云工作负载中。泄露的密钥使攻击者能够“逃离”网络层并在云服务和资源之间横向移动，从而保持持久性。相反，请确保仅将具有最低权限的角色附加到 EC2 实例（Azure 中的严格 RBAC 角色）。这些角色会自动生成临时凭证，从而消除您的环境中长期密钥暴露和潜在持久性的风险。

至于私有 SSH 密钥，组织可以采用更安全的方法对内部机器进行远程身份验证。例如，他们可以使用堡垒主机来防止端口暴露，或者使用基于 IAM 权限的专用云提供商服务，例如 AWS 的SSM API或 GCP 的身份识别代理(IAP)。对于 Linux 机器，这些专用服务将是比密码验证更安全的选择。

3.**修复关键漏洞**

一旦攻击者成功破坏了 VPC 中的工作负载，他们将开始扫描驻留在其中的具有可利用的严重漏洞的其他工作负载。因此，您的 VPC 中任何工作负载上的任何严重漏洞，无论是暴露在 Internet 上的还是未暴露在 Internet 上的，都应该立即修复。

4.**隔离你的环境**

根据功能（例如生产）或组（例如财务）将您的环境拆分为不同的 VPC，可以加强您的安全状况。它通过增强对资源的可见性和在发生安全漏洞时最小化爆炸半径来减少攻击面并降低横向移动风险。

          ![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQt8HuVQwP5Kk0RMdTjUHiaXqV6QEqCnEfdGQd0tiaIqPUBTuYFd1Q1WicXwVZPssAOO1E6cy50XWhJQ/640?wx_fmt=png)

           *网络隔离可降低 VPC 漏洞时的爆炸半径和横向移动风险（图 4）*

5.**采用私有链接**

与提供跨两个不同 VPC 的广泛双向访问的 VPC 对等相反，私有链接是一种更受限制的单向机制。私有链接允许资源向任何选择的订阅公开端点服务，以便直接连接 VPC。它由所有主要 CSP（AWS PrivateLink、GCP Private Service Connect、Azure Private Link）提供。

          ![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaQt8HuVQwP5Kk0RMdTjUHiaXFkkJzUR1xiaDooZogbTtufNa7ZNhyibThxVOyHkJXrtjr6L170q0Df2A/640?wx_fmt=png)

           *私有链接提供限制性和精确的端点访问，降低跨 VPC 横向移动风险（图 5）*

**总结**

深入了解各种攻击 TTP 对于从事网络安全工作的任何人都至关重要。在第一篇博文中，我们介绍了云环境中横向移动的概念，主要关注 VPC  网络层。我们介绍了本地和云环境之间的主要区别，概述了 VPC 中典型的横向移动技术，并强调了 5 个网络最佳实践来减少其攻击面。此外，我们分享了我们团队的研究成果。

 在本系列的下一篇文章中，我们将检查云 IAM 层中的横向移动。我们将讨论它的能力和挑战，解释一些常见的攻击者 TTP，并列出关键的 IAM 最佳实践，以加强组织的环境并最大限度地减少潜在漏洞的扩散范围。

**【火线Zone云安全社区群】**

进群可以与技术大佬互相交流

进群有机会免费领取节假日礼品

进群可以免费观看技术分享直播

识别二维码回复**【社区群】**进群

![](https://mmbiz.qpic.cn/mmbiz_jpg/0Z0LqMyVGaSfroia0hFzznncJKBicEDyN5RAXZW93CEdwVkAyQD8TBZgIJNEPiaKZXZC6coDzhREWnvCicOpxoskrQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaSfroia0hFzznncJKBicEDyN5Hf9wBEW2VcEpquEUapHezn22RoL4uktWwmOicax7sbgqLGKkAMDGWVQ/640?wx_fmt=png)

火线Zone是[火线安全平台]运营的云安全社区，内容涵盖云计算、云安全、漏洞分析、攻防等热门主题，研究讨论云安全相关技术，助力所有云上用户实现全面的安全防护。欢迎具备分享和探索精神的云上用户加入火线Zone社区，共建一个云安全优质社区！

如需转载火线Zone公众号内的文章请联系火线小助手：hxanquan（微信）

![](https://mmbiz.qpic.cn/mmbiz_jpg/0Z0LqMyVGaSfroia0hFzznncJKBicEDyN5KuHFFqB30YY721bFs4uqGOoOcWiaia15lpHJ8JGtHNFfzqT1WrJyUMUA/640?wx_fmt=jpeg)

//  火线Zone //

微信号 : huoxian\_zone

![](https://mmbiz.qpic.cn/mmbiz_gif/CkzQxaHZX9KdW919vwagVwhCeicQPXuMGibHcf2WqiaFyvfy5p1oIk1C5SOdtTyLlQmOtEia7FMKicknJzGTmYLWb2Q/640?wx_fmt=gif)

点击阅读原文，加入社区，共建一个有技术氛围的优质社区！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaTIhKZJRWlQlI7jNqgnBiazDQfwhAfLQoWQege0A5eTVNn9ficjgQhsKznU8lFfWBpDfIaz1ia4Kr6HQ/0?wx_fmt=png)

火线Zone

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaTIhKZJRWlQlI7jNqgnBiazDQfwhAfLQoWQege0A5eTVNn9ficjgQhsKznU8lFfWBpDfIaz1ia4Kr6HQ/0?wx_fmt=png)

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