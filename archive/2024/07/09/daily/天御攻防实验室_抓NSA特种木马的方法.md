---
title: 抓NSA特种木马的方法
url: https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485892&idx=1&sn=c04d398e85fd4ad28b7bbf714b1c9153&chksm=fb04caaccc7343ba99536892e2e3bb654867c4b5e64813a8ee69082e61de161c38ced94239c6&scene=58&subscene=0#rd
source: 天御攻防实验室
date: 2024-07-09
fetch_date: 2025-10-06T17:45:56.186810
---

# 抓NSA特种木马的方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBDcHboKGibcuiaxIHGFamYHkdLJR8g2jCqa4XRCsY9zqc2OuynoTTCt9PWtk4MMsIrwSHCtLQUYvHGA/0?wx_fmt=jpeg)

# 抓NSA特种木马的方法

原创

Zer0d0y

天御攻防实验室

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBDPcrVkIEIGfhoDxlTvUqadL92v5upicfGpdHhJoKyoXWuTHpDKCUJk4FyNF3rhty2Jg1BLANRAGRA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

我不会说只有我一个人知道这种方法，但这可能是第一次公开讨论。这就好比，美国情报机构说：“俄罗斯将在2022年2月24日入侵乌克兰”，但美国情报机构绝对不会告诉你，他是如何知道的以及从哪里搞到的情报。所以，这是不管你花多少钱，情报机构、网络安全厂商都绝对不会说的东西！
 **那么，我是如何知道这种抓NSA特种木马的方法呢？以下就是线索**

1.前NSA黑客部门TAO负责人Robert Joyce，也就是国家计算机病毒应急处理中心认为其是网络攻击西北工业大学的行动负责人，在一次演讲上透露，

“一旦攻击者进入了网络，他们会安装一些工具，对吧？通常首先安装的都是轻量级的、简单的信标工具。它们的目的是建立一个立足点，然后再将真正要执行任务的工具传输下来。我认为，反病毒软件行业有时会因为无法阻止某些攻击而备受诟病。如果你的杀毒软件只是一个不应该在电脑上运行的"坏东西"的列表，那不是一个好办法，因为这意味着攻击者只要搞一个独特的、以前从没在你电脑上运行过的程序，就永远不会被列入那个黑名单。但是，随着威胁情报的研究和技术的发展，现在更多地使用基于信誉的服务。这意味着，每一个想在你的机器上执行的软件，都会被哈希，然后提交到云端。**如果一个信誉服务告诉你，一个你认为可以运行的有趣的程序，在整个互联网的历史上只运行过一次，而且是在你的机器上运行的，那你最好提高警惕，因为它八成有问题。**”

2.前NSA TAO黑客Mike Wiacek建立了一个收集全世界可执行文件的平台Stairwell。

“在Stairwell，我们从零开始构建平台，使其具有高度的威胁防御能力。**我们收集企业内每台机器上所有独特的可执行文件和类似可执行的文件**，并将它们永久存储在我们云平台上的不可变存储库中。所有分析、扫描、处理和决策都在后台进行，与终端设备完全隔离。

虽然攻击者可能会通过逆向工程来绕过传统的安全产品，但我们的方法不给他们留下任何可逃避的空间——每一个相关文件都会被收集。我常说："没有一粒灰尘能有选择地逃过吸尘器！"在Stairwell，分析过程不会向终端设备反馈任何信息，攻击者没有东西可以逆向工程或用来测试他们的工具。此外，如果有人快速制造文件变体，我们的变体发现系统会立即察觉，从而揭露任何试图主动探测我们分析能力的企图。

攻击者从我们这里学不到任何东西，反而是我们能从他们每次的规避尝试中获得洞察，这实际上就是在反过来利用攻击者！”

3.当然，还有一些不方便透露来源的情报

A:

你在修补零日漏洞。就像你在修补零日漏洞。你不是在保护好人或坏人。你只是在保护Chrome，对吧？就像在，再说一次，如果你知道Google Project Zero知道一个Chrome零日漏洞正在被野外利用，他们说，它有美国的味道，然后决定置之不理。就像，a，它不包括平行发现。没有其他人拥有它 b，就像他们有一种归因的感觉，你知道，他们确定这是美国，并且对此感到非常舒服。c，就像，你在谈论他们放弃了他们应该做的核心职责。我认为讨论。。。所有这些讨论我们可以进行。但认为他们应该看着一个零日漏洞，这是他们自己个人负责处理的，然后置之不理，这似乎是一个荒谬的要求。

B:

所以你是在说他们应该把他们发现的每个零日漏洞都通过美国政府?
 **除本文提到的方法外，我们之前还曝光过NSA特种木马的攻击手法**

