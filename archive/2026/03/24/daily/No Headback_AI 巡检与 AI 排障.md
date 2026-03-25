---
title: AI 巡检与 AI 排障
url: http://xargin.com/ai-debugging/
source: No Headback
date: 2026-03-24
fetch_date: 2026-03-25T04:16:04.054863
---

# AI 巡检与 AI 排障

[No Headback](http://xargin.com)

* [Home](http://xargin.com/)
* [Readings](http://xargin.com/readings/)
* [WeChat](http://xargin.com/wechat/)
* [Github](http://github.com/cch123)
* [Friends](http://xargin.com/friends/)

# AI 巡检与 AI 排障

Mar 24, 2026

4 min read

# AI 巡检与 AI 排障

> Mar 24, 2026 · 4 min read

前 AI 时代，巡检和排障都是又辛苦又烦人的体力活。

巡检需要你盯着告警和大量的监控面板，时刻思考系统是不是出什么问题了，有问题还得及时介入。之前和朋友聊天，听说国内某头部量化公司，最近一两年居然还要求 SRE 在开盘时间全程盯着监控面板，也是非常神奇。

排障则需要你对自己干活的语言做到基本精通，比如几年前在给人做培训的时候，单是性能优化这一节就做了大概 120 页 PPT，也只是简单介绍了程序员日常排查问题和做性能优化要了解的知识和工具。Systems Performance 的大部头更是让人又爱又恨，读到力竭才勉强消化。

从去年底开始，模型能力的大进化让这两件事变得不太需要人去做了。

## AI 巡检

如果公司内的基建比较完善，做到了 AI native 的全面 MCP/Skill 化，那巡检就是一两句话的事，直接指挥 AI 去关注 OTel 的三大类数据就行。

AI 可以很好地给出一份同事看了都满意的报告。示例：

![巡检报告示例](http://xargin.com/content/images/2026/03/image-3.png)

如果公司的基建比较差，那又得靠 agent browser 了。和之前写的让 AI 去生成 E2E 测试流程一样，只要告诉 AI 监控面板在什么位置，巡检主要关注哪些面板，哪些时间维度，哪些服务，剩下的让 AI 自己探索，直到出现 AI 解决不了的问题，再人工介入。

agent browser 探索你的监控/trace 页也差不多，它出问题了，你帮它修就好：

![agent browser 探索监控页面](http://xargin.com/content/images/2026/03/image-4.png)

多执行几次没有问题之后，再让 AI 总结成 skill，下次就是一句话的事：

![AI 总结成 skill](http://xargin.com/content/images/2026/03/image-5.png)

一句话，帮爷干活吧 AI：

![一句话巡检](http://xargin.com/content/images/2026/03/image-6.png)

## AI 排障

在公司里有时候不得不维护一些让人无语的代码，比如没太多并发开发经验的老同事写的并发+回调来回嵌套的天坑代码，规模一上去，正常人根本理解不了。有了 AI 以后，这种代码可太好对付了。

我们已经拿 AI 定位了不少并发 bug，因为代码难读，人去分析会被恶心很久，AI 则很快：

![AI 定位并发 bug](http://xargin.com/content/images/2026/03/image-7.png)

当然，快是有前提的。除了上面说的 OTel 三件套，你还需要把程序的 stack 也给它，如果是性能衰退，那公司里还需要有一个 continuous profiling 系统，比如已经被 Grafana 收购的 Pyroscope：

![Continuous Profiling](http://xargin.com/content/images/2026/03/image-8.png)

如果现场不全，比如你只有日志和监控，没有 stack，那 AI 给出的结论就不一定靠谱了。

## 总结

相信读者也看出来了，本文中的两种场景目前还都是人在本机完成的，即使在没有 AI 的时代，如果一家公司愿意在 infra 投入，做出自动巡检和自动排障的机器人，其实也并没有那么困难。

而到了 AI 时代，由大模型填平了中型公司和大公司的基建差距，正是所谓的基建不够，智能来凑。

只要技术人员的想象力足够天马行空，几乎没有太多克服不了的工程困难了。

![Xargin]()

#### Xargin

[More posts](/author/xargin/)

If you don't keep moving, you'll quickly fall behind

Beijing

[Previous Post](/book-driven-development/)

Powered by [Ghost](https://ghost.org/)

[No Headback](http://xargin.com)

![](/content/images/2021/05/wechat.png)