---
title: 论文研读与思考｜XSSky：通过局部路径持久模糊测试检测XSS漏洞
url: https://mp.weixin.qq.com/s/pjQyfYPpu_jRHM3RqUt_cQ
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:46:19.687418
---

# 论文研读与思考｜XSSky：通过局部路径持久模糊测试检测XSS漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6TQOF8qUIxcibNEdKkBBUPhHrqEwtIJptGormEQDnh5RUcyPT54VVGyeLViaR1Ia3tQwBT7s6Y9hrvmezcCOyBllaEva8WLEKEPibI5aRMzaI/0?wx_fmt=jpeg)

# 论文研读与思考｜XSSky：通过局部路径持久模糊测试检测XSS漏洞

QIU
QIU

玄枢战队-Arcane Hub

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

原文标题：《XSSky: Detecting XSS Vulnerabilities through Local Path-Persistent Fuzzing》

原文作者：Youkun Shi, Yuan Zhang, Tianhao Bai, Feng Xue, Jiarun Dai, Fengyu Liu, Lei Zhang, Xiapu Luo, Min Yang

发表会议：USENIX Security Symposium 2025

这篇论文处理的是一个很现实的问题：PHP应用里的XSS路径很多，但现有工具面对带sanitizer的路径时，经常不是误报太多，就是漏掉真正能绕过过滤的漏洞。作者没有继续堆更复杂的sanitizer模型，而是把判断标准改成一个更硬的问题：如果一条source-sink路径真的危险，能不能为它生成一个具体输入，在本地执行后真正触发XSS。

XSSky的核心思路是：先让静态工具给出潜在source-sink路径，再把这条路径转成局部可执行的PUT，然后结合sink context感知、解释器反馈和浏览器bug oracle，去验证这条路径究竟能不能被具体payload打穿。它不再先假设sanitizer安全，而是把sanitizer放进真实执行链路里接受测试。

## 一、研究问题、目标与方法

1.1 核心研究问题与研究动机

作者先指出，PHP直到今天仍承载着大量在线网站，而XSS依然是最常见的Web漏洞之一。动态检测方法虽然能给出PoC，但容易受制于代码覆盖率、环境部署和业务流程复杂度；静态方法覆盖面更大，却常常要依赖人工建模去判断路径上的sanitizer是否足够安全。问题恰恰出在这里。现实系统中既有大量自定义sanitizer，也有很多“看起来做了过滤、但放错上下文”的情况。比如htmlentities()放在URL context中，并不能拦住javascript这类协议利用。也就是说，路径上出现sanitizer，并不等于路径真的安全。

作者因此把问题换了一个角度：既然静态工具已经能给出很多可疑source-sink路径，那么下一步不应该继续猜sanitizer是否可靠，而应该直接问，这条路径能否被构造出具体payload并最终触发漏洞。论文的目标，就是把XSS检测从“路径看起来危险”推进到“路径被实际利用确认”。

1.2 论文提出的关键问题与理论框架

要把这件事做成系统，作者先拆出两个挑战。第一个挑战是可执行性。静态工具给出的路径经常带着未定义变量、文件包含引入的外部状态、数据库查询得到的值，甚至还有对象方法调用目标不明的问题。如果这些undefined symbols处理不好，后面的fuzzing根本没法开始。

第二个挑战是有效性。XSS payload是否成立，强依赖sink context、HTML、URL、HTML attribute、JavaScript这几类上下文，对payload结构的要求完全不同；而sanitizer绕过也不是靠纯随机变异就能撞出来的，它需要知道到底是哪一段字符被拦住了、当前策略有没有继续越过新的过滤层。

基于这两个挑战，XSSky的框架如下：先依托TChecker找潜在路径，再由PUT Conversion Module把路径改造成Program Under Testing，随后由PUT Fuzzing Module识别sink context、选择exploit grammar、执行feedback-guided mutation，最后通过浏览器bug oracle判断漏洞是否真正触发。它的关键不是简单把静态和动态拼起来，而是把分析对象收缩到了“局部但可执行”的路径级程序片段。

