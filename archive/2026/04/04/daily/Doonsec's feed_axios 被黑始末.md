---
title: axios 被黑始末
url: https://mp.weixin.qq.com/s/Pn5eElN6uBGAzRbQcRyfHA
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:31:29.395232
---

# axios 被黑始末

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iatDdM4vSwruVZ9wF4csrQep8CoKYEc96TfsnLicB3QZqQ14lIlJERAIQIvbbPFHnu6HibpEz2tjwcYh7cxlFJw9q0gpAu8tM2zZxXqrn0G9Pk/0?wx_fmt=jpeg)

# axios 被黑始末

原创

tonghuaroot
tonghuaroot

RedTeam

![]()

在小说阅读器中沉浸阅读

## 写在前面

两天前，axios 的首席维护者 Jason Saayman 在 GitHub 上发了一个 issue，标题是 *Post Mortem: axios npm supply chain compromise*。

https://github.com/axios/axios/issues/10636

axios 每周有 1.4 亿次下载，是 npm 上被依赖最广的包之一。3 月 31 日，有人用 Jason 的账号往 npm 上推了两个毒版本。这件事本身已经有大量技术分析出来了，但这个帖子不一样，它是 Jason 本人写的，是官方第一次正式发声。

我仔细读了一遍正文、评论、和 Jason 自己在评论区的回复，有些东西值得单独拿出来说。

## 帖子是怎么写的

先说一个细节：帖子的正文和 Jason 在评论区的回复，语气是完全不同的两种风格。

正文措辞非常谨慎：

> We are actively investigating how unauthorized access was obtained and reviewing all aspects of our security posture and access controls. While we do not have confirmed details to share at this time...

"actively investigating"，"do not have confirmed details to share at this time"，这是经过斟酌的公关语言，用词小心，留有余地。

但评论区里有人追问社工的细节，Jason 的回复画风就完全不一样了：

> so the attack vector mimics what google has documented here... they tailored this process specifically to me...

然后他一条一条把整个过程说清楚了。

这两种语气的落差说明什么？正文大概率是经过某种程度的法律或公关审核的，但 Jason 本人其实很想说清楚，所以把细节都扔到了评论里。

## Jason 自己说的：社工是怎么做的

这是整件事最值得仔细看的部分。Jason 在评论里把流程拆开说了：

**第一步：伪装成公司创始人**

攻击者伪装成一家真实公司的创始人，克隆了该创始人的形象和公司本身的品牌。这不是随便捏造一个虚假身份，而是找了一个现实中存在的人来冒充。

**第二步：邀请进一个真实的 Slack 工作区**

注意 Jason 用的词是"real slack workspace"，是真实存在的 Slack，不是截图，不是网页伪造。这个工作区的频道设计得很细致：有在同步真实公司 LinkedIn 帖子的频道，有伪造的团队成员资料，甚至还放入了其他开源维护者的资料来增加可信度。

后面这一点很有意思。为什么要在 Slack 里放其他 OSS 维护者的资料？因为这能让目标觉得：这家公司和开源社区有关联，我加入这个工作区是合理的。

**第三步：安排一个多人 Teams 会议**

约的是 Microsoft Teams，看起来有好几个人参与。这个细节很关键，多人会议天然会降低警戒心，因为"钓鱼"在大多数人的印象里是一对一的事，而不是一场有多个与会者的专业商务会议。

**第四步：会议中说系统有什么东西过期了**

Jason 说：

> the meeting said something on my system was out of date. i installed the missing item as i presumed it was something to do with teams, and this was the RAT.

就这一句话。整个攻击的引爆点，是在一个"看起来很正常的商务会议"里，有个弹窗或提示说系统某个组件需要更新，然后他装了"那个更新"。

Jason 随后说这一切"extremely well co-ordinated looked legit and was done in a professional manner"。

## 2FA 有用吗？

有人在评论里问：npm 不是对大型包强制要求 2FA 了吗？Jason 的回答是：

> i have been told that once the RAT is on your machine they have full unilateral control of everything on your machine... and yes i did have 2fa enabled on my account.

开了 2FA。但 RAT 装上去之后，2FA 就没意义了，因为攻击者看得见你的屏幕，截得到你的验证码，甚至可以在你不知情的情况下帮你完成整个认证流程。

