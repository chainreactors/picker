---
title: 白泽带你读论文 | Poirot
url: https://mp.weixin.qq.com/s?__biz=MzU4NzUxOTI0OQ==&mid=2247486134&idx=1&sn=1b494da65b669d8ca684c43aca941603&chksm=fdeb8ec8ca9c07de7743ab820b9bbbb911b33b2b060733c7f32b07d968fb6d45adf1dffddaa9&scene=58&subscene=0#rd
source: 复旦白泽战队
date: 2023-03-28
fetch_date: 2025-10-04T10:53:33.656004
---

# 白泽带你读论文 | Poirot

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW84jZBrpPg7Y0k8tDpIM1r7yT2BycpalMfNibpjHYfL34AbPUEARPicpoR1gM6ic6mopHsY5jgvriaD0nA/0?wx_fmt=jpeg)

# 白泽带你读论文 | Poirot

复旦白泽战队

**如需转载请注明出处，侵权必究。**

**论文题目：Poirot: Probabilistically Recommending Protections for the Android Framework**

**发表会议：CCS22**

安卓系统是一个经典的基于访问控制系统，它一直存在着权限控制的不一致性问题。安卓Framework层不一致的安全策略可能允许恶意攻击者不正确地访问敏感信息，此工作注重于研究此问题。

作者发现现有的工作有两个缺陷，首先它们不能准确识别访问控制的检查目标，而这可能产生误报，其次它们只检测显式的访问控制不一致性，但忽略了隐式的访问控制不一致性，这导致了一定的漏报。除此之外，作者观察到resource-to-access的控制关联在安卓环境中本质是高度不确定的，进而提出了一个利用概率推理的工具，在识别权限不一致性的同时也给安卓framework层API提供保护建议。

**贡献**

1.  作者开发了Poirot，一种可以为Framework层资源提供概率保护建议的工具；Poirot融合了概率推理与静态程序分析，解决了静态访问控制推理的不确定性问题。

2.  作者提出的方法能通过丰富的语义、结构和数据流关系补充了传统的可达性分析，这些关系更好的展示了安卓框架层资源和所需保护之间的联系。

3.  Poirot在四个安卓image上大大减少了两个SOTA工具（AceDroid和Kratos）的FP。

**背景**

安卓框架层是位于安卓中间件的java库与系统服务的集合，为开发者提供公开的API，使开发者能访问完整的安卓功能，比如相机、蓝牙等。每个安卓API会访问一个或多个安卓资源来实现它的功能，这些资源可以分为三类：

    1. 字段访问和更新
    2. 内部方法调用（比如native层的方法，文件访问方法，非公开服务方法）
    3. API调用（一个API可能会调用另一个API，这时另一个API也算是资源）

    框架层的开发人员需要实现基于资源类别、敏感性的访问控制，比如LocationManagerService 中的 API requestLocationUpdates()需要实现位置的访问控制。访问控制检查需要确保两点：

   1. 调用的应用程序拥有特定权限或满足特定条件（例如，分配了一个特定的 UID）
    2. 调用的用户有足够的权限访问资源。

    不幸的是，由于缺乏精确和完整的安全性规范，访问控制的实现可能存在不一致性的问题，这促使了不一致检测解决方案的研究。

**Motivation**

目前大部分检测访问控制不一致性的工作其实都在用“提取和比较访问相同资源的不同路径上的访问控制条件” 的方法

Kratos：给定一个安卓资源，使用路径不敏感分析来提取到该资源路径上的显式安全检查（比如权限检查或包名检查），然后进行收敛分析确定汇聚到同一资源的路径，并比较每一条路径提取的检查的集合以检测潜在不一致。

AceDroid：由于安卓访问控制的代码实现时具有语法多样而语义等价的特点，AceDroid能够基于路径敏感分析，对更广泛的安全检查进行建模并规范化不同的访问控制检查

ACMiner：前两者都是人工去定义表征安全检查的模式，ACMiner通过追溯抛出的安全异常来半自动的识别安全检查。

如前面所述，它们有两个缺陷：

1. 首先它们不能准确识别访问控制的检查目标，而这可能产生误报。

2. 其次它们只检测显式的访问控制不一致性，但忽略了隐式的访问控制不一致性，这会有一定的漏报

**缺陷1: 不精确的访问控制检查目标识别**

现有的工具认为收敛于相似操作的API是关联的，比如下图中调用mSettings.writePackageRestrictionsLPr() 的两个API会被认为是关联的。然而A只进行user ownership/privilege 检查，B还需要signature permission检查，所以现有工具认为A需要的权限更少，存在不一致的权限检查。但实际上，根据人工分析，A和B由于功能不同，不同的访问控制检查要求是合理的，即现有工具的结果是FP。造成这样的FP是因为现有的不一致性分析无法精确的查明要进行访问控制检查的目标，因此作者提出第一个insight，在进行访问控制检查时，需进行精确的访问控制检查目标识别。作者提出一个基于推理的访问控制检查目标识别做法：

