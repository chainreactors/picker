---
title: AWS CodeConnections 权限透视：一扇控制源代码的全局后门
url: https://mp.weixin.qq.com/s/QO31c2ATqSqKU8G8TUzA0w
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:43:42.329502
---

# AWS CodeConnections 权限透视：一扇控制源代码的全局后门

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibduFLiagZMpiauuvGnTFBjT8OS1mMt1KYRVHJ5bIoKQrm1QhSfwcgT97TMSxHx9JAK1JBeRMe8DSLKEyYo2OUGmqk8mUiafxNZDsA/0?wx_fmt=jpeg)

# AWS CodeConnections 权限透视：一扇控制源代码的全局后门

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 本文详细剖析了AWS CodeConnections的工作原理、它在主流代码托管平台（GitHub、BitBucket、GitLab）的广泛权限，以及其全球资源特性所带来的安全风险。一旦单个AWS账户或服务被攻陷，攻击者可能利用CodeConnections获取对整个组织源代码库的读/写/管理权限。理解其机制对于保护代码和云基础设施至关重要。

## CodeConnections是什么？

简单说，AWS CodeConnections（以前叫CodeStar Connections）是AWS的一项功能，它让AWS资源（比如CodePipeline、CodeBuild）能连接到外部代码仓库。

这样，在AWS里做构建、测试、部署服务时，就不用在AWS里存那些访问源代码的密钥了。听起来像是解了围，对吧？

但关键是，CodeConnections是**全局资源**。这意味着不管你在哪个AWS区域创建的连接，所有其他区域都能访问。这一点在官方文档里写的清楚明白。

## 哪些AWS服务在用CodeConnections？

一开始这玩意儿只支持CodePipeline，但现在名单越来越长。目前知道的至少包括：

* Amazon CodeGuru Reviewer
* Amazon Q Developer
* Amazon SageMaker
* AWS App Runner
* AWS CloudFormation
* Service Catalog
* AWS Proton
* CodeBuild
* CodePipeline

肯定还有更多，而且以后会更多。每增加一个新服务，利用你已有CodeConnections的潜在攻击面就扩大一圈。你得琢磨琢磨，当这些服务都能摸到你的代码时，会带来什么风险？

## CodeConnections在你的代码库有多大权限？

### GitHub Cloud版

想在GitHub上用CodeConnections，你必须安装“AWS Connector for GitHub”这个GitHub应用。通常是装在整个组织上，也可以装在个人账户。

**这里有个大问题**：安装GitHub应用时，你控制不了它申请哪些权限。你唯一能做的主，就是给应用设置一个仓库白名单，决定它能访问哪些仓库。但说实话，大部分安装要么选了“所有仓库”（就是没白名单），要么因为下面要说的“单个应用限制”，白名单里几乎包含了整个组织的大部分仓库。

看看这个应用目前在GitHub Marketplace里要哪些权限（随时可能变）：

* **仓库权限（读写）**：管理、代码、提交状态、Pull Requests、仓库钩子。这意味着它可以读、写、删代码，删掉分支保护规则（比如强制PR的规则），还能改GitHub Actions工作流。
* **仓库权限（只读）**：Actions流水线、部署、环境、Issue等信息。
* **组织权限（读写）**：组织钩子、自托管运行器。这意味着它可以注册恶意运行器。
* **组织权限（只读）**：成员信息。
* **还有一些别的权限**。

总结一下，如果这个应用被滥用，攻击者能：

* 读写或删除你的代码仓库。
* 移除所有的分支保护。
* 修改GitHub Actions流程，植入恶意构建脚本。
* 添加或删除仓库管理员。
* 读取仓库的Secrets和环境秘钥。
* 注册恶意的GitHub Actions运行器。

创建连接时有两种授权方式：

1. **作为Bot连接（App installation）**：选择安装在组织或个人上的“AWS Connector for GitHub”应用。连接获得上面列出的**所有完整权限**，操作日志里显示是这个应用干的。这是最常见的方式。
2. **作为GitHub用户连接**（2024年底才引入）：不选应用安装。连接会“代表”创建连接的那个GitHub用户操作。这时它的权限是**该用户权限与应用权限的交集**。要读一个组织仓库，用户得有读权限，并且应用必须安装在该组织且有该仓库的白名单权限。

所以，在绝大多数现有部署里，都在用“作为Bot连接”这种方式。如果攻击者能通过AWS CodeConnections直接拿到这个应用的权限，他就能对所有该应用能访问的仓库造成重大破坏。

还有个要命的点：**在一个GitHub组织里，这个应用只能装一次**。如果你有多个AWS账户需要访问同一个组织里的不同仓库，所有装在这些AWS账户里的CodeConnections，都将拥有对这个组织里同一组仓库的相同访问权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibd27bzk572AL8pLNm1qibzoXN2jywkHHVLzWZ4sn5ibdT7n2Ovliboia1Xmfhr9VxaKNklAvavqO7H7tNHBRI2vG9uguRewEh7P6wA/640?wx_fmt=png&from=appmsg)

### BitBucket Cloud版

