---
title: 谷歌拒修 Kubernetes 操作器满分漏洞并拒发赏金
url: https://mp.weixin.qq.com/s/24CpFv66uSmVpZU-Kht9Nw
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:04:27.843911
---

# 谷歌拒修 Kubernetes 操作器满分漏洞并拒发赏金

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfUkhJDF3vxhicemkf3PMnBYDibghopB14gfQx09599ff9UQqSKMkGIicoVFictAibUVm8P7D26R1jYcwYlB0QL7rakEreWbqibf3s9cw/0?wx_fmt=jpeg)

# 谷歌拒修 Kubernetes 操作器满分漏洞并拒发赏金

Jessica Lyons
Jessica Lyons

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**安全研究员 Justin O’Leary 表示，谷歌的Kubernetes操作器中存在一个严重漏洞，可导致任何 Kubernetes 命名空间用户绕过Google Cloud Platform（GCP）的身份和访问管理控制，从而完全控制任何组织机构的云环境。但谷歌的说法从最初将该漏洞评级为高优先级和高严重性，变为认为该漏洞不存在因此不会修复漏洞和支付赏金，而且目前该漏洞报告仍被标记为高优先级且已被接受。**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXV4EDPNGOicB89XqeMcia6EMk3rPiaicEHPweZGu8d16PFzIGHCdriaiaiaXAvvicVQj1eGibyPWzLiaeSeB1PWYM3CicGr12u5OjvLDFv1k/640?wx_fmt=gif&from=appmsg)

O’Leary将该漏洞命名为 “ConfigConfusion”，说明了自3月8日以来向谷歌报送漏洞后的情况，并发布文章详述了该漏洞的更多细节。

该漏洞源于开源Kubernetes插件Config Connector中的一个问题，可导致用户通过Kubernetes管理谷歌云资源。O’Leary表示Config Connector未执行授权检查，从而允许任何具有组织级别权限的Config Connector服务账户绕过身份与访问管理（IAM）授权，并获得对整个GCP组织的最高级别即公司在谷歌云内所有资源的根节点的控制权。

3月27日，一名谷歌安全工程师接受了他的报告，并告诉他：“抓得好！”

该员工表示，他们根据O’Leary的报告向相关产品团队提交了一个漏洞，并向他保证，安全团队将与相关谷歌云人员合作修复该漏洞。另外该员工表示修复后会通知O’Leary并让他检查已登记的付款选项。谷歌将该漏洞分配为P1优先级和S1严重性，表明这是一个急需修复的缺陷，因为它影响很大比例的用户，并可能破坏核心组织功能。

本以为一切尘埃落定，但11天后，即4月7日，O’Leary收到了一条来自谷歌安全机器人的新消息，推翻了之前的决定。消息称，云漏洞奖励计划小组决定，“该问题的安全影响不符合获得奖励的标准。”在审查漏洞报告后，谷歌确定该软件“按预期工作”。消息还指出，计划决定不支付赏金“并不意味着产品团队不会修复该问题。”

近三个月后，该案例仍为P1/S1，状态为“进行中（已接受）”。谷歌尚未分配CVE编号或发布修复程序。O’Leary未获得任何奖励。

但这并非O’Leary或其他漏洞提交研究员首次落入这一境遇。O’Leary今年早些时候与微软有过类似经历。在一个漏洞猎手们已耳熟能详的故事中，O’Leary披露了AKS的Azure备份中的一个权限提升漏洞。微软拒绝了他的报告，但随后悄悄修复了该缺陷，且未分配CVE或发布安全公告。O’Leary 对此表示十分沮丧。“这是一种模式。这就是这些万亿美元级公司对待我这样的人的方式。在我日常用的GKE中发现系统中被广泛使用的严重漏洞，却甚至无法让供应商修复他们自己的东西时，这让我非常沮丧。”

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXUBZNicZKPicceTgvvjj7R3j8gfHz7JssqS3qGy2Pdh5ics1b6HgFdia0rQOPSBZromtic2Cbatqic4hN5gmG3rN0pt9zelxcKnKfsI/640?wx_fmt=gif&from=appmsg)

**谷歌的回应**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfVQXgJDRq4ol52TQZl0r5VicNImY8BCJMFBhrrUPWTn2tYDq6QB4rianOqlCljLDteWoLEfic89vJcHMU5HD495YibJlWcscaMFnoU/640?wx_fmt=gif&from=appmsg)

谷歌提到，之所以没有发放漏洞奖励，是因为不存在漏洞。该公司的一名发言人通过邮件表示，“所报告的问题不符合奖励条件，因为GCP IAM授权绕过只有在攻击者能够访问已被组织授予组织管理员角色的Config Connector服务账户时才能被利用（即该账户是特权的）。”此外，攻击者首先需要进入组织环境（例如，暴露的容器），才能利用特权的Config Connector实例并以管理权限执行命令，例如IAM绕过。将这种级别的访问权限授予Config Connector服务账户，违反了谷歌云公开共享的最佳实践和最小权限原则。”但该发言人并未答复关于为什么该漏洞报告案件在其系统中仍标记为“进行中”而非“已关闭”的问题。

