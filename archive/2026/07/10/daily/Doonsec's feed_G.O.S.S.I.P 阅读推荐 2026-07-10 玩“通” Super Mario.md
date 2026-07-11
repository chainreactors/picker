---
title: G.O.S.S.I.P 阅读推荐 2026-07-10 玩“通” Super Mario
url: https://mp.weixin.qq.com/s/qQYGEp0Y7y4_itQfr5N5OQ
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:56:55.641917
---

# G.O.S.S.I.P 阅读推荐 2026-07-10 玩“通” Super Mario

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eQ0Wf6rqolXzHFH4JuwyT9EsjU3086S1qXIyx9Hyz80iafFj3pvUwXmdkAjvZC6YRn85ZOg2aDUaL6cKicmjAsdXpcEv3QFWSbbSf4wNLssI8/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-07-10 玩“通” Super Mario

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

红白机上的经典之作——超级马里奥兄弟可能是一代人的童年回忆，那时候这个游戏似乎有无穷无尽的奥秘（嗯，每一块砖都恨不得去顶一下），比如那个经典的踩乌龟然后可以不停加分最后得到用不完的生命值的trick，作为一个连前四关都过不去的弱鸡选手，小编第一次看到同伴用出来的时候目瞪口呆，而直到后来才知道原来这个小小的游戏里面还藏着更多的神秘机关，而如果你有兴趣去搜索一下关于超级马里奥速通的内容，你肯定会加倍地感觉到不可思议。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolV0bLO8XStIQxjEHHTujAgakqVGn3SicTfbWSZrd9Kn5AtWy5icqeE86mNFteL0TlunYxfkic89dZtHGoGHUbuyBTfNxghKFicCf08/640?wx_fmt=png&from=appmsg)

可是超级马里奥和安全有什么关系呢？诶，你先别急，过去的20年在各大安全学术会议上出现的不知道多少篇关于模糊测试和符号执行的论文，天天都在讨论一个问题——代码的测试覆盖率。大家似乎对工具有一种幻想，觉得只要用足够的算力支持，我们就可以把每一行代码都给测试到位，每一个bug都能被揪出来。不过今天我们就要通过超级马里奥这款游戏，介绍一个用古法来证明上述思路不可靠的实例。

先问一个问题，你知道原始的超级马里奥这款游戏需要多少存储空间吗？

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolUbgHadIyGPiclA8rNiaoW7G0bXEUuZNX3sMuXen0upAEFVtzyMWpKPVkOZsA8fqOTZacR0cmAnNKz0hicMFIwFlWS50aIUqeALcM/640?wx_fmt=png&from=appmsg)

嗯，上面的这个数据是不是让你觉得很惊讶（现在这些软件和游戏厂商是不是更应该觉得羞耻），而从这个数据出发，更有趣的一个问题是：既然只有32K字节的代码，我们能让所有的代码都执行到吗？

知名的超级马里奥速通玩家 Chris Siebert （aka “100th coin”），同时也是NES模拟器开发者和工具辅助速通（Tool Assisted Speedrun，TAS）专业选手前几天放出来了一段视频，在这个视频里面，详细展示的是 Chris Siebert 如何仅仅通过玩游戏这么一个最基本的操作方式，设法去触发整个超级马里奥游戏里面的每一行代码。

这种“玩”游戏的方法简直是带着上帝视角去看游戏，一方面你需要对代码里面每一部分的功能了如指掌，另一方面你还要受限于只能通过游戏设定的方法去想办法触发代码（而不能利用游戏的exploit，还记得我们介绍过的俄罗斯方块的内存破坏漏洞吗）：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolXGz4O1CYiaianyloW9hGArQxYsAWnzMqyb70A70RakPBib3D3cpuHD5WaommdoNzfX0pcrqbwAdruz0D9Jx7eBDTDdgM2icXT1cWc/640?wx_fmt=png&from=appmsg)

如果不是速通大师，你可能根本不知道超级马里奥里面居然还有那么多奇奇怪怪的细节（以及应该如何去触发对应的代码），所以请大家耐着性子把下面这个17分钟的视频看完（如果需要中文字幕可以移步B站去搜索相关的视频，甚至还有人把配音都转成了中文……）

看完视频（特别是看到那个带着5个乌龟去旗杆然后让旗子消失的trick），有什么感觉吗？是不是突然觉得你从来没像这样玩过一款游戏——胸中带着100%的汇编代码去玩游戏，这和一个fuzzer或者符号执行引擎有什么区别？哈哈哈哈哈哈！

可是最后我们发现，哪怕你比开发者都更熟悉代码，还是有这么一点点的代码无法覆盖，而且视频里面也做了详细的分析，相信即使把当年任天堂的开发组全部叫过来，估计他们也会觉得这些代码确实是dead code无法执行到吧？那么话又说回来了，我们的模糊测试社区是不是可以去挑战一下呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolUPdaFVUtR9RoMg1R2vlTuVPgia2O33RwTHn9sT4f7zWA5MDcLoAMnOXs6jllcYhsJB4NGsz0CeFrMniaR7p6Ne1s8k91TlnlibRw/640?wx_fmt=png&from=appmsg)

P.S. 如果要做模糊测试，大家能不能学习一下 Chris Siebert 做点有趣的工作，不要再投稿boring的论文来折磨审稿人了……

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