1.3 论文的整体思路与主要贡献

论文的第一项贡献，是提出了一套面向PHP XSS的PUT转换机制。作者会先沿def-use链回溯变量定义，把能补回路径的语句拉回PUT；只有在静态上确实补不齐时，才把变量替换成fuzzer可控的临时变量。这让系统在“尽量保真”和“保证能跑”之间做了一个比较现实的折中。

第二项贡献，是把XSS fuzzing做成了context-aware的形式。系统先做sink context analysis，再决定哪些exploit grammar真正兼容当前上下文、哪些应该优先尝试。第三项贡献，则是引入解释器反馈：通过hook字符串比较和字符串修改函数，系统可以知道当前payload的哪一段被sanitizer命中，以及哪种变异策略正在产生效果。

最终，作者在20个应用上确认了60个真实XSS，其中31个属于sanitizer绕过，并额外发现了18个所有基线都没抓到的漏洞。就论文意图来说，它最想证明的不是“又做了一个扫描器”，而是“局部路径持久模糊测试”确实能成为连接静态路径定位与动态漏洞确认的中间层。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIxJphYKgBU4ecWgjRFjnDicldaicicCSSmHW8zwI8JCtiagUI4WsJwKYMnCx1Aibeeb1EpFj45n5amwJDicRh5SKSCfAcYLvyo96825E/640?wx_fmt=png&from=appmsg)

图1 四类sink context示意图

## 二、具体方案研究

2.1 核心方法设计

XSSky的流程分成两大阶段。第一阶段是PUT Conversion，把静态工具给出的路径改造成局部可执行程序，第二阶段是PUT Fuzzing，在这个局部程序上完成context判定payload初始化、定向变异和浏览器端漏洞确认。论文用Dolibarr的真实案例串起了整条线路：先定位路径，再补齐变量和函数定义，最后在PUT上通过编码绕过逐步推进，直到浏览器端真正弹窗。

2.2 PUT转换模块：先把路径变成能跑的程序

PUT转换里最关键的是处理undefined symbols。对于未定义变量，XSSky会沿 CPG 做自底向上的def-use回溯，把相关赋值语句并回原始路径；对于静态上无法补齐的变量，比如文件包含引入的外部变量或运行时动态赋值变量，系统则把它们替换成fuzzer可控的临时变量，并根据解释器报错去修正类型。

函数调用的处理也类似。系统会沿调用图提取被调函数实现，写入 function\_definition.php再包含回PUT；如果新引入的函数内部还调用别的函数，就继续递归定位。对于对象方法调用目标不明的情况，作者采用over-approximation：收集同名且参数个数匹配的候选函数，分别构造多个PUT，只要其中任何一个能触发漏洞，就认为原始路径存在风险。这一步的意义在于，XSSky并不是在完整应用上做fuzzing，而是在尽量保留语义依赖的前提下，把局部路径重建成一个能独立运行的测试对象。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIzzMiaj9b0nrXoSCPuKTGMiboKK72EKOmNBfuzmXGdB5YEl8engXj2Is1DTPJdnCC6VnMZWfVVuXVg11pJQ6ayTTZicHsqwH4Z6nk/640?wx_fmt=png)

图2 Dolibarr 真实运行案例

2.3 上下文感知的exploit grammar：先决定该试什么

在PUT可执行之后，XSSky会先做漏洞点上下文分析。系统把程序放进本地 Apache目录，用带唯一标记的请求访问它，再通过文档对象模型（DOM）解析去判断当前sink落在HTML上下文、URL上下文、HTML属性上下文还是JavaScript上下文中。作者还进一步考虑了参数是否参与字符串拼接，因为这会决定是否必须先用终止符逃出原语法结构。

