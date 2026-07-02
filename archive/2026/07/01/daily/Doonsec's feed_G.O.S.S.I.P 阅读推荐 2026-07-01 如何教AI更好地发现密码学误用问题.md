---
title: G.O.S.S.I.P 阅读推荐 2026-07-01 如何教AI更好地发现密码学误用问题
url: https://mp.weixin.qq.com/s/pZrMOfcucWsp7NVRMS6oUw
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:51:55.222936
---

# G.O.S.S.I.P 阅读推荐 2026-07-01 如何教AI更好地发现密码学误用问题

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eQ0Wf6rqolWIORcIFWf4gP1bWwpspz5hCWl3kkyb8fk5GdlT4BGj3XUiasXhQ4Nb3GaRpUhsxtYz5RRN6wgyfMmXDDyC3GF7ftKbG1mCoiaf0/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-07-01 如何教AI更好地发现密码学误用问题

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

虽然2026年只过去了一半，对于大部分网络安全从业人员来说，上半年可以说是行业翻天覆地的6个月：A社忙着不停地 ~~炒作~~ 宣传自家的 Mythos 和 Project Glasswing ~~斩杀了多少网络安全公司~~ 帮助多少企业发现了新漏洞，而很多CTF选手被Agent打得灰头土脸决定退隐江湖（此事在1935年老舍先生的小说《断魂枪》中亦有记载）。因此，在2026年下半年的第一天，我们要介绍一篇来自UC Berkeley的研究论文 *Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities*，原因很简单，论文里面有一个结论大家都喜欢看：“Mythos扫描了WolfSSL没发现问题，而我们的系统发现了两个高危漏洞”。所以到底是怎么回事，请关注今天的阅读推荐：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolXRywWeNFkeOR8gUm41BfiaJXibEWOPU2D7x5U8eDm6ZwibHDia0BRUvBiapFZm7rLldaMOibhqvtMlbQZyOzlFEBjxZuf0RTnPCWSMI/640?wx_fmt=png&from=appmsg)

本文的新知识（对于老同志来说）更多的是关于AI而不是密码学误用（crypto misuse）检测：作者上来讨论的并不是什么密码学误用的新技术，他们注意到现在大部分所谓的AI驱动的代码安全扫描都是如下图这样的范式，也就是把项目代码（当成文本）丢给AI，让AI（不同的agent）去找各种各样的问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolX6cg3qgtDyaE0kv3vwgk6k6KuKBV2a7mFRn2UPXxx4rubDkt1wcVIDuF6diaAQibmTWPTZYfsgicHuYNxR9lOriazeDp77oAZv1ics/640?wx_fmt=png&from=appmsg)

这种思路现在估计在安全社区里面有一万个人都在做，虽然技术细节上各有不同，但本质上也就那样。因为大部分人在找漏洞这件事情其实并不太创造新的知识边界，不管做法怎么变化最终都只能导向差不多的结果。本文的作者表示，既然都这样，大家能不能稍微尊重一点我们安全社区在过去几十年的积累，至少把一些关键技术用起来，而论文的核心思路就是把密码学和软件安全领域最重要的测试技术之一的差分测试（differential testing）给拿过来让AI去“照葫芦画瓢”。

稍微老资格一点的安全社区成员肯定对IEEE S&P 2014年的最佳实践论文 *Using Frankencerts for Automated Adversarial Testing of Certificate Validation in SSL/TLS Implementations* 不陌生，这篇论文早在12年前就把今天我们这篇论文的核心技术路线都设计好了，而本文的核心技术中的第一步——Amplified testing（下图所示）就完完全全是此前的Frankencerts的技术方案：用相同的输入去测试一组（密码学算法库）对象，然后观察这一组对象中谁是“少数派”——对相同输入的处理和其他对象都不一样，产生这种分歧（ambiguity）就暗示着漏洞的存在。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolVaOsWIIBNvljV8ZpicSuicbiaNoIsuhJumPQuJEjAyVKAAcZERQQp9wVwIEZpBbI6ZkaSQUlic6PkiccnwcDH88sOGJDmzwApbVXk4/640?wx_fmt=png&from=appmsg)

和12年前相比，作者现在的“军火库”里面存满了智能化：12年前不管是生成各种变异的输入还是进行测试都要依赖古法开发的代码，而新时代下本文作者开发的Chai分析系统上来甚至首先是让AI来阅读资料、分解任务，然后才开始接下来的测试和分析工作，不得不说时代变了……

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolV4iaaDF2qfQGeoIWF0QQxGXqhSw4t5PFXsQ6wTVOnDj5MibyFYiaSgNZd8FQiaI9pzBonP9wu8hfwEVibe02Y9fU3NWf9roYh1qnsg/640?wx_fmt=png&from=appmsg)

