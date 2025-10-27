---
title: 我花费了400$完成了对大量组织的供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzUyMDgzMDMyMg==&mid=2247484537&idx=1&sn=17fc2d84a99be09f4192fc1e9e816921&chksm=f9e52864ce92a172a48f3c342af1fce37c335f78fea5ffc57afd330bd6a00ebfea8c03669d55&scene=58&subscene=0#rd
source: RedTeaming
date: 2025-02-06
fetch_date: 2025-10-06T20:36:46.904236
---

# 我花费了400$完成了对大量组织的供应链攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D8s0oRfyswlu6dsxC772mkv11S9nuMBBF6gnY5ia68GUia4DtI24WacApIdgtHmOppr2Qic0AiaxUAbeVrmmZoic3OA/0?wx_fmt=jpeg)

# 我花费了400$完成了对大量组织的供应链攻击

XTeam

RedTeaming

> 文章由豆包的沉浸式翻译和语雀插件生成。原文请查看:
>
> https://labs.watchtowr.com/8-million-requests-later-we-made-the-solarwinds-supply-chain-attack-look-amateur/

## 全文总结

本文主要介绍了对废弃的 Amazon S3 存储桶可能带来的安全风险的研究。研究团队通过注册被遗弃的 S3 存储桶，发现了大量来自不同重要组织的 HTTP 请求，包括政府、军事、财富 500 强等。如果被恶意利用，可能导致严重的供应链攻击。团队在研究后决定不再公开触及废弃基础设施话题，并感谢了相关合作实体。文章还介绍了研究的起源、Amazon S3 的概念以及研究过程和目标。

### 重要亮点

* • **研究背景与动机**：网络安全行业对供应链攻击不陌生，过去几年有现实案例。研究团队从一个无法访问的安全供应商报告链接开始，思考废弃 S3 存储桶的安全问题，决定进行相关研究以展示互联网广泛存在的问题，尤其是供应链角度的弱点。
* • **Amazon S3 介绍**：Amazon S3 是一种对象存储服务，具有行业领先的可扩展性、数据可用性、安全性和性能。用户可通过“存储桶”在云端存储文件并分享，非常便宜且易于使用。但当 S3 存储桶被允许衰减并废弃后，可能被不良行为者重新注册利用，带来安全风险。
* • **研究过程与发现**：研究团队在两个月内通过技术手段识别对废弃 S3 存储桶的引用，注册后记录收到的请求。发现这些存储桶在两个月内收到了超过 800 万个 HTTP 请求，来自各种重要组织。如果团队有恶意倾向，可以用恶意内容回应请求，从而访问请求系统或所在网络。
* • **研究影响与合作**：研究团队认为如果研究成果落入坏人之手，可能导致比以往更严重的供应链攻击。他们感谢了 NCSC UK、AWS、主要的未命名 SSLVPN 设备供应商 #2 和 CISA 等实体在研究中的合作。AWS 对已识别的 S3 存储桶进行沉坑处理，降低了风险。
* • **研究结论与反思**：作为一个行业，我们在解决复杂的供应链安全问题时，却常常忽略简单的问题。研究团队决定不再公开触及废弃基础设施话题，并强调不能因研究结果对任何单个组织的安全状况做出错误结论。

## 原文沉浸式翻译

