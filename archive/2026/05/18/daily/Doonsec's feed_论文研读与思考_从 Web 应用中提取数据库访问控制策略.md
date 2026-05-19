---
title: 论文研读与思考|从 Web 应用中提取数据库访问控制策略
url: https://mp.weixin.qq.com/s/U4G6nPSU910uPZOF8PO8og
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:00:54.115527
---

# 论文研读与思考|从 Web 应用中提取数据库访问控制策略

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIzE9kYR7QqibUianCLMDVhwQuHKCV4CNR6wWe4U5x6P7H7ENiaIfHUtUGpxzM83iauS6Ksvd9EStoKNtA5HTj0GGl5ibfpeskricOg88/0?wx_fmt=jpeg)

# 论文研读与思考|从 Web 应用中提取数据库访问控制策略

QIU
QIU

玄枢战队-Arcane Hub

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

原文标题：Extracting Database Access-control Policies From Web Applications

原文作者：Wen Zhang, Dev Bali, Jamison Kerney, Aurojit Panda, Scott Shenker

发表信息：OSDI 2026 / arXiv:2411.11380v2

核心系统：Ote

关键词：访问控制策略抽取、Web应用安全、数据库查询、Concolic Execution、SQL View Policy、Rails应用

# 论文概览

 这篇论文关注的是Web/API授权测试里一个更底层的问题：请求成功了，不一定说明它应该成功。普通用户访问他人数据时，返回200可能是合理的公开访问，也可能是真正的越权。难点不只是构造请求，而是判断这个结果有没有越过应用本身的授权边界。

  作者提出的系统叫Ote。它不直接从某一种漏洞模式入手，而是从Rails Web应用实际发出的SQL查询中，反推出应用隐含的访问控制策略。具体来说，Ote会探索Web应用的执行路径，记录SQL查询和触发这些查询的条件，再把它们整理成SQL view形式的policy，让审计者看到“什么身份、什么数据关系下，用户能访问哪些数据库内容”。

论文在diaspora\*、Autolab和The Odin Project三个真实Rails应用上评估了Ote。结果比较有说服力的一点是：Ote能把大量执行路径和conditioned queries压缩成可人工审查的SQL views，并且在和手写policy对比时，发现了过宽、过窄以及权限检查失效等具体问题。

# 一、研究问题、目标与方法

## 1.1 这篇论文真正想解决什么

很多Web应用没有一个集中、清楚的访问控制策略文件。真实代码里，权限逻辑往往散在controller、model、scope、helper和SQL查询中，最后由这些零散判断共同决定用户能看到哪些数据。

问题在于，这些判断不一定都可靠。看到代码里有access check，并不代表边界就是对的：检查可能写错字段，查询可能漏掉owner条件，外部库也可能让原本的检查失效。审计者真正需要知道的，不只是“有没有检查”，而是“应用最后实际允许访问了哪些数据”。因此，这篇论文把重点放在访问控制策略的恢复上。它关心的不是某一种固定漏洞模式，而是如何把散在代码和查询里的授权证据整理出来，让人能看清一个已有系统真正实现了什么访问边界。

1.2 为什么用SQL view表达policy

  Ote最终把策略表示成SQL views。这样做比较自然，因为这类Web应用的数据访问最终都会落到数据库查询上：哪些表能查、哪些行能看、哪些字段能暴露，都会体现在SQL查询和查询条件里。

  相比自然语言描述，SQL view更具体，也更容易和应用实际行为对照。它能把“某个用户在某种角色或资源关系下可以访问哪些数据”表达出来，方便后续人工检查。

## 1.3 Ote的整体做法

Ote的路线并不复杂：先探索应用如何访问数据库，再把这些访问行为整理成policy。它通过concolic execution执行Web handler，记录路径条件和SQL查询；接着把记录转换成conditioned queries；再生成SQL views；最后做剪枝和合并，得到一组更短、更适合人工审查的views。

  这套流程的重点是保留“查询在什么条件下发生”。因为同一条SQL查询，在不同用户身份、资源关系和业务状态下，含义可能完全不同。Ote不是只收集SQL本身，而是把触发查询的上下文一起记录下来，再转换成可以审查的访问控制策略。

