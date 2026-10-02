---
title: 直播回顾 | 企业开始真正用 AI 后，安全该怎么测？
url: https://mp.weixin.qq.com/s/A_ehlc8cLzSVWea0JM46bg
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:43:48.027546
---

# 直播回顾 | 企业开始真正用 AI 后，安全该怎么测？

# 直播回顾 | 企业开始真正用 AI 后，安全该怎么测？

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX0ib18Eqichf1icGFpHQ5rBnK71acFojmyEkPichplM0P1HulAv2DXFibO24TPxPwE9woUqUZV3bEoeJDvKuMjhNpCg2iaUBcv9ggbKI/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0NlGcH1IBGsXKsic4dk0oQwv8RWxibXbxibrQE2bowgqF1Ny4fEyJKDwClpC3U6snnGhXucdrIW3K5OEStdRpAd8dJKqficOtick2M/640?wx_fmt=png&from=appmsg)

直播精华回顾

当大模型和Agent 真正进入企业业务，安全问题已经不再只是“模型会不会说错话”。敏感数据是否会进入模型、第三方 AI 服务是否可信、Agent 会不会越权调用工具、执行过程能不能被追溯，都开始成为企业必须面对的新问题。

本期播客内容整理自FreeBuf线上直播研讨会《企业开始真正用 AI 后，安全该怎么测？》。

直播围绕 4 个核心问题展开：企业使用 AI 后风险从哪里出现、传统安全测试为什么不够、Agent 开始调用工具后边界如何变化，以及企业怎样把 AI 安全评测真正放进日常研发与上线流程。

扫描二维码，至知识大陆APP可收听完整播客内容：

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0SJUuR47aAGTytFDqLvLcztdCPQNhmTiazIic52pwB0CEPGIhok1deHnxBgYX6XNAtzJP6M1RdErQYuGbf2vicIN29uff0ZgKe9U/640?wx_fmt=png&from=appmsg)

以下是本期核心观点。

***01 企业开始用 AI 后***

***风险首先从哪里出现？***

企业真正把大模型、AI 应用或 Agent 接入业务之后，风险面会从单纯的“模型输出”迅速扩展到数据、权限、第三方服务与真实业务动作。

直播重点讨论了几类典型风险：敏感数据泄露、Prompt 注入与越狱、第三方模型或 API 风险，以及 Agent 工具调用与权限越界。

不同企业场景的重点可能不同，但一个共同变化是：AI 一旦开始连接内部数据、系统和工具，安全边界也必须随之重新定义。

对企业来说，第一步不是一次性把所有风险都测完，而是先明确真实使用场景：哪些数据会进入AI、哪些系统会被调用、哪些权限会被授予，再据此判断哪些风险最需要优先验证。

***02 传统安全测试为什么***

***不一定能发现 AI 系统的问题？***

传统Web 安全测试已经形成较成熟的方法，但 AI 系统的风险并不只存在于接口、漏洞或单次输入输出中。

多轮对话中的行为偏移、Prompt 注入、敏感信息泄露、越权访问、工具调用等问题，往往需要放到连续交互和真实业务链路里才能暴露出来。

因此，AI 安全测试不能只看“最后回答是否正常”。测试对象还要进一步延伸到交互过程、上下文变化、数据访问、工具调用和权限使用。

对于第一次开展AI 安全评测的企业，更实际的做法通常是从高风险业务场景入手，先把最关键的模型、数据、权限和执行链路测深，再逐步扩展覆盖范围。

***03 Agent 开始调用工具后***

***安全边界发生了什么变化？***

Agent 和普通大模型最大的区别，是它开始真正“做事”：读文件、调接口、访问内部数据，甚至执行命令。从这一刻开始，安全关注点就从“回答对不对”进一步变成“行为是否在预期边界内”。

本场重点讨论了权限过大、间接Prompt Injection、调用不该调用的工具、执行过程无法追溯、高风险操作缺少人工确认等问题。

一个非常关键的判断是：最终结果看起来正常，并不意味着整个执行过程就是安全的。如果Agent 在中间调用了不该调用的工具、访问了不该访问的数据，即使最后输出没有明显异常，仍然应被视为需要关注的安全问题。

企业真正需要建立的，是“能做什么”和“应该做什么”之间的边界：哪些操作可自动执行、哪些需要人工确认、哪些权限只能临时授予，以及每一步是否可审计、可追溯。

***04 企业真正落地 AI 安全评测***

***最难的是什么？***

企业落地AI 安全评测，难点往往不只是缺少工具。更现实的问题包括：高风险场景怎么选、测试 Case 从哪里来、什么结果算失败、业务团队如何配合，以及评测结果怎样真正进入研发和上线流程。

直播进一步讨论了几类关键能力：高风险业务场景库、AI 安全测试 Case、持续评测机制、Agent 权限与审计，以及评测与研发/上线流程的结合。

AI 安全并不是“上线前做一次测试”就结束。模型版本、Prompt、工具、权限和业务场景都在持续变化，相应的安全评测也需要跟着变化。

更成熟的做法，是把可自动化的测试逐步纳入研发流程，同时把高风险行为判断、权限边界设定、异常结果研判等关键环节继续留给安全人员。

***05 结语***

• AI 风险正在从“模型输出”向数据、权限、工具和真实业务动作扩展。

• AI 安全测试不能只看最终回答，还要验证多轮交互、数据访问、工具调用和执行过程。

• Agent 的安全核心不是简单限制权限，而是建立可控、可审计、可追溯的行为边界。

• AI 安全评测应从一次性测试走向持续机制，并逐步进入研发和上线流程。

如果你也在关注模型安全评测

Agent 安全、Prompt 攻击

工具调用或 AI 红队测试

可以添加 FreeBuf 官方助手「小星星」

回复「AIBEAT」进入对应交流群

如果你在AI 安全、安全运营、漏洞情报等

方向有实践经验

或有想和同行深入讨论的话题

也可以添加小星星，回复「直播报名」

👇

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2oeIu7ctYJFznyeH8AXur5zlNomntNibbo0OTfedtaAMaWM04DZ6K17GG34aoAiaLNYNY89khVzDG0icP6MXUoR7kiabFiadH7v4u8/640?wx_fmt=png&from=appmsg)

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bRSnFgE3WPnpU3s0eVp7QdRn9fI63ymmlhTHpsMBL2VnRMPZQy9DhvZasynJV1ia534sF84uxxKKulzDlBibjrQ7ylDiaickrCIY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651347479&idx=1&sn=1cf9c858a30d0b7af06d196002bd2913&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yychgqrdWpeazfdwAxHj4T9ILWI3fl6IUFOJEIcOHVC5ia3VjkrzuJLbJ4krtMqID23cDDy61ykbbic6NSXcVHRBvrW1jxxOU4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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