1. A中的user检查部分（绿）针对的可能是黄色框中显示的所有操作（包汇聚点writePackageRestrictionsLPr ），因为它们的名字和参数值相关

2. 而B中的权限检查（红）针对的可能是黄色区域的两个install方法

3. B中的user检查（绿）针对的可能是黄色部分以及writePackageRestrictionsLPr函数，因为它们都用userid。

基于此分析可推断汇聚点writePackageRestrictionsLPr 函数很可能只与user检查相关，即A和B中很可能不存在不一致性，从而降低现有工作的fp。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84jZBrpPg7Y0k8tDpIM1r7ytqw6hOyUtE81mmWhhLabUtbXjAnIpKGlNBSGAam437Xr9T82wkN4Zw/640?wx_fmt=png)

- 左边 (A) PMS.flushPackageRestrictionsAsUser(): 刷新一个指定用户对磁盘的特定访问包限制

- 右边(B) PMS.installExistingPackageAsUser(): 为一个指定用户安装已有的包

**缺陷****2: 隐式访问控制不一致**

以前的工作基于可达性将目标资源和权限关联到一起，或者资源是否可以从受保护的 API 访问。比如A里调用的几个方法，因为都可以直接从这个API调用，因此应该至少需要A这个API的权限（绿色部分），这样显式的可达性分析可以进行资源和保护的大致关联。

尽管这种显式的可达性分析可以进行资源和保护的大致关联，作者观察到可以通过一些隐式关系（包括语义、数据流和结构），来推测资源所关联的相关保护，这样的关系即为隐式访问控制。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84jZBrpPg7Y0k8tDpIM1r7y8aHy3LSD7LP8EOWRsal9CgIia8x03q9bd1f8tfUJyhTnOBfGelB4nZA/640?wx_fmt=png)

图中这个例子B中，一个第三方应用可以操纵mAdminMaps中的内容，而这个资源用来触发setRuntimePermissionGrantState() ，紧接着就可以触发底层的特权操作（黄色部分）。由此可以看出，隐式访问控制不一致也会带来安全问题，作者提出第二个insight，即通过对隐式访问控制建模来检测隐式访问控制不一致问题。

作者处理隐式不一致问题的方式是对资源之间的各种关系进行推理，并聚合相关的控制访问信息，因为这样观察到的关系并不一定意味着某种保护关联，这种不一致存在不确定性。

举例来说，用作者的方法对上面例子进行分析：

1. 对C的静态分析表明grantRuntimePermission()方法需要权限ADJUST\_RUNTIME\_PERMISSION

2.作者将这个信息传递到它的调用者A setRuntimePermissionGrantState() ,这表明A至少应该进行至少相当于ADJUST\_RUNTIME\_PERMISSION的权限检查

3. 作者观察到，A并没有进行这样的权限检查，与此同时，A使用与字段读取相关的触发条件检查，也就是mAdminMaps 控制访问，作者认为这种字段相关的检查要纳入考虑，它可能和权限检查起相同作用

4. 作者将3中得到的隐式访问控制信息传播到mAdminMaps的写入点，也就是B

5. 作者在B中发现了这一不一致性（红色部分）

此外，图中其实还有一个辅助判别的信息，那就是A中6号紫色部分，这种相同判别条件的互斥操作大概率需要类似的访问控制，我们可以认为黄色的访问控制可以传播到6号紫色部分。

**作者的解决方案**

围绕概率，根据安卓隐式关联给的提示（语义、数据流和结构）类型和数量，计算一个资源r关联到一个保护p的概率

**方法**

Poirot首先会对给定的安卓ROM的框架层和系统类进行预处理，识别出系统服务以及它们的API，接着它会通过静态分析API来识别出其中可访问资源，并以路径敏感的方式进行访问控制检查。这里的可访问资源包括字段访问、内部方法调用，以及API调用。由于识别的资源数量过多时会严重影响概率推理，所以工具会通过预处理清除掉不相关的代码块以减少分析出的资源数目。

**基础facts收集**

Poirot首先收集一些基础信息，使用过程间路径敏感分析，该工具识别通向每个资源的可能路径，对于每一个路径，工具提取所有的访问控制检查并将它们的集合作为这个路径的代表，然后它生成一个随机变量，用来表示路径上的一个资源要求这个集合里所有访问控制检查的概率，如果这个资源被发现要其他的保护，那么给它加一个新变量

**访问控制约束检测**