# 二、具体方案研究

## 2.1从路径到conditioned query

Ote开始分析前，需要用户先声明要分析的handler，以及request参数的名字和类型。同时，系统还需要一些数据库约束，比如唯一性、包含关系、非空关系等。论文里提供了约束生成工具，可以自动生成大部分常见约束，但仍然需要人工补充一部分和应用逻辑有关的约束。

真正执行时，Ote使用的是concolic execution。它一边运行真实程序，一边记录和输入相关的符号条件。这样做的好处是，系统不必完全静态理解Rails框架，而是顺着真实执行路径走。程序遇到分支、数据库查询或输入相关操作时，Ote会记录相应条件，并让求解器生成新的输入，继续探索其他路径。

这里最重要的中间产物是conditioned query。它记录的不只是“应用执行了哪条SQL查询”，还包括“这条SQL是在什么条件下执行的”。这些条件可能来自session中的user\_id，也可能来自数据库中的role关系、字段是否为空、权限检查是否通过等。这个设计很关键。对访问控制来说，查询本身并不够。同一条SQL，在不同用户身份、资源关系和业务状态下，含义可能完全不同。Ote把查询和触发条件绑在一起，后面才能把这些行为整理成更接近真实授权语义的policy。

## 2.2为什么这个方法在Web应用里能跑起来

作者的一个观察是：Web应用整体很复杂，但真正决定SQL查询是否发出的query-issuing core往往没有那么大。页面渲染、HTML模板、UI分支可能很多，但影响数据库访问的通常是少数判断：角色是否存在、当前用户是不是owner、资源是否属于某个组织、某个查询结果是否为空等。

这给Ote留下了空间。它不需要理解整个Web应用的所有行为，只要抓住查询发出前后的关键条件，就能恢复出相当一部分访问策略。换句话说，Ote不是试图解释整个应用，而是重点关注“哪些条件会让应用发出哪些数据库查询”。

当然，这个假设不是万能的。当路径数量很多时，concolic execution还是会遇到路径爆炸。论文里Autolab的Assessments#show就是例子，这个handler跑了很久也没有完成。作者也承认，后续可能需要selective constraint generation或近似backward slicing，把

  和查询无关的分支剪掉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIy4m3ZhGCc28umTQTicOddEDeWbNW9GbpmuR5ej8a2avvrEKf9yaiaib2oRxFuia3vzHnJRfQIpsjrbEByHJzhbedaaxxZMwe3dZJQ/640?wx_fmt=png)

图1：Ote的policy extraction workflow

从handler声明和数据库约束出发，经过concolic execution、conditioned queries、view生成与剪枝，最后得到policy。

## 2.3 SQL view的好处和边界

SQL view是这篇论文里很关键的表达方式。它比自然语言policy更容易检查，也比原始执行日志更容易读。对审计者来说，view直接展示了当前用户可以访问哪些表、哪些行、哪些字段组合。

但SQL view也有边界。Ote目前主要支持project-select-join查询，对negation、复杂SQL、排序、字符串操作和写操作支持有限。所以作者没有把结果说成绝对正确，而是反复强调：Ote不保证complete and tight。它可能漏掉部分路径，也可能因为SQL近似导致策略变宽或变窄。

这一点反而让论文更可信。Ote不是替人直接判断“安全/不安全”，而是把原本隐含在代码里的访问逻辑摊开，变成可以检查、比较和继续修正的policy。

## 2.4工程实现

 Ote的实现不是简单的规则扫描。它的concolic driver和policy generator用Scala3实现；SQL解析和关系代数转换使用Apache Calcite；约束求解使用Z3；执行器基于修改后的JRuby；view pruning则复用Blockaid。

