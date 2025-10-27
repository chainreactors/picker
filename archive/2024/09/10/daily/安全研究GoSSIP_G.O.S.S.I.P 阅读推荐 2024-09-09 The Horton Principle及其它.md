---
title: G.O.S.S.I.P 阅读推荐 2024-09-09 The Horton Principle及其它
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498833&idx=1&sn=3dedd9069cdee01a42769f1db6ee34d9&chksm=c063d288f7145b9e2d4a3da6fad3778ff6b9787c47ea0d6ff9ab5dabe5cb113f50a188ca4bb3&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-09-10
fetch_date: 2025-10-06T18:28:26.739970
---

# G.O.S.S.I.P 阅读推荐 2024-09-09 The Horton Principle及其它

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FrUA5OIz14Ur0libVkyic1b2agYItrRq6ZItGEWZHA0cRaFo5ZNMkxWD6gn0UuOmwrE4Yg33a2LuoQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-09-09 The Horton Principle及其它

原创

G.O.S.S.I.P

安全研究GoSSIP

有一个安全原则，似乎没那么出名，但是又经常被提起，而且总是会有人犯错。这个安全原则你知道是什么吗？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FrUA5OIz14Ur0libVkyic1b22JtSHjRo0f56CzafCyMLNstAR9w9lFNmcT7ljic6LiacialBicHoljcbfg/640?wx_fmt=png&from=appmsg)

这个名字叫做 *The Horton Principle* 的原则，在《Cryptography Engineering》这本书的第六章出现，作者是这样描述的：

> *The Horton Principle: Authenticate what is meant, not what is said.*

似乎非常难理解，那就换一个解释：在一篇2011年的博客文章中，给它起了另一个名字叫做 *The Cryptographic Doom Principle*，是什么意思呢？

> https://moxie.org/2011/12/13/the-cryptographic-doom-principle.html
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FrUA5OIz14Ur0libVkyic1b2XLSCOpHVHBHxxFrXSjs1g4E0ATTaic1bKPibq5OriaJBsEldCRUhCpjKQ/640?wx_fmt=png&from=appmsg)

也就是说，对任何（来自不可信的源）的数据，必须要先检查它的完整性（通过消息验证码或者公钥签名验证），确认完整性没有问题之后再进行操作，否则就会出问题。再扩展一下可以这么说，不管是什么样的数据格式，我们在生成完整性的凭据时，永远要把这个数据对象的所有部分当作一个整体（数据流）来处理，而不是把MAC或者签名作为复杂的数据格式中的一个field~

如果不这么做会有什么后果呢？在上面的博客文章中提到了2002年著名的欧密论文，也就是把针对对称密码的padding oracle攻击搬到大家面前的第一篇文章（讲到这个，有兴趣的读者可以去网上搜索《SSL/TLS协议安全系列：SSL的Padding Oracle攻击》这个科普文章，然后你会发现这居然是本专栏的前身——GoSSIP\_SJTU的系列文章哈哈哈，只可惜发表在了“突然死亡”的乌云网站上）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FrUA5OIz14Ur0libVkyic1b2VOphgCW2d4dazdtekicKe7VUsDR0TlDa7bPAot71h2spiatmMsh67XrQ/640?wx_fmt=png&from=appmsg)

不过我们今天并不是要去潼关怀古，而是要介绍一篇最新的安全分析文章，这篇文章非常有意思，它既不是来自学术圈，也不是来自传统的大厂工程师或者研究员，而是一伙“数字罗宾汉”——由一群搞Windows（非法）激活的网友撰写的。这群网友的主要兴趣是搞一个叫做Microsoft Activation Scripts（MAS）的东东，你看ta们是不是很 正义 邪恶呢？不过搞技术的好处就是实事求是，这帮人在分析Windows的时候发现了一个惊天大瓜（漏洞），正开心得不行，本想藏着掖着，没想到过了不久这个瓜还被Cisco Talos Team发现并报告给了M$（CVE-2024-38184，然后就给修掉了），结果这个超级好用的漏洞就没了……于是一怒之下就有了今天要介绍的这篇文章：

> https://massgrave.dev/blog/keyhole （微信应该会提示你 该链接非法，微信已经禁止访问）![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FrUA5OIz14Ur0libVkyic1b2qBmTRb9klQFaXvdwfUV9pMibszibMlFabOTg9P6ibkgeQ0cAGqWRkfZbg/640?wx_fmt=png&from=appmsg)