对每个资源，Poirot生成访问控制约束，其实就是通过分析访问控制属性将先验概率分配给之前的那些随机数，也就是之前收集的基础facts里的访问控制检查和每个资源之间的联系。作者把一对一的访问控制依赖（一个访问控制检查只关联一个资源）概率设为0.95，一对多的设为0.6

**隐式约束检测**

这种隐式约束（结构、语义、数据流关系）提供了一个资源链接到另一个资源的置信度。

作者一共建模了七种隐式约束，分别是：可达性、触发条件、互斥性、名称关联、Getter-to-Setter、数据流和参数流约束。

**概率推理**

收集到的概率约束会传给概率推理引擎，并给出最后的保护建议，开发者可以将每个建议与对应API的实现进行比较，以检测访问的不一致性

**访问控制约束的提取方法**

在从 API 收集访问控制约束之前，作者首先使用程序分析来减少需要分析的资源，具体来说，清除了一些常用的API里的资源，这些API常用于资源检查、日志记录和metric收集。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84jZBrpPg7Y0k8tDpIM1r7yD2nJtPdJcP1kVvy5g5CWOehGiav4ov7ob0kpa0dFN2mG3zZSxUDUc5A/640?wx_fmt=png)

**基础访问控制facts**

首先，作者在ICFG上进行前向的控制流分析，识别目标资源所控制依赖的条件分支。

然后，作者处理分支来推断访问控制模式并使用defuse链提取其他相关约束，如果多条约束在相同路径上被发现，使用and进行合并，如果相反，有多个ICFG路径到达一个目标资源，就用OR进行合并

对于每一个路径，Poirot引入一个新的随机变量来表示目标需要这个路径上的约束集合的概率。

作者对于程序分析时的各种情况进行了建模，以完成隐式访问控制的推断，具体请见原文的table 1。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84jZBrpPg7Y0k8tDpIM1r7yScD2LPLMQNmGDaHNuU0Lic9VoKx9G2DlYf6mOTSAbTES0FG9KTUIHUA/640?wx_fmt=png)

**隐式约束**

首先作者对隐式建模的结果如上图，然后进行每一种隐式约束的详细讨论

getter-to-setter里是将所有的get-set都联系起来，提到的FP是对一个共享Buffer可以append，但是不能读

需要注意的是它使用聚合算法，也就是说比如一条路径上资源r对保护p的概率是0.1，另一条路径上资源r对保护p的概率是0.9，那么最后聚合后的概率会比0.9大

**实现**

Poirot由两个组件构成，一个是静态分析组件（建立在WALA上，并依赖Akka Typed进行并行分析），另一个是概率分析组件，使用（ProbLog作为概率分析引擎）

**实验**

**评估Poirot的保护建议机制**

对于每个系统服务，作者收集10%API作为测试集，其他90% API作为基础facts的训练集，最后准确率分别为77%, 82%, 84%

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84jZBrpPg7Y0k8tDpIM1r7yESWLy6NBID9zvUJl9ZrFGUC08XOSTYCE0JfIFCiaxAqSgZ9rtUWaqgg/640?wx_fmt=png)

**概率约束的影响**

统计了每种约束类型的比例

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84jZBrpPg7Y0k8tDpIM1r7yFBErHCFdYLS6jXldan2iaE0HhkwMExuDZ791VYibMrX8vyOVNtyibAwKQ/640?wx_fmt=png)

**检测不一致性的能力**

作者分析了来自 AOSP、亚马逊、小米和 LG 的四款 ROM，结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84jZBrpPg7Y0k8tDpIM1r7yic8AgIh9KhbichW67OHicyfOpJcUljOib3jHcNrcvXpIBvaUXF5rBvxlng/640?wx_fmt=png)

**降低其他工作的FP**

作者将工具与AceDroid和Kratos结合，极大降低了FP，结果如下表。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84jZBrpPg7Y0k8tDpIM1r7yGK5EmwZhfAKUr4DiaffONxO82GkM62UCtFicoeicCtez8FWmvfewhdicSA/640?wx_fmt=png)

**总结**

作者提出了Poirot，一种新的Android资源概率访问控制检测框架。该框架的特点是使用定制的静态分析收集各种连接资源和访问控制的隐式关系，将它们转化为隐含约束，以将资源与固有的不确定性联系起来，并给出保护建议。作者用Poirot分析了四个Android ROM，评估表明，Poirot能有效地生成保护建议并检测到访问权限控制不一致性。

文案：LJD

排版：YST

戳“阅读原文”即可查看论文原文哦~

复旦白泽战队

一个有情怀的安全团队

还没有关注复旦白泽战队？

公众号、知乎、微博搜索：复旦白泽战队也能找到我们哦~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

复旦白泽战队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

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