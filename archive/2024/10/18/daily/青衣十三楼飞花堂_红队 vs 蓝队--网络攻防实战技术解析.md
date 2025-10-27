---
title: 红队 vs 蓝队--网络攻防实战技术解析
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247487683&idx=1&sn=8b93cbf8b082220d1e4bfe5dd44ee44b&chksm=fab2d3fccdc55aeaf9654a074656950fa7e9cf6f4e564cee9382511e7d95b5dde3a0d6980efe&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2024-10-18
fetch_date: 2025-10-06T18:52:39.612513
---

# 红队 vs 蓝队--网络攻防实战技术解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPPe1Qle265DDneXWQEbD4nnxrREG1xu6a5BmcxpXViczqe3IpvlbouNFicoYMgErLAHiaUIHicyW9CEZw/0?wx_fmt=jpeg)

# 红队 vs 蓝队--网络攻防实战技术解析

原创

沈沉舟

青衣十三楼飞花堂

有本新书，《红队 vs 蓝队--网络攻防实战技术解析》。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPPe1Qle265DDneXWQEbD4nnicGADps3BsqvbaBSJz0ZgkJpRStqCPrYsMqvQ81ziaKOFjIp66zujrAw/640?wx_fmt=png&from=appmsg)

此书出版前，我看过电子版样书的部分章节，当时几位作者让我学习学习，顺便写段荐语。

当时我还真写了一段荐语，但你们在纸版书中看不到，如下:

在近些年某大型网络安全交友活动中，我与本书几位作者有过技术互动，相对而言，对他们的技术背景、技术能力比较了解。看过本书一些样章，同时涉及攻击与防御两方面，我比较感兴趣的是攻击面的内容。从我开始从事网络安全行业工作，二十多年白驹过隙，时代变迁在网络安全行业中的具像化非常明显，这里只说一点，较难在野寻找真实练手环境了，因为各行各业的安全投入、安全意识、安全法规都大大增强。过去，我们为好奇心所驱动，凭兴趣与热爱投身网络安全行业，不可否认的是，干这行必须涉及攻击，不了解攻击的情况下谈防御，别人觉着不靠谱，自己也觉得在骗自己。某大型网络安全交友活动恰恰是一个合法合规的检验攻击能力的机会，本书几位作者在此活动长期实践中凝炼经验，是有此书。受限于公开出版物，书中不能展示具体攻击场景，但提供了宝贵的攻击面思路，不妨一阅。

不要写我名字，就列个ID好了，用小写的scz。

几个月后几位作者反馈:

四哥，实在不好意思，刚刚出版社编辑联系我说，您之前的评论他们社里审核没过[捂脸]。两个原因，一个是现在不能提攻击，政治导向不行。还有一个就是言辞需要相对正式，不能太口语化。现在要么是可以返回修改一下，然后我再交过去，要么就是只能删了这条评论了，您觉得呢四哥？

我说，那就算了，没事儿，删了就是。

我一直不爱写书，就是不想跟这些编辑打交道。我国这些条条框框太多，真到中美对抗时，谁管这些条条框框啊，尽整些虚的，自欺欺人。不让提攻击的安全，就是扯淡。外行领导内行时，这就是必然结局。

再说此书。纸版公开发行，本身决定了这不是捷径式秘笈，应出版要求，已删得七零八落。其意义在于，看一下别人遭遇过的场景，借鉴一下别人用过的思路，开卷有益。若其中的知识对你已无意义，忽略即可，不必找我显摆。我始终是个学习者，在我面前显摆，证明不了什么。

不是来替几位作者卖书的。从与他们的闲聊来看，他们也志不在此，更多是种情怀吧。只是FYI，干我们这行的，不需要直达链接，姜太公钓鱼愿者上钩。

最后，「**May the force be with you**」。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPPe1Qle265DDneXWQEbD4nnKqzI4om5G69JlP4jgJ0GNTvDIwfic9JyBicJLCCy5WL2qWDiaZuNpPia0Q/640?wx_fmt=png&from=appmsg)

预览时标签不可点

个人观点，仅供参考

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

青衣十三楼飞花堂

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

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