基于这些上下文信息，论文设计了八种攻击语法，本质上是这些组件的组合。作者强调，语法之间不是平铺的，而是有兼容性和优先级关系。比如某些语法对当前上下文根本不成立，就没有必要浪费时间去测；而如果简单语法已经全部失败，它的超集语法往往也没有必要继续试。

这部分相当于在payload搜索空间上做了一次“语法层剪枝”。相比把各种跨站脚本攻击XSS载荷无差别地扔出去，XSSky先保证起点是对的，再决定该按什么顺序推进。

2.4 解释器反馈与定向变异：让fuzzing知道自己卡在哪

论文从公开CVE和已有绕过技巧里总结出8类evasion methods，并扩展成18种面向不同exploit组件的变异策略，包括大小写扰动、关键字拆分、不可见字符插入、特殊字符扰动、替代标签、Unicode编码和语义等价改写等。

真正让这套策略变得有效的，是反馈机制。XSSky会hook PHP解释器中的字符串比较函数和字符串修改函数，例如 preg\_replace()，记录调用行号、输入串、被命中的子串以及处理后的返回值。这样一来，系统就能知道当前payload到底是哪一段被sanitizer拦住了。

随后，fuzzer不再对整个输入盲目随机变异，而是围绕被命中的component做更有针对性的尝试。如果反馈表明当前策略又越过了一层过滤，系统就继续沿这条策略推进；如果没有进展，再切换到另一种mutation strategy。这也是XSSky在sanitizer绕过场景里明显强于普通动态测试器的核心原因。

表1 不同sink context的exploit grammar与优先级

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIxBaCk7BKv25TDwnj7Hpcicibria02DShRWuhE3e5jDjS1Z6HLusxeiaJeEpsR85u18fYQ8coZ2FLnzoDTgXfaXCWusBkn9un1xhwE/640?wx_fmt=png)

2.5 Bug Oracle：最后仍然要回到浏览器里确认

论文最后还是把判断标准落回浏览器端。XSSky使用Selenium驱动浏览器访问PUT，并监听JavaScript弹窗是否出现；对于需要点击或悬停才能触发的场景，系统还会模拟这些交互。这意味着它最终给出的不是“代码看起来像漏洞”，而是“浏览器里真的执行了payload”。它让整套系统没有停在静态推断，也没有停在解释器字符串层，而是回到了XSS最真实的验证条件：浏览器端脚本是否被执行。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwtRBV25AZbjcKDeuHqIF5YobzcCjst4Oay9rjReiaUFF23dDId0LuGDQL9HgXlm2FXSCuiazib7eyR9CuvOztQKAc3k4dX8XpFjk/640?wx_fmt=png&from=appmsg)

图3 preg\_replace()的 hook 反馈示例

## 三、实验方法与性能评估

3.1 数据集与实验设置

作者在20个流行PHP Web应用上评估XSSky，总代码量达到4,082,064行。数据集的选择方式也比较规整：先筛出GitHub上star超过100的PHP项目，再随机选出5个star超过10,000、10个超过1,000、5个超过100的应用。实验环境则是Ubuntu 20.04、64核 Xeon Gold 6242、512GB内存，PUT与fuzzing运行在Apache 2.4.41和PHP 7.4.0 上。

3.2 PUT 转换与漏洞检测结果

先看PUT转换。作者从7,005条source-sink路径出发，最终成功把6,997条转成局部可执行PUT，成功率达到99.89%。剩下8条失败路径的原因也比较集中：它们依赖第三方库函数，而这些函数定义不在目标应用源码里，导致系统无法完整拉回。

还有漏洞检测。XSSky一共报告了74个潜在漏洞，人工验证后确认其中60个是真实XSS，precision为81.08%。更关键的是，这60个漏洞里有31个都发生在“路径上已经存在sanitizer的情况下，其中24个属于sanitizer被误用，7个属于policy不充分。这说明论文真正打到的，是很多静态工具最不擅长的那一类场景。按sink context拆解，HTML context有28个漏洞，URL context5个，HTML attribute context19个，JavaScript context8个。其中最值得注意的是HTML attribute context：14/19的漏洞都与sanitizer绕过有关，比例最高。作者用这一结果说明，过滤器如果不结合sink context去部署，就很容易制造错误安全感。

