---
title: G.O.S.S.I.P 阅读推荐 2024-10-24 To Write & To Execute
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499061&idx=1&sn=5dcaf8b4e41019ff274f07adc4835ec9&chksm=c063d3ecf7145afad32ae9e9da2506d892e5eff2cffa13fd85aec28562bc09e9e8a8f066f4e6&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-10-25
fetch_date: 2025-10-06T18:55:54.030922
---

# G.O.S.S.I.P 阅读推荐 2024-10-24 To Write & To Execute

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21HiadSd2NGWah1cxe3anyqNMwju9T8uDXddfvjnE0FH86vMkWnMvMTkealZaP0QpeXNLKZxQDSSvLA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-10-24 To Write & To Execute

原创

G.O.S.S.I.P

安全研究GoSSIP

针对内存溢出的经典安全防护策略之一的`write-xor-execute`（W^X）最早是在什么时候开始应用的呢？根据维基百科的介绍，这个策略最初应该是在2003年5月在OpenBSD上部署，然后微软也很快跟进，在Windows XP上部署了名叫DEP的策略（年长的读者是否有印象~），而Linux从Linux Kernel 2.6.18-8（2006年9月，那时候还没这么多政治）开始也引入了相关的防护。这一晃已经过去了20多年，世界已经大变样，可是研究人员发现，即使现代的操作系统号称已经全面普及W^X（包括user space和kernel space），还是有很多旮旯里面依然存在可执行的栈内存（executable stack）。没想到吧？赶紧来读读今天这篇NDSS 2025论文——*Too Subtle to Notice: Investigating Executable Stack Issues in Linux Systems*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HiadSd2NGWah1cxe3anyqNMKjEtWc4pheGIZZD8rby4GKpy6bgeRnJEvGVskW7J4hLAAiajkCwR4xw/640?wx_fmt=png&from=appmsg)

首先介绍一个叫做"BadAss"的概念：仔细观察下面这张图里面包含的两个不同的编译过程（都是把一个非常平常的`hello_world.c`编译成可执行文件），两者唯一的区别是第二次编译时候引入了一个空文件`a.s`，而这个看起来人畜无害的空文件居然让编译生成的可执行文件的stack变成了可读写且可执行，真是有点奇妙对不对？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HiadSd2NGWah1cxe3anyqNMfMkrfPRqRwxu645uU4Uria4TzzicbmAibwrgWOObBskRBGpKRtCN65YEw/640?wx_fmt=png&from=appmsg)

当然这个问题绝非俄国间谍引入的漏洞，而且Linux社区至少不止一次小范围讨论过这个问题，而且你以为上面图中的例子是刻意制造出来的？错，这是现实世界中获得了3万+ star的GitHub开源项目CockroachDB的开发人员在某次代码提交中引入的问题（就是包含了一个空的.s文件，具体细节可以在 https://github.com/cockroachdb/cockroach/issues/37885 这里去查看讨论），要不是另一个开发人员好巧不巧在一台部署了SELinux的`execmem` policy的机器上运行然后触发了错误，这个问题可能还一直没被发现。

从这个问题出发，我们今天介绍的论文展现了令人愉悦的阅读体验：和别的 八股 论文不一样的是，作者没有使用什么考研英语作文模板，而是像侦探小说一样去抽丝剥茧，一点点带着大家探寻BadAss这个问题的起因和现状，让人大受震撼。

首先，作者想要了解一下开发人员对这个问题的认识，但是估计找太多开发人员很麻烦，于是就 狡辩 指出我们应该去调查的是那些负责安全的开发者，如果他们都对这个问题不了解，那就说明大家基本上都忽视了BadAss这个issue，对不对？当然，你是不是以为接下来作者又要去采访一堆人（甚至又要看到那个什么codebook），那就又错了！我们亲爱的作者把研究对象定为安全工具而不是它们的开发者，直接去分析那些以security为主要设计目标的程序。在本文中，作者把目标集中在一类叫做Inlined Reference Monitor（IRM）的工具，实际上就是代码插桩、代码注入这类工具（你确定你不是要去找rootkit？），因为作者觉得这类工具既然都已经要去保护别人的安全了，那肯定是要特别重视内存防护对不对？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HiadSd2NGWah1cxe3anyqNM2p6FgHCYDAqjlAT076N5WRWuSic039R2YSkm8ia9bbpaVicbLlnK2bE4Q/640?wx_fmt=png&from=appmsg)

作者设计了这么一个实验，先开发了一个开启了W^X防护的二进制代码，然后用IRM工具进行注入防护，再检查看看是否出现了executable stack，结果呢，上面表格里面竟然有超过一半的IRM工具中招（或者说害了别人）！究其原因，其实就是在IRM工具对二进制代码进行重写的时候，对于汇编文件（.s）忘了加入`.note.GNU-stack`这么一个特殊的段，就会让重新编译出的二进制代码中的stack变得可写可执行！（不过据说在旧版的GCC工具链比如GCC 9.3.0上并不会产生这个效果，而GCC 12.1.1这种实际上会有一个warning信息 `/usr/bin/ld: warning: trap.o: missing .note.GNU-stack section implies executable stack` 提示用户）当然要修复这个问题也很简单，就是往汇编文件（.s）里面加上一句：

> .section .note.GNU-stack,"",@progbits

