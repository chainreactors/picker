---
title: 「IaC 保卫战」图文技术干货精炼版
url: https://mp.weixin.qq.com/s?__biz=MzIzOTE1ODczMg==&mid=2247495243&idx=2&sn=65fb83c83699db156acb47d65b852b64&chksm=e92cfae8de5b73fef4ec35482b208acf3a2b82ca4048571a4cea68a7ce782b9db48d1bed6518&scene=58&subscene=0#rd
source: CT Stack 安全社区
date: 2023-03-15
fetch_date: 2025-10-04T09:36:07.685319
---

# 「IaC 保卫战」图文技术干货精炼版

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xLk5PwibzMpT8F8HpraQYtMvhoRhobGWl0ibMKGtv1Nia5HyppkFWrXKxYCawKynG7wkGq11bdfAbUaa4vKDv4O5Q/0?wx_fmt=jpeg)

# 「IaC 保卫战」图文技术干货精炼版

原创

DVKunion

CT Stack 安全社区

“起初，没人注意这场灾难，不过是一个错误的配置，一个默认的口令、一个没有修复的漏洞、一次 DDoS 导致的宕机，直至整个攻击与所有人息息相关。” ——《流浪地球（云原生安全版）》

**「打响“IaC 安全保卫战”」**，今天和大家分享的是 IaC 基础设施即代码的相关安全和一些对应的解决思路。

> ❝
>
> 听到一些红队的小伙伴抱怨:" 政府/医疗/学校项目好做，但是到了互联网厂商和云环境下，就显得有些措手不及。"
>
> ❞

其实 IaC 在很多企业内已经应用十分广泛。但是相对来说**「敏捷开发」**和**「DevOps」**已经将开发技术栈、将传统的技术架构拉开了比较大的鸿沟。

更多的安全研究人员仍专注于传统的**「应用安全」**和**「基础安全」**。应用安全指我们常说的**「web 安全」**，而基础安全一般指**「主机安全」**、**「网络安全」**等。

## 什么是 IaC？

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3uoDzkDw871ic5B9OmKPaw7fdU5ib4gGXDS6WKogCgb53CQDctO3DluKw/640?wx_fmt=png)上图显示的是从文字定义上解释“什么是 IaC？”

但是定义往往都是比较难懂的，对于安全人员，可能实际参与开发的场景比较少，所以对具体开发项目所做的一些流程并不是很熟悉。

从我个人的理解出发，IaC 其实就是一种思想：它将状态性的描述定义为了人类可阅读的代码段，并通过约束工具，来实现从 0状态 到 我们期望的状态 的转变。

> > 举个例子🌰：当你拿到一台崭新的电脑，或者是重装一台主机时，一些常用的应用，环境都需要重新安装。生产业务也相同，当一个新应用需要部署时，新的虚拟机需要为应用提供特定的环境依赖并初始化。这时，老运维通常会掏出祖传的 ansible 脚本，即可快速生成一个完整的、可靠的环境，这便是早期的 IaC 形态。同样的，应用在进行配置管理、自动扩容缩容等等场景，都涉及到了 IaC 的使用。

## IaC 的特征与分类

**「IaC 的特征」**

1. 重复性：一份脚本可以多次使用。
2. 可测试性，可视化：将原本不可见的状态描述出来，层次清晰明了，每一步骤可以单独测试。
3. 可扩展：比如我们现在需要一个 nginx 主机，后面又需要了一个 nginx 主机，则可以利用 IaC 进行快速扩容管理。
4. 一致性：IaC 保证最终的状态保持一致。

**「IaC 的分类：」**
1. 命令式![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3lcRk1nz8xD7cicuJiacG2zicP51xJxZaZ45kw6VLf2l6GiaCCHg053TZBg/640?wx_fmt=png)

* 更直观的控制: 命令式 IaC 更适合对基础设施进行直接的控制和操作，可以更好地控制底层组件的细节。
* 更精准控制：命令式 IaC 允许更细粒度的控制，可以在配置文件中直接指定每个组件的细节，从而更精确地控制基础设施。
* 更容易实现：由于命令式 IaC 使用的是编程语言，因此更容易上手和实现，不需要过多的培训和学习成本。
* 更好的灵活性：命令式 IaC 更适合具有一定灵活性需求的组织，可以根据不同的需求对基础设施进行快速调整。

---

2. 声明式![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3GYIs9llMWs5EslMdVwDSvF5c2pro8hmWmE3N1zaWYYkNJNkVkjCt6Q/640?wx_fmt=png)

