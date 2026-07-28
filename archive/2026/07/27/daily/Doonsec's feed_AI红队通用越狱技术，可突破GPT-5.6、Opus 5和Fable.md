---
title: AI红队通用越狱技术，可突破GPT-5.6、Opus 5和Fable
url: https://mp.weixin.qq.com/s/8KLql2kk5BZPV27yYPVCXQ
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:57:00.196896
---

# AI红队通用越狱技术，可突破GPT-5.6、Opus 5和Fable

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Hxdb7gjfn9m042TroDV7icEj6yCLkST1icxahe8Ovd5GLU9KA2kEnUvqpcCRMb2Ltnqo01eyPOyYI0M0ed703E1XwC1KRT6d9mDCJmx9DILYI/0?wx_fmt=jpeg)

# AI红队通用越狱技术，可突破GPT-5.6、Opus 5和Fable

e安在线
e安在线

e安在线

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9mHOdoCiatBkgKgHk45ClFItE64easianXfdBaCibLTl6w8eXb5RyhuH5xd9U9cg98n2RoS5jhISQE4Z0gl62OEZ3C9Cr1uicKfrWw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9kH2zTaslqOZFzdHLzsQ5ANJn8bDFgia95YycGnKYVOHZEZ4gYEn1stboL78CFE4rFaaicbtljaQtEUSkzicn8m5jvuxibVicPJhYNc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9lVdV081cfmwUiaCapd3zYoCXJ27DNmk0hZycDUzviaxcDKcF7tu7RbWD84wTCWOIx2tibgTibiaJqRpo5AST7yOeQ9nysRGHdk65yk/640?wx_fmt=png&from=appmsg)

**知名AI红队研究员对外宣称自研通用越狱攻击手段，能够绕过GPT-5.6 Sol、Claude Opus 5、Fable等多款主流旗舰大模型的安全防护，该攻击适配各类测试模型，且研究员判断该漏洞难以彻底封堵。为规避监管收紧风险，研究者暂未完整公开攻击细节，选择采用负责任披露模式，邀请行业专家私下核验，预留缓冲窗口供厂商、监管提前研判风险。**

**通用越狱区别于以往仅针对单一模型的绕过手段，一旦证实有效，将暴露现有AI安全训练、防护栏抗对抗能力的多重短板。相关企业现阶段需持续落地输出监控、高危流程人工复核等常规防护，等待厂商官方验证与修复方案。**

一名知名的AI红队成员声称已开发出一种通用越狱技术，可突破包括GPT-5.6 Sol、Claude Opus 5和Fable等严密防护的旗舰模型在内的主流大型语言模型。

在X平台上发布的一篇公开帖子中，Pliny the Liberator将这项技术描述为“对所有模型”以及他所测试的每一类模型均有效。他认为，由于该技术的运作方式，完全修复它可能极其困难甚至不可能。

**Part.1**

**顶级AI模型的越狱技术**

与许多直接以开源形式发布的越狱方法不同，Pliny表示目前暂不公开完整技术。他的目标是设定一个负责任的披露窗口期，让AI实验室、红队成员、安全研究人员和政策制定者能够在技术广泛传播之前对其展开审查。

他邀请AI红队、安全、对齐和政策领域的行业专家私下联系他。他写道，此举是出于当前政治和监管环境的考虑，以及为了避免因混乱的公开披露而引发更严厉的模型限制或禁令。

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9liclKnMA1BR0icp4aUe4gVzNkGBDBRQIDkyFibutT4ap0MsIIXicXHageGEUgydrnr0QwmPb3Mtp6gae4BiaQjl7rnJdWEb2mj8Btw/640?wx_fmt=png&from=appmsg)

越狱是指那些引导模型突破自身安全过滤器的提示或交互模式，使其产生被禁止或高风险的内容。声称具有通用性之所以引人关注，是因为大多数绕过方法都是针对特定模型的，并且在披露后会被加固。

如果该技术经得起独立测试的验证，将凸显以下领域持续存在的差距：

* 安全训练与拒绝行为
* 对抗性提示下防护栏的鲁棒性
* 攻击模式的跨模型泛化能力
* 供应商如何在不过度阻碍合法使用的情况下协调修复措施

Pliny表示，他认为公开披露并不会使世界“变得更危险”，但他也承认其他人可能持不同意见。在披露窗口期内，他的目标是绘制完整的影响范围图，衡量该方法所解锁的额外能力，并帮助决策者理清问题框架。

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9n4icTVNjgOjoezo1FsuSaaVgAzF3TDwplYA2ibK0Erh3Aib0n53xEHWIns3LRzlWuynt1cP2MpTFnYXSicWYNKgQoFxCJh0wukYbI/640?wx_fmt=png&from=appmsg)

**Part.2**

**安全建议与后续应对**

安全团队和AI产品所有者应将此视为早期预警，而非已确认的证据。独立的验证结果、供应商的官方公告以及任何协同发布的补丁指南，都比最初的单方面声明更具参考价值。

在实验室做出回应或该技术通过正规渠道被记录在案之前，依赖这些模型的组织应维持标准防护措施：输出监控、最低权限的工具访问、高风险工作流的人工审核，以及针对违规行为的明确上报路径。

该研究人员表示，他期待“在时机成熟时”分享这一方法。目前，行业下一步的行动是进行内部测试还是引发公众恐慌，将决定事态如何发展。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9kxMiaJqSOibuKQD6iaX0XxQ724F3mcfGR0uib5lXJicXpWia0ZHicgHf7yPic2MNXoM8qglu8Omz7mXUu69EhvBYtlUC9YJK7QhHR9CEw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9kBLxt4z17yY7lbBlXft3rRISg47oN2s7w5yOnDvLibLoSpDKPLRucwrnIuE2dj8uzuj291niaIGKGQverxYZKDwpShZib7O4EeLk/640?wx_fmt=png&from=appmsg)

声明：除发布的文章无法追溯到作者并获得授权外，我们均会注明作者和文章来源。如涉及版权问题请及时联系我们，我们会在第一时间删改，谢谢！文章来源：FreeBuf

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9msglicWIgbFXxb19GBdUtEENUXLbygwbuZeNYEK5gvxevicWD5Y9u5lv1meaxt9eqyyo60EYR6YicibwhA7QnGIz6gfd4guq99edM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9nrEJpnBHibey8xBNRE6VoqqUG3icCX8AV2Mz7Q3XmZCLKyog3LfuAqzWNXUg3kEwCVBPbKicDcQvvLoOGSjRNmYHwH2Yl5FodmK8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9k2ldMMG7FFVOqah8zevogzXRUtyG1Qg61E3iasF1JvibeSHmKHvaelQZ4JELcJmht5GFYDZL2wibBT9e6jlyL2fT4lySicKvPwoXo/640?wx_fmt=png&from=appmsg)

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