O’Leary提到，自己收到了相同的解释，但他并不买账。他表示，Config Connector服务账户确实需要组织级权限来管理多个GKE集群中的资源。但他指出，谷歌自己的文档指导用户如何做到这一点。本媒体也证实了这一点。此外，O’Leary提到“拥有这些权限并不意味着任何命名空间用户都应该能够滥用它们。一个拥有对一个命名空间的kubectl访问权限且没有GCP IAM权限的开发人员，不应能够成为组织所有者。他们也不应该能够在没有审计追踪的情况下模拟项目中的任何服务账户。漏洞在于缺少授权检查。Config Connector代表用户执行特权操作，却不验证这些用户是否被授权。”

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXqevlsrs6YWXeGKxXTwJDwwP1a0uGXnbkyHpZliboiclbnmU0vUGMNJflGZ0Edkxyoym8Ytd4rlwaQ5yrABS9wHC1afxmjpNIcA/640?wx_fmt=gif&from=appmsg)

**三行代码，五秒钟，获管理员完全控制权**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWjWHdqCe3SPCjY8rEFTnxcnrS3kwB5ibXsoX9e3QKnpRN2Jr1QHJXTGIu6ibUtWTcp59Qv3LbKoZLiaMZAakaBrgSFL3JCqEksFw/640?wx_fmt=gif&from=appmsg)

在一个演示ConfigConfusion的视频中，O’Leary展示了攻击者如何编写三行YAML，在大约五秒内实现对一个GCP组织的完全管理控制。

O’Leary提到，Config Connector存在这些缺失的验证检查。Config Connector基本上是一个谷歌管理的Kubernetes操作器，他发现这些缺失的验证检查导致了混淆代理问题，这意味着没有验证谁在请求什么。混淆代理构成了重大安全挑战，因为它们允许没有权限执行操作的主体强制一个权限更高的主体执行该操作。

为了利用该漏洞，一个拥有对一个命名空间的kubectl访问权限且没有GCP权限的用户提交一个恶意的IAMPolicyMember，就能提升攻击者的权限。

Config Connector将用户控制的组织ID直接传递给GCP IAM API，而不执行授权检查，使用户成为GCP组织所有者。这使攻击者对环境中所有内容如项目、密钥、账单和Gmail账户拥有完全管理员控制权。而且不会留下任何记录，这是因为“攻击者的Kubernetes身份从未接触GCP IAM，Config Connector使用自己的提升凭证执行请求。”

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXhTGu8plIpNFfUAZk6af5Ch9RsC9jnctHPoMeZsOIawM9kQ0h5gL7e6mCtOe5aqMaAWGgAD3MMaazxkjdmJhN30GFgAWs0OA0/640?wx_fmt=gif&from=appmsg)

**“叠叠乐”漏洞**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfWufRwXZEASzoaaX4CuWhhzsdbZAYLF5ML535WJhDx4Vreg8icNYaHRFQShjIdRVC1STBd97HZpueCTYA7mUiarn6u6dNpJNoYgQ/640?wx_fmt=gif&from=appmsg)

据O’Leary称，谷歌之前在访问GCP的不同服务中两次修复过此类混淆代理问题。Tenable Research记录并向谷歌报告了这些问题。其中一个名为ImageRunner，滥用了Google Cloud Run中的权限，以拉取同一账户中的私有Google Artifact Registry和Google Container Registry镜像。第二个名为ConfusedComposer，允许在Cloud Composer环境中具有编辑权限的身份将权限提升到默认的Cloud Build服务账户。

Tenable公司的安全研究员表示，“GCP中的这个权限提升漏洞建立在云端服务中更广泛的攻击类别之上，我们称之为‘叠叠乐’。ConfusedComposer利用了与云服务权限相关的、有点隐藏的云提供商错误配置，将权限提升到预期访问级别之上，这个变体突显了攻击者如何滥用云提供商作为服务编排过程的一部分在幕后自动部署的互联服务。”谷歌最终在Cloud Run和Cloud Composer中都添加了授权检查。O’Leary不理解为什么谷歌不能也在Config Connector中添加该检查。

也许他理解。“这只是我与谷歌的对抗，”他说。“他们对Tenable不能玩同样的煤气灯把戏，因为Tenable有公关团队和法律团队与之抗衡。我只是一个说我不明白这怎么可能是真的的人”——也就是说，某件事怎么可能既是高严重性、高优先级的漏洞，又同时是按预期工作的。而他们只是说：‘嗯，它就是真的。’”

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[CVE-2020-11945 Squid未授权整数溢出分析](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247492897&idx=1&sn=f3af6798ae1a4b26a9804bf60b0496d4&scene=21#wechat_redirect)

[【漏洞预警】Squid缓冲区溢出及拒绝服务漏洞安全预警通告](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247490680&idx=3&sn=effac8aee6cde6bf7071e643faf61bee&scene=21#wechat_redirect)

**原文链接**

https://www.theregister.com/security/2026/06/18/google-told-researcher-nice-catch-then-denied-bug-bounty-for-flaw-it-still-hasnt-fixed/5258076

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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