* 更简单和易读：声明式 IaC 使用的是基于声明的语言，代码更容易理解和维护。
* 更自动化：声明式 IaC 可以实现更高程度的自动化，系统能够自动处理基础设施的创建和维护，从而减少了手动错误。
* 更稳定和可靠：由于声明式 IaC 代码描述了期望的最终状态，系统将自动确保所需状态已经实现，从而提高了系统的稳定性和可靠性。
* 更适合大规模部署：声明式 IaC 更适合具有大规模部署的组织，可以减少配置和部署过程中的错误和不一致性。

## IaC 的重要性

我们来看看 IaC 产生的两个实际优势：
其中最明显的就是**「效率提高」**：![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3GrxlfiayZnKEZibBZcibTQs4DlCZXgR1PNic9NCcWS6uUeLAuAQy6ww9Tg/640?wx_fmt=png)
另一个是**「避免手动操作导致的安全风险」**：![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw33gVerEU0kVMMAceDFLibTa5OPuuza5HPibLPK7gqBk7TNmOBoG6lgAOA/640?wx_fmt=png)每次见到一些开发人员为了配置环境或寻找 bug，直接登录到了生产环境的机器进行直接操作，都提心吊胆。

而 IaC 可以提供一套标准流程规范，避免人为操作失误。

## IaC 安全的挑战

下面列出了 IaC 可能存在的风险：![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3S31n60BByLhicTEwBf0Wj6xJwy5buJWrN6UkaqibZFaV0baEuF2MJlvg/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3c5rUxOF2wuk46aQeLIJcGkbQOltfMlhNW2CgGPWM6wTA7hGh1toW4w/640?wx_fmt=png)我们来简单举几个例子🌰：

1. 基础镜像漏洞![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3VTSxasrbzgibSrUyHd0Qib80l0uBklnYTIs36XOFmHEA6ibK39CeUFD3w/640?wx_fmt=png)而以上问题都可以在一开始的 IaC 配置文件，也就是 dockerfile 构建之前的分析就可以发现，并提醒业务进行解决。

2. 镜像源不可信![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3J1vABiaz9oYYMmHR8bwlicELIYm53KicCmnelbWooHgYcoWPuv1ibcgD0Q/640?wx_fmt=png)比如说，我们为了快速构建镜像，使用了一个没有进行过认证的镜像源，拉取了一个 tomcat/nginx 镜像。

若某一天该镜像源遭到黑客入侵，或者是镜像源维护者作恶投毒，则你自己的镜像也会遭到影响。

3. 数据泄露/硬编码![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3XoXtXk2wrM9FDI4Be2uiaIlDtlbMv0tKcL22bxFnP9OricsiabpicsiaqvA/640?wx_fmt=png)直到今天，在 github 搜索阿里云 AK/SK 的关键字样，还可以搜索到不少相关密钥信息。

## IaC 安全最佳实践

防止硬编码密钥渗透到 IaC 中![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3Jo97ib27t4fx6V6oCZNibeksxr3DSdfEK4ibnXVA5CbWOcz33FN53GDKA/640?wx_fmt=png)比如说我们在 dockerfile 构建时为了方便，将 buckets 桶的 AK/SK 硬编码到了 ENV 中，就可能导致被利用从而获取整个云上内网环境权限。

> ❝
>
> 配置错误问题一直是一个微小但是致命的问题，所导致的影响效果可以参考弱口令。
>
> ❞

一百个研发有一百种方式从不同的地方获取配置信息（环境变量、全局变量、config-file、甚至于自带一个小的 sqlite），也侧面说明了配置中心建设的重要性。

理想的状态下，所有的敏感配置信息都应该从配置中心动态的进行获取，而不是以明文的形式出现在文件中。

---

保证 IaC 文件的可靠性![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3KIHKsdkqDUrzqsrO06oJLvGxCtkE3CKpKTlGuCoueuSmqcibSEESOww/640?wx_fmt=png)IaC 太过于方便了，利用起来同样也很方便，只要有权限，我们不需要了解如何去部署挖矿，一键式命令即可帮助完成入侵。

攻击者可能通过一些漏洞: （如 K8s APIServer 不安全的配置）获取到 IaC 工具的控制权限，从而下发了恶意的 yml 配置。所以保证 IaC 文件的可靠性非常重要。

---

遵循IaC文件官方推荐的最佳实践![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3TzkO1sz55fg1x3TNXsa8VZ9X0vyCfzuPsMl0td97463EvDSmy6UQQw/640?wx_fmt=png)