在这篇名为Keyhole（钥匙孔）的文章中，作者讲述了他们在分析Client Licensing Platform（CLiP）这个Windows 10开始引入的、负责对Microsoft Store上的应用软件进行数字版权保护（DRM）的子系统的分析，这个子系统包含了用户态的一些exe、dll以及一个内核态的驱动（sys），看起来就是微软好的不去学，想把苹果那套糟粕学到手：CLiP子系统用来检查一个应用软件的可执行文件是否有合法的签名，如果没有就拒绝安装执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FrUA5OIz14Ur0libVkyic1b2RdQ85IjdNYPMGy8oNEclcUZqAcliaCHHNuia3lycmRvCvh06IU4QbLaA/640?wx_fmt=png&from=appmsg)

然而这个CLiP子系统可以说是漏洞百出，首先是它的主程序文件`clipup.exe`，里面居然包含了一个明文存放的ECDSA key，可以用来签发一个能够让相关的服务（`ClipSvc`）认可的签名，作者分析发现这个key是用来生成一个临时的签名，是开发者在生成可执行文件并上传给Microsoft Store之前进行签名用（然后Microsoft Store会返回一个有正式签名的可执行文件），可是在本地似乎这个签名也是能够通过`ClipSvc`的检查的，那么……

作者接下去对内核态的`ClipSp`这个驱动进行了逆向，同时对合法的数字签名的格式进行了分析（https://github.com/LukeFZ/CikExtractor 这里有细节），他们发现，这里有一个非常非常滑稽的问题——在一个合法的数字签名的文件中，数字签名总是放在被签名的数据段之后，可是如果你在这个后面再加上一个没有任何签名的数据段（只要自身格式是合法的），那么这个具有“空签名”的段就照样会被认可，更为严重的问题在于，如果这个段里面的特定编号和前面的某个带签名的段的编号一致，那么这个在加载过程中更后面加载的数据就会直接覆盖前面的数据。也就是说，攻击者只要找一个有合法签名的文件，往后面加入恶意构造的数据，根本不需要任何签名就可以绕过CLiP子系统的检查。

这个数据段有什么用呢，它实际上保存的是一个应用软件相关的license（你再也不需要手工输入序列号安装软件了），最搞笑的一点在于，由于Windows的license在Microsoft Store上也是可以买的，所以只需要构造一个License就可以激活Windows了………………

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FrUA5OIz14Ur0libVkyic1b2ISibJNomicxfP9TkPN9vWagxhQpQXy3TtXJswWibLrhVpCxOeEGA0YxvQ/640?wx_fmt=png&from=appmsg)

至于具体怎么去构造一个license，我们不能在这里传播非法技术，大家想要学就赶紧去原文里面看看吧！但是看了也没用，因为Cisco的Talos Team已经在今年4月8日（这一天是交大的校庆日哦）把这个问题报告给了微软，然后8月的安全更新就把这个问题给修掉了：

> https://talosintelligence.com/vulnerability\_reports/TALOS-2024-1964

当然，这个问题可不止是构造一个非法的license那么简单，如果你感兴趣，可以看看2年前的另一个相关研究，你会发现更多的黑料：

> https://github.com/KiFilterFiberContext/warbird-hook

打住打住，我们最后看看作者的另一个发现：作者表示写得这么垃圾的代码，我们要追究一下它到底是怎么生产出来的，结果追查一番之后发现，在另一个微软的产品——Xbox One里面，有一个安全处理器（Secure Processor，SP），也是用来进行DRM保护的；而在一些网上泄露的源码中，可以看到这个安全处理器进行license验证的一些实现细节，其中包含了和这个CLiP子系统一模一样的bug！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FrUA5OIz14Ur0libVkyic1b2StMuy1iaCxD2wdtH1toApLWIuTib07MhLd8cSpiaYTMwXJl3JZCHNticZQ/640?wx_fmt=png&from=appmsg)

也就是说，我们完全可以推测Xbox One和Windows用的DRM方案是互相抄来抄去的（微软你养了这么多人有什么用？）并且Xbox One已经被pwn了（https://github.com/exploits-forsale/collateral-damage 嘿嘿），那么是不是说我们可以继续去深入研究CLiP子系统的更多安全问题呢？

当然最后要给人家MAS打个广告：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FrUA5OIz14Ur0libVkyic1b2mnBJfgs8fsfdKtdvwTV0Hs91Vqyb8SmEbib9wN9ficT8mByW9WpmLFdg/640?wx_fmt=png&from=appmsg)

---

> 原文：https://massgrave.dev/blog/keyhole （微信应该会提示你 该链接非法，微信已经禁止访问）

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