NSA的NOBUS指导原则

2013年，前NSA局长Michael Hayden在一次会议上表示“这个世界的进攻和防守都取决于漏洞问题”。接着 Hayden 阐述了NOBUS（Nobody But Us）的概念，即如果NSA认为其他人无法利用某个漏洞，它会放任漏洞不修，以助于自身的间谍活动。

NOBUS作为NSA网络间谍行动（CNE）的指导原则，而这种指导原则反映在漏洞、后门和植入物的设计上。

1.Stuxnet事件表明，NSA可能储备了大量零日漏洞。

2.NSA在Dual EC加密标准中植入的后门就是一个典型的NOBUS后门。

3.TAO在植入物设计上，会为每个目标生成一个新的公钥。
 **我们生活在“砖家”云集的时代！**

某些单位，搞出个什么“挂图作战”（挂图扯蛋），说是什么核心关键技术，笔者怀疑这帮人会不会就是当初那帮喊态势感知（泰式按摩）的那帮人。
 **我们连最基本的检测、响应、取证也没解决好！**

这些年，国内网络安全行业都在“追星”，每年都有很多新名词，但是，最基本的检测、响应、取证都没有做好。谁要是说，帮国家网络安全、行业解决了“卡脖子”问题，无非是欺人愚己。

有一些网络安全厂商宣称自家的大模型是高级安全专家，能自主干活，替代安全专家，“一台机器人能够提供相当于60多位安全专家的运营效率”。

在笔者看来，生成式AI/大模型等人工智能技术只是辅助工具，能够辅助安全专家做一些事情，能自动化做一些事情，但绝对不可能替代安全专家。

生成式AI也好，大模型也好，无非新瓶装旧酒，新技术解决老问题。

不仅是人工智能、网络安全，

新型基础设施，如量子互联网、卫星互联网、天基物联网、海底光缆、海底导航系统、下一代通信网络，以及清洁能源、汽车、半导体、通信技术等

核心关键技术都掌握在西方手里，所以咱们也别总说“遥遥领先”、自己产品、技术多么牛逼（真不是那么回事），别总想着搞钱。多务实，干实事，多想想怎么为行业、国家贡献力量！

最后，

去他的挂图作战，抓不到西方APT的技术，都是狗屁！

**推荐阅读**

**闲谈**