这些组件对应的是几件不同的事：JRuby负责让Rails应用在可插桩环境中运行，Z3负责生成新的路径输入，Calcite负责处理SQL和关系表达，Blockaid负责判断哪些views可以被已有policy覆盖。也就是说，Ote本质上是把程序执行、数据库语义和策略检查接在了一起。

## 2.5为什么还需要人参与

Ote抽出来的policy往往偏紧，因为它忠实记录了当前代码路径中的条件。但有些条件只是实现细节，不一定是真正的隐私边界。比如一个profile在很多场景下都能访问，自动抽取可能生成很多views；如果审计者知道这些profile大体公开，只是少数字段敏感，就可以手动加入更宽、更简洁的view。

论文把这个过程叫policy broadening。人加入一个更宽的view后，Ote再运行pruning，把被覆盖的冗余views删除。这个设计比较现实：工具负责把隐式行为展示出来，人负责判断哪些条件应该保留为真正的安全边界。这样既避免完全依赖人工读代码，也避免自动工具替人下过度确定的结论。

# 三、实验方法与性能评估

## 3.1实验对象

论文选了三个真实Rails应用：diaspora\*、Autolab和The Odin Project。diaspora\* 是社交网络应用，用户规模超过85万；Autolab是课程作业管理平台，被20多所学校使用；Odin是Web开发学习平台，用户超过百万。diaspora\* 和Autolab比较特殊，因为作者以前给它们手写过policy，所以可以直接比较自动抽取结果和人工策略的差异。Odin则是一个新应用，用来看Ote在没有手写经验的情况下是否仍然可用。

实验准备并不是零成本。用户需要声明handler和参数类型，提供数据库约束，还要对少量代码做参数化查询改写。数据库约束方面，自动工具生成了超过80% 的约束，剩下的需要人工补充。也就是说，Ote更像一个面向审计的分析系统，不是点一下就跑完的扫描器。下表能看出Ote并不是零配置扫描器，但自动约束生成已经覆盖了大部分常见约束。

![](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIwicZjaQysZkq0tdicriaiciceK1ougoJibuPCI2XVRkGFYMB2nh76Cg90xxekBCLn273RJ53sI5RicKQWYkSlu89acicOrNoZSe6icN22M/640?wx_fmt=jpeg)

图2：数据库约束数量统计

## 3.2主结果

实验里最值得看的结果是压缩能力。Ote可以把非常大的路径空间和查询记录压缩成可人工审查的view数量。比如diaspora\* 的People#stream handler探索路径超过一百万，conditioned queries超过三百万，但最后SQL views被压缩到148个。这个数量还可以，但和原始路径日志相比已经可读得多。其他handler的最终view数量通常在个位数到几十之间。论文总结，最终policy views在24到140之间，基本还在人可以检查的范围内。

性能瓶颈的话主要来自路径探索和view pruning。最耗时的People#stream端到端大约十小时。view pruning也不便宜，因为系统要反复调用Blockaid判断view是否冗余，而Blockaid原本并不是专门为动态剪枝大量views设计的。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwZ4QRjQicW6nsCvO4PicaF8y0tg0oRv5PHR5BZibwcXZHLSxPqKtMy8icYJqV7w44CGwIRICAfF2IGJ4vYgoMpMIMm0HGwOMalicts/640?wx_fmt=png)

图3：主结果

## 3.3和手写policy对比

这篇论文最有说服力的部分，不是和某个漏洞扫描器比谁报得更多，而是和人工手写policy对比。结果显示，手写策略既可能过宽，也可能过窄。过宽的例子来自Autolab。手写policy允许course assistants访问disabled course中五类记录，但应用逻辑实际只允许instructors访问。如果这个过宽policy被拿去做enforcement，就可能给未来代码留下数据泄露空间。

过窄的问题也存在。diaspora\* 的手写policy漏掉了remote person的pod信息和某些通知相关数据；Autolab的手写policy漏掉了instructor对课程附件的访问。过窄policy不一定造成泄露，但会挡住正常功能，让enforcement很难落地。

