---
title: 我们拆解了5621个先知研究文章，编写了一个研究员skill
url: https://mp.weixin.qq.com/s/30afNhFl6OJTz8db55f8rA
source: Doonsec's feed
date: 2026-01-29
fetch_date: 2026-01-30T04:01:31.269947
---

# 我们拆解了5621个先知研究文章，编写了一个研究员skill

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/VJgAEGkvf0pBSkic15NCNrTDnXAwmdCplqsjoibMqhadNgib0FMUKkicbKaxAia6t4ibwibPOBBbaPorpvgcv2Bhy4s4A/0?wx_fmt=jpeg)

# 我们拆解了5621个先知研究文章，编写了一个研究员skill

六边形攻防安全

![]()

在小说阅读器中沉浸阅读

编者荐语：

ai只会越来越强大，而我们能做的就是让ai为我所用

以下文章来源于探微杜渐人工智能
，作者tanweai

![](http://wx.qlogo.cn/mmhead/zZSYtpeVianQBg9JpTbvM3b79M7xR3OZdvATjmQczWb9slKO1ibAXwQl1A9c3ZVYmzDEWYDx7GErU/0)

**探微杜渐人工智能**
.

探索AI与安全前沿成为意图安全基础设施，让企业专注创新

# 写在前面

继上次我们分析了wooyun legency skill后，我们又做了一件事——把先知社区5621篇安全研究文章全部过了一遍。

不是为了学习具体的漏洞利用技巧（那些网上到处都是），而是想搞清楚一个问题：

> **顶尖安全研究员的思维方式到底有什么共性？**

答案比我们想象的要简单，也更有价值。

但更重要的是——我们不想让这些洞察只停留在一篇文章里。

我们把它做成了一个可复用的"Skill"，让AI能够像顶尖安全研究员一样思考。

# 00 为什么要做这件事？

之前的wooyun legency skill解决的是漏洞发现的corner cases的覆盖问题，也就是skill能抽取wooyun漏洞里足够细的一些犄角旮旯的检测手段以及参数，解决的是具体执行的corner cases问题；而这次先知研究员skill解决的是方法论corner cases的问题，就像一群研究员一起讨论帮你解决问题一样。

llm不能彻底帮你解决这些问题，因为llm无法覆盖具体的思维执行，比如就某个漏洞的研究方法，他的价值判断不如人类，而skill可以很好的把这些专家的价值判断落到硬盘里，你只需要加载对应的文件就行，但是他也有一个缺点，就是比较死，像是一个放大版的workflow，这点是需要读者注意的。

那先说说我们的初衷。

安全行业有个痛点：知识传承效率太低。

一个资深研究员花了十年积累的经验，很难高效地传授给新人。写文章？新人看完记不住。带徒弟？一个人带不了几个。

我们在想：有没有可能把"专家的思维方式"提取出来，变成一种可以被AI调用的能力？

这就是我们做这个Skill的初衷——不是让AI掌握更多漏洞知识，而是让AI学会像专家一样思考问题。

具体来说，我们希望实现：

新人加速

刚入行的研究员，可以借助AI获得专家级的思维引导

经验沉淀

把散落在各处的研究文章，提炼成结构化的方法论

效率提升

减少重复踩坑，把时间花在真正有价值的探索上

# 01 我们是怎么提取这个Skill的？

这里分享一下我们的方法论，也许对其他想做类似事情的团队有参考价值。

第一步：分类与聚类

5621篇文章，我们先做了一轮人工分类：

| 类别 | 数量 | 代表性主题 |
| --- | --- | --- |
| Web注入 | 348篇 | SQL注入、SSTI、命令注入 |
| 反序列化 | 268篇 | Java Gadget链、PHP反序列化 |
| 二进制安全 | 304篇 | ROP、堆利用、House of系列 |
| 域渗透 | 327篇 | Kerberos、委派攻击、横向移动 |
| 代码审计 | 402篇 | PHP/Java框架审计 |
| RCE/持久化 | 553篇 | 内存马、Rootkit、eBPF后门 |
| 其他 | 1419篇 | CTF、逆向、Fuzzing等 |

第二步：抽象思维模式

分类完成后，我们不是去总结"有哪些漏洞类型"，而是去分析：作者在发现和利用这个漏洞时，经历了怎样的思维过程？

我们发现，尽管漏洞类型千差万别，但底层的思维模式高度相似。

比如，无论是挖SQL注入还是挖反序列化，高手都会：

* 先识别输入入口（攻击面）
* 然后追踪数据流向（假设验证）
* 接着探索边界条件（边界探索）
* 最后反推防御逻辑（防御逆向）

这就是我们后面会讲的"四层思维模型"的由来。

第三步：结构化输出

最后，我们把提炼出的思维模式，封装成了Claude Code可以调用的Skill格式

这样做的好处是：当你用Claude Code做安全研究时，它不再是一个只会查资料的工具，而是一个具备专家思维方式的研究伙伴。

---

# 02 这个Skill怎么用？

说了这么多，具体怎么用呢？我们整理了六个典型场景。

场景一：漏洞挖掘思路卡住了

当你卡住的时候，可以让AI用这个Skill来引导你的思考。

![](https://mmecoa.qpic.cn/mmecoa_png/VJgAEGkvf0pBSkic15NCNrTDnXAwmdCplte0d97PY6icFhw6Ap2fDgibcNbAqDkoMbSTISdYsq4b8GS0SFHXiaxflA/640?wx_fmt=png&from=appmsg)

---

场景二：规划完整渗透路径

当你需要规划完整渗透路径时，可以让AI帮你串联各个模块。

![](https://mmecoa.qpic.cn/mmecoa_png/VJgAEGkvf0pBSkic15NCNrTDnXAwmdCplreokiaicsuR1CLamEke3X3ib4yZ1rnuHygficH8zicRmKGgnOkyWxvdppYw/640?wx_fmt=png&from=appmsg)

---

场景三：分析一个新CVE

当你需要快速理解一个新漏洞时。

![](https://mmecoa.qpic.cn/mmecoa_png/VJgAEGkvf0pBSkic15NCNrTDnXAwmdCplM00fkGbUfhUdsQTXFfqjjjRnCQjyr7UhbiaKrGepm1fNqP8OYz4udtw/640?wx_fmt=png&from=appmsg)

---

场景四：代码审计找漏洞

当你需要系统性地审计代码时。

![](https://mmecoa.qpic.cn/mmecoa_png/VJgAEGkvf0pBSkic15NCNrTDnXAwmdCplER9y3rqGVRWGOb8cgM92PnibGKmHDSkAGibaG6zibANw2Gj73B5vTe7VA/640?wx_fmt=png&from=appmsg)

![](https://mmecoa.qpic.cn/mmecoa_png/VJgAEGkvf0pBSkic15NCNrTDnXAwmdCpl2rdTrM6vq551I3ouUAiboQDt1PEKcc0ic7b8ofvsDaibNdakatacKqKqQ/640?wx_fmt=png&from=appmsg)

![](https://mmecoa.qpic.cn/mmecoa_png/VJgAEGkvf0pBSkic15NCNrTDnXAwmdCpleGaHjORC53F09ia4micVK6XNJ6agLwiacqobluCjvpCgUwibI7je59D2Rg/640?wx_fmt=png&from=appmsg)

---

场景五：CTF快速解题

当你需要快速找到利用思路时。

![](https://mmecoa.qpic.cn/mmecoa_png/VJgAEGkvf0pBSkic15NCNrTDnXAwmdCplWcibn738ZfdvPVAUuFe4EvLEag1TPbJA2BHViaiclxNUcD7vUial0YPdWA/640?wx_fmt=png&from=appmsg)

---

场景六：防御审计

反过来用，可以帮助防御方发现盲区。

你的输入：

> 帮我用攻击者视角审计一下我们的Java应用安全

AI调用Skill后的回复：

> 我会按攻击面逐一检查：
>
> **1. 反序列化风险**
>
> * 检查项：ObjectInputStream使用、Fastjson版本、XStream配置
>
> **2. 注入风险**
>
> * 检查项：SQL拼接、OGNL/SpEL表达式、模板引擎
>
> **3. 权限维持风险**
>
> * 检查项：是否有Agent加载入口、Filter动态注册能力
>
> **4. 供应链风险**
>
> * 检查项：依赖库版本、是否存在已知CVE
>
> 需要我详细展开哪个方向？

---

# 03 一个反直觉的发现

现在回到我们最初的问题：高手和新手的差距到底在哪？

我们原以为，差距在于知识量——高手懂得更多漏洞类型、掌握更多利用技巧。

但分析了几千篇文章后，我们发现：差距其实在于提问的方式。

举个例子。

面对同一个目标，新手的思维链条是这样的：

而高手的思维链条是这样的：

91011找到SQL注入点 → 被WAF拦截 → 停下来想：WAF的检测逻辑是什么？→ 它检测POSTbody，那Header呢？→X-Forwarded-For会写入日志表→ 日志写入用的是预编译吗？→ 不是，直接拼接

看出区别了吗？

新手在技术层面打转，高手在认知层面跃迁。

这个跃迁，我们把它抽象成了一个四层模型。

---

# 04 四层思维模型

我们把安全研究中的思维活动，分成了四个层次：

| 层级 | 核心问题 | 思维特征 |
| --- | --- | --- |
| **L1 攻击面识别** | 输入在哪里？信任边界在哪里？ | 枚举、收集 |
| **L2 假设验证** | 我的猜测对不对？如何证伪？ | 实验、验证 |
| **L3 边界探索** | 规范的灰色地带在哪里？ | 突破、创新 |
| **L4 防御逆向** | 如果我是防御者，会怎么做？ | 换位、博弈 |

大多数人卡在L1和L2之间来回打转。

高手的秘密是：当L1-L2走不通时，会主动跳到L4。

这就是上面那个例子中发生的事情——被WAF拦截后，高手没有继续在payload层面较劲，而是切换到防御者视角，去思考"WAF是怎么工作的"。

一旦理解了防御逻辑，绕过就变成了找盲区的游戏。

> **这就是我们说的"元认知"——不是思考问题本身，而是思考"我应该怎么思考这个问题"。**

---

# 05 跨域攻击链：高手的组合拳

分析完单点突破的思维模式后，我们又发现了另一个规律：高手很少只用一种技术。

他们擅长把不同领域的技术串联起来，形成完整的攻击链。

| 起点 | 终点 | 桥接技术 | 真实案例 |
| --- | --- | --- | --- |
| Web注入 | 反序列化 | JNDI注入 | Log4j打Fastjson |
| 反序列化 | RCE | Gadget链 | CC链执行命令 |
| RCE | 持久化 | 内存马 | Filter型内存马 |
| Web漏洞 | 域渗透 | 凭据窃取 | SQL注入拿Hash |

这个表格的价值在于：当你在某个领域卡住时，可以考虑换一个领域突破。

我们内部把这个叫做"攻击链思维"：不要只想着单点突破，要想着如何把多个小漏洞串成一个大漏洞。

---

# 06 几条"元规律"

最后，分享几条我们从5621篇文章中提炼出的跨领域规律。

规律一：复杂度即机会

功能越多，攻击面越大。解析器、引擎、协议处理器是漏洞高发区。

规律二：时序决定可见性

先加载的检测后加载的。内存马检测的本质是时序竞争。

规律三：抽象层越高，防御越难

内核态对用户态天然不可见。eBPF/Rootkit很难用常规手段检测。

规律四：特征可变，行为不变

静态特征可以无限变形，但恶意行为的本质不会变。

规律五：历史会重演

同类问题往往重复出现。Log4j之后，其他日志库大概率也有类似问题。

---

# 07 结构和能力边界

![](https://mmecoa.qpic.cn/mmecoa_png/VJgAEGkvf0pBSkic15NCNrTDnXAwmdCpllNA0Yn6u4O4AN7AqjHVl90XK3qgb7qicoCAyODTSyFuSxqYmAU9pDIg/640?wx_fmt=png&from=appmsg)

![](https://mmecoa.qpic.cn/mmecoa_png/VJgAEGkvf0pBSkic15NCNrTDnXAwmdCplgDadMTxLd1YfdPgJNQSbeKGUkmdyNKrDWKnrWDlySQ9XUZ311yoYKg/640?wx_fmt=png&from=appmsg)

#

---

# 08 写在最后

回到开头那个问题：
> **顶尖安全研究员的思维方式到底有什么共性？**

我们的答案是：

> **他们不是知道更多的漏洞，而是掌握了一套在未知领域快速建立认知框架的能力。**

这也是我们做这个Skill的意义——把这种能力提取出来，让更多人能够借助AI获得专家级的思维引导。

我们相信，未来的安全研究，不再是人与工具的关系，而是人与AI协作的关系。

AI不是来替代研究员的，而是来放大研究员能力的。

而这个Skill，就是我们在这个方向上的一次尝试。

---

如何获取这个Skill？

后台回复“先知”

---

关于我们

探微杜渐安全研究团队，专注于AI+安全的交叉领域研究。

我们相信：让AI学会像专家一样思考，是提升整个行业效率的关键。

如果你也在做类似的事情，欢迎交流。

---

原创内容，转载请注明出处

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9qM7NQ3lGkBM9HNjOYhrvc9CNKbbd8pAl3cpffjDBworJnpCOkbD3Flx1XxRPlQbBAicglpPl0ZEGWVzdtCHsdA/0?wx_fmt=png)

六边形攻防安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9qM7NQ3lGkBM9HNjOYhrvc9CNKbbd8pAl3cpffjDBworJnpCOkbD3Flx1XxRPlQbBAicglpPl0ZEGWVzdtCHsdA/0?wx_fmt=png)

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