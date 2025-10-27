---
title: G.O.S.S.I.P 阅读推荐 2023-03-03
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494369&idx=1&sn=6bd9dd2b8180df337204a5fcee154864&chksm=c063c438f7144d2e44f22b0546633e1437fcc500fca7e436510d401a7d8e00c275e96163d595&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-04
fetch_date: 2025-10-04T08:39:43.605561
---

# G.O.S.S.I.P 阅读推荐 2023-03-03

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSBczGXLuc1uZpKOyVic6bosQxP84VRv5wk0VbIOBsOa9UicR0iaTI17L0w/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-03

原创

G.O.S.S.I.P

安全研究GoSSIP

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSW7jwRFAIJwZwD662oNy4GUwEn9pyktpVUyBtKOBKhmm0weqOOnkzsA/640?wx_fmt=png)

上了年纪的读者看到这幅图，会不会一下子回忆起许许多多的往事？在网上结识了网友mm，想要了解一下她的IP地址和所在地理位置，说不定就像《第一次亲密接触》那样来个线下会面。可惜，这里面发生了很多故事，也导致了我们今天的推送多次发送都遭遇到【审核失败】，我们现在也逐渐告别了QQ，转向微信。但是研究人员没有忘记，今天要介绍的NDSS 2023论文 *Hope of Delivery: Extracting User Locations From Mobile Instant Messengers* 就试图在手机端重现当年珊瑚虫QQ的辉煌！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSLw72XvASFQia651ovw4998hePRb55iaK7khGz945krf82EuENyqCVOaQ/640?wx_fmt=png)

在这篇论文中，位于德国、美国、荷兰和阿联酋几个国家的研究人员联合开展了针对Signal、Threema和Whatsapp这三个常用的IM软件的移动版本的网络测量实验。按照下图所示的流程，首先，在不同的地方（德国、希腊、荷兰和阿联酋）通过发送数据包并测量时间延迟，分析这些IM软件的服务器位置；其次，选择同一个地理位置，让邻近的两台手机（可能是Wi-Fi也可能用了移动网络）互相通信，进一步测量通信数据的各种特性；最后，对收集的数据进行分类，看能否和其他流量进行区分，从而帮助判定相关的位置信息。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSdGwhZuY3eWsCT0HknkiafQJkoaicbgGMcsV3b8ibzGfJDkicicl8gmVCykg/640?wx_fmt=png)

作者的实验具体设定如下表所示，选择了不同的地区和不同的手机（手机设备看起来有点老），还使用了一个比较古老的Android app——tPacketCapture来进行无root环境的手机抓包。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSlIdkHZVbAicTzGOWlSiae7HcEbs6jWX4ru91bw8AflWzFPQ2CWiazBsSQ/640?wx_fmt=png)

经过初始的分析，首先能够确定的是Signal、Threema和Whatsapp三家IM的TCP包的长度特征：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSADR1vwAt7s5yXrn6OaAic78YpAWsXmMvJGlJdPOCqxHRaKDpMiaqtkIg/640?wx_fmt=png)

仅仅是基于这些长度特征，在做区分的时候，就可以看出来特定的IM软件的运行数据（当然这些数据可能也是在比较纯净的运行环境下才容易区分？）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSxjtHiazsxia8Wt6HdCEfSrf6VpZR6wPMpIzXNPusQNM1WowiaEibHPFwUQ/640?wx_fmt=png)

其次，由于实验的过程中，不同设备的位置都是研究人员已知的，所以可以通过测量收到通知信息的时间，寻找设备与IM服务器地理距离的相关性：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSxIGo4IvhNEic7A5Rs1ok6PGNJHZTLcAnlr114ssCRj50JSLFicfiaXibPQ/640?wx_fmt=png)

最后，作者想要回答的核心问题是，诸如所在的地理位置（国家、地区甚至城市）以及手机使用了Wi-Fi还是移动网络这些差异，是否能够通过他们的测量和分类进行区分呢？来看看实验数据，首先是针对所在国家的区分：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSlrIeuxRzYmEDHHicmpSm5ibZwB1pnUzeibJMjKznFKuSlH3LL8PGoetCg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbS9l9tXmiaxxGVrc8lMuPbEEDeED6meL95ZarzuOna6RT6rNTciaUCUnBA/640?wx_fmt=png)

上面的数据表明，并不是所有情况下，都能很好地区分IM用户所在的国家。如果你使用的是Signal且刚好在德国（而不是希腊和荷兰），区分度还是比较明显的，但是要区分你是在希腊畅游地中海还是在荷兰看郁金香，误报率就一下子会上去。看来想要精确检查网友的行踪也不是那么容易的，作者指出，如果是对两个距离较远的位置进行区分（到底网友是人在蒙古刚下航母，还是就在你家隔壁），是容易做到高精度的（见Figure 9）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSQhtuoO715ziciaJicDyIMia8ibkGrusGCkibUoYKhc2NDnCvZbYXmXD7LOMw/640?wx_fmt=png)

如果想要区分在同一个国家（地区）的不同位置的IM用户，采集到的数据是否支持这种更为细粒度的区分呢？下面的实验数据其实一定程度也是支持这种区分结论的。虽然有一些情况下（猜测用户在地点A还是B），实验数据表明这种区分器准确度在60%，也就比随机瞎猜的50%好一点。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSoyU3o3hdll8ljw3zsVM1BZLdT7WSlb3Sdpyic79yYTK722d07qPicXicg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSdK4aGFD97xibFNu3h1AHVZgnh1EdKic7zic2VXjicpADXYAAxWPicCV1Zkg/640?wx_fmt=png)

如果用户在不同的地点使用的既有移动网络又有Wi-Fi的情况，那么区分性会更加明显。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSKaMtK5mx1vvxYS6iaGEticOd2BCUnWgZ9y6q7O0RVBA3Q8K0184mE9BA/640?wx_fmt=png)

总之，在这种可获得探测信息非常少的情况下，我们的作者仍然实现了一定程度的区分（见下图），也对不同IM的服务器进行了地理位置的测量。尽管我们回不到那个随便查看网友IP的年代了，但隐私保护的飞速发展（除了那些“发表于上海/萨拉热窝”的提示），是不是也能促成更多的痞子蔡和轻舞飞扬呢？

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSzuoRibqgNILb19RiccBf7oDiaUFvMmiaEa4BPFFjpjpr8p59sVcIq75yCg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21F6dicyYNLPKd1NZLYHHUIbSdFX9WzEMVUpngInWaMBef92cs15Y5P8Q748fNzZN485CickXgzTfJpg/640?wx_fmt=png)

---

> 论文：https://www.ndss-symposium.org/wp-content/uploads/2023/02/ndss2023\_s188\_paper.pdf

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