虽然智能化程度大大增加，但是本文的研究思路似乎没有什么新的突破：在做完了差分测试（并找到了ambiguity）之后，接下来要做的事情非常的简单，就是去分析哪些密码学算法库是“少数派”，至于为什么这些算法库会存在和别的大多数算法库不一样的行为，Chai根本不管，它直接就跳到下一阶段去分析哪些软件会依赖这个“有问题的”算法库。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolUuTDhwLXgTOKs5nsJJrw6b8A6aByibYQK20zwwh7ib1vfkzZEfJTRluNdOh77icQDFUzmkFVJTOTC8sHO0pBOECzo53VZIialeMxE/640?wx_fmt=png&from=appmsg)

在确定了哪些软件依赖特定的“有问题的”算法库之后，Chai的最后一步分析工作实在是有点过于straightforward了，它就直接引入了一个叫做targeted audit的概念（如下图所示），可一般来说论文里面出现新概念（不是《新概念英语》）不是什么好事，说明作者想要欲盖弥彰？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolU5Yu44LPSmLOC2nibhzr3X6oSNdiafVN50X0XibFwdice6oQCTqwenhBcOdeFjCe2ibyiakQnyZu5yU16lGtAjyZiayanfO4w18ZKU8c/640?wx_fmt=png&from=appmsg)

呃，看下面这个对比你就懂了，所谓的targeted audit就是通过前面几步的测试分析，缩小了问题的范围，然后写出一个更加精确的prompt，让AI来分析（当然在找到问题后也会依赖一些coding agent来帮忙写PoC exploit）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolVTHxISKUcBJEOXNt61iatVyYaXV8FInRYLttW8DMxFFAZsLzhyvZBwSpBTSokvJTCAYNUNoOBUtwWiaVjuKLfroAqdfISHEz7nc/640?wx_fmt=png&from=appmsg)

好了，That’s it~ 这就是Chai的核心思路，基于这么一个设计，作者宣称Chai能比较复杂的系统中的密码学误用进行更好的审计。作者对处理SSL、JWT和SAML的代码库进行了分析（47个代码库、8种不同的编程语言），当然也测试了不同的大语言模型（包括GPT-5.5 (gpt-5.5-2026-04-23)、Gemini 3.5 Flash、Claude Opus 4.8, 以及Kimi K2.6），在分析的47个代码库中最后揪出来了13个“少数派”存在问题：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolULVs5kTpMs4mSCXDUS8IKx0wico1I3JgWLKMb2Nr9V5FfVl19sudJnNv4m0ZcW67q12JUncic5JwDiacJ7eHqKqbGQ1MUuCoibZX0/640?wx_fmt=png&from=appmsg)

当然，作者也和旧时代的工具进行了对比，发现Chai能够找到的新问题基本上是旧时代的工具不能发现的，嗯，这一点上又要归功于AI的进步了。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolXKxzAzsHP7P90tdo1dEYSSiaC3NFefiakbqziaLfvmsGmsZDFupmXSkt4T2MmUgtAFycc86bRS5BL6Z58uhPIP4XKru1s0f7Bga8/640?wx_fmt=png&from=appmsg)

作者还进行了一个测试：不使用他们发明的targeted audit，而给AI一点提示（比如指明哪个文件包含了漏洞，或者指明哪个commit修复了问题），这样评估了一遍，发现即使是在指明了有问题的文件的情况下，表现最好的Claude Code（Opus 4.8）也不能稳定地发现问题（10次测试做不到每次都能发现问题，特定的漏洞甚至只能1/10的概率发现）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolW80KAkSSd0TCIu9fU9n9dzZM6ibNjP3zmnQUk0hzybySaAy60K6RceiapVU3aQghzyNRc0ZfB99FRaEnGKkzOuxwdpUKROeURuY/640?wx_fmt=png&from=appmsg)

好了，让我们看看这个“Chai能发现，Mythos发现不了”的wolfSSL密码学误用问题：这个问题其实是wolfSSL在执行X.509的证书链验证（chain validation）过程中的一个bug，简单总结下来就是当wolfSSL验证一个叶子证书的证书链时，正常情况下应该是把根证书和中间证书全部考虑进去，但是这时候中间证书**只是暂时性地作为可信证书集合的一部分**，如果一个中间证书没法link到有效的根证书，它也就没法形成有效的证书链，就应该从可信证书集合中移除。然而，如果有一个中间证书的`Subject Key Identifier` SKI）字段缺失，wolfSSL在某一次特定的验证过程中，只要把它临时放进可信证书集合**就一直到验证结束也不会把它拿掉**，那么如果现在还有另一条证书链，从叶子证书一直link到了这个本该被拿掉的中间证书，wolfSSL也会认为此时已经有了一条可靠的证书链，从而认定了这个叶子证书的合法性。

最后补充一点看法，其实从过去的几十年的人类知识宝库中，我们可以挖掘出来非常多的有效的技术，就像今天这篇论文实际上就是在前人的工作基础上做了一些AI增强（原谅我们的评论）。那么，我们真的是充分把这么多年的安全研究工作的积累利用和发扬光大了吗？还是说大家只是在这里坐以待毙，等着AI来收割一切（而其实并不能做到）？

---

> 论文：https://arxiv.org/pdf/2606.26933

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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