---
title: AI在代码中埋的三颗雷，快要爆了！
url: https://mp.weixin.qq.com/s/rozL6Hab7t6jByU_fCZbxg
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:41:03.282614
---

# AI在代码中埋的三颗雷，快要爆了！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f6MknOKr7AETNOY2JoDDwTDb6vFF6cNu6bibHJ0jpYhC6kWIFSnmWMsP7frWvXmXHUF26ibvOnqOElZOXOzxTU4A/0?wx_fmt=jpeg)

# AI在代码中埋的三颗雷，快要爆了！

AI与代码安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于想躺平的程序员
，作者躺平的程序员

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6CJ6NkwzOEibLEWj7tr0n7eQrebAIxwmiatgmxUS95wReg/0)

**想躺平的程序员**
.

人生短短三万天，躺平一天算一天！

**0****1**

**完美代码**

张大胖一上班，就看到了小梁和小王昨天晚上发来的两个Code Review请求。

张大胖先打开了小梁的代码，这是要并发调用三个服务（用户资料、最近订单和忠诚度状态）， 然后把结果汇集起来，用于在用户仪表盘中展示。

张大胖快速看了一下代码：写得挺漂亮的嘛！

```
@Servicepublic class DashboardService {    private final ProfileServiceClient profileClient;    private final OrderServiceClient orderClient;    private final LoyaltyServiceClient loyaltyClient;       public UserDashboard aggregateDashboardData(UUID userId) throws ExecutionException, InterruptedException {        CompletableFuture<Profile> profileFuture = CompletableFuture.supplyAsync(() -> profileClient.fetchUserProfile(userId));        CompletableFuture<List<Order>> ordersFuture = CompletableFuture.supplyAsync(() -> orderClient.fetchRecentOrders(userId));        CompletableFuture<LoyaltyStatus> loyaltyFuture = CompletableFuture.supplyAsync(() -> loyaltyClient.fetchLoyaltyStatus(userId));        CompletableFuture.allOf(profileFuture, ordersFuture, loyaltyFuture).join();        return new UserDashboard(            profileFuture.get(),            ordersFuture.get(),            loyaltyFuture.get()        );    }}
```

利用了现代Java的特性，使用 CompletableFuture 协调异步调用。

张大胖又打开了小王的代码，processMessage 并行调用两个外部 API（Promise.all），然后依赖返回结果更新数据库。

```
//简化版代码async function processMessage(message) {  const [result1, result2] = await Promise.all([    callExternalApi1(message.data),    callExternalApi2(message.relatedId)  ]);  await updateDatabase({ result1, result2, message });  }
```

代码写得也很漂亮，张大胖上午忙得四脚朝天，匆匆地看了一眼，就Approve了。

不久以后，经过功能测试的代码进入了CI流水线，然后就进入了生产系统。

闲下来的张大胖到茶水间倒水，猛然间想起了小梁和小王的代码：这不对啊，我们团队写代码不是这样的啊！

代码也太干净了，就像教科书上的代码，或者网上博客的示例代码。

仔细琢磨一下，代码中其实埋了三个雷：

**地雷1：线程问题**

小梁的代码用的supplyAsync()，但是却没有指定自己的线程池，这意味着所有的任务都跑在默认的ForkJoinPool 上。

ForkJoinPool 是为CPU密集型任务设计的，而这里的网络调用是阻塞I/O！在高负载下，这些阻塞调用可能会把线程全占满，嗯，后果非常可怕啊。

团队不是早有规定了吗，I/O任务必须用专门的虚拟线程执行器。

**地雷2：失败处理**

代码没有给出超时策略，如果 loyaltyClient 挂起了 30 秒，整个请求会被它拖住。

如果其中一个 future 失败会怎样？allOf 众所周知是要么全部成功要么失败的。

**地雷3：违反了团队约定**

小梁直接使用构造函数创建UserDashboardDTO，但是团队规范要求用静态工厂方法UserDashboard.from(profile, orders, status) ，这样可以统一处理 null、保证对象不可变。

小王更是犯了一个低级的错误：竟然假定调用API1和API2这两个操作互不影响！这两个API可是有依赖关系的啊。

张大胖把小梁和小王找来，质问他俩是怎么回事：“你们也是有几年经验的程序员了，为什么还会犯这种低级错误？”

两人支支吾吾了半天：“最近太忙了，我们用AI生成了一些代码。”

张大胖背后一凉：“坏了，AI在代码中埋的三颗雷，快要爆了！赶紧回滚代码，fix bug！”

AI写得飞快，但只是会照着教科书写一个“看起来很对”的版本，但它不知道团队的一些约定，更是会忽略分布式系统至关重要的容错策略，例如超时、降级、部分响应等等。