Surprise surprise, we've done it again. We've demonstrated an ability to compromise significantly sensitive networks, including governments, militaries, space agencies, cyber security companies, supply chains, software development systems and environments, and more. Surprise，我们又做到了。我们已经实现了如何破坏敏感网络设施的能力，包括政府、军队、航天机构、网络安全公司、供应链、软件开发系统和环境等。![](https://mmbiz.qpic.cn/sz_mmbiz_png/D8s0oRfyswlu6dsxC772mkv11S9nuMBBfoZXKF2SsFu562Pa2ldIdyjJruGLron4I65YIFdryGmTgjkwfoz6Pw/640?wx_fmt=png&from=appmsg "null")

From those of you who enjoy our research, to the PSIRT and CERT teams who dread an email originating from `@watchTowr.com`, you are likely aware that we’ve historically delivered research that shone a spotlight on the security impact of abandoned infrastructure in various forms:从喜欢我们研究的人，到害怕来自 `@watchTowr.com` 的电子邮件的 PSIRT 和 CERT 团队，您可能知道我们过去提供的研究以各种形式关注废弃基础设施的安全影响：

* • Obtaining the ability to issue valid TLS/SSL certificates for any .MOBI domain (via abandoned domains used for WHOIS servers)获得为任何 .MOBI 域颁发有效 TLS/SSL 证书的能力（通过用于 WHOIS 服务器的废弃域）
* • Hijacking backdoors in backdoors to compromise government networks (by registering domains for backdoors, within widely used backdoors)劫持后门中的后门以破坏政府网络（通过在广泛使用的后门中为后门注册域）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D8s0oRfyswlu6dsxC772mkv11S9nuMBBoTm5fMNIL1xlYliaXz7nAnIgqJ6ibjsyjLzJBbwjn3ickgqnFEZRARTag/640?wx_fmt=png&from=appmsg "null")

Apparently, though, this wasn’t enough to satisfy us that we’d demonstrated just how held-together-by-string the Internet is and at the same time point out the reality that we as an industry seem so excited to demonstrate skills that would allow us to defend civilization from a Neo-from-the-Matrix-tier attacker - while a metaphorical drooling-kid-with-a-fork-tier attacker, in reality, has the power to undermine the world.然而，显然，这还不足以让我们满意，因为我们已经展示了互联网是多么紧密地联系在一起，同时指出了一个现实，即我们作为一个行业似乎非常兴奋地展示了能够让我们保护文明免受矩阵新级攻击者攻击的技能——而一个隐喻的流口水的孩子拿着叉子级攻击者，实际上却有能力破坏世界。

Therefore, almost without choice - once again, we’re excited to share our research with everyone and be somewhat depressed by the results - misery loves company, and a problem shared is a problem halved (thank you).因此，几乎别无选择——再一次，我们很高兴与大家分享我们的研究，并对结果感到有些沮丧——痛苦喜欢陪伴，分享的问题就是问题减半（谢谢）。

Arguably armed still with a somewhat inhibited ability to perceive risk and seemingly no fear, in November 2024, we decided to prove out the scenario of a significant Internet-wide supply chain attack caused by abandoned infrastructure. This time however, we dropped our obsession with expired domains, and instead shifted our focus to Amazon’s S3 buckets.可以说，我们仍然拥有某种抑制的感知风险的能力，而且似乎没有恐惧，因此在 2024 年 11 月，我们决定证明由废弃的基础设施引起的重大互联网范围供应链攻击的场景。然而，这一次，我们放弃了对过期域的痴迷，而是将重点转移到 Amazon 的 S3 存储桶上。

It’s important to note that although we focused on Amazon’s S3 for this endeavour, this research challenge, approach and theme is cloud-provider agnostic and applicable to any managed storage solution. Amazon’s S3 just happened to be the first storage solution we thought of, and we're **certain** this same challenge would apply to any customer/organization usage of any storage solution provided by any cloud provider.需要注意的是，尽管我们专注于 Amazon 的 S3 进行这项工作，但这项研究的挑战、方法和主题与云提供商无关，适用于任何托管存储解决方案。Amazon 的 S3 恰好是我们想到的第一个存储解决方案，我们**确信**同样的挑战将适用于任何客户/组织对任何云提供商提供的任何存储解决方案的使用。

The TL;DR is that this time, we ended up discovering ~150 Amazon S3 buckets that had previously been used across commercial and open source software products, governments, and infrastructure deployment/update pipelines - and then abandoned.The TL;DR 是，这一次，我们最终发现了 ~150 个 Amazon S3 存储桶，这些存储桶之前曾用于商业和开源软件产品、政府和基础设施部署/更新管道，然后被放弃了。