1. [中国网络安全行业出了什么问题？](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485457&idx=1&sn=d45cc35242cdc83e98b124531ea7c093&chksm=fb04cb79cc73426f21801f35912b626bf515dc2b9d85b3da578f8087d0a2960396ef1e6347bc&scene=21#wechat_redirect)
2. [国内威胁情报行业的五大“悲哀”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484999&idx=1&sn=485863f4e66a62f55aa69334c787e6f3&chksm=fb04c52fcc734c3919fc28c61a9b13488b89efe4c1ba5cb16f8f00f0c6e996c7f1df47984463&scene=21#wechat_redirect)
3. [安全产品的终局](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484846&idx=1&sn=35bab89f917f5043919e40893268d576&chksm=fb04c6c6cc734fd05c0423dc971a0578eb8b951ef1764be0a99e2bdd1c26b736d64cf61b6d77&scene=21#wechat_redirect)

**威胁情报**

1.[威胁情报 - 最危险的网络安全工作](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485331&idx=1&sn=0857185a1bc7ed04c2d1edc60cb93a34&chksm=fb04c4fbcc734dede0fd243984c30250ff7859f68a265b1a278ac72a5761ac0ccaf0038537ec&scene=21#wechat_redirect)
2.[威胁情报专栏 | 威胁情报这十年（前传）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484880&idx=1&sn=c2b5730f2a7011959096526ff775c8ac&chksm=fb04c6b8cc734fae9f6d2e0693cecd5fd594a01694d8e38bd95926cb88a0f627c3d5b2f36ea2&scene=21#wechat_redirect)
3.[网络威胁情报的未来](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485003&idx=1&sn=76253d23e51dde8dbf4d675b79ab43cf&chksm=fb04c523cc734c352490ca37f55f1c3a989d55807298cb308aa3c126e24816d6fda11a8766f1&scene=21#wechat_redirect)
4.[情报内生？| 利用威胁情报平台落地网空杀伤链的七种方法](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485042&idx=1&sn=afd1212b585f30bccdece8471fadd31d&chksm=fb04c51acc734c0c9fd0d1d388b7672defbe5ce17a10af58d3a5d336ba21fa21398b4ad860e2&scene=21#wechat_redirect)
5.[威胁情报专栏 | 特别策划 - 网空杀伤链](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484709&idx=1&sn=649a27516ca01baab49ce750e3502cc3&chksm=fb04c64dcc734f5becd252686228f6c3c2bd00bff52041e9dae6fde2008e1a43057989b9d16f&scene=21#wechat_redirect)
 **APT**

1. [XZ计划中的后门手法 - “NOBUS”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485524&idx=1&sn=aa2b7b0d57b250e5cc101e5dcbebbca6&chksm=fb04cb3ccc73422a9fe22937b801eceb205ceaf8bf3b76a92143d575d55e5fd2eef5adfacb36&scene=21#wechat_redirect)
2. [十个常见的归因偏见（上）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484868&idx=1&sn=3d65e81115c967b165fa16021a211967&chksm=fb04c6accc734fba7c760fd14caaaf9a2d7991acc2557ee340e772ccbb805b30f1a46c793e8a&scene=21#wechat_redirect)
3. [抓APT的一点故事](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485237&idx=1&sn=9152fcb5f5b1f884e6da97ba9b04f69a&chksm=fb04c45dcc734d4bd8fbede2ae93dc52feeaaa11e215a3240bca32f3d43444a2c909e01a2814&scene=21#wechat_redirect)
4. [揭秘三角行动（Operation Triangulation）一](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485278&idx=1&sn=9def52d0d9063e86acb16533be2a52e8&chksm=fb04c436cc734d20b8c67348f7db21fa10921ad3826b37c713e847b73972f50de82b6c1f1e6b&scene=21#wechat_redirect)
5. [闲话APT报告生产与消费](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485325&idx=1&sn=d0219cfe811afe5e8fc8729c603de2bc&chksm=fb04c4e5cc734df3a8ad433a992172c1a9a0f236fd69550c72eb499e1202d23b81f32b379259&scene=21#wechat_redirect)
6. [一名TAO黑客的网络安全之旅](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485451&idx=1&sn=5f794deaaccf45e7d81958eba82cd556&chksm=fb04cb63cc73427538546f24b1be7cd78375a9017498efb3fd2da46de5c38c0d4599c2e01100&scene=21#wechat_redirect)
7. [NSA TAO负责人警告私营部门不要搞“黑回去”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485250&idx=1&sn=a35def8b58f86f8a149e335f3df3a1c9&chksm=fb04c42acc734d3cdfd1e8f2ae852731c3569533ab8fa83bd0126b788ea20673a2f912cdf011&scene=21#wechat_redirect)

**入侵分析与红队攻防**

1. [入侵分析与痛苦金字塔](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485464&idx=1&sn=f05718bec99d4506a8fe1c49dc2bf337&chksm=fb04cb70cc734266a436d4225d4eb0486becaed5f0258748e6ff3de46a22caaa01b0da1b0e4f&scene=21#wechat_redirect)
2. [资深红队专家谈EDR的工作原理与规避](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485494&idx=1&sn=f45125e76dd412a291cfa3bccd5943c5&chksm=fb04cb5ecc734248332218f7df17be9a31d4b09777b8cd846b69821248a5e75b44baa6bfbfe4&scene=21#wechat_redirect)

**天御智库**

1. [独家研判：五眼情报机构黑客纷纷浮出水面](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485100&idx=1&sn=b88f8864594b76d4e1412db7cf204f77&chksm=fb04c5c4cc734cd2f5440ee760377afce1745a3abade998a40b9fe3752acb3be14574e6e6f9a&scene=21#wechat_redirect)
2. [美军前出狩猎并不孤单，美国网络外交局优先事项分析](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485570&idx=1&sn=38c8f12e5167bddaf62fde58b5448eb0&chksm=fb04cbeacc7342fc32dba4a5d595b166ac38ba73e89eac008ff5b170888352b3e92044451fe1&scene=21#wechat_redirect)
3. [《国际关系中的网络冲突》](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485071&idx=1&sn=b8edcb9cd0ab78d1b6f7c149dce2e49a&chksm=fb04c5e7cc734cf18c1a9c63c1ed9435ec2b93923635ea18076b5d34fe46407e3183cbef5fba&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hPq2VZ0zUBBx2ESUwvicgTOfTm1Otk2tv0jvPWFeaWeawQUfRuIichBCuk3sxT9YcXGtx6ib9jdenUHMIKuMYSDRg/0?wx_fmt=png)

天御攻防实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hPq2VZ0zUBBx2ESUwvicgTOfTm1Otk2tv0jvPWFeaWeawQUfRuIichBCuk3sxT9YcXGtx6ib9jdenUHMIKuMYSDRg/0?wx_fmt=png)

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