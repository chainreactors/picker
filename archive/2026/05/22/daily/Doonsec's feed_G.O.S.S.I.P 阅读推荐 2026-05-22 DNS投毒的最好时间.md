---
title: G.O.S.S.I.P 阅读推荐 2026-05-22 DNS投毒的最好时间
url: https://mp.weixin.qq.com/s/lbf1WPvT8JiVBR2oZvL8dw
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:33:19.197869
---

# G.O.S.S.I.P 阅读推荐 2026-05-22 DNS投毒的最好时间

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eQ0Wf6rqolVQpBCicpZySBNggWdUEl9AcqfUibCIicHK6ChTE9lXUeQ8gzIUCLuBXybXuLja7rbpZqNmh6SIziaQPps4tbavTbib6uuPX8tVnlEA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-05-22 DNS投毒的最好时间

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

*~~DNS投毒最好的时间是20年前，其次是现在 —白岩松~~*

虽然中东地区战火纷飞，今年的USENIX Security会议上我们看到了一篇来自以色列的希伯来大学的论文*DNS Cache Poisoning Like it’s 2006*，从标题到内容都非常的old school（也就是不靠LLM来帮助思考），和现在成吨批发的AI口味的安全论文相比简直是一股清流，今天我们就为大家介绍这篇复古风的研究论文（然而后面你会看到论文中逃不掉的AI痕迹）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolVkbUl04PYkcEkHdEIORzM6HQ96wc7miciaB7F8OU03YMPnbyrCT0kU7DtRPykVtxE4V5edSIM0wKKc91VWfYYl4EJypHugDMxOA/640?wx_fmt=png&from=appmsg)

DNS是上个世纪80年代诞生的古老协议，但今天的互联网哪怕一秒钟都离不开它。首先，关于DNS投毒攻击的背景知识，推荐大家去阅读来自哈尔滨工业大学的王一航撰写的综述性调研报告（嗯，知道你们不可能读长长的文章，只会问AI，虽然这篇调研报告也就10来页）：

> https://overflow.host/materials/DNS-Cache-Spoofing-Overview.pdf

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolUdlRWaJJibwWHicnWRcVFkQz148T94pIa3nZXyFA6H7EUUCibk75IS4cCS8hsh8YRXRUCia4Wiaiap9hy9icMVibqggpVUHHT5uPzdR2M/640?wx_fmt=png&from=appmsg)

读完上面这篇报告，其实对DNS投毒的核心技术就应该理解得差不多了，实际上在2026年，想要对DNS请求进行投毒，攻击者除了需要在时间上精确把握受害者什么时候发起DNS请求，并抢在正确的回复到来之前投送污染请求之外，还需要同时猜对一些关键的信息。如下图所示，攻击者构造的恶意DNS回复，里面有两个**取值随机**的变量：目标端口和Transaction ID（TxID），这两个变量理论上的取值组合可能是2的32次方，攻击者如果不是完美的中间人而是旁观者（off-path），那么要猜中其实还不如去买彩票（不是双色球，双色球你穿越回过去了也买不中）。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolXcI4d46EOCZq2KXWx2x2ewEkRnNPpYiaeib6ibJo5Rqbj1IicgMIKRuVjZ97icBSrYXB6IOeDnIa2sw9GdLncMPVT8FsPV4ia2icsLso/640?wx_fmt=png&from=appmsg)

在猜测目标端口和TxID这个方向上，不得不提到的就是钱志云和段海新老师团队在2020 ACM CCS 拿到唯一最佳论文奖的 *DNS Cache Poisoning Attack Reloaded: Revolutions with Side Channels* 这个研究成果，如果你看过钱志云老师2016年的off-path TCP exploits再来看这篇2020年的论文，就忍不住拍自己大腿说“我怎么不带着最强AI大模型回到过去然后让它把这些利用ICMP的思路组合起来”（当然你也可以驱使AI去证明Erdos的数学猜想）。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolWpRZKcfmNFDlpaXElMe6rxNrvicRH53RgxB8XkcFv5g1ibgH7QwWicPKWrNBJ2z6AuRcibueYrC8v4ex9HKuL3D4gDxX5j9OwXTes/640?wx_fmt=png&from=appmsg)

嗯，终于要回到今天我们介绍的这篇论文了，这篇论文的核心作者Amit Klein其实是一个资深的DNS安全研究人员，一直专注于这个方向（有多资深呢？后面会说）。今天这篇论文的核心是针对目前使用最广泛的DNS服务软件`BIND`里面用到的随机数发生器——Xoshiro128\*\* PRNG（别怀疑，那两个\*\*不是markdown排版忘记了，就是有这么两个星号）进行了相关攻击，接下来要进入的就是这篇论文最 ~~糗~~ 精彩的部分：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolUICNTfFqlOeFDaWJkibetzNr1icFyJGFiaSWObia8Glwm3KrvAkJ3G7bfPr3BvoDY65iczHru7oIgEAkolTXSCZtZQHSaALDy96tMY/640?wx_fmt=png&from=appmsg)