![](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIxVXqBnVOcb9gVKDGJQxmN6nlQibkgOyueKF7T4E0XnX0RVmF957cIsucDczibNVHVibl9ibHtca6lxibicvhjn1r1kBrAicjg2cU9K8A/640?wx_fmt=jpeg)

图4：Table 3对比extracted policy和handwritten policy的view数量

## 3.4主要案例

论文里最有传播性的案例，是Autolab的隐藏access-check bug。作者在检查Ote抽出来的policy时发现，submissions相关views中没有检查assessments.exam字段。这很奇怪，因为Autolab本来应该禁止学生下载过去考试提交。继续追查后，问题出在lazy\_column gem的误用。开发者本来想把assessments表中的敏感列延迟加载，但配置时把列名写成了exam?，而实际列名是exam。结果就是，一个看起来正确的访问检查被悄悄变成了no-op。

这个例子说明，访问控制错误不一定是“完全没有检查”。有时检查写了，但字段名、库行为、框架语义或数据流让它失效。Ote不是直接扫描出这个bug，而是从抽取出的policy里发现预期条件缺失，再反向定位到代码问题。

# 四、论文的局限、未来展望和适用场景

## 4.1这篇论文没有解决什么

Ote的局限写得比较清楚。首先，它现在主要面向Ruby on Rails，而且依赖修改后的运行环境。方法思想可以迁移，但工程上不会很轻。

其次，它主要处理数据库读查询，也就是SELECT。写操作、副作用、复杂业务状态变化，不是这篇论文的重点。第三，concolic execution可能漏路径，也可能遇到路径爆炸。第四，SQL view policy对negation、复杂SQL、排序和字符串操作的表达也有限。

还有一个实际问题是policy comprehension。SQL views比原始日志好读，但复杂应用抽出来的views仍然可能很长。审计者还是要判断这些views到底是不是安全边界，哪些地方应该放宽，哪些地方不能放。作者也把自然语言解释、DSL和可视化放到了未来工作里。

## 4.2 启发

  这篇论文更适合被当作一种安全审计思路来看：复杂系统里的授权边界，很多时候不是写在一个清楚的policy文件里，而是散在查询、分支、角色判断和数据关系中。真正有价值的工具，不只是报告某个请求“可能越权”，而是把这个判断背后的依据摊开，让人能追着证据回到代码和数据库。

第一，授权问题不能只看有没有检查。代码里出现access check，并不等于最终边界正确。字段名可能写错，框架行为可能和预期不一样，查询条件也可能漏掉关键约束。Autolab那个例子就很典型：检查看起来存在，但实际没有生效。

第二，自动化结果应该方便人复核，而不是直接替人下结论。Ote抽出的SQL views不一定完美，但它把原来藏在应用里的访问逻辑变成了可以阅读、比较和讨论的形式。对安全审计来说，这比只给一个“高危/低危”的标签更有用。

第三，真实系统里的研究最好讲清楚具体问题是怎么被发现的。单纯说工具生成了多少条结果，意义不大；更重要的是，这些结果如何帮助人发现手写policy过宽、过窄，或者定位到一个原本很难注意到的权限检查失效问题。

所以，这篇论文不是教我们写一个Rails扫描器，而是它提供了一个很清楚的思路：先恢复真实应用里的隐式授权语义，再把它变成可审查的证据，最后用具体案例说明这些证据确实能帮助人发现问题。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/lmfaAJ5WqA1sUVs3bkh8pbJCu96cmwJ5JrqlejuC2Cia3prrW7Nia2b7dibjBwqjMnLV95ibBrOQkEbm9PIDw5IvFQ/0?wx_fmt=png)

玄枢战队-Arcane Hub

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/lmfaAJ5WqA1sUVs3bkh8pbJCu96cmwJ5JrqlejuC2Cia3prrW7Nia2b7dibjBwqjMnLV95ibBrOQkEbm9PIDw5IvFQ/0?wx_fmt=png)

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