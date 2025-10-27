---
title: G.O.S.S.I.P 阅读推荐 2024-11-05 勿在浮沙筑高台
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499109&idx=1&sn=aa4fd7aa399bbd0b3e425e9929e19808&chksm=c063d3bcf7145aaa448750ba2acadce268e898376b37ba55ba2a0dae3307806a484a61f57887&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-11-06
fetch_date: 2025-10-06T19:19:18.014656
---

# G.O.S.S.I.P 阅读推荐 2024-11-05 勿在浮沙筑高台

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Gotv7LrrHf8Vj3yMJueickmE0fVAsciaoWebIXLcNOZ1YQRhkicmib1yqXFuaYMA1ianRQOYpoLF16GPQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-11-05 勿在浮沙筑高台

原创

G.O.S.S.I.P

安全研究GoSSIP

前几天，网络上披露了一个关于一家专门开发身份认证解决方案的公司——Okta的安全漏洞，这个漏洞非常幽默，起因是在某个地方的密钥生成的时候，密钥生成的材料是`userId + username + password`；而好巧不巧的是，这个时候使用的密钥生成算法（key derivation function，KDF）是知名但古老的bcrypt，它的特点之一是最多接受72个字符作为输入，其余的会被截断，那么如果username太长的话，就会把password给“挤出去”，也就是说，只需要用公开的userId和username就可以构造特定的key了……

上面的故事只是抛砖引玉，今天要介绍的文章其实是一篇“伪”密码安全攻击的文章：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Gotv7LrrHf8Vj3yMJueickmbFSAzGErvEbsVQ409EIEmdAp7KrW1rsnkYINpHCYMA5zzWUIcLxlRw/640?wx_fmt=png&from=appmsg)

乍一看这篇文章的标题，似乎介绍了一系列hash算法的破解，堪比王小云院士，但是生活在我们这个AI和自媒体每天都在生产大量信息垃圾（*啊，我们好像也是自媒体？*）的时代，看任何标题都要三思对不对？实际上标题里面提到的一系列算法（CityHash64、MurmurHash2/3、wyhash等）除了名字里面带了一个“hash”以外，和我们平常接触的hash算法可谓大相径庭。我们平时所说的hash算法，严格来说应该叫做“cryptographic hash function”，是满足了密码学上一些特殊的安全定义（比如要让攻击者难以找到两个不同输入得到相同的输出hash）的算法，大家熟知的MD5、SHA-1算法都属于此类（尽管它们在一定程度上已经不安全了）。而今天文章讨论的主角，却都不属于cryptographic hash function的范畴，而是用来实现某些编程开发需求（例如对字符串进行散列操作）的功能函数。

如果你搞不清楚上面的区别，而且不慎因为名字的原因（当然也可能不是你，而是AI向你推荐）误用了这些hash函数来实现一些高安全需求的功能，那么就丸辣！请看下面的例子：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Gotv7LrrHf8Vj3yMJueickmzTxI4rVv4NLyERvIGktb676qJNEs3h45RGbuN0Cqrl8qHrKk1QSGQg/640?wx_fmt=png&from=appmsg)

实际上，由于这些“普通”的hash函数的构造十分简单（例如下面这个murmurhash64a的例子），它们主要是为了快速处理一些“无恶意”的输入数据，因此要找到它们的碰撞是分分钟的事情。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Gotv7LrrHf8Vj3yMJueickmuU90PrucPdaPUab11E9bBhPibNBGbWA3MLcx2syxRg6GrKkuauPCTOQ/640?wx_fmt=png&from=appmsg)

至于怎么去攻击，这个技术细节也很简单，就留给我们的读者做课后练习好了~ 实际上，大家读完今天的文章，只需要记住不要在需要使用cryptographic hash function的时候错误地使用文章里面列出的这些hash函数就可以啦！

---

> 原文：https://orlp.net/blog/breaking-hash-functions/

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