当然，上面都只是一些简单的调查，接下来要进入到技术分析环节，我们在上课的时候（嗯，特别是某交通大学的《计算机系统安全》课）里面都会学到如下的编译流程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HiadSd2NGWah1cxe3anyqNMumbibonU4k5JTnLLC164UVtahNj7tibiawExkngX1fS7tLQKlOCcH8IYA/640?wx_fmt=png&from=appmsg)

但是在本文中，我们要看到的是更为细致的编译流程（Linux系统）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HiadSd2NGWah1cxe3anyqNMbllH7PI97ibCYxNc1NVdbCX7jl2yLAcbREGogtTd3NHmJx2bPkF450A/640?wx_fmt=png&from=appmsg)

在这个复杂的流程中，各个环节都可能包含产生executable stack的情况，我们来详细看。首先是下面的一个代码实例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HiadSd2NGWah1cxe3anyqNMPF3Hic8eO92rMMWmoy3eg5xOtblJog5FuFNzgsFibyZFpMaXJ1OariaVg/640?wx_fmt=png&from=appmsg)

在这个代码实例中，由于所谓的nested function（在函数f里面还定义了一个函数g，记得当年好像刚从pascal转到C的时候，我就会这么写代码…… 注意，这个并不是规范的C和C语法，只有GNU C这个奇怪的扩展才会支持，甚至GNU C都不支持）的引入，GCC非得让stack变得可执行，还专门在生成的.s里面进行了如下标记（注意到里面的那个扎眼的x）：

> .section .note.GNU-stack,“x”,@progbits

GNU的汇编器`AS`在处理那些手写的汇编代码（.s文件）时候，必须要人工指定`--execstack`或者`--noexecstack`选项，如果不指定的话，默认就只看代码里面`.note.GNU-stack`后面跟的描述是否为空（或者说有没有找到`.note.GNU-stack`）。只要`.note.GNU-stack`的描述不为空或者没找到`.note.GNU-stack`，就会产生executable stack，这也是论文一开始那个例子的问题所在。

进入到链接环节， GNU的链接器`LD`在链接多个不同的object文件（这里面可能都显式指定了`.note.GNU-stack`，也可能都没有，或者部分指定了）时候，情况非常复杂，下面这个表算是一个可供查询的“真值表”，具体的解释大家可以参考论文的Section V.C：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HiadSd2NGWah1cxe3anyqNManNmf5jaDoSmmDjkctrYoicj1dafAViaPLHkdRpUEw3DZfQpASiaIAbaw/640?wx_fmt=png&from=appmsg)

然后进入到可执行文件加载到内存的阶段，首先看看主可执行文件的加载，这个阶段主要是由Linux内核来负责加载并设置stack的属性，可是这里作者发现了内核的一个“devastating feature”——允许把所有的可读的内存页（不光是stack）统统设置为可执行（设置为`READ_IMPLIES_EXEC`这个特殊的属性）！为什么会有这么个炸裂的特性呢？内核开发者（你不能批评他们，也不能用科学实验告诉他们commit可能引入bug，但是他们可以删掉你）在这考虑了很多兼容情况，比如在ARMv6以及更早的CPU上没有NX bit支持等等。特别地，对于IRM工具改写过的二进制文件，由于它们大部分会设置`PT_GNU_STACK`段里面的`PF_X` flag，也会导致stack变成可执行！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HiadSd2NGWah1cxe3anyqNMicXS8CYowcsE9ibRzWBwHVKEVnLs66z62Lpg2rib971veKicWuC4C8IMWw/640?wx_fmt=png&from=appmsg)

最后是动态链接库的加载，loader在这一步对stack的属性设置既取决于动态库本身的`PT_GNU_STACK`段里面的`PF_?` flag的情况，同时也要考虑到主可执行文件的`PT_GNU_STACK`段里面的`PF_?`情况：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HiadSd2NGWah1cxe3anyqNM5CQO6z4f1RliaulxrRp9hJFLqB1o6ux5FZtHCyUjsrf6rKAaHVu2WYQ/640?wx_fmt=png&from=appmsg)

把所有这些情况综合起来，画成一张图，就是下面这幅图啦！用一个词总结，就是error-prone对不对？其实对于（我这种）读图困难的人，看看上面的文字解释反而更容易理解~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HiadSd2NGWah1cxe3anyqNMRb7RjT5gs5v50XgfLoDdzASDBoVTCT6o4fmtdFBc7rEOTWYicRww6fg/640?wx_fmt=png&from=appmsg)

最后，作者还发散思维了一把：既然进行二进制代码的重写有可能误把W^X关掉，那么有没有可能同时也把其他一些安全加固措施也disable了呢？带着这个思路，作者去调查了`PIE`、`RELRO`、stack canary、`FORTIFY_SOURCE`和Intel CET这几个安全防护特性，结果发现所研究的11个IRM工具里面，有三个会关闭掉`FORTIFY_SOURCE`特性，而所有11个工具都会禁止Intel CET（这是和Intel有仇啊）！具体细节可以参考论文的Section VI哦

最后的最后，再多说一句，以后我们会在阅读推荐的末尾给出G.O.S.S.I.P对于一篇论文的推荐指数，其实也是想跟大家说，千万不要神话论文审稿人，他们跟你我一样。

> G.O.S.S.I.P 推荐指数：strong accept

---

> 论文：https://huhong789.github.io/papers/ye:badass.pdf

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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