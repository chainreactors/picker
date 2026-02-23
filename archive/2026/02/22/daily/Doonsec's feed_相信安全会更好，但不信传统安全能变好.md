---
title: 相信安全会更好，但不信传统安全能变好
url: https://mp.weixin.qq.com/s/D6J5M-MXfifWJtFGFlNV4Q
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:18:59.123623
---

# 相信安全会更好，但不信传统安全能变好

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/z0u4bSRUopPKMtXliaaibZfa4LXeWicNPPMjRvseECfIuBfpkdkDt4SOC0l1VmUkvLPRskVxs1UTUbbPvnwmy8JiatibOKonicQmicxLxNQicia2jVFk/0?wx_fmt=jpeg)

# 相信安全会更好，但不信传统安全能变好

原创

heyong
heyong

AI安全圈

![]()

在小说阅读器中沉浸阅读

很久没有认真地写一篇长文了，现在重新提笔来写想必大家也都知道原因了。对，就是昨天的那个网图。

![](https://mmbiz.qpic.cn/mmbiz_png/z0u4bSRUopOyB0Oe90aickQY0icI3zOJdY0MaGEBJOTJ4J31CbWOEvhQIDVP11ib1UNgvXQqeSeDdx0sDHn9qwuOyugup8p5ibWOiaEMzcaib65ew/640?wx_fmt=png&from=appmsg)

我想在这篇帖子里，说明白两个事情：

1. AI只会越来越强，传统安全很难变好。
2. Anthropic在claude上所做的安全，远没有我们想的那么简单。

1

先说第一个吧。

之所以出现昨天这样的局面，其实一点也不奇怪。

主要原因是大多数人平常对AI安全关注太少了，现在猛地有人弄出点动静，像深夜窜出来炸街的黄毛小子。

去年7月份的时候我就在说（没看过的同学可以阅读[安全行业正在经历的"iPhone时刻"](https://mp.weixin.qq.com/s?__biz=MzU5NzQ3NzIwMA==&mid=2247486784&idx=1&sn=1032a1e89f730b7ec38f1acfe2006e76&scene=21#wechat_redirect)），判断的逻辑很简单：一个像claude ai这样的顶级程序猿，是不可能干不好安全这事，区别只是需要再花费多少时间投入到安全领域而已。

当Anthropic 发布"Claude Code Security"公告时，这只靴子就宣告落地了。在未来很长的一段时间内，它都将影响着安全行业，带来潜移默化的改变。

我也是做传统安全出身的，杀软、防火墙、攻防、认证、审计 ......开始我也不信AI会改变安全行业，但当我看到外面越来越多、成规模、成建制的新型团队的案例，我不得不信。

做程序猿也好，做安全也好，本质上是在做事，通过做事来体现这个岗位的价值，从而在市场中存活下来。

可是，未来呢？你有没有想过，未来的某天，这些事情它没有了，或者从每年100件变成了每年3~5件，传统安全它还能好吗？

有时候，我想对传统安全赛道上创业的朋友们说，放弃吧停止投入，这条路是走不通的，前面没有路了。但话不好听，到嘴边又吞下去了。

可以预判的是，AI正在逐步改变未来，和软件蚕食世界的逻辑一样。

随着底层大模型能力的增强，现在我们在用的几十、几百个IT系统，会逐渐减少，当能力逐步由一个大模型系统替代时，当大模型自身具备安全能力时，那些曾经令人烦恼的弱口令、高危端口，以及那么多修复不完的漏洞，也会逐步收敛或消失。

AI先是蚕食掉可以软件化、系统化的一部分，比如正在进行的AI Coding；接着是它的上下游，上游的产品需求、架构设计，下游的测试部署、日常运维。

与此同时，它也会从一个岗位、一个行业，向其他岗位、其他行业拓展，从程序猿岗位，拓展到测试工程师岗位，从技术工拓展到客服、接待员。。。。就像我们现在关注的具身智能是软件智能的延伸一样。

从对某个行业流水线的40%替代，到85%替代；从替代某个行业，到替代大多数行业的95%，最终形成人机协同的局面。

当然，这个过程的演进相对是比较长的。是3~5年？5~10年？还是50~100年更久？难以判断。

AI进化给我们带来的影响，不仅仅说技术层面的，更重要、更尖锐是生产力、组织形态、乃至社会结构的改变，这才是我们要花大力气去长远考虑的。

2

说完了第一个问题，接着来说第二个。

今天Anthropic 给网络安全公司带来的还仅仅是股价下跌，但当我们醒来发现AI的强大，想模仿它抄袭它，才发现它做过的安全工作，也是真正的护城河。

对于Claude Code Security，Anthropic 在公告里明确地说了传统的规则不行，它采用的是类人类的方式来做的：

> 公司没有扫描已知的模式,而是以人类安全研究人员的方式阅读代码并了解其原因:了解组件如何交互,追踪数据在应用程序中的移动方式,以及发现基于规则的工具所忽略的复杂漏洞。
>
> 每一项发现都经过多阶段验证流程后,才联系到分析师。Claude 重新审视每个结果,试图证明或反驳自身发现,并筛选出误报结果。研究结果同时被标注严重程度评分,以便团队首先能够专注于最重要的修复措施。
>
> Claude Code Security 会识别问题并提出解决方案,但开发者始终会主动提出。

代码审计和 0 day漏洞挖掘只是Claude安全中很小的一部分，如何训练出Claude的安全能力，做好Claude自身的安全性才是整个安全里面的重头戏。作为安全研究人员，不要被网络的言论带偏了。

Claude做了哪些呢？这里，我抛砖引玉，简要地列举几个在个人视角下发现的关键点供诸位参考。

1.语料的安全合规

您且看下面的这段描述：

> Claude的训练数据包括截至 2025 年 5 月的公开互联网信息、第三方非公开数据、数据标签服务和付费承包商提供的数据、选择使用其数据用于培训的 Claude 用户数据，以及 Anthropic 内部生成的数据。
>
> 在训练过程中，使用了多种数据清理和过滤方法，比如去重和分类。
>
> 我们使用网络爬虫从公共网站获取数据，爬虫遵循行业标准做法，遵循网站robots.txt指令，说明是否允许爬取其网站内容。
>
> 当确实有不能访问受密码保护的页面或需要登录或验证码验证的页面，我们对所使用的训练数据进行尽职调查。
>
> 我们的爬行器运行是透明，网站运营者可以轻松识别其网页爬取时间，并向我们传达他们的偏好。

先不说Anthropic 上述内容说的是真是假，但仅仅就构建安全合规的语料这一项，很多公司就被拦在门外了。

有了这些数据，再经过数据预训练后，Claude再经过了大量后期训练和微调、RLHF等，最终成为一个有用、诚实且无害的AI助手。

是不是有点明白“无害”两个字的份量了？但是，还有许多安全问题是Claude需要考虑的。

2.泛安全领域的保障

主要有生物武器、儿童安全、致命武器、自杀和自残、恋爱骗局、追踪与监视、暴力极端主义与激进化、政治价值观等（如下图截取的部分大纲）：

![](https://mmbiz.qpic.cn/mmbiz_png/z0u4bSRUopOkhO8RhlnMIlZBe6To0fDrkMmhgYhn4KIyAnls2SvhHFzicj1mJRicCJd8oe073ReXkxAjicVtVzaA7lricNxFRbCPKrK1SYbRQMs/640?wx_fmt=png&from=appmsg)

3、技术验证与控制

训练完了，不一定就是可以拿出来用的版本。Anthropic又做了以下几点：

* 训练的大模型，保留训练过程的多份快照版本，从中选择最安全的版本拿来发布
* 为了验证模型的能力，Anthropic让大模型参加多项安全竞赛（如下图翻译）

  ![](https://mmbiz.qpic.cn/mmbiz_png/z0u4bSRUopOEWJl9zqrjR9Sh3riaFibSgaCj17vHiboxn3ib7NzakCe8sqpONBvlOKt9XR2WqIkp7hFWJKW7U2s4BwPdt3oGol1ZKSxQMKGpZLQ/640?wx_fmt=png&from=appmsg)

* 比赛与人工的数据对比

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/z0u4bSRUopMGclx9GRbKIepUQ8oLhk7aN9yJbCicTleaJpwa2oQibudfCoZCESuKqcjyVibIiajhIcKkTANm7CTVUhqdm1c6XOGrLNeD3p0yw1Q/640?wx_fmt=png&from=appmsg)

* 即使是Claude Code Security，也是小范围试用，提交单子等审批。

  ![](https://mmbiz.qpic.cn/mmbiz_jpg/z0u4bSRUopNiaXzn7Q0DKjGnShvujXsrKB0f7kcbibvxQwAH9LWSAy77wYUDia79br5rKnPfBEQPBAgYQ63iatfaD1xPUchzWO4gH2iaP7zPAr6Y/640?wx_fmt=jpeg&from=appmsg)

  因为它知道，AI安全的两面性，被好人使用能造福群众，被坏人使用能造成更严重的破坏。

抓紧时间学习AI安全吧，因为你是安全人，要和另一部分人抢夺漏洞的挖掘和修复权！

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/0R80na6wzXdZWBKECSwo8H5S6LNZvXaLNemfgTALpBNqL3VpUlA3mQtwfrEoIh2LHb1zJuv8A5z0Jo60tH7pgw/0?wx_fmt=png)

AI安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0R80na6wzXdZWBKECSwo8H5S6LNZvXaLNemfgTALpBNqL3VpUlA3mQtwfrEoIh2LHb1zJuv8A5z0Jo60tH7pgw/0?wx_fmt=png)

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