---
title: G.O.S.S.I.P 阅读推荐 2024-05-24 都是黑客犯的错
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498084&idx=1&sn=0ffc8fdbb0645509fed67b75bebee937&chksm=c063d7bdf7145eab06af2fce5d8b5df6ad7ddb333da5d574f8de5dae4ee59922ec71670d0a58&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-05-25
fetch_date: 2025-10-06T17:18:09.228502
---

# G.O.S.S.I.P 阅读推荐 2024-05-24 都是黑客犯的错

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21HJ42x6rl650wyicickIH7Ykncze9ACXBncqGFaMuFrRCOSOZibrHVQJVsBxgwibyppCmibaxnkPcwUFicg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-05-24 都是黑客犯的错

原创

G.O.S.S.I.P

安全研究GoSSIP

开局先看一张图：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21HJ42x6rl650wyicickIH7YkneZibW1icdFgOicWDGt2YSxShjN5EU3MXtmlcdOrmOlpsB8BPwXOpeof3g/640?wx_fmt=jpeg&from=appmsg)

当黑客有什么前途？除了牢底坐穿，也可以去当主播赚钱对不对？在电子竞技早已成为热门的网络直播项目的今天，传统的一些智力活动比如国际象棋和ACM编程竞赛也都开始进军直播界，而且已经诞生了很多明星主播，比如国际象棋界的中村光和Alexander Botez（有兴趣的读者可以去搜索一下著名的“Botez Gambit”哈哈），不过也有很惨淡的，例如B站上面好像一直有一个“前华为女黑客”在直播编程，还一直吐槽说0人观看，不知道是真是假？

> https://www.bilibili.com/video/BV1H44y1F769/?spm\_id\_from=333.788.recommend\_more\_video.1&vd\_source=696de27f58d8d02ff361e305a56be520
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HJ42x6rl650wyicickIH7YknQicug15bibmU1Pzv1QtzGfRstTteBbvsfdGzj90o5Xss6GT0Ticq1BDbQ/640?wx_fmt=png&from=appmsg)

总之，真正的黑客确实会去搞直播的，比如大名鼎鼎的GeoHot就在Twitch直播平台上直播自己写代码，当然他也会发布一些CTF解题的视频放在YouTube上：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HJ42x6rl650wyicickIH7YknRmWtxlMicWh8iaYJ1TK21yRAASpFibQpiaTARZwF6lGxyKkE0LWT3QPKmA/640?wx_fmt=png&from=appmsg)

所以我们今天要介绍的这篇IEEE S&P 2024论文 *“Watching over the shoulder of a professional”:* *Why Hackers Make Mistakes and How They Fix Them*（怎么感觉前面一直在跑题）是一篇对YouTube上面那些上传了自己CTF解题视频的up主（嗯，权且也把他们叫做up主吧）的分析。主要关注的点是什么呢？当然是想要了解这些敢于展示自己解题过程的“大神”（当然也不全是，但是没两把刷子可能也不敢上传视频吧）在“实战”（严格来说解题不能完全等同于安全研究和安全实践）中会犯哪些错误，而且调查这些错误的目的并不是要嘲笑他们，而是深入探讨作为我们这个安全研究社区群体的代表，这些安全从业人员犯错误的类型、原因以及如何避免继续犯错（毕竟太多人不懂得“前事不忘后事之师”的道理）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HJ42x6rl650wyicickIH7YknGIlQKhpb2galkamcshY1kqBUgozxT9NjiaiaItR5bZcrFSsGFCqCGvLg/640?wx_fmt=png&from=appmsg)

进入到这篇论文的细节，作者首先去YouTube上搜索了很多CTF解题视频，然后选择了11个up主（相关的分布如下表）的31个视频

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HJ42x6rl650wyicickIH7YknHpQPCagSqibgal19EhFfEqrOdPWolMHl6lWIromoyjzWIibVqZNqQN7w/640?wx_fmt=png&from=appmsg)

作者选取的31个视频里面包含了28道CTF题目的解答过程，其中有一个视频里面包含了两道题目的解答，然后有一些视频是不同的up主解答同一个题目，具体的题目分布如下表所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HJ42x6rl650wyicickIH7YknPBBnBo01Edm6oV3DpsKFJVKAOU0wUzhiaCxnVXuic7KDAdrfevkLqlyQ/640?wx_fmt=png&from=appmsg)

