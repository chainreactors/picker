---
title: G.O.S.S.I.P 阅读推荐 2024-08-21 击败波加查？
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498709&idx=1&sn=c4efa22f24142d3299100b95afa72e1b&chksm=c063d50cf7145c1a6131b1d269376ce02d11a1c335a13deb8620bee54b662cf42a9e4f04a74b&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-08-22
fetch_date: 2025-10-06T18:03:58.863260
---

# G.O.S.S.I.P 阅读推荐 2024-08-21 击败波加查？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GNAAQ5MchKHWVHx5sPHWOcE3ZBYh35ZGlNxXSVVickiclpahsyEgMfFdOhwBsiaSSgmg8ajPLg6gm5A/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-08-21 击败波加查？

原创

G.O.S.S.I.P

安全研究GoSSIP

先问一个问题，你在什么世界顶级比赛里面获得了最后一名，却成为了这项比赛的传奇？

答案就是世界上最富盛名的自行车大环赛——环法自行车赛2024年的比赛最后一名，英国人马克·卡文迪什。号称“曼岛飞弹”的卡文迪什在2024年的环法自行车赛第5赛段中拿到了他个人的第35个环法单站冠军，从而一举超越了环法历史上的“食人魔”埃迪·默克斯（Eddy Merckx），独享历史第一。当然，如果你比较了解环法自行车赛，应该知道拿到哪怕一个环法单站冠军有多困难，以及有“关门”的规则导致很多平路冲刺车手无法完赛，今年卡文迪什早早完成历史突破后就一直慢悠悠地完赛（每赛段都考60分完赛），成为了可能是环法历史上最大牌的倒数第一。

> https://www.letour.fr/en/rankings
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNAAQ5MchKHWVHx5sPHWOc21bvfriartL1gyfxQfrgNsnIyjOHkBSNADxwc0Xr2Xlfbx4GMFmNc3A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNAAQ5MchKHWVHx5sPHWOc71ibCo0O3LQTjOQPN8OLxrVE03ECfyGAmy89Tpvg3rhX9TrljjbbicZQ/640?wx_fmt=png&from=appmsg)

不过，实际上卡文迪什在2023年就宣布退役了，因为他当时差一点就提前一年完成了“35冠王”的伟业，却因为变速器故障而错失了当年第七赛段冠军而排名第二，接下来就在第八赛段摔车退赛。心有不甘的他最终决定在39岁高龄复出并再次冲击记录，而最终实现了心愿。今天我们要介绍的这篇论文，就是从去年卡文迪什的变速器故障说起，介绍一下研究人员（也可能是饭圈粉丝）对自行车中的重要器件——无线变速器的安全攻击：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNAAQ5MchKHWVHx5sPHWOcD2TBvL3F3Lv1ZVTL3t4EPBYx8XmyeYiarvslnq5XHUUzVnzhV3vLBNw/640?wx_fmt=png&from=appmsg)

在这篇名为*MakeShift: Security Analysis of Shimano Di2 Wireless Gear Shifting in Bicycles*的WOOT 2024论文中，作者对目前公路自行车比赛领域变速器的绝对巨头——Shimano的新型套件Di2的安全性进行了分析，作者对Di2套件的蓝牙无线通信协议（私有协议）进行了安全分析，发现这套协议无法对抗重放攻击、拒绝服务攻击和通信内容窃听，在某些关键场合（比如三大环赛中）可能被某些疯狂的车迷拿来干坏事。

先来说一下背景知识，现在很多我们的读者可能也都是车友，在2020年代入坑自行车的话，不用花很多钱就能买到很好的配置，其中有一个比较革命性的零部件就是现在很多中高端自行车使用的无线变速器（wireless shifter）。早年玩车的同学们都知道，变速器和变速线的调试是自行车保养里面最主要的项目，因为这货实在是容易出问题，稍微骑行时间长一点（特别是在路况不好的情况下），变速器可能就不那么精确了，要么就是换档换不动，要么就是容易一下从n档换到了n+2档而跳过n+1档，作为普通骑行者还能忍受，在职业自行车比赛里面，关键时刻掉链子（这真是字面意义，想想伟大的卡文迪什也栽了跟头）是什么感受。随着电子技术的进步，于是自行车设备厂商就开始研究通过无线通信而不是变速线来连接车把上的变速控制器和车轮上的拨链器。这个技术突破之后，很快职业车手就用上了，然后就是各种不差钱的骑友纷纷跟进，到现在差不多就成为标配了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNAAQ5MchKHWVHx5sPHWOcvM4Ob5mz7FCfuVhpwpOBfOTlP5pDearkW4wqXH18Xn89Xse7t941Fw/640?wx_fmt=png&from=appmsg)

作者通过购买了最新的Shimano套件（没说是哪个，Di2无线变速器可能是用在中端的105套件中，也可能用在更加昂贵的DURA-ACE套件中，估计是分析了105套件）来对Di2无线变速器的通信协议进行了黑盒分析，结果发现这套协议并不复杂，就是换档。整个换档系统中，负责换档的拨链器（Derailleur，分为大盘拨链器Front Derailleur和后轮拨链器Rear Derailleur）安装在齿轮附近，而手拨（Shifter）装在车把上，两者都通过电池供能，使用低功耗蓝牙协议BLE进行通信。除了手拨和拨链器的通信，Shimano还提供了一个E-TUBE PROJECT APP来对Di2组件进行微调。值得注意的是，Di2套件在BLE之外还用了另一个轻量级的通信协议ANT+ protocol（据说是搞智能手表的那个Garmin也就是佳明搞出来的东西，主要也就是游泳健身了解一下各种可穿戴运动外围设备在用）来传输骑行数据（听上去就很佳明）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNAAQ5MchKHWVHx5sPHWOc0dWkMiaiaaibVHJP7EZVkqNrTTuPmZONHqRrggoYNJ888FBS2GAzRlZ1Q/640?wx_fmt=png&from=appmsg)

