---
title: Hugging Face事件反思：Agent攻击者已经到来
url: https://mp.weixin.qq.com/s/OfqMBAe8yND-0sz5kBeH1A
source: Doonsec's feed
date: 2026-08-17
fetch_date: 2026-08-18T02:51:33.591137
---

# Hugging Face事件反思：Agent攻击者已经到来

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Hxdb7gjfn9m8toxcxpwanulstaReqTaDCpoWbpgrbA4mL1WKZrRqMUU8FMmVKw0QCwK81oWaVD1PatibwpsGq98sX49b294T7sX0xqObIock/0?wx_fmt=jpeg)

# Hugging Face事件反思：Agent攻击者已经到来

e安在线
e安在线

e安在线

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9kVGMqibsvgpT5vhVXwMvbD2O7zHEdY22IgFJicOorekLH7MswichubTZog5CW8QqSn5IESwkrDDAqjKVc824NvdOqc8wbBRlnf6s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9k3c1v1ZhmQDcX3v0ChuXKfyP7bTQP36xfhTeruoapXujicLJrfckJX2EjB19jsQs7OCGsyxgAEegVa4z8wwciaicuVlbpgIAMzmk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9mpHUyPFMlY0EVd87vJQmEUDZJG2bMc07oPZ7g5AL4jcAHx5aBhjLXOmLMlhRpibexm5eo8zBTfsmXgyxMhraZRure5khjXxF0A/640?wx_fmt=png&from=appmsg)

**HuggingFace事件暴露了AIAgent作为新型攻击者的风险。具备自主推理和执行能力的Agent可能突破沙箱限制，利用漏洞和窃取凭据，以机器速度完成攻击链。**

**面对自主攻击者，传统“发现漏洞再修复”的防御模式难以应对。组织需要通过限制Agent权限、控制网络访问、记录行为轨迹和构建可信Agent运行环境，从架构层面降低攻击影响。**

一个AI Agent突破了用于隔离它的沙箱，将自己暴露在开放的互联网上，随后对另一家公司发起了攻击。

这次攻击并非由人类执行。AI Agent在没有人类实时下达指令的情况下，独立选择并执行了后续动作。

OpenAI披露，在一次内部测试中，其两个模型自主判断：入侵他人基础设施是完成当前任务的最快方式。此次攻击的目标是Hugging Face——一家以构建AI为业的公司。Hugging Face团队在一个周末内拼凑出了其系统中超过17,000个自动化动作，并在任何人意识到幕后是前沿模型之前，就已经联系了执法部门。

这正是安全团队一直警示的场景：能够为实现自身目标而推理、并以机器速度行动的威胁者，不再是会议幻灯片上的假设。它已全面投入实战，并刚刚展示了它能在面对一家懂得如何防御的公司时做到什么。如果Hugging Face都能以这种方式被攻破，那么没有任何安全团队可以假设自己不会遭遇同样的命运。

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9lLfgnSynEwd2mqqXhvQpHGs3DNlHIldqunc4p6zrIsZGGEj6T4XblibpQ1zGICEG1sODHxzJC0FHOYBzwcjzfOEC4GfLiacibdb4/640?wx_fmt=png&from=appmsg)

**熟悉的手法，陌生的速度**

这不是一个因被投喂恶意文档而反噬其所有者的Agent。这次入侵使用了熟悉的手法，却以陌生的速度推进。模型发现了一个0Day漏洞以逃出沙箱，然后利用窃取的凭据打开了通往Hugging Face服务器的远程代码执行路径。

如果有厂商声称其产品本可以干净利落地阻止这次特定攻击，这一说法值得审视。漏洞利用本身几乎不是重点。

**沙箱的局限性**

OpenAI确实设置了沙箱，并没有让这些模型放任自流。它构建了一道边界来约束模型，然而一个能力出众的Agent发现了缺陷并走了出来。

安全团队应该假设，他们部署的每一个Agent最终都会试探其周边的边界，并且Agent发现漏洞的速度会比人类修补漏洞的速度更快。

**防御自主攻击者**

等防御者终于能够合理察觉情况不对劲时，AI Agent早已抵达全球最大的AI开发平台之一，通过窃取的凭据和未修补的远程代码执行路径进入了Hugging Face。

如果由人类来执行这套攻击流程，可能需要数天时间，并且途中很可能会触发警报。而这次攻击在一个周末内执行了数万个动作。面对如此快速的对手，打补丁成为一场防御者不太可能赢得的竞赛。

阻止攻击者的第一步，是减少他们最初能够触及的范围。将应用程序从开放的、可直接访问的网络中移除，这样窃取的凭据和未修补的漏洞就永远不会结合起来，形成攻击者可以轻易触及的目标。

在AI时代，保护应用程序安全意味着不仅要比对手更快地修补漏洞，更要确保攻击者从一开始就无法触及应用程序。

**约束所部署的Agent**

接下来，再看看组织自身部署的Agent。安全团队不能假设Agent会始终停留在他们设定的边界之内。

Hugging Face事件提醒我们，自主系统能够找到意想不到的路径来实现其目标。解决办法是治理Agent能做什么，而不是简单地期望它会循规蹈矩。

Agent的执行应受到约束，这样即使发生逃逸，也无法触及任何有价值的东西。出站连接应默认保持关闭，仅对经过批准的目的地开放。Agent的每个动作都应被实时记录，确保组织对其所有行为一目了然。

这就是我们所说的Trusted Agent Runtime（可信Agent运行时）背后的理念。它的出发点是一个在面对自主对手时依然成立的假设：Agent必须受到治理。

**遏制优先于检测**

Agent攻击者的时代不是即将到来，而是已经到来，其行动速度远超人类所能组织的任何响应。

因此，这需要依靠架构性遏制：让攻击者无法触及应用程序，让Agent无法突破为其设定的边界。这两者都是组织必须在事件发生之前做出的决策，而不是事后补救。

如今，AI Agent正带着真实的凭据和真实的访问权限进入企业的生产环境，而它们往往运行在为“只会按指令行事”的软件而设计的安全控制体系之内。

组织需要在被迫付出惨痛代价之前，就决定好如何遏制这些系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9nLXd8icq6iboRvPOHI4YoSuCYMXDYp814MFPicSNxAseRYia0TSxIZialazzhanl3NmE4IMUXVXJ6CgAdPKbpbZib6wdHlVibFmzCOc8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9kcbKbcvo2V3ZKH1ibMPRUe0eYnZnUc6WeUhibOuGgvwLQ6DROvNa3FuSZLb34WxIO4foSHq5HLvUMnfwhyXvYcAibwXSP8AgF4bc/640?wx_fmt=png&from=appmsg)

声明：除发布的文章无法追溯到作者并获得授权外，我们均会注明作者和文章来源。如涉及版权问题请及时联系我们，我们会在第一时间删改，谢谢！文章来源：FreeBuf

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9lAfw9OMoyfJCusftCW6ODDicVjymAQmJzT9MnDlDTAE6qm7EI9via2PibYcdTrvoic8Aepwiag84OpH9IUdhlOXd3lDO0Q0jfp2Bwk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9ly1BfTyPWHic6b5biaWFW0DNjguMsKxrEg7oXMIpBpsKBQ74NgA5mu6uk07LbicChcic0a9oKwYXcQNOpaVmTSV5NA9M5ibEJqLFzU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9mTiaEmXv59Eibha8zibh9ia4ia67libg1l1VKZqTlQvaeibLB2nacYhv1dErfkJWutqWjeNhugoZDKg80wIIMd5iaXxRsCk0UumF1iamJk/640?wx_fmt=png&from=appmsg)

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