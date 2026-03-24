---
title: book driven development
url: http://xargin.com/book-driven-development/
source: No Headback
date: 2026-03-23
fetch_date: 2026-03-24T04:16:09.378254
---

# book driven development

[No Headback](http://xargin.com)

* [Home](http://xargin.com/)
* [Readings](http://xargin.com/readings/)
* [WeChat](http://xargin.com/wechat/)
* [Github](http://github.com/cch123)
* [Friends](http://xargin.com/friends/)

# book driven development

Mar 23, 2026

5 min read

嗯，最近一直在测试 opus 和 gpt5.4 的能力差别，目前结论是各有千秋。

今天我们从 opus 的一个最大优势讲起。先来看两张图。

第一张是用 kafka definitive guide 第二版去问 opus：

![](http://xargin.com/content/images/2026/03/bdd_1.jpg)

注意看 opus 的思考过程

第二张是用同样的问题去问 chatgpt：

![](http://xargin.com/content/images/2026/03/bdd_2.jpg)

同样注意看 gpt 的思考过程

可能有些读者还一头雾水，这能说明啥？嗯，先卖个关子，我们来看看之前关于 anthropic 的一篇报道：

> 当地时间9月5日，人工智能初创公司Anthropic提交的法庭文件显示，该公司将支付至少15亿美元来解决一起在美国的集体诉讼，该诉讼指控Anthropic涉嫌使用盗版书籍来训练聊天机器人Claude。

> 这一和解若获得法官批准，将成为AI公司与创作者之间版权争议的里程碑，也可能对整个出版业、创作者群体及AI行业的商业策略产生深远影响。**根据和解协议，Anthropic将向约50万部纳入和解范围的书籍的作者或出版商支付每部约3000美元的赔偿**。原告方律师贾斯汀·尼尔森（Justin Nelson）表示：“据我们所知，这是有史以来金额最高的版权赔偿，也是人工智能时代的首例此类案例。”

说结论，anthropic 用大量的书籍去训练了自己的模型，并且在模型的思考过程中大方地告诉你了，这本书我知道，它就在我的训练数据里。

个人认为，这些书的内容，目前是 opus 相比 gpt5.4 的最大的优势之一，这意味着什么呢？

最简单的，通过与 opus 互动，了解书的主要内容，加速书籍内容的理解和消化：

![](http://xargin.com/content/images/2026/03/image.png)

比如我可以通过互动了解到 TLPI 这本经典大部头里的内容

在 AI 时代，只是让 AI 做学习助手就有点 low 了。我们可以合理利用对我们自己脑中书籍的了解，让 AI 借助某本书的方法论来辅助我们进行开发。

比如我之前读过 righting software，觉得这本书里有个观点有点意思，按照代码的易变性来对代码进行分层：

![](http://xargin.com/content/images/2026/03/image-1.png)

让 AI 快速帮我出了一个版本，并且说明分层原因之后，对当年这本书的观点又加深了一层。这本书我当时读完只对 workflow 和 rule 的组合印象深刻，对易变性的理解其实没那么深。基于易变性来分层，当时更是没怎么多想，有了 AI 去做实验就方便多了，极大缩短了方法论的落地路径。

上面都是前互联网时代的东西，有没有更 AI native 一点的东西呢？有的，兄弟，有的。

我们可以直接让 AI 把我们认为不错的书转成 skill：

![](http://xargin.com/content/images/2026/03/image-2.png)

要求 opus 把 ddia 转成一个 senior archiect 视角的 review skill

当然，这只是 review，整个软件开发生命周期的每一个环节都有优秀的书籍介绍，所以如果你喜欢哪本著作，并且高度认同书中的观点，你就可以把这本书转成软件生产某个环境的 skill。

转换完之后，还需要再 review 一遍，因为方法论都是有时效性的，读书的时候要有批判性地读，自动转换出来的结果自然也不应该全盘接受。

我在某个群里和朋友分享观点之后，另外一个朋友也提出了同样的看法，并且给了我一个清单，是他的偏好（注意，不是我的）：

```
我在用这个： 需求分析：
- Are Your Lights On? — Gerald Weinberg
Specification by Example Gojko Adzic
- Exploring Requirements — Gerald Weinberg & Donald Gause

User Stories Applied Mike Cohn
User Story Mapping Jeff Patton

OO 建模：
Object Design: Roles, Responsibilities, and Collaborations
Object-Oriented Methods: A Foundation, UML Edition James Martin

设计：
《Software Architecture in Practice》 — Bass, Clements, Kazman
Patterns of Enterprise Application Architecture  - Fowler
《Domain-Driven Design》 — Eric Evans
《Designing Data-Intensive Applications》 — Martin Kleppmann
Fundamentals of Software Architecture: An Engineering Approach

编码：
《Refactoring》— Martin Fowler（1999，第二版2018）
《Test Driven Development: By Example》— Kent Beck（2003）
《Working Effectively with Legacy Code》— Michael Feathers（2004）

测试：
Agile Testing: A Practical Guide for Testers and Agile Teams Lisa Crispin
More Agile Testing: Learning Journeys for the Whole Team Lisa Crispin
XUnit Test Patterns: Refactoring Test Code
Lessons Learned in Software Testing: Kaner/Bach/Pettichord
```

读者应该要有自己的想法。

![Xargin]()

#### Xargin

[More posts](/author/xargin/)

If you don't keep moving, you'll quickly fall behind

Beijing

[Previous Post](/ai-panic/)

Powered by [Ghost](https://ghost.org/)

[No Headback](http://xargin.com)

![](/content/images/2021/05/wechat.png)