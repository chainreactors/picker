---
title: 当安全研究进入 AI 时代
url: https://blog.cnpanda.net/life/1324.html
source: Panda | 热爱安全的理想少年
date: 2026-08-04
fetch_date: 2026-08-05T04:58:38.804413
---

# 当安全研究进入 AI 时代

[![Panda | 热爱安全的理想少年](https://www.cnpanda.net/logo.png)](https://www.cnpanda.net/)

搜一搜

# 当安全研究进入 AI 时代

本文最后更新于 2026.08.04，总计 2879 字，阅读本文大概需要3 ~ 5 分钟。

本文已超过 1天没有更新。如果文章内容或图片资源失效，请留言反馈，我会及时处理，谢谢！

![640.png](https://www.cnpanda.net/usr/uploads/2026/08/3215898325.png "640.png")

最近有几件事让我深刻意识到了，在安全这个领域上，真正的迎来了 AI 时代。因而有了这篇随笔，让自己思考未来。

第一件事是 PSRC 平台关闭。

> 7 月 23 日，PSRC 发布公告，称由于业务调整，平台将在 7 月 30 日停止运营并关闭。

看到这条消息的时候，不禁有点感慨，在最近一年里，漏洞发现的速度变得太快了。

以前一个人挖掘一个漏洞、审计一个大型项目，可能需要几周，甚至几个月。但是现在，只需要把代码或者目标交给 AI，很多工作几天就能做完，有些边界比较清楚的问题，几个小时就能看到结果。安全人员寻找漏洞的效率被 AI 无限放大了。

第二件事是 fastjson 被爆 RCE。

> 7 月 19 日，Kirill Firsov 在 X 上公开表示，Fastjson 1.2.83 存在一个不依赖 classpath gadget 的远程代码执行漏洞。

简单来说，就是不需要目标环境里提前存在某个传统意义上的可利用类，也能把利用链跑起来。

最开始公开的信息其实很少，主要是漏洞结论、一段演示视频，以及“不依赖 classpath gadget”这个关键提示。完整的请求、触发条件、调用过程和利用代码，当时并没有直接给出来。

但几个小时之后，漏洞的 exp 就已经出来。十几个小时后，就已经有人在github上提交了可以复现的 PoC 和测试环境。这放到以前，这类问题即使给一个对 Java、Fastjson 和历史反序列化漏洞都比较熟悉的人来做，没几天的时间也是不可能的事情。

因为同样的 case ，我经历过了两次。第一次是 CobaltStrike RCE，当时 Beichen 师傅挖掘出后，群里的师傅们讨论了一夜，当初我也算是第一批复现出这个漏洞的人，但也是耗费了一夜时间。另一件就是 Spring4Shell，也是在很少的信息前提下，花了几个小时才复现出来。

现在是完全不一样了。这两个case，目前来看，交给 AI 几个小时内就可以解决。

这件事真正让我有感触的，不是 Fastjson 又出了一个 RCE，也不是这个漏洞的利用方式有多特别。而是从一个很有限的提示，到顺着源码找到关键路径，再到补全触发条件、搭建环境、写出 PoC，整个过程已经被压缩到了按小时计算。

只需要有人先给出一个比较准确的方向，AI 就完全可以尝试自动化的搭建环境，分析代码，追踪具体函数调用关系和数据流。

AI 与人最大的不同是，它可以不知疲倦地尝试不同的思路，并且每一种思路是根据当前分析的代码来进行的，其底层知识储备的完整性，就注定了其只要发现核心问题点，就可以构建出核心链路。

更重要的是，这些思路的相关研究工作可以同时进行。但对于人类来说，一次通常只能跟一两条路径，AI 却可以把十几条可能性同时展开，再把结果整理出来交给人判断。

所以传统意义上的代码审计，已经”死“了。

过去我们经常说，一个好的代码审计人员要有经验，看到某个函数，马上想到历史上出过什么问题，看到一个参数，知道它可能从哪里被控制，看到一段奇怪的兼容代码，愿意继续往下追。还需要有足够的细心，不能漏掉某个分支，不能忽略某次类型转换，不能因为函数名字看起来普通就直接跳过去。

这些能力在以前确实很重要，因为人脑能处理的信息有限。经验越丰富，筛选代码的速度越快，越有耐心，越可能在别人放弃之后继续找到问题。

但现在，经验和细心正在变成 AI 最擅长的部分。

常见漏洞模式，AI 懂得比大多数安全人员都多。重复跟踪几十层调用关系，丝毫不在话下。一个项目检查完之后，同样的方法还能立刻复制到几十个相似项目里。

如果一个安全人员的主要优势，是知道哪些函数危险，或者愿意连续几天追踪变量，那么这种优势已经近乎全无。

至少在“已经拿到代码，并且大概知道要找什么”的情况下，AI 已经可以超过绝大多数人。乃至于你只要和 AI 说，这个项目存在 RCE 漏洞，它就可能给你挖掘一个 RCE 漏洞。

以前我们花大量时间读代码，最后才从代码里想出一个方向，以后更可能是先有一个方向，再让 AI 把相关代码全部翻出来去研究。

真正能拉开差距的，首先是攻击面的选择。

比如 Fastjson 这次的问题，AI 可以做到很快帮忙对比版本、追踪反序列化流程，分析哪些检查被绕过，再根据报错不断调整测试代码，最后把 PoC 跑出来。

但真正值得研究的，不是“还能不能找到一条新的 gadget 利用方式”，而是有没有新的 RCE 方式。

过去大家对 Fastjson 风险的判断，很多时候建立在目标环境里是否存在可利用类这个前提上。如果这个前提不再成立，那么原来对利用条件、影响范围和防护方式的判断，是否都是从零开始了？

从零开始，就意味着无限的可能。告诉 AI 后，AI 就会思考哪些路径可以在不依赖传统 classpath gadget 的情况下，仍然能够走到代码执行，就会像安全人员一样，分析源码、搭环境，测 PoC。

但这一句“不依赖 classpath gadget”，才是最核心的点，也是安全人员最有价值的输入。

AI 可以很快把一条路走通，但该走哪条路，是不同安全人员区分度的体现，安全人员输入的价值越高，AI 产出的质量也就可能越高。

另一个区分度，是安全人员怎么使用 AI 产出的信息。

在日常的工作里，有很多信息单独看都很普通，比如网页的错误相应、某些配置项的开关或者是一些功能的feature，AI 都可以帮助分析或关联。但这些信息最终能形成多大的价值，仍然取决于个人怎么去利用，以及愿意把结论推到哪一步。

人类之所以是智人，是因为会使用工具。AI 就是新时代的工具。因此，未来安全人员并不是用来和 AI 比谁更牛逼，而是安全人员可以利用 AI 做到哪一步。

AI 能产出的信息会越来越多，能独立完成的工作也会越来越复杂。我们也不必为此感到焦虑，顺应时代的发展要比焦虑更实在。

从我的角度来看，对于安全人员来说，真正稀缺的不是通过 AI 发现了什么漏洞或者获取到了什么信息，而是我们能够知道在哪里可能会出现漏洞以及能够利用获取到的信息来做什么。

安全人员发现漏洞的能力已经在 AI 时代被逐渐拉平了，差距可能也就是 AI 深度思考的那几个小时，以后真正的差距就是你让 AI 去做什么，以及你为什么会想到做这件事。

最后一句话总结：

**工程上的差距将不再是差距，真正拉开人与人之间距离的，是对问题的理解、对方向的判断，以及对 AI 产出信息的利用程度。**

#####

「感谢老板送来的软糖/蛋糕/布丁/牛奶/冰阔乐！」

赞赏

×

![](https://www.cnpanda.net/tx.png)panda

(๑＞ڡ＜)☆谢谢老板~

2元
5元
10元
50元
100元
任意金额

2元

使用微信扫描二维码打赏

![](https://www.cnpanda.net/usr/themes/7TEC/img/alipay-2.jpg)

![](https://www.cnpanda.net/usr/themes/7TEC/img/alipay-btn.png)

![](https://www.cnpanda.net/usr/themes/7TEC/img/wechat-btn.png)

版权属于：

Panda | 热爱安全的理想少年

本文链接：

https://blog.cnpanda.net/life/1324.html（转载时请注明本文出处及文章链接）

作品采用：

《[署名-非商业性使用-相同方式共享 4.0 国际 (CC BY-NC-SA 4.0)](//creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)》许可协议授权

* [生活](https://blog.cnpanda.net/category/life/)
* 2026-08-04
* [评论](https://blog.cnpanda.net/life/1324.html#comments)
* 2879 字
* 46 次浏览

[ByteCTF Guess Cookie 出题思路详解](https://blog.cnpanda.net/ctf/1301.html "ByteCTF Guess Cookie 出题思路详解")
1/1
没有了

#### 添加新评论

提交

暂无评论

![](/tx.png)

**panda**

---

喜爱程序分析以及研究一些有趣的 Web 安全问题

#####

##### 文章分类[共 77 篇] [[归档](https://www.cnpanda.net/archives.html)]

* [安全研究 (24)](https://blog.cnpanda.net/category/sec/)
* [代码审计 (17)](https://blog.cnpanda.net/category/codeaudit/)
* [技术杂谈 (12)](https://blog.cnpanda.net/category/talksafe/)
* [CTF (10)](https://blog.cnpanda.net/category/ctf/)
* [编程算法 (1)](https://blog.cnpanda.net/category/program/)
* [理论研究 (3)](https://blog.cnpanda.net/category/sci/)
* [生活 (9)](https://blog.cnpanda.net/category/life/)

##### 热门文章

* [个人经验泛谈之工控安全入门](https://blog.cnpanda.net/sec/592.html "个人经验泛谈之工控安全入门") 116,327 人看过
* [第十届信息安全国赛 Web WriteUp（部分）](https://blog.cnpanda.net/ctf/81.html "第十届信息安全国赛 Web WriteUp（部分）") 49,846 人看过
* [fastadmin最新版前台getshell漏洞分析](https://blog.cnpanda.net/codeaudit/777.html "fastadmin最新版前台getshell漏洞分析") 38,675 人看过
* [【Java 代码审计入门-01】审计前的准备](https://blog.cnpanda.net/codeaudit/588.html "【Java 代码审计入门-01】审计前的准备") 27,984 人看过
* [maccms v8 80w 字符的 RCE 分析](https://blog.cnpanda.net/codeaudit/660.html " maccms v8 80w 字符的 RCE 分析") 25,928 人看过
* [带你走进 S7COMM 与 MODBUS 工控协议](https://blog.cnpanda.net/sec/578.html "带你走进 S7COMM 与 MODBUS 工控协议") 25,446 人看过
* [【Java 代码审计入门-04】SSRF 漏洞原理与实际案例介绍](https://blog.cnpanda.net/codeaudit/678.html "【Java 代码审计入门-04】SSRF 漏洞原理与实际案例介绍") 24,449 人看过
* [T-Star高校挑战赛WP](https://blog.cnpanda.net/ctf/731.html "T-Star高校挑战赛WP") 23,367 人看过
* [挖洞神器之XRAY使用初体验](https://blog.cnpanda.net/talksafe/657.html "挖洞神器之XRAY使用初体验 ")  22,468 人看过
* [【Java 代码审计入门-05】RCE 漏洞原理与实际案例介绍](https://blog.cnpanda.net/codeaudit/759.html "【Java 代码审计入门-05】RCE 漏洞原理与实际案例介绍") 22,124 人看过

##### 标签

[ByteCTF](https://blog.cnpanda.net/tag/ByteCTF/ "1 个话题")
[年度总结](https://blog.cnpanda.net/tag/%E5%B9%B4%E5%BA%A6%E6%80%BB%E7%BB%93/ "2 个话题")
[logback](https://blog.cnpanda.net/tag/logback/ "2 个话题")
[log4j](https://blog.cnpanda.net/tag/log4j/ "2 个话题")
[log4j2](https://blog.cnpanda.net/tag/log4j2/ "3 个话题")
[jn'di](https://blog.cnpanda.net/tag/jn-di/ "1 个话题")
[Thymeleaf Bypass](https://blog.cnpanda.net/tag/Thymeleaf-Bypass/ "1 个话题")
[Thymeleaf](https://blog.cnpanda.net/tag/Thymeleaf/ "1 个话题")
[SSTI](https://blog.cnpanda.net/tag/SSTI/ "1 个话题")
[java 代码审计入门](https://blog.cnpanda.net/tag/java-%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1%E5%85%A5%E9%97%A8/ "1 个话题")
[JDK8u20](https://blog.cnpanda.net/tag/JDK8u20/ "1 个话题")
[JEP290](https://blog.cnpanda.net/tag/JEP290/ "1 个话题")
[Java序列化](https://blog.cnpanda.net/tag/Java%E5%BA%8F%E5%88%97%E5%8C%96/ "1 个话题")
[java 序列化](https://blog.cnpanda.net/tag/java-%E5%BA%8F%E5%88%97%E5%8C%96/ "2 个话题")
[序列化](https://blog.cnpanda.net/tag/%E5%BA%8F%E5%88%97%E5%8C%96/ "3 个话题")
[gadget](https://blog.cnpanda.net/tag/gadget/ "1 个话题")
[JDK7U21](https://blog.cnpanda.net/tag/JDK7U21/ "1 个话题")
[JDK](https://blog.cnpanda.net/tag/JDK/ "2 个话题")
[反序列化](https://blog.cnpanda.net/tag/%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/ "2 个话题")
[java 反序列化](https://blog.cnpanda.net/tag/java-%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/ "4 个话题")
[微擎](https://blog.cnpanda.net/tag/%E5%BE%AE%E6%93%8E/ "1 个话题")
[内卷](https://blog.cnpanda.net/tag/%E5%86%85%E5%8D%B7/ "1 个话题")
[面试](https://blog.cnpanda.net/tag/%E9%9D%A2%E8%AF%95/ "1 个话题")
[生活](https://blog.cnpanda.net/tag/%E7%94%9F%E6%B4%BB/ "1 个话题")
[读研](https://blog.cnpanda.net/tag/%E8%AF%BB%E7%A0%94/ "1 个话题")
[蚂蚁金服](https://blog.cnpanda.net/tag/%E8%9A%82%E8%9A%81%E9%87%91%E6%9C%8D/ "1 个话题")
[非攻实验室](https://blog.cnpanda.net/tag/%E9%9D%9E%E6%94%BB%E5%AE%9E%E9%AA%8C%E5%AE%A4/ "1 个话题")
[远程代码执行](https://blog.cnpanda.net/tag/%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C/ "1 个话题")
[骑士 CMS](https://blog.cnpanda.net/tag/%E9%AA%91%E5%A3%AB-CMS/ "1 个话题")
[74cms](https://blog.cnpanda.net/tag/74cms/ "1 个话题")

##### 订阅

* [RSS](https://blog.cnpanda.net/feed/)

*[皖ICP备16023761号-1](https://beian.miit.gov.cn/)
© 2026 [Panda | 热爱安全的理想少年](https://www.cnpanda.net/).

站点已稳定运行：*