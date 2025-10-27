---
title: G.O.S.S.I.P 阅读推荐 2024-11-07 区域化的艺术
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499120&idx=1&sn=ab2c4c9491fcf2ebc01864b25d89167d&chksm=c063d3a9f7145abf5581b31a4542980a9189f11e853accfb2c8a8541dc0ee69320fbfe074254&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-11-08
fetch_date: 2025-10-06T19:20:07.146197
---

# G.O.S.S.I.P 阅读推荐 2024-11-07 区域化的艺术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21G05iby6wSZFI9xfBKodAHjianPQtMlWZt3LDCia5uClxlic9NySLIiaHuXLnXQNdiavPYEib0MTeOXBTlzA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-11-07 区域化的艺术

原创

G.O.S.S.I.P

安全研究GoSSIP

关于 compartmentalization 这个单词，你今天看到它第一印象是什么？是不是下面这幅图？（嗯，老美的网格化管理）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21G05iby6wSZFI9xfBKodAHjiasyZaiczoQ4iaRDpaNldMWvLab0qx9GBQaiaF3GOhjHk0PkzvoWRLDaSzw/640?wx_fmt=png&from=appmsg)

小时候对于 Compartmentalization 最初最深刻的印象，是从泰坦尼克号的海难故事里面第一次了解到。当时读到关于冰海沉船的历史事件描述，里面专门提到了这艘巨轮有一个设计：船体被分为16个水密舱，舱体进水时水密门自动关闭，这样即使有4个水密舱进水，它也能漂浮在海面上。然而好死不死的是当时泰坦尼克号遇到冰山的时候进行了躲避（没有印象的童鞋快去看电影补课，不是叫你去看凯特·温斯莱特的），本来直接撞上去可能还没事，结果和冰山擦身而过却划破了船侧，拉出来的一个大口子导致5个水密舱（也有说6个，反正刚好超过4个，天要亡你啊）进水，最后又加上一系列的设计缺陷，导致本来就算是出事了也可以在海上漂个2天才沉的事故变成了2小时就全部沉到底。。。不管怎么样，小时候看完这个记载，对 compartment （虽然那时候还不认识这个单词）的概念有了印象非常深刻的粗浅认识。

进入到计算机的系统性学习后，大家肯定很快就会从软件工程的模块化设计、操作系统的进程隔离这些知识里面了解到计算机系统中大量使用的compartmentalization思想。特别是在计算机安全研究领域，对系统进行分区权限控制已经是安全设计的common sense之一了。尽管如此，在实践中我们还是会遇到很多很多的麻烦，如果简单的“划分+隔离”有效，那么想想过去的几年是什么个情况呢？世界没那么简单，所以今天我们要给大家介绍的一篇IEEE S&P 2025的论文*SoK: Software Compartmentalization*就是要全面总结过去、展望未来，让安全研究社区能够更好地思考我们究竟应该怎么去做好compartmentalization：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21G05iby6wSZFI9xfBKodAHjiaCEMBMnXgrb33lFnwdDRX9DmK0aDYc8u2miaiaFZzBbsuwvAwhXfO2bCg/640?wx_fmt=png&from=appmsg)

当然，前面讲了半天，我们都还没定义什么是compartmentalization，请看论文给出的定义：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21G05iby6wSZFI9xfBKodAHjiaRYFvDNQopAj5RD3s6ia8DIFiaf1f3OrkXWa6c5L5ic0qR9IzbibIvutpEQ/640?wx_fmt=png&from=appmsg)

这个定义包括了两个要点：第一是要把程序分隔为至少2个以上的domain（也就是compartment，我们在这里权且翻译成“区域”，并且把compartmentalization翻译成“**区域化**”），第二是在运行时对不同domain实施不同的隔离策略。从这个定义出发，对于compartmentalization而言最关键的点在于在区域与区域的边界上要进行严格的控制流和数据流检查。作者把这个关键的需求叫做*interface safety*，后续的讨论也围绕着这个核心的安全需求展开。除了安全问题，论文还特别关注了其他三个和compartmentalization息息相关的要素：

1. 实施区域化之后，软件的性能（performance）；
2. 实施区域化之后，软件的兼容性（compatibility）；
3. 实施区域化之后，软件的可用性（usability）；

总结一下，就是对实施区域化分割的软件的安全性、运行性能、兼容性和可用性这四大要素进行评估。这样看起来是不是很清晰呢？当然啦，假设你现在遇到一篇关于compartmentalization的论文要审稿，无非也就是看这四方面的要素，所以只读到这里，还没法体会到这篇SoK论文的妙处，我们就照着刚刚的这个假设（需要去审稿一篇关于compartmentalization的研究论文），继续往下看，就会发现，作者给了我们一套非常有效的方法论去系统地审视所有的compartmentalization相关研究工作，不管它是关于什么，怎么做的，只要拿着作者给出的框架往上一套，基本上就能很好地评估一个工作是什么类别，然后再根据论文后面的一些评价标准去评估它到底行不行。