这一点在评论区引发了一些讨论。有人指出，npm 目前没有办法强制要求"只能通过 OIDC 发布"。axios 的 v1.x 分支其实从 2023 年开始就用了 GitHub Actions 的 OIDC Trusted Publisher 来发布，最后几个正版版本都有可验证的 provenance attestation。

但这也没用，因为攻击者绕过了 CI/CD，直接用盗来的 token 手动发布，`axios@1.14.1` 没有 gitHead 引用，没有对应的 GitHub commit，完全不走正常流程。而 **npm 没有提供任何设置让包强制只接受 OIDC 发布、拒绝所有手动 token 发布**。

这一点是有人在评论里专门说清楚的：

> npmjs (and other registries) should allow packages to opt in to OIDC-only publishing rejecting all non-OIDC publishes at the registry level.

目前这个功能在 npm 上不存在。

## 评论区里出现了一个更大的背景

帖子的评论里有一条很长的回复，作者是 tayvano，是加密货币安全领域的研究者。她给出了一个更大的背景：

这套手法，和 Google 威胁情报团队文档里记录的 **UNC1069** 的操作方式高度吻合。UNC1069，即 BlueNoroff，是朝鲜国家支持的黑客组织。

他们这几年一直在用类似的套路攻击加密货币行业，基本操作是：

1. 伪装成行业相关的人发起联系（投资人、合作方、播客主持人）
2. 建立长线信任关系，不着急，可能周期以周计
3. 安排一个"有多人参与的视频会议"
4. 会议里触发一个"系统需要更新"的提示，引导目标安装 RAT

tayvano 说：

> This evolution to targeting you guys (meaning: you, OSS maintainers) is a bit concerning in my opinion.

以前他们盯的是加密货币创始人、VC，因为直接有钱。现在开始盯开源维护者，一个高影响力的开源包，是比一个人的资产更有价值的攻击入口。

> Why have calls one by one by one to eventually get the one rich dude when you can get 1 million+ dudes at once?

他还说：

> I can assure you that after this situation, they will ABSOLUTELY continue doing this. They smelled blood.

另一个评论者 voxpelli 说他几周前遭遇了一模一样的操作，被邀请上播客，进群，聊了很久，到了"录制"的时候网站出了问题，提示他安装一个没有经过 notarize 签名的原生 App。他没装，躲过去了。他猜对方盯着的是他维护的 Mocha。

## 帖子最后说了什么

Jason 在正文末尾列了一张"What's changing"的表：

| 措施 | 类型 |
| --- | --- |
| 重置所有设备和凭证 | 事后补救 |
| 引入不可变发布设置 | 预防 |
| 迁移到 OIDC 流程发布 | 预防 |
| 提升整体安全基线 | 预防 |
| 更新所有 GitHub Actions 遵循最佳实践 | 预防 |

然后他说"This list is not the end."

值得注意的是这张表里没有提到"使用硬件密钥"。有评论者指出，在机器已经被 RAT 控制的情况下，哪怕是硬件 FIDO2 密钥，也不一定能提供有效保护，因为攻击者拿到的是活跃会话，不需要重新认证。

帖子的结尾是对 DigitalBrainJS 的致谢，正是这位维护者在注意到有人用被盗的 Jason 账号删 issue 之后，迅速采取行动，开了 deprecation PR，联系了 npm，才让这个事情在三个小时内得到控制。

## 读完这个帖子之后

这件事如果只看技术分析，很容易陷入"看 payload，看混淆，看 IOC"的视角。但 Jason 的这个帖子提供了另一个视角：一个真实的人，在一段时间内被专业的攻击者系统性地欺骗，然后做了一个在当时看来完全合理的操作，结果是整个供应链被污染了三个小时。

这不是"有人点了钓鱼邮件"式的粗心大意。这是一套精心设计的、专门针对特定个人的长期操作。

Jason 在正文里说的那句话值得单独记一下：

> Open source maintainers with high-impact packages are active targets for sophisticated social engineering. Hyper vigilance is needed both on the registry and in a personal capacity.

这句话放在两年前听起来像是套话。现在有了这个帖子作为注脚，不一样了。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

RedTeam

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

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