这些小细节往往是埋雷的根源。

**0****2**

**我们该怎么办？**

AI其实就像一个超级聪明，有无限耐心，但没经验的实习生。

它严重缺乏品味、智慧和架构远见。

你让它干啥它都干，但它不懂背景、不懂约定，也不懂“为什么要这么做”。

要想让AI真正帮上忙，需要你来带，就像你指导新人干活儿一样。

![](https://mmbiz.qpic.cn/mmbiz_jpg/f6MknOKr7AHq8jazdMgxmylCUibzANY64gcBTPIlp3tb192icbPianZuibcotbm26kYWztbOKY7cIknObX6YsNM0hw/640?wx_fmt=jpeg&from=appmsg)

**1.以人为主导的架构设计**

别一上来就让AI写代码，先自己想清楚几个问题：

* 这个功能要怎么融入现有系统？
* 对下游应用有什么影响，失效的情况有哪些？
* 最简单、最优雅的数据流是什么？
* 需要创建新服务，还是扩展现有的？

做出了这些关键的决策以后，才开始向AI下命令来实现。

**2. 给AI喂上下文**

不要被动地使用AI，盲目地接受AI的输出，一定要给它提供上下文（规则、约定、示例代码）。

（1） 把团队约定告诉AI

例如 “我们对 DTO 使用静态工厂方法：UserDTO.from(user)。

错误用自定义 ApiServiceException 处理。

所有异步方法必须返回 CompletableFuture。

（2）提供示例

给它一段项目中已有的优质代码片段，作为风格范例。

（3）明确定义目标

例如 “我要在 Spring Boot 中实现一个 REST 控制器端点，它是非阻塞的、支持这三种查询参数，并调用 UserService。”

这样它写出来的东西才不会“跑偏”。

**3. 深度调试**

遇到Bug时，我们现在的第一反应就是把错误日志扔给AI，让它去修复。

这确实快，但治标不治本。

更好的做法是：把 AI 作为“提问伙伴”，用它来推动自己深入分析，而不是仅仅获得一个Bug Fix。

* 不要只说“修复这个 NullPointerException”，而问：“在并发 Java 环境中，可能导致这个 NPE 的五种常见竞态条件是什么？”
* - 不要只问“为什么慢？”，而问：“请分析这段代码的内存分配模式，有没有降低堆压力的机会？”
* 不要只说“重写这个”，而问：“在这个特定任务中，使用 CompletableFuture 与 Java 21 的 Structured Concurrency 的权衡是什么？”

用 AI 提问来强化自己的技术思考（深挖根因、比较方案、权衡利弊），把工具变成学习催化剂而非快捷键。

**4.工匠打磨：从正确到优雅**

普通代码和卓越代码之间的最大差别是工艺感。

这最后的10%是AI做不到的，也是人类程序员介入的价值所在：把AI生成的代码变成别人阅读和维护都很愉悦的作品。

(1) 重命名：

把 data\_list 改为 activeCustomerProfiles。AI 给出的是泛化名称，你赋予它们领域特定的意义。

(2) 添加“为什么这么做”的注释

删掉无用的注释（如 //对users进行循环遍历），改为解释为什么用这种方式实现（例如 // 这里用手工循环是因为对象较大，性能更优）。

(3) 简化并美化

拆分长函数，对齐参数以提升可读性，确保代码有着流畅的逻辑，能清晰地讲述一个“故事”。

**0****3**

**写在最后**

写代码这件事，从来就不是“谁敲键盘更快”的比赛。

AI确实能帮我们省下很多时间，但它不会替你理解复杂的业务、权衡架构的取舍，也不会替你承担线上事故的后果。

真正厉害的程序员，不是拒绝用AI，而是能驾驭AI。

用它写代码，而不是被它牵着走。

让AI负责“速度”，让人类保留“判断”和“品味”，那才是我们的价值所在。

本文改编自：https://ai.gopubby.com/theres-a-phantom-author-in-your-codebase-and-it-s-a-problem-0c304daf7087

这篇文章内容很好，就是读起来费劲，我把它改写了一下，加了一点儿故事进去，希望大家喜欢。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/gbFHCWYSgF4dWsMlOVnEDAzyugosHQFicRvViccFWcTR87YWA0ZVg0p2tXglgnXEQElwnIhhmpEwulCbzCbzKb1A/0?wx_fmt=png)

AI与代码安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/gbFHCWYSgF4dWsMlOVnEDAzyugosHQFicRvViccFWcTR87YWA0ZVg0p2tXglgnXEQElwnIhhmpEwulCbzCbzKb1A/0?wx_fmt=png)

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