那么我们就详细介绍一下作者提出的这套方法论，首先它主要是考虑了compartmentalization的几个核心特性，首先关注的是主体性（subject selection），这个名字听上去有点让人摸不着头脑对不对？这也是这篇论文的特点，光看concept你会觉得很晕，但是一旦看了作者的举例解释你又会觉得很清晰：所谓的subject selection可以分为code-centric、data-centric和hybrid三类划分方法，第一类（code-centric）划分方法指的是在实施区域化时，把程序代码作为主要的考虑对象，例如把浏览器的主体代码和使用的第三方库划分成不同的domain，或者在一个程序里面把能够访问密钥的部分和不允许访问的部分划分为privileged和non-privileged domain；第二类（data-centric）划分方法是指对程序运行之后的状态进行划分，例如以process或者thread为单位来分隔不同的domain和权限；注意到前面两类划分方法并不互斥，因此有了第三类（hybrid）划分方法，可以同时使用前两者的特性。作者特别指出，第一类（code-centric）划分方法特别适用于程序代码的各部分有着明确且不同的职责的情况，而第二类（data-centric）划分方法适用于那种相同的代码要去处理不同的数据（有点context sensitive的意思）的情况。

接下来，作者考虑的是compartmentalization的目标性（target property），也就是在实施区域化之后希望满足什么目标。这里面有我们非常熟悉的两个目标——integrity和confidentiality之外，还有一个可能往往被忽视的availability目标，这个目标主要指的就是实施区域化后的domain不能影响其他的domain，我们平时最熟悉的例子可能就是docker的容器隔离的情况：除了一些基本的资源隔离之外，我们也要考虑到一个容器是不是会把整个主机的CPU和内存资源都吃光了，如果它一个容器全部消耗掉了所有的资源，其他的容器即使没有被侵入也会受到影响。

最后作者考虑了compartmentalization的防御性（trust & thread model），这个性质主要是确定compartmentalization的到底要给被区域化的不同domain带去什么样的防护能力。这里作者再次甩出三个名词——sandbox、safebox和mutual distrust，让我们继续解释。sandbox指的是domain的权限受到了限制，而系统其他部分不受限，这个很容易理解，毕竟“沙盒”这个词已经深入安全研究者的人心了；safebox则是指像TEE这种本身具有较高权限（例如访问生物传感器），而系统其他部分权限受限的情况；mutual distrust则有一点“三权分立”的感觉，就是大家把权限给拆分了，谁也不能独揽大权，除非合谋起来干坏事。

这篇论文有一个比较让我们读起来恼火的地方，就是本来读完第二章，作者就可以把整理的一个Table 2拿出来讨论了，但是他们非常啰嗦地在后面又扯了一通，我们建议的阅读顺序是读完第二章就可以直接跳到论文第7页去看Table 2以及相关介绍（主要就是总结了各种已有系统的各种特性），对第二章讲的概念有个感性认识：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21G05iby6wSZFI9xfBKodAHjiaZm5mzQTbrWcquotqtBBmxDczbhLa5gXbAZ1kaPdFJmUbJt7uYLlt1Q/640?wx_fmt=png&from=appmsg)

---

一旦理解了上面这一通理论框架（第二章），接下来我们就可以拿着这个方法论去 拒稿 审稿啦！论文的第三章就是教你怎么利用这种 文学批判理论 系统视角去审查一篇compartmentalization相关论文，马上试试！

首先，我们先去看一下待审查的compartmentalization工作的Policy Definition Method（PDM），也就是这个compartmentalization工作它是怎么去制定具体的区域化政策，这里面包含几点：

1. 实施compartmentalization的过程是否能够自动化；
2. 怎么描述特定的政策：用的是什么样的policy language，是比较粗糙的high-level的描述（placement rule），还是细粒度但是和代码绑定比较死、不容易迁移的标注（annotation）；
3. domain分割粒度；
4. 如果是自动化进行compartmentalization，依赖的方法是静态分析还是动态分析；

作者按照这四大点，就把已有的一些工作进行了总结如下表，如果你再遇到一篇新的compartmentalization的工作，就先关注下它对应上面四个点的类型是什么，然后去查一下下面的表，看看是不是已有相关的工作了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21G05iby6wSZFI9xfBKodAHjiaX2Ge8zfSsTSl68G07WIBFJicxE6tNia1UUP2HdGXP1H10TtQjNgXsKfw/640?wx_fmt=png&from=appmsg)

其次，我们要审查的是compartmentalization的设计，作者建议我们从compartmentalization abstraction的角度去审查，还给了一个很简单的model，用来对compartmentalization的特性进行抽象，其中只包含了五个操作以及相关需要考虑的设计：

1. CREATE：创建domain，不仅要考虑domain的范围，还要考虑给它分配的资源是什么，在运行过程中会不会变化；
2. DESTROY：销毁domain，同时要考虑分配给它的资源应该怎么收回；
3. CALL：切换至特定domain，这种特定的控制流变化伴随着的是权限的切换；
4. RETURN：从特定domain返回，和CALL一样标志着权限的切换；
5. ASSIGN：如何让domain和domain之间传递信息，可以通过消息传递机制，也可以使用数据共享机制，但是这里面也非常多的细节容易出错；