在BitBucket上用，得安装“AWS CodeStar application”。跟GitHub比起来，BitBucket连个仓库白名单的控制都没有。你只能选择在整个工作区（Workspace）上安装，还是不安。就这么点控制。

安装时，它要的权限包括：读写仓库及Pull Request、管理仓库、读写仓库Webhook。又是管理员权限，又能读写代码，同样可以用来绕过保护，夺取仓库控制权。

### GitLab Cloud版

和BitBucket类似，需要安装“AWS Connector for GitLab”，同样没有细粒度的仓库白名单控制。安装时要的权限包括读写仓库、管理运行器等。虽然没有GitHub那样直接的管理员权限，但能管理运行器也是个风险点，可以用来篡改构建任务。

### 其他支持的类型

官方还支持自托管的GitHub Enterprise Server、GitLab以及Azure DevOps。不过这个系列文章主要聚焦在云端版本。

## CodeConnections是怎么安装和管理的？

安装一个CodeConnection，通常需要一位在代码平台上有足够权限的人（比如组织所有者），在AWS账户里完成一次OAuth授权流程。

流程走完，连接就建立了，而且会一直有效，直到有人主动删除这个连接，或者在代码提供商那边把这个应用删掉。

**关键来了：在AWS账户里安装CodeConnection时，你无法进一步限定它在这个账户内的访问范围。**一旦装上，它就拥有了所连接的那个代码平台应用的全部权限。

你在AWS这边能做的控制，就是在使用CodeConnections的服务（比如CodeBuild）时，用IAM角色和条件键（Condition Keys）去限制能访问的权限和仓库。这就像在房间门口加了个保安。

但如果账户里有个能创建IAM角色的管理员，他完全可以绕过保安——新建一个没有任何限制的角色，从而利用那个已认证CodeConnection的全部权限。AWS的RAM（Resource Access Manager）可以集中管理和共享连接，但这不改变共享后每个账户获取的源代码权限，只是管理上方便点。

## 一个典型的安装风险场景

假设你是某大公司的一个团队，你们有5个GitHub仓库想用AWS CodePipeline。你请GitHub组织管理员帮忙。

管理员在组织上装了“AWS Connector for GitHub”应用，只给这5个仓库的白名单权限。

然后他在你的AWS账户里帮你安装了CodeConnection，选择“作为Bot连接”。请注意：**在这个安装过程中，管理员无法进一步缩小应用的权限**。所以最终的结果是，你的AWS账户里的这个连接，能访问这应用有权访问的所有仓库——目前是5个。

你是AWS管理员，可以在IAM策略里加条件键，只允许CodePipeline角色访问这5个中的一个，看起来挺安全。

但账户内的高权限用户（比如另一个管理员），完全可以创建一个没有限制的IAM角色，从而访问到这5个仓库的全部内容。

过了一阵，兄弟团队也要用，需要访问同一个GitHub组织里的另外5个仓库。

组织管理员更新了“AWS Connector for GitHub”的白名单，加上了兄弟团队的5个仓库，然后帮他们在自己的AWS账户里也装了CodeConnection。

问题出现了：兄弟团队的CodeConnection现在能访问10个仓库。而**你账户里的那个CodeConnection，现在也能访问这10个仓库了**，因为你们共享的是同一个后端GitHub应用。

发现规律了吗？接入的团队和AWS账户越多，你的GitHub组织面临的风险就越大。你不得不依赖于每一个AWS账户、以及每一个有权访问这些账户的用户，都是安全的。

你当然可以强制每个团队用自己的GitHub组织，这样每个组织可以装独立的应用，权限就隔离了。但这会带来巨大的管理开销。很多大公司不会这么干。

而在BitBucket和GitLab上，情况更“干脆”，连白名单都没有，应用一装就是整个工作区/项目的完全访问权限。所有安装了这个连接的AWS账户，都获得了相同的完全访问权。

## 小结与展望

现在你应该明白了，CodeConnections像一个“权限放大器”。它将原本在代码平台应用上的广泛权限，通过连接的方式，暴露给了多个AWS账户和服务。

如果你的组织有成千上万个仓库，数百个AWS账户，那么只要有**一个AWS账户**被攻陷，攻击者就可能顺着CodeConnections的藤，摸到你代码庄园的每一个角落。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibd7ldcxLejYibOtGuwkmX7wRibcjvaaVP3CZweFDLhnMiaI9AVzUY5q3SibyibNT2TUUoLUPGmG5KxSkTU9AiaXnFKXWq7yDw1v7LEqg/640?wx_fmt=png&from=appmsg)

这还只是系列文章的第一篇概览。接下来我们会深入具体服务，比如CodePipeline，看看攻击者如何利用`UseConnection`这类权限，在代码仓库和AWS账户之间实现权限提升。

权限管理就像洋葱，一层套一层，而CodeConnections把最里面那层——源代码——的访问权，做成了一把可供多人使用的全局钥匙。钥匙丢了，整个堡垒都可能从内部瓦解。

---

### 参考资料

[1] https://thomaspreece.com/2025/12/04/part-1-overview-of-aws-codeconnections-escalating-privileges-via-aws-codeconnections/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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