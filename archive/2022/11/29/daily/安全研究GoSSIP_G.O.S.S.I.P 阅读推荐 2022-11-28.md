---
title: G.O.S.S.I.P 阅读推荐 2022-11-28
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493411&idx=1&sn=ed92732823c9279642732c4f6b926be5&chksm=c063c9faf71440ec4508dfbd207a26d6cd1de438c6271fe6f9604885803cda72fa6071bea781&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-11-29
fetch_date: 2025-10-04T00:01:04.325631
---

# G.O.S.S.I.P 阅读推荐 2022-11-28

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GvQoz9PpiaXGEh9O3zc7b4brJcU272iaUKtr4AibSUaFkZBS22bOfWxSYOCCoZ514JDlmb4bT6iacEiag/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-11-28

原创

G.O.S.S.I.P

安全研究GoSSIP

猛然发现，00后已经成长起来，而著名的冠希老师艳照门事件已和我们相隔快15年了，我们经历了计算机数据保护技术的日益发展，同时也在忍受个人信息日渐被搜集和滥用。最近，一篇来自加拿大安大略省Guelph大学的研究人员发表的研究论文提醒我们，虽然修电脑（修手机）是我们日常活动之一，但要注意保护自己，有时候计算机维修也是一件非常危险的事情哦（冠希老师点赞）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GvQoz9PpiaXGEh9O3zc7b4biaN57cIp80IiaWdjWWqt4GqOO5G6wT5vVJPAvb0MaVFjPVUsibWEzgVTQ/640?wx_fmt=png)

在这篇名为*No Privacy in the Electronics Repair Industry*的研究论文中，研究人员开展了“钓鱼执法”：他们将笔记本电脑送到16家不同的电脑维修店更换电池，等拿回笔记本电脑后，通过恢复日志，检查数据访问情况。研究人员观察发现，电脑维修店经常欺负顾客不懂技术，要求顾客提供账户访问密码（你换个电池要密码做甚），然后悄悄访问顾客数据：有6家维修店的技术人员访问了个人数据，其中2家还将数据拷贝到个人设备上。作者甚至发现在其中3次维修服务中，技术人员删除了Windows快速访问和最近访问的文件。作者同时也关注了手机送修服务，发现情况也差不多，维修店很少会明确其服务是否包含了对消费者数据的保护。

进一步，作者开展了一个参与人数为112人的在线调研，了解大家对电脑维修的一些看法，其中30位被调研者还深度参与了后续的访谈。作者通过这样的一个user study，总结了普通用户的习惯和顾虑，同时也为电脑维修行业的监管提供了宝贵的参考（我们搞监管是否也能做到这样先深入调研再行动呢？）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GvQoz9PpiaXGEh9O3zc7b4b5kwAmtSjQ5HJrbpibhiadbuSo4KNxuA3LSBsbuUsNIwyzLdntmTiaZBTQ/640?wx_fmt=png)

具体到研究问题上，本文围绕下面的5个研究问题展开，虽然我们的读者大部分并不是做这种比较“软”的安全研究，但本文的这些思维模式和组织形式，也是对我们平时经常“硬马硬桥”的研究风格的一种有益补充。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GvQoz9PpiaXGEh9O3zc7b4bHw5djCL9L3qygI6Aa9oicRlb4icxhQBNTEnBnOWalU40d44AKdzDjdeQ/640?wx_fmt=png)

虽然这篇论文的调查是在加拿大展开的，但是全世界的维修服务可能都有相同之处——欺负不太懂技术的用户，比如下面的“霸王条款”：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GvQoz9PpiaXGEh9O3zc7b4bJ5icL17bfPeB92rYTCz2qibMibaAxwnwPvoMTzphYxjIZq8Axc1xZK2tg/640?wx_fmt=png)

事实上，全世界用户都经常需要维修计算机/手机（下图），这一点上苹果的设备在保护用户数据安全和隐私上还算不错（然而反过来，如果用作生产力设备，那你要考虑一下数据丢失的损失。。。）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GvQoz9PpiaXGEh9O3zc7b4bd3zt2IevibXibcwwBbhJlssbTpomzeUfHcOoic5Q8wTzys6S8q0b5Mibkg/640?wx_fmt=png)

作者也了解了广大用户存储的敏感数据的情况，除了工作内容，有一半的用户也会将自己的adult content存在电脑/手机上呢~~~ 陈老师你不孤独！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GvQoz9PpiaXGEh9O3zc7b4bibayicfuWuHAJBZia4EDeSXU3AMdtCtAibwBibWic3R0kvWvmTy9nIEYosUA/640?wx_fmt=png)

最后我们想说，研究只有有趣和无趣之分，很多同学非常着迷“硬核”技术，却忘记了自己的爸爸妈妈可能在你离家读书的时候，遇到手机或者电脑问题时往往只能就近求助于一些小店铺，这里面隐藏的安全风险是否也值得我们关注呢？本文被IEEE S&P 2023录用，可能正提醒我们，什么是安全研究人员的初心！

---

> 论文PDF：https://arxiv.org/pdf/2211.05824.pdf

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