···

## 策略引擎：OPA

> ❝
>
> “OPA，来打造自己的 IaC 扫描器。”
>
> ❞

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3WJf7s7rYm16Rwr8MG9AUicYpBPMJcx8SBfzicDuF2nUMCP7d6OMiba3Bg/640?wx_fmt=png)什么是 OPA 呢?
我个人的描述：**「是一个云原生时代的统一化策略引擎」**。

比如在传统互联网架构中，先不提不同厂家之间的差异，同一厂家、不同安全设备之间的规则也完全不相同。

Waf 的过滤规则文件和 Sast/Dast 检查的规则文件，肯定完全不同的。

而 OPA 提供一套标准化的准则引擎，可应用于整个云开发生命周期中的各个部分，标准化策略的格式。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3wq3IKjyVibjuA6vLGnVMUf6oyhKg4YQXPsIhiabMGzBYK3F1ykXt2KEQ/640?wx_fmt=png)声明式语言：OPA 使用一种声明式语言，称为 Rego 语言，来定义策略。Rego 是一种基于集合的语言，它允许您使用基于模式匹配和条件逻辑的规则来定义策略。这种语言的优势在于，可以方便地描述和组合不同的策略。

策略评估：OPA 可以在不修改应用程序代码的情况下，直接将其集成到应用程序中，并评估请求或数据是否符合定义的策略。OPA 通过使用 Rego 语言和集成 API 来使策略评估成为可能。

---

如何将 OPA 应用于我们的 IaC 检测中呢？![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfs7t3icnNQiasXQezjxFP2qw3PHkdFByUPcvZYMR5s3vCeGBx0ib9TxPjLDKIfFMxZGnCoL9znRiaeA3w/640?wx_fmt=png)将OPA应用于IaC扫描的思路：

* 规范化扫描文本对象，抽象成固定的模版类。
* 将规则转化为 .rego 策略文件。
* 按照不同的类别命名 rego package, 来区分策略级别。

···

今天的公开课就分享到这里啦，由于文章篇幅问题不能将所讲细节一一列出，更多内容详见文末**「直播录屏及PPT」**。

---

> ❝
>
> 需要直播录屏、PPT的小伙伴请私信微信公众号**「CT Stack 安全社区」**：
> 第三期直播录屏、第三期PPT 即可获取。
>
> ❞

**扫码添加小助手，一起学习、共同进步！**

![](https://mmbiz.qpic.cn/mmbiz_png/NtPFQib0CNabiaAiaCKn4Gj60LeAJYhtWJsgBAUnxFUV0dsqtlkOuhibUOglQKeXslRqkB3PNKbSH5BJHDLK0azkSw/640?wx_fmt=png)

---

问脉 Tools 社区版是长亭牧云团队孵化的一款开源容器安全检测工具集。目前已支持镜像/容器漏洞、逃逸风险、恶意文件、后门、敏感信息、弱口令、资产识别等扫描功能。

为了提供更优质的服务，我们同时提供商业版牧云·云原生安全平台。首推零侵入探针，采用 Agentless 方案进行部署，保证业务节点实现严格意义上的零侵入检测，让用户能够轻装上阵，轻松解决云原生安全问题。

---

精选回顾

[「问脉」底层架构大揭秘｜长亭科技·云原生安全公开课第二期](http://mp.weixin.qq.com/s?__biz=MzIzOTE1ODczMg==&mid=2247495192&idx=2&sn=a2a84cba86f8bc3988d191b8915d929f&chksm=e92cfabbde5b73ad586414e90552a15564e4cbd6b112ca65e7c6269f6d1abe11033a84020201&scene=21#wechat_redirect)

[云原生安全趋势演进大揭秘｜长亭科技·云原生安全公开课第一期](http://mp.weixin.qq.com/s?__biz=MzIzOTE1ODczMg==&mid=2247494949&idx=1&sn=72a3c3ece72df8ea82d70f30a1460012&chksm=e92cf986de5b70905331cf6a82819a28ab14180fdf8a05b34ab3272cd71abc1bd8937e3bb8da&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpRbyCZNQHcXYS8ZnGg2SLZEey7tficiaJdAaAMsDMX62UV6ClbgNUF6CMyay80xjnX9qrCRKLHHGnIg/0?wx_fmt=png)

CT Stack 安全社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpRbyCZNQHcXYS8ZnGg2SLZEey7tficiaJdAaAMsDMX62UV6ClbgNUF6CMyay80xjnX9qrCRKLHHGnIg/0?wx_fmt=png)

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