Naturally, we registered them, just to see what would happen - “how many people are really trying to request software updates from S3 buckets that appear to have been abandoned months or even years ago?”, we naively thought to ourselves.自然而然地，我们注册了它们，只是为了看看会发生什么 - “有多少人\_真的\_试图从似乎在几个月甚至几年前就被放弃的 S3 存储桶中请求软件更新？

As always, what we didn’t anticipate was how this would turn out (you could argue that we regularly seem to underestimate what is about to happen).与往常一样，我们没有预料到结果会如何（你可以说我们似乎经常低估即将发生的事情）。

Before you ask, for many reasons, after this research is published we’re resolutely vowing not to touch the subject of abandoned infrastructure again (publicly). We’ve beaten this proverbial horse to death in three different ways, and frankly we don’t want to completely lose faith in the Internet.在您提出要求之前，出于多种原因，在这项研究发表后，我们坚决发誓不再（公开）触及废弃基础设施的话题。我们已经以三种不同的方式将这匹众所周知的马打死了，坦率地说，我们不想完全对互联网失去信心。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D8s0oRfyswlu6dsxC772mkv11S9nuMBBqIQoe85koxRAjqK5Q7gANjvBaxb787P8ZMr3D2GiafyjxJxCrYXCvmA/640?wx_fmt=png&from=appmsg "null")

As for the research itself, it panned out progressively, with S3 buckets registered as they were discovered. It went rather quickly from “Haha, we could put our logo on this website” to “Uhhh, `.mil`, we should probably speak to someone”.至于研究本身，它逐步进行，S3 存储桶在被发现时就进行了注册。它很快就从“哈哈，我们可以把我们的标志放在这个网站上”变成了“呃，`.mil`，我们可能应该找人谈谈”。

$400+ USD later (we’ve included S3, CloudTrail, and CloudWatch - because we relentlessly queried the logs), we had some results worth talking about.400+ 美元后（我们包括 S3、CloudTrail 和 CloudWatch - 因为我们不断查询日志），我们取得了一些值得讨论的结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D8s0oRfyswlu6dsxC772mkv11S9nuMBBibPKJbIPAzsAge20sGvQgz6QLnyIvUFgQOs8dA9Jovib9E3edxe39JpA/640?wx_fmt=png&from=appmsg "null")

(You can clearly see when we discovered the ‘Run Query’ button in CloudWatch in December 2024, mashing it to the point that we almost spent $8 USD)（您可以清楚地看到，当我们在 2024 年 12 月在 CloudWatch 中发现“Run Query”按钮时，将其粉碎到我们几乎花费了 8 美元的程度）

When creating these S3 buckets, we enabled logging - allowing us to track:在创建这些 S3 存储桶时，我们启用了日志记录 - 允许我们跟踪：

* • Who requested files from each S3 bucket (via the source IP address)谁从每个 S3 存储桶请求文件（通过源 IP 地址）
* • What they requested (filename, path, and the name of the S3 bucket itself)他们请求的内容（文件名、路径和 S3 存储桶本身的名称）

These S3 buckets received **more than 8 million HTTP requests over a 2 month period** for all sorts of things -这些 S3 存储桶**在 2 个月内收到了超过 800 万个 HTTP 请求**，涉及各种问题 -

* • Software updates,软件更新、
* • Pre-compiled (unsigned!) Windows, Linux and macOS binaries,预编译 （unsigned！）Windows、Linux 和 macOS 二进制文件，
* • Virtual machine images (?!),虚拟机映像 （？！）、
* • JavaScript files,JavaScript 文件、
* • CloudFormation templates,CloudFormation 模板、
* • SSLVPN server configurations,SSLVPN 服务器配置，
* • and more.和更多。

Put extraordinarily simply - if we were villainously inclined, we could’ve responded to each of these requests with something malicious like:简而言之 - 如果我们有邪恶的倾向，我们可以用恶意的东西来回应这些请求中的每一个，例如：

* • A nefarious software update, 一个邪恶的软件更新，
* • A CloudFormation template that gave us access to an AWS environment, 一个 CloudFormation 模板，它使我们能够访问 AWS 环境，
* • Virtual Machine images backdoored with ‘...