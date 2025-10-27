---
title: G.O.S.S.I.P 阅读推荐 2023-02-01
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494007&idx=1&sn=c87f50b84c2cdec4bcffb9700e218c7d&chksm=c063c7aef7144eb883054659c7c4681ecd73c8adb3ba7bb6d838b9a613ec84521d9bc4844cdd&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-02-02
fetch_date: 2025-10-04T05:29:43.754277
---

# G.O.S.S.I.P 阅读推荐 2023-02-01

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21EfbRnUnXN9bXKQic8KQhWVUQOyunlicPyeF3UAPedMBDqy1jo87eEdUEVJZNw0hyITNurRnK2XmCkg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-02-01

原创

G.O.S.S.I.P

安全研究GoSSIP

2月的第一篇论文推荐，我们介绍来自USENIX Security 2023的论文*The Impostor Among US(B): Off-Path Injection Attacks on USB Communications*

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EfbRnUnXN9bXKQic8KQhWVU4Sp0bic8GjalNm4x0s7S94CpPwZicYNYoxDslMdQejNMSKE3fwibRIcpQ/640?wx_fmt=png)

开门见山，我们来看一下到底在2023年，这篇论文讨论的针对USB设备的Off-Path Injection Attack是什么？下图比较了已有的攻击和作者在本文中探讨的攻击的差别：在传统攻击模型（下图左边）中，攻击设备和被攻击的USB设备连接到同一个USB hub上，然后执行中间人攻击，可以监听和篡改流量（因为USB通信协议并没有考虑机密性和完整性保护）；而在本文的攻击模型（下图右边）中，攻击设备甚至不需要进行中间人攻击，就可以实施流量的控制，这是怎么做到的呢？

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EfbRnUnXN9bXKQic8KQhWVUyEuEGyYYksmKibDFMN2VsSGLDJdFjRKWSxW7biauPENEZHUX3z7JXQLg/640?wx_fmt=png)

实际上，本文的部分作者早在2017年的USENIX Security就已经发表了一篇名为*USB Snooping Made Easy: Crosstalk Leakage Attacks on USB Hubs*的论文，展示了连接在同一个USB hub上的不同设备之间存在的信息泄露问题：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EfbRnUnXN9bXKQic8KQhWVUNMiaCicHbXjMV8KORz3Mvg5Zl1SibNXHPdIgyzGQVJe0wUfJV8oF7nQ6A/640?wx_fmt=png)

到了2023年，这些研究人员再接再厉，继续深入挖掘USB通信的设计缺陷。他们发现，当计算机主机（host）查询连接的USB外设时，存在一个非常致命的问题，那就是外设的身份并没有什么严格的认证机制，也就是说，一个外设可以（在使用过程中）被其他外设冒充。看到这里，我们的读者是不是会马上联想起熟知的DNS投毒攻击？对，本文的攻击也是类似的方法（计算机安全的原理都是相通的），当主机去轮询（probe）USB外设时，恶意的USB设备可以抢先举手回答！一旦恶意设备先于被攻击的设备回复了消息，就可以将恶意的信息注入到通信过程中去，完成攻击~

和网络通信类似，USB设备（特别是多台设备）与系统主机的通信也有相关的握手协议和路由方式，对这方面不熟悉的读者可以阅读论文的第二章，非常好的USB工作原理快速入门！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EfbRnUnXN9bXKQic8KQhWVUO45BWXYlGWMOT3EAGlQrW7hvJBdIk0nF3TZMXUqP0mFFQ5nbZrapZQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EfbRnUnXN9bXKQic8KQhWVUmUHXiaJzr2PmdNtfUwia6FtkqA0iaF8P50AKaNz21CFGVfwSD2Axa1Tng/640?wx_fmt=png)

了解了原理之后，我们就可以进入到攻击阶段了。在攻击者视角下（作为一个恶意USB外设连接到USB hub上），系统主机对外设进行probe是一种广播方式，一旦系统广播了这种probe消息，攻击者就可以立即抢先回答。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EfbRnUnXN9bXKQic8KQhWVUtagS7ULic0Ecv0PJ7QQkhnSodegGPK6L427ahIA3urROI6LM32FAl4w/640?wx_fmt=png)

注意，在本文的攻击模型中，攻击者即使次次抢先举手，也不一定总是能快过原有的设备，如果需要对很多次通信过程进行攻击，那么必然会遇到攻击者设备和原始设备的回复在USB hub上“撞车”（collision）的情况（见下图），这时候USB hub的处理方式就完全是根据实现而定了。USB specification规定了两种不同的处理方式，有些hub会按照“先到先有效”的方式，丢弃掉后来的信息；而有些hub会检测消息的collision，然后给主机发送一个`garble`的错误信息。一般来说，如果hub采取了第一种处理方式，那么就很容易被本文提出的Off-Path Injection Attack攻击，而如果采取的是后一种方式，攻击者则只能进行拒绝服务攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EfbRnUnXN9bXKQic8KQhWVU4QkJzaI4EibYGKAia105tvLTEhmXtjqLSAP6zKYSKO58SzpEqqmz3uDg/640?wx_fmt=png)

在实验测试中，作者对29种不同的USB hub开展了安全调研，发现其中有14种存在安全问题（如下表所示）：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EfbRnUnXN9bXKQic8KQhWVU2rDyl4gqTQib2OVSUgFSzOw2IicYWniaDkVfqGk2f7YryV6fUHK6h0h1A/640?wx_fmt=png)

作者发现，在现实世界中，USB hub如果支持USB 3.0版本以上，那么被攻击的概率就大大减少（在测试中仅有1/13出现问题），而如果USB hub只支持到USB 2.0，很有可能就面临攻击（13/16的被测试设备存在安全问题）。当然，支持USB 3.0版本以上的USB hub仍然会被拒绝服务攻击影响。

作者针对USB键盘和U盘进行了安全评估，对键盘输入和文件传输都成功实施了注入攻击。这部分具体的实现细节，感兴趣的读者可以仔细阅读论文的第7章。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EfbRnUnXN9bXKQic8KQhWVUc5A28QJPUMLkgnRPsNk2iclmUFXMNiaUeQAPic8TkBodulvrLSaM7mZBQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EfbRnUnXN9bXKQic8KQhWVUwiae6GxfEg9KYHrIyRbHk3uUfaMj9UxOm8L3KUS92zZtzNLcSjibo8YQ/640?wx_fmt=png)

读完这篇论文，大家有什么感想吗？是不是赶紧把新年的压岁钱拿出来升级你的设备呢？（如果你已经到了要给晚辈发压岁钱的年纪，那就给他们多发一点，让他们采购的时候升级到USB 3.0吧）

---

> 论文：https://www.usenix.org/system/files/sec23summer\_9-dumitru-prepub.pdf

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