既然从背景知识中可以看到，Di2套件这些通信都比较私密，所以厂商很可能无视安全只考虑开发的便捷性。而且由于这个协议涉及的操作非常少（往上或者往下换档），只需要监听一下信道（2.478 GHz频段），很容易就发现规律（间接说明没有使用加密，或者说没有使用安全的加密模式，导致固定模式出现）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNAAQ5MchKHWVHx5sPHWOcd1KmavMAWfUoOFVP9YfaptNicQ7L5qRQEibauzGnQTALy8kvMibwXzZhQ/640?wx_fmt=png&from=appmsg)

进一步，作者查阅了一些资料后发现，Shimano使用了高斯频移键控（Gaussian Frequency-Shift Keying，GFSK）这种数字调制方式来对其数字信息进行调制，随后就成功解调了模拟信号，然后分析出了如下图所示的命令格式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNAAQ5MchKHWVHx5sPHWOc7msON81JuGic1Bp07lE8jN4uZpPGkWiaOSndKJOOgA9y2Fh8zkSibfF4g/640?wx_fmt=png&from=appmsg)

在前面这些工作的基础之上，作者分析了数据包的信息，发现它们使用了朴素的密码学防护，大概只是1995年的安全防护水平吧，里面有几个关键的问题：

1. 对消息的内容而不是整个消息进行加密，这个典型的设计缺陷在《密码学实践》里面专门提过，明显Shimano的安全人员没有读过（为什么这是安全问题，请大家思考）；
2. 缺乏时间戳和消息序列号，导致重放攻击。

接下来就是作者教大家如何破坏环法自行车赛：作者指出，在不使用功率放大器的情况下，攻击者可以在10米的距离内使用常见的软件无线电设备（SDR）对无线变速器发起攻击，攻击的方法也很简单，先靠近目前两名外星车手（塔代伊·波加查和约纳斯·温格高），监听他们的车上变速器的特定换档信号，然后重放，干扰比赛节奏（特别是在那个喜欢attack的波加查突然开始attack的时候）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNAAQ5MchKHWVHx5sPHWOc3ftr3phpk9eCRoIaUatKs9aT2Kyuz9lCPq4hyy7avFPS2zfqIQvQRQ/640?wx_fmt=png&from=appmsg)

当然这个攻击有距离限制，如果10米以内还好，10米以上效果就很差了，不过10米对于那帮环法车手是什么概念呢？前面提到的卡文迪什选手在冲刺的时候可以刷出83KM每小时的时速，也就是每秒23米的速度，1秒钟就从你面前的有效攻击范围经过了。如果在比赛选手爬坡的时候攻击可能还好，但是这些功率怪兽在13%的坡度甚至都可以刷出30KM+/h的时速，你扛着一堆设备还需要在陡坡上跟着他们跑（特别是考虑到你还要先去窃听他们的换档信号了才能重放），这个对于键盘侠长期坐在键盘前面不锻炼的家伙们肯定是个巨大的挑战。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNAAQ5MchKHWVHx5sPHWOcVYicibXJFv34v6d7b9NEKmcg5AGbBIvDibiarAAqC4Lm9ricva4jC2iafbNQ/640?wx_fmt=png&from=appmsg)

当然你也可以实施《全频带阻塞干扰》的策略，使用干扰的方法让车手们换不了档，但是这个可能只能在车手单飞的时候实施，如果对主车群进行干扰，里面可是有一大堆使用Shimano的选手哦。当然，你还可以监听ANT+通信，获取一些数据，但是这个意义并不大，现在顶级车手的各种功率数据都可以在网上查到了，这种攻击可能只会对城市骑行车友的隐私造成一定的威胁，再说了每小时不到20公里的菜鸡骑行数据可能也没啥好窃听的……

最后要补充的一点是，环法比赛实际上是要讲礼仪的，如果真的有一天总成绩车手（GC车手，指的是多赛段的总成绩排名前列，有机会争夺总冠军的车手）在比拼的时候，某个车手的变速器因为受到黑客攻击出现故障，实际上这时候要进入到比赛中立。这个并不是今天才有的礼仪，在没有无线变速系统的年代，GC车手中的任何人出现机械故障，竞争对手要等待出现故障的车手换完车之后才会进入到竞争模式，如果你趁对手故障的时候进攻，要被喷到抬不起头来啊~

再多说一句，Shimano家的变速器虽然存在无线安全问题，但是另一家供应商——SRAM的套件容易出现机械故障啊，不知道坑了多少车手。再说了，虽然电子变速器现在价格不是那么贵了，但是一般配套电变的车起码都是要用105变速套件啊，这价格也不是我们贫民骑行能够承担的。算了，反正除了可控核聚变套件，就算是骑上10万块钱一辆的自行车，难道现在这些都市骑行大军还不都是均速20公里，还不如1块5毛钱开一辆共享单车（手动狗头）。

还有一点，今天最后要使用下流量密码，给大家提个醒，本文的一作Maryam Motallebighomi来自伊朗（安全研究社区版的《我在伊朗长大》），摘下头巾之后，安全研究社区的正义指数上升了1000%，大家还有什么借口不好好去学习安全？！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GNAAQ5MchKHWVHx5sPHWOcqkdZ0icGUy9jFCKEiasfledh3F1dfNLLLiabkic0ogMzPGtZky9n4UBF0Q/640?wx_fmt=jpeg&from=appmsg)

---

> 论文：https://www.usenix.org/system/files/woot24-motallebighomi.pdf

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