嗯，作者用了AI生图，水印也没去掉，而且截图还没截全……

不影响不影响，画图本来就是写论文的痛点，没几个人喜欢画图。回归到技术本身，作者发现`BIND`里面用到的Xoshiro128\*\* 这个伪随机数发生器虽然性能很好（boost库里面已经用到了，据说是CPU和内存消耗大幅低于C++11 STL自带的梅森旋转也就是MT19937算法，但是boost.ac.cn这个“伪”boost中文网上的这个翻译也很搞笑），而`BIND`却依赖它来对目标端口和TxID进行随机化，而且TxID信息会暴露出Xoshiro128\*\* 内部9个bit的信息；除了这9个bit的信息，作者还观察到另一条信息泄露的途径：一个叫做RRset order randomization的操作。这个操作是做什么用的呢？它是负责对DNS请求的回复信息中的多条记录（比如一个域名对应了多个A记录信息）进行随机化排序，然后返回给查询的重排序操作，但是这个操作能够暴露PRNG内部32个bit的信息，攻击者利用这些信息（9+32 bit）再用到一些简单的数学计算（高斯消元）就可以完整恢复Xoshiro128\*\* 内部128 bit的状态信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolUcwyEeNoZoJUqaclRSzLEyLlVBOTkOruV3baDzGRWdxStuqPH6OBkcyjeezXMXD9SCMYlQv2YZ1VMlqaMTpTicSicrHiaeNibk4z8/640?wx_fmt=png&from=appmsg)

数学这部分细节在论文中有详细记录，不过你可能会关心怎么去“诱骗”`BIND`，因为现实中的服务器可能并不会只给你一个人服务，会有非常多的请求同时处理，论文中的攻击如果中间插入了一些其他的查询请求（攻击者无法获得回复）就失效了。因此论文中提到了一些“奇技淫巧”，比如自己注册一个域名，里面放上足够多的记录（超过23条），然后自己查询这个，那`BIND`就一定会一次性处理这一批数据而不会被其他查询打断。这些技巧在论文中亦有详细记载，我们参考ChatGPT和Claude的最新安全围栏策略，不在这里公布细节了哈哈哈哈哈哈（偷懒的借口）！

顺便说一下，如果你关注Amit Klein这个人，会发现他真的是一个孤独的中东研究人员，这篇最新的USENIX Security论文的一作Omer Ben-Simhon你以为是他的学生？一查网络会发现其实是一个政治学专业的学生？？？？Amit Klein的另一篇论文（发表于2021年的IEEE S&P）*Cross Layer Attacks and How to Use Them (for DNS Cache Poisoning, Device Tracking and More)* 只有他自己作为作者，更神奇的是，你回去互联网的故纸堆里面一翻（其实就是20年前），发现在2007年的时候Amit Klein就已经研究过`BIND`的DNS投毒了…… 他真的是一个二十年如一日的研究人员吖……

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolWZu3EjLNe6Mq6LNw7sE9dQA1QTeXqbWwpBAoJpXpgnrmFkBqIMFO154Prcs1qntmNDbUnjGib5SZiahOC1iacKqHvUPYhtfRBK8g/640?wx_fmt=png&from=appmsg)

20年不算长也不算短，20年前Amit Klein在研究DNS投毒，而差不多同时期的另一位研究DNS投毒的安全研究人员Dan Kaminsky（https://blackhat.com/html/bh-usa-08/bh-usa-08-speakers.html#Kaminsky 2008年关于DNS投毒的Blackhat报告）却昔人已乘黄鹤去，永远停留在了2021年。仔细一想，人生能有多少个20年呢？不过正如大刘在《球状闪电》里面说的：

*“儿子，过一个美妙的人生并不难，听爸爸教你：你选一个公认的世界难题，最好是只用一张纸和一只铅笔的数学难题，比如歌德巴赫猜想或费尔马大定理什么的，或连纸笔都不要的纯自然哲学难题，比如宇宙的本源之类，投入全部身心钻研，只问耕耘不问收获，不知不觉的专注中，一辈子也就过去了。人们常说的寄托，也就是这么回事。或是相反，把挣钱作为惟一的目标，所有的时间都想着怎么挣，也不问挣来干什么用，到死的时候像葛朗台一样抱者一堆金币说：啊，真暖和啊……所以，美妙人生的关键在于你能迷上什么东西。”*

---

> 论文：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_ben-simhon.pdf

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