表2 XSSky检测到的XSS漏洞的分类统计

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIwtNSU9e5IEqWrWC2iaChACPVd7kOuTr62MWyYpkkqTgA50uVoRPPbVjrjknLlf2Yz7MJxsF53ibkFgPzD3eSfibyEqHp76CBuUzc/640?wx_fmt=png)

3.3 与基线方法对比

论文把XSSky与TChecker以及四个动态测试器做了对比。结果非常直观：XSSky 达到60个TP、14个FP、0个FN，对应81.08% precision和100% recall；TChecker只有32个TP、261个FP、28个FN；四个动态测试器里表现最好的XSSky-Burp也只发现了29个漏洞，recall为48.33%。

作者进一步指出，XSSky相对各基线的precision提升范围为11.48%到642.49%，recall提升范围为87.51%到172.70%，并额外发现了18个所有基线都没抓到的独有漏洞。静态工具的问题，主要还是过度依赖sanitizer先验模型；动态工具的问题，则在于缺少sink context analysis和解释器反馈驱动的定向变异，因此在sanitizer绕过场景里明显不行。

3.4 效率与误差来源

效率方面，XSSky的端到端平均耗时为每个应用13,472.48秒，约3.74小时；中位数只有692.04秒，说明平均值被少数复杂应用明显拉高。分模块看，PUT转换最耗时，其次才是路径定位和fuzzing。误报方面，论文确认了14个false positives，主要来自上游静态工具给出的路径缺少控制流约束，或者路径位于dead code中。这也说明XSSky的上限，仍然会受到输入路径质量影响。

表3 与静态与动态基线的效果对比

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIw4ogNBYMQZeq05WsgAXJZ2ydw6YcKEZMJeb7CGgL4hM52ibiaAzicKQko1xISBsuZeXOnupow4GfUmDclmmHcxJWic5uEbp5rRkFU/640?wx_fmt=png)

## 四、论文的局限、未来展望

4.1 研究的不足与限制因素

XSSky的路线是完整的，但它的边界也很明确。首先，它依赖上游静态工具给出source-sink路径，因此只要静态工具在控制流约束、死代码识别、对象分派或第三方库调用上出现偏差，XSSky的后续阶段就只能在一个不完美输入上继续工作。

还有，PUT本地执行终究是对真实应用环境的一种重建，而不是完整复刻。论文在实验里没有观察到由此直接导致的误报，但从方法论上说，这仍是一种值得警惕的近似。再者，当前系统主要聚焦reflected server-side XSS，对stored XSS和client-side XSS不是直接覆盖。

4.2 未来研究方向与适用场景

论文自己给出的两个未来方向都很自然。第一个方向是继续扩充sanitizer绕过技巧库；第二个方向是把框架拓展到stored XSS，只是这需要重新界定数据回流路径中的 source。就方法本身而言，我认为它最适合有源码、规模较大、带有大量自定义过滤逻辑的PHP应用安全审计。

如果面对的是没有源码的纯黑盒目标、高度依赖前端JavaScript的SPA，或者大量依赖外部服务和复杂业务状态的系统，XSSky的优势会被削弱。因为它的方法前提就是先拿到source-sink path，再把路径局部重建出来。

这篇论文仍然给了一个很强的研究启发：很多程序安全问题并不一定非要在“完整系统”和“静态路径”之间二选一。像XSSky这样，先把候选路径压缩成局部可执行程序，再用上下文感知和反馈驱动的方式做漏洞确认，可能同样适用于其他需要“局部证据确认”的漏洞类型。

预览时标签不可点

修改于

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