仔细想想，是不是其实搞区域化就是这五个关键步骤？注意到这一部分的很多内容可以提前读，当然如果你看完了model部分再来读，认识也会更深刻。

最后，我们可以去挑剔一下待审查工作的实现方式，也就是compartmentalization mechanism，从抽象的角度，要实现一套compartmentalization机制，只需要实现两类原语（primitive）：保护原语（protection domain primitive）和通信原语（communication primitive）就好，实际上每年提出的新研究工作，基本上都是在这两类原语的实现上面做各种花活。我们可以从下表看到作者列出了很多典型的实现手段，以及这些手段分别是怎么影响前面讨论的那些主体性、目标性和防御性的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21G05iby6wSZFI9xfBKodAHjia20zI8TCReicOlCQhnUoFYh76fj3hFXPQaZn44ynh8mEPWnwU532shQw/640?wx_fmt=png&from=appmsg)

搞完上面这一趟流程，恭喜你，你基本上就已经成为了compartmentalization领域的审稿专家啦！不过除了研究工作，作者在第4章继续深入去关注了现实世界的软件中的区域化部署情况，并且一针见血地指出，虽然compartmentalization这个研究方向非常火热，可真正在代码里面（特别是生产环境中），部署的情况可不怎么地。这里面问题很多，包括很多时候还需要人工去进行干预（包括进行区域划分、设计隔离政策等等），同时性能开销往往也是导致大家不喜欢compartmentalization的主要原因之一，此外还有很多现实的设计太关注性能了，在安全方面可能还会挂一漏万。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21G05iby6wSZFI9xfBKodAHjiaT4cRKl4CvlUr0YHLAvCCyNWG7lFyp0Pvuc3TwlSml6AtiaNYOBictkWw/640?wx_fmt=png&from=appmsg)

本文的一大特色是随处可见的“insight”，作者总结了很多关键的思考，这边列举一些：

1. 由于主体性、目标性和防御性的差异，世界上就不存在一种统一的compartmentalization模式和威胁模型；
2. 想要自动化生成隔离策略，往往就要牺牲细粒度，而人工制定的策略（消耗开发者的精力）一般来说是更细致的；
3. 目前的研究*过多*关注了code-centric的划分方法，对data-centric和hybrid的划分方法关注不够（显然是因为它们更复杂）；
4. 此前关于不同domain之间的通信，大都默认使用消息传递机制，而且较少考虑同步性，但是最近（可能是为了性能）更多地转向使用共享内存的通信方式，而且对同步性的要求也增加了；
5. 目前很多的compartmentalization方案对于availability目标都考虑得不够，这可能是潜在的安全威胁之一；
6. 在安全设计中，往往把domain的接口安全（例如实施严格的参数检查、输入过滤）往往被认为和compartmentalization本身的安全策略是独立的两回事（即正交的），但这种思路往往并不科学，实际上通过更好的compartmentalization设计，可以强迫domain暴露的接口不会被误用；
7. 大家过分关注domain switch的开销这个点了，似乎这个就涵盖了一切compartmentalization方案的性能开销，但是还有很多其他因素需要考虑；
8. 和现实世界的很多系统一样，compartmentalization也面临很多side channel安全攻击，现有的设计通常都不会去考虑；

作者最后总结了这个领域的一些基本的挑战，大家可以以此作为guideline来开展下一步研究：

1. 对一个compartmentalization方案而言，制定隔离策略、compartmentalization方案的模型还是compartmentalization的实现，三者是需要同步考虑、互相影响的，不存在单独去设计某一方面就能做好的，现在很多方案都是在割裂的情况下（只考虑其中某一方面）来设计的，这种局面需要改变；
2. 如何制定好的compartmentalization policy？想象一下SELinux这么多年下来，最主要的问题之一就是很难找到能够写好policy的开发者。在这点上，一方面需要更多的自动化工具来帮助那些不专业的开发者写出准确的policy，另一方面也需要给专业的policy maker提供维护和改进已有策略的机制；
3. 很多学术的compartmentalization方案考虑的威胁模型比较局限，通常假定某方面是安全的（例如提到MPK防护大家就说那我们假设内存安全是由CFI提供的），当然这个也不能怪作者，其实大家都知道不可能开发出来万无一失的防护机制，但是你不这样写审稿人又要挑三拣四对不对？
4. compartmentalization要考虑“实践是检验真理的唯一标准”，更多地落地到真实软件中去，毕竟现在学术界喊了这么多年，好像真正应用上新型compartmentalization方案的软件屈指可数（我们曾经介绍过的FireFox沙盒算一个）。

大家可能对于这篇论文的读后感会有非常大的出入，如果你不熟悉这个领域，可能会觉得觉得它非常枯燥无味（你看我们今天的论文推荐就全是文字描述），但是如果在这个领域做过一些研究的读者，相信你会很享受这篇论文的全面性。出于这篇论文对读者的“挑剔”，我们稍微降低一下它的推荐指数：

> G.O.S.S.I.P 推荐指数：accept

---

> 论文：https://arxiv.org/pdf/2410.08434v1

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