---
title: G.O.S.S.I.P 阅读推荐 2024-12-13 向Linux内核投毒（不是）
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499408&idx=1&sn=10212d4836dd50dee2d2d519f7fb645c&chksm=c063d049f714595f262ada384e0478362802d611effe4a7d07c3c941c2d9d1f95639262ed027&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-12-14
fetch_date: 2025-10-06T19:41:20.895970
---

# G.O.S.S.I.P 阅读推荐 2024-12-13 向Linux内核投毒（不是）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21H3MhL28ZX1tYc25L1NP3TC5icC6wXwPDOxRUzqcmADZ5tZyYb7YGp8ombibAXibBkZ1HMsHjmE4FlZA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-12-13 向Linux内核投毒（不是）

原创

G.O.S.S.I.P

安全研究GoSSIP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H3MhL28ZX1tYc25L1NP3TCMRRicQeWIyVe0xD9iaPMhsH7KhoKxY5yicSayiaBibGMeF2W612UQ03jajA/640?wx_fmt=png&from=appmsg)

过去20年，安全攻击者从来没有停止过往各种供应链投毒的企图，而Linux Kernel可能算得上是投毒者的“圣杯”，如果谁能往内核里面投毒成功，那简直可以在黑魔法的万神殿里面有自己的位置了。今天我们要介绍的这个演讲来自Linux Security Summit，演讲者可能是最有资格讨论往Linux内核投毒这个话题的，因为**他就是kernel.org的管理员Konstantin Ryabitsev**（以下简称KR），而他这个演讲的题目也就很直接：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H3MhL28ZX1tYc25L1NP3TCW82SOto1A7R9iceXIldJyrUzKYPUmDcpcdwL7HISkHsm4gqvWXAUvMw/640?wx_fmt=png&from=appmsg)

当然，作为管理员，KR的这个演讲肯定不是教你怎么干坏事，他只是在给大家介绍Linux Kernel的整个代码审核流程（pipeline），以及到底在哪些环节、有哪些人（比如Linus或者Greg）能够想办法投毒成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H3MhL28ZX1tYc25L1NP3TC52iaksE6ibN3MxIiaxemJrKSuPx9QS3LQtXtiaI7zkqaibicsNntiaxyk4Tibg/640?wx_fmt=png&from=appmsg)

作为可能是全世界对Linux Kernel代码审核流程最熟悉的几个人之一，KR娓娓道来，讨论了在各种环节可能的投毒方式以及目前社区的防御手段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H3MhL28ZX1tYc25L1NP3TCzxWG4UhvzOFPAVQdQb7MbSiaVoHOibeicDkliaKn3IfZib1tOXC6wOYVMkQ/640?wx_fmt=png&from=appmsg)

当然也不忘调侃下自己：“如果是我本人被收买了去投毒呢？” 自然也是行不通的，去贿赂一下maintainer大概可行，但是太贵~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H3MhL28ZX1tYc25L1NP3TC3pNQS7Zbb5JW8JKGvicdQdQLeOLdiaRUBm4VfYC7aSqeHjWDbwKDEncA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H3MhL28ZX1tYc25L1NP3TCzht0uP343vsNtzL0Y2H79sTaStoNanRkEkoGa6kpnBrwkIjn2VSWpw/640?wx_fmt=png&from=appmsg)

更重要的是，全世界又不是只有你一个人想干坏事，黑吃黑听说过吗，你放一个后门，其他想放后门的人就不会盯着？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H3MhL28ZX1tYc25L1NP3TCRjsfWr7jJ3WX821byhnyKdS73Zf4icOl0X6K7dPdyCrW24tD8enO3Aw/640?wx_fmt=png&from=appmsg)

最后，KR给了几个非常方便的投毒建议：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H3MhL28ZX1tYc25L1NP3TCZfAoQ0Hfjsyf2mMIsn6mUxWVjHvYALA8pawMw2A50b6p6k9fHBnWhw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21H3MhL28ZX1tYc25L1NP3TCxhiajLqwriaz4NckIibpeaRet2fZatkWYlC41yucbSicPvFNrVQxAp7Y6Q/640?wx_fmt=png&from=appmsg)

你学会了吗？

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