由于作者本身也是专业级别的CTF选手，因此可以更好地审视这些视频里面的问题（好一个“名师把脉”，教培机构也可以考虑一下）。论文里面用了很多user study的方法，比如我们以前介绍过的什么codebook，这些就不再赘述了，我们直接进入到作者的总结部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HJ42x6rl650wyicickIH7YknjvM7mzlrVlgpS5Z1tQzHAPISd9LDHQXunib18GgrZYhcIwSa5vudTtg/640?wx_fmt=png&from=appmsg)

作者把视频里面看到的这些up主在hacking过程所犯的错误归为五大类（比例分布如上图所示）：

1. Implementation：主要是指在hacking的时候，对内存地址的操作没搞对，比如下图中，本来应该是`write_offset`减去`write_addr`来计算`system_addr`，却用了加法去计算；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HJ42x6rl650wyicickIH7Ykn4MQwsngSXu35jr8lfbfnwPEz0QINiaowGMLHFbL4RBhJE8Ey8VQJf1A/640?wx_fmt=png&from=appmsg)

2. Programming/Miscellaneous：就是代码写挫了，比如下面这个例子里面，从`puts`那边拿到的地址也要用`p32`处理一下，但是忘记了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HJ42x6rl650wyicickIH7YknMBltr3G9ianibRArH87biaibeH9PlxKeLJ2BRS4eViamXEBtN5S3jkTJiaMg/640?wx_fmt=png&from=appmsg)

3. Strategy：这个大概就是委婉地说你水平不够哈哈哈，使用的exploit的方式方法不到位；
4. Tooling：工具的问题（也是人的水平问题），比如在使用GDB去调试的时候没设置好mode之类的；
5. Technical Issues：这个我们都懂，就是有时会遇到一些非常奇怪的技术问题，可能跟要去做的题目没啥关系，反而是跟自己的系统环境之类的乱七八糟的因素有关；

接下来作者继续分析了大家解决各类问题的平均时间，从下图可以看出，像编程或者工具类的问题，一般来说很快就能被发现和纠正，但是思路上的问题（Implementation和Strategy）就要花更多的时间，另外遇到那种奇怪的技术疑难杂症也很容易让人卡住。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HJ42x6rl650wyicickIH7YknyleYabHEfaOoLicnklDEtib8vOdpjJGYgSXu1I4R1o16NVAmsV9kgibyQ/640?wx_fmt=png&from=appmsg)

更细致的统计数据表明，有时你可能遇到一个没法运行代码的问题就能卡住卡到让人发狂：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HJ42x6rl650wyicickIH7YknOFvEcfiamlnc3DE2heUTJ2sKsBOjcb0crIcG1ylRw3oewRibt49KRfOQ/640?wx_fmt=png&from=appmsg)

论文的第七章很有意思，探讨了up主也就是hacker群体们在视频中如何体现出来他们在精神上和智力上孜孜不倦地与问题缠斗的一些重要因素。这里面包括：

1. 过往积累的一些经验和可复用代码；
2. 各种工具、插件；
3. 在直播过程中还和同伴交流，并且快速学习新知识

当然，作者也描述了很多人在做不出来题目时候的暴躁情绪：

> The level of irritation usually increased as the problem persisted, and a hacker felt an absence of progress. Depending on the hacker’s style, frustration could manifest as a negative self-talk

总之，这篇论文相当有趣，之前那个什么讲CTF的电视剧《亲爱的，热爱的》如果想要改进改进，应该好好阅读这篇论文。大家也可以去细读原文，看看到底是什么因素导致了自己别人水平不行。

最后，我们回到开局那张图，现在发现，其实黑客们有了一个新的闭环赛道：

> 学黑客技术->搞直播->刷写论文->刷被引用->评上教授->培养学生学黑客技术（说的就是你，Yan）

---

> 论文：https://adamdoupe.com/publications/hacker-mistakes-oakland2024.pdf
> 数据集：https://github.com/sefcom/hackers-mistakes-paper-public-access

预览时标签不可点

阅读原文

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